"""Check the claim ledger. Exits 1 if any check fails.

1. Every claim has claim_text, source_doc and location.
2. method and status are from the allowed lists (ledger.METHODS / ledger.STATUSES).
3. Every "quoted" or "mentor" claim has a quote.
4. Every quote is found, after normalising whitespace and hyphenation (src/sources.py), in its
   source_doc at EVERY location the ledger gives. This re-reads the source; it does not trust
   the loader.
5. Every claim with a value has a unit.
6. Every quote has an explicit language (quote_lang "fi" or "en"); unknown language fails.
7. English quotes are quotes of Hellu's brief and must belong to a brief claim (not a loose q: claim).
8. The scanned docs contain no unmarked straight "…" quotes: source quotes must be <q lang="…">.
9. Every superseded claim names, in its notes, existing claims that supersede it.

Prints claims per status and per method.
"""
import re
import sqlite3
import sys
from collections import Counter
from pathlib import Path

import ledger
import sources

SCANNED_DOCS = ("docs/source_verification.md", "docs/recommendations.md", "docs/blind_spots.md")
BRIEF = "docs/pathway_brief.md"


def unmarked_quotes(path: str) -> list[str]:
    """Lines with a straight double quote outside <q lang="…"> tags and `code` spans."""
    problems = []
    for i, line in enumerate(Path(path).read_text(encoding="utf-8").splitlines(), start=1):
        bare = re.sub(r'<q lang="[a-z]{2}">', "", line)
        bare = re.sub(r"`[^`]*`", "", bare)
        if '"' in bare:
            problems.append(f"{path}:{i}: unmarked straight quote (use <q lang=\"fi\"> or <q lang=\"en\">): "
                            f"{line.strip()[:100]}")
    return problems


def main() -> int:
    if not ledger.DB.exists():
        print(f"{ledger.DB} not found; run src/load_claims.py first")
        return 1
    con = sqlite3.connect(ledger.DB)
    con.row_factory = sqlite3.Row
    claims = [dict(r) for r in con.execute("SELECT * FROM claims ORDER BY id")]
    con.close()

    failures: list[str] = []

    def fail(c: dict, why: str) -> None:
        failures.append(f"{c['id']}: {why}")

    known = {c["id"] for c in claims}
    for doc in SCANNED_DOCS:
        failures.extend(unmarked_quotes(doc))

    for c in claims:
        if not (c["claim_text"] or "").strip():
            fail(c, "no claim_text")
        if not (c["source_doc"] or "").strip() or not (c["location"] or "").strip():
            fail(c, f"missing source_doc/location (source_doc={c['source_doc']!r}, location={c['location']!r})")
        if c["method"] not in ledger.METHODS:
            fail(c, f"unknown method {c['method']!r}")
        if c["status"] not in ledger.STATUSES:
            fail(c, f"unknown status {c['status']!r}")
        if c["value"] is not None and not c["unit"]:
            fail(c, "value without unit")
        if c["method"] in ("quoted", "mentor") and not (c["quote"] or "").strip():
            fail(c, f"method {c['method']} but no quote")
        src = c["source_doc"] or ""
        if src.startswith(("data/", "docs/")) and not Path(src).exists():
            fail(c, f"source_doc not found: {src}")

        if c["quote"] and c["quote_lang"] not in ledger.QUOTE_LANGS:
            fail(c, f"quote language unknown ({c['quote_lang']!r}); mark it <q lang=\"fi\"> or <q lang=\"en\">: "
                    f"{c['quote'][:80]!r}")
        if c["quote_lang"] == "en" and (src != BRIEF or c["id"].startswith("q:")):
            fail(c, f"English quote not attached to a claim in BRIEF_CLAIMS (src/load_claims.py): {c['quote'][:80]!r}")
        if c["status"] == "superseded":
            ids = re.findall(r"\bq:[0-9a-f]{10}\b", c["notes"] or "")
            if not ids or not all(i in known for i in ids):
                fail(c, "superseded claim must name existing superseding claims (q:… ids) in notes")

        if c["quote"] and c["location"]:
            if src not in sources.SOURCES:
                fail(c, f"quote but source_doc {src!r} is not a checkable local source")
                continue
            found = set(sources.find(src, c["quote"]))
            for loc in (l.strip() for l in c["location"].split(";")):
                if loc not in found:
                    where = ", ".join(sorted(found)) if found else "nowhere"
                    fail(c, f"quote not found at {loc!r} in {src} (found: {where}): {c['quote'][:80]!r}")

    n_quotes = sum(1 for c in claims if c["quote"])
    print(f"Checked {len(claims)} claims ({n_quotes} with quotes re-verified against their sources)")
    for field in ("status", "method"):
        print(f"\nClaims per {field}:")
        for k, n in Counter(c[field] for c in claims).most_common():
            print(f"  {k:<18} {n}")

    if failures:
        print(f"\nFAILED: {len(failures)} problem(s)")
        for f in failures:
            print("  " + f)
        return 1
    print("\nAll checks passed.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
