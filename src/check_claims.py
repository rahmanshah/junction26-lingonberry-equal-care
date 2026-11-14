"""Check the claim ledger. Exits 1 if any check fails.

1. Every claim has claim_text, source_doc and location.
2. method and status are from the allowed lists (ledger.METHODS / ledger.STATUSES).
3. Every "quoted" or "mentor" claim has a quote.
4. Every quote is found, after normalising whitespace and hyphenation (src/sources.py), in its
   source_doc at EVERY location the ledger gives. This re-reads the source; it does not trust
   the loader.
5. Every claim with a value has a unit.

Prints claims per status and per method.
"""
import sqlite3
import sys
from collections import Counter
from pathlib import Path

import ledger
import sources


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
