"""Compare review flags across pipeline runs, grouped by cause.

Causes are assigned by keyword rules on the flag text (first match wins, in CAUSES order). This is a
transparent, repeatable classification, not a judgement: a few flags may be assigned to the wrong cause
(on the 41 flags of the first all-county run, about 2 were), so every flag of the last run is listed in
full under its assigned cause.

Usage: uv run python src/compare_flags.py LABEL=summary1.json LABEL=summary2.json [LABEL=summary3.json ...]
       (oldest first). Writes outputs/briefs/flags_before_after.md
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
OUT = Path("outputs/briefs/flags_before_after.md")


def cause(text: str) -> str:
    return next((name for name, rule in CAUSES if rule(text)), OTHER)


def load(path: str) -> tuple[dict, list[dict]]:
    s = json.loads(Path(path).read_text(encoding="utf-8"))
    fl = [{"county": r["county"], **f, "cause": cause(f["problem"])} for r in s["counties"] for f in r["flags"]]
    return s, fl


def main() -> int:
    args = sys.argv[1:]
    if len(args) < 2 or not all("=" in a for a in args):
        print(__doc__)
        return 2
    runs = [(label, *load(path)) for label, path in (a.split("=", 1) for a in args)]
    labels = [r[0] for r in runs]
    head = "| " + " | ".join(labels) + " |"
    sep = "|---" * len(labels) + "|"

    lines = ["# Review flags across pipeline runs", ""]
    for label, s, _ in runs:
        retries = sum(1 for r in s["counties"] if (r.get("attempts") or 0) > 1)
        lines.append(f"- **{label}**: {s['finished_at']} · {s['totals']} · {retries} needed the retry")
    lines += ["", "Causes are assigned by keyword rules on the flag text (`src/compare_flags.py`; first match "
              "wins). Flags come from the model review: for human review only, and not fully repeatable "
              "between runs.", "", "## By cause", "", "| Cause " + head + " Change |", "|---" + sep + "---|"]
    counts = [Counter(f["cause"] for f in fl) for _, _, fl in runs]
    for c in ORDER:
        lines.append(f"| {c} | " + " | ".join(str(k[c]) for k in counts) + f" | {counts[-1][c] - counts[0][c]:+d} |")
    totals = [len(fl) for _, _, fl in runs]
    lines.append("| **Total** | " + " | ".join(f"**{t}**" for t in totals) + f" | **{totals[-1] - totals[0]:+d}** |")
    lines += ["", "## By severity", "", "| Severity " + head, "|---" + sep]
    sev = [Counter(f["severity"] for f in fl) for _, _, fl in runs]
    for s in ("high", "medium", "low"):
        lines.append(f"| {s} | " + " | ".join(str(k[s]) for k in sev) + " |")
    lines += ["", "## By county (flags)", "", "| County " + head + " Status (last) | Attempts (last) |",
              "|---" + sep + "---|---|"]
    per = [{r["county"]: r for r in s["counties"]} for _, s, _ in runs]
    for county in per[-1]:
        last = per[-1][county]
        lines.append(f"| {county} | " + " | ".join(str(len(p.get(county, {}).get("flags", []))) for p in per)
                     + f" | {last['status']} | {last['attempts']} |")
    lines += ["", f"## All flags in the last run ({labels[-1]})", ""]
    last_flags = runs[-1][2]
    for c in ORDER:
        fl = [f for f in last_flags if f["cause"] == c]
        if fl:
            lines += [f"**{c}** ({len(fl)})", ""] + [
                f"- [{f['severity']}] {f['county']}, `{f['location']}`: {f['problem']}" for f in fl] + [""]
    OUT.write_text("\n".join(lines) + "\n", encoding="utf-8")
    print("\n".join(lines[: lines.index("## By severity")]))
    print(f"Wrote {OUT}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
