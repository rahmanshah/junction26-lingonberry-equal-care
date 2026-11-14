# Satakunta: lung cancer pathway brief

Status: **validated** · gemini-4-argon (thinking HIGH) · 2026-11-14T13:04:20+00:00 · attempts: 1

## Where do we lag?

**In Satakunta, crude shares across overlapping treatment categories lag national values for recorded MDT meetings and symptomatic treatment, while a regional study found the biggest diagnostic delay in specialist care.** `cty:mdt_recorded:Satakunnan_hyvinvointialue, cty:symptomatic:Satakunnan_hyvinvointialue, reg:satakunta_study`

- In Satakunta, the crude curative treatment share is 24.5% (95% CI 21.4–27.9; n=167/682), whose 95% confidence interval includes the national 27.0% (4009/14873) in 2019–2023. `cty:curative:Satakunnan_hyvinvointialue, nat:curative`
- In these overlapping treatment categories where a patient can have several, the crude symptomatic treatment share is 29.0% (95% CI 25.8–32.5; n=198/682), whose 95% confidence interval excludes and lies below the national 39.5% (5871/14873), whereas crude life-prolonging treatment is 45.0% (95% CI 41.3–48.8; n=307/682), above the national 30.4% (4522/14873). `cty:symptomatic:Satakunnan_hyvinvointialue, nat:symptomatic, cty:life_prolonging:Satakunnan_hyvinvointialue, nat:life_prolonging`
- Across overlapping categories, Satakunta's crude share with a recorded MDT meeting is 0.6% (95% CI 0.2–1.5; n=4/682), whose 95% confidence interval excludes the national 6.0% (893/14873), while the crude share with no treatment record within 12 months is 29.8% (95% CI 26.4–33.3; n=203/682), whose 95% confidence interval includes the national 27.5% (4089/14873). `cty:mdt_recorded:Satakunnan_hyvinvointialue, nat:mdt_recorded, cty:no_treatment_record:Satakunnan_hyvinvointialue, nat:no_treatment_record`
- A University of Turku regional study in Satakunta found referral to diagnosis took just under two months with the biggest delay in specialist care, while preliminary national averages show 155 days from symptoms to treatment in Finland (107 in Sweden, 67 in Denmark): 58 days in specialist care, 41 days in primary care and 56 days of patient delay. `reg:satakunta_study, mot:total_fi, mot:total_se, mot:total_dk, mot:specialist, mot:primary, mot:patient`

## How sure are we?

**Public data show where 95% confidence intervals for crude county shares exclude national values, but lack age and stage adjustment and omit pathway timestamps and pre-specialist stages.** `cty:curative:Satakunnan_hyvinvointialue, bs:coverage:Diagnosis, bs:coverage:Referral, bs:coverage:Treatment_start`

- County shares are crude, with separate limitations: they are not age-adjusted, as age-adjusted values exist only in Kuva 16 for curative treatment by sex (digitised from a figure at ±0.5 percentage points precision; dashed national reference lines 26.7% for men, 26.9% for women), and separately they cannot be stage-adjusted because stage at diagnosis is missing for about 48% of patients. `cty:curative:Satakunnan_hyvinvointialue, k16:curative:men:national, k16:curative:women:national, bs:coverage:Diagnosis, q:7885b0974f`
- A journal article found HILMO diagnoses match the Cancer Registry for about 90% of most cancer types, but across overlapping categories, Satakunta's crude 0.6% (95% CI 0.2–1.5) MDT share measures recording practice (HILMO captures direct patient contacts only), and the crude 29.8% (95% CI 26.4–33.3) with no treatment record within 12 months mixes untreated patients and unrecorded treatment. `lit:hilmo_90, cty:mdt_recorded:Satakunnan_hyvinvointialue, bs:coverage:MDT, q:39e6ba43a9, cty:no_treatment_record:Satakunnan_hyvinvointialue, bs:coverage:Treatment_start`
- Public data do not measure symptoms or referral dates, do not include primary care visits in the report's data or mention occupational health, note imaging only where diagnosis rests on clinical examination alone (about 20% of patients), and record whether a specialist visit (93.6% nationally) or treatment occurred within 12 months but not when it started. `bs:coverage:Symptoms, bs:coverage:Referral, bs:coverage:Primary_care_occupational_health, q:323de0d90d, bs:coverage:Imaging, q:5eb155decc, bs:coverage:First_specialist_visit, bs:coverage:Treatment_start`

## What should we do first?

**The team recommends that Satakunta report THL 21/2016 access times with handover alerts, standardise referrals with a named diagnostic contact, and publish stage, drug and MDT recording.** `rec:1, rec:2, rec:3, thl:21_2016`

- Because a University of Turku regional study of Satakunta found the biggest delay in specialist care and the Health Care Act sets no maximum wait for cancer suspicion, the team recommends reporting THL Ohjaus 21/2016 access times for 16 cancers and flagging stalled handovers; the STM roadmap (measure 3.1.2) plans national pathways and access times for five cancers by 2026–2028. `rec:1, reg:satakunta_study, law:no_max, thl:21_2016, q:def306014c, q:b326e35410`
- Because referrals follow local instructions and mentor insight notes weak referrals get lower urgency ratings, the team recommends a KYS-style referral template, pulmonologist referral for persistent symptoms after a normal X-ray, and a named diagnostic contact; the Filha programme's diagnostics recommendation with primary-care referral criteria and recommended time limits is to be carried out before the 2030 mid-term evaluation. `rec:2, q:556431a0c2, mentor:kaisa_referral, q:29b792498e, q:432c0e51d6, q:614febebf2`
- With stage missing for about 48% of patients, incomplete data reporting, and Satakunta's crude 0.6% (95% CI 0.2–1.5; n=4/682) recorded MDT share versus 6.0% nationally, the team recommends publishing per county how completely stage, drug treatment and MDT meetings are recorded and reading gaps as data-quality signals; the STM roadmap (measure 3.2.1) plans a national quality registry by 2026–2028. `rec:3, bs:coverage:Diagnosis, q:7885b0974f, q:950a2f797b, cty:mdt_recorded:Satakunnan_hyvinvointialue, nat:mdt_recorded, q:f07a34a300`

## Review flags (for human review only)

_Flags are for human review only; they never change the brief's status or approve it._

- [medium] `where_we_lag.details[0]`: Missing caveat: the cited claim [cty:curative:Satakunnan_hyvinvointialue] notes that treatment categories overlap, which is not stated in this sentence.
- [medium] `what_to_do_first.details[0]`: Overreach: [rec:1] recommends reporting lung cancer access times using THL Ohjaus 21/2016 definitions, whereas [thl:21_2016] states that THL Ohjaus 21/2016 defines how access times are recorded for 16 cancers; the team did not recommend reporting all 16 cancers.
- [medium] `what_to_do_first.details[2]`: Misleading timeline and missing caveat: [q:f07a34a300] notes that STM roadmap measure 3.2.1 updates the registry decree by 2026–2028 and schedules annual reports for at least five cancers by 2029–2031, rather than completing the national quality registry itself by 2026–2028; also [cty:mdt_recorded:Satakunnan_hyvinvointialue] notes that categories overlap, which is omitted.

## Claims cited

- `bs:coverage:Diagnosis` (verified locally): Pathway stage 'Diagnosis' is measured in public data: yes (by county: yes (Kuva 7, 10, 13: PNG only)) — keuhkosyoparaportti_2019_2023.html, §4.1, Taulukko 2–4, Kuva 5–13
- `bs:coverage:First_specialist_visit` (verified locally): Pathway stage 'First specialist visit' is measured in public data: partly (by county: no) — keuhkosyoparaportti_2019_2023.html, §3.1, §4.2, Taulukko 5
- `bs:coverage:Imaging` (verified locally): Pathway stage 'Imaging' is measured in public data: partly (by county: partly (Kuva 7, PNG only)) — keuhkosyoparaportti_2019_2023.html, §4.1.1, Taulukko 2, Kuva 5–7
- `bs:coverage:MDT` (verified locally): Pathway stage 'MDT' is measured in public data: partly (by county: yes (Taulukko 11)) — keuhkosyoparaportti_2019_2023.html, §3.3, §4.2, Taulukko 5, 10, 11, 13
- `bs:coverage:Primary_care_occupational_health` (verified locally): Pathway stage 'Primary care / occupational health' is measured in public data: no (by county: no) — keuhkosyoparaportti_2019_2023.html, §3.3
- `bs:coverage:Referral` (verified locally): Pathway stage 'Referral' is measured in public data: no (by county: no) — keuhkosyoparaportti_2019_2023.html, whole report (no relevant data found)
- `bs:coverage:Symptoms` (verified locally): Pathway stage 'Symptoms' is measured in public data: no (by county: no) — keuhkosyoparaportti_2019_2023.html, whole report (no relevant data found)
- `bs:coverage:Treatment_start` (verified locally): Pathway stage 'Treatment start' is measured in public data: partly (by county: yes (type only, Taulukko 11)) — keuhkosyoparaportti_2019_2023.html, §4.2, §4.2.2, Taulukko 6–9, 11, 12, Kuva 14, 17
- `cty:curative:Satakunnan_hyvinvointialue` (verified locally): Satakunnan hyvinvointialue: curative treatment 24.5% (95% CI 21.4–27.9; n=167/682), not distinguishable vs national 27.0% — keuhkosyoparaportti_2019_2023.html, Taulukko 11
- `cty:life_prolonging:Satakunnan_hyvinvointialue` (verified locally): Satakunnan hyvinvointialue: life-prolonging treatment 45.0% (95% CI 41.3–48.8; n=307/682), above vs national 30.4% — keuhkosyoparaportti_2019_2023.html, Taulukko 11
- `cty:mdt_recorded:Satakunnan_hyvinvointialue` (verified locally): Satakunnan hyvinvointialue: MDT meeting recorded 0.6% (95% CI 0.2–1.5; n=4/682), below vs national 6.0% — keuhkosyoparaportti_2019_2023.html, Taulukko 11
- `cty:no_treatment_record:Satakunnan_hyvinvointialue` (verified locally): Satakunnan hyvinvointialue: no treatment record within 12 months 29.8% (95% CI 26.4–33.3; n=203/682), not distinguishable vs national 27.5% — keuhkosyoparaportti_2019_2023.html, Taulukko 11
- `cty:symptomatic:Satakunnan_hyvinvointialue` (verified locally): Satakunnan hyvinvointialue: symptomatic treatment 29.0% (95% CI 25.8–32.5; n=198/682), below vs national 39.5% — keuhkosyoparaportti_2019_2023.html, Taulukko 11
- `k16:curative:men:national` (verified locally): Finland (national reference line): age-adjusted curative treatment share, men, 26.7% — keuhkosyoparaportti_2019_2023.html, Kuva 16
- `k16:curative:women:national` (verified locally): Finland (national reference line): age-adjusted curative treatment share, women, 26.9% — keuhkosyoparaportti_2019_2023.html, Kuva 16
- `law:no_max` (verified by Hellu): There is no legal maximum time for a cancer suspicion — pathway_brief.md, 5. What the law guarantees (Health Care Act, §52)
- `lit:hilmo_90` (verified by Hellu): HILMO diagnoses match the Cancer Registry for about 90% of most cancer types — pathway_brief.md, 6. Regional pathways compared
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
- `q:29b792498e` (verified locally): Policy evidence for pathway stage 'Referral' — filha_lung_programme_2026_fi.pdf, p.16
- `q:323de0d90d` (verified locally): Report evidence for pathway stage 'Primary care / occupational health' — keuhkosyoparaportti_2019_2023.html, §3.3 Menetelmät
- `q:39e6ba43a9` (verified locally): Report evidence for pathway stage 'MDT' — keuhkosyoparaportti_2019_2023.html, §3.3 Menetelmät
- `q:432c0e51d6` (verified locally): The upcoming national diagnostics recommendation will include “suositellut aikarajat erikoissairaanhoitoon eri diagnostiikan polun vaiheille” (recommended time limits in specialist care), to be carried out (“toteutetaan”; may mean produced or implemented) before the 2030 mid-term evaluation — filha_lung_programme_2026_fi.pdf, p.16
- `q:556431a0c2` (verified locally): the patient is referred to specialist care according to local instructions — filha_lung_programme_2026_fi.pdf, p.15
- `q:5eb155decc` (verified locally): Report evidence for pathway stage 'Imaging' — keuhkosyoparaportti_2019_2023.html, §4.1.1 Toteamistapa
- `q:614febebf2` (verified locally): When (p.24): > “Väliarvio toteutetaan vuonna 2030, ohjelman puolivälissä ja loppuarviointi vuonna 2036. Eri > osa-alueiden suositukset toteutetaan ennen väliarviointia.” — filha_lung_programme_2026_fi.pdf, p.24
- `q:7885b0974f` (verified locally): Report evidence for pathway stage 'Diagnosis' — keuhkosyoparaportti_2019_2023.html, §4.1.3 Levinneisyystiedon kattavuus
- `q:950a2f797b` (verified locally): Reporting, collection and storage of lung cancer data is currently incomplete. — filha_lung_programme_2026_fi.pdf, p.21
- `q:b326e35410` (verified locally): National pathways with “syöpäkohtaiset hoitoonpääsyajat” for five (unnamed) cancers in 2026–2028, Nordic model — roadmap_2026_2031_fi.pdf, p.57
- `q:def306014c` (verified locally): p.57, timetable: > “2026–2028: Kansalliset hoitoketjukuvaukset tehty viidestä syövästä ja syöpäkohtaiset > hoitoonpääsyajat on määritetty.” — roadmap_2026_2031_fi.pdf, p.57
- `q:f07a34a300` (verified locally): A national cancer care quality registry will be set up alongside THL's Cancer Registry. — roadmap_2026_2031_fi.pdf, p.59
- `rec:1` (recommendation (ours)): Team recommendation 1: Counties report access times using the THL 21/2016 definitions, with handover alerts. Each wellbeing services county reports lung cancer access times (referral → first specialist visit → diagnosis → treatment start) using the definitions in THL's Hoitoonpääsyn seuranta syövän hoidossa (Ohjaus 21/2016). Until national target times exist, flag stalled handovers. — recommendations.md, §1. Counties report access times using the THL 21/2016 definitions, with handover alerts
- `rec:2` (recommendation (ours)): Team recommendation 2: A KYS-style referral template, a persistent-symptoms rule and a named contact. Adopt a standard referral content list and template, modelled on KYS. • Add a rule for primary care: if symptoms persist after a normal X-ray, refer for a pulmonologist assessment. • Name a contact person for the diagnostic phase, from referral to diagnosis. — recommendations.md, §2. A KYS-style referral template, a persistent-symptoms rule and a named contact
- `rec:3` (recommendation (ours)): Team recommendation 3: Report recording completeness per county: stage, drug treatment, MDT coding. Publish, per county, how completely stage, drug treatment and MDT meetings are recorded. Read county ‘gaps’ in these fields as data-quality signals first. — recommendations.md, §3. Report recording completeness per county: stage, drug treatment, MDT coding
- `reg:satakunta_study` (verified by Hellu): Satakunta study: referral to diagnosis just under two months; biggest delay in specialist care — pathway_brief.md, 6. Regional pathways compared
- `thl:21_2016` (verified by Hellu): THL Ohjaus 21/2016 defines how cancer access times are recorded, for 16 cancers — pathway_brief.md, 6. Regional pathways compared
