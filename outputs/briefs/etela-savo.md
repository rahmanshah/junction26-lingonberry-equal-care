# Etelä-Savo: lung cancer pathway brief

Status: **validated** · gemini-4-argon (thinking HIGH) · 2026-11-14T13:40:39+00:00 · attempts: 2

## Where do we lag?

**Where treatment categories overlap, Etelä-Savo lags in crude recorded multidisciplinary meetings (0.2% vs 6.0% nationally), while crude curative treatment (23.4%) is not distinguishable from 27.0% nationally.** `cty:mdt_recorded:Etelä_Savon_hyvinvointialue, nat:mdt_recorded, cty:curative:Etelä_Savon_hyvinvointialue, nat:curative`

- In overlapping treatment categories where a patient can have several treatments, Etelä-Savo's crude curative treatment share is 23.4% (95% CI 19.8–27.6; n=105/448) versus 27.0% (4009/14873) nationally, with the 95% confidence interval including the national value. `cty:curative:Etelä_Savon_hyvinvointialue, nat:curative, bs:coverage:Treatment_start`
- Because treatment categories overlap and a patient can receive several types, Etelä-Savo's crude shares are above national benchmarks for life-prolonging treatment at 36.4% (95% CI 32.1–40.9; n=163/448) versus 30.4% (4522/14873) and symptomatic treatment at 46.2% (95% CI 41.6–50.8; n=207/448) versus 39.5% (5871/14873), with 95% confidence intervals excluding the national values. `cty:life_prolonging:Etelä_Savon_hyvinvointialue, nat:life_prolonging, cty:symptomatic:Etelä_Savon_hyvinvointialue, nat:symptomatic`
- Etelä-Savo's crude share of patients with a recorded multidisciplinary team meeting is 0.2% (95% CI 0.0–1.2; n=1/448) compared with 6.0% (893/14873) nationally, with the 95% confidence interval excluding the national value, though this indicator measures HILMO recording practice from direct patient contacts rather than care. `cty:mdt_recorded:Etelä_Savon_hyvinvointialue, nat:mdt_recorded, bs:coverage:MDT, q:39e6ba43a9`
- Nationally, preliminary unpublished figures show lung cancer care takes 155 days on average from initial symptoms to treatment in Finland compared with 107 days in Sweden and 67 days in Denmark, comprising 56 days of patient delay, 41 days in primary care, and 58 days in specialist care. `mot:total_fi, mot:total_se, mot:total_dk, mot:patient, mot:primary, mot:specialist`

## How sure are we?

**Etelä-Savo's crude no-treatment-record share of 23.2% is below 27.5% nationally, suggesting relatively complete treatment recording, but county shares are crude and public data miss key pathway stages.** `cty:no_treatment_record:Etelä_Savon_hyvinvointialue, nat:no_treatment_record, fig:age_adjusted_only_kuva16, bs:coverage:Referral`

- Etelä-Savo's crude share with no treatment record within 12 months—which mixes untreated patients and unrecorded treatment—is 23.2% (95% CI 19.5–27.3; n=104/448), with the 95% confidence interval entirely below 27.5% (4089/14873) nationally; as an inference, not a finding, this is consistent with relatively complete treatment recording, making a low curative share less likely to be only a recording artefact. `cty:no_treatment_record:Etelä_Savon_hyvinvointialue, nat:no_treatment_record, bs:coverage:Treatment_start`
- Taulukko 11 gives crude county shares only, which have separate limitations: they are not age-adjusted—county-level age-adjusted shares appear only in Kuva 16, where national curative reference lines digitised from the figure at ±0.5 percentage points are 26.7% for men and 26.9% for women—and independently, they cannot be stage-adjusted because stage at diagnosis is missing for about 48% of patients. `fig:age_adjusted_only_kuva16, k16:curative:men:national, k16:curative:women:national, bs:coverage:Diagnosis, q:7885b0974f`
- A journal article found HILMO diagnoses match the Cancer Registry for about 90% of most cancer types, concerning diagnosis concordance only, while public report data do not measure symptoms or referrals, do not mention occupational health, and outpatient primary care visits are not included in the report's data. `lit:hilmo_90, bs:coverage:Symptoms, bs:coverage:Referral, bs:coverage:Primary_care_occupational_health, q:323de0d90d`
- Public data measure imaging only indirectly as diagnoses based on clinical examination alone in approximately 20% of patients, and while 93.6% of patients have a recorded specialist visit within 12 months, the report does not show when specialist visits or treatments start. `bs:coverage:Imaging, q:5eb155decc, bs:coverage:First_specialist_visit, bs:coverage:Treatment_start`

## What should we do first?

**The team recommends auditing recording completeness for multidisciplinary meetings, stage and drug treatment, tracking access times using THL Ohjaus 21/2016 definitions, and standardising referrals and diagnostic-phase coordination.** `rec:1, rec:2, rec:3`

- The team recommends publishing county recording completeness for stage, drug treatment, and multidisciplinary team meetings and reading gaps as data-quality signals, since Etelä-Savo's crude recorded multidisciplinary team share is 0.2% (95% CI 0.0–1.2; n=1/448) versus 6.0% (893/14873) nationally, stage is missing for about 48% of patients, and national lung cancer data collection is currently incomplete. `rec:3, cty:mdt_recorded:Etelä_Savon_hyvinvointialue, nat:mdt_recorded, bs:coverage:Diagnosis, q:7885b0974f, q:950a2f797b, q:82d365cd2c`
- The team recommends reporting access times from referral to treatment start using THL Ohjaus 21/2016 guidance definitions—which cover 16 cancers—with handover alerts, because the Health Care Act sets no legal maximum time for a cancer suspicion and the Filha National Lung Cancer Programme's diagnostics recommendation with recommended time limits is to be carried out before the 2030 mid-term evaluation. `rec:1, thl:21_2016, law:no_max, q:432c0e51d6, q:614febebf2`
- The team recommends adopting a referral template and persistent-symptoms rule modelled on the KYS regional pathway document and naming a diagnostic-phase contact person—which regional pathway documents currently lack—as mentor insight notes weak referrals get lower urgency ratings and the STM roadmap's measure 1.2.3 plans care-coordinator guidance by 2026–2028 for county adoption by 2029–2031. `rec:2, reg:kys_template, reg:kys_persistent, reg:named_contact, mentor:kaisa_referral, q:fc81032a80, q:abcbb06ae3, q:050ee09ebe`

## Review flags (for human review only)

_Flags are for human review only; they never change the brief's status or approve it._

- [medium] `where_we_lag.details[1]`: Causal overreach: saying Etelä-Savo's crude shares are above national benchmarks 'Because treatment categories overlap and a patient can receive several types' asserts a cause not supported by the cited claims, as overlapping categories apply to both county and national figures.
- [low] `what_to_do_first.headline`: Minor overreach in verb choice: rec:3 recommends reporting and publishing recording completeness per county, not 'auditing' it.

## Claims cited

- `bs:coverage:Diagnosis` (verified locally): Pathway stage 'Diagnosis' is measured in public data: yes (by county: yes (Kuva 7, 10, 13: PNG only)) — keuhkosyoparaportti_2019_2023.html, §4.1, Taulukko 2–4, Kuva 5–13
- `bs:coverage:First_specialist_visit` (verified locally): Pathway stage 'First specialist visit' is measured in public data: partly (by county: no) — keuhkosyoparaportti_2019_2023.html, §3.1, §4.2, Taulukko 5
- `bs:coverage:Imaging` (verified locally): Pathway stage 'Imaging' is measured in public data: partly (by county: partly (Kuva 7, PNG only)) — keuhkosyoparaportti_2019_2023.html, §4.1.1, Taulukko 2, Kuva 5–7
- `bs:coverage:MDT` (verified locally): Pathway stage 'MDT' is measured in public data: partly (by county: yes (Taulukko 11)) — keuhkosyoparaportti_2019_2023.html, §3.3, §4.2, Taulukko 5, 10, 11, 13
- `bs:coverage:Primary_care_occupational_health` (verified locally): Pathway stage 'Primary care / occupational health' is measured in public data: no (by county: no) — keuhkosyoparaportti_2019_2023.html, §3.3
- `bs:coverage:Referral` (verified locally): Pathway stage 'Referral' is measured in public data: no (by county: no) — keuhkosyoparaportti_2019_2023.html, whole report (no relevant data found)
- `bs:coverage:Symptoms` (verified locally): Pathway stage 'Symptoms' is measured in public data: no (by county: no) — keuhkosyoparaportti_2019_2023.html, whole report (no relevant data found)
- `bs:coverage:Treatment_start` (verified locally): Pathway stage 'Treatment start' is measured in public data: partly (by county: yes (type only, Taulukko 11)) — keuhkosyoparaportti_2019_2023.html, §4.2, §4.2.2, Taulukko 6–9, 11, 12, Kuva 14, 17
- `cty:curative:Etelä_Savon_hyvinvointialue` (verified locally): Etelä-Savon hyvinvointialue: curative treatment 23.4% (95% CI 19.8–27.6; n=105/448), not distinguishable vs national 27.0% — keuhkosyoparaportti_2019_2023.html, Taulukko 11
- `cty:life_prolonging:Etelä_Savon_hyvinvointialue` (verified locally): Etelä-Savon hyvinvointialue: life-prolonging treatment 36.4% (95% CI 32.1–40.9; n=163/448), above vs national 30.4% — keuhkosyoparaportti_2019_2023.html, Taulukko 11
- `cty:mdt_recorded:Etelä_Savon_hyvinvointialue` (verified locally): Etelä-Savon hyvinvointialue: MDT meeting recorded 0.2% (95% CI 0.0–1.2; n=1/448), below vs national 6.0% — keuhkosyoparaportti_2019_2023.html, Taulukko 11
- `cty:no_treatment_record:Etelä_Savon_hyvinvointialue` (verified locally): Etelä-Savon hyvinvointialue: no treatment record within 12 months 23.2% (95% CI 19.5–27.3; n=104/448), below vs national 27.5% — keuhkosyoparaportti_2019_2023.html, Taulukko 11
- `cty:symptomatic:Etelä_Savon_hyvinvointialue` (verified locally): Etelä-Savon hyvinvointialue: symptomatic treatment 46.2% (95% CI 41.6–50.8; n=207/448), above vs national 39.5% — keuhkosyoparaportti_2019_2023.html, Taulukko 11
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
- `thl:21_2016` (verified by Hellu): THL Ohjaus 21/2016 defines how cancer access times are recorded, for 16 cancers — pathway_brief.md, 6. Regional pathways compared
