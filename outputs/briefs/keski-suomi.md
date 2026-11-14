# Keski-Suomi: lung cancer pathway brief

Status: **validated** · gemini-4-argon (thinking HIGH) · 2026-11-14T12:06:00+00:00 · attempts: 1

## Where do we lag?

**Keski-Suomi lags nationally in crude recorded multidisciplinary team meetings at 3.8% (95% CI 2.5–5.5; n=24/637) versus 6.0% (893/14873), and its regional pathway document lacks referral time limits.** `cty:mdt_recorded:Keski_Suomen_hyvinvointialue, nat:mdt_recorded, reg:ks_referral`

- The county's crude recorded MDT share of 3.8% (95% CI 2.5–5.5; n=24/637) has a 95% confidence interval that excludes the national 6.0% (893/14873), even though Keski-Suomi's regional pathway document states every new case is reviewed in an MDT, because HILMO records only direct patient contacts and measures recording practice rather than care. `cty:mdt_recorded:Keski_Suomen_hyvinvointialue, nat:mdt_recorded, reg:mdt_practice, bs:coverage:MDT, q:39e6ba43a9`
- Across overlapping treatment categories, crude county shares include the national value within their 95% confidence intervals for curative care at 27.2% (95% CI 23.9–30.7; n=173/637) versus 27.0% (4009/14873) and symptomatic care at 36.3% (95% CI 32.6–40.1; n=231/637) versus 39.5% (5871/14873), whereas crude life-prolonging care at 37.2% (95% CI 33.5–41.0; n=237/637) excludes the national 30.4% (4522/14873). `cty:curative:Keski_Suomen_hyvinvointialue, nat:curative, cty:symptomatic:Keski_Suomen_hyvinvointialue, nat:symptomatic, cty:life_prolonging:Keski_Suomen_hyvinvointialue, nat:life_prolonging`
- Keski-Suomi's regional pathway document targets a lung clinic appointment within 2–3 weeks or at latest about 1 month and tissue sample results in about 1–2 weeks, but it states referrals are handled as quickly as possible without a time limit, names no diagnostic contact person, and does not report whether target times are met. `reg:ks_target, reg:ks_tissue, reg:ks_referral, reg:named_contact, reg:not_monitored`
- In preliminary, unpublished national figures, time from symptoms to treatment averages 155 days in Finland versus 107 days in Sweden and 67 days in Denmark—with 56 days of patient delay, 41 days in primary care, and 58 days in specialist care—and the Health Care Act sets no legal maximum time for a cancer suspicion. `mot:total_fi, mot:total_se, mot:total_dk, mot:patient, mot:primary, mot:specialist, law:no_max`

## How sure are we?

**Public registry data show 12-month treatment types, but county shares are crude, stage at diagnosis is often missing, and public data lack primary care, referral, and waiting-time timestamps.** `bs:coverage:Diagnosis, q:7885b0974f, bs:coverage:Primary_care_occupational_health, bs:coverage:Referral, bs:coverage:Treatment_start`

- County shares are crude—unadjusted for age or stage because stage at diagnosis is frequently missing—and while national age-adjusted curative reference values exist in Kuva 16 (digitised from a figure at ±0.5 percentage points: 26.7% for men, 26.9% for women), Keski-Suomi's crude 27.2% (95% CI 23.9–30.7; n=173/637) already includes the national 27.0% (4009/14873). `cty:curative:Keski_Suomen_hyvinvointialue, nat:curative, k16:curative:men:national, k16:curative:women:national, bs:coverage:Diagnosis, q:7885b0974f`
- Keski-Suomi's crude share with no treatment record within 12 months—mixing patients without treatment and unrecorded treatment—is 24.5% (95% CI 21.3–28.0; n=156/637), whose 95% confidence interval includes the national 27.5% (4089/14873); as an inference, not a finding, this is consistent with relatively complete treatment recording, while a journal article on about 90% HILMO concordance covers diagnoses only. `cty:no_treatment_record:Keski_Suomen_hyvinvointialue, nat:no_treatment_record, bs:coverage:Treatment_start, lit:hilmo_90`
- Public report data do not measure symptom onset, referral dates, or when treatment started; outpatient primary care visits are not included in the report's data and occupational health is not mentioned, imaging appears only indirectly as the diagnostic basis in approximately 20% of cases, and specialist visits (93.6% nationally within 12 months) lack county breakdowns or dates. `bs:coverage:Symptoms, bs:coverage:Primary_care_occupational_health, q:323de0d90d, bs:coverage:Referral, bs:coverage:Imaging, q:5eb155decc, bs:coverage:First_specialist_visit, bs:coverage:Treatment_start`

## What should we do first?

**The team recommends reporting access times using THL guidance 21/2016 definitions with handover alerts, standardising referrals with a named diagnostic contact, and publishing county recording completeness.** `rec:1, rec:2, rec:3, thl:21_2016`

- The team recommends reporting access times using THL guidance 21/2016 definitions and flagging stalled handovers, since Keski-Suomi's regional pathway document lacks referral time limits and monitoring data, while the roadmap plans pathway target times by 2026–2028 and the Filha programme's diagnostics recommendation with time limits is due before the 2030 mid-term evaluation. `rec:1, thl:21_2016, q:24169121a4, reg:ks_referral, reg:not_monitored, q:4e702a20fe, q:def306014c, q:432c0e51d6, q:614febebf2`
- The team recommends a standard referral template, a rule to refer persistent symptoms after a normal X-ray to a pulmonologist, and a named diagnostic contact—absent from regional pathway documents—supported by mentor insight that weak referrals get lower urgency ratings and roadmap plans for referral criteria and coordinator guidance in 2026–2028 (adopted in 2029–2031). `rec:2, mentor:kaisa_referral, reg:named_contact, q:556431a0c2, q:37bb4c3b38, q:c61439b30f, q:fc81032a80, q:abcbb06ae3, q:050ee09ebe`
- The team recommends publishing county recording completeness for stage, drug treatment, and MDT coding—reading Keski-Suomi's crude 3.8% (95% CI 2.5–5.5; n=24/637) recorded MDT share, whose 95% confidence interval excludes the national 6.0% (893/14873), as a recording gap—while a national quality registry targeting 90% coverage including stage is planned alongside the Cancer Registry. `rec:3, cty:mdt_recorded:Keski_Suomen_hyvinvointialue, nat:mdt_recorded, bs:coverage:MDT, q:950a2f797b, q:4c7a01d84c, q:f07a34a300, q:4a856bd695`

## Review flags (for human review only)

_Flags are for human review only; they never change the brief's status or approve it._

- [low] `how_sure_are_we.details[2]`: The cited quote (q:5eb155decc) attributes the approximately 20% share to clinical examination alone, giving imaging as an example ('clinical examination alone, such as imaging, in approximately 20%'), rather than to imaging specifically.

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
- `q:24169121a4` (verified locally): Strategy p.5 (= PDF p.5), “Strategiset tavoitteet”, indicator under “Varmistetaan yhdenvertainen ja vaikuttava syövänhoito”: > “Potilaat pääsevät hoitoon tavoiteaikojen puitteissa” > “ THL (Ohjaus 21/2016). Hoitoonpääsyn seuranta syövän hoidossa.” — strategy_2026_2035_fi.pdf, p.5
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
- `q:950a2f797b` (verified locally): Reporting, collection and storage of lung cancer data is currently incomplete. — filha_lung_programme_2026_fi.pdf, p.21
- `q:abcbb06ae3` (verified locally): 2026–2028: guidance on a named doctor, nurse or specialist worker coordinating cancer care. 2029–2031: wellbeing services counties have adopted it. — roadmap_2026_2031_fi.pdf, p.32
- `q:c61439b30f` (verified locally): 2026–2028: standardised referral criteria and symptom-based models included in the national pathways of at least the five most common cancers. — roadmap_2026_2031_fi.pdf, p.53
- `q:def306014c` (verified locally): p.57, timetable: > “2026–2028: Kansalliset hoitoketjukuvaukset tehty viidestä syövästä ja syöpäkohtaiset > hoitoonpääsyajat on määritetty.” — roadmap_2026_2031_fi.pdf, p.57
- `q:f07a34a300` (verified locally): A national cancer care quality registry will be set up alongside THL's Cancer Registry. — roadmap_2026_2031_fi.pdf, p.59
- `q:fc81032a80` (verified locally): Measure 1.2.3: Create an operating model and guidance for a named worker responsible for coordinating cancer care. — roadmap_2026_2031_fi.pdf, p.32
- `rec:1` (recommendation (ours)): Team recommendation 1: Counties report access times using the THL 21/2016 definitions, with handover alerts. Each wellbeing services county reports lung cancer access times (referral → first specialist visit → diagnosis → treatment start) using the definitions in THL's Hoitoonpääsyn seuranta syövän hoidossa (Ohjaus 21/2016). Until national target times exist, flag stalled handovers. — recommendations.md, §1. Counties report access times using the THL 21/2016 definitions, with handover alerts
- `rec:2` (recommendation (ours)): Team recommendation 2: A KYS-style referral template, a persistent-symptoms rule and a named contact. Adopt a standard referral content list and template, modelled on KYS. • Add a rule for primary care: if symptoms persist after a normal X-ray, refer for a pulmonologist assessment. • Name a contact person for the diagnostic phase, from referral to diagnosis. — recommendations.md, §2. A KYS-style referral template, a persistent-symptoms rule and a named contact
- `rec:3` (recommendation (ours)): Team recommendation 3: Report recording completeness per county: stage, drug treatment, MDT coding. Publish, per county, how completely stage, drug treatment and MDT meetings are recorded. Read county ‘gaps’ in these fields as data-quality signals first. — recommendations.md, §3. Report recording completeness per county: stage, drug treatment, MDT coding
- `reg:ks_referral` (verified by Hellu): Keski-Suomi: referral handled as quickly as possible (no time stated) — pathway_brief.md, 6. Regional pathways compared
- `reg:ks_target` (verified by Hellu): Keski-Suomi: lung clinic appointment within 2–3 weeks, at the latest about 1 month — pathway_brief.md, 6. Regional pathways compared
- `reg:ks_tissue` (verified by Hellu): Keski-Suomi: tissue sample results in about 1–2 weeks — pathway_brief.md, 6. Regional pathways compared
- `reg:mdt_practice` (verified by Hellu): MDT practice differs: KYS every patient weekly, Keski-Suomi every new case, HUS when needed — pathway_brief.md, 6. Regional pathways compared
- `reg:named_contact` (verified by Hellu): No region names a contact person for the diagnostic phase — pathway_brief.md, 6. Regional pathways compared
- `reg:not_monitored` (verified by Hellu): No region says whether it meets its stated times — pathway_brief.md, 6. Regional pathways compared
- `thl:21_2016` (verified by Hellu): THL Ohjaus 21/2016 defines how cancer access times are recorded, for 16 cancers — pathway_brief.md, 6. Regional pathways compared
