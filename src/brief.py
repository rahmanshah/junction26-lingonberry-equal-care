"""Generate a county brief with Gemini, grounded only in the claim ledger.

For a county, the model gets:
  - the county's claims (shares with CIs, age-adjusted Kuva 16 values)
  - the national claims
  - the evidence behind the recommendations (blind spots, verified policy quotes, Hellu's brief:
    MOT delays, regional pathways, law, mentor insights)
  - the three draft recommendations from docs/recommendations.md, as context
Only claims with a citable status are given (verified locally / verified by Hellu / preliminary /
mentor insight); draft and superseded claims never reach the model.

The model (MODEL_REASON, thinking level HIGH) returns three sections of sentences, each sentence with
the claim IDs it relies on. src/validate_brief.py checks it. On problems the model gets one retry
with the problem list; if it still fails, the brief is saved with status DRAFT.

Raw responses: data/processed/gemini_raw/. Brief: outputs/briefs/<county>.json (+ .md for reading).

Usage: uv run python src/brief.py Kymenlaakso "Varsinais-Suomi"
"""
import json
import re
import sqlite3
import sys
from datetime import datetime, timezone
from pathlib import Path

from pydantic import BaseModel, Field

import counties
import gemini
import ledger
from review_brief import review, rule_problems
from validate_brief import SECTIONS, iter_sentences, validate

OUT = Path("outputs/briefs")
THINKING = "HIGH"


class Sentence(BaseModel):
    text: str = Field(description="One plain-English sentence.")
    claim_ids: list[str] = Field(description="IDs of the claims this sentence relies on (at least one).")


class Section(BaseModel):
    headline: Sentence = Field(description="The main point in one sentence (at most 30 words), with claim IDs.")
    details: list[Sentence] = Field(description="2–4 supporting sentences, each with claim IDs.")


class Brief(BaseModel):
    where_we_lag: Section
    how_sure_are_we: Section
    what_to_do_first: Section


SYSTEM = """You write a short evidence brief on the lung cancer care pathway for one Finnish wellbeing \
services county, for the county's health managers. You may use ONLY the claims provided. Each claim has \
an ID, a status and a text.

Rules:
1. Every sentence must list the IDs of the claims it relies on in claim_ids (at least one). Use IDs \
exactly as given. Do not cite anything that is not in the list.
2. Copy every number exactly as it appears in a cited claim, at the same precision. Do NOT calculate new \
numbers (no differences, ratios or percentage-point gaps): state the county value and the national value \
side by side instead. Spell out no numbers in words.
3. State uncertainty. Give 95% confidence intervals where the claim has one. Never say "certain": say \
the 95% confidence interval excludes (or includes) the national value. Say that the county shares are \
crude. They have two separate limitations: (a) they are not age-adjusted (an age-adjusted value exists \
only from Kuva 16, for curative treatment, by sex); (b) they cannot be stage-adjusted because stage at \
diagnosis is missing for about 48% of patients. Never present missing stage as the reason the shares \
are not age-adjusted. Where an age-adjusted value exists (Kuva 16, digitised from a figure, about ±0.5 \
percentage points), use it to say whether a gap holds after age adjustment, say it is digitised, and \
pass on any caveat in the claim's notes (e.g. a confidence interval that could not be read).
4. The treatment categories overlap (a patient can have several); never add them up or present them as \
a breakdown, and whenever a sentence mentions two or more county treatment shares, say in that sentence \
that the categories overlap. "No treatment record within 12 months" mixes untreated patients and \
treatment that was not recorded; never call it "untreated" or "missing data". MDT records measure \
recording practice, not care.
5. Read the no-treatment-record share as a data-quality signal, using its 95% interval (the claim says \
"below", "above" or "not distinguishable" vs national). Only if the county's claim says "below" (the \
interval is entirely below national) may you say this is consistent with relatively complete treatment \
recording, as an inference, not a finding; a low curative share is then less likely to be only a \
recording artefact. If it says "not distinguishable", say nothing about recording completeness. If it \
says "above", you may say low treatment shares may partly reflect unrecorded treatment.
6. Label status in the sentence itself: a sentence citing a claim with status "preliminary" must say \
"preliminary" (e.g. "preliminary, unpublished figures"); one citing "mentor insight" must say \
"mentor insight". Claims "verified by Hellu" were read in full by a teammate in documents we do not \
hold locally (regional pathway documents, the Health Care Act, THL guidance, a journal article); \
describe them by what they are, not as regional documents unless they are. Every sentence that cites a \
county share (a claim whose ID starts with "cty:") must say the share is crude (the word "crude"). A \
sentence citing a claim with status "recommendation (ours)" must say it is the team's recommendation \
(e.g. "the team recommends"). In what_to_do_first, cite the relevant team recommendation (rec:1, rec:2 \
or rec:3) together with the evidence claims that support it; do not add steps that are in neither.
7. Respect each claim's scope ("scope: …" in its notes). Never use a claim for something outside its \
scope: e.g. the HILMO ~90% claim concerns diagnosis concordance only and says nothing about treatment \
recording; a regional finding describes only the named region's document; national averages are not \
county figures.
8. Describe planned national measures as plans, with the plan's own verb and date, in the present \
tense: e.g. "the roadmap plans national pathways with target access times for five cancers by \
2026–2028"; "the Filha programme's diagnostics recommendation is to be carried out before the 2030 \
mid-term evaluation" (say "carried out", never "completed" or "implemented"). Attribute each plan to the \
document, measure and date in its notes ("plan: …"): the STM roadmap and the Filha programme are \
different documents with different dates; never mix them in one attribution. Never write "will" about \
national measures. Never use the words certain, proves, guarantees or definitely.
9. Each section has a headline (the main point, one sentence of at most 30 words, with claim IDs) and \
2–4 detail sentences. "where_we_lag": where this county's pathway lags national values. \
"how_sure_are_we": what is well supported, what is uncertain and what public data cannot show. \
"what_to_do_first": the first steps, drawn from the team's draft recommendations and suited to this \
county's data, each backed by evidence claims.
10. Plain, direct English. No claims about other counties. No headings or numbering inside sentences. \
Apply these rules and the claim notes by writing accurately; do not restate them in the brief (do not \
write things like "this describes only its own document" or explain the meaning of a Finnish verb), and \
keep each sentence under about 60 words."""


def load(statuses=ledger.CITABLE) -> list[dict]:
    con = sqlite3.connect(ledger.DB)
    con.row_factory = sqlite3.Row
    q = f"SELECT * FROM claims WHERE status IN ({','.join('?' * len(statuses))})"
    rows = [dict(r) for r in con.execute(q, statuses)]
    con.close()
    return rows


def select_claims(full_name: str) -> list[dict]:
    rows = load()
    county = [r for r in rows if r["county"] == full_name]
    national = [r for r in rows if r["id"].startswith("nat:") or r["id"].startswith("k16:curative:") and r["county"] is None]
    evidence = [r for r in rows if r["county"] is None and not r["id"].startswith(("nat:", "k16:", "cty:"))]
    return county + national + evidence


def render_claim(c: dict) -> str:
    line = f"[{c['id']}] status={c['status']} | {c['claim_text']}"
    if c.get("quote"):
        line += f" | quote ({c['quote_lang']}): {c['quote']}"
        if c.get("quote_en"):
            line += f" | translation: {c['quote_en']}"
    src = (c.get("source_doc") or "").split("/")[-1]
    line += f" | source: {src}, {c.get('location')}"
    # County share notes only repeat the claim text; other notes carry caveats the model needs.
    if c.get("notes") and not c["id"].startswith("cty:"):
        line += f" | notes: {c['notes']}"
    return line


def build_prompt(short: str, full: str, claims: list[dict]) -> str:
    groups = [
        ("COUNTY CLAIMS", [c for c in claims if c["county"] == full]),
        ("NATIONAL CLAIMS", [c for c in claims if c["county"] is None and c["id"].startswith(("nat:", "k16:"))]),
        ("THE TEAM'S OWN DRAFT RECOMMENDATIONS (status 'recommendation (ours)'; citable, but they are "
         "proposals, not evidence)", [c for c in claims if c["id"].startswith("rec:")]),
        ("EVIDENCE (pathway coverage, policy, regional pathways, delays, mentor input)",
         [c for c in claims if c["county"] is None and not c["id"].startswith(("nat:", "k16:", "rec:"))]),
    ]
    body = [f"County: {short} ({full}). Data: new lung cancer patients 2019–2023, 12-month follow-up "
            "(Finnish Cancer Registry, Keuhkosyöpä Suomessa 2019–2023)."]
    for title, rows in groups:
        body.append(f"\n## {title}\n" + "\n".join(render_claim(c) for c in rows))
    return "\n".join(body)


def retry_prompt(prompt: str, previous: str, problems: list[str]) -> str:
    return (prompt + "\n\n## YOUR PREVIOUS ANSWER\n" + previous
            + "\n\n## PROBLEMS FOUND BY THE VALIDATOR (fix all of them; return the full brief again)\n"
            + "\n".join(f"- {p}" for p in problems))


def run(name: str) -> dict:
    short, full = counties.resolve(name)
    slug = counties.slug(short)
    claims = select_claims(full)
    allowed = {c["id"] for c in claims}
    by_id = {c["id"]: c for c in load(ledger.STATUSES)}
    model = gemini.model_name("MODEL_REASON")
    prompt = build_prompt(short, full, claims)

    attempts, raw_files, brief, problems, previous = 0, [], None, [], ""
    for attempt in (1, 2):
        attempts = attempt
        p = prompt if attempt == 1 else retry_prompt(prompt, previous, problems)
        parsed, text, raw = gemini.structured_call(model, SYSTEM, p, Brief, f"brief_{slug}_attempt{attempt}",
                                                   thinking_level=THINKING)
        raw_files.append(str(raw).replace("\\", "/"))
        previous = text
        if parsed is None:
            problems = ["response did not match the schema (no valid JSON)"]
            brief = None
            continue
        brief = parsed.model_dump()
        problems = validate(brief, allowed, by_id) + rule_problems(brief, by_id)
        if not problems:
            break

    status = "validated" if brief is not None and not problems else "DRAFT"
    cited = sorted({cid for _, s in iter_sentences(brief or {}) for cid in s["claim_ids"]})
    doc = {
        "county": short, "county_full": full, "status": status,
        "generated_at": datetime.now(timezone.utc).isoformat(timespec="seconds"),
        "model": model, "thinking_level": THINKING, "attempts": attempts, "problems": problems,
        "brief": brief, "raw_responses": raw_files, "provided_claim_ids": sorted(allowed),
        "cited_claims": {cid: {k: by_id[cid].get(k) for k in ("claim_text", "status", "method", "source_doc",
                                                                "location", "quote", "quote_lang", "quote_en")}
                         for cid in cited if cid in by_id},
    }
    OUT.mkdir(parents=True, exist_ok=True)
    # Model review: flags for human review only, saved next to the brief; never changes `status`.
    rev = review(doc, slug, OUT, by_id)
    doc["review"] = {"file": f"outputs/briefs/{slug}.review.json", "flags": len(rev["flags"]),
                     "note": rev["note"]}
    (OUT / f"{slug}.json").write_text(json.dumps(doc, ensure_ascii=False, indent=1), encoding="utf-8")
    (OUT / f"{slug}.md").write_text(to_markdown(doc, rev), encoding="utf-8")
    return doc


TITLES = {"where_we_lag": "Where do we lag?", "how_sure_are_we": "How sure are we?",
          "what_to_do_first": "What should we do first?"}


def to_markdown(doc: dict, rev: dict | None = None) -> str:
    lines = [f"# {doc['county']}: lung cancer pathway brief", "",
             f"Status: **{doc['status']}** · {doc['model']} (thinking {doc['thinking_level']}) · "
             f"{doc['generated_at']} · attempts: {doc['attempts']}", ""]
    if doc["problems"]:
        lines += ["**Validation problems:**", ""] + [f"- {p}" for p in doc["problems"]] + [""]
    for s in SECTIONS:
        sec = (doc["brief"] or {}).get(s) or {}
        lines += [f"## {TITLES[s]}", ""]
        if sec.get("headline"):
            h = sec["headline"]
            lines += [f"**{h['text']}** `{', '.join(h['claim_ids'])}`", ""]
        for x in sec.get("details") or []:
            lines.append(f"- {x['text']} `{', '.join(x['claim_ids'])}`")
        lines.append("")
    if rev is not None:
        lines += ["## Review flags (for human review only)", "", f"_{rev['note']}_", ""]
        lines += [f"- [{f['severity']}] `{f['location']}`: {f['problem']}" for f in rev["flags"]] or ["- none"]
        lines.append("")
    lines += ["## Claims cited", ""]
    for cid, c in doc["cited_claims"].items():
        lines.append(f"- `{cid}` ({c['status']}): {c['claim_text']} — {(c['source_doc'] or '').split('/')[-1]}, "
                     f"{c['location']}")
    return "\n".join(lines) + "\n"


def main() -> int:
    names = sys.argv[1:]
    if not names:
        print(__doc__)
        return 2
    for name in names:
        doc = run(name)
        print(f"{doc['county']}: {doc['status']} after {doc['attempts']} attempt(s); "
              f"{len(doc['problems'])} problem(s) -> outputs/briefs/{counties.slug(doc['county'])}.json")
        for p in doc["problems"]:
            print("   ", p)
    return 0


if __name__ == "__main__":
    sys.exit(main())
