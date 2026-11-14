# Lappi: lung cancer pathway brief

Status: **validated** · gemini-4-argon (thinking HIGH) · 2026-11-14T12:14:20+00:00 · attempts: 1

## Where do we lag?

**In Lapin hyvinvointialue, crude curative and life-prolonging treatment shares lag national values, while the crude share with no treatment record within 12 months exceeds the national share.** `cty:curative:Lapin_hyvinvointialue, cty:life_prolonging:Lapin_hyvinvointialue, cty:no_treatment_record:Lapin_hyvinvointialue, nat:curative, nat:life_prolonging, nat:no_treatment_record`

- The county's crude curative treatment share is 18.5% (95% CI 15.8–21.5; n=131/710) versus 27.0% (4009/14873) nationally, and its crude life-prolonging treatment share is 16.1% (95% CI 13.5–18.9; n=114/710) versus 30.4% (4522/14873) nationally, with the 95% confidence intervals excluding the national values. `cty:curative:Lapin_hyvinvointialue, nat:curative, cty:life_prolonging:Lapin_hyvinvointialue, nat:life_prolonging`
- Across overlapping treatment categories, the crude symptomatic treatment share is 44.5% (95% CI 40.9–48.2; n=316/710) versus 39.5% (5871/14873) nationally, and the crude share with no treatment record within 12 months is 33.8% (95% CI 30.4–37.4; n=240/710) versus 27.5% (4089/14873) nationally, with the 95% confidence intervals excluding the national values. `cty:symptomatic:Lapin_hyvinvointialue, nat:symptomatic, cty:no_treatment_record:Lapin_hyvinvointialue, nat:no_treatment_record`
- The crude share with a recorded multidisciplinary team (MDT) meeting is 3.0% (95% CI 1.9–4.5; n=21/710) versus 6.0% (893/14873) nationally, with the 95% confidence interval excluding the national value, though HILMO MDT codes come only from direct patient contacts and measure recording practice rather than care. `cty:mdt_recorded:Lapin_hyvinvointialue, nat:mdt_recorded, bs:coverage:MDT, q:39e6ba43a9`
- Nationally, preliminary, unpublished figures show an average of 155 days from first symptoms to treatment in Finland, compared with 107 in Sweden and 67 in Denmark, including 56 days of patient delay, 41 days in primary care, and 58 days in specialist care. `mot:total_fi, mot:total_se, mot:total_dk, mot:patient, mot:primary, mot:specialist`

## How sure are we?

**County treatment shares are crude and unadjusted for age or stage, and the elevated crude share with no treatment record suggests low treatment shares may partly reflect unrecorded care.** `cty:no_treatment_record:Lapin_hyvinvointialue, cty:curative:Lapin_hyvinvointialue, cty:life_prolonging:Lapin_hyvinvointialue, bs:coverage:Diagnosis, bs:coverage:Treatment_start`

- Because the county's crude 33.8% share with no treatment record within 12 months is above the 27.5% national value and mixes untreated patients with unrecorded treatment, we infer as a data-quality signal that the low crude 18.5% curative and 16.1% life-prolonging shares may partly reflect unrecorded treatment. `cty:no_treatment_record:Lapin_hyvinvointialue, nat:no_treatment_record, cty:curative:Lapin_hyvinvointialue, cty:life_prolonging:Lapin_hyvinvointialue, bs:coverage:Treatment_start`
- While national age-adjusted curative treatment shares digitised from a figure (about ±0.5 percentage points) are 26.7% for men and 26.9% for women, the county shares are crude—not adjusted for age or stage—and stage at diagnosis is missing for a large share of new patients. `k16:curative:men:national, k16:curative:women:national, cty:curative:Lapin_hyvinvointialue, bs:coverage:Diagnosis, q:7885b0974f`
- A journal article found that HILMO diagnoses match the Cancer Registry for about 90% of most cancer types, which concerns diagnosis concordance only; Finland has no cancer quality registry, and reporting, collection, and storage of lung cancer data are currently incomplete. `lit:hilmo_90, filha:registry, q:47c7e11303, q:950a2f797b`
- In public data, primary care visits are not included in the report's data, occupational health is not mentioned, symptoms and referrals are not measured, and the report tracks whether a specialist visit or treatment type occurred within 12 months rather than when it started. `bs:coverage:Symptoms, bs:coverage:Referral, bs:coverage:Primary_care_occupational_health, q:323de0d90d, bs:coverage:First_specialist_visit, bs:coverage:Treatment_start`

## What should we do first?

**The team recommends publishing recording completeness for stage, drug treatment, and MDT coding, reporting access times using THL guidance 21/2016 definitions, and standardising referrals and diagnostic coordination.** `rec:1, rec:2, rec:3, thl:21_2016, q:950a2f797b, q:37bb4c3b38`

- Given the county's 33.8% crude share with no treatment record within 12 months and 3.0% crude MDT share, the team recommends publishing county recording completeness for stage, drug treatment, and MDT coding to read gaps as data-quality signals first, while a national quality registry (targeting 90% coverage including stage) and uniform recording instructions are planned. `rec:3, cty:no_treatment_record:Lapin_hyvinvointialue, cty:mdt_recorded:Lapin_hyvinvointialue, filha:registry, q:f07a34a300, q:4a856bd695, q:82d365cd2c, q:0c7bf2dacb`
- Because the Health Care Act sets no maximum time for a cancer suspicion and national access-time monitoring is lacking, the team recommends reporting referral-to-treatment access times using THL guidance 21/2016 definitions and flagging stalled handovers while the roadmap plans target access times by 2026–2028 and Filha's diagnostics recommendation is due before the 2030 mid-term evaluation. `rec:1, law:no_max, thl:21_2016, q:4e702a20fe, q:24169121a4, q:def306014c, q:432c0e51d6, q:614febebf2`
- Given the 18.5% crude curative share and the mentor insight that a weak referral gets a lower urgency rating in specialist care, the team recommends a standard referral content list and template, pulmonologist referral for persistent symptoms after a normal X-ray, and a named diagnostic-phase contact while the roadmap plans referral criteria and coordinator guidance by 2026–2028 (adopted by 2029–2031). `rec:2, cty:curative:Lapin_hyvinvointialue, mentor:kaisa_referral, q:9a1cd194f5, q:c61439b30f, q:abcbb06ae3, q:050ee09ebe`

## Review flags (for human review only)

_Flags are for human review only; they never change the brief's status or approve it._

- none

## Claims cited

- `bs:coverage:Diagnosis` (verified locally): Pathway stage 'Diagnosis' is measured in public data: yes (by county: yes (Kuva 7, 10, 13: PNG only)) — keuhkosyoparaportti_2019_2023.html, §4.1, Taulukko 2–4, Kuva 5–13
- `bs:coverage:First_specialist_visit` (verified locally): Pathway stage 'First specialist visit' is measured in public data: partly (by county: no) — keuhkosyoparaportti_2019_2023.html, §3.1, §4.2, Taulukko 5
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
- `q:0c7bf2dacb` (verified locally): p.56, content of pathways: > “Ketjuissa määritellään ja sovitaan mm. työnjaosta eri toimijoiden välillä, tavoitelluista > hoitoonpääsyajoista, keskeisistä laatu- ja vaikuttavuusindikaattoreista sekä kirjaamis- ja > koodistokäytännöistä.” — roadmap_2026_2031_fi.pdf, p.56
- `q:24169121a4` (verified locally): Strategy p.5 (= PDF p.5), “Strategiset tavoitteet”, indicator under “Varmistetaan yhdenvertainen ja vaikuttava syövänhoito”: > “Potilaat pääsevät hoitoon tavoiteaikojen puitteissa” > “ THL (Ohjaus 21/2016). Hoitoonpääsyn seuranta syövän hoidossa.” — strategy_2026_2035_fi.pdf, p.5
- `q:323de0d90d` (verified locally): Report evidence for pathway stage 'Primary care / occupational health' — keuhkosyoparaportti_2019_2023.html, §3.3 Menetelmät
- `q:37bb4c3b38` (verified locally): Policy evidence for pathway stage 'Referral' — roadmap_2026_2031_fi.pdf, p.52; p.106
- `q:39e6ba43a9` (verified locally): Report evidence for pathway stage 'MDT' — keuhkosyoparaportti_2019_2023.html, §3.3 Menetelmät
- `q:432c0e51d6` (verified locally): The upcoming national diagnostics recommendation will include “suositellut aikarajat erikoissairaanhoitoon eri diagnostiikan polun vaiheille” (recommended time limits in specialist care), due before the 2030 mid-term evaluation — filha_lung_programme_2026_fi.pdf, p.16
- `q:47c7e11303` (verified locally): Finland has no quality registry for lung cancer or for any other cancer. — filha_lung_programme_2026_fi.pdf, p.21
- `q:4a856bd695` (verified locally): the registry's data, including stage, allows reliable assessment and comparison of quality and effectiveness, with 90% data coverage — roadmap_2026_2031_fi.pdf, p.60
- `q:4e702a20fe` (verified locally): Finland has no unified national system to steer the drafting of cancer-specific treatment recommendations, or the implementation and monitoring of care pathways based on them (quality and effectiveness targets/indicators, including access to care, and cancer-specific and generic PROMs). Existing recommendations and pathways, and the targets and indicators to be monitored, are not coordinated nationally. This maintains regional inequality in the availability and effectiveness of cancer care. — strategy_2026_2035_fi.pdf, p.33
- `q:614febebf2` (verified locally): When (p.24): > “Väliarvio toteutetaan vuonna 2030, ohjelman puolivälissä ja loppuarviointi vuonna 2036. Eri > osa-alueiden suositukset toteutetaan ennen väliarviointia.” — filha_lung_programme_2026_fi.pdf, p.24
- `q:7885b0974f` (verified locally): Report evidence for pathway stage 'Diagnosis' — keuhkosyoparaportti_2019_2023.html, §4.1.3 Levinneisyystiedon kattavuus
- `q:82d365cd2c` (verified locally): “Tällä hetkellä keuhkosyöpään liittyvien tietojen raportointi, kerääminen ja tallentaminen on puutteellista”; nationally uniform recording instructions (“yhtenäiset kirjaamisohjeet”) must be ensured — filha_lung_programme_2026_fi.pdf, p.21
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
