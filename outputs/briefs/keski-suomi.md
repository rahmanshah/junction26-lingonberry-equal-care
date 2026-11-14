# Keski-Suomi: lung cancer pathway brief

Status: **validated** · gemini-4-argon (thinking HIGH) · 2026-11-14T12:59:44+00:00 · attempts: 1

## Where do we lag?

**In Keski-Suomi, the crude MDT-recorded share is 3.8% (95% CI 2.5–5.5; n=24/637), whose 95% confidence interval excludes the national 6.0% (893/14873), though MDT records measure recording practice, not care.** `cty:mdt_recorded:Keski_Suomen_hyvinvointialue, nat:mdt_recorded, bs:coverage:MDT`

- Across overlapping treatment categories, the 95% confidence intervals include the national values for Keski-Suomi's crude curative share of 27.2% (95% CI 23.9–30.7; n=173/637) vs 27.0% (4009/14873) and crude symptomatic share of 36.3% (95% CI 32.6–40.1; n=231/637) vs 39.5% (5871/14873), whereas the crude life-prolonging share of 37.2% (95% CI 33.5–41.0; n=237/637) excludes the national 30.4% (4522/14873). `cty:curative:Keski_Suomen_hyvinvointialue, nat:curative, cty:symptomatic:Keski_Suomen_hyvinvointialue, nat:symptomatic, cty:life_prolonging:Keski_Suomen_hyvinvointialue, nat:life_prolonging, bs:coverage:Treatment_start`
- Although Keski-Suomi's regional pathway document states that every new case is reviewed in an MDT, specialised care procedures are entered into HILMO only from direct patient contacts, so the crude 3.8% (95% CI 2.5–5.5; n=24/637) MDT share reflects recording practice rather than care. `reg:mdt_practice, q:39e6ba43a9, bs:coverage:MDT, cty:mdt_recorded:Keski_Suomen_hyvinvointialue`
- Keski-Suomi's regional pathway document handles referrals as quickly as possible with no time stated, targets a lung clinic appointment within 2–3 weeks or at the latest about 1 month and tissue sample results in about 1–2 weeks, names occupational health as a referral source, and names no diagnostic contact person, without reporting whether target times are met. `reg:ks_referral, reg:ks_target, reg:ks_tissue, reg:occupational, reg:named_contact, reg:not_monitored`
- Nationally, preliminary unpublished study figures show the average time from symptoms to treatment is 155 days in Finland compared with 107 in Sweden and 67 in Denmark, with 56 days of patient delay, 41 days in primary care, and 58 days in specialist care as the longest stage. `mot:total_fi, mot:total_se, mot:total_dk, mot:patient, mot:primary, mot:specialist`

## How sure are we?

**Registry diagnosis concordance is about 90%, but county treatment shares are crude, unadjusted for age or stage, and public data omit key pathway dates and pre-referral steps.** `lit:hilmo_90, bs:coverage:Diagnosis, bs:coverage:Primary_care_occupational_health, bs:coverage:Referral, bs:coverage:Treatment_start`

- County shares are crude and not age-adjusted; age-adjusted values exist only from Kuva 16 for curative treatment by sex, digitised from a figure at about ±0.5 percentage points precision (national lines 26.7% for men, 26.9% for women), while Keski-Suomi's crude curative 27.2% (95% CI 23.9–30.7; n=173/637) shows no gap vs the national 27.0% (4009/14873). `cty:curative:Keski_Suomen_hyvinvointialue, nat:curative, k16:curative:men:national, k16:curative:women:national`
- As a separate limitation from age adjustment, county shares cannot be stage-adjusted because stage at diagnosis is missing for about 48% of patients, while a journal article found that HILMO diagnoses match the Cancer Registry for about 90% of most cancer types, concerning diagnosis concordance only. `bs:coverage:Diagnosis, q:7885b0974f, lit:hilmo_90`
- Keski-Suomi's crude share with no treatment record within 12 months is 24.5% (95% CI 21.3–28.0; n=156/637), whose 95% confidence interval includes the national 27.5% (4089/14873) and is not distinguishable from it, and this category mixes untreated patients and treatment that was not recorded. `cty:no_treatment_record:Keski_Suomen_hyvinvointialue, nat:no_treatment_record, bs:coverage:Treatment_start`
- Public data do not measure symptoms or referral dates, primary care visits are not included in the report's data, occupational health is not mentioned, imaging appears only where diagnosis rests on clinical examination alone in approximately 20% of patients, and although 93.6% have a specialist visit within 12 months, visit and treatment start dates are not reported. `bs:coverage:Symptoms, bs:coverage:Primary_care_occupational_health, q:323de0d90d, bs:coverage:Imaging, q:5eb155decc, bs:coverage:Referral, bs:coverage:First_specialist_visit, bs:coverage:Treatment_start`

## What should we do first?

**The team recommends that Keski-Suomi publish stage, drug, and MDT recording completeness, report access times using THL 21/2016 definitions with handover alerts, and standardise referrals and diagnostic coordination.** `rec:1, rec:2, rec:3, q:950a2f797b, reg:not_monitored, reg:named_contact`

- With Keski-Suomi's crude 3.8% (95% CI 2.5–5.5; n=24/637) MDT-recorded share despite its pathway document reviewing every new case, stage missing for about 48% of patients, and incomplete national data, the team recommends publishing county recording completeness for stage, drug treatment, and MDT coding while the STM roadmap (measure 3.2.1) plans a national quality registry with its decree updated by 2026–2028. `rec:3, cty:mdt_recorded:Keski_Suomen_hyvinvointialue, reg:mdt_practice, bs:coverage:Diagnosis, q:7885b0974f, q:950a2f797b, q:f07a34a300`
- Since the Health Care Act (§52) sets no maximum time for a cancer suspicion and Keski-Suomi's pathway document does not monitor its targets, the team recommends reporting access times using THL Ohjaus 21/2016 definitions for 16 cancers with handover alerts, while the Filha programme's diagnostics recommendation with referral criteria and time limits is to be carried out before the 2030 mid-term evaluation. `rec:1, law:no_max, reg:not_monitored, thl:21_2016, q:29b792498e, q:432c0e51d6, q:614febebf2`
- Since mentor insight notes a weak referral gets a lower urgency rating and Keski-Suomi's pathway document states no referral time and names no diagnostic contact, the team recommends a KYS-style referral template, a persistent-symptoms rule after a normal X-ray, and a named diagnostic contact, while the STM roadmap (measure 1.2.3) plans care-coordinator guidance by 2026–2028 for county adoption by 2029–2031. `rec:2, mentor:kaisa_referral, reg:ks_referral, reg:named_contact, q:050ee09ebe, q:abcbb06ae3`

## Review flags (for human review only)

_Flags are for human review only; they never change the brief's status or approve it._

- [low] `how_sure_are_we.headline`: None of the claims cited for this sentence mention that county treatment shares are crude or unadjusted for age (only stage adjustment is supported by bs:coverage:Diagnosis); the crude and age-adjustment claims are cited in details[0] rather than here.

## Claims cited

- `bs:coverage:Diagnosis` (verified locally): Pathway stage 'Diagnosis' is measured in public data: yes (by county: yes (Kuva 7, 10, 13: PNG only)) — keuhkosyoparaportti_2019_2023.html, §4.1, Taulukko 2–4, Kuva 5–13
- `bs:coverage:First_specialist_visit` (verified locally): Pathway stage 'First specialist visit' is measured in public data: partly (by county: no) — keuhkosyoparaportti_2019_2023.html, §3.1, §4.2, Taulukko 5
- `bs:coverage:Imaging` (verified locally): Pathway stage 'Imaging' is measured in public data: partly (by county: partly (Kuva 7, PNG only)) — keuhkosyoparaportti_2019_2023.html, §4.1.1, Taulukko 2, Kuva 5–7
- `bs:coverage:MDT` (verified locally): Pathway stage 'MDT' is measured in public data: partly (by county: yes (Taulukko 11)) — keuhkosyoparaportti_2019_2023.html, §3.3, §4.2, Taulukko 5, 10, 11, 13
- `bs:coverage:Primary_care_occupational_health` (verified locally): Pathway stage 'Primary care / occupational health' is measured in public data: no (by county: no) — keuhkosyoparaportti_2019_2023.html, §3.3
- `bs:coverage:Referral` (verified locally): Pathway stage 'Referral' is measured in public data: no (by county: no) — keuhkosyoparaportti_2019_2023.html, whole report (no relevant data found)
- `bs:coverage:Symptoms` (verified locally): Pathway stage 'Symptoms' is measured in public data: no (by county: no) — keuhkosyoparaportti_2019_2023.html, whole report (no relevant data found)
- `bs:coverage:Treatment_start` (verified locally): Pathway stage 'Treatment start' is measured in public data: partly (by county: yes (type only, Taulukko 11)) — keuhkosyoparaportti_2019_2023.html, §4.2, §4.2.2, Taulukko 6–9, 11, 12, Kuva 14, 17
- `cty:curative:Keski_Suomen_hyvinvointialue` (verified locally): Keski-Suomen hyvinvointialue: curative treatment 27.2% (95% CI 23.9–30.7; n=173/637), not distinguishable vs national 27.0% — keuhkosyoparaportti_2019_2023.html, Taulukko 11
- `cty:life_prolonging:Keski_Suomen_hyvinvointialue` (verified locally): Keski-Suomen hyvinvointialue: life-prolonging treatment 37.2% (95% CI 33.5–41.0; n=237/637), above vs national 30.4% — keuhkosyoparaportti_2019_2023.html, Taulukko 11
- `cty:mdt_recorded:Keski_Suomen_hyvinvointialue` (verified locally): Keski-Suomen hyvinvointialue: MDT meeting recorded 3.8% (95% CI 2.5–5.5; n=24/637), below vs national 6.0% — keuhkosyoparaportti_2019_2023.html, Taulukko 11
- `cty:no_treatment_record:Keski_Suomen_hyvinvointialue` (verified locally): Keski-Suomen hyvinvointialue: no treatment record within 12 months 24.5% (95% CI 21.3–28.0; n=156/637), not distinguishable vs national 27.5% — keuhkosyoparaportti_2019_2023.html, Taulukko 11
- `cty:symptomatic:Keski_Suomen_hyvinvointialue` (verified locally): Keski-Suomen hyvinvointialue: symptomatic treatment 36.3% (95% CI 32.6–40.1; n=231/637), not distinguishable vs national 39.5% — keuhkosyoparaportti_2019_2023.html, Taulukko 11
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
- `q:29b792498e` (verified locally): Policy evidence for pathway stage 'Referral' — filha_lung_programme_2026_fi.pdf, p.16
- `q:323de0d90d` (verified locally): Report evidence for pathway stage 'Primary care / occupational health' — keuhkosyoparaportti_2019_2023.html, §3.3 Menetelmät
- `q:39e6ba43a9` (verified locally): Report evidence for pathway stage 'MDT' — keuhkosyoparaportti_2019_2023.html, §3.3 Menetelmät
- `q:432c0e51d6` (verified locally): The upcoming national diagnostics recommendation will include “suositellut aikarajat erikoissairaanhoitoon eri diagnostiikan polun vaiheille” (recommended time limits in specialist care), to be carried out (“toteutetaan”; may mean produced or implemented) before the 2030 mid-term evaluation — filha_lung_programme_2026_fi.pdf, p.16
- `q:5eb155decc` (verified locally): Report evidence for pathway stage 'Imaging' — keuhkosyoparaportti_2019_2023.html, §4.1.1 Toteamistapa
- `q:614febebf2` (verified locally): When (p.24): > “Väliarvio toteutetaan vuonna 2030, ohjelman puolivälissä ja loppuarviointi vuonna 2036. Eri > osa-alueiden suositukset toteutetaan ennen väliarviointia.” — filha_lung_programme_2026_fi.pdf, p.24
- `q:7885b0974f` (verified locally): Report evidence for pathway stage 'Diagnosis' — keuhkosyoparaportti_2019_2023.html, §4.1.3 Levinneisyystiedon kattavuus
- `q:950a2f797b` (verified locally): Reporting, collection and storage of lung cancer data is currently incomplete. — filha_lung_programme_2026_fi.pdf, p.21
- `q:abcbb06ae3` (verified locally): 2026–2028: guidance on a named doctor, nurse or specialist worker coordinating cancer care. 2029–2031: wellbeing services counties have adopted it. — roadmap_2026_2031_fi.pdf, p.32
- `q:f07a34a300` (verified locally): A national cancer care quality registry will be set up alongside THL's Cancer Registry. — roadmap_2026_2031_fi.pdf, p.59
- `rec:1` (recommendation (ours)): Team recommendation 1: Counties report access times using the THL 21/2016 definitions, with handover alerts. Each wellbeing services county reports lung cancer access times (referral → first specialist visit → diagnosis → treatment start) using the definitions in THL's Hoitoonpääsyn seuranta syövän hoidossa (Ohjaus 21/2016). Until national target times exist, flag stalled handovers. — recommendations.md, §1. Counties report access times using the THL 21/2016 definitions, with handover alerts
- `rec:2` (recommendation (ours)): Team recommendation 2: A KYS-style referral template, a persistent-symptoms rule and a named contact. Adopt a standard referral content list and template, modelled on KYS. • Add a rule for primary care: if symptoms persist after a normal X-ray, refer for a pulmonologist assessment. • Name a contact person for the diagnostic phase, from referral to diagnosis. — recommendations.md, §2. A KYS-style referral template, a persistent-symptoms rule and a named contact
- `rec:3` (recommendation (ours)): Team recommendation 3: Report recording completeness per county: stage, drug treatment, MDT coding. Publish, per county, how completely stage, drug treatment and MDT meetings are recorded. Read county ‘gaps’ in these fields as data-quality signals first. — recommendations.md, §3. Report recording completeness per county: stage, drug treatment, MDT coding
- `reg:ks_referral` (verified by Hellu): Keski-Suomi: referral handled as quickly as possible (no time stated) — pathway_brief.md, 6. Regional pathways compared
- `reg:ks_target` (verified by Hellu): Keski-Suomi: lung clinic appointment within 2–3 weeks, at the latest about 1 month — pathway_brief.md, 6. Regional pathways compared
- `reg:ks_tissue` (verified by Hellu): Keski-Suomi: tissue sample results in about 1–2 weeks — pathway_brief.md, 6. Regional pathways compared
- `reg:mdt_practice` (verified by Hellu): MDT practice differs: KYS every patient weekly, Keski-Suomi every new case, HUS when needed — pathway_brief.md, 6. Regional pathways compared
- `reg:named_contact` (verified by Hellu): No region names a contact person for the diagnostic phase — pathway_brief.md, 6. Regional pathways compared
- `reg:not_monitored` (verified by Hellu): No region says whether it meets its stated times — pathway_brief.md, 6. Regional pathways compared
- `reg:occupational` (verified by Hellu): OYS and Keski-Suomi name occupational health as a referral source — pathway_brief.md, 6. Regional pathways compared
- `thl:21_2016` (verified by Hellu): THL Ohjaus 21/2016 defines how cancer access times are recorded, for 16 cancers — pathway_brief.md, 6. Regional pathways compared
