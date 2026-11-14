# Etelä-Pohjanmaa: lung cancer pathway brief

Status: **validated** · gemini-4-argon (thinking HIGH) · 2026-11-14T12:17:25+00:00 · attempts: 1

## Where do we lag?

**Etelä-Pohjanmaa lags the national average in its crude symptomatic treatment share at 28.1% (95% CI 24.5–32.1; n=152/540), whose 95% confidence interval excludes the national 39.5% (5871/14873).** `cty:symptomatic:Etelä_Pohjanmaan_hyvinvointialue, nat:symptomatic`

- Across overlapping treatment categories, the county's crude curative share is 30.6% (95% CI 26.8–34.6; n=165/540), whose 95% confidence interval includes the national 27.0% (4009/14873), while its crude life-prolonging share of 40.4% (95% CI 36.3–44.6; n=218/540) has a 95% confidence interval excluding the national 30.4% (4522/14873). `cty:curative:Etelä_Pohjanmaan_hyvinvointialue, nat:curative, cty:life_prolonging:Etelä_Pohjanmaan_hyvinvointialue, nat:life_prolonging`
- The crude share with no treatment record within 12 months is 25.7% (95% CI 22.2–29.6; n=139/540), whose 95% confidence interval includes the national 27.5% (4089/14873), and the crude share with a recorded MDT meeting is 32.4% (95% CI 28.6–36.5; n=175/540), whose 95% confidence interval excludes the national 6.0% (893/14873). `cty:no_treatment_record:Etelä_Pohjanmaan_hyvinvointialue, nat:no_treatment_record, cty:mdt_recorded:Etelä_Pohjanmaan_hyvinvointialue, nat:mdt_recorded`
- Public data do not measure county waiting times from symptoms, primary care, or referral to treatment start, while preliminary, unpublished national figures average 155 days from symptoms to treatment in Finland versus 107 days in Sweden and 67 days in Denmark, including 56 days for patient delay, 41 days in primary care, and 58 days in specialist care. `bs:coverage:Symptoms, bs:coverage:Primary_care_occupational_health, bs:coverage:Referral, bs:coverage:Treatment_start, mot:total_fi, mot:total_se, mot:total_dk, mot:patient, mot:primary, mot:specialist`

## How sure are we?

**County treatment shares are crude figures unadjusted for age or stage, and public registry data omit referral dates, treatment start dates, and outpatient primary care visits.** `cty:curative:Etelä_Pohjanmaan_hyvinvointialue, bs:coverage:Diagnosis, bs:coverage:Referral, bs:coverage:Treatment_start, bs:coverage:Primary_care_occupational_health`

- Because the crude 25.7% (95% CI 22.2–29.6; n=139/540) share with no treatment record within 12 months—which mixes untreated patients and unrecorded care—has a 95% confidence interval including the national 27.5% (4089/14873), we infer treatment recording is relatively complete, making the crude 28.1% (95% CI 24.5–32.1; n=152/540) symptomatic share against 39.5% (5871/14873) nationally unlikely to be only a recording artefact. `cty:no_treatment_record:Etelä_Pohjanmaan_hyvinvointialue, nat:no_treatment_record, bs:coverage:Treatment_start, cty:symptomatic:Etelä_Pohjanmaan_hyvinvointialue, nat:symptomatic`
- While Kuva 16 gives digitised national age-adjusted curative reference lines of 26.7% for men and 26.9% for women (±0.5 percentage points), county shares cannot be stage-adjusted because stage is often missing; furthermore, a journal article finding about 90% HILMO diagnosis concordance covers diagnoses only, and MDT codes measure direct-contact recording rather than care. `k16:curative:men:national, k16:curative:women:national, bs:coverage:Diagnosis, q:7885b0974f, lit:hilmo_90, bs:coverage:MDT, q:39e6ba43a9`
- Outpatient primary care visits are not included in the report's data and occupational health is not mentioned, imaging appears only indirectly as the basis of diagnosis in approximately 20% of cases without wait times, and HILMO records a specialist visit within 12 months for 93.6% of patients nationally without county figures or timestamps. `bs:coverage:Primary_care_occupational_health, q:323de0d90d, bs:coverage:Imaging, q:5eb155decc, bs:coverage:First_specialist_visit`

## What should we do first?

**The team recommends reporting access times using THL guidance 21/2016 with handover alerts, standardising referrals and diagnostic contacts, and publishing county recording completeness for stage, drugs, and MDT.** `rec:1, rec:2, rec:3, thl:21_2016`

- The team recommends reporting access times from referral to treatment start using THL guidance 21/2016 definitions for 16 cancers and flagging stalled handovers, since the Health Care Act sets no maximum time for a cancer suspicion and national pathways with target access times are only planned for 2026–2028, alongside a Filha diagnostics recommendation due before the 2030 interim evaluation. `rec:1, thl:21_2016, law:no_max, q:4e702a20fe, q:def306014c, q:b326e35410, q:8f358a9de6, q:614febebf2, q:432c0e51d6`
- The team recommends a standard referral template, a primary care rule to refer persistent symptoms after a normal X-ray to a pulmonologist, and a named diagnostic-phase contact, given mentor insight that weak referrals receive lower specialist urgency ratings and that national referral criteria and care-coordinator guidance are only planned for 2026–2028, with county coordinator adoption planned for 2029–2031. `rec:2, mentor:kaisa_referral, q:556431a0c2, q:37bb4c3b38, q:9a1cd194f5, q:c61439b30f, q:fc81032a80, q:e31448e9c9, q:abcbb06ae3, q:050ee09ebe`
- To clarify whether Etelä-Pohjanmaa's crude 28.1% (95% CI 24.5–32.1; n=152/540) symptomatic share versus 39.5% (5871/14873) nationally and crude 32.4% (95% CI 28.6–36.5; n=175/540) MDT share versus 6.0% (893/14873) reflect care or coding, the team recommends publishing county recording completeness for stage, drug treatment, and MDT coding while a national quality registry targeting 90% coverage is planned. `rec:3, cty:symptomatic:Etelä_Pohjanmaan_hyvinvointialue, nat:symptomatic, cty:mdt_recorded:Etelä_Pohjanmaan_hyvinvointialue, nat:mdt_recorded, q:7885b0974f, q:950a2f797b, q:4c7a01d84c, q:f07a34a300, q:4a856bd695`

## Review flags (for human review only)

_Flags are for human review only; they never change the brief's status or approve it._

- [medium] `where_we_lag.headline`: Overreach and missing caveat: the cited claim only shows the county's symptomatic treatment share is below the national average, not that it 'lags' (a lower share of symptomatic-only care does not indicate worse performance), and the sentence omits the required caveat that treatment categories overlap.
- [medium] `how_sure_are_we.details[0]`: Overreach: having a no-treatment-record share indistinguishable from the national 27.5% (which mixes untreated patients and unrecorded treatment) does not support inferring that treatment recording is relatively complete or that the symptomatic-treatment difference is unlikely to be a recording artefact.
- [low] `how_sure_are_we.details[2]`: Minor imprecision: the cited quote states that approximately 20% of diagnoses are based on clinical examination alone, such as imaging, rather than imaging alone.
- [low] `what_to_do_first.headline`: Minor imprecision: recommendation 2 proposes naming a contact person for the diagnostic phase (and adding a persistent-symptoms referral rule), rather than 'standardising ... diagnostic contacts'.

## Claims cited

- `bs:coverage:Diagnosis` (verified locally): Pathway stage 'Diagnosis' is measured in public data: yes (by county: yes (Kuva 7, 10, 13: PNG only)) — keuhkosyoparaportti_2019_2023.html, §4.1, Taulukko 2–4, Kuva 5–13
- `bs:coverage:First_specialist_visit` (verified locally): Pathway stage 'First specialist visit' is measured in public data: partly (by county: no) — keuhkosyoparaportti_2019_2023.html, §3.1, §4.2, Taulukko 5
- `bs:coverage:Imaging` (verified locally): Pathway stage 'Imaging' is measured in public data: partly (by county: partly (Kuva 7, PNG only)) — keuhkosyoparaportti_2019_2023.html, §4.1.1, Taulukko 2, Kuva 5–7
- `bs:coverage:MDT` (verified locally): Pathway stage 'MDT' is measured in public data: partly (by county: yes (Taulukko 11)) — keuhkosyoparaportti_2019_2023.html, §3.3, §4.2, Taulukko 5, 10, 11, 13
- `bs:coverage:Primary_care_occupational_health` (verified locally): Pathway stage 'Primary care / occupational health' is measured in public data: no (by county: no) — keuhkosyoparaportti_2019_2023.html, §3.3
- `bs:coverage:Referral` (verified locally): Pathway stage 'Referral' is measured in public data: no (by county: no) — keuhkosyoparaportti_2019_2023.html, whole report (no relevant data found)
- `bs:coverage:Symptoms` (verified locally): Pathway stage 'Symptoms' is measured in public data: no (by county: no) — keuhkosyoparaportti_2019_2023.html, whole report (no relevant data found)
- `bs:coverage:Treatment_start` (verified locally): Pathway stage 'Treatment start' is measured in public data: partly (by county: yes (type only, Taulukko 11)) — keuhkosyoparaportti_2019_2023.html, §4.2, §4.2.2, Taulukko 6–9, 11, 12, Kuva 14, 17
- `cty:curative:Etelä_Pohjanmaan_hyvinvointialue` (verified locally): Etelä-Pohjanmaan hyvinvointialue: curative treatment 30.6% (95% CI 26.8–34.6; n=165/540), not distinguishable vs national 27.0% — keuhkosyoparaportti_2019_2023.html, Taulukko 11
- `cty:life_prolonging:Etelä_Pohjanmaan_hyvinvointialue` (verified locally): Etelä-Pohjanmaan hyvinvointialue: life-prolonging treatment 40.4% (95% CI 36.3–44.6; n=218/540), above vs national 30.4% — keuhkosyoparaportti_2019_2023.html, Taulukko 11
- `cty:mdt_recorded:Etelä_Pohjanmaan_hyvinvointialue` (verified locally): Etelä-Pohjanmaan hyvinvointialue: MDT meeting recorded 32.4% (95% CI 28.6–36.5; n=175/540), above vs national 6.0% — keuhkosyoparaportti_2019_2023.html, Taulukko 11
- `cty:no_treatment_record:Etelä_Pohjanmaan_hyvinvointialue` (verified locally): Etelä-Pohjanmaan hyvinvointialue: no treatment record within 12 months 25.7% (95% CI 22.2–29.6; n=139/540), not distinguishable vs national 27.5% — keuhkosyoparaportti_2019_2023.html, Taulukko 11
- `cty:symptomatic:Etelä_Pohjanmaan_hyvinvointialue` (verified locally): Etelä-Pohjanmaan hyvinvointialue: symptomatic treatment 28.1% (95% CI 24.5–32.1; n=152/540), below vs national 39.5% — keuhkosyoparaportti_2019_2023.html, Taulukko 11
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
- `q:37bb4c3b38` (verified locally): Policy evidence for pathway stage 'Referral' — roadmap_2026_2031_fi.pdf, p.52; p.106
- `q:39e6ba43a9` (verified locally): Report evidence for pathway stage 'MDT' — keuhkosyoparaportti_2019_2023.html, §3.3 Menetelmät
- `q:432c0e51d6` (verified locally): The upcoming national diagnostics recommendation will include “suositellut aikarajat erikoissairaanhoitoon eri diagnostiikan polun vaiheille” (recommended time limits in specialist care), due before the 2030 mid-term evaluation — filha_lung_programme_2026_fi.pdf, p.16
- `q:4a856bd695` (verified locally): the registry's data, including stage, allows reliable assessment and comparison of quality and effectiveness, with 90% data coverage — roadmap_2026_2031_fi.pdf, p.60
- `q:4c7a01d84c` (verified locally): nationally uniform recording instructions, and their use, must be ensured — filha_lung_programme_2026_fi.pdf, p.21
- `q:4e702a20fe` (verified locally): Finland has no unified national system to steer the drafting of cancer-specific treatment recommendations, or the implementation and monitoring of care pathways based on them (quality and effectiveness targets/indicators, including access to care, and cancer-specific and generic PROMs). Existing recommendations and pathways, and the targets and indicators to be monitored, are not coordinated nationally. This maintains regional inequality in the availability and effectiveness of cancer care. — strategy_2026_2035_fi.pdf, p.33
- `q:556431a0c2` (verified locally): the patient is referred to specialist care according to local instructions — filha_lung_programme_2026_fi.pdf, p.15
- `q:5eb155decc` (verified locally): Report evidence for pathway stage 'Imaging' — keuhkosyoparaportti_2019_2023.html, §4.1.1 Toteamistapa
- `q:614febebf2` (verified locally): When (p.24): > “Väliarvio toteutetaan vuonna 2030, ohjelman puolivälissä ja loppuarviointi vuonna 2036. Eri > osa-alueiden suositukset toteutetaan ennen väliarviointia.” — filha_lung_programme_2026_fi.pdf, p.24
- `q:7885b0974f` (verified locally): Report evidence for pathway stage 'Diagnosis' — keuhkosyoparaportti_2019_2023.html, §4.1.3 Levinneisyystiedon kattavuus
- `q:8f358a9de6` (verified locally): p.16: > “Tämän ohjelman yhtenä toimenpiteenä tuotetaan kansallinen suositus keuhkosyöpien diagnostiikasta. Se > sisältää myös lähetekriteerit perusterveydenhuollolle ja suositellut aikarajat erikoissairaanhoitoon > eri diagnostiikan polun vaiheille.” — filha_lung_programme_2026_fi.pdf, p.16
- `q:950a2f797b` (verified locally): Reporting, collection and storage of lung cancer data is currently incomplete. — filha_lung_programme_2026_fi.pdf, p.21
- `q:9a1cd194f5` (verified locally): support a smooth transfer to specialist care by defining standardised referral criteria within the national pathways, so that patients with possible cancer symptoms who meet them are directed quickly to diagnostic tests — roadmap_2026_2031_fi.pdf, p.52
- `q:abcbb06ae3` (verified locally): 2026–2028: guidance on a named doctor, nurse or specialist worker coordinating cancer care. 2029–2031: wellbeing services counties have adopted it. — roadmap_2026_2031_fi.pdf, p.32
- `q:b326e35410` (verified locally): National pathways with “syöpäkohtaiset hoitoonpääsyajat” for five (unnamed) cancers in 2026–2028, Nordic model — roadmap_2026_2031_fi.pdf, p.57
- `q:c61439b30f` (verified locally): 2026–2028: standardised referral criteria and symptom-based models included in the national pathways of at least the five most common cancers. — roadmap_2026_2031_fi.pdf, p.53
- `q:def306014c` (verified locally): p.57, timetable: > “2026–2028: Kansalliset hoitoketjukuvaukset tehty viidestä syövästä ja syöpäkohtaiset > hoitoonpääsyajat on määritetty.” — roadmap_2026_2031_fi.pdf, p.57
- `q:e31448e9c9` (verified locally): The review will map at which phase of care, and for which patient groups, a care coordinator is most important. — roadmap_2026_2031_fi.pdf, p.32
- `q:f07a34a300` (verified locally): A national cancer care quality registry will be set up alongside THL's Cancer Registry. — roadmap_2026_2031_fi.pdf, p.59
- `q:fc81032a80` (verified locally): Measure 1.2.3: Create an operating model and guidance for a named worker responsible for coordinating cancer care. — roadmap_2026_2031_fi.pdf, p.32
- `rec:1` (recommendation (ours)): Team recommendation 1: Counties report access times using the THL 21/2016 definitions, with handover alerts. Each wellbeing services county reports lung cancer access times (referral → first specialist visit → diagnosis → treatment start) using the definitions in THL's Hoitoonpääsyn seuranta syövän hoidossa (Ohjaus 21/2016). Until national target times exist, flag stalled handovers. — recommendations.md, §1. Counties report access times using the THL 21/2016 definitions, with handover alerts
- `rec:2` (recommendation (ours)): Team recommendation 2: A KYS-style referral template, a persistent-symptoms rule and a named contact. Adopt a standard referral content list and template, modelled on KYS. • Add a rule for primary care: if symptoms persist after a normal X-ray, refer for a pulmonologist assessment. • Name a contact person for the diagnostic phase, from referral to diagnosis. — recommendations.md, §2. A KYS-style referral template, a persistent-symptoms rule and a named contact
- `rec:3` (recommendation (ours)): Team recommendation 3: Report recording completeness per county: stage, drug treatment, MDT coding. Publish, per county, how completely stage, drug treatment and MDT meetings are recorded. Read county ‘gaps’ in these fields as data-quality signals first. — recommendations.md, §3. Report recording completeness per county: stage, drug treatment, MDT coding
- `thl:21_2016` (verified by Hellu): THL Ohjaus 21/2016 defines how cancer access times are recorded, for 16 cancers — pathway_brief.md, 6. Regional pathways compared
