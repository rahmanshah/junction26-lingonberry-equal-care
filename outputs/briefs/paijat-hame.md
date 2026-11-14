# Päijät-Häme: lung cancer pathway brief

Status: **validated** · gemini-4-argon (thinking HIGH) · 2026-11-14T13:38:12+00:00 · attempts: 1

## Where do we lag?

**Päijät-Häme's crude recorded MDT meeting share of 0.3% (95% CI 0.1–1.1; n=2/659) lags the national 6.0% (893/14873), though this reflects recording practice rather than care.** `cty:mdt_recorded:Päijät_Hämeen_hyvinvointialue, nat:mdt_recorded, bs:coverage:MDT`

- In Päijät-Häme, the crude curative treatment share is 29.6% (95% CI 26.2–33.2; n=195/659) compared with 27.0% (4009/14873) nationally, so the 95% confidence interval includes the national value and is not distinguishable from it. `cty:curative:Päijät_Hämeen_hyvinvointialue, nat:curative`
- Across overlapping treatment categories where a patient can have several treatments within 12 months, Päijät-Häme's crude shares exceed national values, with 95% confidence intervals excluding the national benchmark for life-prolonging treatment at 44.5% (95% CI 40.7–48.3; n=293/659) versus 30.4% (4522/14873) and symptomatic treatment at 50.8% (95% CI 47.0–54.6; n=335/659) versus 39.5% (5871/14873). `cty:life_prolonging:Päijät_Hämeen_hyvinvointialue, nat:life_prolonging, cty:symptomatic:Päijät_Hämeen_hyvinvointialue, nat:symptomatic, bs:coverage:Treatment_start`
- For recorded multidisciplinary team (MDT) meetings, Päijät-Häme's crude share is 0.3% (95% CI 0.1–1.1; n=2/659) and its 95% confidence interval excludes the national value of 6.0% (893/14873), but HILMO captures specialist procedures only from direct patient contacts, so MDT records measure recording practice rather than care. `cty:mdt_recorded:Päijät_Hämeen_hyvinvointialue, nat:mdt_recorded, bs:coverage:MDT, q:39e6ba43a9`
- While public county data do not report when treatment starts, preliminary national figures show lung cancer care in Finland averages 155 days from first symptoms to first treatment versus 107 days in Sweden and 67 days in Denmark, comprising 56 days of patient delay, 41 days in primary care, and 58 days in specialist care. `bs:coverage:Treatment_start, mot:total_fi, mot:total_se, mot:total_dk, mot:patient, mot:primary, mot:specialist`

## How sure are we?

**Päijät-Häme's crude 17.8% (95% CI 15.0–20.9) share with no treatment record within 12 months is below the national 27.5%, while crude shares lack age and stage adjustment.** `cty:no_treatment_record:Päijät_Hämeen_hyvinvointialue, nat:no_treatment_record, fig:age_adjusted_only_kuva16, bs:coverage:Diagnosis`

- The category 'no treatment record within 12 months' mixes untreated patients and unrecorded treatment; because Päijät-Häme's crude share of 17.8% (95% CI 15.0–20.9; n=117/659) has a 95% confidence interval entirely below the national 27.5% (4089/14873), this is consistent, as an inference rather than a finding, with relatively complete treatment recording. `cty:no_treatment_record:Päijät_Hämeen_hyvinvointialue, nat:no_treatment_record, bs:coverage:Treatment_start`
- Taulukko 11 county shares are crude with separate limitations: they are not age-adjusted, since county age-adjusted shares appear only in Kuva 16 (with digitised national curative lines, precision ±0.5 percentage points, at 26.7% for men and 26.9% for women), and separately they cannot be stage-adjusted because stage at diagnosis is missing for about 48% of patients. `fig:age_adjusted_only_kuva16, k16:curative:men:national, k16:curative:women:national, bs:coverage:Diagnosis, q:7885b0974f`
- A journal article found that hospital discharge register (HILMO) diagnoses match the Cancer Registry for about 90% of most cancer types, but this concerns diagnosis concordance only and says nothing about how completely treatment, referral, or MDT is recorded, while national lung cancer data reporting, collection, and storage remain incomplete. `lit:hilmo_90, q:950a2f797b`
- Public data do not measure symptom onset, referral dates, or county timing for the first specialist visit (recorded within 12 months for 93.6% nationally) or treatment start; primary care visits are not included in the report's data, occupational health is not mentioned, and imaging appears only indirectly as clinical-only diagnosis in about 20% of patients. `bs:coverage:Symptoms, bs:coverage:Primary_care_occupational_health, q:323de0d90d, bs:coverage:Imaging, q:5eb155decc, bs:coverage:Referral, bs:coverage:First_specialist_visit, bs:coverage:Treatment_start`

## What should we do first?

**The team recommends auditing recording completeness for stage, drug treatment, and MDT coding, tracking access times under THL Ohjaus 21/2016 definitions, and standardising referrals and diagnostic coordination.** `rec:1, rec:2, rec:3, thl:21_2016, q:950a2f797b, q:ccda20dce9`

- Given Päijät-Häme's crude 0.3% (95% CI 0.1–1.1; n=2/659) recorded MDT share versus 6.0% (893/14873) nationally and about 48% missing stage at diagnosis nationally, the team recommends publishing county recording completeness for stage, drug treatment, and MDT meetings while reading gaps as data-quality signals, since Finland lacks a cancer quality registry and uniform recording instructions are needed. `rec:3, cty:mdt_recorded:Päijät_Hämeen_hyvinvointialue, nat:mdt_recorded, bs:coverage:Diagnosis, q:7885b0974f, bs:coverage:MDT, q:47c7e11303, q:950a2f797b, q:82d365cd2c`
- Because the Health Care Act sets no legal maximum time for a cancer suspicion and national pathway monitoring is lacking, the team recommends reporting referral-to-treatment access times using THL Ohjaus 21/2016 definitions (covering 16 cancers) with handover alerts; the Filha programme's diagnostics recommendation with recommended time limits is to be carried out before the 2030 mid-term evaluation. `rec:1, law:no_max, thl:21_2016, q:ccda20dce9, q:20d6ca414e, q:432c0e51d6, q:614febebf2`
- Since referrals follow local instructions and mentor insight notes a weak referral gets a lower urgency rating, the team recommends a referral template and persistent-symptoms rule after a normal X-ray (as in KYS's pathway document) plus a diagnostic-phase contact person; the STM roadmap (measure 1.2.3) plans care-coordinator guidance by 2026–2028 for county adoption by 2029–2031. `rec:2, q:556431a0c2, mentor:kaisa_referral, reg:kys_template, reg:kys_persistent, reg:named_contact, q:050ee09ebe, q:abcbb06ae3`

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
- `cty:curative:Päijät_Hämeen_hyvinvointialue` (verified locally): Päijät-Hämeen hyvinvointialue: curative treatment 29.6% (95% CI 26.2–33.2; n=195/659), not distinguishable vs national 27.0% — keuhkosyoparaportti_2019_2023.html, Taulukko 11
- `cty:life_prolonging:Päijät_Hämeen_hyvinvointialue` (verified locally): Päijät-Hämeen hyvinvointialue: life-prolonging treatment 44.5% (95% CI 40.7–48.3; n=293/659), above vs national 30.4% — keuhkosyoparaportti_2019_2023.html, Taulukko 11
- `cty:mdt_recorded:Päijät_Hämeen_hyvinvointialue` (verified locally): Päijät-Hämeen hyvinvointialue: MDT meeting recorded 0.3% (95% CI 0.1–1.1; n=2/659), below vs national 6.0% — keuhkosyoparaportti_2019_2023.html, Taulukko 11
- `cty:no_treatment_record:Päijät_Hämeen_hyvinvointialue` (verified locally): Päijät-Hämeen hyvinvointialue: no treatment record within 12 months 17.8% (95% CI 15.0–20.9; n=117/659), below vs national 27.5% — keuhkosyoparaportti_2019_2023.html, Taulukko 11
- `cty:symptomatic:Päijät_Hämeen_hyvinvointialue` (verified locally): Päijät-Hämeen hyvinvointialue: symptomatic treatment 50.8% (95% CI 47.0–54.6; n=335/659), above vs national 39.5% — keuhkosyoparaportti_2019_2023.html, Taulukko 11
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
- `q:abcbb06ae3` (verified locally): 2026–2028: guidance on a named doctor, nurse or specialist worker coordinating cancer care. 2029–2031: wellbeing services counties have adopted it. — roadmap_2026_2031_fi.pdf, p.32
- `q:ccda20dce9` (verified locally): Finland has no national system steering cancer pathways or their monitoring, “mukaan lukien hoitoonpääsy” — strategy_2026_2035_fi.pdf, p.33
- `rec:1` (recommendation (ours)): Team recommendation 1: Counties report access times using the THL 21/2016 definitions, with handover alerts. Each wellbeing services county reports lung cancer access times (referral → first specialist visit → diagnosis → treatment start) using the definitions in THL's Hoitoonpääsyn seuranta syövän hoidossa (Ohjaus 21/2016). Until national target times exist, flag stalled handovers. — recommendations.md, §1. Counties report access times using the THL 21/2016 definitions, with handover alerts
- `rec:2` (recommendation (ours)): Team recommendation 2: A KYS-style referral template, a persistent-symptoms rule and a named contact. Adopt a standard referral content list and template, modelled on KYS. • Add a rule for primary care: if symptoms persist after a normal X-ray, refer for a pulmonologist assessment. • Name a contact person for the diagnostic phase, from referral to diagnosis. — recommendations.md, §2. A KYS-style referral template, a persistent-symptoms rule and a named contact
- `rec:3` (recommendation (ours)): Team recommendation 3: Report recording completeness per county: stage, drug treatment, MDT coding. Publish, per county, how completely stage, drug treatment and MDT meetings are recorded. Read county ‘gaps’ in these fields as data-quality signals first. — recommendations.md, §3. Report recording completeness per county: stage, drug treatment, MDT coding
- `reg:kys_persistent` (verified by Hellu): KYS: refer persistent unexplained symptoms even if the X-ray is clear — pathway_brief.md, 6. Regional pathways compared
- `reg:kys_template` (verified by Hellu): Only KYS lists required referral content and provides a referral template — pathway_brief.md, 6. Regional pathways compared
- `reg:named_contact` (verified by Hellu): No region names a contact person for the diagnostic phase — pathway_brief.md, 6. Regional pathways compared
- `thl:21_2016` (verified by Hellu): THL Ohjaus 21/2016 defines how cancer access times are recorded, for 16 cancers — pathway_brief.md, 6. Regional pathways compared
