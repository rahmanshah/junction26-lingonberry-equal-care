# Pohjois-Savo: lung cancer pathway brief

Status: **validated** · gemini-4-argon (thinking HIGH) · 2026-11-14T12:10:03+00:00 · attempts: 1

## Where do we lag?

**Pohjois-Savo lags the national value in crude multidisciplinary team meeting recording at 0.2% (95% CI 0.0–0.9; n=1/641) compared with 6.0% (893/14873) nationally.** `cty:mdt_recorded:Pohjois_Savon_hyvinvointialue, nat:mdt_recorded`

- The 95% confidence interval for this crude multidisciplinary team share of 0.2% (95% CI 0.0–0.9; n=1/641) excludes the national 6.0% (893/14873), but HILMO codes only direct patient contacts and measures recording practice rather than care, whereas the KYS regional care chain document states KYS reviews every patient weekly. `cty:mdt_recorded:Pohjois_Savon_hyvinvointialue, nat:mdt_recorded, bs:coverage:MDT, q:39e6ba43a9, reg:mdt_practice`
- Pohjois-Savo's crude curative treatment share is 24.5% (95% CI 21.3–28.0; n=157/641) compared with 27.0% (4009/14873) nationally, and because the 95% confidence interval includes the national value, this unadjusted figure is not distinguishable from the national benchmark. `cty:curative:Pohjois_Savon_hyvinvointialue, nat:curative`
- Across overlapping treatment categories within 12 months, Pohjois-Savo's crude life-prolonging treatment share of 38.7% (95% CI 35.0–42.5; n=248/641) and crude symptomatic treatment share of 51.2% (95% CI 47.3–55.0; n=328/641) have 95% confidence intervals that exclude the national values of 30.4% (4522/14873) and 39.5% (5871/14873). `cty:life_prolonging:Pohjois_Savon_hyvinvointialue, nat:life_prolonging, cty:symptomatic:Pohjois_Savon_hyvinvointialue, nat:symptomatic, bs:coverage:Treatment_start`
- Public data do not measure county access times, while preliminary, unpublished national figures average 155 days from initial symptoms to treatment in Finland versus 107 days in Sweden and 67 days in Denmark, comprising 56 days of patient delay, 41 days in primary care, and 58 days in specialist care. `bs:coverage:Symptoms, bs:coverage:Primary_care_occupational_health, bs:coverage:Referral, bs:coverage:Treatment_start, mot:total_fi, mot:total_se, mot:total_dk, mot:patient, mot:primary, mot:specialist`

## How sure are we?

**Pohjois-Savo's crude 19.3% (95% CI 16.5–22.6; n=124/641) no-treatment-record share is below 27.5% (4089/14873) nationally, suggesting relatively complete treatment recording, though county shares remain unadjusted for age or stage.** `cty:no_treatment_record:Pohjois_Savon_hyvinvointialue, nat:no_treatment_record, bs:coverage:Diagnosis`

- The crude 19.3% (95% CI 16.5–22.6; n=124/641) share with no treatment record within 12 months mixes untreated patients and unrecorded treatment, and its 95% confidence interval excludes the national 27.5% (4089/14873). `cty:no_treatment_record:Pohjois_Savon_hyvinvointialue, nat:no_treatment_record, bs:coverage:Treatment_start`
- Reading that crude 19.3% (95% CI 16.5–22.6; n=124/641) share as a data-quality signal is, by inference rather than direct evidence, consistent with relatively complete treatment recording, so the crude 24.5% (95% CI 21.3–28.0; n=157/641) curative share is less likely to be only a recording artefact. `cty:no_treatment_record:Pohjois_Savon_hyvinvointialue, nat:no_treatment_record, cty:curative:Pohjois_Savon_hyvinvointialue, nat:curative`
- A journal article reports HILMO diagnoses match the Cancer Registry for about 90% of most cancer types without assessing treatment recording, and county treatment shares remain unadjusted for stage or age, with Kuva 16 providing only national age-adjusted curative reference lines digitised from a figure at ±0.5 percentage points (26.7% for men, 26.9% for women). `lit:hilmo_90, bs:coverage:Diagnosis, q:7885b0974f, k16:curative:men:national, k16:curative:women:national`
- Outpatient primary care visits are not included in the report's data and occupational health is not mentioned, while public data also lack symptom onset, referral dates, and treatment start dates, capturing imaging only indirectly in approximately 20% of diagnoses. `bs:coverage:Symptoms, bs:coverage:Primary_care_occupational_health, q:323de0d90d, bs:coverage:Imaging, q:5eb155decc, bs:coverage:Referral, bs:coverage:First_specialist_visit, bs:coverage:Treatment_start`

## What should we do first?

**The team recommends publishing stage, drug, and multidisciplinary recording completeness, tracking THL 21/2016 access times with handover alerts, and naming a diagnostic contact alongside KYS referral rules.** `rec:1, rec:2, rec:3, q:24169121a4, q:37bb4c3b38, q:950a2f797b`

- The team recommends publishing county recording completeness for stage, drug treatment, and multidisciplinary meetings: Pohjois-Savo's crude multidisciplinary share is 0.2% (95% CI 0.0–0.9; n=1/641) versus 6.0% (893/14873) nationally despite the KYS regional care chain document specifying weekly review for every patient, and the roadmap plans a national quality registry with 90% coverage including stage. `rec:3, cty:mdt_recorded:Pohjois_Savon_hyvinvointialue, nat:mdt_recorded, reg:mdt_practice, bs:coverage:Diagnosis, q:950a2f797b, q:f07a34a300, q:4a856bd695`
- The team recommends reporting access times from referral to treatment start using THL Ohjaus 21/2016 guidance definitions for 16 cancers and flagging stalled handovers, as the Health Care Act sets no maximum time for a cancer suspicion, the roadmap plans target access times in 2026–2028, and the Filha diagnostics guideline is due before 2030. `rec:1, thl:21_2016, law:no_max, q:def306014c, q:8f358a9de6, q:614febebf2`
- The team recommends maintaining the KYS regional care chain document's referral template and rule to refer persistent unexplained symptoms after a clear X-ray—supported by mentor insight that weak referrals receive lower urgency ratings—while naming a diagnostic-phase contact person, since reviewed regional pathway documents name none and the roadmap plans coordinator guidelines in 2026–2028 for county adoption in 2029–2031. `rec:2, reg:kys_template, reg:kys_persistent, reg:only_kys_xray, mentor:kaisa_referral, reg:named_contact, q:abcbb06ae3, q:050ee09ebe`

## Review flags (for human review only)

_Flags are for human review only; they never change the brief's status or approve it._

- [medium] `how_sure_are_we.headline`: The cited claims only give the county and national no-treatment-record shares and stage missingness; they do not establish that a lower no-treatment-record share indicates relatively complete treatment recording. Because the indicator mixes untreated patients and unrecorded treatment, presenting this inference as what the data suggest without that caveat is an overreach.

## Claims cited

- `bs:coverage:Diagnosis` (verified locally): Pathway stage 'Diagnosis' is measured in public data: yes (by county: yes (Kuva 7, 10, 13: PNG only)) — keuhkosyoparaportti_2019_2023.html, §4.1, Taulukko 2–4, Kuva 5–13
- `bs:coverage:First_specialist_visit` (verified locally): Pathway stage 'First specialist visit' is measured in public data: partly (by county: no) — keuhkosyoparaportti_2019_2023.html, §3.1, §4.2, Taulukko 5
- `bs:coverage:Imaging` (verified locally): Pathway stage 'Imaging' is measured in public data: partly (by county: partly (Kuva 7, PNG only)) — keuhkosyoparaportti_2019_2023.html, §4.1.1, Taulukko 2, Kuva 5–7
- `bs:coverage:MDT` (verified locally): Pathway stage 'MDT' is measured in public data: partly (by county: yes (Taulukko 11)) — keuhkosyoparaportti_2019_2023.html, §3.3, §4.2, Taulukko 5, 10, 11, 13
- `bs:coverage:Primary_care_occupational_health` (verified locally): Pathway stage 'Primary care / occupational health' is measured in public data: no (by county: no) — keuhkosyoparaportti_2019_2023.html, §3.3
- `bs:coverage:Referral` (verified locally): Pathway stage 'Referral' is measured in public data: no (by county: no) — keuhkosyoparaportti_2019_2023.html, whole report (no relevant data found)
- `bs:coverage:Symptoms` (verified locally): Pathway stage 'Symptoms' is measured in public data: no (by county: no) — keuhkosyoparaportti_2019_2023.html, whole report (no relevant data found)
- `bs:coverage:Treatment_start` (verified locally): Pathway stage 'Treatment start' is measured in public data: partly (by county: yes (type only, Taulukko 11)) — keuhkosyoparaportti_2019_2023.html, §4.2, §4.2.2, Taulukko 6–9, 11, 12, Kuva 14, 17
- `cty:curative:Pohjois_Savon_hyvinvointialue` (verified locally): Pohjois-Savon hyvinvointialue: curative treatment 24.5% (95% CI 21.3–28.0; n=157/641), not distinguishable vs national 27.0% — keuhkosyoparaportti_2019_2023.html, Taulukko 11
- `cty:life_prolonging:Pohjois_Savon_hyvinvointialue` (verified locally): Pohjois-Savon hyvinvointialue: life-prolonging treatment 38.7% (95% CI 35.0–42.5; n=248/641), above vs national 30.4% — keuhkosyoparaportti_2019_2023.html, Taulukko 11
- `cty:mdt_recorded:Pohjois_Savon_hyvinvointialue` (verified locally): Pohjois-Savon hyvinvointialue: MDT meeting recorded 0.2% (95% CI 0.0–0.9; n=1/641), below vs national 6.0% — keuhkosyoparaportti_2019_2023.html, Taulukko 11
- `cty:no_treatment_record:Pohjois_Savon_hyvinvointialue` (verified locally): Pohjois-Savon hyvinvointialue: no treatment record within 12 months 19.3% (95% CI 16.5–22.6; n=124/641), below vs national 27.5% — keuhkosyoparaportti_2019_2023.html, Taulukko 11
- `cty:symptomatic:Pohjois_Savon_hyvinvointialue` (verified locally): Pohjois-Savon hyvinvointialue: symptomatic treatment 51.2% (95% CI 47.3–55.0; n=328/641), above vs national 39.5% — keuhkosyoparaportti_2019_2023.html, Taulukko 11
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
- `q:050ee09ebe` (verified locally): Guidance on a named worker coordinating cancer care by 2026–2028, adopted by counties by 2029–2031; the care phase is left open (“missä hoidon vaiheessa … olisi tärkeintä kohdentaa”) — roadmap_2026_2031_fi.pdf, p.32
- `q:24169121a4` (verified locally): Strategy p.5 (= PDF p.5), “Strategiset tavoitteet”, indicator under “Varmistetaan yhdenvertainen ja vaikuttava syövänhoito”: > “Potilaat pääsevät hoitoon tavoiteaikojen puitteissa” > “ THL (Ohjaus 21/2016). Hoitoonpääsyn seuranta syövän hoidossa.” — strategy_2026_2035_fi.pdf, p.5
- `q:323de0d90d` (verified locally): Report evidence for pathway stage 'Primary care / occupational health' — keuhkosyoparaportti_2019_2023.html, §3.3 Menetelmät
- `q:37bb4c3b38` (verified locally): Policy evidence for pathway stage 'Referral' — roadmap_2026_2031_fi.pdf, p.52; p.106
- `q:39e6ba43a9` (verified locally): Report evidence for pathway stage 'MDT' — keuhkosyoparaportti_2019_2023.html, §3.3 Menetelmät
- `q:4a856bd695` (verified locally): the registry's data, including stage, allows reliable assessment and comparison of quality and effectiveness, with 90% data coverage — roadmap_2026_2031_fi.pdf, p.60
- `q:5eb155decc` (verified locally): Report evidence for pathway stage 'Imaging' — keuhkosyoparaportti_2019_2023.html, §4.1.1 Toteamistapa
- `q:614febebf2` (verified locally): When (p.24): > “Väliarvio toteutetaan vuonna 2030, ohjelman puolivälissä ja loppuarviointi vuonna 2036. Eri > osa-alueiden suositukset toteutetaan ennen väliarviointia.” — filha_lung_programme_2026_fi.pdf, p.24
- `q:7885b0974f` (verified locally): Report evidence for pathway stage 'Diagnosis' — keuhkosyoparaportti_2019_2023.html, §4.1.3 Levinneisyystiedon kattavuus
- `q:8f358a9de6` (verified locally): p.16: > “Tämän ohjelman yhtenä toimenpiteenä tuotetaan kansallinen suositus keuhkosyöpien diagnostiikasta. Se > sisältää myös lähetekriteerit perusterveydenhuollolle ja suositellut aikarajat erikoissairaanhoitoon > eri diagnostiikan polun vaiheille.” — filha_lung_programme_2026_fi.pdf, p.16
- `q:950a2f797b` (verified locally): Reporting, collection and storage of lung cancer data is currently incomplete. — filha_lung_programme_2026_fi.pdf, p.21
- `q:abcbb06ae3` (verified locally): 2026–2028: guidance on a named doctor, nurse or specialist worker coordinating cancer care. 2029–2031: wellbeing services counties have adopted it. — roadmap_2026_2031_fi.pdf, p.32
- `q:def306014c` (verified locally): p.57, timetable: > “2026–2028: Kansalliset hoitoketjukuvaukset tehty viidestä syövästä ja syöpäkohtaiset > hoitoonpääsyajat on määritetty.” — roadmap_2026_2031_fi.pdf, p.57
- `q:f07a34a300` (verified locally): A national cancer care quality registry will be set up alongside THL's Cancer Registry. — roadmap_2026_2031_fi.pdf, p.59
- `rec:1` (recommendation (ours)): Team recommendation 1: Counties report access times using the THL 21/2016 definitions, with handover alerts. Each wellbeing services county reports lung cancer access times (referral → first specialist visit → diagnosis → treatment start) using the definitions in THL's Hoitoonpääsyn seuranta syövän hoidossa (Ohjaus 21/2016). Until national target times exist, flag stalled handovers. — recommendations.md, §1. Counties report access times using the THL 21/2016 definitions, with handover alerts
- `rec:2` (recommendation (ours)): Team recommendation 2: A KYS-style referral template, a persistent-symptoms rule and a named contact. Adopt a standard referral content list and template, modelled on KYS. • Add a rule for primary care: if symptoms persist after a normal X-ray, refer for a pulmonologist assessment. • Name a contact person for the diagnostic phase, from referral to diagnosis. — recommendations.md, §2. A KYS-style referral template, a persistent-symptoms rule and a named contact
- `rec:3` (recommendation (ours)): Team recommendation 3: Report recording completeness per county: stage, drug treatment, MDT coding. Publish, per county, how completely stage, drug treatment and MDT meetings are recorded. Read county ‘gaps’ in these fields as data-quality signals first. — recommendations.md, §3. Report recording completeness per county: stage, drug treatment, MDT coding
- `reg:kys_persistent` (verified by Hellu): KYS: refer persistent unexplained symptoms even if the X-ray is clear — pathway_brief.md, 6. Regional pathways compared
- `reg:kys_template` (verified by Hellu): Only KYS lists required referral content and provides a referral template — pathway_brief.md, 6. Regional pathways compared
- `reg:mdt_practice` (verified by Hellu): MDT practice differs: KYS every patient weekly, Keski-Suomi every new case, HUS when needed — pathway_brief.md, 6. Regional pathways compared
- `reg:named_contact` (verified by Hellu): No region names a contact person for the diagnostic phase — pathway_brief.md, 6. Regional pathways compared
- `reg:only_kys_xray` (verified by Hellu): Only KYS tells primary care what to do with a normal X-ray and continuing symptoms — pathway_brief.md, 6. Regional pathways compared
- `thl:21_2016` (verified by Hellu): THL Ohjaus 21/2016 defines how cancer access times are recorded, for 16 cancers — pathway_brief.md, 6. Regional pathways compared
