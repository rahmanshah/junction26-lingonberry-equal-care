"""Blind-spot table: which lung cancer pathway stages are measured, how long they take, and what
regions and national policy say about them.

Single source of truth for data/processed/blind_spots.csv and docs/blind_spots.md.

Evidence layers, each with its own status column:
  report        "Keuhkosyöpä Suomessa 2019–2023" (saved HTML)       -> verified locally
  policy        strategy 2026–2035 + roadmap 2026–2031 (Finnish PDFs) -> verified locally
                (quotes and page numbers: docs/source_verification.md)
  regional      regional pathway documents (Hellu, docs/pathway_brief.md §6) -> verified by Hellu
  MOT delays    Yle MOT 2025, preliminary unpublished study             -> not verifiable
  mentor        mentor input                                             -> "mentor insight (name)"
Section/table numbers are the report's own (1-based), not our CSV numbering.
"""
from pathlib import Path

import pandas as pd

CSV = Path("data/processed/blind_spots.csv")
MD = Path("docs/blind_spots.md")

ST_REPORT = "verified locally (report)"
ST_POLICY = "verified locally (strategy/roadmap/Filha PDF)"
ST_HELLU = "verified by Hellu, read 14 Nov"
ST_MOT = "preliminary, unpublished, Yle MOT 2025 (primary author unknown)"

# MOT intervals, mean days from first symptoms to first treatment (pathway_brief.md §7).
# Mapping of our stages to the three MOT intervals is OUR assumption: patient delay = symptoms to
# first contact; primary care = first contact to referral; specialist = referral to treatment.
MOT = {
    "patient": ("Patient delay", 56),
    "primary": ("Primary care", 41),
    "specialist": ("Specialist care", 58),
}
MOT_TOTAL = {"Finland": 155, "Sweden": 107, "Denmark": 67}
assert sum(d for _, d in MOT.values()) == MOT_TOTAL["Finland"], "MOT intervals must sum to 155"

def fi(text: str) -> str:
    """A verbatim Finnish source quote (checked by src/check_claims.py)."""
    return f'<q lang="fi">{text}</q>'


def en(text: str) -> str:
    """A verbatim English quote, from Hellu's brief (checked by src/check_claims.py)."""
    return f'<q lang="en">{text}</q>'


ACCESS_TARGETS = ("Roadmap 3.1.2 (pp.56–57): national pathways with target access times for five "
                  "(unnamed) cancers by 2026–2028, Nordic model; strategy p.5 indicator "
                  + fi("Potilaat pääsevät hoitoon tavoiteaikojen puitteissa") + " tied to THL Ohjaus 21/2016.")
FILHA_DIAGNOSTICS = ("Filha programme (pp.3, 16, 24; printed pages): a national lung cancer diagnostics "
                     "recommendation with primary-care referral criteria ("
                     + fi("lähetekriteerit perusterveydenhuollolle") + ") and recommended time limits for "
                     "the diagnostic pathway stages in specialist care (" + fi("suositellut aikarajat")
                     + "), due before the 2030 mid-term evaluation.")

ROWS = [
    {
        "stage": "Symptoms",
        "measured": "no",
        "by_county": "no",
        "source": "none",
        "note": "Nothing in the report on symptoms, symptom onset or time from symptoms to care.",
        "mot": "patient",
        "regional": "",
        "policy": ("Roadmap 2.5.2 (pp.52–53): symptom-based models (" + fi("oirelähtöiset toimintamallit")
                   + ") in national pathways of at least the five most common cancers by 2026–2028."),
        "mentor": "",
    },
    {
        "stage": "Primary care / occupational health",
        "measured": "no",
        "by_county": "no",
        "source": "§3.3",
        "note": ("Primary care visits are not included in the report's data: "
                 + fi("Avoterveydenhuollon käyntejä ei ole mukana aineistossa.")
                 + " Occupational health is not mentioned in the report at all."),
        "mot": "primary",
        "regional": ("Only KYS tells primary care what to do when the X-ray is normal but symptoms continue "
                     "(refer anyway). OYS and Keski-Suomi name occupational health as a referral source."),
        "policy": "Roadmap 2.5.2 (pp.52–53): primary-care investigation responsibilities and direct test routes.",
        "mentor": "Occupational health gets patients to specialist care faster (mentor insight, Hanna).",
    },
    {
        "stage": "Imaging",
        "measured": "partly",
        "by_county": "partly (Kuva 7, PNG only)",
        "source": "§4.1.1, Taulukko 2, Kuva 5–7",
        "note": ("Only indirectly, as the basis of diagnosis: "
                 + fi("pelkkään kliiniseen tutkimukseen, kuten kuvantamiseen, noin 20 %:ssa")
                 + ". No imaging procedures, dates or waits: the code list (Taulukko 13) has no imaging codes."),
        "mot": "primary",
        "regional": "Pirha: CT " + en("most often within a week") + ". Other regions state no imaging times.",
        "policy": "",
        "mentor": "",
    },
    {
        "stage": "Referral",
        "measured": "no",
        "by_county": "no",
        "source": "none",
        "note": "No referral data or referral dates in the report.",
        "mot": "primary",
        "regional": ("Only KYS lists what a referral must contain and provides a template; urgency R1 with "
                     "no time. Pirha handles referrals " + en("usually within 1–2 working days")
                     + "; Keski-Suomi " + en("as quickly as possible") + "."),
        "policy": ("Roadmap 2.5.2 (pp.52–53): standardised referral criteria ("
                   + fi("standardoidut lähetekriteerit") + ") by 2026–2028. Strategy p.33: no national "
                   "system for pathways. " + FILHA_DIAGNOSTICS),
        "mentor": ("Referral quality affects triage: a weak referral gets a lower urgency rating "
                   "(mentor insight, Kaisa)."),
    },
    {
        "stage": "First specialist visit",
        "measured": "partly",
        "by_county": "no",
        "source": "§3.1, §4.2, Taulukko 5",
        "note": ("Whether a lung cancer visit (C33–C34, D38.1) appears in HILMO within 12 months: 93.6% "
                 "(Taulukko 5). Not when: a visit up to 3 months before diagnosis only sets the start of "
                 "follow-up (§3.1)."),
        "mot": "specialist",
        "regional": ("Keski-Suomi target: lung clinic within 2–3 weeks, at the latest ~1 month after the "
                     "referral. Pirha: invitation usually within 3–4 working days. No region names a "
                     "contact person for the diagnostic phase; HUS assigns a nurse at the first visit."),
        "policy": ACCESS_TARGETS + (" Roadmap 1.2.3 (p.32): named care coordinator guidance 2026–2028; "
                                    "care phase not specified."),
        "mentor": "",
    },
    {
        "stage": "Diagnosis",
        "measured": "yes",
        "by_county": "yes (Kuva 7, 10, 13: PNG only)",
        "source": "§4.1, Taulukko 2–4, Kuva 5–13",
        "note": ("Registry diagnosis date, diagnosis basis, histology. Stage is a blind spot within it: "
                 + fi("levinneisyys toteamishetkellä puuttuu lähes puolelta uusia potilaita") + " (§4.1.3, ~48%), "
                 "so curative shares cannot be stage-adjusted."),
        "mot": "specialist",
        "regional": ("Keski-Suomi: tissue results in ~1–2 weeks. Pirha: bronchoscopy results usually in 3–5 "
                     "days. Satakunta study (Univ. Turku): referral to diagnosis just under two months."),
        "policy": ("Roadmap 3.2.1 (pp.59–60): national quality registry; indicator: data incl. stage with "
                   "90% coverage. Strategy p.5: ≥70% diagnosed at stage I–II."),
        "mentor": "",
    },
    {
        "stage": "MDT",
        "measured": "partly",
        "by_county": "yes (Taulukko 11)",
        "source": "§3.3, §4.2, Taulukko 5, 10, 11, 13",
        "note": ("Codes WZC15/WZC20 only; 6.0% nationally, 21.6–37.4% in Sisä-Suomi counties, 0 records in "
                 "4 counties. "
                 + fi("Erikoissairaanhoidon toimenpiteet viedään HILMO:on vain suorista potilaskontakteista, "
                      "joten saatu tieto ei kuvaa kattavasti moniammatillisen käsittelyn laajuutta.")
                 + " Measures recording practice, not care."),
        "mot": "specialist",
        "regional": "KYS: every patient in a weekly MDT. Keski-Suomi: every new case. HUS: " + en("when needed") + ".",
        "policy": ("Roadmap 3.1.2 (p.56): pathways will define recording and coding practices ("
                   + fi("kirjaamis- ja koodistokäytännöistä") + ")."),
        "mentor": "",
    },
    {
        "stage": "Treatment start",
        "measured": "partly",
        "by_county": "yes (type only, Taulukko 11)",
        "source": "§4.2, §4.2.2, Taulukko 6–9, 11, 12, Kuva 14, 17",
        "note": ("Which treatment type is recorded within 12 months, and the first one (§4.2.2), but not "
                 "when it started. 27.5% have no treatment record at all (mixes untreated patients and "
                 "unrecorded treatment)."),
        "mot": "specialist",
        "regional": ("No region states a time to treatment, and none says whether its stated times are "
                     "monitored. Law (Health Care Act §52): treatment within 6 months; no cancer-specific "
                     "maximum."),
        "policy": ACCESS_TARGETS + " " + FILHA_DIAGNOSTICS + " The Filha time limits cover diagnostic "
                  "stages; it names no time to treatment.",
        "mentor": "",
    },
]

records = []
for r in ROWS:
    interval, days = MOT[r["mot"]]
    records.append({
        "stage": r["stage"],
        "measured": r["measured"],
        "by_county": r["by_county"],
        "report_source": r["source"],
        "report_note": r["note"],
        "report_status": ST_REPORT,
        "mot_interval": interval,
        "mot_interval_days": days,
        "mot_status": ST_MOT,
        "regional_pathways": r["regional"],
        "regional_status": ST_HELLU if r["regional"] else "",
        "policy": r["policy"],
        "policy_status": ST_POLICY if r["policy"] else "",
        "mentor_insight": r["mentor"],
    })
df = pd.DataFrame(records)
assert set(df["measured"]) <= {"yes", "partly", "no"}
assert all("mentor insight" in m for m in df["mentor_insight"] if m), "Mentor input must be labelled"
CSV.parent.mkdir(parents=True, exist_ok=True)
df.to_csv(CSV, index=False, encoding="utf-8")


def cell(text: str) -> str:
    return text.replace("|", "/") if text else "–"


lines = [
    "# Blind spots on the lung cancer pathway",
    "",
    "Which pathway stages public data measures, how long each stage takes, and what regions and national",
    "policy say about it. Built by `src/build_blind_spots.py` (also writes `data/processed/blind_spots.csv`);",
    "edit the script, not this file.",
    "",
    "## Sources and status",
    "",
    "| Layer | Source | Status |",
    "|---|---|---|",
    f"| Measured? | ‘Keuhkosyöpä Suomessa 2019–2023’ (Finnish Cancer Registry) | {ST_REPORT} |",
    f"| Policy | National Cancer Strategy 2026–2035, Roadmap 2026–2031 (STM); Filha National Lung Cancer Programme 2026–2035 | {ST_POLICY}; quotes in `docs/source_verification.md` |",
    f"| Regional pathways | Hellu's review: 5 regional pathways (Keski-Suomi, Pirha, KYS, HUS, OYS), Satakunta clinic page, 1 regional study (`docs/pathway_brief.md` §6) | {ST_HELLU} |",
    f"| Delays | MOT ‘Hitaasti syöpähoitoon’ (Yle 2025) | {ST_MOT} |",
    "| Mentor insight | Kaisa, Hanna | mentor insight |",
    "",
    "## Where the time goes (MOT, preliminary)",
    "",
    "| Interval | Days | Our stages |",
    "|---|---|---|",
]
for key, (name, days) in MOT.items():
    stages = ", ".join(r["stage"] for r in ROWS if r["mot"] == key)
    lines.append(f"| {name} | {days} | {stages} |")
lines += [
    f"| **Total, Finland** | **{MOT_TOTAL['Finland']}** | Sweden {MOT_TOTAL['Sweden']}, Denmark {MOT_TOTAL['Denmark']} |",
    "",
    "Mean days from first symptoms to first treatment. Preliminary and unpublished; primary author unknown.",
    "Which of our stages fall in which interval is our assumption.",
    "",
    "## By stage",
    "",
    "| Stage | Measured? | By county? | Report source | What the report shows | MOT interval | Regional pathways | National policy | Mentor insight |",
    "|---|---|---|---|---|---|---|---|---|",
]
for r, rec in zip(ROWS, records):
    lines.append(
        f"| {rec['stage']} | **{rec['measured']}** | {cell(rec['by_county'])} | {cell(rec['report_source'])} | "
        f"{cell(rec['report_note'])} | {rec['mot_interval']} ({rec['mot_interval_days']} d) | "
        f"{cell(rec['regional_pathways'])} | {cell(rec['policy'])} | {cell(rec['mentor_insight'])} |"
    )
lines += [
    "",
    "## What this means",
    "",
    "- Public data starts at diagnosis. Everything before it (symptoms, primary care, imaging, referral),",
    f"  {MOT['patient'][1] + MOT['primary'][1]} of the {MOT_TOTAL['Finland']} days in the MOT figures, is "
    "unmeasured, so delays before diagnosis",
    "  cannot be compared between counties.",
    "- The longest interval, specialist care (58 days), is also unmeasured in public data: the report shows",
    "  *whether* and *which* treatment was recorded, never *when*.",
    "- Regions describe the same steps but different times; none says whether it meets them. National",
    "  target times arrive only with roadmap 3.1.2 (2026–2028, five unnamed cancers).",
    "- MDT and ‘no treatment record’ mostly measure recording practice. Treat county differences there as",
    "  data-quality signals, not care-quality findings.",
    "- Missing stage for ~half of patients means no curative-share comparison can be stage-adjusted.",
    "",
    "## Open",
    "",
    "- Whether lung cancer is one of roadmap 3.1.2's five cancers (not named in the roadmap).",
    "- Whether any THL 21/2016 access-time report has been published (to confirm with mentors).",
    "- Primary author of the MOT figures.",
]
MD.parent.mkdir(parents=True, exist_ok=True)
MD.write_text("\n".join(lines) + "\n", encoding="utf-8")
print(df[["stage", "measured", "mot_interval", "mot_interval_days"]].to_string(index=False))
print("Saved", CSV, "and", MD)
