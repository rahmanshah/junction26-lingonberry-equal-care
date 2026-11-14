# Helsinki: lung cancer pathway brief

Status: **validated** · gemini-4-argon (thinking HIGH) · 2026-11-14T12:25:48+00:00 · attempts: 1

## Where do we lag?

**Helsinki lags nationally in crude recorded MDT meetings (0.1%, 95% CI 0.0–0.4 vs 6.0%) and has lower crude symptomatic treatment (34.5%, 95% CI 32.1–37.0 vs 39.5%).** `cty:mdt_recorded:Helsingin_kaupunki, nat:mdt_recorded, cty:symptomatic:Helsingin_kaupunki, nat:symptomatic`

- In Helsinki, the crude share of patients with a recorded MDT meeting is 0.1% (95% CI 0.0–0.4; n=1/1486) compared with 6.0% (893/14873) nationally; the 95% confidence interval excludes the national value, though HILMO MDT codes measure recording practice from direct patient contacts rather than multidisciplinary care. `cty:mdt_recorded:Helsingin_kaupunki, nat:mdt_recorded, bs:coverage:MDT, q:39e6ba43a9`
- Across overlapping crude treatment categories that are not adjusted for age or stage, Helsinki's crude symptomatic share is 34.5% (95% CI 32.1–37.0; n=513/1486) versus 39.5% (5871/14873) nationally and crude curative share is 33.0% (95% CI 30.7–35.5; n=491/1486) versus 27.0% (4009/14873), with each 95% confidence interval excluding the national value. `cty:symptomatic:Helsingin_kaupunki, nat:symptomatic, cty:curative:Helsingin_kaupunki, nat:curative`
- Helsinki's crude life-prolonging treatment share is 30.8% (95% CI 28.5–33.1; n=457/1486) versus 30.4% (4522/14873) nationally, and its crude share with no treatment record within 12 months is 29.1% (95% CI 26.8–31.4; n=432/1486) versus 27.5% (4089/14873); the 95% confidence intervals include the national values. `cty:life_prolonging:Helsingin_kaupunki, nat:life_prolonging, cty:no_treatment_record:Helsingin_kaupunki, nat:no_treatment_record`
- Public data do not measure county access times, but preliminary, unpublished national averages show lung cancer takes 155 days from symptom onset to treatment in Finland versus 107 in Sweden and 67 in Denmark, with 56 days of patient delay, 41 days in primary care, and 58 days in specialist care. `bs:coverage:Symptoms, bs:coverage:Referral, bs:coverage:Treatment_start, mot:total_fi, mot:total_se, mot:total_dk, mot:patient, mot:primary, mot:specialist`

## How sure are we?

**Diagnosis counts are well supported, but crude county treatment shares lack age or stage adjustment, and public registry data do not capture pathway dates or pre-specialist care.** `lit:hilmo_90, bs:coverage:Diagnosis, bs:coverage:Primary_care_occupational_health, bs:coverage:Treatment_start`

- "No treatment record within 12 months" mixes untreated patients and unrecorded treatment; as an inference from this data-quality signal, not a finding, Helsinki's crude 29.1% share (95% CI 26.8–31.4; n=432/1486) versus 27.5% (4089/14873) nationally has a 95% confidence interval including 27.5%, though being above 27.5% means lower crude symptomatic share (34.5%, 95% CI 32.1–37.0) may partly reflect unrecorded treatment. `cty:no_treatment_record:Helsingin_kaupunki, nat:no_treatment_record, cty:symptomatic:Helsingin_kaupunki, bs:coverage:Treatment_start`
- County treatment shares are crude and not adjusted for age or stage: stage at diagnosis is missing for ~48% of new patients, and while Kuva 16 provides digitised national age-adjusted curative shares of 26.7% for men and 26.9% for women (read off a figure, precision ±0.5 percentage points), no age-adjusted county value is provided. `bs:coverage:Diagnosis, q:7885b0974f, k16:curative:men:national, k16:curative:women:national`
- A journal article found HILMO diagnoses match the Cancer Registry for about 90% of most cancer types, concerning diagnosis concordance only, while symptoms and referrals are not measured in public data, occupational health is not mentioned, and outpatient primary care visits are not included in the report's data. `lit:hilmo_90, bs:coverage:Symptoms, bs:coverage:Referral, bs:coverage:Primary_care_occupational_health, q:323de0d90d`
- Public data capture imaging only indirectly as the basis of diagnosis in approximately 20% of cases without imaging dates or waits, record whether a specialist visit occurred within 12 months (93.6% nationally) rather than when, and show treatment types within 12 months without treatment start dates. `bs:coverage:Imaging, q:5eb155decc, bs:coverage:First_specialist_visit, bs:coverage:Treatment_start`

## What should we do first?

**The team recommends auditing stage, drug, and MDT recording completeness, reporting access times using THL 21/2016 definitions with handover alerts, and standardising referrals and diagnostic-phase contacts.** `rec:1, rec:2, rec:3, thl:21_2016, q:950a2f797b, q:556431a0c2`

- Given Helsinki's 0.1% (95% CI 0.0–0.4; n=1/1486) crude recorded MDT share, 29.1% (95% CI 26.8–31.4; n=432/1486) crude no-treatment-record share, ~48% missing stage nationally, and incomplete national data collection, the team recommends publishing county recording completeness for stage, drug treatment, and MDT coding while the roadmap plans a national quality registry targeting 90% coverage. `rec:3, cty:mdt_recorded:Helsingin_kaupunki, cty:no_treatment_record:Helsingin_kaupunki, bs:coverage:Diagnosis, q:950a2f797b, q:f07a34a300, q:4a856bd695`
- Because Health Care Act §52 sets no legal maximum time for a cancer suspicion, the roadmap plans national pathway descriptions and target access times by 2026–2028, and the Filha diagnostics guideline is due before the 2030 mid-term evaluation, the team recommends reporting access times using THL Ohjaus 21/2016 definitions (for 16 cancers) with handover alerts. `rec:1, law:no_max, thl:21_2016, q:def306014c, q:8f358a9de6, q:614febebf2`
- Since referrals follow local instructions and mentor insight notes weak referrals receive lower specialist urgency ratings, the team recommends a standard referral template, referring persistent symptoms after a normal X-ray to a pulmonologist, and naming a diagnostic-phase contact, while the roadmap plans standardised referral criteria and care-coordinator guidance by 2026–2028 (for county adoption by 2029–2031). `rec:2, q:556431a0c2, mentor:kaisa_referral, q:9a1cd194f5, q:c61439b30f, q:abcbb06ae3, q:050ee09ebe`

## Review flags (for human review only)

_Flags are for human review only; they never change the brief's status or approve it._

- [medium] `how_sure_are_we.headline`: Overreaches and partly contradicts the cited claims: bs:coverage:Diagnosis explicitly states that the registry records the diagnosis date ('Registry diagnosis date'), so saying public registry data do not capture 'pathway dates' is inaccurate; additionally, bs:coverage:Primary_care_occupational_health states that primary care visits are not included in the report's data and occupational health is not mentioned in the report (rather than claiming that no public registry data capture pre-specialist care).
- [medium] `how_sure_are_we.details[1]`: None of the cited claims support the statement that 'no age-adjusted county value is provided'; k16:curative:men:national and k16:curative:women:national only report the digitised national reference lines from Kuva 16 and say nothing about whether age-adjusted county values are provided.

## Claims cited

- `bs:coverage:Diagnosis` (verified locally): Pathway stage 'Diagnosis' is measured in public data: yes (by county: yes (Kuva 7, 10, 13: PNG only)) — keuhkosyoparaportti_2019_2023.html, §4.1, Taulukko 2–4, Kuva 5–13
- `bs:coverage:First_specialist_visit` (verified locally): Pathway stage 'First specialist visit' is measured in public data: partly (by county: no) — keuhkosyoparaportti_2019_2023.html, §3.1, §4.2, Taulukko 5
- `bs:coverage:Imaging` (verified locally): Pathway stage 'Imaging' is measured in public data: partly (by county: partly (Kuva 7, PNG only)) — keuhkosyoparaportti_2019_2023.html, §4.1.1, Taulukko 2, Kuva 5–7
- `bs:coverage:MDT` (verified locally): Pathway stage 'MDT' is measured in public data: partly (by county: yes (Taulukko 11)) — keuhkosyoparaportti_2019_2023.html, §3.3, §4.2, Taulukko 5, 10, 11, 13
- `bs:coverage:Primary_care_occupational_health` (verified locally): Pathway stage 'Primary care / occupational health' is measured in public data: no (by county: no) — keuhkosyoparaportti_2019_2023.html, §3.3
- `bs:coverage:Referral` (verified locally): Pathway stage 'Referral' is measured in public data: no (by county: no) — keuhkosyoparaportti_2019_2023.html, whole report (no relevant data found)
- `bs:coverage:Symptoms` (verified locally): Pathway stage 'Symptoms' is measured in public data: no (by county: no) — keuhkosyoparaportti_2019_2023.html, whole report (no relevant data found)
- `bs:coverage:Treatment_start` (verified locally): Pathway stage 'Treatment start' is measured in public data: partly (by county: yes (type only, Taulukko 11)) — keuhkosyoparaportti_2019_2023.html, §4.2, §4.2.2, Taulukko 6–9, 11, 12, Kuva 14, 17
- `cty:curative:Helsingin_kaupunki` (verified locally): Helsingin kaupunki: curative treatment 33.0% (95% CI 30.7–35.5; n=491/1486), above vs national 27.0% — keuhkosyoparaportti_2019_2023.html, Taulukko 11
- `cty:life_prolonging:Helsingin_kaupunki` (verified locally): Helsingin kaupunki: life-prolonging treatment 30.8% (95% CI 28.5–33.1; n=457/1486), not distinguishable vs national 30.4% — keuhkosyoparaportti_2019_2023.html, Taulukko 11
- `cty:mdt_recorded:Helsingin_kaupunki` (verified locally): Helsingin kaupunki: MDT meeting recorded 0.1% (95% CI 0.0–0.4; n=1/1486), below vs national 6.0% — keuhkosyoparaportti_2019_2023.html, Taulukko 11
- `cty:no_treatment_record:Helsingin_kaupunki` (verified locally): Helsingin kaupunki: no treatment record within 12 months 29.1% (95% CI 26.8–31.4; n=432/1486), not distinguishable vs national 27.5% — keuhkosyoparaportti_2019_2023.html, Taulukko 11
- `cty:symptomatic:Helsingin_kaupunki` (verified locally): Helsingin kaupunki: symptomatic treatment 34.5% (95% CI 32.1–37.0; n=513/1486), below vs national 39.5% — keuhkosyoparaportti_2019_2023.html, Taulukko 11
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
- `q:323de0d90d` (verified locally): Report evidence for pathway stage 'Primary care / occupational health' — keuhkosyoparaportti_2019_2023.html, §3.3 Menetelmät
- `q:39e6ba43a9` (verified locally): Report evidence for pathway stage 'MDT' — keuhkosyoparaportti_2019_2023.html, §3.3 Menetelmät
- `q:4a856bd695` (verified locally): the registry's data, including stage, allows reliable assessment and comparison of quality and effectiveness, with 90% data coverage — roadmap_2026_2031_fi.pdf, p.60
- `q:556431a0c2` (verified locally): the patient is referred to specialist care according to local instructions — filha_lung_programme_2026_fi.pdf, p.15
- `q:5eb155decc` (verified locally): Report evidence for pathway stage 'Imaging' — keuhkosyoparaportti_2019_2023.html, §4.1.1 Toteamistapa
- `q:614febebf2` (verified locally): When (p.24): > “Väliarvio toteutetaan vuonna 2030, ohjelman puolivälissä ja loppuarviointi vuonna 2036. Eri > osa-alueiden suositukset toteutetaan ennen väliarviointia.” — filha_lung_programme_2026_fi.pdf, p.24
- `q:7885b0974f` (verified locally): Report evidence for pathway stage 'Diagnosis' — keuhkosyoparaportti_2019_2023.html, §4.1.3 Levinneisyystiedon kattavuus
- `q:8f358a9de6` (verified locally): p.16: > “Tämän ohjelman yhtenä toimenpiteenä tuotetaan kansallinen suositus keuhkosyöpien diagnostiikasta. Se > sisältää myös lähetekriteerit perusterveydenhuollolle ja suositellut aikarajat erikoissairaanhoitoon > eri diagnostiikan polun vaiheille.” — filha_lung_programme_2026_fi.pdf, p.16
- `q:950a2f797b` (verified locally): Reporting, collection and storage of lung cancer data is currently incomplete. — filha_lung_programme_2026_fi.pdf, p.21
- `q:9a1cd194f5` (verified locally): support a smooth transfer to specialist care by defining standardised referral criteria within the national pathways, so that patients with possible cancer symptoms who meet them are directed quickly to diagnostic tests — roadmap_2026_2031_fi.pdf, p.52
- `q:abcbb06ae3` (verified locally): 2026–2028: guidance on a named doctor, nurse or specialist worker coordinating cancer care. 2029–2031: wellbeing services counties have adopted it. — roadmap_2026_2031_fi.pdf, p.32
- `q:c61439b30f` (verified locally): 2026–2028: standardised referral criteria and symptom-based models included in the national pathways of at least the five most common cancers. — roadmap_2026_2031_fi.pdf, p.53
- `q:def306014c` (verified locally): p.57, timetable: > “2026–2028: Kansalliset hoitoketjukuvaukset tehty viidestä syövästä ja syöpäkohtaiset > hoitoonpääsyajat on määritetty.” — roadmap_2026_2031_fi.pdf, p.57
- `q:f07a34a300` (verified locally): A national cancer care quality registry will be set up alongside THL's Cancer Registry. — roadmap_2026_2031_fi.pdf, p.59
- `rec:1` (recommendation (ours)): Team recommendation 1: Counties report access times using the THL 21/2016 definitions, with handover alerts. Each wellbeing services county reports lung cancer access times (referral → first specialist visit → diagnosis → treatment start) using the definitions in THL's Hoitoonpääsyn seuranta syövän hoidossa (Ohjaus 21/2016). Until national target times exist, flag stalled handovers. — recommendations.md, §1. Counties report access times using the THL 21/2016 definitions, with handover alerts
- `rec:2` (recommendation (ours)): Team recommendation 2: A KYS-style referral template, a persistent-symptoms rule and a named contact. Adopt a standard referral content list and template, modelled on KYS. • Add a rule for primary care: if symptoms persist after a normal X-ray, refer for a pulmonologist assessment. • Name a contact person for the diagnostic phase, from referral to diagnosis. — recommendations.md, §2. A KYS-style referral template, a persistent-symptoms rule and a named contact
- `rec:3` (recommendation (ours)): Team recommendation 3: Report recording completeness per county: stage, drug treatment, MDT coding. Publish, per county, how completely stage, drug treatment and MDT meetings are recorded. Read county ‘gaps’ in these fields as data-quality signals first. — recommendations.md, §3. Report recording completeness per county: stage, drug treatment, MDT coding
- `thl:21_2016` (verified by Hellu): THL Ohjaus 21/2016 defines how cancer access times are recorded, for 16 cancers — pathway_brief.md, 6. Regional pathways compared
