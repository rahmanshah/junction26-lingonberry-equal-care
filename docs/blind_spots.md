# Blind spots on the lung cancer pathway

Which pathway stages public data measures, how long each stage takes, and what regions and national
policy say about it. Built by `src/build_blind_spots.py` (also writes `data/processed/blind_spots.csv`);
edit the script, not this file.

## Sources and status

| Layer | Source | Status |
|---|---|---|
| Measured? | ‘Keuhkosyöpä Suomessa 2019–2023’ (Finnish Cancer Registry) | verified locally (report) |
| Policy | National Cancer Strategy 2026–2035, Roadmap 2026–2031 (STM); Filha National Lung Cancer Programme 2026–2035 | verified locally (strategy/roadmap/Filha PDF); quotes in `docs/source_verification.md` |
| Regional pathways | Hellu's review: 5 regional pathways (Keski-Suomi, Pirha, KYS, HUS, OYS), Satakunta clinic page, 1 regional study (`docs/pathway_brief.md` §6) | verified by Hellu, read 14 Nov |
| Delays | MOT ‘Hitaasti syöpähoitoon’ (Yle 2025) | preliminary, unpublished, Yle MOT 2025 (primary author unknown) |
| Mentor insight | Kaisa, Hanna | mentor insight |

## Where the time goes (MOT, preliminary)

| Interval | Days | Our stages |
|---|---|---|
| Patient delay | 56 | Symptoms |
| Primary care | 41 | Primary care / occupational health, Imaging, Referral |
| Specialist care | 58 | First specialist visit, Diagnosis, MDT, Treatment start |
| **Total, Finland** | **155** | Sweden 107, Denmark 67 |

Mean days from first symptoms to first treatment. Preliminary and unpublished; primary author unknown.
Which of our stages fall in which interval is our assumption.

## By stage

| Stage | Measured? | By county? | Report source | What the report shows | MOT interval | Regional pathways | National policy | Mentor insight |
|---|---|---|---|---|---|---|---|---|
| Symptoms | **no** | no | none | Nothing in the report on symptoms, symptom onset or time from symptoms to care. | Patient delay (56 d) | – | Roadmap 2.5.2 (pp.52–53): symptom-based models (<q lang="fi">oirelähtöiset toimintamallit</q>) in national pathways of at least the five most common cancers by 2026–2028. | – |
| Primary care / occupational health | **no** | no | §3.3 | Primary care visits are excluded from the data: <q lang="fi">Avoterveydenhuollon käyntejä ei ole mukana aineistossa.</q> Occupational health is not mentioned. | Primary care (41 d) | Only KYS tells primary care what to do when the X-ray is normal but symptoms continue (refer anyway). OYS and Keski-Suomi name occupational health as a referral source. | Roadmap 2.5.2 (pp.52–53): primary-care investigation responsibilities and direct test routes. | Occupational health gets patients to specialist care faster (mentor insight, Hanna). |
| Imaging | **partly** | partly (Kuva 7, PNG only) | §4.1.1, Taulukko 2, Kuva 5–7 | Only indirectly, as the basis of diagnosis: <q lang="fi">pelkkään kliiniseen tutkimukseen, kuten kuvantamiseen, noin 20 %:ssa</q>. No imaging procedures, dates or waits: the code list (Taulukko 13) has no imaging codes. | Primary care (41 d) | Pirha: CT <q lang="en">most often within a week</q>. Other regions state no imaging times. | – | – |
| Referral | **no** | no | none | No referral data or referral dates in the report. | Primary care (41 d) | Only KYS lists what a referral must contain and provides a template; urgency R1 with no time. Pirha handles referrals <q lang="en">usually within 1–2 working days</q>; Keski-Suomi <q lang="en">as quickly as possible</q>. | Roadmap 2.5.2 (pp.52–53): standardised referral criteria (<q lang="fi">standardoidut lähetekriteerit</q>) by 2026–2028. Strategy p.33: no national system for pathways. Filha programme (pp.3, 16, 24; printed pages): a national lung cancer diagnostics recommendation with primary-care referral criteria (<q lang="fi">lähetekriteerit perusterveydenhuollolle</q>) and recommended time limits for the diagnostic pathway stages in specialist care (<q lang="fi">suositellut aikarajat</q>), due before the 2030 mid-term evaluation. | Referral quality affects triage: a weak referral gets a lower urgency rating (mentor insight, Kaisa). |
| First specialist visit | **partly** | no | §3.1, §4.2, Taulukko 5 | Whether a lung cancer visit (C33–C34, D38.1) appears in HILMO within 12 months: 93.6% (Taulukko 5). Not when: a visit up to 3 months before diagnosis only sets the start of follow-up (§3.1). | Specialist care (58 d) | Keski-Suomi target: lung clinic within 2–3 weeks, at the latest ~1 month after the referral. Pirha: invitation usually within 3–4 working days. No region names a contact person for the diagnostic phase; HUS assigns a nurse at the first visit. | Roadmap 3.1.2 (pp.56–57): national pathways with target access times for five (unnamed) cancers by 2026–2028, Nordic model; strategy p.5 indicator <q lang="fi">Potilaat pääsevät hoitoon tavoiteaikojen puitteissa</q> tied to THL Ohjaus 21/2016. Roadmap 1.2.3 (p.32): named care coordinator guidance 2026–2028; care phase not specified. | – |
| Diagnosis | **yes** | yes (Kuva 7, 10, 13: PNG only) | §4.1, Taulukko 2–4, Kuva 5–13 | Registry diagnosis date, diagnosis basis, histology. Stage is a blind spot within it: <q lang="fi">levinneisyys toteamishetkellä puuttuu lähes puolelta uusia potilaita</q> (§4.1.3, ~48%), so curative shares cannot be stage-adjusted. | Specialist care (58 d) | Keski-Suomi: tissue results in ~1–2 weeks. Pirha: bronchoscopy results usually in 3–5 days. Satakunta study (Univ. Turku): referral to diagnosis just under two months. | Roadmap 3.2.1 (pp.59–60): national quality registry; indicator: data incl. stage with 90% coverage. Strategy p.5: ≥70% diagnosed at stage I–II. | – |
| MDT | **partly** | yes (Taulukko 11) | §3.3, §4.2, Taulukko 5, 10, 11, 13 | Codes WZC15/WZC20 only; 6.0% nationally, 21.6–37.4% in Sisä-Suomi counties, 0 records in 4 counties. <q lang="fi">Erikoissairaanhoidon toimenpiteet viedään HILMO:on vain suorista potilaskontakteista, joten saatu tieto ei kuvaa kattavasti moniammatillisen käsittelyn laajuutta.</q> Measures recording practice, not care. | Specialist care (58 d) | KYS: every patient in a weekly MDT. Keski-Suomi: every new case. HUS: <q lang="en">when needed</q>. | Roadmap 3.1.2 (p.56): pathways will define recording and coding practices (<q lang="fi">kirjaamis- ja koodistokäytännöistä</q>). | – |
| Treatment start | **partly** | yes (type only, Taulukko 11) | §4.2, §4.2.2, Taulukko 6–9, 11, 12, Kuva 14, 17 | Which treatment type is recorded within 12 months, and the first one (§4.2.2), but not when it started. 27.5% have no treatment record at all (mixes untreated patients and unrecorded treatment). | Specialist care (58 d) | No region states a time to treatment, and none says whether its stated times are monitored. Law (Health Care Act §52): treatment within 6 months; no cancer-specific maximum. | Roadmap 3.1.2 (pp.56–57): national pathways with target access times for five (unnamed) cancers by 2026–2028, Nordic model; strategy p.5 indicator <q lang="fi">Potilaat pääsevät hoitoon tavoiteaikojen puitteissa</q> tied to THL Ohjaus 21/2016. Filha programme (pp.3, 16, 24; printed pages): a national lung cancer diagnostics recommendation with primary-care referral criteria (<q lang="fi">lähetekriteerit perusterveydenhuollolle</q>) and recommended time limits for the diagnostic pathway stages in specialist care (<q lang="fi">suositellut aikarajat</q>), due before the 2030 mid-term evaluation. The Filha time limits cover diagnostic stages; it names no time to treatment. | – |

## What this means

- Public data starts at diagnosis. Everything before it (symptoms, primary care, imaging, referral),
  97 of the 155 days in the MOT figures, is unmeasured, so delays before diagnosis
  cannot be compared between counties.
- The longest interval, specialist care (58 days), is also unmeasured in public data: the report shows
  *whether* and *which* treatment was recorded, never *when*.
- Regions describe the same steps but different times; none says whether it meets them. National
  target times arrive only with roadmap 3.1.2 (2026–2028, five unnamed cancers).
- MDT and ‘no treatment record’ mostly measure recording practice. Treat county differences there as
  data-quality signals, not care-quality findings.
- Missing stage for ~half of patients means no curative-share comparison can be stage-adjusted.

## Open

- Whether lung cancer is one of roadmap 3.1.2's five cancers (not named in the roadmap).
- Whether any THL 21/2016 access-time report has been published (to confirm with mentors).
- Primary author of the MOT figures.
