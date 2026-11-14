# Länsi-Uusimaa: lung cancer pathway brief

Status: **validated** · gemini-4-argon (thinking HIGH) · 2026-11-14T12:54:06+00:00 · attempts: 1

## Where do we lag?

**Across overlapping treatment categories and procedure records, Länsi-Uusimaa lags national values in its crude life-prolonging treatment share and crude recorded MDT meeting share, though MDT figures measure recording practice.** `cty:life_prolonging:Länsi_Uudenmaan_hyvinvointialue, nat:life_prolonging, cty:mdt_recorded:Länsi_Uudenmaan_hyvinvointialue, nat:mdt_recorded, bs:coverage:MDT`

- In overlapping treatment categories, the county's crude life-prolonging treatment share is 25.2% (95% CI 22.7–27.9; n=267/1058) alongside the national 30.4% (4522/14873), and the 95% confidence interval excludes the national value. `cty:life_prolonging:Länsi_Uudenmaan_hyvinvointialue, nat:life_prolonging`
- Across overlapping treatment categories where a patient can have several treatments, Länsi-Uusimaa's crude curative share is 31.9% (95% CI 29.1–34.7; n=337/1058), with the 95% confidence interval excluding and exceeding the national 27.0% (4009/14873), while its crude symptomatic share is 40.1% (95% CI 37.2–43.1; n=424/1058), with the 95% confidence interval including the national 39.5% (5871/14873). `cty:curative:Länsi_Uudenmaan_hyvinvointialue, nat:curative, cty:symptomatic:Länsi_Uudenmaan_hyvinvointialue, nat:symptomatic`
- The crude share of patients with a recorded MDT meeting is 0.2% (95% CI 0.1–0.7; n=2/1058), whose 95% confidence interval excludes the national 6.0% (893/14873), but MDT records measure recording practice, not care, because specialist procedures enter HILMO only from direct patient contacts. `cty:mdt_recorded:Länsi_Uudenmaan_hyvinvointialue, nat:mdt_recorded, bs:coverage:MDT, q:39e6ba43a9`

## How sure are we?

**Public county data omit wait times, referrals and primary care visits, and crude treatment shares cannot be stage-adjusted because stage is missing for about 48% of patients.** `cty:life_prolonging:Länsi_Uudenmaan_hyvinvointialue, bs:coverage:Referral, bs:coverage:Primary_care_occupational_health, bs:coverage:Treatment_start, bs:coverage:Diagnosis, q:7885b0974f`

- County shares are crude and have separate limitations: they are not age-adjusted (digitised age-adjusted figures from Kuva 16, at ±0.5 percentage points precision, exist for curative treatment only, by sex, with national lines at 26.7% for men and 26.9% for women), and separately they cannot be stage-adjusted because stage at diagnosis is missing for about 48% of patients. `cty:curative:Länsi_Uudenmaan_hyvinvointialue, k16:curative:men:national, k16:curative:women:national, bs:coverage:Diagnosis, q:7885b0974f`
- The crude share with no treatment record within 12 months is 28.5% (95% CI 25.9–31.3; n=302/1058), with its 95% confidence interval including the national 27.5% (4089/14873); this mixes untreated patients and treatment that was not recorded, while a journal article finding about 90% HILMO and Cancer Registry concordance applies to diagnoses only. `cty:no_treatment_record:Länsi_Uudenmaan_hyvinvointialue, nat:no_treatment_record, bs:coverage:Treatment_start, lit:hilmo_90`
- Public report data do not measure symptoms, referrals or treatment start dates by county, primary care visits are not included in the report's data, occupational health is not mentioned at all, and imaging appears only indirectly because about 20% of patients are diagnosed on clinical examination alone, such as imaging. `bs:coverage:Symptoms, bs:coverage:Referral, bs:coverage:Treatment_start, bs:coverage:Primary_care_occupational_health, q:323de0d90d, bs:coverage:Imaging, q:5eb155decc`
- In preliminary, unpublished national averages (not county-specific), lung cancer takes 155 days from symptoms to treatment in Finland compared with 107 days in Sweden and 67 days in Denmark, with 56 days of patient delay, 41 days in primary care and 58 days in specialist care. `mot:total_fi, mot:total_se, mot:total_dk, mot:patient, mot:primary, mot:specialist`

## What should we do first?

**The team recommends publishing stage, drug and MDT coding coverage, tracking THL Ohjaus 21/2016 access times with handover alerts, and adopting a referral template with a diagnostic contact person.** `rec:1, rec:2, rec:3, thl:21_2016`

- Given Länsi-Uusimaa's crude recorded MDT share of 0.2% (95% CI 0.1–0.7; n=2/1058) versus 6.0% (893/14873) nationally, its crude life-prolonging share of 25.2% (95% CI 22.7–27.9; n=267/1058) versus 30.4% (4522/14873) across overlapping treatment categories, and missing stage for about 48% of patients, the team recommends publishing per-county stage, drug treatment and MDT recording coverage as data-quality signals. `rec:3, cty:mdt_recorded:Länsi_Uudenmaan_hyvinvointialue, nat:mdt_recorded, cty:life_prolonging:Länsi_Uudenmaan_hyvinvointialue, nat:life_prolonging, bs:coverage:Diagnosis, q:7885b0974f, q:950a2f797b`
- Because the Health Care Act sets no legal maximum time for a cancer suspicion and uniform diagnostic timetables are lacking, the team recommends reporting access times using THL Ohjaus 21/2016 definitions for 16 cancers and flagging stalled handovers, while the Filha programme's diagnostics recommendation with recommended time limits is to be carried out before the 2030 mid-term evaluation. `rec:1, law:no_max, thl:21_2016, q:24169121a4, q:20d6ca414e, q:8f358a9de6, q:432c0e51d6, q:614febebf2`
- Backed by mentor insight that a weak referral gets a lower urgency rating and by KYS's regional pathway document, the team recommends adopting a KYS-style referral template and referring persistent unexplained symptoms for a pulmonologist assessment after a normal X-ray, while under measure 2.5.2 the STM roadmap plans standardised referral criteria and symptom-based models by 2026–2028. `rec:2, mentor:kaisa_referral, reg:kys_template, reg:kys_persistent, reg:only_kys_xray, q:0780bf74b0, q:37bb4c3b38, q:9a1cd194f5, q:c61439b30f`
- Because no reviewed regional pathway document names a diagnostic-phase contact person, the team recommends naming a contact person from referral to diagnosis, while under measure 1.2.3 the STM roadmap plans guidance on a named care-coordinator model by 2026–2028 that counties adopt by 2029–2031 without specifying the care phase. `rec:2, reg:named_contact, q:fc81032a80, q:74a8cee731, q:abcbb06ae3, q:050ee09ebe`

## Review flags (for human review only)

_Flags are for human review only; they never change the brief's status or approve it._

- none

## Claims cited

- `bs:coverage:Diagnosis` (verified locally): Pathway stage 'Diagnosis' is measured in public data: yes (by county: yes (Kuva 7, 10, 13: PNG only)) — keuhkosyoparaportti_2019_2023.html, §4.1, Taulukko 2–4, Kuva 5–13
- `bs:coverage:Imaging` (verified locally): Pathway stage 'Imaging' is measured in public data: partly (by county: partly (Kuva 7, PNG only)) — keuhkosyoparaportti_2019_2023.html, §4.1.1, Taulukko 2, Kuva 5–7
- `bs:coverage:MDT` (verified locally): Pathway stage 'MDT' is measured in public data: partly (by county: yes (Taulukko 11)) — keuhkosyoparaportti_2019_2023.html, §3.3, §4.2, Taulukko 5, 10, 11, 13
- `bs:coverage:Primary_care_occupational_health` (verified locally): Pathway stage 'Primary care / occupational health' is measured in public data: no (by county: no) — keuhkosyoparaportti_2019_2023.html, §3.3
- `bs:coverage:Referral` (verified locally): Pathway stage 'Referral' is measured in public data: no (by county: no) — keuhkosyoparaportti_2019_2023.html, whole report (no relevant data found)
- `bs:coverage:Symptoms` (verified locally): Pathway stage 'Symptoms' is measured in public data: no (by county: no) — keuhkosyoparaportti_2019_2023.html, whole report (no relevant data found)
- `bs:coverage:Treatment_start` (verified locally): Pathway stage 'Treatment start' is measured in public data: partly (by county: yes (type only, Taulukko 11)) — keuhkosyoparaportti_2019_2023.html, §4.2, §4.2.2, Taulukko 6–9, 11, 12, Kuva 14, 17
- `cty:curative:Länsi_Uudenmaan_hyvinvointialue` (verified locally): Länsi-Uudenmaan hyvinvointialue: curative treatment 31.9% (95% CI 29.1–34.7; n=337/1058), above vs national 27.0% — keuhkosyoparaportti_2019_2023.html, Taulukko 11
- `cty:life_prolonging:Länsi_Uudenmaan_hyvinvointialue` (verified locally): Länsi-Uudenmaan hyvinvointialue: life-prolonging treatment 25.2% (95% CI 22.7–27.9; n=267/1058), below vs national 30.4% — keuhkosyoparaportti_2019_2023.html, Taulukko 11
- `cty:mdt_recorded:Länsi_Uudenmaan_hyvinvointialue` (verified locally): Länsi-Uudenmaan hyvinvointialue: MDT meeting recorded 0.2% (95% CI 0.1–0.7; n=2/1058), below vs national 6.0% — keuhkosyoparaportti_2019_2023.html, Taulukko 11
- `cty:no_treatment_record:Länsi_Uudenmaan_hyvinvointialue` (verified locally): Länsi-Uudenmaan hyvinvointialue: no treatment record within 12 months 28.5% (95% CI 25.9–31.3; n=302/1058), not distinguishable vs national 27.5% — keuhkosyoparaportti_2019_2023.html, Taulukko 11
- `cty:symptomatic:Länsi_Uudenmaan_hyvinvointialue` (verified locally): Länsi-Uudenmaan hyvinvointialue: symptomatic treatment 40.1% (95% CI 37.2–43.1; n=424/1058), not distinguishable vs national 39.5% — keuhkosyoparaportti_2019_2023.html, Taulukko 11
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
- `q:0780bf74b0` (verified locally): Policy evidence for pathway stage 'Symptoms' — roadmap_2026_2031_fi.pdf, p.52; p.53
- `q:20d6ca414e` (verified locally): “Valtakunnallisesti ei ole ollut tarkkaa yhtenäistä ohjeistusta siitä, millä aikataululla diagnostiikan eri osa-alueet tulisi olla tehtyinä”; regional variation in diagnostic speed is large. The programme itself sets no day-based targets — filha_lung_programme_2026_fi.pdf, p.4
- `q:24169121a4` (verified locally): Strategy p.5 (= PDF p.5), “Strategiset tavoitteet”, indicator under “Varmistetaan yhdenvertainen ja vaikuttava syövänhoito”: > “Potilaat pääsevät hoitoon tavoiteaikojen puitteissa” > “ THL (Ohjaus 21/2016). Hoitoonpääsyn seuranta syövän hoidossa.” — strategy_2026_2035_fi.pdf, p.5
- `q:323de0d90d` (verified locally): Report evidence for pathway stage 'Primary care / occupational health' — keuhkosyoparaportti_2019_2023.html, §3.3 Menetelmät
- `q:37bb4c3b38` (verified locally): Policy evidence for pathway stage 'Referral' — roadmap_2026_2031_fi.pdf, p.52; p.106
- `q:39e6ba43a9` (verified locally): Report evidence for pathway stage 'MDT' — keuhkosyoparaportti_2019_2023.html, §3.3 Menetelmät
- `q:432c0e51d6` (verified locally): The upcoming national diagnostics recommendation will include “suositellut aikarajat erikoissairaanhoitoon eri diagnostiikan polun vaiheille” (recommended time limits in specialist care), to be carried out (“toteutetaan”; may mean produced or implemented) before the 2030 mid-term evaluation — filha_lung_programme_2026_fi.pdf, p.16
- `q:5eb155decc` (verified locally): Report evidence for pathway stage 'Imaging' — keuhkosyoparaportti_2019_2023.html, §4.1.1 Toteamistapa
- `q:614febebf2` (verified locally): When (p.24): > “Väliarvio toteutetaan vuonna 2030, ohjelman puolivälissä ja loppuarviointi vuonna 2036. Eri > osa-alueiden suositukset toteutetaan ennen väliarviointia.” — filha_lung_programme_2026_fi.pdf, p.24
- `q:74a8cee731` (verified locally): The most important thing is that the patient knows who has the overall picture of their care, and how they can contact the treating unit when needed. — roadmap_2026_2031_fi.pdf, p.32
- `q:7885b0974f` (verified locally): Report evidence for pathway stage 'Diagnosis' — keuhkosyoparaportti_2019_2023.html, §4.1.3 Levinneisyystiedon kattavuus
- `q:8f358a9de6` (verified locally): p.16: > “Tämän ohjelman yhtenä toimenpiteenä tuotetaan kansallinen suositus keuhkosyöpien diagnostiikasta. Se > sisältää myös lähetekriteerit perusterveydenhuollolle ja suositellut aikarajat erikoissairaanhoitoon > eri diagnostiikan polun vaiheille.” — filha_lung_programme_2026_fi.pdf, p.16
- `q:950a2f797b` (verified locally): Reporting, collection and storage of lung cancer data is currently incomplete. — filha_lung_programme_2026_fi.pdf, p.21
- `q:9a1cd194f5` (verified locally): support a smooth transfer to specialist care by defining standardised referral criteria within the national pathways, so that patients with possible cancer symptoms who meet them are directed quickly to diagnostic tests — roadmap_2026_2031_fi.pdf, p.52
- `q:abcbb06ae3` (verified locally): 2026–2028: guidance on a named doctor, nurse or specialist worker coordinating cancer care. 2029–2031: wellbeing services counties have adopted it. — roadmap_2026_2031_fi.pdf, p.32
- `q:c61439b30f` (verified locally): 2026–2028: standardised referral criteria and symptom-based models included in the national pathways of at least the five most common cancers. — roadmap_2026_2031_fi.pdf, p.53
- `q:fc81032a80` (verified locally): Measure 1.2.3: Create an operating model and guidance for a named worker responsible for coordinating cancer care. — roadmap_2026_2031_fi.pdf, p.32
- `rec:1` (recommendation (ours)): Team recommendation 1: Counties report access times using the THL 21/2016 definitions, with handover alerts. Each wellbeing services county reports lung cancer access times (referral → first specialist visit → diagnosis → treatment start) using the definitions in THL's Hoitoonpääsyn seuranta syövän hoidossa (Ohjaus 21/2016). Until national target times exist, flag stalled handovers. — recommendations.md, §1. Counties report access times using the THL 21/2016 definitions, with handover alerts
- `rec:2` (recommendation (ours)): Team recommendation 2: A KYS-style referral template, a persistent-symptoms rule and a named contact. Adopt a standard referral content list and template, modelled on KYS. • Add a rule for primary care: if symptoms persist after a normal X-ray, refer for a pulmonologist assessment. • Name a contact person for the diagnostic phase, from referral to diagnosis. — recommendations.md, §2. A KYS-style referral template, a persistent-symptoms rule and a named contact
- `rec:3` (recommendation (ours)): Team recommendation 3: Report recording completeness per county: stage, drug treatment, MDT coding. Publish, per county, how completely stage, drug treatment and MDT meetings are recorded. Read county ‘gaps’ in these fields as data-quality signals first. — recommendations.md, §3. Report recording completeness per county: stage, drug treatment, MDT coding
- `reg:kys_persistent` (verified by Hellu): KYS: refer persistent unexplained symptoms even if the X-ray is clear — pathway_brief.md, 6. Regional pathways compared
- `reg:kys_template` (verified by Hellu): Only KYS lists required referral content and provides a referral template — pathway_brief.md, 6. Regional pathways compared
- `reg:named_contact` (verified by Hellu): No region names a contact person for the diagnostic phase — pathway_brief.md, 6. Regional pathways compared
- `reg:only_kys_xray` (verified by Hellu): Only KYS tells primary care what to do with a normal X-ray and continuing symptoms — pathway_brief.md, 6. Regional pathways compared
- `thl:21_2016` (verified by Hellu): THL Ohjaus 21/2016 defines how cancer access times are recorded, for 16 cancers — pathway_brief.md, 6. Regional pathways compared
