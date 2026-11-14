# Länsi-Uusimaa: lung cancer pathway brief

Status: **validated** · gemini-4-argon (thinking HIGH) · 2026-11-14T12:02:04+00:00 · attempts: 1

## Where do we lag?

**Länsi-Uusimaa lags nationally in crude life-prolonging treatment (25.2%, 95% CI 22.7–27.9 vs 30.4%) and crude MDT recording (0.2%, 95% CI 0.1–0.7 vs 6.0%).** `cty:life_prolonging:Länsi_Uudenmaan_hyvinvointialue, nat:life_prolonging, cty:mdt_recorded:Länsi_Uudenmaan_hyvinvointialue, nat:mdt_recorded`

- Among patients diagnosed in 2019–2023, the county's crude life-prolonging treatment share is 25.2% (95% CI 22.7–27.9; n=267/1058) compared with 30.4% (4522/14873) nationally, with the 95% confidence interval excluding the national value. `cty:life_prolonging:Länsi_Uudenmaan_hyvinvointialue, nat:life_prolonging`
- Across overlapping treatment categories, the crude curative share is 31.9% (95% CI 29.1–34.7; n=337/1058) versus 27.0% (4009/14873) nationally, excluding the national value, while crude symptomatic care is 40.1% (95% CI 37.2–43.1; n=424/1058) versus 39.5% (5871/14873), with the 95% confidence interval including the national value. `cty:curative:Länsi_Uudenmaan_hyvinvointialue, nat:curative, cty:symptomatic:Länsi_Uudenmaan_hyvinvointialue, nat:symptomatic`
- Multidisciplinary team (MDT) meetings are recorded for a crude 0.2% (95% CI 0.1–0.7; n=2/1058) of county patients versus 6.0% (893/14873) nationally, with the 95% confidence interval excluding the national value, though HILMO captures MDT codes only from direct patient contacts and thus measures recording practice rather than care. `cty:mdt_recorded:Länsi_Uudenmaan_hyvinvointialue, nat:mdt_recorded, bs:coverage:MDT, q:39e6ba43a9`
- A crude 28.5% (95% CI 25.9–31.3; n=302/1058) have no treatment record within 12 months versus 27.5% (4089/14873) nationally (95% confidence interval includes the national value); reading this mix of untreated patients and unrecorded care as a data-quality signal, our inference is that the lower crude life-prolonging share (25.2%, 95% CI 22.7–27.9) may partly reflect unrecorded treatment. `cty:no_treatment_record:Länsi_Uudenmaan_hyvinvointialue, nat:no_treatment_record, cty:life_prolonging:Länsi_Uudenmaan_hyvinvointialue, bs:coverage:Treatment_start`

## How sure are we?

**Public registry tables provide unadjusted 12-month procedure shares, but lack stage adjustment, primary care and referral data, and county-level pathway waiting times.** `bs:coverage:Diagnosis, bs:coverage:Primary_care_occupational_health, bs:coverage:Referral, bs:coverage:Treatment_start`

- County treatment shares in the public report are crude (not adjusted for age or stage) because stage at diagnosis is missing for ~48% of new patients nationally, and age-adjusted figures digitised from Kuva 16 (precision ±0.5 percentage points) provide national reference lines here only for curative treatment (26.7% for men; 26.9% for women). `bs:coverage:Diagnosis, q:7885b0974f, k16:curative:men:national, k16:curative:women:national`
- A journal article indicates that HILMO hospital discharge diagnoses match the Cancer Registry for about 90% of most cancer types, but this concerns diagnosis concordance only and says nothing about treatment, referral, or MDT recording, which the national lung cancer programme notes is currently incomplete. `lit:hilmo_90, q:950a2f797b`
- Public report data do not measure symptom onset or referrals, do not include outpatient primary care visits or mention occupational health, capture imaging only indirectly as the diagnostic basis in approximately 20% of cases, and show whether a specialist visit (93.6%) or treatment occurred within 12 months without start dates. `bs:coverage:Symptoms, bs:coverage:Referral, bs:coverage:Primary_care_occupational_health, q:323de0d90d, bs:coverage:Imaging, q:5eb155decc, bs:coverage:First_specialist_visit, bs:coverage:Treatment_start`
- For pathway delays, only preliminary, unpublished national averages from an Yle MOT study are available: 155 days from symptoms to treatment in Finland (compared with 107 in Sweden and 67 in Denmark), comprising 56 days of patient delay, 41 days in primary care, and 58 days in specialist care. `mot:total_fi, mot:total_se, mot:total_dk, mot:patient, mot:primary, mot:specialist`

## What should we do first?

**The team recommends auditing recording completeness for MDT, stage, and drug treatments, reporting access times using THL Ohjaus 21/2016 guidance definitions, and standardising referrals and diagnostic coordination.** `rec:1, rec:2, rec:3, thl:21_2016, q:950a2f797b`

- Given Länsi-Uusimaa's crude 0.2% (95% CI 0.1–0.7) MDT recording versus 6.0% nationally and crude 25.2% (95% CI 22.7–27.9) life-prolonging share versus 30.4%, the team recommends publishing county recording completeness for stage, drug treatment, and MDT coding while the roadmap plans uniform coding practices and a national quality registry with 90% coverage. `rec:3, cty:mdt_recorded:Länsi_Uudenmaan_hyvinvointialue, nat:mdt_recorded, cty:life_prolonging:Länsi_Uudenmaan_hyvinvointialue, nat:life_prolonging, q:950a2f797b, q:0c7bf2dacb, q:f07a34a300, q:4a856bd695`
- Because the Health Care Act sets no maximum time for a cancer suspicion, the team recommends reporting referral-to-treatment access times and handover alerts using THL Ohjaus 21/2016 guidance definitions for 16 cancers, while the roadmap plans target times by 2026–2028 and the Filha diagnostics recommendation is due before the 2030 evaluation. `rec:1, law:no_max, thl:21_2016, q:24169121a4, q:def306014c, q:8f358a9de6, q:614febebf2`
- Supported by mentor insight that a weak referral gets a lower urgency rating in specialist care and because local referral instructions vary, the team recommends a standard referral template, referring persistent symptoms after a normal X-ray to a pulmonologist, and naming a diagnostic contact, while the roadmap plans standardised referral criteria and care-coordinator guidance by 2026–2028. `rec:2, mentor:kaisa_referral, q:556431a0c2, q:82b59905ad, q:c61439b30f, q:abcbb06ae3`

## Review flags (for human review only)

_Flags are for human review only; they never change the brief's status or approve it._

- [low] `how_sure_are_we.details[0]`: The cited claims state that missing stage at diagnosis (~48%) prevents stage adjustment of curative shares, not that it is the reason county treatment shares are not age-adjusted.
- [low] `how_sure_are_we.details[2]`: According to the cited quote q:5eb155decc, approximately 20% refers to clinical examination alone (such as imaging), rather than imaging specifically.

## Claims cited

- `bs:coverage:Diagnosis` (verified locally): Pathway stage 'Diagnosis' is measured in public data: yes (by county: yes (Kuva 7, 10, 13: PNG only)) — keuhkosyoparaportti_2019_2023.html, §4.1, Taulukko 2–4, Kuva 5–13
- `bs:coverage:First_specialist_visit` (verified locally): Pathway stage 'First specialist visit' is measured in public data: partly (by county: no) — keuhkosyoparaportti_2019_2023.html, §3.1, §4.2, Taulukko 5
- `bs:coverage:Imaging` (verified locally): Pathway stage 'Imaging' is measured in public data: partly (by county: partly (Kuva 7, PNG only)) — keuhkosyoparaportti_2019_2023.html, §4.1.1, Taulukko 2, Kuva 5–7
- `bs:coverage:MDT` (verified locally): Pathway stage 'MDT' is measured in public data: partly (by county: yes (Taulukko 11)) — keuhkosyoparaportti_2019_2023.html, §3.3, §4.2, Taulukko 5, 10, 11, 13
- `bs:coverage:Primary_care_occupational_health` (verified locally): Pathway stage 'Primary care / occupational health' is measured in public data: no (by county: no) — keuhkosyoparaportti_2019_2023.html, §3.3
- `bs:coverage:Referral` (verified locally): Pathway stage 'Referral' is measured in public data: no (by county: no) — keuhkosyoparaportti_2019_2023.html, whole report (no relevant data found)
- `bs:coverage:Symptoms` (verified locally): Pathway stage 'Symptoms' is measured in public data: no (by county: no) — keuhkosyoparaportti_2019_2023.html, whole report (no relevant data found)
- `bs:coverage:Treatment_start` (verified locally): Pathway stage 'Treatment start' is measured in public data: partly (by county: yes (type only, Taulukko 11)) — keuhkosyoparaportti_2019_2023.html, §4.2, §4.2.2, Taulukko 6–9, 11, 12, Kuva 14, 17
- `cty:curative:Länsi_Uudenmaan_hyvinvointialue` (verified locally): Länsi-Uudenmaan hyvinvointialue: curative treatment 31.9% (95% CI 29.1–34.7; n=337/1058), above vs national 27.0% — keuhkosyoparaportti_2019_2023.html, Taulukko 11
- `cty:life_prolonging:Länsi_Uudenmaan_hyvinvointialue` (verified locally): Länsi-Uudenmaan hyvinvointialue: life-prolonging treatment 25.2% (95% CI 22.7–27.9; n=267/1058), below vs national 30.4% — keuhkosyoparaportti_2019_2023.html, Taulukko 11
- `cty:mdt_recorded:Länsi_Uudenmaan_hyvinvointialue` (verified locally): Länsi-Uudenmaan hyvinvointialue: MDT meeting recorded 0.2% (95% CI 0.1–0.7; n=2/1058), below vs national 6.0% — keuhkosyoparaportti_2019_2023.html, Taulukko 11
- `cty:no_treatment_record:Länsi_Uudenmaan_hyvinvointialue` (verified locally): Länsi-Uudenmaan hyvinvointialue: no treatment record within 12 months 28.5% (95% CI 25.9–31.3; n=302/1058), not distinguishable vs national 27.5% — keuhkosyoparaportti_2019_2023.html, Taulukko 11
- `cty:symptomatic:Länsi_Uudenmaan_hyvinvointialue` (verified locally): Länsi-Uudenmaan hyvinvointialue: symptomatic treatment 40.1% (95% CI 37.2–43.1; n=424/1058), not distinguishable vs national 39.5% — keuhkosyoparaportti_2019_2023.html, Taulukko 11
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
- `q:0c7bf2dacb` (verified locally): p.56, content of pathways: > “Ketjuissa määritellään ja sovitaan mm. työnjaosta eri toimijoiden välillä, tavoitelluista > hoitoonpääsyajoista, keskeisistä laatu- ja vaikuttavuusindikaattoreista sekä kirjaamis- ja > koodistokäytännöistä.” — roadmap_2026_2031_fi.pdf, p.56
- `q:24169121a4` (verified locally): Strategy p.5 (= PDF p.5), “Strategiset tavoitteet”, indicator under “Varmistetaan yhdenvertainen ja vaikuttava syövänhoito”: > “Potilaat pääsevät hoitoon tavoiteaikojen puitteissa” > “ THL (Ohjaus 21/2016). Hoitoonpääsyn seuranta syövän hoidossa.” — strategy_2026_2035_fi.pdf, p.5
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
