"""Review a county brief in two layers.

(a) rule_problems(): code rules. These are hard problems, treated like validation failures
    (src/brief.py feeds them into the retry; if they remain, the brief is saved as DRAFT):
      - overclaiming words: certain, proves, guarantees, definitely, will be implemented, ...
      - future tense about planned measures: "will" / "going to" in a sentence that cites the national
        strategy, the roadmap or the Filha programme. Plans must be described as plans.
      - occupational health described as "excluded": the report does not mention it at all; say
        "not included in the report's data".
(b) model_flags(): MODEL_EXTRACT reads each sentence with its cited claims and returns flags
    {location, sentence, problem, severity}. Flags are for HUMAN REVIEW ONLY: they never change the
    brief's status and never approve anything.

Flags are saved next to the brief: outputs/briefs/<county>.review.json.
Usage (re-review a saved brief): uv run python src/review_brief.py outputs/briefs/<county>.json
"""
import json
import re
import sys
from datetime import datetime, timezone
from pathlib import Path
from typing import Literal

from pydantic import BaseModel

import gemini
from validate_brief import iter_sentences, load_claims

OVERCLAIM = re.compile(r"\b(certain(ly)?|proves?|proven|guarantees?|guaranteed|definitely|undoubtedly|"
                       r"will be implemented)\b", re.I)
FUTURE = re.compile(r"\b(will|shall|going to)\b|\w'll\b", re.I)
PLAN_SOURCES = ("strategy_2026_2035_fi.pdf", "roadmap_2026_2031_fi.pdf", "filha_lung_programme_2026_fi.pdf")
NOTE = "Flags are for human review only; they never change the brief's status or approve it."
# As repeatable as the API allows: greedy decoding and a fixed seed. Recorded in every review file.
REVIEW_SETTINGS = {"temperature": 0.0, "seed": 20261114}
SOURCE_NAMES = {
    "keuhkosyoparaportti_2019_2023.html": "Finnish Cancer Registry report Keuhkosyöpä Suomessa 2019–2023",
    "strategy_2026_2035_fi.pdf": "National Cancer Strategy 2026–2035 (STM)",
    "roadmap_2026_2031_fi.pdf": "Cancer strategy implementation roadmap 2026–2031 (STM)",
    "filha_lung_programme_2026_fi.pdf": "Filha National Lung Cancer Programme 2026–2035",
    "pathway_brief.md": "teammate Hellu's background brief",
}


def rule_problems(brief: dict, claims: dict[str, dict] | None = None) -> list[str]:
    claims = claims if claims is not None else load_claims()
    problems = []
    for where, s in iter_sentences(brief):
        text = s.get("text", "")
        for m in OVERCLAIM.finditer(text):
            problems.append(f"{where}: overclaiming word {m.group(0)!r}: {text!r}")
        cites_plan = any((claims.get(cid) or {}).get("source_doc", "").endswith(PLAN_SOURCES)
                         for cid in s.get("claim_ids") or [])
        if cites_plan:
            for m in FUTURE.finditer(text):
                problems.append(f"{where}: future tense ({m.group(0)!r}) about a planned measure; describe "
                                f"the plan as a plan (e.g. 'the roadmap plans … by 2026–2028'): {text!r}")
        if re.search(r"occupational", text, re.I) and re.search(r"\bexclud", text, re.I):
            problems.append(f"{where}: says occupational health is excluded; the report does not mention it "
                            f"(say 'not included in the report's data'): {text!r}")
    return problems


class Flag(BaseModel):
    location: str
    sentence: str
    problem: str
    severity: Literal["low", "medium", "high"]


class Review(BaseModel):
    flags: list[Flag]


SYSTEM = """You are a careful fact-checker. For each sentence of a county health brief you get the \
claims it cites (ID, status, text, notes, and for quotes the original and an English translation). \
Flag a sentence ONLY if it is not fully supported by its cited claims. Look for:
- overreach: saying more than the claims say (stronger wording, causes, trends, certainty);
- scope: using a claim outside the scope stated in its notes ("scope: …"), e.g. a diagnosis-concordance \
claim used about treatment recording, or a regional finding presented as true for this county;
- wrong numbers, directions or comparisons, or a number attached to the wrong measure;
- plans described as done, certain, or in the future tense (e.g. "will be implemented"), or with the \
wrong verb (a recommendation "completed" is not "implemented");
- missing caveats that the claims require (crude shares, overlapping categories, digitised values, \
preliminary figures, mentor insight);
- sources misdescribed (e.g. a law or a journal article called a regional document).
Severity: high = factually wrong or misleading; medium = overreach or missing caveat; low = minor \
imprecision. Do not flag style. Do not flag supported sentences. Return an empty list if all are fine."""


def model_flags(brief: dict, claims: dict[str, dict], tag: str) -> tuple[list[dict], str, str]:
    """Returns (flags, model, raw file)."""
    blocks = []
    for where, s in iter_sentences(brief):
        cited = []
        for cid in s.get("claim_ids") or []:
            c = claims.get(cid) or {}
            src = SOURCE_NAMES.get((c.get("source_doc") or "").split("/")[-1], c.get("source_doc"))
            line = (f"  [{cid}] status={c.get('status')} | source: {src}, {c.get('location')} | "
                    f"{c.get('claim_text')}")
            if c.get("notes"):
                line += f" | notes: {c['notes']}"
            if c.get("quote"):
                line += f" | quote ({c.get('quote_lang')}): {c['quote']}"
                if c.get("quote_en"):
                    line += f" | translation: {c['quote_en']}"
            cited.append(line)
        blocks.append(f"### {where}\nSentence: {s.get('text')}\nCited claims:\n" + "\n".join(cited))
    model = gemini.model_name("MODEL_EXTRACT")
    parsed, _, raw = gemini.structured_call(model, SYSTEM, "\n\n".join(blocks), Review, tag, **REVIEW_SETTINGS)
    flags = [f.model_dump() for f in parsed.flags] if parsed else [
        {"location": "-", "sentence": "-", "problem": "review model returned no valid JSON", "severity": "high"}]
    return flags, model, str(raw).replace("\\", "/")


def review(doc: dict, slug: str, out_dir: Path, claims: dict[str, dict] | None = None) -> dict:
    """Run both layers on a saved brief document and write <slug>.review.json next to it."""
    claims = claims if claims is not None else load_claims()
    brief = doc.get("brief") or {}
    flags, model, raw = model_flags(brief, claims, f"review_{slug}") if brief else ([], None, None)
    result = {
        "county": doc.get("county"), "brief_generated_at": doc.get("generated_at"),
        "reviewed_at": datetime.now(timezone.utc).isoformat(timespec="seconds"), "note": NOTE,
        "rule_problems": rule_problems(brief, claims), "model": model,
        "settings": {**REVIEW_SETTINGS, "thinking_level": "model default"}, "raw_response": raw, "flags": flags,
    }
    (out_dir / f"{slug}.review.json").write_text(json.dumps(result, ensure_ascii=False, indent=1), encoding="utf-8")
    return result


def main() -> int:
    if len(sys.argv) != 2:
        print(__doc__)
        return 2
    path = Path(sys.argv[1])
    doc = json.loads(path.read_text(encoding="utf-8"))
    result = review(doc, path.stem, path.parent)
    from brief import to_markdown  # local import: brief.py imports this module
    doc["review"] = {"file": str(path.parent / f"{path.stem}.review.json").replace("\\", "/"),
                     "flags": len(result["flags"]), "note": NOTE}
    path.write_text(json.dumps(doc, ensure_ascii=False, indent=1), encoding="utf-8")
    path.with_suffix(".md").write_text(to_markdown(doc, result), encoding="utf-8")
    print(f"{len(result['rule_problems'])} rule problem(s), {len(result['flags'])} flag(s) -> "
          f"{path.parent / (path.stem + '.review.json')}")
    for p in result["rule_problems"]:
        print("RULE:", p)
    for f in result["flags"]:
        print(f"FLAG [{f['severity']}] {f['location']}: {f['problem']}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
