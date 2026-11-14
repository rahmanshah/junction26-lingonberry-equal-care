# Länsi-Uusimaa: lung cancer pathway brief

Status: **validated** · gemini-4-argon (thinking HIGH) · 2026-11-14T13:36:48+00:00 · attempts: 2

## Where do we lag?

**Länsi-Uusimaa falls below national benchmarks in crude life-prolonging treatment (25.2% vs 30.4%) and crude recorded MDT meetings (0.2% vs 6.0%) across overlapping categories.** `cty:life_prolonging:Länsi_Uudenmaan_hyvinvointialue, nat:life_prolonging, cty:mdt_recorded:Länsi_Uudenmaan_hyvinvointialue, nat:mdt_recorded`

- In Länsi-Uusimaa, the crude life-prolonging treatment share is 25.2% (95% CI 22.7–27.9; n=267/1058), with a 95% confidence interval that excludes and lies below the national 30.4% (4522/14873), while across overlapping treatment categories (where a patient can have several) the crude curative share of 31.9% (95% CI 29.1–34.7; n=337/1058) excludes and exceeds the national 27.0% (4009/14873). `cty:life_prolonging:Länsi_Uudenmaan_hyvinvointialue, nat:life_prolonging, cty:curative:Länsi_Uudenmaan_hyvinvointialue, nat:curative`
- Across these overlapping treatment categories (a patient can have several), the crude symptomatic treatment share is 40.1% (95% CI 37.2–43.1; n=424/1058), whose 95% confidence interval includes the national 39.5% (5871/14873), and the crude share with no treatment record within 12 months is 28.5% (95% CI 25.9–31.3; n=302/1058), whose 95% confidence interval includes the national 27.5% (4089/14873). `cty:symptomatic:Länsi_Uudenmaan_hyvinvointialue, nat:symptomatic, cty:no_treatment_record:Länsi_Uudenmaan_hyvinvointialue, nat:no_treatment_record`
- An MDT meeting is recorded for a crude share of 0.2% (95% CI 0.1–0.7; n=2/1058) of patients, whose 95% confidence interval excludes and lies below the national 6.0% (893/14873), though MDT records measure recording practice rather than care because HILMO captures specialist procedures only from direct patient contacts. `cty:mdt_recorded:Länsi_Uudenmaan_hyvinvointialue, nat:mdt_recorded, bs:coverage:MDT, q:39e6ba43a9`
- Public registry data do not report county waiting times, but preliminary, unpublished national figures show lung cancer takes 155 days on average from symptoms to first treatment in Finland (versus 107 days in Sweden and 67 days in Denmark), comprising 56 days of patient delay, 41 days in primary care, and 58 days in specialist care, the longest stage. `bs:coverage:Referral, bs:coverage:First_specialist_visit, bs:coverage:Treatment_start, mot:total_fi, mot:total_se, mot:total_dk, mot:patient, mot:primary, mot:specialist`

## How sure are we?

**Public registry data show diagnosis patterns, but crude county treatment shares lack age and stage adjustment, and public data omit primary care, referral, and treatment timestamps.** `fig:age_adjusted_only_kuva16, bs:coverage:Diagnosis, bs:coverage:Primary_care_occupational_health, bs:coverage:Referral, bs:coverage:Treatment_start`

- Taulukko 11 gives crude county shares that are not age-adjusted (county age-adjusted shares appear only in Kuva 16, with digitised national curative lines of 26.7% for men and 26.9% for women, ±0.5 percentage points, and no digitised Länsi-Uusimaa value); as a separate limitation, shares cannot be stage-adjusted because stage at diagnosis is missing for about 48% of patients. `fig:age_adjusted_only_kuva16, k16:curative:men:national, k16:curative:women:national, bs:coverage:Diagnosis, q:7885b0974f`
- A journal article found HILMO diagnoses match the Cancer Registry for about 90% of most cancer types (diagnosis concordance only), while the crude 28.5% (95% CI 25.9–31.3; n=302/1058) with no treatment record within 12 months (95% CI includes the national 27.5%, 4089/14873) mixes untreated patients and treatment that was not recorded, and Finland has no cancer quality registry. `lit:hilmo_90, cty:no_treatment_record:Länsi_Uudenmaan_hyvinvointialue, nat:no_treatment_record, bs:coverage:Treatment_start, filha:registry, q:47c7e11303`
- Public report data do not measure symptom onset or referrals, primary care visits are not included in the report's data, occupational health is not mentioned at all, and imaging appears only indirectly because diagnosis relies on clinical examination alone, such as imaging, in approximately 20% of patients. `bs:coverage:Symptoms, bs:coverage:Referral, bs:coverage:Primary_care_occupational_health, q:323de0d90d, bs:coverage:Imaging, q:5eb155decc`
- For specialist care, public data show whether a lung cancer specialist visit appears in HILMO within 12 months (93.6% nationally) and which treatment type is recorded within 12 months, but cannot show when the first specialist visit or treatment started, and no reviewed regional pathway document reports whether stated target times are met. `bs:coverage:First_specialist_visit, bs:coverage:Treatment_start, reg:not_monitored`

## What should we do first?

**The team recommends auditing stage, drug treatment, and MDT coding, reporting access times using THL 21/2016 definitions with handover alerts, and standardising referrals and diagnostic-phase contacts.** `rec:1, rec:2, rec:3, thl:21_2016, bs:coverage:Diagnosis, bs:coverage:MDT`

- Because Länsi-Uusimaa's crude recorded MDT share is 0.2% (95% CI 0.1–0.7; n=2/1058) versus 6.0% (893/14873) nationally and crude life-prolonging share is 25.2% (95% CI 22.7–27.9; n=267/1058) versus 30.4% (4522/14873) across overlapping categories, with stage missing for about 48% nationally, the team recommends publishing per-county stage, drug, and MDT recording coverage as data-quality signals first. `rec:3, cty:mdt_recorded:Länsi_Uudenmaan_hyvinvointialue, nat:mdt_recorded, cty:life_prolonging:Länsi_Uudenmaan_hyvinvointialue, nat:life_prolonging, bs:coverage:Diagnosis, q:7885b0974f, bs:coverage:MDT, q:950a2f797b, q:82d365cd2c`
- Since Health Care Act §52 sets no legal maximum time for a cancer suspicion and preliminary national intervals average 41 days in primary care and 58 days in specialist care, the team recommends reporting access times (referral to first specialist visit, diagnosis, and treatment start) using THL Ohjaus 21/2016 guidance definitions for 16 cancers and flagging stalled handovers. `rec:1, law:no_max, mot:primary, mot:specialist, thl:21_2016, q:24169121a4, q:ccda20dce9`
- Because a mentor insight notes weak referrals receive lower urgency ratings, and in reviewed regional pathway documents only KYS provides a referral template and a rule to refer persistent symptoms despite a clear X-ray while no reviewed document names a diagnostic contact, the team recommends adopting a KYS-style template, a persistent-symptoms rule, and a named diagnostic contact. `rec:2, mentor:kaisa_referral, reg:kys_template, reg:kys_persistent, reg:only_kys_xray, reg:named_contact, q:556431a0c2`
- The team recommends acting while national plans proceed: STM roadmap measure 1.2.3 plans care-coordinator guidance by 2026–2028 (county adoption by 2029–2031) and measure 3.2.1 plans updating the quality registry decree by 2026–2028, while the Filha programme's diagnostics recommendation with primary-care referral criteria and time limits is to be carried out before the 2030 mid-term evaluation. `rec:1, rec:2, rec:3, q:fc81032a80, q:abcbb06ae3, q:f07a34a300, q:8f358a9de6, q:614febebf2`

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
- `cty:curative:Länsi_Uudenmaan_hyvinvointialue` (verified locally): Länsi-Uudenmaan hyvinvointialue: curative treatment 31.9% (95% CI 29.1–34.7; n=337/1058), above vs national 27.0% — keuhkosyoparaportti_2019_2023.html, Taulukko 11
- `cty:life_prolonging:Länsi_Uudenmaan_hyvinvointialue` (verified locally): Länsi-Uudenmaan hyvinvointialue: life-prolonging treatment 25.2% (95% CI 22.7–27.9; n=267/1058), below vs national 30.4% — keuhkosyoparaportti_2019_2023.html, Taulukko 11
- `cty:mdt_recorded:Länsi_Uudenmaan_hyvinvointialue` (verified locally): Länsi-Uudenmaan hyvinvointialue: MDT meeting recorded 0.2% (95% CI 0.1–0.7; n=2/1058), below vs national 6.0% — keuhkosyoparaportti_2019_2023.html, Taulukko 11
- `cty:no_treatment_record:Länsi_Uudenmaan_hyvinvointialue` (verified locally): Länsi-Uudenmaan hyvinvointialue: no treatment record within 12 months 28.5% (95% CI 25.9–31.3; n=302/1058), not distinguishable vs national 27.5% — keuhkosyoparaportti_2019_2023.html, Taulukko 11
- `cty:symptomatic:Länsi_Uudenmaan_hyvinvointialue` (verified locally): Länsi-Uudenmaan hyvinvointialue: symptomatic treatment 40.1% (95% CI 37.2–43.1; n=424/1058), not distinguishable vs national 39.5% — keuhkosyoparaportti_2019_2023.html, Taulukko 11
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
- `q:24169121a4` (verified locally): Strategy p.5 (= PDF p.5), “Strategiset tavoitteet”, indicator under “Varmistetaan yhdenvertainen ja vaikuttava syövänhoito”: > “Potilaat pääsevät hoitoon tavoiteaikojen puitteissa” > “ THL (Ohjaus 21/2016). Hoitoonpääsyn seuranta syövän hoidossa.” — strategy_2026_2035_fi.pdf, p.5
- `q:323de0d90d` (verified locally): Report evidence for pathway stage 'Primary care / occupational health' — keuhkosyoparaportti_2019_2023.html, §3.3 Menetelmät
- `q:39e6ba43a9` (verified locally): Report evidence for pathway stage 'MDT' — keuhkosyoparaportti_2019_2023.html, §3.3 Menetelmät
- `q:47c7e11303` (verified locally): Finland has no quality registry for lung cancer or for any other cancer. — filha_lung_programme_2026_fi.pdf, p.21
- `q:556431a0c2` (verified locally): the patient is referred to specialist care according to local instructions — filha_lung_programme_2026_fi.pdf, p.15
- `q:5eb155decc` (verified locally): Report evidence for pathway stage 'Imaging' — keuhkosyoparaportti_2019_2023.html, §4.1.1 Toteamistapa
- `q:614febebf2` (verified locally): When (p.24): > “Väliarvio toteutetaan vuonna 2030, ohjelman puolivälissä ja loppuarviointi vuonna 2036. Eri > osa-alueiden suositukset toteutetaan ennen väliarviointia.” — filha_lung_programme_2026_fi.pdf, p.24
- `q:7885b0974f` (verified locally): Report evidence for pathway stage 'Diagnosis' — keuhkosyoparaportti_2019_2023.html, §4.1.3 Levinneisyystiedon kattavuus
- `q:82d365cd2c` (verified locally): “Tällä hetkellä keuhkosyöpään liittyvien tietojen raportointi, kerääminen ja tallentaminen on puutteellista”; nationally uniform recording instructions (“yhtenäiset kirjaamisohjeet”) must be ensured — filha_lung_programme_2026_fi.pdf, p.21
- `q:8f358a9de6` (verified locally): p.16: > “Tämän ohjelman yhtenä toimenpiteenä tuotetaan kansallinen suositus keuhkosyöpien diagnostiikasta. Se > sisältää myös lähetekriteerit perusterveydenhuollolle ja suositellut aikarajat erikoissairaanhoitoon > eri diagnostiikan polun vaiheille.” — filha_lung_programme_2026_fi.pdf, p.16
- `q:950a2f797b` (verified locally): Reporting, collection and storage of lung cancer data is currently incomplete. — filha_lung_programme_2026_fi.pdf, p.21
- `q:abcbb06ae3` (verified locally): 2026–2028: guidance on a named doctor, nurse or specialist worker coordinating cancer care. 2029–2031: wellbeing services counties have adopted it. — roadmap_2026_2031_fi.pdf, p.32
- `q:ccda20dce9` (verified locally): Finland has no national system steering cancer pathways or their monitoring, “mukaan lukien hoitoonpääsy” — strategy_2026_2035_fi.pdf, p.33
- `q:f07a34a300` (verified locally): A national cancer care quality registry will be set up alongside THL's Cancer Registry. — roadmap_2026_2031_fi.pdf, p.59
- `q:fc81032a80` (verified locally): Measure 1.2.3: Create an operating model and guidance for a named worker responsible for coordinating cancer care. — roadmap_2026_2031_fi.pdf, p.32
- `rec:1` (recommendation (ours)): Team recommendation 1: Counties report access times using the THL 21/2016 definitions, with handover alerts. Each wellbeing services county reports lung cancer access times (referral → first specialist visit → diagnosis → treatment start) using the definitions in THL's Hoitoonpääsyn seuranta syövän hoidossa (Ohjaus 21/2016). Until national target times exist, flag stalled handovers. — recommendations.md, §1. Counties report access times using the THL 21/2016 definitions, with handover alerts
- `rec:2` (recommendation (ours)): Team recommendation 2: A KYS-style referral template, a persistent-symptoms rule and a named contact. Adopt a standard referral content list and template, modelled on KYS. • Add a rule for primary care: if symptoms persist after a normal X-ray, refer for a pulmonologist assessment. • Name a contact person for the diagnostic phase, from referral to diagnosis. — recommendations.md, §2. A KYS-style referral template, a persistent-symptoms rule and a named contact
- `rec:3` (recommendation (ours)): Team recommendation 3: Report recording completeness per county: stage, drug treatment, MDT coding. Publish, per county, how completely stage, drug treatment and MDT meetings are recorded. Read county ‘gaps’ in these fields as data-quality signals first. — recommendations.md, §3. Report recording completeness per county: stage, drug treatment, MDT coding
- `reg:kys_persistent` (verified by Hellu): KYS: refer persistent unexplained symptoms even if the X-ray is clear — pathway_brief.md, 6. Regional pathways compared
- `reg:kys_template` (verified by Hellu): Only KYS lists required referral content and provides a referral template — pathway_brief.md, 6. Regional pathways compared
- `reg:named_contact` (verified by Hellu): No region names a contact person for the diagnostic phase — pathway_brief.md, 6. Regional pathways compared
- `reg:not_monitored` (verified by Hellu): No region says whether it meets its stated times — pathway_brief.md, 6. Regional pathways compared
- `reg:only_kys_xray` (verified by Hellu): Only KYS tells primary care what to do with a normal X-ray and continuing symptoms — pathway_brief.md, 6. Regional pathways compared
- `thl:21_2016` (verified by Hellu): THL Ohjaus 21/2016 defines how cancer access times are recorded, for 16 cancers — pathway_brief.md, 6. Regional pathways compared
