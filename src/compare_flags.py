"""Compare review flags before and after a pipeline change, grouped by cause.

Causes are assigned by keyword rules on the flag text (first match wins, in CAUSES order). This is a
transparent, repeatable classification, not a judgement: a few flags may be assigned to the wrong cause
(on the 41 flags of the first all-county run, about 2 were), so every flag after the change is listed in
full under its assigned cause.

Usage: uv run python src/compare_flags.py outputs/briefs/summary_before.json outputs/briefs/summary.json
Writes outputs/briefs/flags_before_after.md
"""
import json
import re
import sys
from collections import Counter
from pathlib import Path

CAUSES = [
    ("Overlap caveat missing",
     lambda t: re.search(r"overlap", t, re.I) and re.search(r"caveat|missing|does not (note|say|mention)|without", t, re.I)),
    ("~20% clinical-diagnosis claim read as imaging",
     lambda t: re.search(r"(?<![\d.])20\s?%", t) and re.search(r"clinical|imaging", t, re.I)),
    ("No-record share read as recording completeness",
     lambda t: re.search(r"no[-_ ]treatment[-_ ]record", t, re.I)
     and re.search(r"complete|distinguishable|indistinguishable|signal|inference", t, re.I)),
    ("Stage vs age-adjustment wording",
     lambda t: re.search(r"stage", t, re.I) and re.search(r"age[- ]adjust|not age|age or stage|for age", t, re.I)),
    ("Plan attribution, dates or verb",
     lambda t: re.search(r"roadmap|filha|20(26|28|29|30|31)|\bplan|implement|carried out|\bcompleted\b|\bdue\b", t, re.I)),
]
OTHER = "Other"
ORDER = [c for c, _ in CAUSES] + [OTHER]


def cause(text: str) -> str:
    return next((name for name, rule in CAUSES if rule(text)), OTHER)


def flags(path: str) -> list[dict]:
    s = json.loads(Path(path).read_text(encoding="utf-8"))
    return [{"county": r["county"], **f, "cause": cause(f["problem"])} for r in s["counties"] for f in r["flags"]]


def main() -> int:
    if len(sys.argv) != 3:
        print(__doc__)
        return 2
    before, after = flags(sys.argv[1]), flags(sys.argv[2])
    sb = json.loads(Path(sys.argv[1]).read_text(encoding="utf-8"))
    sa = json.loads(Path(sys.argv[2]).read_text(encoding="utf-8"))

    def by(fl, key):
        return Counter(f[key] for f in fl)

    lines = ["# Review flags before and after the pipeline fixes", "",
             f"Before: {sb['finished_at']} · {sb['totals']}  ", f"After: {sa['finished_at']} · {sa['totals']}", "",
             "Causes are assigned by keyword rules on the flag text (`src/compare_flags.py`; first match wins). "
             "Flags are from the model review: for human review only, and not fully repeatable between runs.", "",
             "## By cause", "", "| Cause | Before | After | Change |", "|---|---|---|---|"]
    cb, ca = by(before, "cause"), by(after, "cause")
    for c in ORDER:
        lines.append(f"| {c} | {cb[c]} | {ca[c]} | {ca[c] - cb[c]:+d} |")
    lines.append(f"| **Total** | **{len(before)}** | **{len(after)}** | **{len(after) - len(before):+d}** |")
    lines += ["", "## By severity", "", "| Severity | Before | After |", "|---|---|---|"]
    sevb, seva = by(before, "severity"), by(after, "severity")
    for s in ("high", "medium", "low"):
        lines.append(f"| {s} | {sevb[s]} | {seva[s]} |")
    lines += ["", "## By county", "", "| County | Before | After | Status after | Attempts after |", "|---|---|---|---|---|"]
    after_rows = {r["county"]: r for r in sa["counties"]}
    for r in sb["counties"]:
        a = after_rows.get(r["county"], {})
        lines.append(f"| {r['county']} | {len(r['flags'])} | {len(a.get('flags', []))} | {a.get('status', '–')} | "
                     f"{a.get('attempts', '–')} |")
    lines += ["", "## All flags after the fixes", ""]
    for c in ORDER:
        fl = [f for f in after if f["cause"] == c]
        if fl:
            lines += [f"**{c}** ({len(fl)})", ""] + [
                f"- [{f['severity']}] {f['county']}, `{f['location']}`: {f['problem']}" for f in fl] + [""]
    out = Path(sys.argv[2]).parent / "flags_before_after.md"
    out.write_text("\n".join(lines) + "\n", encoding="utf-8")
    print("\n".join(lines[:4 + 6 + len(ORDER) + 2]))
    print(f"\nWrote {out}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
