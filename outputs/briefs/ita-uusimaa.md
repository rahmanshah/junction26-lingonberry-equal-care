# Itä-Uusimaa: lung cancer pathway brief

Status: **validated** · gemini-4-argon (thinking HIGH) · 2026-11-14T12:49:26+00:00 · attempts: 2

## Where do we lag?

**In Itä-Uusimaa, the crude recorded MDT share of 0.0% lags the national 6.0%, while crude treatment shares (whose categories overlap) are not distinguishable from national values.** `cty:mdt_recorded:Itä_Uudenmaan_hyvinvointialue, nat:mdt_recorded, cty:curative:Itä_Uudenmaan_hyvinvointialue, cty:life_prolonging:Itä_Uudenmaan_hyvinvointialue, cty:symptomatic:Itä_Uudenmaan_hyvinvointialue`

- The county's crude recorded MDT meeting share is 0.0% (95% CI 0.0–1.4; n=0/272), whose 95% confidence interval excludes the national 6.0% (893/14873), though HILMO MDT codes capture only direct patient contacts and measure recording practice rather than care. `cty:mdt_recorded:Itä_Uudenmaan_hyvinvointialue, nat:mdt_recorded, bs:coverage:MDT, q:39e6ba43a9`
- Across overlapping treatment categories where a patient can have several treatments, crude county shares have 95% confidence intervals that include national values: curative 28.3% (95% CI 23.3–33.9; n=77/272) vs 27.0% (4009/14873), life-prolonging 30.1% (95% CI 25.0–35.9; n=82/272) vs 30.4% (4522/14873), and symptomatic 36.8% (95% CI 31.3–42.6; n=100/272) vs 39.5% (5871/14873). `cty:curative:Itä_Uudenmaan_hyvinvointialue, nat:curative, cty:life_prolonging:Itä_Uudenmaan_hyvinvointialue, nat:life_prolonging, cty:symptomatic:Itä_Uudenmaan_hyvinvointialue, nat:symptomatic`
- The crude county share with no treatment record within 12 months is 31.6% (95% CI 26.4–37.4; n=86/272), whose 95% confidence interval includes the national 27.5% (4089/14873); this category mixes untreated patients and treatment that was not recorded. `cty:no_treatment_record:Itä_Uudenmaan_hyvinvointialue, nat:no_treatment_record, bs:coverage:Treatment_start`
- While county wait times are unmeasured in public data, preliminary national averages from an unpublished study show 155 days from symptoms to first treatment in Finland (vs 107 in Sweden and 67 in Denmark), comprising 56 days of patient delay, 41 days in primary care, and 58 days in specialist care. `bs:coverage:Symptoms, bs:coverage:Treatment_start, mot:total_fi, mot:total_se, mot:total_dk, mot:patient, mot:primary, mot:specialist`

## How sure are we?

**Hospital discharge diagnoses match the Cancer Registry well, but crude county treatment shares lack age and stage adjustment, and public data omit key pathway timestamps.** `lit:hilmo_90, cty:curative:Itä_Uudenmaan_hyvinvointialue, bs:coverage:Diagnosis, bs:coverage:Treatment_start`

- County shares are crude and have separate limitations: they are not age-adjusted (age-adjusted values exist only from Kuva 16 for curative treatment by sex, digitised from a figure at about ±0.5 percentage points, with national reference lines at 26.7% for men and 26.9% for women), and they cannot be stage-adjusted because stage at diagnosis is missing for about 48% of patients. `cty:curative:Itä_Uudenmaan_hyvinvointialue, k16:curative:men:national, k16:curative:women:national, bs:coverage:Diagnosis, q:7885b0974f`
- A journal article found hospital discharge register (HILMO) diagnoses matched the Cancer Registry for about 90% of most cancer types, but this concerns diagnosis concordance only and says nothing about referral, MDT, or treatment recording, while Finland currently has no cancer quality registry. `lit:hilmo_90, filha:registry, q:47c7e11303, q:950a2f797b`
- Public report data do not measure symptom onset or referrals, do not include primary care visits in the report's data, do not mention occupational health at all, and note imaging only where diagnosis rests on clinical examination alone in approximately 20% of patients. `bs:coverage:Symptoms, bs:coverage:Referral, bs:coverage:Primary_care_occupational_health, q:323de0d90d, bs:coverage:Imaging, q:5eb155decc`
- For specialist care, public data record whether a lung cancer visit (93.6% nationally) or treatment type appears in HILMO within 12 months, not when the first specialist visit or treatment started. `bs:coverage:First_specialist_visit, bs:coverage:Treatment_start`

## What should we do first?

**The team recommends auditing stage, treatment, and MDT recording completeness, reporting access times using THL 21/2016 definitions, and standardising referrals and diagnostic-phase care coordination.** `rec:3, rec:1, rec:2`

- Given Itä-Uusimaa's 0.0% crude recorded MDT share vs 6.0% nationally and about 48% missing stage nationally, the team recommends publishing county recording completeness for stage, drug treatment, and MDT coding as data-quality signals; meanwhile, the STM roadmap (measure 3.2.1) plans updating the quality-registry decree by 2026–2028 and annual reports targeting 90% coverage by 2029–2031. `rec:3, cty:mdt_recorded:Itä_Uudenmaan_hyvinvointialue, nat:mdt_recorded, bs:coverage:Diagnosis, q:7885b0974f, q:bfa4196bfd, q:950a2f797b, q:f07a34a300, q:4a856bd695, q:f540c706f8`
- Because the Health Care Act sets no maximum time for a cancer suspicion, the team recommends reporting access times using THL 21/2016 definitions for 16 cancers with handover alerts; meanwhile, the STM roadmap (measure 3.1.2) plans cancer-specific access times by 2026–2028, and the Filha programme's diagnostics recommendation with time limits is to be carried out before the 2030 mid-term evaluation. `rec:1, law:no_max, thl:21_2016, q:ccda20dce9, q:20d6ca414e, q:b326e35410, q:def306014c, q:432c0e51d6, q:614febebf2`
- As referrals follow local instructions and a mentor insight notes weak referrals get lower urgency, the team recommends a KYS-style referral template, a persistent-symptoms rule, and a named diagnostic contact; the STM roadmap plans referral criteria (measure 2.5.2) and coordinator guidance (measure 1.2.3) by 2026–2028, while the Filha programme's referral criteria are to be carried out before the 2030 mid-term evaluation. `rec:2, q:556431a0c2, mentor:kaisa_referral, q:c61439b30f, q:abcbb06ae3, q:050ee09ebe, q:29b792498e, q:614febebf2`

## Review flags (for human review only)

_Flags are for human review only; they never change the brief's status or approve it._

- [low] `what_to_do_first.headline`: Claim rec:3 recommends publishing/reporting per-county recording completeness for stage, drug treatment, and MDT coding—not 'auditing', and specifically 'drug treatment' rather than 'treatment' in general.
- [low] `what_to_do_first.details[0]`: Under STM roadmap measure 3.2.1, the 2029–2031 milestone is annual reports for at least five cancers, whereas the 90% data coverage indicator applies to the quality registry's data base rather than the annual reports.
- [medium] `what_to_do_first.details[1]`: STM roadmap measure 3.1.2 plans cancer-specific access times only for five (unnamed) cancers by 2026–2028 (with all significant cancers following by 2029–2031); omitting this scope restriction overstates what is planned by 2026–2028.
- [low] `what_to_do_first.details[2]`: STM roadmap measure 2.5.2 plans standardised referral criteria for at least the five most common cancers by 2026–2028 (and all significant cancers by 2029–2031), rather than for all cancers by 2026–2028.

## Claims cited

- `bs:coverage:Diagnosis` (verified locally): Pathway stage 'Diagnosis' is measured in public data: yes (by county: yes (Kuva 7, 10, 13: PNG only)) — keuhkosyoparaportti_2019_2023.html, §4.1, Taulukko 2–4, Kuva 5–13
- `bs:coverage:First_specialist_visit` (verified locally): Pathway stage 'First specialist visit' is measured in public data: partly (by county: no) — keuhkosyoparaportti_2019_2023.html, §3.1, §4.2, Taulukko 5
- `bs:coverage:Imaging` (verified locally): Pathway stage 'Imaging' is measured in public data: partly (by county: partly (Kuva 7, PNG only)) — keuhkosyoparaportti_2019_2023.html, §4.1.1, Taulukko 2, Kuva 5–7
- `bs:coverage:MDT` (verified locally): Pathway stage 'MDT' is measured in public data: partly (by county: yes (Taulukko 11)) — keuhkosyoparaportti_2019_2023.html, §3.3, §4.2, Taulukko 5, 10, 11, 13
- `bs:coverage:Primary_care_occupational_health` (verified locally): Pathway stage 'Primary care / occupational health' is measured in public data: no (by county: no) — keuhkosyoparaportti_2019_2023.html, §3.3
- `bs:coverage:Referral` (verified locally): Pathway stage 'Referral' is measured in public data: no (by county: no) — keuhkosyoparaportti_2019_2023.html, whole report (no relevant data found)
- `bs:coverage:Symptoms` (verified locally): Pathway stage 'Symptoms' is measured in public data: no (by county: no) — keuhkosyoparaportti_2019_2023.html, whole report (no relevant data found)
- `bs:coverage:Treatment_start` (verified locally): Pathway stage 'Treatment start' is measured in public data: partly (by county: yes (type only, Taulukko 11)) — keuhkosyoparaportti_2019_2023.html, §4.2, §4.2.2, Taulukko 6–9, 11, 12, Kuva 14, 17
- `cty:curative:Itä_Uudenmaan_hyvinvointialue` (verified locally): Itä-Uudenmaan hyvinvointialue: curative treatment 28.3% (95% CI 23.3–33.9; n=77/272), not distinguishable vs national 27.0% — keuhkosyoparaportti_2019_2023.html, Taulukko 11
- `cty:life_prolonging:Itä_Uudenmaan_hyvinvointialue` (verified locally): Itä-Uudenmaan hyvinvointialue: life-prolonging treatment 30.1% (95% CI 25.0–35.9; n=82/272), not distinguishable vs national 30.4% — keuhkosyoparaportti_2019_2023.html, Taulukko 11
- `cty:mdt_recorded:Itä_Uudenmaan_hyvinvointialue` (verified locally): Itä-Uudenmaan hyvinvointialue: MDT meeting recorded 0.0% (95% CI 0.0–1.4; n=0/272), below vs national 6.0% — keuhkosyoparaportti_2019_2023.html, Taulukko 11
- `cty:no_treatment_record:Itä_Uudenmaan_hyvinvointialue` (verified locally): Itä-Uudenmaan hyvinvointialue: no treatment record within 12 months 31.6% (95% CI 26.4–37.4; n=86/272), not distinguishable vs national 27.5% — keuhkosyoparaportti_2019_2023.html, Taulukko 11
- `cty:symptomatic:Itä_Uudenmaan_hyvinvointialue` (verified locally): Itä-Uudenmaan hyvinvointialue: symptomatic treatment 36.8% (95% CI 31.3–42.6; n=100/272), not distinguishable vs national 39.5% — keuhkosyoparaportti_2019_2023.html, Taulukko 11
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
- `q:29b792498e` (verified locally): Policy evidence for pathway stage 'Referral' — filha_lung_programme_2026_fi.pdf, p.16
- `q:323de0d90d` (verified locally): Report evidence for pathway stage 'Primary care / occupational health' — keuhkosyoparaportti_2019_2023.html, §3.3 Menetelmät
- `q:39e6ba43a9` (verified locally): Report evidence for pathway stage 'MDT' — keuhkosyoparaportti_2019_2023.html, §3.3 Menetelmät
- `q:432c0e51d6` (verified locally): The upcoming national diagnostics recommendation will include “suositellut aikarajat erikoissairaanhoitoon eri diagnostiikan polun vaiheille” (recommended time limits in specialist care), to be carried out (“toteutetaan”; may mean produced or implemented) before the 2030 mid-term evaluation — filha_lung_programme_2026_fi.pdf, p.16
- `q:47c7e11303` (verified locally): Finland has no quality registry for lung cancer or for any other cancer. — filha_lung_programme_2026_fi.pdf, p.21
- `q:4a856bd695` (verified locally): the registry's data, including stage, allows reliable assessment and comparison of quality and effectiveness, with 90% data coverage — roadmap_2026_2031_fi.pdf, p.60
- `q:556431a0c2` (verified locally): the patient is referred to specialist care according to local instructions — filha_lung_programme_2026_fi.pdf, p.15
- `q:5eb155decc` (verified locally): Report evidence for pathway stage 'Imaging' — keuhkosyoparaportti_2019_2023.html, §4.1.1 Toteamistapa
- `q:614febebf2` (verified locally): When (p.24): > “Väliarvio toteutetaan vuonna 2030, ohjelman puolivälissä ja loppuarviointi vuonna 2036. Eri > osa-alueiden suositukset toteutetaan ennen väliarviointia.” — filha_lung_programme_2026_fi.pdf, p.24
- `q:7885b0974f` (verified locally): Report evidence for pathway stage 'Diagnosis' — keuhkosyoparaportti_2019_2023.html, §4.1.3 Levinneisyystiedon kattavuus
- `q:950a2f797b` (verified locally): Reporting, collection and storage of lung cancer data is currently incomplete. — filha_lung_programme_2026_fi.pdf, p.21
- `q:abcbb06ae3` (verified locally): 2026–2028: guidance on a named doctor, nurse or specialist worker coordinating cancer care. 2029–2031: wellbeing services counties have adopted it. — roadmap_2026_2031_fi.pdf, p.32
- `q:b326e35410` (verified locally): National pathways with “syöpäkohtaiset hoitoonpääsyajat” for five (unnamed) cancers in 2026–2028, Nordic model — roadmap_2026_2031_fi.pdf, p.57
- `q:bfa4196bfd` (verified locally): MDT coding: 21.6–37.4% in Sisä-Suomi counties, 0 records in 4 counties. “…ei kuvaa kattavasti moniammatillisen käsittelyn laajuutta” — keuhkosyoparaportti_2019_2023.html, §3.3 Menetelmät
- `q:c61439b30f` (verified locally): 2026–2028: standardised referral criteria and symptom-based models included in the national pathways of at least the five most common cancers. — roadmap_2026_2031_fi.pdf, p.53
- `q:ccda20dce9` (verified locally): Finland has no national system steering cancer pathways or their monitoring, “mukaan lukien hoitoonpääsy” — strategy_2026_2035_fi.pdf, p.33
- `q:def306014c` (verified locally): p.57, timetable: > “2026–2028: Kansalliset hoitoketjukuvaukset tehty viidestä syövästä ja syöpäkohtaiset > hoitoonpääsyajat on määritetty.” — roadmap_2026_2031_fi.pdf, p.57
- `q:f07a34a300` (verified locally): A national cancer care quality registry will be set up alongside THL's Cancer Registry. — roadmap_2026_2031_fi.pdf, p.59
- `q:f540c706f8` (verified locally): A national quality registry is planned; indicator: data incl. stage (“ml. levinneisyystieto”) at 90% coverage — roadmap_2026_2031_fi.pdf, p.60
- `rec:1` (recommendation (ours)): Team recommendation 1: Counties report access times using the THL 21/2016 definitions, with handover alerts. Each wellbeing services county reports lung cancer access times (referral → first specialist visit → diagnosis → treatment start) using the definitions in THL's Hoitoonpääsyn seuranta syövän hoidossa (Ohjaus 21/2016). Until national target times exist, flag stalled handovers. — recommendations.md, §1. Counties report access times using the THL 21/2016 definitions, with handover alerts
- `rec:2` (recommendation (ours)): Team recommendation 2: A KYS-style referral template, a persistent-symptoms rule and a named contact. Adopt a standard referral content list and template, modelled on KYS. • Add a rule for primary care: if symptoms persist after a normal X-ray, refer for a pulmonologist assessment. • Name a contact person for the diagnostic phase, from referral to diagnosis. — recommendations.md, §2. A KYS-style referral template, a persistent-symptoms rule and a named contact
- `rec:3` (recommendation (ours)): Team recommendation 3: Report recording completeness per county: stage, drug treatment, MDT coding. Publish, per county, how completely stage, drug treatment and MDT meetings are recorded. Read county ‘gaps’ in these fields as data-quality signals first. — recommendations.md, §3. Report recording completeness per county: stage, drug treatment, MDT coding
- `thl:21_2016` (verified by Hellu): THL Ohjaus 21/2016 defines how cancer access times are recorded, for 16 cancers — pathway_brief.md, 6. Regional pathways compared
