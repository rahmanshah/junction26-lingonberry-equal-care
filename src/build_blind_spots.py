"""Blind-spot table: which lung cancer pathway stages are measured in public data.

Single source of truth for data/processed/blind_spots.csv and docs/blind_spots.md.
Evidence is limited to the 2019-2023 report ("Keuhkosyöpä Suomessa 2019–2023"), including
what it says about the national lung cancer programme (Keuhkosyöpäohjelma, §2).
basis: "report" | "strategy" | "mentor insight" (mentor input must be labelled as such).
Section/table numbers are the report's own (1-based), not our CSV numbering.
"""
from pathlib import Path

import pandas as pd

CSV = Path("data/processed/blind_spots.csv")
MD = Path("docs/blind_spots.md")

PROGRAMME_GOAL = ("Keuhkosyöpäohjelma goal (report §2): \"keuhkosyövän hoitoketjut ovat sujuvia ja "
                  "laadukkaita\"; no published interval lets us check this.")

ROWS = [
    {
        "stage": "Symptoms",
        "measured": "no",
        "by_county": "no",
        "source": "none",
        "note": "Nothing in the report on symptoms, symptom onset or time from symptoms to care.",
        "basis": "report",
    },
    {
        "stage": "Primary care / occupational health",
        "measured": "no",
        "by_county": "no",
        "source": "§3.3",
        "note": ("Primary care visits are excluded from the data: \"Avoterveydenhuollon käyntejä ei ole "
                 "mukana aineistossa.\" Occupational health is not mentioned."),
        "basis": "report",
    },
    {
        "stage": "Imaging",
        "measured": "partly",
        "by_county": "partly (Kuva 7, PNG only)",
        "source": "§4.1.1, Taulukko 2, Kuva 5–7",
        "note": ("Only indirectly, as the basis of diagnosis: \"pelkkään kliiniseen tutkimukseen, kuten "
                 "kuvantamiseen, noin 20 %:ssa\". No imaging procedures, dates or waits: the code list "
                 "(Taulukko 13) has no imaging codes."),
        "basis": "report",
    },
    {
        "stage": "Referral",
        "measured": "no",
        "by_county": "no",
        "source": "none",
        "note": "No referral data or referral dates in the report. " + PROGRAMME_GOAL,
        "basis": "report",
    },
    {
        "stage": "First specialist visit",
        "measured": "partly",
        "by_county": "no",
        "source": "§3.1, §4.2, Taulukko 5",
        "note": ("Whether a lung cancer visit (C33–C34, D38.1) appears in HILMO within 12 months: 93.6% "
                 "(Taulukko 5). Not when: a visit up to 3 months before diagnosis only sets the start of "
                 "follow-up (§3.1); no time to first visit is published."),
        "basis": "report",
    },
    {
        "stage": "Diagnosis",
        "measured": "yes",
        "by_county": "yes (Kuva 7, 10, 13: PNG only)",
        "source": "§4.1, Taulukko 2–4, Kuva 5–13",
        "note": ("Registry diagnosis date, diagnosis basis, histology. Stage is a blind spot within it: "
                 "\"levinneisyys toteamishetkellä puuttuu lähes puolelta uusia potilaita\" (§4.1.3, ~48%), "
                 "so curative shares cannot be stage-adjusted."),
        "basis": "report",
    },
    {
        "stage": "MDT",
        "measured": "partly",
        "by_county": "yes (Taulukko 11)",
        "source": "§3.3, §4.2, Taulukko 5, 10, 11, 13",
        "note": ("Codes WZC15/WZC20 only; 6.0% nationally, 21.6–37.4% in Sisä-Suomi counties, 0 records in "
                 "4 counties. \"Erikoissairaanhoidon toimenpiteet viedään HILMO:on vain suorista "
                 "potilaskontakteista, joten saatu tieto ei kuvaa kattavasti moniammatillisen käsittelyn "
                 "laajuutta.\" Measures recording practice, not care."),
        "basis": "report",
    },
    {
        "stage": "Treatment start",
        "measured": "partly",
        "by_county": "yes (type only, Taulukko 11)",
        "source": "§4.2, §4.2.2, Taulukko 6–9, 11, 12, Kuva 14, 17",
        "note": ("Which treatment type is recorded within 12 months, and the first one (§4.2.2), but not "
                 "when it started: no time from diagnosis to treatment. 27.5% have no treatment record at "
                 "all (mixes untreated patients and unrecorded treatment). " + PROGRAMME_GOAL),
        "basis": "report",
    },
]

df = pd.DataFrame(ROWS)
assert set(df["measured"]) <= {"yes", "partly", "no"}
assert set(df["basis"]) <= {"report", "strategy", "mentor insight"}
CSV.parent.mkdir(parents=True, exist_ok=True)
df.to_csv(CSV, index=False, encoding="utf-8")

lines = [
    "# Blind spots on the lung cancer pathway",
    "",
    "Which pathway stages can be measured from public aggregate data. Built by `src/build_blind_spots.py`",
    "(also writes `data/processed/blind_spots.csv`); edit the script, not this file.",
    "",
    "Source: \"Keuhkosyöpä Suomessa 2019–2023\" (Finnish Cancer Registry). Section and table numbers are the",
    "report's own. `basis` marks where each row comes from; mentor input is labelled \"mentor insight\".",
    "",
    "| Stage | Measured? | By county? | Source | Note | Basis |",
    "|---|---|---|---|---|---|",
]
for r in ROWS:
    lines.append(f"| {r['stage']} | **{r['measured']}** | {r['by_county']} | {r['source']} | {r['note']} | {r['basis']} |")
lines += [
    "",
    "## What this means",
    "",
    "- Public data starts at diagnosis. Everything before it (symptoms, primary care, imaging, referral) is",
    "  unmeasured, so delays before diagnosis cannot be compared between counties.",
    "- After diagnosis we see *whether* and *which* treatment was recorded, never *when*. The programme's",
    "  goal of smooth care chains cannot be checked from this report.",
    "- MDT and \"no treatment record\" mostly measure recording practice. Treat county differences there as",
    "  data-quality signals, not care-quality findings.",
    "- Missing stage for ~half of patients means no curative-share comparison can be stage-adjusted.",
    "",
    "## Still to add",
    "",
    "- The national strategy / roadmap documents are not in the repo yet; only the programme goals quoted",
    "  in report §2 are used.",
    "- No mentor insights recorded yet.",
]
MD.parent.mkdir(parents=True, exist_ok=True)
MD.write_text("\n".join(lines) + "\n", encoding="utf-8")
print(df[["stage", "measured", "by_county", "source"]].to_string(index=False))
print("Saved", CSV, "and", MD)
