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
from validate_brief import SECTIONS, validate

OUT = Path("outputs/briefs")
RECS = Path("docs/recommendations.md")
THINKING = "HIGH"


class Sentence(BaseModel):
    text: str = Field(description="One plain-English sentence.")
    claim_ids: list[str] = Field(description="IDs of the claims this sentence relies on (at least one).")


class Brief(BaseModel):
    where_we_lag: list[Sentence]
    how_sure_are_we: list[Sentence]
    what_to_do_first: list[Sentence]


SYSTEM = """You write a short evidence brief on the lung cancer care pathway for one Finnish wellbeing \
services county, for the county's health managers. You may use ONLY the claims provided. Each claim has \
an ID, a status and a text.

Rules:
1. Every sentence must list the IDs of the claims it relies on in claim_ids (at least one). Use IDs \
exactly as given. Do not cite anything that is not in the list.
2. Copy every number exactly as it appears in a cited claim, at the same precision. Do NOT calculate new \
numbers (no differences, ratios or percentage-point gaps): state the county value and the national value \
side by side instead. Spell out no numbers in words.
3. State uncertainty. Give 95% confidence intervals where the claim has one. Say that the county shares \
are crude (not adjusted for age or stage). Where an age-adjusted value exists (Kuva 16, digitised from a \
figure, about ±0.5 percentage points), use it to say whether a gap holds after age adjustment, and say \
it is digitised.
4. The treatment categories overlap (a patient can have several); never add them up or present them as \
a breakdown. "No treatment record within 12 months" mixes untreated patients and treatment that was not \
recorded; never call it "untreated" or "missing data". MDT records measure recording practice, not care.
5. Label status in the sentence itself: a sentence citing a claim with status "preliminary" must say \
"preliminary" (e.g. "preliminary, unpublished figures"); one citing "mentor insight" must say \
"mentor insight". Claims "verified by Hellu" come from a teammate's reading of regional documents.
6. "where_we_lag": where this county's pathway lags national values (3–5 sentences). \
"how_sure_are_we": what is certain, what is uncertain and what public data cannot show (3–5 sentences). \
"what_to_do_first": the first steps, drawn from the team's draft recommendations and suited to this \
county's data, each backed by evidence claims (2–4 sentences).
7. Plain, direct English. No claims about other counties. No headings or numbering inside sentences."""


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


def recommendations() -> str:
    text = RECS.read_text(encoding="utf-8")
    text = re.sub(r'<q lang="[a-z]{2}">(.*?)</q>', r"“\1”", text, flags=re.S)
    parts = []
    for m in re.finditer(r"^## (\d\..+?)\n(.*?)(?=^## |\Z)", text, re.M | re.S):
        what = re.search(r"\*\*What:\*\*(.*?)(?=\n\*\*|\Z)", m.group(2), re.S)
        parts.append(f"{m.group(1).strip()}\n{re.sub(r'\s+', ' ', what.group(1)).strip() if what else ''}")
    assert len(parts) == 3, f"Expected 3 recommendations in {RECS}, found {len(parts)}"
    return "\n\n".join(parts)


def render_claim(c: dict) -> str:
    line = f"[{c['id']}] status={c['status']} | {c['claim_text']}"
    if c.get("quote"):
        line += f" | quote ({c['quote_lang']}): {c['quote']}"
        if c.get("quote_en"):
            line += f" | translation: {c['quote_en']}"
    src = (c.get("source_doc") or "").split("/")[-1]
    line += f" | source: {src}, {c.get('location')}"
    return line


def build_prompt(short: str, full: str, claims: list[dict]) -> str:
    groups = [
        ("COUNTY CLAIMS", [c for c in claims if c["county"] == full]),
        ("NATIONAL CLAIMS", [c for c in claims if c["county"] is None and c["id"].startswith(("nat:", "k16:"))]),
        ("EVIDENCE FOR THE RECOMMENDATIONS (pathway, policy, regional pathways, delays)",
         [c for c in claims if c["county"] is None and not c["id"].startswith(("nat:", "k16:"))]),
    ]
    body = [f"County: {short} ({full}). Data: new lung cancer patients 2019–2023, 12-month follow-up "
            "(Finnish Cancer Registry, Keuhkosyöpä Suomessa 2019–2023)."]
    for title, rows in groups:
        body.append(f"\n## {title}\n" + "\n".join(render_claim(c) for c in rows))
    body.append("\n## THE TEAM'S DRAFT RECOMMENDATIONS (context only; cite the evidence claims, not these)\n"
                + recommendations())
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
        problems = validate(brief, allowed, by_id)
        if not problems:
            break

    status = "validated" if brief is not None and not problems else "DRAFT"
    cited = sorted({cid for s in SECTIONS for x in (brief or {}).get(s, []) for cid in x["claim_ids"]})
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
    (OUT / f"{slug}.json").write_text(json.dumps(doc, ensure_ascii=False, indent=1), encoding="utf-8")
    (OUT / f"{slug}.md").write_text(to_markdown(doc), encoding="utf-8")
    return doc


def to_markdown(doc: dict) -> str:
    titles = {"where_we_lag": "Where we lag", "how_sure_are_we": "How sure are we",
              "what_to_do_first": "What to do first"}
    lines = [f"# {doc['county']}: lung cancer pathway brief", "",
             f"Status: **{doc['status']}** · {doc['model']} (thinking {doc['thinking_level']}) · "
             f"{doc['generated_at']} · attempts: {doc['attempts']}", ""]
    if doc["problems"]:
        lines += ["**Validation problems:**", ""] + [f"- {p}" for p in doc["problems"]] + [""]
    for s in SECTIONS:
        lines += [f"## {titles[s]}", ""]
        for x in (doc["brief"] or {}).get(s, []):
            lines.append(f"- {x['text']} `{', '.join(x['claim_ids'])}`")
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
