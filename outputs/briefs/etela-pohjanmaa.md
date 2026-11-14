# Etelä-Pohjanmaa: lung cancer pathway brief

Status: **validated** · gemini-4-argon (thinking HIGH) · 2026-11-14T13:09:44+00:00 · attempts: 1

## Where do we lag?

**In Etelä-Pohjanmaa, the crude symptomatic treatment share of 28.1% (95% CI 24.5–32.1; n=152/540) is below the national 39.5% (5871/14873), as its 95% confidence interval excludes the national value.** `cty:symptomatic:Etelä_Pohjanmaan_hyvinvointialue, nat:symptomatic`

- Because treatment categories overlap, patients can receive several types: the crude curative treatment share is 30.6% (95% CI 26.8–34.6; n=165/540), whose 95% confidence interval includes the national 27.0% (4009/14873), while the crude life-prolonging treatment share is 40.4% (95% CI 36.3–44.6; n=218/540), whose 95% confidence interval excludes the national 30.4% (4522/14873). `cty:curative:Etelä_Pohjanmaan_hyvinvointialue, nat:curative, cty:life_prolonging:Etelä_Pohjanmaan_hyvinvointialue, nat:life_prolonging`
- The crude share with no treatment record within 12 months is 25.7% (95% CI 22.2–29.6; n=139/540), whose 95% confidence interval includes the national 27.5% (4089/14873), and this category mixes untreated patients and unrecorded treatment. `cty:no_treatment_record:Etelä_Pohjanmaan_hyvinvointialue, nat:no_treatment_record, bs:coverage:Treatment_start`
- The crude share with a multidisciplinary team (MDT) meeting recorded is 32.4% (95% CI 28.6–36.5; n=175/540) versus 6.0% (893/14873) nationally, but MDT records measure recording practice, not care, because HILMO captures procedures only from direct patient contacts. `cty:mdt_recorded:Etelä_Pohjanmaan_hyvinvointialue, nat:mdt_recorded, bs:coverage:MDT, q:39e6ba43a9`
- Public registry data do not report county waiting times, while preliminary, unpublished figures show lung cancer care in Finland takes 155 days on average from first symptoms to treatment (56 days patient delay, 41 days in primary care, and 58 days in specialist care), compared with 107 days in Sweden and 67 days in Denmark. `bs:coverage:Symptoms, bs:coverage:Treatment_start, mot:total_fi, mot:patient, mot:primary, mot:specialist, mot:total_se, mot:total_dk`

## How sure are we?

**County treatment shares are crude, unadjusted figures, and public registry data do not capture primary care, referrals, stage at diagnosis for about 48% of patients, or treatment start dates.** `bs:coverage:Primary_care_occupational_health, bs:coverage:Referral, bs:coverage:Diagnosis, bs:coverage:Treatment_start`

- The county shares are crude and have separate limitations: they are not age-adjusted (digitised age-adjusted shares from Kuva 16, at ±0.5 percentage points precision, exist only for curative treatment by sex, with national lines at 26.7% for men and 26.9% for women), and they cannot be stage-adjusted because stage at diagnosis is missing for about 48% of patients. `k16:curative:men:national, k16:curative:women:national, bs:coverage:Diagnosis, q:7885b0974f`
- According to a journal article, hospital discharge register (HILMO) diagnoses match the Cancer Registry for about 90% of most cancer types, but this concerns diagnosis concordance only, and 93.6% of patients have a specialist lung cancer visit in HILMO within 12 months without showing when the visit or treatment started. `lit:hilmo_90, bs:coverage:First_specialist_visit, bs:coverage:Treatment_start`
- Public report data do not measure symptom onset or referral dates, primary care visits are not included in the report's data, occupational health is not mentioned, and imaging appears only indirectly as diagnosis by clinical examination alone in about 20% of patients rather than imaging waits. `bs:coverage:Symptoms, bs:coverage:Referral, bs:coverage:Primary_care_occupational_health, q:323de0d90d, bs:coverage:Imaging, q:5eb155decc`

## What should we do first?

**The team recommends tracking access times with THL guidance Ohjaus 21/2016 definitions, standardising referrals and diagnostic coordination, and publishing county recording coverage for stage, drug treatment, and MDT coding.** `rec:1, rec:2, rec:3, thl:21_2016`

- Because the Health Care Act (§52) sets no legal maximum time for a cancer suspicion and Finland lacks a unified national monitoring system, the team recommends reporting county access times (referral to first specialist visit to diagnosis to treatment start) using THL guidance Ohjaus 21/2016 definitions for 16 cancers and flagging stalled handovers. `rec:1, law:no_max, q:4e702a20fe, thl:21_2016`
- Since mentor insight indicates a weak referral gets a lower urgency rating, and the Filha programme's diagnostics recommendation with primary-care referral criteria and recommended time limits is to be carried out before the 2030 mid-term evaluation, the team recommends adopting a standard referral template, referring persistent symptoms after a normal X-ray, and naming a diagnostic contact person. `rec:2, mentor:kaisa_referral, q:8f358a9de6, q:614febebf2`
- While the STM roadmap (measure 3.2.1) plans a national cancer quality registry alongside THL's Cancer Registry with the registry decree updated by 2026–2028 and 90% data coverage including stage by 2029–2031, the team recommends publishing per-county recording coverage for stage, drug treatment, and MDT coding and reading county gaps in these fields as data-quality signals first. `rec:3, q:f07a34a300, q:4a856bd695, q:950a2f797b`

## Review flags (for human review only)

_Flags are for human review only; they never change the brief's status or approve it._

- [medium] `what_to_do_first.details[2]`: The cited claims state that the 2029–2031 timeframe in STM roadmap measure 3.2.1 applies to publishing annual reports for at least five cancers, whereas the 90% data coverage target in q:4a856bd695 is stated without a 2029–2031 deadline.

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
- `q:323de0d90d` (verified locally): Report evidence for pathway stage 'Primary care / occupational health' — keuhkosyoparaportti_2019_2023.html, §3.3 Menetelmät
- `q:39e6ba43a9` (verified locally): Report evidence for pathway stage 'MDT' — keuhkosyoparaportti_2019_2023.html, §3.3 Menetelmät
- `q:4a856bd695` (verified locally): the registry's data, including stage, allows reliable assessment and comparison of quality and effectiveness, with 90% data coverage — roadmap_2026_2031_fi.pdf, p.60
- `q:4e702a20fe` (verified locally): Finland has no unified national system to steer the drafting of cancer-specific treatment recommendations, or the implementation and monitoring of care pathways based on them (quality and effectiveness targets/indicators, including access to care, and cancer-specific and generic PROMs). Existing recommendations and pathways, and the targets and indicators to be monitored, are not coordinated nationally. This maintains regional inequality in the availability and effectiveness of cancer care. — strategy_2026_2035_fi.pdf, p.33
- `q:5eb155decc` (verified locally): Report evidence for pathway stage 'Imaging' — keuhkosyoparaportti_2019_2023.html, §4.1.1 Toteamistapa
- `q:614febebf2` (verified locally): When (p.24): > “Väliarvio toteutetaan vuonna 2030, ohjelman puolivälissä ja loppuarviointi vuonna 2036. Eri > osa-alueiden suositukset toteutetaan ennen väliarviointia.” — filha_lung_programme_2026_fi.pdf, p.24
- `q:7885b0974f` (verified locally): Report evidence for pathway stage 'Diagnosis' — keuhkosyoparaportti_2019_2023.html, §4.1.3 Levinneisyystiedon kattavuus
- `q:8f358a9de6` (verified locally): p.16: > “Tämän ohjelman yhtenä toimenpiteenä tuotetaan kansallinen suositus keuhkosyöpien diagnostiikasta. Se > sisältää myös lähetekriteerit perusterveydenhuollolle ja suositellut aikarajat erikoissairaanhoitoon > eri diagnostiikan polun vaiheille.” — filha_lung_programme_2026_fi.pdf, p.16
- `q:950a2f797b` (verified locally): Reporting, collection and storage of lung cancer data is currently incomplete. — filha_lung_programme_2026_fi.pdf, p.21
- `q:f07a34a300` (verified locally): A national cancer care quality registry will be set up alongside THL's Cancer Registry. — roadmap_2026_2031_fi.pdf, p.59
- `rec:1` (recommendation (ours)): Team recommendation 1: Counties report access times using the THL 21/2016 definitions, with handover alerts. Each wellbeing services county reports lung cancer access times (referral → first specialist visit → diagnosis → treatment start) using the definitions in THL's Hoitoonpääsyn seuranta syövän hoidossa (Ohjaus 21/2016). Until national target times exist, flag stalled handovers. — recommendations.md, §1. Counties report access times using the THL 21/2016 definitions, with handover alerts
- `rec:2` (recommendation (ours)): Team recommendation 2: A KYS-style referral template, a persistent-symptoms rule and a named contact. Adopt a standard referral content list and template, modelled on KYS. • Add a rule for primary care: if symptoms persist after a normal X-ray, refer for a pulmonologist assessment. • Name a contact person for the diagnostic phase, from referral to diagnosis. — recommendations.md, §2. A KYS-style referral template, a persistent-symptoms rule and a named contact
- `rec:3` (recommendation (ours)): Team recommendation 3: Report recording completeness per county: stage, drug treatment, MDT coding. Publish, per county, how completely stage, drug treatment and MDT meetings are recorded. Read county ‘gaps’ in these fields as data-quality signals first. — recommendations.md, §3. Report recording completeness per county: stage, drug treatment, MDT coding
- `thl:21_2016` (verified by Hellu): THL Ohjaus 21/2016 defines how cancer access times are recorded, for 16 cancers — pathway_brief.md, 6. Regional pathways compared
