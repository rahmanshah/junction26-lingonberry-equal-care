"""Validate a county brief against the claim ledger.

A brief has three sections (where_we_lag, how_sure_are_we, what_to_do_first); each is a list of
sentences {text, claim_ids}. Problems reported:
  - a section is empty, or a sentence has no claim ID
  - a claim ID does not exist in data/ledger.sqlite
  - a claim ID has a status a brief may not cite (draft, superseded)
  - a claim ID was not among the claims given to the model for this county
  - a number in the sentence matches no number in its cited claims (value, claim text, notes,
    quote, translation, location), allowing rounding to the precision printed in the sentence
  - a sentence citing a preliminary claim does not say "preliminary", or one citing a mentor
    insight does not say "mentor"

Numbers that describe the study frame, not a finding, are always allowed: FRAME_NUMBERS.

Usage: uv run python src/validate_brief.py outputs/briefs/<county>.json   (exit 1 on problems)
"""
import json
import re
import sqlite3
import sys
from pathlib import Path

import ledger

SECTIONS = ("where_we_lag", "how_sure_are_we", "what_to_do_first")
# Study period 2019–2023, 95% confidence level, 12-month follow-up window.
FRAME_NUMBERS = {2019.0, 2023.0, 95.0, 12.0}
NUM = re.compile(r"(?<![\w.,])(\d{1,3}(?:,\d{3})+(?![\d])|\d+(?:[.,]\d+)?)(?!\w)")


def numbers(text: str) -> list[tuple[float, int]]:
    """(value, decimals printed) for every number in a text. 14,873 is a thousands separator;
    9,7 is a Finnish decimal."""
    out = []
    for m in NUM.finditer(text or ""):
        s = m.group(1)
        if re.fullmatch(r"\d{1,3}(?:,\d{3})+", s):
            out.append((float(s.replace(",", "")), 0))
        else:
            s = s.replace(",", ".")
            out.append((float(s), len(s.split(".")[1]) if "." in s else 0))
    return out


def claim_numbers(c: dict) -> set[float]:
    vals = {float(c["value"])} if c.get("value") is not None else set()
    for field in ("claim_text", "notes", "quote", "quote_en", "location"):
        vals.update(v for v, _ in numbers(c.get(field) or ""))
    return vals


def matches(x: float, decimals: int, candidates: set[float]) -> bool:
    tol = 0.5 * 10 ** -decimals + 1e-9
    return any(abs(round(c, decimals) - x) < 1e-9 or abs(c - x) <= tol for c in candidates)


def load_claims() -> dict[str, dict]:
    con = sqlite3.connect(ledger.DB)
    con.row_factory = sqlite3.Row
    out = {r["id"]: dict(r) for r in con.execute("SELECT * FROM claims")}
    con.close()
    return out


def validate(brief: dict, allowed_ids: set[str] | None = None, claims: dict[str, dict] | None = None) -> list[str]:
    claims = claims if claims is not None else load_claims()
    problems = []
    for section in SECTIONS:
        sentences = brief.get(section) or []
        if not sentences:
            problems.append(f"{section}: section is empty")
        for i, s in enumerate(sentences):
            where = f"{section}[{i}]"
            text, ids = s.get("text", ""), s.get("claim_ids") or []
            if not ids:
                problems.append(f"{where}: no claim ID: {text!r}")
                continue
            cited = []
            for cid in ids:
                c = claims.get(cid)
                if c is None:
                    problems.append(f"{where}: claim ID {cid!r} does not exist")
                elif c["status"] not in ledger.CITABLE:
                    problems.append(f"{where}: claim {cid!r} has status {c['status']!r}, which may not be cited")
                elif allowed_ids is not None and cid not in allowed_ids:
                    problems.append(f"{where}: claim {cid!r} was not provided for this county")
                else:
                    cited.append(c)
            if not cited:
                continue
            pool = set().union(*(claim_numbers(c) for c in cited))
            for x, d in numbers(text):
                if x in FRAME_NUMBERS or matches(x, d, pool):
                    continue
                problems.append(f"{where}: number {x:g} is not in its cited claims {ids}: {text!r}")
            statuses = {c["status"] for c in cited}
            if "preliminary" in statuses and "preliminary" not in text.lower():
                problems.append(f"{where}: cites a preliminary claim but does not say 'preliminary': {text!r}")
            if "mentor insight" in statuses and "mentor" not in text.lower():
                problems.append(f"{where}: cites a mentor insight but does not say 'mentor': {text!r}")
    return problems


def main() -> int:
    if len(sys.argv) != 2:
        print(__doc__)
        return 2
    doc = json.loads(Path(sys.argv[1]).read_text(encoding="utf-8"))
    allowed = set(doc.get("provided_claim_ids") or []) or None
    problems = validate(doc["brief"], allowed)
    for p in problems:
        print(p)
    print("OK" if not problems else f"{len(problems)} problem(s)")
    return 1 if problems else 0


if __name__ == "__main__":
    sys.exit(main())
