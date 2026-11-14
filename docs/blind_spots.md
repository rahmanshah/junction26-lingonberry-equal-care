# Blind spots on the lung cancer pathway

Which pathway stages can be measured from public aggregate data. Built by `src/build_blind_spots.py`
(also writes `data/processed/blind_spots.csv`); edit the script, not this file.

Source: "Keuhkosyöpä Suomessa 2019–2023" (Finnish Cancer Registry). Section and table numbers are the
report's own. `basis` marks where each row comes from; mentor input is labelled "mentor insight".

| Stage | Measured? | By county? | Source | Note | Basis |
|---|---|---|---|---|---|
| Symptoms | **no** | no | none | Nothing in the report on symptoms, symptom onset or time from symptoms to care. | report |
| Primary care / occupational health | **no** | no | §3.3 | Primary care visits are excluded from the data: "Avoterveydenhuollon käyntejä ei ole mukana aineistossa." Occupational health is not mentioned. | report |
| Imaging | **partly** | partly (Kuva 7, PNG only) | §4.1.1, Taulukko 2, Kuva 5–7 | Only indirectly, as the basis of diagnosis: "pelkkään kliiniseen tutkimukseen, kuten kuvantamiseen, noin 20 %:ssa". No imaging procedures, dates or waits: the code list (Taulukko 13) has no imaging codes. | report |
| Referral | **no** | no | none | No referral data or referral dates in the report. Keuhkosyöpäohjelma goal (report §2): "keuhkosyövän hoitoketjut ovat sujuvia ja laadukkaita"; no published interval lets us check this. | report |
| First specialist visit | **partly** | no | §3.1, §4.2, Taulukko 5 | Whether a lung cancer visit (C33–C34, D38.1) appears in HILMO within 12 months: 93.6% (Taulukko 5). Not when: a visit up to 3 months before diagnosis only sets the start of follow-up (§3.1); no time to first visit is published. | report |
| Diagnosis | **yes** | yes (Kuva 7, 10, 13: PNG only) | §4.1, Taulukko 2–4, Kuva 5–13 | Registry diagnosis date, diagnosis basis, histology. Stage is a blind spot within it: "levinneisyys toteamishetkellä puuttuu lähes puolelta uusia potilaita" (§4.1.3, ~48%), so curative shares cannot be stage-adjusted. | report |
| MDT | **partly** | yes (Taulukko 11) | §3.3, §4.2, Taulukko 5, 10, 11, 13 | Codes WZC15/WZC20 only; 6.0% nationally, 21.6–37.4% in Sisä-Suomi counties, 0 records in 4 counties. "Erikoissairaanhoidon toimenpiteet viedään HILMO:on vain suorista potilaskontakteista, joten saatu tieto ei kuvaa kattavasti moniammatillisen käsittelyn laajuutta." Measures recording practice, not care. | report |
| Treatment start | **partly** | yes (type only, Taulukko 11) | §4.2, §4.2.2, Taulukko 6–9, 11, 12, Kuva 14, 17 | Which treatment type is recorded within 12 months, and the first one (§4.2.2), but not when it started: no time from diagnosis to treatment. 27.5% have no treatment record at all (mixes untreated patients and unrecorded treatment). Keuhkosyöpäohjelma goal (report §2): "keuhkosyövän hoitoketjut ovat sujuvia ja laadukkaita"; no published interval lets us check this. | report |

## What this means

- Public data starts at diagnosis. Everything before it (symptoms, primary care, imaging, referral) is
  unmeasured, so delays before diagnosis cannot be compared between counties.
- After diagnosis we see *whether* and *which* treatment was recorded, never *when*. The programme's
  goal of smooth care chains cannot be checked from this report.
- MDT and "no treatment record" mostly measure recording practice. Treat county differences there as
  data-quality signals, not care-quality findings.
- Missing stage for ~half of patients means no curative-share comparison can be stage-adjusted.

## Still to add

- The national strategy / roadmap documents are not in the repo yet; only the programme goals quoted
  in report §2 are used.
- No mentor insights recorded yet.
