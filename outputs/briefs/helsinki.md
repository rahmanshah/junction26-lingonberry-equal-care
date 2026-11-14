# Helsinki: lung cancer pathway brief

Status: **validated** · gemini-4-argon (thinking HIGH) · 2026-11-14T13:34:29+00:00 · attempts: 2

## Where do we lag?

**Helsingin kaupunki's crude recorded MDT share is 0.1% (95% CI 0.0–0.4; n=1/1486) versus 6.0% (893/14873) nationally, measuring recording practice, not care.** `cty:mdt_recorded:Helsingin_kaupunki, nat:mdt_recorded, bs:coverage:MDT`

- For recorded MDT meetings, Helsingin kaupunki's crude share of 0.1% (95% CI 0.0–0.4; n=1/1486) has a 95% confidence interval that excludes the national value of 6.0% (893/14873), reflecting that specialist procedures enter HILMO only from direct patient contacts rather than comprehensive multidisciplinary review. `cty:mdt_recorded:Helsingin_kaupunki, nat:mdt_recorded, bs:coverage:MDT, q:39e6ba43a9`
- Among overlapping treatment categories where a patient can have several, Helsingin kaupunki's crude symptomatic treatment share is 34.5% (95% CI 32.1–37.0; n=513/1486), with a 95% confidence interval excluding the national 39.5% (5871/14873), while crude curative treatment is 33.0% (95% CI 30.7–35.5; n=491/1486), excluding the national 27.0% (4009/14873) from above. `cty:symptomatic:Helsingin_kaupunki, nat:symptomatic, cty:curative:Helsingin_kaupunki, nat:curative`
- In the remaining overlapping categories where a patient can have several, the crude life-prolonging treatment share is 30.8% (95% CI 28.5–33.1; n=457/1486), whose 95% confidence interval includes the national 30.4% (4522/14873), and the crude share with no treatment record within 12 months—mixing untreated patients and unrecorded treatment—is 29.1% (95% CI 26.8–31.4; n=432/1486), including the national 27.5% (4089/14873). `cty:life_prolonging:Helsingin_kaupunki, nat:life_prolonging, cty:no_treatment_record:Helsingin_kaupunki, nat:no_treatment_record, bs:coverage:Treatment_start`
- While county-level wait times are not in public data, preliminary unpublished national figures show an average of 155 days from first symptoms to treatment in Finland (versus 107 in Sweden and 67 in Denmark), comprising a 56-day patient delay, a 41-day primary care interval, and a 58-day specialist care interval. `bs:coverage:Symptoms, bs:coverage:Treatment_start, mot:total_fi, mot:total_se, mot:total_dk, mot:patient, mot:primary, mot:specialist`

## How sure are we?

**Taulukko 11 gives only unadjusted crude county shares, and as a separate limitation, shares cannot be stage-adjusted because stage at diagnosis is missing for about 48% of patients.** `fig:age_adjusted_only_kuva16, bs:coverage:Diagnosis, q:7885b0974f`

- Taulukko 11 county shares are crude and not age-adjusted; age-adjusted county shares appear only in Kuva 16 (by sex, with 95% CIs), where national curative reference lines are digitised from the figure at 26.7% for men and 26.9% for women (±0.5 percentage points), with no digitised Helsingin kaupunki value to test whether its curative gap holds after age adjustment. `fig:age_adjusted_only_kuva16, k16:curative:men:national, k16:curative:women:national`
- As a separate limitation from age adjustment, treatment shares cannot be stage-adjusted because stage at diagnosis is missing for about 48% of patients, even though a journal article found that HILMO hospital discharge diagnoses match the Cancer Registry for about 90% of most cancer types regarding diagnosis concordance. `bs:coverage:Diagnosis, q:7885b0974f, lit:hilmo_90`
- Public report data do not measure symptoms or referral dates, outpatient primary care visits are not included in the report's data, occupational health is not mentioned, and imaging appears only indirectly because about 20% of patients are diagnosed on clinical examination alone, such as imaging. `bs:coverage:Symptoms, bs:coverage:Referral, bs:coverage:Primary_care_occupational_health, q:323de0d90d, bs:coverage:Imaging, q:5eb155decc`
- In specialist care, public data show that 93.6% of patients have a lung cancer visit in HILMO within 12 months and which treatment type is recorded, but not when visits or treatments started, while the HUS regional pathway document states that HUS refers patients to the MDT only when needed. `bs:coverage:First_specialist_visit, bs:coverage:Treatment_start, reg:mdt_practice`

## What should we do first?

**The team recommends publishing how completely stage, drug treatment, and MDT coding are recorded, reporting access times using THL 21/2016 definitions, and standardising referrals and diagnostic-phase contacts.** `rec:1, rec:2, rec:3, q:24169121a4, q:556431a0c2, q:950a2f797b, bs:coverage:MDT`

- Because Helsingin kaupunki's crude recorded MDT share is 0.1% (95% CI 0.0–0.4; n=1/1486) versus 6.0% (893/14873) nationally—measuring recording practice, not care—and stage is missing for about 48% of patients, the team recommends publishing per county how completely stage, drug treatment, and MDT meetings are recorded and reading gaps as data-quality signals first. `rec:3, cty:mdt_recorded:Helsingin_kaupunki, nat:mdt_recorded, bs:coverage:MDT, bs:coverage:Diagnosis, q:7885b0974f, q:950a2f797b`
- Since Finland has no cancer quality registry or unified national system monitoring access to care, and the Health Care Act (§52) sets no legal maximum time for a cancer suspicion, the team recommends reporting county access times using THL guidance Ohjaus 21/2016 definitions (covering 16 cancers) and flagging stalled handovers until national target times exist. `rec:1, filha:registry, q:47c7e11303, q:4e702a20fe, q:ccda20dce9, law:no_max, thl:21_2016, q:24169121a4`
- Supported by mentor insight that a weak referral gets a lower urgency rating in specialist care, the team recommends a standard referral template and referring persistent unexplained symptoms after a normal X-ray to a pulmonologist, modelled on the KYS regional pathway document, while the Filha programme's diagnostics recommendation is to be carried out before the 2030 mid-term evaluation. `rec:2, mentor:kaisa_referral, reg:kys_template, reg:kys_persistent, reg:only_kys_xray, q:29b792498e, q:8f358a9de6, q:614febebf2`
- Because regional pathway documents show no region names a diagnostic-phase contact person—with the HUS regional pathway document assigning a nurse at the first visit—the team recommends naming a contact person from referral to diagnosis, while STM roadmap measure 1.2.3 plans guidance on a named care-coordinator model by 2026–2028 for counties to adopt by 2029–2031 without specifying the care phase. `rec:2, reg:named_contact, q:fc81032a80, q:abcbb06ae3, q:050ee09ebe`

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
- `cty:curative:Helsingin_kaupunki` (verified locally): Helsingin kaupunki: curative treatment 33.0% (95% CI 30.7–35.5; n=491/1486), above vs national 27.0% — keuhkosyoparaportti_2019_2023.html, Taulukko 11
- `cty:life_prolonging:Helsingin_kaupunki` (verified locally): Helsingin kaupunki: life-prolonging treatment 30.8% (95% CI 28.5–33.1; n=457/1486), not distinguishable vs national 30.4% — keuhkosyoparaportti_2019_2023.html, Taulukko 11
- `cty:mdt_recorded:Helsingin_kaupunki` (verified locally): Helsingin kaupunki: MDT meeting recorded 0.1% (95% CI 0.0–0.4; n=1/1486), below vs national 6.0% — keuhkosyoparaportti_2019_2023.html, Taulukko 11
- `cty:no_treatment_record:Helsingin_kaupunki` (verified locally): Helsingin kaupunki: no treatment record within 12 months 29.1% (95% CI 26.8–31.4; n=432/1486), not distinguishable vs national 27.5% — keuhkosyoparaportti_2019_2023.html, Taulukko 11
- `cty:symptomatic:Helsingin_kaupunki` (verified locally): Helsingin kaupunki: symptomatic treatment 34.5% (95% CI 32.1–37.0; n=513/1486), below vs national 39.5% — keuhkosyoparaportti_2019_2023.html, Taulukko 11
- `fig:age_adjusted_only_kuva16` (verified locally): In the 2019–2023 report, county-level age-adjusted treatment shares appear only in Kuva 16 (a PNG figure, by sex, with 95% CIs); the county table (Taulukko 11) gives crude shares only — chart_data.md, Summary table; section 'Kuva 16 in detail'
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
- `q:24169121a4` (verified locally): Strategy p.5 (= PDF p.5), “Strategiset tavoitteet”, indicator under “Varmistetaan yhdenvertainen ja vaikuttava syövänhoito”: > “Potilaat pääsevät hoitoon tavoiteaikojen puitteissa” > “ THL (Ohjaus 21/2016). Hoitoonpääsyn seuranta syövän hoidossa.” — strategy_2026_2035_fi.pdf, p.5
- `q:29b792498e` (verified locally): Policy evidence for pathway stage 'Referral' — filha_lung_programme_2026_fi.pdf, p.16
- `q:323de0d90d` (verified locally): Report evidence for pathway stage 'Primary care / occupational health' — keuhkosyoparaportti_2019_2023.html, §3.3 Menetelmät
- `q:39e6ba43a9` (verified locally): Report evidence for pathway stage 'MDT' — keuhkosyoparaportti_2019_2023.html, §3.3 Menetelmät
- `q:47c7e11303` (verified locally): Finland has no quality registry for lung cancer or for any other cancer. — filha_lung_programme_2026_fi.pdf, p.21
- `q:4e702a20fe` (verified locally): Finland has no unified national system to steer the drafting of cancer-specific treatment recommendations, or the implementation and monitoring of care pathways based on them (quality and effectiveness targets/indicators, including access to care, and cancer-specific and generic PROMs). Existing recommendations and pathways, and the targets and indicators to be monitored, are not coordinated nationally. This maintains regional inequality in the availability and effectiveness of cancer care. — strategy_2026_2035_fi.pdf, p.33
- `q:556431a0c2` (verified locally): the patient is referred to specialist care according to local instructions — filha_lung_programme_2026_fi.pdf, p.15
- `q:5eb155decc` (verified locally): Report evidence for pathway stage 'Imaging' — keuhkosyoparaportti_2019_2023.html, §4.1.1 Toteamistapa
- `q:614febebf2` (verified locally): When (p.24): > “Väliarvio toteutetaan vuonna 2030, ohjelman puolivälissä ja loppuarviointi vuonna 2036. Eri > osa-alueiden suositukset toteutetaan ennen väliarviointia.” — filha_lung_programme_2026_fi.pdf, p.24
- `q:7885b0974f` (verified locally): Report evidence for pathway stage 'Diagnosis' — keuhkosyoparaportti_2019_2023.html, §4.1.3 Levinneisyystiedon kattavuus
- `q:8f358a9de6` (verified locally): p.16: > “Tämän ohjelman yhtenä toimenpiteenä tuotetaan kansallinen suositus keuhkosyöpien diagnostiikasta. Se > sisältää myös lähetekriteerit perusterveydenhuollolle ja suositellut aikarajat erikoissairaanhoitoon > eri diagnostiikan polun vaiheille.” — filha_lung_programme_2026_fi.pdf, p.16
- `q:950a2f797b` (verified locally): Reporting, collection and storage of lung cancer data is currently incomplete. — filha_lung_programme_2026_fi.pdf, p.21
- `q:abcbb06ae3` (verified locally): 2026–2028: guidance on a named doctor, nurse or specialist worker coordinating cancer care. 2029–2031: wellbeing services counties have adopted it. — roadmap_2026_2031_fi.pdf, p.32
- `q:ccda20dce9` (verified locally): Finland has no national system steering cancer pathways or their monitoring, “mukaan lukien hoitoonpääsy” — strategy_2026_2035_fi.pdf, p.33
- `q:fc81032a80` (verified locally): Measure 1.2.3: Create an operating model and guidance for a named worker responsible for coordinating cancer care. — roadmap_2026_2031_fi.pdf, p.32
- `rec:1` (recommendation (ours)): Team recommendation 1: Counties report access times using the THL 21/2016 definitions, with handover alerts. Each wellbeing services county reports lung cancer access times (referral → first specialist visit → diagnosis → treatment start) using the definitions in THL's Hoitoonpääsyn seuranta syövän hoidossa (Ohjaus 21/2016). Until national target times exist, flag stalled handovers. — recommendations.md, §1. Counties report access times using the THL 21/2016 definitions, with handover alerts
- `rec:2` (recommendation (ours)): Team recommendation 2: A KYS-style referral template, a persistent-symptoms rule and a named contact. Adopt a standard referral content list and template, modelled on KYS. • Add a rule for primary care: if symptoms persist after a normal X-ray, refer for a pulmonologist assessment. • Name a contact person for the diagnostic phase, from referral to diagnosis. — recommendations.md, §2. A KYS-style referral template, a persistent-symptoms rule and a named contact
- `rec:3` (recommendation (ours)): Team recommendation 3: Report recording completeness per county: stage, drug treatment, MDT coding. Publish, per county, how completely stage, drug treatment and MDT meetings are recorded. Read county ‘gaps’ in these fields as data-quality signals first. — recommendations.md, §3. Report recording completeness per county: stage, drug treatment, MDT coding
- `reg:kys_persistent` (verified by Hellu): KYS: refer persistent unexplained symptoms even if the X-ray is clear — pathway_brief.md, 6. Regional pathways compared
- `reg:kys_template` (verified by Hellu): Only KYS lists required referral content and provides a referral template — pathway_brief.md, 6. Regional pathways compared
- `reg:mdt_practice` (verified by Hellu): MDT practice differs: KYS every patient weekly, Keski-Suomi every new case, HUS when needed — pathway_brief.md, 6. Regional pathways compared
- `reg:named_contact` (verified by Hellu): No region names a contact person for the diagnostic phase — pathway_brief.md, 6. Regional pathways compared
- `reg:only_kys_xray` (verified by Hellu): Only KYS tells primary care what to do with a normal X-ray and continuing symptoms — pathway_brief.md, 6. Regional pathways compared
- `thl:21_2016` (verified by Hellu): THL Ohjaus 21/2016 defines how cancer access times are recorded, for 16 cancers — pathway_brief.md, 6. Regional pathways compared
