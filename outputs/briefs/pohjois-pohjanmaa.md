# Pohjois-Pohjanmaa: lung cancer pathway brief

Status: **validated** · gemini-4-argon (thinking HIGH) · 2026-11-14T13:53:24+00:00 · attempts: 2

## Where do we lag?

**Pohjois-Pohjanmaa lags nationally in crude curative treatment at 23.6% (95% CI 21.1–26.3; n=248/1050) versus 27.0% (4009/14873) across Finland.** `cty:curative:Pohjois_Pohjanmaan_hyvinvointialue, nat:curative`

- The 95% confidence interval for Pohjois-Pohjanmaa's crude curative treatment share of 23.6% (95% CI 21.1–26.3; n=248/1050) excludes and lies below the national benchmark of 27.0% (4009/14873). `cty:curative:Pohjois_Pohjanmaan_hyvinvointialue, nat:curative`
- Because treatment categories overlap and a patient can receive several treatments, the county's crude life-prolonging share of 37.4% (95% CI 34.5–40.4; n=393/1050) has a 95% confidence interval that excludes and exceeds the national 30.4% (4522/14873), whereas crude symptomatic treatment at 38.8% (95% CI 35.9–41.7; n=407/1050) includes the national 39.5% (5871/14873). `cty:life_prolonging:Pohjois_Pohjanmaan_hyvinvointialue, nat:life_prolonging, cty:symptomatic:Pohjois_Pohjanmaan_hyvinvointialue, nat:symptomatic`
- Pohjois-Pohjanmaa's crude share of patients with a recorded MDT meeting is 1.1% (95% CI 0.7–2.0; n=12/1050), whose 95% confidence interval excludes the national 6.0% (893/14873), though MDT records measure recording practice rather than care because HILMO captures specialised procedures only from direct patient contacts. `cty:mdt_recorded:Pohjois_Pohjanmaan_hyvinvointialue, nat:mdt_recorded, bs:coverage:MDT, q:39e6ba43a9`
- In preliminary, unpublished national figures, lung cancer care in Finland takes an average of 155 days from initial symptoms to treatment, compared with 107 days in Sweden and 67 days in Denmark, comprising 56 days of patient delay, 41 days in primary care, and 58 days in specialist care. `mot:total_fi, mot:total_se, mot:total_dk, mot:patient, mot:primary, mot:specialist`

## How sure are we?

**Public registry data show crude 12-month treatment shares with 95% confidence intervals, but lack county age-adjusted tables, stage for about 48% of patients, and pathway wait times.** `fig:age_adjusted_only_kuva16, bs:coverage:Diagnosis, q:7885b0974f, bs:coverage:Treatment_start`

- The county table (Taulukko 11) reports crude shares that are not age-adjusted; county-level age-adjusted shares appear only in Kuva 16, where digitised national curative reference lines are 26.7% for men and 26.9% for women (±0.5 percentage points), with no digitised county value available here to test whether Pohjois-Pohjanmaa's gap holds after age adjustment. `fig:age_adjusted_only_kuva16, k16:curative:men:national, k16:curative:women:national`
- As a separate limitation, crude county treatment shares cannot be stage-adjusted because stage at diagnosis is missing for about 48% of new patients in the report. `fig:age_adjusted_only_kuva16, bs:coverage:Diagnosis, q:7885b0974f`
- Pohjois-Pohjanmaa's crude share with no treatment record within 12 months is 25.0% (95% CI 22.5–27.8; n=263/1050), whose 95% confidence interval includes the national 27.5% (4089/14873) and mixes untreated patients with unrecorded treatment, while a journal article finding that HILMO diagnoses match the Cancer Registry for about 90% of most cancer types concerns diagnosis concordance only. `cty:no_treatment_record:Pohjois_Pohjanmaan_hyvinvointialue, nat:no_treatment_record, bs:coverage:Treatment_start, lit:hilmo_90`
- Public report data do not measure symptoms or referrals, primary care visits are not included in the report's data, occupational health is not mentioned, imaging appears only indirectly as the clinical basis of diagnosis in approximately 20% of cases, and HILMO records whether specialist visits (93.6% nationally within 12 months) or treatments occurred within 12 months but not when. `bs:coverage:Symptoms, bs:coverage:Referral, bs:coverage:Primary_care_occupational_health, q:323de0d90d, bs:coverage:Imaging, q:5eb155decc, bs:coverage:First_specialist_visit, bs:coverage:Treatment_start`

## What should we do first?

**The team recommends tracking access times using THL 21/2016 definitions, standardising referral templates and diagnostic contacts, and publishing how completely stage, drug treatment, and MDT meetings are recorded.** `rec:1, rec:2, rec:3, thl:21_2016`

- Given Pohjois-Pohjanmaa's crude 1.1% (95% CI 0.7–2.0; n=12/1050) recorded MDT share versus 6.0% (893/14873) nationally and about 48% missing stage nationally, the team recommends publishing per county how completely stage, drug treatment, and MDT meetings are recorded while Finland lacks a cancer quality registry and lung cancer data reporting remains incomplete. `rec:3, cty:mdt_recorded:Pohjois_Pohjanmaan_hyvinvointialue, nat:mdt_recorded, bs:coverage:Diagnosis, q:7885b0974f, q:47c7e11303, q:950a2f797b, q:82d365cd2c`
- Because the Health Care Act sets no maximum time for a cancer suspicion and national pathway monitoring is lacking, the team recommends reporting access times using THL Ohjaus 21/2016 definitions for 16 cancers and flagging stalled handovers while the Filha programme's diagnostics recommendation with time limits is to be carried out before the 2030 mid-term evaluation. `rec:1, law:no_max, q:4e702a20fe, thl:21_2016, q:8c9c032c25, q:432c0e51d6, q:614febebf2`
- Supported by mentor insight that weak referrals receive lower urgency ratings and by varying local referral instructions, the team recommends a standard referral template, pulmonologist referral for persistent symptoms after a normal X-ray, and a named diagnostic-phase contact while the STM roadmap (measure 1.2.3) plans care-coordinator guidance by 2026–2028 for county adoption by 2029–2031. `rec:2, mentor:kaisa_referral, q:556431a0c2, q:82b59905ad, q:fc81032a80, q:abcbb06ae3, q:050ee09ebe`

## Review flags (for human review only)

_Flags are for human review only; they never change the brief's status or approve it._

- [low] `how_sure_are_we.headline`: The cited claims do not say that public registry data provide 95% confidence intervals for crude 12-month treatment shares; fig:age_adjusted_only_kuva16 states that Taulukko 11 gives crude shares only (while Kuva 16 has 95% CIs for age-adjusted shares). In addition, the cited claims only support missing treatment start dates rather than pathway wait times overall.

## Claims cited

- `bs:coverage:Diagnosis` (verified locally): Pathway stage 'Diagnosis' is measured in public data: yes (by county: yes (Kuva 7, 10, 13: PNG only)) — keuhkosyoparaportti_2019_2023.html, §4.1, Taulukko 2–4, Kuva 5–13
- `bs:coverage:First_specialist_visit` (verified locally): Pathway stage 'First specialist visit' is measured in public data: partly (by county: no) — keuhkosyoparaportti_2019_2023.html, §3.1, §4.2, Taulukko 5
- `bs:coverage:Imaging` (verified locally): Pathway stage 'Imaging' is measured in public data: partly (by county: partly (Kuva 7, PNG only)) — keuhkosyoparaportti_2019_2023.html, §4.1.1, Taulukko 2, Kuva 5–7
- `bs:coverage:MDT` (verified locally): Pathway stage 'MDT' is measured in public data: partly (by county: yes (Taulukko 11)) — keuhkosyoparaportti_2019_2023.html, §3.3, §4.2, Taulukko 5, 10, 11, 13
- `bs:coverage:Primary_care_occupational_health` (verified locally): Pathway stage 'Primary care / occupational health' is measured in public data: no (by county: no) — keuhkosyoparaportti_2019_2023.html, §3.3
- `bs:coverage:Referral` (verified locally): Pathway stage 'Referral' is measured in public data: no (by county: no) — keuhkosyoparaportti_2019_2023.html, whole report (no relevant data found)
- `bs:coverage:Symptoms` (verified locally): Pathway stage 'Symptoms' is measured in public data: no (by county: no) — keuhkosyoparaportti_2019_2023.html, whole report (no relevant data found)
- `bs:coverage:Treatment_start` (verified locally): Pathway stage 'Treatment start' is measured in public data: partly (by county: yes (type only, Taulukko 11)) — keuhkosyoparaportti_2019_2023.html, §4.2, §4.2.2, Taulukko 6–9, 11, 12, Kuva 14, 17
- `cty:curative:Pohjois_Pohjanmaan_hyvinvointialue` (verified locally): Pohjois-Pohjanmaan hyvinvointialue: curative treatment 23.6% (95% CI 21.1–26.3; n=248/1050), below vs national 27.0% — keuhkosyoparaportti_2019_2023.html, Taulukko 11
- `cty:life_prolonging:Pohjois_Pohjanmaan_hyvinvointialue` (verified locally): Pohjois-Pohjanmaan hyvinvointialue: life-prolonging treatment 37.4% (95% CI 34.5–40.4; n=393/1050), above vs national 30.4% — keuhkosyoparaportti_2019_2023.html, Taulukko 11
- `cty:mdt_recorded:Pohjois_Pohjanmaan_hyvinvointialue` (verified locally): Pohjois-Pohjanmaan hyvinvointialue: MDT meeting recorded 1.1% (95% CI 0.7–2.0; n=12/1050), below vs national 6.0% — keuhkosyoparaportti_2019_2023.html, Taulukko 11
- `cty:no_treatment_record:Pohjois_Pohjanmaan_hyvinvointialue` (verified locally): Pohjois-Pohjanmaan hyvinvointialue: no treatment record within 12 months 25.0% (95% CI 22.5–27.8; n=263/1050), not distinguishable vs national 27.5% — keuhkosyoparaportti_2019_2023.html, Taulukko 11
- `cty:symptomatic:Pohjois_Pohjanmaan_hyvinvointialue` (verified locally): Pohjois-Pohjanmaan hyvinvointialue: symptomatic treatment 38.8% (95% CI 35.9–41.7; n=407/1050), not distinguishable vs national 39.5% — keuhkosyoparaportti_2019_2023.html, Taulukko 11
- `fig:age_adjusted_only_kuva16` (verified locally): In the 2019–2023 report, county-level age-adjusted treatment shares appear only in Kuva 16 (a PNG figure, by sex, with 95% CIs); the county table (Taulukko 11) gives crude shares only — chart_data.md, Summary table; section 'Kuva 16 in detail'
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
- `q:432c0e51d6` (verified locally): The upcoming national diagnostics recommendation will include “suositellut aikarajat erikoissairaanhoitoon eri diagnostiikan polun vaiheille” (recommended time limits in specialist care), to be carried out (“toteutetaan”; may mean produced or implemented) before the 2030 mid-term evaluation — filha_lung_programme_2026_fi.pdf, p.16
- `q:47c7e11303` (verified locally): Finland has no quality registry for lung cancer or for any other cancer. — filha_lung_programme_2026_fi.pdf, p.21
- `q:4e702a20fe` (verified locally): Finland has no unified national system to steer the drafting of cancer-specific treatment recommendations, or the implementation and monitoring of care pathways based on them (quality and effectiveness targets/indicators, including access to care, and cancer-specific and generic PROMs). Existing recommendations and pathways, and the targets and indicators to be monitored, are not coordinated nationally. This maintains regional inequality in the availability and effectiveness of cancer care. — strategy_2026_2035_fi.pdf, p.33
- `q:556431a0c2` (verified locally): the patient is referred to specialist care according to local instructions — filha_lung_programme_2026_fi.pdf, p.15
- `q:5eb155decc` (verified locally): Report evidence for pathway stage 'Imaging' — keuhkosyoparaportti_2019_2023.html, §4.1.1 Toteamistapa
- `q:614febebf2` (verified locally): When (p.24): > “Väliarvio toteutetaan vuonna 2030, ohjelman puolivälissä ja loppuarviointi vuonna 2036. Eri > osa-alueiden suositukset toteutetaan ennen väliarviointia.” — filha_lung_programme_2026_fi.pdf, p.24
- `q:7885b0974f` (verified locally): Report evidence for pathway stage 'Diagnosis' — keuhkosyoparaportti_2019_2023.html, §4.1.3 Levinneisyystiedon kattavuus
- `q:82b59905ad` (verified locally): the organisation of care varies by wellbeing services county — filha_lung_programme_2026_fi.pdf, p.15
- `q:82d365cd2c` (verified locally): “Tällä hetkellä keuhkosyöpään liittyvien tietojen raportointi, kerääminen ja tallentaminen on puutteellista”; nationally uniform recording instructions (“yhtenäiset kirjaamisohjeet”) must be ensured — filha_lung_programme_2026_fi.pdf, p.21
- `q:8c9c032c25` (verified locally): Policy evidence for pathway stage 'Referral' — filha_lung_programme_2026_fi.pdf, p.16
- `q:950a2f797b` (verified locally): Reporting, collection and storage of lung cancer data is currently incomplete. — filha_lung_programme_2026_fi.pdf, p.21
- `q:abcbb06ae3` (verified locally): 2026–2028: guidance on a named doctor, nurse or specialist worker coordinating cancer care. 2029–2031: wellbeing services counties have adopted it. — roadmap_2026_2031_fi.pdf, p.32
- `q:fc81032a80` (verified locally): Measure 1.2.3: Create an operating model and guidance for a named worker responsible for coordinating cancer care. — roadmap_2026_2031_fi.pdf, p.32
- `rec:1` (recommendation (ours)): Team recommendation 1: Counties report access times using the THL 21/2016 definitions, with handover alerts. Each wellbeing services county reports lung cancer access times (referral → first specialist visit → diagnosis → treatment start) using the definitions in THL's Hoitoonpääsyn seuranta syövän hoidossa (Ohjaus 21/2016). Until national target times exist, flag stalled handovers. — recommendations.md, §1. Counties report access times using the THL 21/2016 definitions, with handover alerts
- `rec:2` (recommendation (ours)): Team recommendation 2: A KYS-style referral template, a persistent-symptoms rule and a named contact. Adopt a standard referral content list and template, modelled on KYS. • Add a rule for primary care: if symptoms persist after a normal X-ray, refer for a pulmonologist assessment. • Name a contact person for the diagnostic phase, from referral to diagnosis. — recommendations.md, §2. A KYS-style referral template, a persistent-symptoms rule and a named contact
- `rec:3` (recommendation (ours)): Team recommendation 3: Report recording completeness per county: stage, drug treatment, MDT coding. Publish, per county, how completely stage, drug treatment and MDT meetings are recorded. Read county ‘gaps’ in these fields as data-quality signals first. — recommendations.md, §3. Report recording completeness per county: stage, drug treatment, MDT coding
- `thl:21_2016` (verified by Hellu): THL Ohjaus 21/2016 defines how cancer access times are recorded, for 16 cancers — pathway_brief.md, 6. Regional pathways compared
