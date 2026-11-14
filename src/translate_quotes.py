"""Translate every Finnish quote in the ledger to English with MODEL_EXTRACT.

Translations are stored in data/processed/quote_translations.csv (quote_key, quote, quote_en, model,
translated_at), keyed by the quote text, so they survive ledger rebuilds; src/load_claims.py copies
them into the ledger's quote_en column. The Finnish quote is never replaced.

Only quotes without a translation are sent (use --all to redo every quote). Checks: every quote gets
exactly one translation, and every number in the quote appears in its translation.
Raw responses: data/processed/gemini_raw/.

Usage: uv run python src/translate_quotes.py [--all]
"""
import re
import sqlite3
import sys
from datetime import datetime, timezone

import pandas as pd
from pydantic import BaseModel

import gemini
import ledger
from load_claims import TRANSLATIONS, quote_key
from load_claims import main as reload_ledger

SYSTEM = """You translate short Finnish quotes from Finnish health-policy documents (national cancer \
strategy, implementation roadmap, national lung cancer programme, Cancer Registry report) into English.
Translate faithfully and literally enough to be checked against the original: keep every number, \
date, percentage, section or table reference and abbreviation exactly; do not add, explain or omit \
anything. If a quote is a fragment, translate it as a fragment. Return one translation per key."""


class Item(BaseModel):
    key: str
    translation: str


class Translations(BaseModel):
    items: list[Item]


def digits(text: str) -> list[str]:
    return sorted(re.findall(r"\d+", text))


def main() -> int:
    redo = "--all" in sys.argv
    con = sqlite3.connect(ledger.DB)
    quotes = {quote_key(q): q for (q,) in con.execute(
        "SELECT DISTINCT quote FROM claims WHERE quote_lang = 'fi' AND quote IS NOT NULL")}
    con.close()
    old = pd.read_csv(TRANSLATIONS, dtype=str).fillna("") if TRANSLATIONS.exists() else \
        pd.DataFrame(columns=["quote_key", "quote", "quote_en", "model", "translated_at"])
    done = set() if redo else set(old.loc[old["quote_en"] != "", "quote_key"])
    todo = {k: q for k, q in quotes.items() if k not in done}
    print(f"{len(quotes)} Finnish quotes; {len(todo)} to translate")
    if not todo:
        return 0

    model = gemini.model_name("MODEL_EXTRACT")
    prompt = "Translate each quote. Return items with the same keys.\n\n" + "\n".join(
        f"[{k}] {q}" for k, q in todo.items())
    parsed, _, raw = gemini.structured_call(model, SYSTEM, prompt, Translations, "translate_quotes")
    if parsed is None:
        print(f"No valid structured response; raw saved to {raw}")
        return 1
    got = {i.key.strip("[] "): i.translation.strip() for i in parsed.items}

    problems = [f"missing translation for {k}" for k in todo if not got.get(k)]
    problems += [f"unexpected key {k}" for k in got if k not in todo]
    for k, q in todo.items():
        if got.get(k) and not set(digits(q)) <= set(digits(got[k])):
            problems.append(f"{k}: numbers {digits(q)} not all kept in {got[k]!r}")
    now = datetime.now(timezone.utc).isoformat(timespec="seconds")
    new = pd.DataFrame([{"quote_key": k, "quote": q, "quote_en": got.get(k, ""), "model": model,
                         "translated_at": now} for k, q in todo.items() if got.get(k)])
    keep = old[~old["quote_key"].isin(new["quote_key"])] if len(new) else old
    out = pd.concat([keep, new], ignore_index=True).sort_values("quote_key")
    TRANSLATIONS.parent.mkdir(parents=True, exist_ok=True)
    out.to_csv(TRANSLATIONS, index=False, encoding="utf-8")
    print(f"Saved {len(new)} translations to {TRANSLATIONS} (raw: {raw})")
    for p in problems:
        print("PROBLEM:", p)

    reload_ledger()  # copy translations into the ledger's quote_en column
    return 1 if problems else 0


if __name__ == "__main__":
    sys.exit(main())
