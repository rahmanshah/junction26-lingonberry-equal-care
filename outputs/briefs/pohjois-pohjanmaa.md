# Pohjois-Pohjanmaa: lung cancer pathway brief

Status: **validated** · gemini-4-argon (thinking HIGH) · 2026-11-14T12:17:52+00:00 · attempts: 1

## Where do we lag?

**Pohjois-Pohjanmaa lags the national share in crude curative treatment at 23.6% versus 27.0% nationally and in crude recorded multidisciplinary team meetings at 1.1% versus 6.0%.** `cty:curative:Pohjois_Pohjanmaan_hyvinvointialue, nat:curative, cty:mdt_recorded:Pohjois_Pohjanmaan_hyvinvointialue, nat:mdt_recorded`

- Among 1050 new lung cancer patients in 2019–2023, the county's crude curative treatment share was 23.6% (95% CI 21.1–26.3; n=248/1050), where the 95% confidence interval excludes the national value of 27.0% (4009/14873), and these crude shares are not adjusted for age or stage. `cty:curative:Pohjois_Pohjanmaan_hyvinvointialue, nat:curative, bs:coverage:Diagnosis`
- In overlapping treatment categories where patients can receive multiple types, the crude life-prolonging share was 37.4% (95% CI 34.5–40.4; n=393/1050), with its 95% confidence interval excluding the national 30.4% (4522/14873), while the crude symptomatic share of 38.8% (95% CI 35.9–41.7; n=407/1050) has a 95% confidence interval that includes the national 39.5% (5871/14873). `cty:life_prolonging:Pohjois_Pohjanmaan_hyvinvointialue, nat:life_prolonging, cty:symptomatic:Pohjois_Pohjanmaan_hyvinvointialue, nat:symptomatic`
- The crude share of patients with a multidisciplinary team meeting recorded in HILMO was 1.1% (95% CI 0.7–2.0; n=12/1050), whose 95% confidence interval excludes the national 6.0% (893/14873), and this measures recording practice from direct patient contacts rather than actual multidisciplinary review. `cty:mdt_recorded:Pohjois_Pohjanmaan_hyvinvointialue, nat:mdt_recorded, bs:coverage:MDT, q:39e6ba43a9`

## How sure are we?

**The low crude curative share is unlikely to be only a recording artefact, but crude figures lack stage adjustment and public data omit key pathway timestamps.** `cty:curative:Pohjois_Pohjanmaan_hyvinvointialue, cty:no_treatment_record:Pohjois_Pohjanmaan_hyvinvointialue, bs:coverage:Diagnosis, bs:coverage:Treatment_start`

- The crude share with no treatment record within 12 months—mixing untreated patients and unrecorded treatment—is 25.0% (95% CI 22.5–27.8; n=263/1050), with its 95% confidence interval including the national 27.5% (4089/14873); as an inference, not a finding, this is consistent with relatively complete recording (not direct evidence), making the 23.6% crude curative share less likely to be only a recording artefact. `cty:no_treatment_record:Pohjois_Pohjanmaan_hyvinvointialue, nat:no_treatment_record, bs:coverage:Treatment_start, cty:curative:Pohjois_Pohjanmaan_hyvinvointialue`
- Although a figure digitised at ±0.5 percentage points shows national age-adjusted curative shares of 26.7% for men and 26.9% for women, county shares here are crude, stage is missing for nearly half of new patients nationally, and a journal article's roughly 90% HILMO–Cancer Registry match covers diagnosis concordance only, not treatment or multidisciplinary recording. `k16:curative:men:national, k16:curative:women:national, bs:coverage:Diagnosis, q:7885b0974f, lit:hilmo_90`
- While preliminary, unpublished national averages show 155 days from symptoms to treatment in Finland (56 days patient delay, 41 days primary care, 58 days specialist care), outpatient primary care visits and occupational health are not included in the report's data, which also lack timestamps for symptoms, referrals, imaging, first specialist visits, and treatment start. `mot:total_fi, mot:patient, mot:primary, mot:specialist, bs:coverage:Symptoms, bs:coverage:Primary_care_occupational_health, q:323de0d90d, bs:coverage:Imaging, bs:coverage:Referral, bs:coverage:First_specialist_visit, bs:coverage:Treatment_start`

## What should we do first?

**To address the lower crude curative share of 23.6%, the team recommends tracking THL 21/2016 access times, standardising referrals and diagnostic contacts, and auditing stage and multidisciplinary coding completeness.** `cty:curative:Pohjois_Pohjanmaan_hyvinvointialue, rec:1, rec:2, rec:3`

- Because the Health Care Act §52 sets no legal maximum time for a cancer suspicion and national target access times are only planned for 2026–2028 (with Filha's diagnostics guideline due before the 2030 interim evaluation), the team recommends reporting referral-to-treatment access times using THL Ohjaus 21/2016 definitions for 16 cancers and flagging stalled handovers. `rec:1, law:no_max, thl:21_2016, q:24169121a4, q:ccda20dce9, q:def306014c, q:b326e35410, q:432c0e51d6, q:614febebf2`
- Since patients are referred under local instructions, a mentor insight notes weak referrals receive lower specialist urgency ratings, and national referral criteria and care-coordinator guidance are only planned for 2026–2028 (for county adoption in 2029–2031), the team recommends a standard referral template, referring persistent symptoms after a normal X-ray to a pulmonologist, and naming a diagnostic-phase contact. `rec:2, q:556431a0c2, mentor:kaisa_referral, q:37bb4c3b38, q:0780bf74b0, q:c61439b30f, q:29b792498e, q:fc81032a80, q:abcbb06ae3, q:050ee09ebe`
- Given the county's 1.1% crude recorded multidisciplinary meeting share versus 6.0% nationally, missing stage data for nearly half of new patients nationally, and incomplete national reporting while a quality registry with 90% coverage is planned, the team recommends publishing county recording completeness for stage, drug treatment, and multidisciplinary coding and reading gaps as data-quality signals first. `rec:3, cty:mdt_recorded:Pohjois_Pohjanmaan_hyvinvointialue, nat:mdt_recorded, bs:coverage:MDT, q:7885b0974f, q:950a2f797b, q:82d365cd2c, q:990a0d39a0, q:f07a34a300, q:4a856bd695`

## Review flags (for human review only)

_Flags are for human review only; they never change the brief's status or approve it._

- none

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
- `k16:curative:men:national` (verified locally): Finland (national reference line): age-adjusted curative treatment share, men, 26.7% — keuhkosyoparaportti_2019_2023.html, Kuva 16
- `k16:curative:women:national` (verified locally): Finland (national reference line): age-adjusted curative treatment share, women, 26.9% — keuhkosyoparaportti_2019_2023.html, Kuva 16
- `law:no_max` (verified by Hellu): There is no legal maximum time for a cancer suspicion — pathway_brief.md, 5. What the law guarantees (Health Care Act, §52)
- `lit:hilmo_90` (verified by Hellu): HILMO diagnoses match the Cancer Registry for about 90% of most cancer types — pathway_brief.md, 6. Regional pathways compared
- `mentor:kaisa_referral` (mentor insight): A weak referral gets a lower urgency rating in specialist care — pathway_brief.md, 7. Where patients get stuck
- `mot:patient` (preliminary): Patient delay (symptoms to first contact): 56 days — pathway_brief.md, 7. Where patients get stuck
- `mot:primary` (preliminary): Primary care interval: 41 days — pathway_brief.md, 7. Where patients get stuck
- `mot:specialist` (preliminary): Specialist care interval: 58 days, the longest stage — pathway_brief.md, 7. Where patients get stuck
- `mot:total_fi` (preliminary): Symptoms to first treatment, Finland: 155 days on average — pathway_brief.md, 1. Key points
- `nat:curative` (verified locally): Finland: curative treatment 27.0% (4009/14873), 2019–2023 — keuhkosyoparaportti_2019_2023.html, Taulukko 6
- `nat:life_prolonging` (verified locally): Finland: life-prolonging treatment 30.4% (4522/14873), 2019–2023 — keuhkosyoparaportti_2019_2023.html, Taulukko 6
- `nat:mdt_recorded` (verified locally): Finland: MDT meeting recorded 6.0% (893/14873), 2019–2023 — keuhkosyoparaportti_2019_2023.html, Taulukko 5
- `nat:no_treatment_record` (verified locally): Finland: no treatment record within 12 months 27.5% (4089/14873), 2019–2023 — keuhkosyoparaportti_2019_2023.html, Taulukko 5
- `nat:symptomatic` (verified locally): Finland: symptomatic treatment 39.5% (5871/14873), 2019–2023 — keuhkosyoparaportti_2019_2023.html, Taulukko 6
- `q:050ee09ebe` (verified locally): Guidance on a named worker coordinating cancer care by 2026–2028, adopted by counties by 2029–2031; the care phase is left open (“missä hoidon vaiheessa … olisi tärkeintä kohdentaa”) — roadmap_2026_2031_fi.pdf, p.32
- `q:0780bf74b0` (verified locally): Policy evidence for pathway stage 'Symptoms' — roadmap_2026_2031_fi.pdf, p.52; p.53
- `q:24169121a4` (verified locally): Strategy p.5 (= PDF p.5), “Strategiset tavoitteet”, indicator under “Varmistetaan yhdenvertainen ja vaikuttava syövänhoito”: > “Potilaat pääsevät hoitoon tavoiteaikojen puitteissa” > “ THL (Ohjaus 21/2016). Hoitoonpääsyn seuranta syövän hoidossa.” — strategy_2026_2035_fi.pdf, p.5
- `q:29b792498e` (verified locally): Policy evidence for pathway stage 'Referral' — filha_lung_programme_2026_fi.pdf, p.16
- `q:323de0d90d` (verified locally): Report evidence for pathway stage 'Primary care / occupational health' — keuhkosyoparaportti_2019_2023.html, §3.3 Menetelmät
- `q:37bb4c3b38` (verified locally): Policy evidence for pathway stage 'Referral' — roadmap_2026_2031_fi.pdf, p.52; p.106
- `q:39e6ba43a9` (verified locally): Report evidence for pathway stage 'MDT' — keuhkosyoparaportti_2019_2023.html, §3.3 Menetelmät
- `q:432c0e51d6` (verified locally): The upcoming national diagnostics recommendation will include “suositellut aikarajat erikoissairaanhoitoon eri diagnostiikan polun vaiheille” (recommended time limits in specialist care), due before the 2030 mid-term evaluation — filha_lung_programme_2026_fi.pdf, p.16
- `q:4a856bd695` (verified locally): the registry's data, including stage, allows reliable assessment and comparison of quality and effectiveness, with 90% data coverage — roadmap_2026_2031_fi.pdf, p.60
- `q:556431a0c2` (verified locally): the patient is referred to specialist care according to local instructions — filha_lung_programme_2026_fi.pdf, p.15
- `q:614febebf2` (verified locally): When (p.24): > “Väliarvio toteutetaan vuonna 2030, ohjelman puolivälissä ja loppuarviointi vuonna 2036. Eri > osa-alueiden suositukset toteutetaan ennen väliarviointia.” — filha_lung_programme_2026_fi.pdf, p.24
- `q:7885b0974f` (verified locally): Report evidence for pathway stage 'Diagnosis' — keuhkosyoparaportti_2019_2023.html, §4.1.3 Levinneisyystiedon kattavuus
- `q:82d365cd2c` (verified locally): “Tällä hetkellä keuhkosyöpään liittyvien tietojen raportointi, kerääminen ja tallentaminen on puutteellista”; nationally uniform recording instructions (“yhtenäiset kirjaamisohjeet”) must be ensured — filha_lung_programme_2026_fi.pdf, p.21
- `q:950a2f797b` (verified locally): Reporting, collection and storage of lung cancer data is currently incomplete. — filha_lung_programme_2026_fi.pdf, p.21
- `q:990a0d39a0` (verified locally): Policy evidence for pathway stage 'MDT' — roadmap_2026_2031_fi.pdf, p.56
- `q:abcbb06ae3` (verified locally): 2026–2028: guidance on a named doctor, nurse or specialist worker coordinating cancer care. 2029–2031: wellbeing services counties have adopted it. — roadmap_2026_2031_fi.pdf, p.32
- `q:b326e35410` (verified locally): National pathways with “syöpäkohtaiset hoitoonpääsyajat” for five (unnamed) cancers in 2026–2028, Nordic model — roadmap_2026_2031_fi.pdf, p.57
- `q:c61439b30f` (verified locally): 2026–2028: standardised referral criteria and symptom-based models included in the national pathways of at least the five most common cancers. — roadmap_2026_2031_fi.pdf, p.53
- `q:ccda20dce9` (verified locally): Finland has no national system steering cancer pathways or their monitoring, “mukaan lukien hoitoonpääsy” — strategy_2026_2035_fi.pdf, p.33
- `q:def306014c` (verified locally): p.57, timetable: > “2026–2028: Kansalliset hoitoketjukuvaukset tehty viidestä syövästä ja syöpäkohtaiset > hoitoonpääsyajat on määritetty.” — roadmap_2026_2031_fi.pdf, p.57
- `q:f07a34a300` (verified locally): A national cancer care quality registry will be set up alongside THL's Cancer Registry. — roadmap_2026_2031_fi.pdf, p.59
- `q:fc81032a80` (verified locally): Measure 1.2.3: Create an operating model and guidance for a named worker responsible for coordinating cancer care. — roadmap_2026_2031_fi.pdf, p.32
- `rec:1` (recommendation (ours)): Team recommendation 1: Counties report access times using the THL 21/2016 definitions, with handover alerts. Each wellbeing services county reports lung cancer access times (referral → first specialist visit → diagnosis → treatment start) using the definitions in THL's Hoitoonpääsyn seuranta syövän hoidossa (Ohjaus 21/2016). Until national target times exist, flag stalled handovers. — recommendations.md, §1. Counties report access times using the THL 21/2016 definitions, with handover alerts
- `rec:2` (recommendation (ours)): Team recommendation 2: A KYS-style referral template, a persistent-symptoms rule and a named contact. Adopt a standard referral content list and template, modelled on KYS. • Add a rule for primary care: if symptoms persist after a normal X-ray, refer for a pulmonologist assessment. • Name a contact person for the diagnostic phase, from referral to diagnosis. — recommendations.md, §2. A KYS-style referral template, a persistent-symptoms rule and a named contact
- `rec:3` (recommendation (ours)): Team recommendation 3: Report recording completeness per county: stage, drug treatment, MDT coding. Publish, per county, how completely stage, drug treatment and MDT meetings are recorded. Read county ‘gaps’ in these fields as data-quality signals first. — recommendations.md, §3. Report recording completeness per county: stage, drug treatment, MDT coding
- `thl:21_2016` (verified by Hellu): THL Ohjaus 21/2016 defines how cancer access times are recorded, for 16 cancers — pathway_brief.md, 6. Regional pathways compared
