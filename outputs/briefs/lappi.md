# Lappi: lung cancer pathway brief

Status: **validated** · gemini-4-argon (thinking HIGH) · 2026-11-14T13:20:48+00:00 · attempts: 2

## Where do we lag?

**In Lapin hyvinvointialue, crude shares for overlapping curative (18.5% vs 27.0% nationally) and life-prolonging (16.1% vs 30.4% nationally) treatment categories lag behind national benchmarks.** `cty:curative:Lapin_hyvinvointialue, nat:curative, cty:life_prolonging:Lapin_hyvinvointialue, nat:life_prolonging`

- Among overlapping treatment categories where a patient can receive several treatments, the county's crude curative share is 18.5% (95% CI 15.8–21.5; n=131/710) versus 27.0% (4009/14873) nationally, and its crude life-prolonging share is 16.1% (95% CI 13.5–18.9; n=114/710) versus 30.4% (4522/14873) nationally, with each 95% confidence interval excluding the national value. `cty:curative:Lapin_hyvinvointialue, nat:curative, cty:life_prolonging:Lapin_hyvinvointialue, nat:life_prolonging`
- The crude symptomatic treatment share, which overlaps with other treatment categories, is 44.5% (95% CI 40.9–48.2; n=316/710) versus 39.5% (5871/14873) nationally, while the crude share with no treatment record within 12 months—mixing untreated patients and unrecorded treatment—is 33.8% (95% CI 30.4–37.4; n=240/710) versus 27.5% (4089/14873) nationally, with each 95% confidence interval excluding the national value. `cty:symptomatic:Lapin_hyvinvointialue, nat:symptomatic, cty:no_treatment_record:Lapin_hyvinvointialue, nat:no_treatment_record, bs:coverage:Treatment_start`
- A multidisciplinary team (MDT) meeting is recorded for a crude share of 3.0% (95% CI 1.9–4.5; n=21/710) of patients in Lapin hyvinvointialue versus 6.0% (893/14873) nationally, with the 95% confidence interval excluding the national value, though HILMO MDT codes require direct patient contact and measure recording practice, not care. `cty:mdt_recorded:Lapin_hyvinvointialue, nat:mdt_recorded, bs:coverage:MDT, q:39e6ba43a9`
- At the national level, preliminary, unpublished figures indicate that lung cancer care in Finland takes an average of 155 days from initial symptoms to treatment—comprising 56 days of patient delay, 41 days in primary care and 58 days in specialist care—compared with 107 days in Sweden and 67 days in Denmark. `mot:total_fi, mot:total_se, mot:total_dk, mot:patient, mot:primary, mot:specialist`

## How sure are we?

**Although 95% confidence intervals exclude national values, Lapin hyvinvointialue's crude shares across overlapping treatment categories lack age and stage adjustment and may partly reflect unrecorded treatment.** `cty:curative:Lapin_hyvinvointialue, cty:no_treatment_record:Lapin_hyvinvointialue, bs:coverage:Diagnosis`

- Read as a data-quality signal, the county's crude 33.8% (95% CI 30.4–37.4) no-treatment-record share is above 27.5% nationally, meaning low crude shares in overlapping treatment categories may partly reflect unrecorded treatment, while a journal article's finding of about 90% HILMO–Cancer Registry concordance concerns diagnoses only, not treatment, referral or MDT recording. `cty:no_treatment_record:Lapin_hyvinvointialue, nat:no_treatment_record, cty:curative:Lapin_hyvinvointialue, cty:life_prolonging:Lapin_hyvinvointialue, lit:hilmo_90`
- The county shares are crude and have separate limitations: they are not age-adjusted—age-adjusted shares exist only in Kuva 16 for curative treatment by sex, with digitised national reference lines (±0.5 percentage points) of 26.7% for men and 26.9% for women—and, separately, they cannot be stage-adjusted because diagnosis stage is missing for about 48% of patients. `cty:curative:Lapin_hyvinvointialue, k16:curative:men:national, k16:curative:women:national, bs:coverage:Diagnosis, q:7885b0974f`
- Public registry data cannot show where delays occur: symptom onset and referrals are not measured, primary care visits are not included in the report's data, occupational health is not mentioned, imaging appears only indirectly as the diagnosis basis in approximately 20% of patients, and HILMO lacks specialist-visit and treatment-start timestamps. `bs:coverage:Symptoms, bs:coverage:Primary_care_occupational_health, q:323de0d90d, bs:coverage:Imaging, q:5eb155decc, bs:coverage:Referral, bs:coverage:First_specialist_visit, bs:coverage:Treatment_start`

## What should we do first?

**The team recommends auditing recording completeness for Lapin hyvinvointialue's crude shares across overlapping categories, tracking access times using THL 21/2016 definitions, and standardising referrals and diagnostic coordination.** `rec:1, rec:2, rec:3, cty:no_treatment_record:Lapin_hyvinvointialue, cty:mdt_recorded:Lapin_hyvinvointialue, thl:21_2016`

- Because Lapin hyvinvointialue has a 33.8% (95% CI 30.4–37.4) crude no-treatment-record share and a 3.0% (95% CI 1.9–4.5) crude MDT-recorded share among overlapping categories alongside incomplete national data and 48% missing stage, the team recommends reporting county recording completeness for stage, drug treatment and MDT coding while THL, FICAN and the Cancer Registry assess a lung cancer quality registry. `rec:3, cty:no_treatment_record:Lapin_hyvinvointialue, cty:mdt_recorded:Lapin_hyvinvointialue, bs:coverage:Diagnosis, q:7885b0974f, q:950a2f797b, q:82d365cd2c, filha:registry`
- Since the Health Care Act §52 sets no legal maximum wait for a cancer suspicion and Finland lacks uniform diagnostic timetables, the team recommends reporting access times using THL Ohjaus 21/2016 definitions for 16 cancers with handover alerts, while the Filha programme's diagnostics recommendation with recommended time limits is to be carried out before the 2030 mid-term evaluation. `rec:1, law:no_max, thl:21_2016, q:20d6ca414e, q:432c0e51d6, q:614febebf2`
- Because mentor insight indicates that weak referrals receive lower specialist urgency ratings and reviewed regional pathway documents name no diagnostic-phase contact person, the team recommends adopting a KYS-modelled referral template and persistent-symptoms referral rule, alongside naming a diagnostic contact person while STM roadmap measure 1.2.3 plans care-coordinator guidance by 2026–2028 for county adoption by 2029–2031. `rec:2, mentor:kaisa_referral, reg:kys_template, reg:kys_persistent, reg:only_kys_xray, reg:named_contact, q:fc81032a80, q:abcbb06ae3, q:050ee09ebe`

## Review flags (for human review only)

_Flags are for human review only; they never change the brief's status or approve it._

- [low] `what_to_do_first.headline`: Team recommendation 3 ([rec:3]) recommends reporting and publishing county-level recording completeness for stage, drug treatment, and MDT coding, not auditing recording completeness for crude treatment shares.
- [low] `what_to_do_first.details[0]`: The cited claims ([bs:coverage:Diagnosis] and [q:7885b0974f]) state that stage at diagnosis is missing for 'nearly half' (~48%) of new patients, whereas '48% missing stage' omits the approximation.

## Claims cited

- `bs:coverage:Diagnosis` (verified locally): Pathway stage 'Diagnosis' is measured in public data: yes (by county: yes (Kuva 7, 10, 13: PNG only)) — keuhkosyoparaportti_2019_2023.html, §4.1, Taulukko 2–4, Kuva 5–13
- `bs:coverage:First_specialist_visit` (verified locally): Pathway stage 'First specialist visit' is measured in public data: partly (by county: no) — keuhkosyoparaportti_2019_2023.html, §3.1, §4.2, Taulukko 5
- `bs:coverage:Imaging` (verified locally): Pathway stage 'Imaging' is measured in public data: partly (by county: partly (Kuva 7, PNG only)) — keuhkosyoparaportti_2019_2023.html, §4.1.1, Taulukko 2, Kuva 5–7
- `bs:coverage:MDT` (verified locally): Pathway stage 'MDT' is measured in public data: partly (by county: yes (Taulukko 11)) — keuhkosyoparaportti_2019_2023.html, §3.3, §4.2, Taulukko 5, 10, 11, 13
- `bs:coverage:Primary_care_occupational_health` (verified locally): Pathway stage 'Primary care / occupational health' is measured in public data: no (by county: no) — keuhkosyoparaportti_2019_2023.html, §3.3
- `bs:coverage:Referral` (verified locally): Pathway stage 'Referral' is measured in public data: no (by county: no) — keuhkosyoparaportti_2019_2023.html, whole report (no relevant data found)
- `bs:coverage:Symptoms` (verified locally): Pathway stage 'Symptoms' is measured in public data: no (by county: no) — keuhkosyoparaportti_2019_2023.html, whole report (no relevant data found)
- `bs:coverage:Treatment_start` (verified locally): Pathway stage 'Treatment start' is measured in public data: partly (by county: yes (type only, Taulukko 11)) — keuhkosyoparaportti_2019_2023.html, §4.2, §4.2.2, Taulukko 6–9, 11, 12, Kuva 14, 17
- `cty:curative:Lapin_hyvinvointialue` (verified locally): Lapin hyvinvointialue: curative treatment 18.5% (95% CI 15.8–21.5; n=131/710), below vs national 27.0% — keuhkosyoparaportti_2019_2023.html, Taulukko 11
- `cty:life_prolonging:Lapin_hyvinvointialue` (verified locally): Lapin hyvinvointialue: life-prolonging treatment 16.1% (95% CI 13.5–18.9; n=114/710), below vs national 30.4% — keuhkosyoparaportti_2019_2023.html, Taulukko 11
- `cty:mdt_recorded:Lapin_hyvinvointialue` (verified locally): Lapin hyvinvointialue: MDT meeting recorded 3.0% (95% CI 1.9–4.5; n=21/710), below vs national 6.0% — keuhkosyoparaportti_2019_2023.html, Taulukko 11
- `cty:no_treatment_record:Lapin_hyvinvointialue` (verified locally): Lapin hyvinvointialue: no treatment record within 12 months 33.8% (95% CI 30.4–37.4; n=240/710), above vs national 27.5% — keuhkosyoparaportti_2019_2023.html, Taulukko 11
- `cty:symptomatic:Lapin_hyvinvointialue` (verified locally): Lapin hyvinvointialue: symptomatic treatment 44.5% (95% CI 40.9–48.2; n=316/710), above vs national 39.5% — keuhkosyoparaportti_2019_2023.html, Taulukko 11
- `filha:registry` (verified locally): No lung cancer or other cancer quality registry; Cancer Registry, THL and FICAN are assessing one, starting with lung cancer — pathway_brief.md, 3. National level: a programme, but no pathway or time targets
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
- `q:20d6ca414e` (verified locally): “Valtakunnallisesti ei ole ollut tarkkaa yhtenäistä ohjeistusta siitä, millä aikataululla diagnostiikan eri osa-alueet tulisi olla tehtyinä”; regional variation in diagnostic speed is large. The programme itself sets no day-based targets — filha_lung_programme_2026_fi.pdf, p.4
- `q:323de0d90d` (verified locally): Report evidence for pathway stage 'Primary care / occupational health' — keuhkosyoparaportti_2019_2023.html, §3.3 Menetelmät
- `q:39e6ba43a9` (verified locally): Report evidence for pathway stage 'MDT' — keuhkosyoparaportti_2019_2023.html, §3.3 Menetelmät
- `q:432c0e51d6` (verified locally): The upcoming national diagnostics recommendation will include “suositellut aikarajat erikoissairaanhoitoon eri diagnostiikan polun vaiheille” (recommended time limits in specialist care), to be carried out (“toteutetaan”; may mean produced or implemented) before the 2030 mid-term evaluation — filha_lung_programme_2026_fi.pdf, p.16
- `q:5eb155decc` (verified locally): Report evidence for pathway stage 'Imaging' — keuhkosyoparaportti_2019_2023.html, §4.1.1 Toteamistapa
- `q:614febebf2` (verified locally): When (p.24): > “Väliarvio toteutetaan vuonna 2030, ohjelman puolivälissä ja loppuarviointi vuonna 2036. Eri > osa-alueiden suositukset toteutetaan ennen väliarviointia.” — filha_lung_programme_2026_fi.pdf, p.24
- `q:7885b0974f` (verified locally): Report evidence for pathway stage 'Diagnosis' — keuhkosyoparaportti_2019_2023.html, §4.1.3 Levinneisyystiedon kattavuus
- `q:82d365cd2c` (verified locally): “Tällä hetkellä keuhkosyöpään liittyvien tietojen raportointi, kerääminen ja tallentaminen on puutteellista”; nationally uniform recording instructions (“yhtenäiset kirjaamisohjeet”) must be ensured — filha_lung_programme_2026_fi.pdf, p.21
- `q:950a2f797b` (verified locally): Reporting, collection and storage of lung cancer data is currently incomplete. — filha_lung_programme_2026_fi.pdf, p.21
- `q:abcbb06ae3` (verified locally): 2026–2028: guidance on a named doctor, nurse or specialist worker coordinating cancer care. 2029–2031: wellbeing services counties have adopted it. — roadmap_2026_2031_fi.pdf, p.32
- `q:fc81032a80` (verified locally): Measure 1.2.3: Create an operating model and guidance for a named worker responsible for coordinating cancer care. — roadmap_2026_2031_fi.pdf, p.32
- `rec:1` (recommendation (ours)): Team recommendation 1: Counties report access times using the THL 21/2016 definitions, with handover alerts. Each wellbeing services county reports lung cancer access times (referral → first specialist visit → diagnosis → treatment start) using the definitions in THL's Hoitoonpääsyn seuranta syövän hoidossa (Ohjaus 21/2016). Until national target times exist, flag stalled handovers. — recommendations.md, §1. Counties report access times using the THL 21/2016 definitions, with handover alerts
- `rec:2` (recommendation (ours)): Team recommendation 2: A KYS-style referral template, a persistent-symptoms rule and a named contact. Adopt a standard referral content list and template, modelled on KYS. • Add a rule for primary care: if symptoms persist after a normal X-ray, refer for a pulmonologist assessment. • Name a contact person for the diagnostic phase, from referral to diagnosis. — recommendations.md, §2. A KYS-style referral template, a persistent-symptoms rule and a named contact
- `rec:3` (recommendation (ours)): Team recommendation 3: Report recording completeness per county: stage, drug treatment, MDT coding. Publish, per county, how completely stage, drug treatment and MDT meetings are recorded. Read county ‘gaps’ in these fields as data-quality signals first. — recommendations.md, §3. Report recording completeness per county: stage, drug treatment, MDT coding
- `reg:kys_persistent` (verified by Hellu): KYS: refer persistent unexplained symptoms even if the X-ray is clear — pathway_brief.md, 6. Regional pathways compared
- `reg:kys_template` (verified by Hellu): Only KYS lists required referral content and provides a referral template — pathway_brief.md, 6. Regional pathways compared
- `reg:named_contact` (verified by Hellu): No region names a contact person for the diagnostic phase — pathway_brief.md, 6. Regional pathways compared
- `reg:only_kys_xray` (verified by Hellu): Only KYS tells primary care what to do with a normal X-ray and continuing symptoms — pathway_brief.md, 6. Regional pathways compared
- `thl:21_2016` (verified by Hellu): THL Ohjaus 21/2016 defines how cancer access times are recorded, for 16 cancers — pathway_brief.md, 6. Regional pathways compared
