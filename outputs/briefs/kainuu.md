# Kainuu: lung cancer pathway brief

Status: **validated** · gemini-4-argon (thinking HIGH) · 2026-11-14T13:06:19+00:00 · attempts: 1

## Where do we lag?

**Kainuu's crude shares for overlapping treatment categories lag Finland in curative (20.8%, 95% CI 16.0–26.6 vs 27.0%) and life-prolonging care (18.6%, 95% CI 14.1–24.2 vs 30.4%).** `cty:curative:Kainuun_hyvinvointialue, nat:curative, cty:life_prolonging:Kainuun_hyvinvointialue, nat:life_prolonging`

- Because a patient can receive several treatments, these treatment categories overlap: Kainuu's crude curative share of 20.8% (95% CI 16.0–26.6; n=47/226) and crude life-prolonging share of 18.6% (95% CI 14.1–24.2; n=42/226) have 95% confidence intervals that exclude the national values of 27.0% (4009/14873) and 30.4% (4522/14873). `cty:curative:Kainuun_hyvinvointialue, nat:curative, cty:life_prolonging:Kainuun_hyvinvointialue, nat:life_prolonging, bs:coverage:Treatment_start`
- Across these overlapping categories, Kainuu's crude symptomatic treatment share is 48.2% (95% CI 41.8–54.7; n=109/226), with a 95% confidence interval that excludes the national 39.5% (5871/14873), whereas the crude share with no treatment record within 12 months is 28.3% (95% CI 22.9–34.5; n=64/226), whose 95% confidence interval includes and is not distinguishable from the national 27.5% (4089/14873). `cty:symptomatic:Kainuun_hyvinvointialue, nat:symptomatic, cty:no_treatment_record:Kainuun_hyvinvointialue, nat:no_treatment_record`
- Kainuu's crude share of patients with a recorded MDT meeting is 0.9% (95% CI 0.2–3.2; n=2/226), with a 95% confidence interval excluding the national 6.0% (893/14873), though MDT records measure recording practice rather than care because HILMO captures codes WZC15 and WZC20 only from direct patient contacts. `cty:mdt_recorded:Kainuun_hyvinvointialue, nat:mdt_recorded, bs:coverage:MDT, q:39e6ba43a9`
- Nationally, preliminary figures show lung cancer care takes 155 days on average from symptoms to treatment in Finland (56 days patient delay, 41 days in primary care, and 58 days in specialist care, the longest stage), compared with 107 days in Sweden and 67 days in Denmark, while public data lack county waiting times. `mot:total_fi, mot:patient, mot:primary, mot:specialist, mot:total_se, mot:total_dk, bs:coverage:Symptoms, bs:coverage:Referral, bs:coverage:First_specialist_visit, bs:coverage:Treatment_start`

## How sure are we?

**Kainuu's treatment shares are crude—neither age-adjusted nor stage-adjusted—and public registry data do not capture primary care, referrals, or pathway waiting times.** `cty:curative:Kainuun_hyvinvointialue, bs:coverage:Diagnosis, bs:coverage:Primary_care_occupational_health, bs:coverage:Referral, bs:coverage:Treatment_start`

- Kainuu's county shares are crude and have separate limitations: they are not age-adjusted (age-adjusted values exist only from Kuva 16 for curative treatment by sex, digitised at ±0.5 percentage points precision, with national lines of 26.7% for men and 26.9% for women), and separately they cannot be stage-adjusted because stage at diagnosis is missing for about 48% of patients. `cty:curative:Kainuun_hyvinvointialue, k16:curative:men:national, k16:curative:women:national, bs:coverage:Diagnosis, q:7885b0974f`
- A journal article reports that HILMO diagnoses match the Cancer Registry for about 90% of most cancer types, which concerns diagnosis concordance only, while the 27.5% national and 28.3% (95% CI 22.9–34.5) crude Kainuu shares with no treatment record within 12 months mix untreated patients and unrecorded treatment. `lit:hilmo_90, nat:no_treatment_record, cty:no_treatment_record:Kainuun_hyvinvointialue, bs:coverage:Treatment_start`
- Primary care visits are not included in the report's data, occupational health is not mentioned, symptom and referral dates are absent, imaging appears only indirectly as clinical-only diagnosis (about 20% of patients), and HILMO shows whether a specialist visit (93.6% nationally, up to 3 months before diagnosis) or treatment occurred within 12 months, not when. `bs:coverage:Primary_care_occupational_health, q:323de0d90d, bs:coverage:Symptoms, bs:coverage:Referral, bs:coverage:Imaging, q:5eb155decc, bs:coverage:First_specialist_visit, bs:coverage:Treatment_start`

## What should we do first?

**The team recommends that Kainuu report THL 21/2016 access times with handover alerts, adopt a KYS-style referral template and contact model, and publish how completely stage, drugs, and MDT are recorded.** `rec:1, rec:2, rec:3, thl:21_2016, reg:kys_template, reg:named_contact, q:950a2f797b`

- The team recommends reporting lung cancer access times using THL guidance Ohjaus 21/2016 definitions (covering 16 cancers) and flagging stalled handovers, because the Health Care Act sets no legal maximum time for a cancer suspicion and the Filha programme's diagnostics recommendation with recommended time limits is to be carried out before the 2030 mid-term evaluation. `rec:1, thl:21_2016, law:no_max, q:432c0e51d6, q:614febebf2`
- The team recommends a KYS-style referral template, referring persistent symptoms after a normal X-ray, and a diagnostic-phase contact person: mentor insight notes weak referrals get lower urgency, reviewed regional pathway documents show only KYS has those referral rules and no reviewed region names a diagnostic contact, and STM roadmap measure 1.2.3 plans coordinator guidance by 2026–2028 (adopted 2029–2031) without specifying the phase. `rec:2, mentor:kaisa_referral, reg:kys_template, reg:kys_persistent, reg:only_kys_xray, reg:named_contact, q:fc81032a80, q:abcbb06ae3, q:050ee09ebe`
- Given Kainuu's crude 0.9% (95% CI 0.2–3.2; n=2/226) recorded MDT share versus 6.0% (893/14873) nationally, missing stage for about 48% of patients, and incomplete national data collection, the team recommends publishing per county how completely stage, drug treatment, and MDT meetings are recorded while STM roadmap measure 3.2.1 plans a quality registry (decree 2026–2028; reports 2029–2031 at 90% coverage). `rec:3, cty:mdt_recorded:Kainuun_hyvinvointialue, nat:mdt_recorded, bs:coverage:Diagnosis, q:7885b0974f, q:950a2f797b, q:82d365cd2c, q:f07a34a300, q:4a856bd695, q:f540c706f8`

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
- `q:432c0e51d6` (verified locally): The upcoming national diagnostics recommendation will include “suositellut aikarajat erikoissairaanhoitoon eri diagnostiikan polun vaiheille” (recommended time limits in specialist care), to be carried out (“toteutetaan”; may mean produced or implemented) before the 2030 mid-term evaluation — filha_lung_programme_2026_fi.pdf, p.16
- `q:4a856bd695` (verified locally): the registry's data, including stage, allows reliable assessment and comparison of quality and effectiveness, with 90% data coverage — roadmap_2026_2031_fi.pdf, p.60
- `q:5eb155decc` (verified locally): Report evidence for pathway stage 'Imaging' — keuhkosyoparaportti_2019_2023.html, §4.1.1 Toteamistapa
- `q:614febebf2` (verified locally): When (p.24): > “Väliarvio toteutetaan vuonna 2030, ohjelman puolivälissä ja loppuarviointi vuonna 2036. Eri > osa-alueiden suositukset toteutetaan ennen väliarviointia.” — filha_lung_programme_2026_fi.pdf, p.24
- `q:7885b0974f` (verified locally): Report evidence for pathway stage 'Diagnosis' — keuhkosyoparaportti_2019_2023.html, §4.1.3 Levinneisyystiedon kattavuus
- `q:82d365cd2c` (verified locally): “Tällä hetkellä keuhkosyöpään liittyvien tietojen raportointi, kerääminen ja tallentaminen on puutteellista”; nationally uniform recording instructions (“yhtenäiset kirjaamisohjeet”) must be ensured — filha_lung_programme_2026_fi.pdf, p.21
- `q:950a2f797b` (verified locally): Reporting, collection and storage of lung cancer data is currently incomplete. — filha_lung_programme_2026_fi.pdf, p.21
- `q:abcbb06ae3` (verified locally): 2026–2028: guidance on a named doctor, nurse or specialist worker coordinating cancer care. 2029–2031: wellbeing services counties have adopted it. — roadmap_2026_2031_fi.pdf, p.32
- `q:f07a34a300` (verified locally): A national cancer care quality registry will be set up alongside THL's Cancer Registry. — roadmap_2026_2031_fi.pdf, p.59
- `q:f540c706f8` (verified locally): A national quality registry is planned; indicator: data incl. stage (“ml. levinneisyystieto”) at 90% coverage — roadmap_2026_2031_fi.pdf, p.60
- `q:fc81032a80` (verified locally): Measure 1.2.3: Create an operating model and guidance for a named worker responsible for coordinating cancer care. — roadmap_2026_2031_fi.pdf, p.32
- `rec:1` (recommendation (ours)): Team recommendation 1: Counties report access times using the THL 21/2016 definitions, with handover alerts. Each wellbeing services county reports lung cancer access times (referral → first specialist visit → diagnosis → treatment start) using the definitions in THL's Hoitoonpääsyn seuranta syövän hoidossa (Ohjaus 21/2016). Until national target times exist, flag stalled handovers. — recommendations.md, §1. Counties report access times using the THL 21/2016 definitions, with handover alerts
- `rec:2` (recommendation (ours)): Team recommendation 2: A KYS-style referral template, a persistent-symptoms rule and a named contact. Adopt a standard referral content list and template, modelled on KYS. • Add a rule for primary care: if symptoms persist after a normal X-ray, refer for a pulmonologist assessment. • Name a contact person for the diagnostic phase, from referral to diagnosis. — recommendations.md, §2. A KYS-style referral template, a persistent-symptoms rule and a named contact
- `rec:3` (recommendation (ours)): Team recommendation 3: Report recording completeness per county: stage, drug treatment, MDT coding. Publish, per county, how completely stage, drug treatment and MDT meetings are recorded. Read county ‘gaps’ in these fields as data-quality signals first. — recommendations.md, §3. Report recording completeness per county: stage, drug treatment, MDT coding
- `reg:kys_persistent` (verified by Hellu): KYS: refer persistent unexplained symptoms even if the X-ray is clear — pathway_brief.md, 6. Regional pathways compared
- `reg:kys_template` (verified by Hellu): Only KYS lists required referral content and provides a referral template — pathway_brief.md, 6. Regional pathways compared
- `reg:named_contact` (verified by Hellu): No region names a contact person for the diagnostic phase — pathway_brief.md, 6. Regional pathways compared
- `reg:only_kys_xray` (verified by Hellu): Only KYS tells primary care what to do with a normal X-ray and continuing symptoms — pathway_brief.md, 6. Regional pathways compared
- `thl:21_2016` (verified by Hellu): THL Ohjaus 21/2016 defines how cancer access times are recorded, for 16 cancers — pathway_brief.md, 6. Regional pathways compared
