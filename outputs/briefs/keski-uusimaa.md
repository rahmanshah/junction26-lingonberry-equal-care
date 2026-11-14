# Keski-Uusimaa: lung cancer pathway brief

Status: **validated** · gemini-4-argon (thinking HIGH) · 2026-11-14T12:02:28+00:00 · attempts: 1

## Where do we lag?

**Keski-Uusimaa lags nationally in crude MDT recording at 0.0% (95% CI 0.0–0.8) versus 6.0%, while crude curative treatment is 33.7% (95% CI 29.6–38.0) versus 27.0%.** `cty:mdt_recorded:Keski_Uudenmaan_hyvinvointialue, nat:mdt_recorded, cty:curative:Keski_Uudenmaan_hyvinvointialue, nat:curative`

- In Keski-Uusimaa, the crude recorded MDT meeting share is 0.0% (95% CI 0.0–0.8; n=0/481) compared with 6.0% (893/14873) nationally; the 95% confidence interval excludes the national value, though HILMO entries come only from direct patient contacts and measure recording practice, not care. `cty:mdt_recorded:Keski_Uudenmaan_hyvinvointialue, nat:mdt_recorded, bs:coverage:MDT, q:39e6ba43a9`
- Across overlapping treatment categories where a patient can have several treatments, Keski-Uusimaa's crude curative share is 33.7% (95% CI 29.6–38.0; n=162/481) versus 27.0% (4009/14873) nationally, and its 95% confidence interval excludes the national value. `cty:curative:Keski_Uudenmaan_hyvinvointialue, nat:curative`
- The county's crude life-prolonging treatment share is 28.9% (95% CI 25.0–33.1; n=139/481) versus 30.4% (4522/14873) nationally, and its crude symptomatic treatment share is 39.5% (95% CI 35.2–43.9; n=190/481) versus 39.5% (5871/14873) nationally; their 95% confidence intervals include the national values. `cty:life_prolonging:Keski_Uudenmaan_hyvinvointialue, nat:life_prolonging, cty:symptomatic:Keski_Uudenmaan_hyvinvointialue, nat:symptomatic`
- Public data do not measure county waiting times, while preliminary, unpublished national figures average 155 days from symptoms to treatment in Finland versus 107 days in Sweden and 67 days in Denmark, with 56 days of patient delay, 41 days in primary care, and 58 days in specialist care. `bs:coverage:Referral, bs:coverage:First_specialist_visit, bs:coverage:Treatment_start, mot:total_fi, mot:total_se, mot:total_dk, mot:patient, mot:primary, mot:specialist`

## How sure are we?

**Keski-Uusimaa's crude 26.4% (95% CI 22.7–30.5) no-treatment-record share versus 27.5% nationally suggests relatively complete treatment recording, but county shares lack age and stage adjustment and pathway timestamps.** `cty:no_treatment_record:Keski_Uudenmaan_hyvinvointialue, nat:no_treatment_record, bs:coverage:Diagnosis, bs:coverage:Treatment_start`

- The crude share with no treatment record within 12 months is 26.4% (95% CI 22.7–30.5; n=127/481) versus 27.5% (4089/14873) nationally, with the 95% confidence interval including 27.5%; this mixes untreated patients and treatment that was not recorded, and as an inference, a data-quality signal below 27.5% is consistent with relatively complete treatment recording, not direct evidence. `cty:no_treatment_record:Keski_Uudenmaan_hyvinvointialue, nat:no_treatment_record, bs:coverage:Treatment_start`
- County shares are crude and not adjusted for age or stage; stage at diagnosis is missing for a large share of new patients nationally, and while Kuva 16 provides digitised national age-adjusted curative reference lines of 26.7% for men and 26.9% for women (±0.5 percentage points precision), no county age-adjusted figure is available here. `bs:coverage:Diagnosis, q:7885b0974f, k16:curative:men:national, k16:curative:women:national`
- A journal article reports that HILMO hospital discharge diagnoses match the Cancer Registry for about 90% of most cancer types, but this concerns diagnosis concordance only and says nothing about how completely treatment, referrals, or MDT meetings are recorded. `lit:hilmo_90, q:950a2f797b`
- Public report data do not measure symptom onset or referrals, primary care visits are not included in the report's data and occupational health is not mentioned, imaging appears only indirectly as the diagnostic basis in approximately 20% of cases nationally, and specialist visits and treatments lack county waiting-time timestamps. `bs:coverage:Symptoms, bs:coverage:Referral, bs:coverage:Primary_care_occupational_health, q:323de0d90d, bs:coverage:Imaging, q:5eb155decc, bs:coverage:First_specialist_visit, bs:coverage:Treatment_start`

## What should we do first?

**The team recommends publishing county recording completeness for MDT, stage, and drug treatment, reporting access times using THL 21/2016 definitions, and standardising referrals and diagnostic coordination.** `rec:3, rec:1, rec:2, thl:21_2016, q:950a2f797b`

- Given Keski-Uusimaa's crude recorded MDT share of 0.0% (95% CI 0.0–0.8; n=0/481) versus 6.0% (893/14873) nationally and incomplete national stage and lung cancer data, the team recommends publishing county recording completeness for stage, drug treatment, and MDT coding while reading gaps as data-quality signals, as the roadmap plans a quality registry with 90% coverage including stage. `rec:3, cty:mdt_recorded:Keski_Uudenmaan_hyvinvointialue, nat:mdt_recorded, q:7885b0974f, q:950a2f797b, q:f07a34a300, q:4a856bd695`
- Because the Health Care Act sets no legal maximum time for a cancer suspicion, the team recommends reporting access times using THL guidance Ohjaus 21/2016 definitions for 16 cancers and flagging stalled handovers, while the roadmap plans national target access times in 2026–2028 and the Filha programme's diagnostics guideline is due before the 2030 interim evaluation. `rec:1, law:no_max, thl:21_2016, q:def306014c, q:8f358a9de6, q:614febebf2`
- Because referral instructions vary by county and mentor insight notes that weak referrals receive lower urgency ratings in specialist care, the team recommends a standard referral template, pulmonologist referral for persistent symptoms despite a normal X-ray, and a named diagnostic-phase contact person, while the roadmap plans standardised referral criteria and care-coordinator guidance in 2026–2028. `rec:2, q:556431a0c2, q:82b59905ad, mentor:kaisa_referral, q:c61439b30f, q:abcbb06ae3`

## Review flags (for human review only)

_Flags are for human review only; they never change the brief's status or approve it._

- [medium] `how_sure_are_we.headline`: Overreach: the cited claim [cty:no_treatment_record:Keski_Uudenmaan_hyvinvointialue] states that 26.4% (95% CI 22.7–30.5) is not distinguishable from the national 27.5%, and [bs:coverage:Treatment_start] notes that the 27.5% share mixes untreated patients with unrecorded treatment; neither claim supports the conclusion that 26.4% versus 27.5% suggests relatively complete treatment recording.
- [medium] `how_sure_are_we.details[0]`: Overreach: even framed as an inference, the cited claims do not support treating the county figure as a signal below 27.5% or consistent with relatively complete treatment recording, since [cty:no_treatment_record:Keski_Uudenmaan_hyvinvointialue] states it is not distinguishable from 27.5% and [bs:coverage:Treatment_start] notes that the 27.5% rate mixes untreated patients and unrecorded treatment.
- [low] `how_sure_are_we.details[3]`: Minor imprecision in measure: [bs:coverage:Imaging] and [q:5eb155decc] state that approximately 20% is the share based on clinical examination alone, such as imaging, rather than imaging alone.
- [low] `what_to_do_first.details[1]`: Plan presented with certainty: stating that the Filha programme's diagnostics guideline "is due" before the 2030 interim evaluation frames a future programme plan from [q:8f358a9de6] and [q:614febebf2] as a fixed deadline rather than something the programme plans or intends.

## Claims cited

- `bs:coverage:Diagnosis` (verified locally): Pathway stage 'Diagnosis' is measured in public data: yes (by county: yes (Kuva 7, 10, 13: PNG only)) — keuhkosyoparaportti_2019_2023.html, §4.1, Taulukko 2–4, Kuva 5–13
- `bs:coverage:First_specialist_visit` (verified locally): Pathway stage 'First specialist visit' is measured in public data: partly (by county: no) — keuhkosyoparaportti_2019_2023.html, §3.1, §4.2, Taulukko 5
- `bs:coverage:Imaging` (verified locally): Pathway stage 'Imaging' is measured in public data: partly (by county: partly (Kuva 7, PNG only)) — keuhkosyoparaportti_2019_2023.html, §4.1.1, Taulukko 2, Kuva 5–7
- `bs:coverage:MDT` (verified locally): Pathway stage 'MDT' is measured in public data: partly (by county: yes (Taulukko 11)) — keuhkosyoparaportti_2019_2023.html, §3.3, §4.2, Taulukko 5, 10, 11, 13
- `bs:coverage:Primary_care_occupational_health` (verified locally): Pathway stage 'Primary care / occupational health' is measured in public data: no (by county: no) — keuhkosyoparaportti_2019_2023.html, §3.3
- `bs:coverage:Referral` (verified locally): Pathway stage 'Referral' is measured in public data: no (by county: no) — keuhkosyoparaportti_2019_2023.html, whole report (no relevant data found)
- `bs:coverage:Symptoms` (verified locally): Pathway stage 'Symptoms' is measured in public data: no (by county: no) — keuhkosyoparaportti_2019_2023.html, whole report (no relevant data found)
- `bs:coverage:Treatment_start` (verified locally): Pathway stage 'Treatment start' is measured in public data: partly (by county: yes (type only, Taulukko 11)) — keuhkosyoparaportti_2019_2023.html, §4.2, §4.2.2, Taulukko 6–9, 11, 12, Kuva 14, 17
- `cty:curative:Keski_Uudenmaan_hyvinvointialue` (verified locally): Keski-Uudenmaan hyvinvointialue: curative treatment 33.7% (95% CI 29.6–38.0; n=162/481), above vs national 27.0% — keuhkosyoparaportti_2019_2023.html, Taulukko 11
- `cty:life_prolonging:Keski_Uudenmaan_hyvinvointialue` (verified locally): Keski-Uudenmaan hyvinvointialue: life-prolonging treatment 28.9% (95% CI 25.0–33.1; n=139/481), not distinguishable vs national 30.4% — keuhkosyoparaportti_2019_2023.html, Taulukko 11
- `cty:mdt_recorded:Keski_Uudenmaan_hyvinvointialue` (verified locally): Keski-Uudenmaan hyvinvointialue: MDT meeting recorded 0.0% (95% CI 0.0–0.8; n=0/481), below vs national 6.0% — keuhkosyoparaportti_2019_2023.html, Taulukko 11
- `cty:no_treatment_record:Keski_Uudenmaan_hyvinvointialue` (verified locally): Keski-Uudenmaan hyvinvointialue: no treatment record within 12 months 26.4% (95% CI 22.7–30.5; n=127/481), not distinguishable vs national 27.5% — keuhkosyoparaportti_2019_2023.html, Taulukko 11
- `cty:symptomatic:Keski_Uudenmaan_hyvinvointialue` (verified locally): Keski-Uudenmaan hyvinvointialue: symptomatic treatment 39.5% (95% CI 35.2–43.9; n=190/481), not distinguishable vs national 39.5% — keuhkosyoparaportti_2019_2023.html, Taulukko 11
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
- `q:323de0d90d` (verified locally): Report evidence for pathway stage 'Primary care / occupational health' — keuhkosyoparaportti_2019_2023.html, §3.3 Menetelmät
- `q:39e6ba43a9` (verified locally): Report evidence for pathway stage 'MDT' — keuhkosyoparaportti_2019_2023.html, §3.3 Menetelmät
- `q:4a856bd695` (verified locally): the registry's data, including stage, allows reliable assessment and comparison of quality and effectiveness, with 90% data coverage — roadmap_2026_2031_fi.pdf, p.60
- `q:556431a0c2` (verified locally): the patient is referred to specialist care according to local instructions — filha_lung_programme_2026_fi.pdf, p.15
- `q:5eb155decc` (verified locally): Report evidence for pathway stage 'Imaging' — keuhkosyoparaportti_2019_2023.html, §4.1.1 Toteamistapa
- `q:614febebf2` (verified locally): When (p.24): > “Väliarvio toteutetaan vuonna 2030, ohjelman puolivälissä ja loppuarviointi vuonna 2036. Eri > osa-alueiden suositukset toteutetaan ennen väliarviointia.” — filha_lung_programme_2026_fi.pdf, p.24
- `q:7885b0974f` (verified locally): Report evidence for pathway stage 'Diagnosis' — keuhkosyoparaportti_2019_2023.html, §4.1.3 Levinneisyystiedon kattavuus
- `q:82b59905ad` (verified locally): the organisation of care varies by wellbeing services county — filha_lung_programme_2026_fi.pdf, p.15
- `q:8f358a9de6` (verified locally): p.16: > “Tämän ohjelman yhtenä toimenpiteenä tuotetaan kansallinen suositus keuhkosyöpien diagnostiikasta. Se > sisältää myös lähetekriteerit perusterveydenhuollolle ja suositellut aikarajat erikoissairaanhoitoon > eri diagnostiikan polun vaiheille.” — filha_lung_programme_2026_fi.pdf, p.16
- `q:950a2f797b` (verified locally): Reporting, collection and storage of lung cancer data is currently incomplete. — filha_lung_programme_2026_fi.pdf, p.21
- `q:abcbb06ae3` (verified locally): 2026–2028: guidance on a named doctor, nurse or specialist worker coordinating cancer care. 2029–2031: wellbeing services counties have adopted it. — roadmap_2026_2031_fi.pdf, p.32
- `q:c61439b30f` (verified locally): 2026–2028: standardised referral criteria and symptom-based models included in the national pathways of at least the five most common cancers. — roadmap_2026_2031_fi.pdf, p.53
- `q:def306014c` (verified locally): p.57, timetable: > “2026–2028: Kansalliset hoitoketjukuvaukset tehty viidestä syövästä ja syöpäkohtaiset > hoitoonpääsyajat on määritetty.” — roadmap_2026_2031_fi.pdf, p.57
- `q:f07a34a300` (verified locally): A national cancer care quality registry will be set up alongside THL's Cancer Registry. — roadmap_2026_2031_fi.pdf, p.59
- `rec:1` (recommendation (ours)): Team recommendation 1: Counties report access times using the THL 21/2016 definitions, with handover alerts. Each wellbeing services county reports lung cancer access times (referral → first specialist visit → diagnosis → treatment start) using the definitions in THL's Hoitoonpääsyn seuranta syövän hoidossa (Ohjaus 21/2016). Until national target times exist, flag stalled handovers. — recommendations.md, §1. Counties report access times using the THL 21/2016 definitions, with handover alerts
- `rec:2` (recommendation (ours)): Team recommendation 2: A KYS-style referral template, a persistent-symptoms rule and a named contact. Adopt a standard referral content list and template, modelled on KYS. • Add a rule for primary care: if symptoms persist after a normal X-ray, refer for a pulmonologist assessment. • Name a contact person for the diagnostic phase, from referral to diagnosis. — recommendations.md, §2. A KYS-style referral template, a persistent-symptoms rule and a named contact
- `rec:3` (recommendation (ours)): Team recommendation 3: Report recording completeness per county: stage, drug treatment, MDT coding. Publish, per county, how completely stage, drug treatment and MDT meetings are recorded. Read county ‘gaps’ in these fields as data-quality signals first. — recommendations.md, §3. Report recording completeness per county: stage, drug treatment, MDT coding
- `thl:21_2016` (verified by Hellu): THL Ohjaus 21/2016 defines how cancer access times are recorded, for 16 cancers — pathway_brief.md, 6. Regional pathways compared
