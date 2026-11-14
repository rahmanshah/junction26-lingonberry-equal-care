# Keski-Suomi: lung cancer pathway brief

Status: **validated** · gemini-4-argon (thinking HIGH) · 2026-11-14T13:41:26+00:00 · attempts: 1

## Where do we lag?

**Keski-Suomi's crude recorded MDT share of 3.8% (95% CI 2.5–5.5; n=24/637) lags the 6.0% (893/14873) national share, and its regional pathway document states no referral handling time.** `cty:mdt_recorded:Keski_Suomen_hyvinvointialue, nat:mdt_recorded, reg:ks_referral`

- The county's crude recorded MDT meeting share of 3.8% (95% CI 2.5–5.5; n=24/637) has a 95% confidence interval that excludes the national 6.0% (893/14873), although HILMO MDT codes measure recording practice rather than care and Keski-Suomi's regional pathway document states every new case is reviewed. `cty:mdt_recorded:Keski_Suomen_hyvinvointialue, nat:mdt_recorded, bs:coverage:MDT, q:39e6ba43a9, reg:mdt_practice`
- In overlapping treatment categories, Keski-Suomi's crude curative share of 27.2% (95% CI 23.9–30.7; n=173/637) vs 27.0% (4009/14873) nationally and crude symptomatic share of 36.3% (95% CI 32.6–40.1; n=231/637) vs 39.5% (5871/14873) have 95% confidence intervals including national values, whereas crude life-prolonging treatment of 37.2% (95% CI 33.5–41.0; n=237/637) excludes and exceeds 30.4% (4522/14873). `cty:curative:Keski_Suomen_hyvinvointialue, nat:curative, cty:symptomatic:Keski_Suomen_hyvinvointialue, nat:symptomatic, cty:life_prolonging:Keski_Suomen_hyvinvointialue, nat:life_prolonging`
- The county's crude share of patients with no treatment record within 12 months is 24.5% (95% CI 21.3–28.0; n=156/637) compared with 27.5% (4089/14873) nationally, with the 95% confidence interval including the national value in a category that mixes untreated patients and treatment that was not recorded. `cty:no_treatment_record:Keski_Suomen_hyvinvointialue, nat:no_treatment_record, bs:coverage:Treatment_start`
- Keski-Suomi's regional pathway document targets a lung clinic appointment within 2–3 weeks or at the latest about 1 month and tissue sample results in about 1–2 weeks without reporting if targets are met, while preliminary, unpublished national figures average 155 days from symptoms to treatment, including 58 days in specialist care. `reg:ks_target, reg:ks_tissue, reg:not_monitored, mot:total_fi, mot:specialist`

## How sure are we?

**Taulukko 11 gives only crude county shares without age or stage adjustment, and public report data omit primary care visits, referral dates, and pathway waiting times.** `fig:age_adjusted_only_kuva16, bs:coverage:Diagnosis, bs:coverage:Primary_care_occupational_health, bs:coverage:Referral, bs:coverage:Treatment_start`

- Taulukko 11 reports crude county shares that are not age-adjusted; in the 2019–2023 report, county-level age-adjusted shares appear only in Kuva 16 (a PNG figure by sex with 95% CIs), from which only the digitised national curative reference lines of 26.7% for men and 26.9% for women (±0.5 percentage points) are available here. `fig:age_adjusted_only_kuva16, k16:curative:men:national, k16:curative:women:national`
- Separately from age adjustment, county shares cannot be stage-adjusted because stage at diagnosis is missing for about 48% of patients, and while a journal article found HILMO diagnoses match the Cancer Registry for about 90% of most cancer types, this measures diagnosis concordance only and not treatment or MDT recording. `bs:coverage:Diagnosis, q:7885b0974f, lit:hilmo_90`
- Public report data do not measure symptoms, referral dates, when the first specialist visit or treatment started, or imaging waits (showing only that about 20% are diagnosed on clinical examination such as imaging alone), and outpatient primary care visits are not included in the report's data while occupational health is unmentioned. `bs:coverage:Symptoms, bs:coverage:Referral, bs:coverage:First_specialist_visit, bs:coverage:Treatment_start, bs:coverage:Imaging, q:5eb155decc, bs:coverage:Primary_care_occupational_health, q:323de0d90d`
- Preliminary, unpublished national figures indicate delays of 56 days for patients and 41 days in primary care before the 58-day specialist care interval, yet Finland has no cancer quality registry and the Health Care Act sets no legal maximum time for a cancer suspicion. `mot:patient, mot:primary, mot:specialist, filha:registry, q:47c7e11303, law:no_max`

## What should we do first?

**The team recommends publishing county recording completeness for MDT, stage, and drug treatment, reporting access times using THL 21/2016 definitions with handover alerts, and standardising referrals and diagnostic coordination.** `rec:3, rec:1, rec:2`

- The team recommends publishing county recording completeness for stage, drug treatment, and MDT meetings to read gaps as data-quality signals, as Keski-Suomi's crude recorded MDT share is 3.8% (95% CI 2.5–5.5; n=24/637) vs 6.0% (893/14873) nationally despite its regional pathway document reviewing every new case, stage is missing for about 48%, and national data reporting is incomplete. `rec:3, cty:mdt_recorded:Keski_Suomen_hyvinvointialue, nat:mdt_recorded, reg:mdt_practice, bs:coverage:Diagnosis, q:82d365cd2c`
- The team recommends reporting lung cancer access times from referral to first specialist visit, diagnosis, and treatment start using THL guidance Ohjaus 21/2016 definitions for 16 cancers and flagging stalled handovers, because Keski-Suomi's regional pathway document states no referral handling time and does not report whether target times are met. `rec:1, thl:21_2016, q:24169121a4, reg:ks_referral, reg:not_monitored`
- The team recommends adopting a standard referral content list and template, a primary-care rule to refer persistent symptoms after a normal X-ray to a pulmonologist, and a named diagnostic-phase contact person, supported by mentor insight that weak referrals get lower urgency ratings while occupational health—included in Keski-Suomi's regional pathway document—reaches specialist care faster. `rec:2, mentor:kaisa_referral, mentor:hanna_occupational, reg:occupational, q:556431a0c2`
- The team's recommendations address local gaps while the Filha National Lung Cancer Programme's diagnostics recommendation with primary-care referral criteria and recommended time limits is to be carried out before the 2030 mid-term evaluation, and while the STM roadmap's measure 1.2.3 plans guidance on a named care-coordinator model by 2026–2028 for county adoption by 2029–2031. `rec:1, rec:2, q:29b792498e, q:432c0e51d6, q:614febebf2, q:050ee09ebe, q:abcbb06ae3`

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
- `cty:curative:Keski_Suomen_hyvinvointialue` (verified locally): Keski-Suomen hyvinvointialue: curative treatment 27.2% (95% CI 23.9–30.7; n=173/637), not distinguishable vs national 27.0% — keuhkosyoparaportti_2019_2023.html, Taulukko 11
- `cty:life_prolonging:Keski_Suomen_hyvinvointialue` (verified locally): Keski-Suomen hyvinvointialue: life-prolonging treatment 37.2% (95% CI 33.5–41.0; n=237/637), above vs national 30.4% — keuhkosyoparaportti_2019_2023.html, Taulukko 11
- `cty:mdt_recorded:Keski_Suomen_hyvinvointialue` (verified locally): Keski-Suomen hyvinvointialue: MDT meeting recorded 3.8% (95% CI 2.5–5.5; n=24/637), below vs national 6.0% — keuhkosyoparaportti_2019_2023.html, Taulukko 11
- `cty:no_treatment_record:Keski_Suomen_hyvinvointialue` (verified locally): Keski-Suomen hyvinvointialue: no treatment record within 12 months 24.5% (95% CI 21.3–28.0; n=156/637), not distinguishable vs national 27.5% — keuhkosyoparaportti_2019_2023.html, Taulukko 11
- `cty:symptomatic:Keski_Suomen_hyvinvointialue` (verified locally): Keski-Suomen hyvinvointialue: symptomatic treatment 36.3% (95% CI 32.6–40.1; n=231/637), not distinguishable vs national 39.5% — keuhkosyoparaportti_2019_2023.html, Taulukko 11
- `fig:age_adjusted_only_kuva16` (verified locally): In the 2019–2023 report, county-level age-adjusted treatment shares appear only in Kuva 16 (a PNG figure, by sex, with 95% CIs); the county table (Taulukko 11) gives crude shares only — chart_data.md, Summary table; section 'Kuva 16 in detail'
- `filha:registry` (verified locally): No lung cancer or other cancer quality registry; Cancer Registry, THL and FICAN are assessing one, starting with lung cancer — pathway_brief.md, 3. National level: a programme, but no pathway or time targets
- `k16:curative:men:national` (verified locally): Finland (national reference line): age-adjusted curative treatment share, men, 26.7% — keuhkosyoparaportti_2019_2023.html, Kuva 16
- `k16:curative:women:national` (verified locally): Finland (national reference line): age-adjusted curative treatment share, women, 26.9% — keuhkosyoparaportti_2019_2023.html, Kuva 16
- `law:no_max` (verified by Hellu): There is no legal maximum time for a cancer suspicion — pathway_brief.md, 5. What the law guarantees (Health Care Act, §52)
- `lit:hilmo_90` (verified by Hellu): HILMO diagnoses match the Cancer Registry for about 90% of most cancer types — pathway_brief.md, 6. Regional pathways compared
- `mentor:hanna_occupational` (mentor insight): Occupational health gets patients to specialist care faster — pathway_brief.md, 7. Where patients get stuck
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
- `q:24169121a4` (verified locally): Strategy p.5 (= PDF p.5), “Strategiset tavoitteet”, indicator under “Varmistetaan yhdenvertainen ja vaikuttava syövänhoito”: > “Potilaat pääsevät hoitoon tavoiteaikojen puitteissa” > “ THL (Ohjaus 21/2016). Hoitoonpääsyn seuranta syövän hoidossa.” — strategy_2026_2035_fi.pdf, p.5
- `q:29b792498e` (verified locally): Policy evidence for pathway stage 'Referral' — filha_lung_programme_2026_fi.pdf, p.16
- `q:323de0d90d` (verified locally): Report evidence for pathway stage 'Primary care / occupational health' — keuhkosyoparaportti_2019_2023.html, §3.3 Menetelmät
- `q:39e6ba43a9` (verified locally): Report evidence for pathway stage 'MDT' — keuhkosyoparaportti_2019_2023.html, §3.3 Menetelmät
- `q:432c0e51d6` (verified locally): The upcoming national diagnostics recommendation will include “suositellut aikarajat erikoissairaanhoitoon eri diagnostiikan polun vaiheille” (recommended time limits in specialist care), to be carried out (“toteutetaan”; may mean produced or implemented) before the 2030 mid-term evaluation — filha_lung_programme_2026_fi.pdf, p.16
- `q:47c7e11303` (verified locally): Finland has no quality registry for lung cancer or for any other cancer. — filha_lung_programme_2026_fi.pdf, p.21
- `q:556431a0c2` (verified locally): the patient is referred to specialist care according to local instructions — filha_lung_programme_2026_fi.pdf, p.15
- `q:5eb155decc` (verified locally): Report evidence for pathway stage 'Imaging' — keuhkosyoparaportti_2019_2023.html, §4.1.1 Toteamistapa
- `q:614febebf2` (verified locally): When (p.24): > “Väliarvio toteutetaan vuonna 2030, ohjelman puolivälissä ja loppuarviointi vuonna 2036. Eri > osa-alueiden suositukset toteutetaan ennen väliarviointia.” — filha_lung_programme_2026_fi.pdf, p.24
- `q:7885b0974f` (verified locally): Report evidence for pathway stage 'Diagnosis' — keuhkosyoparaportti_2019_2023.html, §4.1.3 Levinneisyystiedon kattavuus
- `q:82d365cd2c` (verified locally): “Tällä hetkellä keuhkosyöpään liittyvien tietojen raportointi, kerääminen ja tallentaminen on puutteellista”; nationally uniform recording instructions (“yhtenäiset kirjaamisohjeet”) must be ensured — filha_lung_programme_2026_fi.pdf, p.21
- `q:abcbb06ae3` (verified locally): 2026–2028: guidance on a named doctor, nurse or specialist worker coordinating cancer care. 2029–2031: wellbeing services counties have adopted it. — roadmap_2026_2031_fi.pdf, p.32
- `rec:1` (recommendation (ours)): Team recommendation 1: Counties report access times using the THL 21/2016 definitions, with handover alerts. Each wellbeing services county reports lung cancer access times (referral → first specialist visit → diagnosis → treatment start) using the definitions in THL's Hoitoonpääsyn seuranta syövän hoidossa (Ohjaus 21/2016). Until national target times exist, flag stalled handovers. — recommendations.md, §1. Counties report access times using the THL 21/2016 definitions, with handover alerts
- `rec:2` (recommendation (ours)): Team recommendation 2: A KYS-style referral template, a persistent-symptoms rule and a named contact. Adopt a standard referral content list and template, modelled on KYS. • Add a rule for primary care: if symptoms persist after a normal X-ray, refer for a pulmonologist assessment. • Name a contact person for the diagnostic phase, from referral to diagnosis. — recommendations.md, §2. A KYS-style referral template, a persistent-symptoms rule and a named contact
- `rec:3` (recommendation (ours)): Team recommendation 3: Report recording completeness per county: stage, drug treatment, MDT coding. Publish, per county, how completely stage, drug treatment and MDT meetings are recorded. Read county ‘gaps’ in these fields as data-quality signals first. — recommendations.md, §3. Report recording completeness per county: stage, drug treatment, MDT coding
- `reg:ks_referral` (verified by Hellu): Keski-Suomi: referral handled as quickly as possible (no time stated) — pathway_brief.md, 6. Regional pathways compared
- `reg:ks_target` (verified by Hellu): Keski-Suomi: lung clinic appointment within 2–3 weeks, at the latest about 1 month — pathway_brief.md, 6. Regional pathways compared
- `reg:ks_tissue` (verified by Hellu): Keski-Suomi: tissue sample results in about 1–2 weeks — pathway_brief.md, 6. Regional pathways compared
- `reg:mdt_practice` (verified by Hellu): MDT practice differs: KYS every patient weekly, Keski-Suomi every new case, HUS when needed — pathway_brief.md, 6. Regional pathways compared
- `reg:not_monitored` (verified by Hellu): No region says whether it meets its stated times — pathway_brief.md, 6. Regional pathways compared
- `reg:occupational` (verified by Hellu): OYS and Keski-Suomi name occupational health as a referral source — pathway_brief.md, 6. Regional pathways compared
- `thl:21_2016` (verified by Hellu): THL Ohjaus 21/2016 defines how cancer access times are recorded, for 16 cancers — pathway_brief.md, 6. Regional pathways compared
