# Keski-Pohjanmaa: lung cancer pathway brief

Status: **validated** · gemini-4-argon (thinking HIGH) · 2026-11-14T13:51:46+00:00 · attempts: 2

## Where do we lag?

**In overlapping categories, Keski-Pohjanmaa's crude MDT-recorded share, 1.4% (95% CI 0.4–4.8), is below 6.0% nationally; crude curative treatment, 22.3% (95% CI 16.3–29.7), is not distinguishable from 27.0%.** `cty:mdt_recorded:Keski_Pohjanmaan_hyvinvointialue, nat:mdt_recorded, cty:curative:Keski_Pohjanmaan_hyvinvointialue, nat:curative`

- In 2019–2023, a multidisciplinary team (MDT) meeting was recorded for a crude share of 1.4% (95% CI 0.4–4.8; n=2/148) of new patients in Keski-Pohjanmaa, where the 95% confidence interval excludes the national 6.0% (893/14873); however, HILMO captures specialist procedures only from direct patient contacts, so MDT records measure recording practice rather than care. `cty:mdt_recorded:Keski_Pohjanmaan_hyvinvointialue, nat:mdt_recorded, bs:coverage:MDT, q:39e6ba43a9`
- Across overlapping treatment categories where a patient may receive several treatments, Keski-Pohjanmaa's crude shares are 22.3% (95% CI 16.3–29.7; n=33/148) vs 27.0% (4009/14873) nationally for curative treatment, 32.4% (95% CI 25.4–40.3; n=48/148) vs 30.4% (4522/14873) for life-prolonging treatment, and 46.6% (95% CI 38.8–54.6; n=69/148) vs 39.5% (5871/14873) for symptomatic treatment, with every 95% confidence interval including its national value. `cty:curative:Keski_Pohjanmaan_hyvinvointialue, nat:curative, cty:life_prolonging:Keski_Pohjanmaan_hyvinvointialue, nat:life_prolonging, cty:symptomatic:Keski_Pohjanmaan_hyvinvointialue, nat:symptomatic`
- Public registry data do not show when treatment started or measure referral and primary-care waits, while preliminary, unpublished figures report an average of 155 days from symptoms to treatment in Finland (compared with 107 days in Sweden and 67 days in Denmark), comprising 56 days of patient delay, 41 days in primary care, and 58 days in specialist care. `bs:coverage:Treatment_start, bs:coverage:Referral, bs:coverage:Primary_care_occupational_health, mot:total_fi, mot:total_se, mot:total_dk, mot:patient, mot:primary, mot:specialist`

## How sure are we?

**Taulukko 11 reports only crude county shares that are neither age-adjusted nor stage-adjusted, as stage is missing for about 48% of patients, and public data omit key pathway timestamps.** `fig:age_adjusted_only_kuva16, bs:coverage:Diagnosis, q:7885b0974f, bs:coverage:First_specialist_visit, bs:coverage:Treatment_start`

- Taulukko 11 gives crude county shares with separate limitations: they are not age-adjusted (county age-adjusted shares appear only in Kuva 16, where digitised national curative reference lines read from the figure are 26.7% for men and 26.9% for women, ±0.5 percentage points) and, separately, they cannot be stage-adjusted because stage at diagnosis is missing for about 48% of patients. `fig:age_adjusted_only_kuva16, k16:curative:men:national, k16:curative:women:national, bs:coverage:Diagnosis, q:7885b0974f`
- In Keski-Pohjanmaa, the crude share with no treatment record within 12 months is 25.0% (95% CI 18.7–32.5; n=37/148), whose 95% confidence interval includes the national 27.5% (4089/14873); this category mixes untreated patients and treatment that was not recorded, while a journal article found about 90% HILMO–Cancer Registry concordance for diagnoses only. `cty:no_treatment_record:Keski_Pohjanmaan_hyvinvointialue, nat:no_treatment_record, bs:coverage:Treatment_start, lit:hilmo_90`
- Public data in the report do not measure symptom onset or referrals, primary-care visits are not included in the report's data, occupational health is not mentioned, imaging appears only indirectly as the basis of diagnosis in approximately 20% of patients, and HILMO shows whether a specialist visit occurred within 12 months (93.6%) but not when. `bs:coverage:Symptoms, bs:coverage:Referral, bs:coverage:Primary_care_occupational_health, q:323de0d90d, bs:coverage:Imaging, q:5eb155decc, bs:coverage:First_specialist_visit`

## What should we do first?

**To address data blind spots and delays, the team recommends publishing county stage, drug, and MDT coding coverage, tracking THL 21/2016 access times, and standardising referrals and diagnostic coordination.** `rec:1, rec:2, rec:3, thl:21_2016, q:950a2f797b, q:556431a0c2`

- Because Keski-Pohjanmaa's crude MDT-recorded share is 1.4% (95% CI 0.4–4.8; n=2/148) versus 6.0% (893/14873) nationally, stage is missing for about 48% of patients, and Finland lacks a cancer quality registry while lung cancer data reporting is incomplete and requires uniform recording instructions, the team recommends publishing per-county stage, drug-treatment, and MDT coding completeness. `rec:3, cty:mdt_recorded:Keski_Pohjanmaan_hyvinvointialue, nat:mdt_recorded, bs:coverage:Diagnosis, q:7885b0974f, q:47c7e11303, q:950a2f797b, q:82d365cd2c`
- Because the Health Care Act sets no maximum time for a cancer suspicion and Finland lacks uniform diagnostic timetable guidance, the team recommends reporting referral-to-treatment access times using THL Ohjaus 21/2016 definitions (16 cancers) and flagging stalled handovers until the Filha programme's diagnostics recommendation with recommended time limits is carried out before the 2030 mid-term evaluation. `rec:1, law:no_max, thl:21_2016, q:20d6ca414e, q:ccda20dce9, q:432c0e51d6, q:614febebf2, q:14dff3e002`
- Because referrals follow local instructions and mentor insight notes that weak referrals receive lower urgency ratings, the team recommends adopting a referral template and referring persistent symptoms after a normal X-ray (as in the KYS pathway document), plus naming a diagnostic contact person while the STM roadmap plans referral criteria (measure 2.5.2) and coordinator guidance (measure 1.2.3) by 2026–2028. `rec:2, q:556431a0c2, mentor:kaisa_referral, reg:kys_template, reg:kys_persistent, reg:named_contact, q:9a1cd194f5, q:c61439b30f, q:fc81032a80, q:050ee09ebe, q:abcbb06ae3`

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
- `cty:curative:Keski_Pohjanmaan_hyvinvointialue` (verified locally): Keski-Pohjanmaan hyvinvointialue: curative treatment 22.3% (95% CI 16.3–29.7; n=33/148), not distinguishable vs national 27.0% — keuhkosyoparaportti_2019_2023.html, Taulukko 11
- `cty:life_prolonging:Keski_Pohjanmaan_hyvinvointialue` (verified locally): Keski-Pohjanmaan hyvinvointialue: life-prolonging treatment 32.4% (95% CI 25.4–40.3; n=48/148), not distinguishable vs national 30.4% — keuhkosyoparaportti_2019_2023.html, Taulukko 11
- `cty:mdt_recorded:Keski_Pohjanmaan_hyvinvointialue` (verified locally): Keski-Pohjanmaan hyvinvointialue: MDT meeting recorded 1.4% (95% CI 0.4–4.8; n=2/148), below vs national 6.0% — keuhkosyoparaportti_2019_2023.html, Taulukko 11
- `cty:no_treatment_record:Keski_Pohjanmaan_hyvinvointialue` (verified locally): Keski-Pohjanmaan hyvinvointialue: no treatment record within 12 months 25.0% (95% CI 18.7–32.5; n=37/148), not distinguishable vs national 27.5% — keuhkosyoparaportti_2019_2023.html, Taulukko 11
- `cty:symptomatic:Keski_Pohjanmaan_hyvinvointialue` (verified locally): Keski-Pohjanmaan hyvinvointialue: symptomatic treatment 46.6% (95% CI 38.8–54.6; n=69/148), not distinguishable vs national 39.5% — keuhkosyoparaportti_2019_2023.html, Taulukko 11
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
- `q:14dff3e002` (verified locally): Policy evidence for pathway stage 'Referral' — filha_lung_programme_2026_fi.pdf, PDF p.7 (unnumbered); p.15; p.17; p.20; p.21; p.23; p.24
- `q:20d6ca414e` (verified locally): “Valtakunnallisesti ei ole ollut tarkkaa yhtenäistä ohjeistusta siitä, millä aikataululla diagnostiikan eri osa-alueet tulisi olla tehtyinä”; regional variation in diagnostic speed is large. The programme itself sets no day-based targets — filha_lung_programme_2026_fi.pdf, p.4
- `q:323de0d90d` (verified locally): Report evidence for pathway stage 'Primary care / occupational health' — keuhkosyoparaportti_2019_2023.html, §3.3 Menetelmät
- `q:39e6ba43a9` (verified locally): Report evidence for pathway stage 'MDT' — keuhkosyoparaportti_2019_2023.html, §3.3 Menetelmät
- `q:432c0e51d6` (verified locally): The upcoming national diagnostics recommendation will include “suositellut aikarajat erikoissairaanhoitoon eri diagnostiikan polun vaiheille” (recommended time limits in specialist care), to be carried out (“toteutetaan”; may mean produced or implemented) before the 2030 mid-term evaluation — filha_lung_programme_2026_fi.pdf, p.16
- `q:47c7e11303` (verified locally): Finland has no quality registry for lung cancer or for any other cancer. — filha_lung_programme_2026_fi.pdf, p.21
- `q:556431a0c2` (verified locally): the patient is referred to specialist care according to local instructions — filha_lung_programme_2026_fi.pdf, p.15
- `q:5eb155decc` (verified locally): Report evidence for pathway stage 'Imaging' — keuhkosyoparaportti_2019_2023.html, §4.1.1 Toteamistapa
- `q:614febebf2` (verified locally): When (p.24): > “Väliarvio toteutetaan vuonna 2030, ohjelman puolivälissä ja loppuarviointi vuonna 2036. Eri > osa-alueiden suositukset toteutetaan ennen väliarviointia.” — filha_lung_programme_2026_fi.pdf, p.24
- `q:7885b0974f` (verified locally): Report evidence for pathway stage 'Diagnosis' — keuhkosyoparaportti_2019_2023.html, §4.1.3 Levinneisyystiedon kattavuus
- `q:82d365cd2c` (verified locally): “Tällä hetkellä keuhkosyöpään liittyvien tietojen raportointi, kerääminen ja tallentaminen on puutteellista”; nationally uniform recording instructions (“yhtenäiset kirjaamisohjeet”) must be ensured — filha_lung_programme_2026_fi.pdf, p.21
- `q:950a2f797b` (verified locally): Reporting, collection and storage of lung cancer data is currently incomplete. — filha_lung_programme_2026_fi.pdf, p.21
- `q:9a1cd194f5` (verified locally): support a smooth transfer to specialist care by defining standardised referral criteria within the national pathways, so that patients with possible cancer symptoms who meet them are directed quickly to diagnostic tests — roadmap_2026_2031_fi.pdf, p.52
- `q:abcbb06ae3` (verified locally): 2026–2028: guidance on a named doctor, nurse or specialist worker coordinating cancer care. 2029–2031: wellbeing services counties have adopted it. — roadmap_2026_2031_fi.pdf, p.32
- `q:c61439b30f` (verified locally): 2026–2028: standardised referral criteria and symptom-based models included in the national pathways of at least the five most common cancers. — roadmap_2026_2031_fi.pdf, p.53
- `q:ccda20dce9` (verified locally): Finland has no national system steering cancer pathways or their monitoring, “mukaan lukien hoitoonpääsy” — strategy_2026_2035_fi.pdf, p.33
- `q:fc81032a80` (verified locally): Measure 1.2.3: Create an operating model and guidance for a named worker responsible for coordinating cancer care. — roadmap_2026_2031_fi.pdf, p.32
- `rec:1` (recommendation (ours)): Team recommendation 1: Counties report access times using the THL 21/2016 definitions, with handover alerts. Each wellbeing services county reports lung cancer access times (referral → first specialist visit → diagnosis → treatment start) using the definitions in THL's Hoitoonpääsyn seuranta syövän hoidossa (Ohjaus 21/2016). Until national target times exist, flag stalled handovers. — recommendations.md, §1. Counties report access times using the THL 21/2016 definitions, with handover alerts
- `rec:2` (recommendation (ours)): Team recommendation 2: A KYS-style referral template, a persistent-symptoms rule and a named contact. Adopt a standard referral content list and template, modelled on KYS. • Add a rule for primary care: if symptoms persist after a normal X-ray, refer for a pulmonologist assessment. • Name a contact person for the diagnostic phase, from referral to diagnosis. — recommendations.md, §2. A KYS-style referral template, a persistent-symptoms rule and a named contact
- `rec:3` (recommendation (ours)): Team recommendation 3: Report recording completeness per county: stage, drug treatment, MDT coding. Publish, per county, how completely stage, drug treatment and MDT meetings are recorded. Read county ‘gaps’ in these fields as data-quality signals first. — recommendations.md, §3. Report recording completeness per county: stage, drug treatment, MDT coding
- `reg:kys_persistent` (verified by Hellu): KYS: refer persistent unexplained symptoms even if the X-ray is clear — pathway_brief.md, 6. Regional pathways compared
- `reg:kys_template` (verified by Hellu): Only KYS lists required referral content and provides a referral template — pathway_brief.md, 6. Regional pathways compared
- `reg:named_contact` (verified by Hellu): No region names a contact person for the diagnostic phase — pathway_brief.md, 6. Regional pathways compared
- `thl:21_2016` (verified by Hellu): THL Ohjaus 21/2016 defines how cancer access times are recorded, for 16 cancers — pathway_brief.md, 6. Regional pathways compared
