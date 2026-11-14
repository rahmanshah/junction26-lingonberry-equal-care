# Varsinais-Suomi: lung cancer pathway brief

Status: **validated** · gemini-4-argon (thinking HIGH) · 2026-11-14T11:31:07+00:00 · attempts: 1

## Where do we lag?

**In Varsinais-Suomen hyvinvointialue, crude recorded curative, life-prolonging, and symptomatic treatment shares and MDT recording lag behind national values, while 43.1% have no treatment record within 12 months.** `cty:curative:Varsinais_Suomen_hyvinvointialue, cty:life_prolonging:Varsinais_Suomen_hyvinvointialue, cty:symptomatic:Varsinais_Suomen_hyvinvointialue, cty:no_treatment_record:Varsinais_Suomen_hyvinvointialue, cty:mdt_recorded:Varsinais_Suomen_hyvinvointialue`

- Across overlapping treatment categories that are crude and not adjusted for age or stage, curative treatment is 24.3% (95% CI 22.1–26.6; n=349/1437) versus 27.0% nationally, life-prolonging treatment is 9.7% (95% CI 8.3–11.4; n=140/1437) versus 30.4%, and symptomatic treatment is 30.8% (95% CI 28.5–33.3; n=443/1437) versus 39.5%, with all 95% confidence intervals excluding the national values. `cty:curative:Varsinais_Suomen_hyvinvointialue, nat:curative, cty:life_prolonging:Varsinais_Suomen_hyvinvointialue, nat:life_prolonging, cty:symptomatic:Varsinais_Suomen_hyvinvointialue, nat:symptomatic, bs:coverage:Diagnosis`
- In figures digitised from Kuva 16 (precision about ±0.5 percentage points), the curative gap holds after age adjustment for men at 22.7% versus 26.7% nationally (confidence interval bar hidden inside the dot, half-width < ~3.3 percentage points), but not for women at 27.4% (95% CI 23.1–31.8), whose 95% confidence interval includes the national 26.9%. `k16:curative:men:Varsinais_Suomen_hyvinvointialue, k16:curative:men:national, k16:curative:women:Varsinais_Suomen_hyvinvointialue, k16:curative:women:national`
- Meanwhile, 43.1% (95% CI 40.5–45.6; n=619/1437) have no treatment record within 12 months compared with 27.5% nationally (4089/14873), and a multidisciplinary team (MDT) meeting is recorded for 1.6% (95% CI 1.1–2.4; n=23/1437) compared with 6.0% nationally (893/14873), with these 95% confidence intervals excluding the national values. `cty:no_treatment_record:Varsinais_Suomen_hyvinvointialue, nat:no_treatment_record, cty:mdt_recorded:Varsinais_Suomen_hyvinvointialue, nat:mdt_recorded`

## How sure are we?

**The county's high share of patients with no treatment record within 12 months suggests unrecorded care, while public data omit stage for ~48% of patients and lack pathway timestamps.** `cty:no_treatment_record:Varsinais_Suomen_hyvinvointialue, bs:coverage:Treatment_start, bs:coverage:Diagnosis, bs:coverage:Referral`

- Because having no treatment record within 12 months mixes untreated patients and unrecorded treatment, we infer from the 43.1% county share (versus 27.5% nationally) as a data-quality signal that low recorded treatment shares may partly reflect unrecorded treatment, whereas a journal article shows hospital discharge register concordance of about 90% for diagnoses only. `cty:no_treatment_record:Varsinais_Suomen_hyvinvointialue, nat:no_treatment_record, bs:coverage:Treatment_start, lit:hilmo_90`
- Similarly, MDT records measure recording practice rather than care because specialist procedures enter HILMO only from direct patient contacts, and stage at diagnosis is missing for ~48% of new patients nationally, preventing stage adjustment of county treatment shares. `bs:coverage:MDT, q:39e6ba43a9, bs:coverage:Diagnosis, q:7885b0974f`
- Public data exclude outpatient primary care and occupational health visits and lack dates for symptoms, referrals, imaging waits, specialist visits, and treatment start, though preliminary, unpublished national figures show 155 days on average from symptoms to treatment in Finland (versus 107 in Sweden and 67 in Denmark), including 56 patient, 41 primary care, and 58 specialist care days. `bs:coverage:Symptoms, bs:coverage:Primary_care_occupational_health, q:323de0d90d, bs:coverage:Imaging, bs:coverage:Referral, bs:coverage:First_specialist_visit, bs:coverage:Treatment_start, mot:total_fi, mot:total_se, mot:total_dk, mot:patient, mot:primary, mot:specialist`

## What should we do first?

**Varsinais-Suomen hyvinvointialue should prioritise auditing treatment, stage, and MDT recording, tracking pathway handovers using THL Ohjaus 21/2016 definitions, and standardising referral criteria and diagnostic care coordination.** `cty:no_treatment_record:Varsinais_Suomen_hyvinvointialue, q:950a2f797b, thl:21_2016, q:37bb4c3b38, q:fc81032a80`

- Given the 43.1% share with no treatment record within 12 months, 1.6% MDT recording, and incomplete lung cancer data collection nationally, the county should audit and publish recording completeness for treatments, stage, and MDT coding using uniform recording instructions, while the roadmap plans a national quality registry with 90% coverage including stage. `cty:no_treatment_record:Varsinais_Suomen_hyvinvointialue, cty:mdt_recorded:Varsinais_Suomen_hyvinvointialue, q:950a2f797b, q:4c7a01d84c, q:990a0d39a0, q:f07a34a300, q:4a856bd695`
- Because the Health Care Act sets no legal maximum time for a cancer suspicion and Finland lacks uniform national access-time monitoring, the county should monitor referral-to-treatment handovers using THL guidance Ohjaus 21/2016 definitions for 16 cancers now, as the Filha programme's diagnostics recommendation with recommended time limits is due before the 2030 mid-term evaluation. `law:no_max, q:4e702a20fe, thl:21_2016, q:24169121a4, q:8f358a9de6, q:614febebf2`
- Because mentor insight indicates that a weak referral gets a lower urgency rating in specialist care and occupational health gets patients to specialist care faster, the county should adopt standardised primary care referral criteria, symptom-based models, and a designated care coordinator now, while the roadmap plans national coordinator guidelines in 2026–2028 for county adoption in 2029–2031. `mentor:kaisa_referral, mentor:hanna_occupational, q:37bb4c3b38, q:29b792498e, q:0780bf74b0, q:fc81032a80, q:74a8cee731, q:abcbb06ae3`

## Review flags (for human review only)

_Flags are for human review only; they never change the brief's status or approve it._

- none

## Claims cited

- `bs:coverage:Diagnosis` (verified locally): Pathway stage 'Diagnosis' is measured in public data: yes (by county: yes (Kuva 7, 10, 13: PNG only)) — keuhkosyoparaportti_2019_2023.html, §4.1, Taulukko 2–4, Kuva 5–13
- `bs:coverage:First_specialist_visit` (verified locally): Pathway stage 'First specialist visit' is measured in public data: partly (by county: no) — keuhkosyoparaportti_2019_2023.html, §3.1, §4.2, Taulukko 5
- `bs:coverage:Imaging` (verified locally): Pathway stage 'Imaging' is measured in public data: partly (by county: partly (Kuva 7, PNG only)) — keuhkosyoparaportti_2019_2023.html, §4.1.1, Taulukko 2, Kuva 5–7
- `bs:coverage:MDT` (verified locally): Pathway stage 'MDT' is measured in public data: partly (by county: yes (Taulukko 11)) — keuhkosyoparaportti_2019_2023.html, §3.3, §4.2, Taulukko 5, 10, 11, 13
- `bs:coverage:Primary_care_occupational_health` (verified locally): Pathway stage 'Primary care / occupational health' is measured in public data: no (by county: no) — keuhkosyoparaportti_2019_2023.html, §3.3
- `bs:coverage:Referral` (verified locally): Pathway stage 'Referral' is measured in public data: no (by county: no) — keuhkosyoparaportti_2019_2023.html, whole report (no relevant data found)
- `bs:coverage:Symptoms` (verified locally): Pathway stage 'Symptoms' is measured in public data: no (by county: no) — keuhkosyoparaportti_2019_2023.html, whole report (no relevant data found)
- `bs:coverage:Treatment_start` (verified locally): Pathway stage 'Treatment start' is measured in public data: partly (by county: yes (type only, Taulukko 11)) — keuhkosyoparaportti_2019_2023.html, §4.2, §4.2.2, Taulukko 6–9, 11, 12, Kuva 14, 17
- `cty:curative:Varsinais_Suomen_hyvinvointialue` (verified locally): Varsinais-Suomen hyvinvointialue: curative treatment 24.3% (95% CI 22.1–26.6; n=349/1437), below vs national 27.0% — keuhkosyoparaportti_2019_2023.html, Taulukko 11
- `cty:life_prolonging:Varsinais_Suomen_hyvinvointialue` (verified locally): Varsinais-Suomen hyvinvointialue: life-prolonging treatment 9.7% (95% CI 8.3–11.4; n=140/1437), below vs national 30.4% — keuhkosyoparaportti_2019_2023.html, Taulukko 11
- `cty:mdt_recorded:Varsinais_Suomen_hyvinvointialue` (verified locally): Varsinais-Suomen hyvinvointialue: MDT meeting recorded 1.6% (95% CI 1.1–2.4; n=23/1437), below vs national 6.0% — keuhkosyoparaportti_2019_2023.html, Taulukko 11
- `cty:no_treatment_record:Varsinais_Suomen_hyvinvointialue` (verified locally): Varsinais-Suomen hyvinvointialue: no treatment record within 12 months 43.1% (95% CI 40.5–45.6; n=619/1437), above vs national 27.5% — keuhkosyoparaportti_2019_2023.html, Taulukko 11
- `cty:symptomatic:Varsinais_Suomen_hyvinvointialue` (verified locally): Varsinais-Suomen hyvinvointialue: symptomatic treatment 30.8% (95% CI 28.5–33.3; n=443/1437), below vs national 39.5% — keuhkosyoparaportti_2019_2023.html, Taulukko 11
- `k16:curative:men:Varsinais_Suomen_hyvinvointialue` (verified locally): Varsinais-Suomen hyvinvointialue: age-adjusted curative treatment share, men, 22.7% — keuhkosyoparaportti_2019_2023.html, Kuva 16
- `k16:curative:men:national` (verified locally): Finland (national reference line): age-adjusted curative treatment share, men, 26.7% — keuhkosyoparaportti_2019_2023.html, Kuva 16
- `k16:curative:women:Varsinais_Suomen_hyvinvointialue` (verified locally): Varsinais-Suomen hyvinvointialue: age-adjusted curative treatment share, women, 27.4% (95% CI 23.1–31.8) — keuhkosyoparaportti_2019_2023.html, Kuva 16
- `k16:curative:women:national` (verified locally): Finland (national reference line): age-adjusted curative treatment share, women, 26.9% — keuhkosyoparaportti_2019_2023.html, Kuva 16
- `law:no_max` (verified by Hellu): There is no legal maximum time for a cancer suspicion — pathway_brief.md, 5. What the law guarantees (Health Care Act, §52)
- `lit:hilmo_90` (verified by Hellu): HILMO diagnoses match the Cancer Registry for about 90% of most cancer types — pathway_brief.md, 6. Regional pathways compared
- `mentor:hanna_occupational` (mentor insight): Occupational health gets patients to specialist care faster — pathway_brief.md, 7. Where patients get stuck
- `mentor:kaisa_referral` (mentor insight): A weak referral gets a lower urgency rating in specialist care — pathway_brief.md, 7. Where patients get stuck
- `mot:patient` (preliminary): Patient delay (symptoms to first contact): 56 days — pathway_brief.md, 7. Where patients get stuck
- `mot:primary` (preliminary): Primary care interval: 41 days — pathway_brief.md, 7. Where patients get stuck
- `mot:specialist` (preliminary): Specialist care interval: 58 days, the longest stage — pathway_brief.md, 7. Where patients get stuck
- `mot:total_dk` (preliminary): Symptoms to first treatment, Denmark: 67 days — pathway_brief.md, 1. Key points
- `mot:total_fi` (preliminary): Symptoms to first treatment, Finland: 155 days on average — pathway_brief.md, 1. Key points
- `mot:total_se` (preliminary): Symptoms to first treatment, Sweden: 107 days — pathway_brief.md, 1. Key points
- `nat:curative` (verified locally): Finland: curative treatment 27.0% (4009/14873), 2019–2023 — keuhkosyoparaportti_2019_2023.html, Taulukko 6
- `nat:life_prolonging` (verified locally): Finland: life-prolonging treatment 30.4% (4522/14873), 2019–2023 — keuhkosyoparaportti_2019_2023.html, Taulukko 6
- `nat:mdt_recorded` (verified locally): Finland: MDT meeting recorded 6.0% (893/14873), 2019–2023 — keuhkosyoparaportti_2019_2023.html, Taulukko 5
- `nat:no_treatment_record` (verified locally): Finland: no treatment record within 12 months 27.5% (4089/14873), 2019–2023 — keuhkosyoparaportti_2019_2023.html, Taulukko 5
- `nat:symptomatic` (verified locally): Finland: symptomatic treatment 39.5% (5871/14873), 2019–2023 — keuhkosyoparaportti_2019_2023.html, Taulukko 6
- `q:0780bf74b0` (verified locally): Policy evidence for pathway stage 'Symptoms' — roadmap_2026_2031_fi.pdf, p.52; p.53
- `q:24169121a4` (verified locally): Strategy p.5 (= PDF p.5), “Strategiset tavoitteet”, indicator under “Varmistetaan yhdenvertainen ja vaikuttava syövänhoito”: > “Potilaat pääsevät hoitoon tavoiteaikojen puitteissa” > “ THL (Ohjaus 21/2016). Hoitoonpääsyn seuranta syövän hoidossa.” — strategy_2026_2035_fi.pdf, p.5
- `q:29b792498e` (verified locally): Policy evidence for pathway stage 'Referral' — filha_lung_programme_2026_fi.pdf, p.16
- `q:323de0d90d` (verified locally): Report evidence for pathway stage 'Primary care / occupational health' — keuhkosyoparaportti_2019_2023.html, §3.3 Menetelmät
- `q:37bb4c3b38` (verified locally): Policy evidence for pathway stage 'Referral' — roadmap_2026_2031_fi.pdf, p.52; p.106
- `q:39e6ba43a9` (verified locally): Report evidence for pathway stage 'MDT' — keuhkosyoparaportti_2019_2023.html, §3.3 Menetelmät
- `q:4a856bd695` (verified locally): the registry's data, including stage, allows reliable assessment and comparison of quality and effectiveness, with 90% data coverage — roadmap_2026_2031_fi.pdf, p.60
- `q:4c7a01d84c` (verified locally): nationally uniform recording instructions, and their use, must be ensured — filha_lung_programme_2026_fi.pdf, p.21
- `q:4e702a20fe` (verified locally): Finland has no unified national system to steer the drafting of cancer-specific treatment recommendations, or the implementation and monitoring of care pathways based on them (quality and effectiveness targets/indicators, including access to care, and cancer-specific and generic PROMs). Existing recommendations and pathways, and the targets and indicators to be monitored, are not coordinated nationally. This maintains regional inequality in the availability and effectiveness of cancer care. — strategy_2026_2035_fi.pdf, p.33
- `q:614febebf2` (verified locally): When (p.24): > “Väliarvio toteutetaan vuonna 2030, ohjelman puolivälissä ja loppuarviointi vuonna 2036. Eri > osa-alueiden suositukset toteutetaan ennen väliarviointia.” — filha_lung_programme_2026_fi.pdf, p.24
- `q:74a8cee731` (verified locally): The most important thing is that the patient knows who has the overall picture of their care, and how they can contact the treating unit when needed. — roadmap_2026_2031_fi.pdf, p.32
- `q:7885b0974f` (verified locally): Report evidence for pathway stage 'Diagnosis' — keuhkosyoparaportti_2019_2023.html, §4.1.3 Levinneisyystiedon kattavuus
- `q:8f358a9de6` (verified locally): p.16: > “Tämän ohjelman yhtenä toimenpiteenä tuotetaan kansallinen suositus keuhkosyöpien diagnostiikasta. Se > sisältää myös lähetekriteerit perusterveydenhuollolle ja suositellut aikarajat erikoissairaanhoitoon > eri diagnostiikan polun vaiheille.” — filha_lung_programme_2026_fi.pdf, p.16
- `q:950a2f797b` (verified locally): Reporting, collection and storage of lung cancer data is currently incomplete. — filha_lung_programme_2026_fi.pdf, p.21
- `q:990a0d39a0` (verified locally): Policy evidence for pathway stage 'MDT' — roadmap_2026_2031_fi.pdf, p.56
- `q:abcbb06ae3` (verified locally): 2026–2028: guidance on a named doctor, nurse or specialist worker coordinating cancer care. 2029–2031: wellbeing services counties have adopted it. — roadmap_2026_2031_fi.pdf, p.32
- `q:f07a34a300` (verified locally): A national cancer care quality registry will be set up alongside THL's Cancer Registry. — roadmap_2026_2031_fi.pdf, p.59
- `q:fc81032a80` (verified locally): Measure 1.2.3: Create an operating model and guidance for a named worker responsible for coordinating cancer care. — roadmap_2026_2031_fi.pdf, p.32
- `thl:21_2016` (verified by Hellu): THL Ohjaus 21/2016 defines how cancer access times are recorded, for 16 cancers — pathway_brief.md, 6. Regional pathways compared
