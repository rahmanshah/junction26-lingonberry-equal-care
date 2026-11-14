"""Write outputs/verification_snapshot.json: the results of src/check_claims.py and src/validate_brief.py
as last run locally, for deployments that do not have data/raw/ (where check_claims.py cannot re-find
quotes in the source documents).

Records: time, git commit (and whether the working tree had uncommitted changes), the MD5 of
data/ledger.sqlite (so the app can tell whether the ledger changed since), the full check_claims.py
output, and a validate_brief.py result per county brief.

Run on a clean working tree, after committing, so the commit hash describes exactly what was verified;
then commit the snapshot itself. Refuses to run without the raw sources.
Usage: uv run python src/write_verification_snapshot.py
"""
import hashlib
import json
import os
import subprocess
import sys
from datetime import datetime, timezone
from pathlib import Path

import counties
import ledger
import sources
from validate_brief import load_claims, validate

OUT = Path("outputs/verification_snapshot.json")
BRIEFS = Path("outputs/briefs")


def git(*args: str) -> str:
    return subprocess.run(["git", *args], capture_output=True, text=True, check=True).stdout.strip()


def main() -> int:
    missing = [p for p in sources.SOURCES if p.startswith("data/raw/") and not Path(p).exists()]
    if missing:
        print("Cannot verify without the raw sources; missing:", ", ".join(missing))
        return 1
    dirty = bool(git("status", "--porcelain", "--", ".", ":!outputs/verification_snapshot.json"))
    if dirty:
        print("WARNING: uncommitted changes; the snapshot's commit hash will not describe them exactly.")

    check = subprocess.run([sys.executable, "src/check_claims.py"], capture_output=True, text=True,
                           encoding="utf-8", env={**os.environ, "PYTHONIOENCODING": "utf-8"})
    claims = load_claims()
    briefs = {}
    for short in counties.FULL:
        path = BRIEFS / f"{counties.slug(short)}.json"
        if not path.exists():
            briefs[short] = {"file": None, "valid": False, "problems": ["no saved brief"]}
            continue
        doc = json.loads(path.read_text(encoding="utf-8"))
        problems = validate(doc["brief"], set(doc.get("provided_claim_ids") or []) or None, claims)
        briefs[short] = {"file": str(path).replace("\\", "/"), "valid": not problems, "problems": problems,
                         "status_at_generation": doc["status"], "generated_at": doc["generated_at"]}

    snap = {
        "written_at": datetime.now(timezone.utc).isoformat(timespec="seconds"),
        "commit": git("rev-parse", "HEAD"), "commit_dirty": dirty,
        "ledger_md5": hashlib.md5(ledger.DB.read_bytes()).hexdigest(),
        "check_claims": {"exit_code": check.returncode, "passed": check.returncode == 0,
                         "output": (check.stdout + check.stderr).strip()},
        "validate_brief": briefs,
        "totals": {"briefs": len(briefs), "valid": sum(b["valid"] for b in briefs.values())},
    }
    OUT.parent.mkdir(parents=True, exist_ok=True)
    OUT.write_text(json.dumps(snap, ensure_ascii=False, indent=1), encoding="utf-8")
    print(f"Wrote {OUT}: check_claims {'passed' if snap['check_claims']['passed'] else 'FAILED'}, "
          f"{snap['totals']['valid']}/{snap['totals']['briefs']} briefs valid, commit {snap['commit'][:7]}"
          + (" (dirty)" if dirty else ""))
    return 0 if snap["check_claims"]["passed"] and snap["totals"]["valid"] == snap["totals"]["briefs"] else 1


if __name__ == "__main__":
    sys.exit(main())
