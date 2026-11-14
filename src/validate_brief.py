"""Validate a county brief against the claim ledger.

A brief has three sections (where_we_lag, how_sure_are_we, what_to_do_first); each is
{headline: sentence, details: [sentence, ...]} and a sentence is {text, claim_ids}. Problems reported:
  - a section has no headline or no details; a headline is longer than HEADLINE_MAX_WORDS
  - a sentence has no claim ID
  - a claim ID does not exist in data/ledger.sqlite
  - a claim ID has a status a brief may not cite (draft, superseded)
  - a claim ID was not among the claims given to the model for this county
  - a number in the sentence matches no number in its cited claims (value, claim text, notes,
    quote, translation, location), allowing rounding to the precision printed in the sentence
  - a sentence citing a preliminary claim does not say "preliminary", or one citing a mentor
    insight does not say "mentor"
  - a sentence citing a county share (cty: claim, crude) does not say so: "crude", "unadjusted",
    "not adjusted" (or Finnish "vakioimaton")
  - a sentence citing one of our recommendations (status "recommendation (ours)") does not say it is
    a recommendation ("recommend…")
  - a sentence citing two or more different county treatment shares does not say they overlap
  - a sentence says treatment recording looks (relatively) complete although the county's
    no-treatment-record 95% interval is not entirely below the national value (vs_national != below)
  - a sentence citing roadmap measure 3.1.2 or 2.5.2 mentions 2026–2028 without saying the milestone
    covers five cancers ("five" / "5")
  - a sentence citing roadmap measure 3.2.1 puts a date next to the 90% coverage indicator (it has none)

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
HEADLINE_MAX_WORDS = 35


def iter_sentences(brief: dict):
    """(location, sentence) for every sentence: each section's headline, then its details."""
    for section in SECTIONS:
        sec = brief.get(section) or {}
        if sec.get("headline"):
            yield f"{section}.headline", sec["headline"]
        for i, s in enumerate(sec.get("details") or []):
            yield f"{section}.details[{i}]", s
# Study period 2019–2023, 95% confidence level, 12-month follow-up window.
FRAME_NUMBERS = {2019.0, 2023.0, 95.0, 12.0}
CRUDE = re.compile(r"\bcrude\b|\bunadjusted\b|\bnot adjusted\b|vakioimato", re.I)
OVERLAP = re.compile(r"\boverlap", re.I)
YEARS_2026_2028 = re.compile(r"2026\s*[–-]\s*2028")
FIVE = re.compile(r"\bfive\b|\b5\b", re.I)
DATED_90 = re.compile(r"90\s?%[^.;]{0,60}\b20(26|28|29|31)\b|\b20(26|28|29|31)\b[^.;]{0,60}90\s?%")
_Q = r"(?:relatively |fairly |largely |reasonably |more |mostly )"
COMPLETE_RECORDING = re.compile(
    rf"{_Q}complete\w*[^.;]{{0,30}}\brecord|\brecord\w*[^.;]{{0,30}}\b(?:looks|appears|is|seems|being) {_Q}?complete\b"
    rf"|consistent with {_Q}?complete", re.I)
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
        sec = brief.get(section) or {}
        if not sec.get("headline"):
            problems.append(f"{section}: no headline")
        elif len(sec["headline"].get("text", "").split()) > HEADLINE_MAX_WORDS:
            problems.append(f"{section}.headline: longer than {HEADLINE_MAX_WORDS} words")
        if not sec.get("details"):
            problems.append(f"{section}: no detail sentences")
    for where, s in iter_sentences(brief):
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
        if any(c["id"].startswith("cty:") for c in cited) and not CRUDE.search(text):
            problems.append(f"{where}: cites a crude county share but does not say 'crude': {text!r}")
        if ledger.RECOMMENDATION in statuses and "recommend" not in text.lower():
            problems.append(f"{where}: cites our recommendation but does not say it is a recommendation: {text!r}")
        cty_metrics = {c["metric"] for c in cited if c["id"].startswith("cty:")}
        if len(cty_metrics) >= 2 and not OVERLAP.search(text):
            problems.append(f"{where}: cites {len(cty_metrics)} county treatment shares but does not say the "
                            f"categories overlap: {text!r}")
        if COMPLETE_RECORDING.search(text):
            pool_ids = (allowed_ids or set()) | set(ids)
            nr = [claims[i] for i in pool_ids if i.startswith("cty:no_treatment_record:") and i in claims]
            vs = re.search(r"vs_national=([^;]+)", nr[0]["notes"]).group(1).strip() if nr else "unknown"
            if vs != "below":
                problems.append(f"{where}: says recording looks complete, but the county's no-treatment-record "
                                f"95% interval is not entirely below national (vs_national={vs}): {text!r}")
        notes = " ".join(c.get("notes") or "" for c in cited)
        if re.search(r"measure (3\.1\.2|2\.5\.2)", notes) and YEARS_2026_2028.search(text) and not FIVE.search(text):
            problems.append(f"{where}: mentions 2026–2028 for roadmap measure 3.1.2/2.5.2 without saying the "
                            f"milestone covers five cancers: {text!r}")
        if "measure 3.2.1" in notes and DATED_90.search(text):
            problems.append(f"{where}: puts a date next to the 90% coverage indicator, which has no date "
                            f"(roadmap 3.2.1): {text!r}")
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
