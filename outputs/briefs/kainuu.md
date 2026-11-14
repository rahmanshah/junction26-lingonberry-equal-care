# Kainuu: lung cancer pathway brief

Status: **validated** · gemini-4-argon (thinking HIGH) · 2026-11-14T12:15:03+00:00 · attempts: 1

## Where do we lag?

**In Kainuun hyvinvointialue, crude shares for curative and life-prolonging treatment and recorded multidisciplinary team meetings lag national benchmarks, while crude symptomatic treatment is higher.** `cty:curative:Kainuun_hyvinvointialue, cty:life_prolonging:Kainuun_hyvinvointialue, cty:symptomatic:Kainuun_hyvinvointialue, cty:mdt_recorded:Kainuun_hyvinvointialue`

- Among new lung cancer patients in 2019–2023, the county's crude curative treatment share is 20.8% (95% CI 16.0–26.6; n=47/226) versus 27.0% (4009/14873) nationally, and the crude life-prolonging treatment share is 18.6% (95% CI 14.1–24.2; n=42/226) versus 30.4% (4522/14873) nationally, with 95% confidence intervals excluding national values. `cty:curative:Kainuun_hyvinvointialue, nat:curative, cty:life_prolonging:Kainuun_hyvinvointialue, nat:life_prolonging`
- Conversely, the crude symptomatic treatment share is 48.2% (95% CI 41.8–54.7; n=109/226) compared with 39.5% (5871/14873) nationally, where the 95% confidence interval excludes the national value across these overlapping treatment categories. `cty:symptomatic:Kainuun_hyvinvointialue, nat:symptomatic, bs:coverage:Treatment_start`
- A multidisciplinary team meeting is recorded for a crude 0.9% (95% CI 0.2–3.2; n=2/226) of county patients versus 6.0% (893/14873) nationally—an interval excluding the national value that reflects recording practice rather than care—while the crude share with no treatment record within 12 months is 28.3% (95% CI 22.9–34.5; n=64/226), whose interval includes 27.5% (4089/14873) nationally. `cty:mdt_recorded:Kainuun_hyvinvointialue, nat:mdt_recorded, bs:coverage:MDT, q:39e6ba43a9, cty:no_treatment_record:Kainuun_hyvinvointialue, nat:no_treatment_record`

## How sure are we?

**County treatment gaps are statistically distinct in crude registry data, but public data omit key pathway stages and adjustment for age or stage.** `cty:curative:Kainuun_hyvinvointialue, cty:life_prolonging:Kainuun_hyvinvointialue, bs:coverage:Diagnosis, bs:coverage:Referral`

- Reading the crude 28.3% (95% CI 22.9–34.5; n=64/226) share with no treatment record within 12 months—mixing untreated patients and unrecorded treatment—as a data-quality signal, we infer that because its 95% confidence interval includes the 27.5% (4089/14873) national value, lower crude curative shares are unlikely to be only a recording artefact, though unrecorded treatment may partly contribute. `cty:no_treatment_record:Kainuun_hyvinvointialue, nat:no_treatment_record, bs:coverage:Treatment_start, cty:curative:Kainuun_hyvinvointialue`
- County shares are crude (unadjusted for age or stage): stage at diagnosis is often missing nationally, a journal article finds about 90% hospital discharge diagnosis concordance with the Cancer Registry, and digitised Kuva 16 age-adjusted curative figures (about ±0.5 percentage points) provide only national reference lines of 26.7% for men and 26.9% for women. `bs:coverage:Diagnosis, q:7885b0974f, lit:hilmo_90, k16:curative:men:national, k16:curative:women:national`
- Public registry data do not capture symptom onset, referral dates, imaging waits, or exact specialist visit and treatment start dates, while outpatient primary care visits are not included in the report's data and occupational health is unmentioned. `bs:coverage:Symptoms, bs:coverage:Primary_care_occupational_health, q:323de0d90d, bs:coverage:Imaging, bs:coverage:Referral, bs:coverage:First_specialist_visit, bs:coverage:Treatment_start`
- Preliminary, unpublished figures from an MOT study indicate that lung cancer care in Finland takes 155 days on average from symptoms to treatment (versus 107 in Sweden and 67 in Denmark), including 56 days of patient delay, 41 days in primary care, and 58 days in specialist care. `mot:total_fi, mot:total_se, mot:total_dk, mot:patient, mot:primary, mot:specialist`

## What should we do first?

**The team recommends tracking access times using THL Ohjaus 21/2016 guidance, standardising referrals and diagnostic coordination, and auditing stage, drug treatment, and multidisciplinary meeting recording completeness.** `rec:1, rec:2, rec:3, thl:21_2016, q:950a2f797b`

- Because the Health Care Act sets no legal maximum time for a cancer suspicion, the team recommends reporting referral-to-treatment access times using THL Ohjaus 21/2016 guidance (for 16 cancers) with handover alerts while the roadmap plans target times in 2026–2028 and the Filha diagnostics guideline is due before the 2030 interim evaluation. `rec:1, law:no_max, thl:21_2016, q:ccda20dce9, q:def306014c, q:b326e35410, q:432c0e51d6, q:614febebf2`
- Since mentor insight indicates a weak referral gets a lower specialist urgency rating and the roadmap plans standardised referral criteria and coordinator guidance in 2026–2028, the team recommends a referral template and a persistent-symptoms pulmonologist referral rule after a normal X-ray—modelled on the KYS regional pathway document—plus a diagnostic-phase contact person, which reviewed regional pathway documents lack. `rec:2, mentor:kaisa_referral, reg:kys_template, reg:kys_persistent, reg:only_kys_xray, reg:named_contact, q:c61439b30f, q:abcbb06ae3, q:050ee09ebe`
- With multidisciplinary team meetings recorded for a crude 0.9% (95% CI 0.2–3.2; n=2/226) of county patients versus 6.0% (893/14873) nationally and stage often missing nationally, the team recommends publishing county recording completeness for stage, drug treatment, and multidisciplinary coding while a national quality registry targeting 90% coverage including stage is planned. `rec:3, cty:mdt_recorded:Kainuun_hyvinvointialue, nat:mdt_recorded, bs:coverage:Diagnosis, q:7885b0974f, q:950a2f797b, q:f07a34a300, q:f540c706f8`

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
- `cty:curative:Kainuun_hyvinvointialue` (verified locally): Kainuun hyvinvointialue: curative treatment 20.8% (95% CI 16.0–26.6; n=47/226), below vs national 27.0% — keuhkosyoparaportti_2019_2023.html, Taulukko 11
- `cty:life_prolonging:Kainuun_hyvinvointialue` (verified locally): Kainuun hyvinvointialue: life-prolonging treatment 18.6% (95% CI 14.1–24.2; n=42/226), below vs national 30.4% — keuhkosyoparaportti_2019_2023.html, Taulukko 11
- `cty:mdt_recorded:Kainuun_hyvinvointialue` (verified locally): Kainuun hyvinvointialue: MDT meeting recorded 0.9% (95% CI 0.2–3.2; n=2/226), below vs national 6.0% — keuhkosyoparaportti_2019_2023.html, Taulukko 11
- `cty:no_treatment_record:Kainuun_hyvinvointialue` (verified locally): Kainuun hyvinvointialue: no treatment record within 12 months 28.3% (95% CI 22.9–34.5; n=64/226), not distinguishable vs national 27.5% — keuhkosyoparaportti_2019_2023.html, Taulukko 11
- `cty:symptomatic:Kainuun_hyvinvointialue` (verified locally): Kainuun hyvinvointialue: symptomatic treatment 48.2% (95% CI 41.8–54.7; n=109/226), above vs national 39.5% — keuhkosyoparaportti_2019_2023.html, Taulukko 11
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
- `q:432c0e51d6` (verified locally): The upcoming national diagnostics recommendation will include “suositellut aikarajat erikoissairaanhoitoon eri diagnostiikan polun vaiheille” (recommended time limits in specialist care), due before the 2030 mid-term evaluation — filha_lung_programme_2026_fi.pdf, p.16
- `q:614febebf2` (verified locally): When (p.24): > “Väliarvio toteutetaan vuonna 2030, ohjelman puolivälissä ja loppuarviointi vuonna 2036. Eri > osa-alueiden suositukset toteutetaan ennen väliarviointia.” — filha_lung_programme_2026_fi.pdf, p.24
- `q:7885b0974f` (verified locally): Report evidence for pathway stage 'Diagnosis' — keuhkosyoparaportti_2019_2023.html, §4.1.3 Levinneisyystiedon kattavuus
- `q:950a2f797b` (verified locally): Reporting, collection and storage of lung cancer data is currently incomplete. — filha_lung_programme_2026_fi.pdf, p.21
- `q:abcbb06ae3` (verified locally): 2026–2028: guidance on a named doctor, nurse or specialist worker coordinating cancer care. 2029–2031: wellbeing services counties have adopted it. — roadmap_2026_2031_fi.pdf, p.32
- `q:b326e35410` (verified locally): National pathways with “syöpäkohtaiset hoitoonpääsyajat” for five (unnamed) cancers in 2026–2028, Nordic model — roadmap_2026_2031_fi.pdf, p.57
- `q:c61439b30f` (verified locally): 2026–2028: standardised referral criteria and symptom-based models included in the national pathways of at least the five most common cancers. — roadmap_2026_2031_fi.pdf, p.53
- `q:ccda20dce9` (verified locally): Finland has no national system steering cancer pathways or their monitoring, “mukaan lukien hoitoonpääsy” — strategy_2026_2035_fi.pdf, p.33
- `q:def306014c` (verified locally): p.57, timetable: > “2026–2028: Kansalliset hoitoketjukuvaukset tehty viidestä syövästä ja syöpäkohtaiset > hoitoonpääsyajat on määritetty.” — roadmap_2026_2031_fi.pdf, p.57
- `q:f07a34a300` (verified locally): A national cancer care quality registry will be set up alongside THL's Cancer Registry. — roadmap_2026_2031_fi.pdf, p.59
- `q:f540c706f8` (verified locally): A national quality registry is planned; indicator: data incl. stage (“ml. levinneisyystieto”) at 90% coverage — roadmap_2026_2031_fi.pdf, p.60
- `rec:1` (recommendation (ours)): Team recommendation 1: Counties report access times using the THL 21/2016 definitions, with handover alerts. Each wellbeing services county reports lung cancer access times (referral → first specialist visit → diagnosis → treatment start) using the definitions in THL's Hoitoonpääsyn seuranta syövän hoidossa (Ohjaus 21/2016). Until national target times exist, flag stalled handovers. — recommendations.md, §1. Counties report access times using the THL 21/2016 definitions, with handover alerts
- `rec:2` (recommendation (ours)): Team recommendation 2: A KYS-style referral template, a persistent-symptoms rule and a named contact. Adopt a standard referral content list and template, modelled on KYS. • Add a rule for primary care: if symptoms persist after a normal X-ray, refer for a pulmonologist assessment. • Name a contact person for the diagnostic phase, from referral to diagnosis. — recommendations.md, §2. A KYS-style referral template, a persistent-symptoms rule and a named contact
- `rec:3` (recommendation (ours)): Team recommendation 3: Report recording completeness per county: stage, drug treatment, MDT coding. Publish, per county, how completely stage, drug treatment and MDT meetings are recorded. Read county ‘gaps’ in these fields as data-quality signals first. — recommendations.md, §3. Report recording completeness per county: stage, drug treatment, MDT coding
- `reg:kys_persistent` (verified by Hellu): KYS: refer persistent unexplained symptoms even if the X-ray is clear — pathway_brief.md, 6. Regional pathways compared
- `reg:kys_template` (verified by Hellu): Only KYS lists required referral content and provides a referral template — pathway_brief.md, 6. Regional pathways compared
- `reg:named_contact` (verified by Hellu): No region names a contact person for the diagnostic phase — pathway_brief.md, 6. Regional pathways compared
- `reg:only_kys_xray` (verified by Hellu): Only KYS tells primary care what to do with a normal X-ray and continuing symptoms — pathway_brief.md, 6. Regional pathways compared
- `thl:21_2016` (verified by Hellu): THL Ohjaus 21/2016 defines how cancer access times are recorded, for 16 cancers — pathway_brief.md, 6. Regional pathways compared
