"""Generate, validate and review briefs for all 22 wellbeing services counties.

Runs src/brief.py's pipeline (brief -> validate + code rules -> one retry -> DRAFT if still failing ->
model review flags) for every county, a few in parallel. No county is skipped: a county whose run raises
an error is recorded with status ERROR and the error message.

Writes outputs/briefs/summary.json and outputs/briefs/summary.md and prints the summary.
Usage: uv run python src/generate_all.py [--workers 4] [County ...]
"""
import json
import sys
import time
import traceback
from collections import Counter
from concurrent.futures import ThreadPoolExecutor, as_completed
from datetime import datetime, timezone
from pathlib import Path

import counties
from brief import run

OUT = Path("outputs/briefs")


def one(short: str) -> dict:
    started = time.time()
    try:
        doc = run(short)
        rev = json.loads((OUT / f"{counties.slug(short)}.review.json").read_text(encoding="utf-8"))
        return {
            "county": short, "status": doc["status"], "attempts": doc["attempts"],
            "problems": doc["problems"], "rule_problems": rev["rule_problems"],
            "flags": rev["flags"], "flags_by_severity": dict(Counter(f["severity"] for f in rev["flags"])),
            "seconds": round(time.time() - started), "error": None,
        }
    except BaseException as e:  # noqa: BLE001 - record every failure, never skip a county
        return {"county": short, "status": "ERROR", "attempts": None, "problems": [], "rule_problems": [],
                "flags": [], "flags_by_severity": {}, "seconds": round(time.time() - started),
                "error": f"{type(e).__name__}: {e}", "traceback": traceback.format_exc(limit=3)}


def to_markdown(summary: dict) -> str:
    rows = summary["counties"]
    lines = ["# Brief generation: all counties", "",
             f"Run {summary['finished_at']} · {summary['totals']}", "",
             "| County | Status | Attempts | Remaining problems | Flags (high / medium / low) |",
             "|---|---|---|---|---|"]
    for r in rows:
        s = r["flags_by_severity"]
        lines.append(f"| {r['county']} | {r['status']} | {r['attempts'] or '–'} | "
                     f"{len(r['problems']) if r['status'] != 'ERROR' else r['error']} | "
                     f"{s.get('high', 0)} / {s.get('medium', 0)} / {s.get('low', 0)} |")
    for r in rows:
        if r["status"] == "DRAFT" or r["problems"]:
            lines += ["", f"## {r['county']}: why DRAFT", ""] + [f"- {p}" for p in r["problems"]]
    lines += ["", "## Review flags (for human review only)", ""]
    for r in rows:
        if r["flags"]:
            lines += [f"**{r['county']}**", ""] + [f"- [{f['severity']}] `{f['location']}`: {f['problem']}"
                                                   for f in r["flags"]] + [""]
    return "\n".join(lines) + "\n"


def main() -> int:
    args = sys.argv[1:]
    workers = 4
    if "--workers" in args:
        i = args.index("--workers")
        workers = int(args[i + 1])
        args = args[:i] + args[i + 2:]
    names = [counties.resolve(a)[0] for a in args] or list(counties.FULL)
    print(f"Generating {len(names)} briefs with {workers} workers…", flush=True)
    results = {}
    with ThreadPoolExecutor(max_workers=workers) as pool:
        futures = {pool.submit(one, n): n for n in names}
        for f in as_completed(futures):
            r = f.result()
            results[r["county"]] = r
            print(f"  {r['county']:<18} {r['status']:<9} attempts={r['attempts']} problems={len(r['problems'])} "
                  f"flags={r['flags_by_severity']} {r['seconds']}s" + (f" ERROR {r['error']}" if r["error"] else ""),
                  flush=True)
    assert set(results) == set(names), "a county went missing"
    # Merge with the previous summary so a partial re-run updates only the counties it ran.
    prev_path = OUT / "summary.json"
    prev = {r["county"]: r for r in json.loads(prev_path.read_text(encoding="utf-8"))["counties"]} \
        if prev_path.exists() else {}
    merged = {**prev, **results}
    rows = [merged.get(n) or {"county": n, "status": "NOT RUN", "attempts": None, "problems": [],
                              "rule_problems": [], "flags": [], "flags_by_severity": {}, "seconds": None,
                              "error": "not run yet"} for n in counties.FULL]
    totals = dict(Counter(r["status"] for r in rows))
    summary = {"finished_at": datetime.now(timezone.utc).isoformat(timespec="seconds"),
               "totals": totals, "counties": rows}
    OUT.mkdir(parents=True, exist_ok=True)
    prev_path.write_text(json.dumps(summary, ensure_ascii=False, indent=1), encoding="utf-8")
    (OUT / "summary.md").write_text(to_markdown(summary), encoding="utf-8")
    print(f"\nTotals (all 22 counties): {totals}")
    return 0 if not ({"ERROR", "NOT RUN"} & set(totals)) else 1


if __name__ == "__main__":
    sys.exit(main())
