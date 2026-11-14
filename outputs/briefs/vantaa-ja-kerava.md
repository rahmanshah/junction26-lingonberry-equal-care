# Vantaa ja Kerava: lung cancer pathway brief

Status: **validated** · gemini-4-argon (thinking HIGH) · 2026-11-14T12:05:43+00:00 · attempts: 1

## Where do we lag?

**Vantaa ja Kerava lags nationally in crude life-prolonging treatment at 20.3% (95% CI 17.3–23.8) versus 30.4% and crude recorded MDT meetings at 0.2% (95% CI 0.0–0.9) versus 6.0%.** `cty:life_prolonging:Vantaan_ja_Keravan_hyvinvointialue, nat:life_prolonging, cty:mdt_recorded:Vantaan_ja_Keravan_hyvinvointialue, nat:mdt_recorded`

- In Vantaa ja Kerava, the crude life-prolonging treatment share is 20.3% (95% CI 17.3–23.8; n=121/595), where the 95% confidence interval excludes the national value of 30.4% (4522/14873), while the crude curative treatment share of 35.6% (95% CI 31.9–39.6; n=212/595) has a 95% confidence interval that excludes the national 27.0% (4009/14873) upward. `cty:life_prolonging:Vantaan_ja_Keravan_hyvinvointialue, nat:life_prolonging, cty:curative:Vantaan_ja_Keravan_hyvinvointialue, nat:curative`
- The crude symptomatic treatment share is 36.1% (95% CI 32.4–40.1; n=215/595) versus 39.5% (5871/14873) nationally, and the crude share with no treatment record within 12 months—mixing untreated patients and unrecorded treatment—is 28.9% (95% CI 25.4–32.7; n=172/595) versus 27.5% (4089/14873) nationally, with each 95% confidence interval including the national value. `cty:symptomatic:Vantaan_ja_Keravan_hyvinvointialue, nat:symptomatic, cty:no_treatment_record:Vantaan_ja_Keravan_hyvinvointialue, nat:no_treatment_record, bs:coverage:Treatment_start`
- The crude share of patients with a recorded MDT meeting is 0.2% (95% CI 0.0–0.9; n=1/595), whose 95% confidence interval excludes the national value of 6.0% (893/14873), though this measures HILMO recording from direct patient contacts rather than actual multidisciplinary care. `cty:mdt_recorded:Vantaan_ja_Keravan_hyvinvointialue, nat:mdt_recorded, bs:coverage:MDT, q:39e6ba43a9`
- Nationally, preliminary unpublished figures show lung cancer takes 155 days on average from symptoms to treatment in Finland (56 days patient delay, 41 days primary care, and 58 days specialist care) versus 107 days in Sweden and 67 days in Denmark, though public data do not measure county wait times. `mot:total_fi, mot:total_se, mot:total_dk, mot:patient, mot:primary, mot:specialist, bs:coverage:Symptoms, bs:coverage:Treatment_start`

## How sure are we?

**County treatment figures are crude and unadjusted for stage, while public registry data do not capture primary care, referrals, or treatment wait times.** `bs:coverage:Diagnosis, bs:coverage:Primary_care_occupational_health, bs:coverage:Referral, bs:coverage:Treatment_start`

- All county treatment shares are crude—unadjusted for age or stage because stage at diagnosis is missing for ~48% of new patients—and treatment categories overlap, while Kuva 16 provides only digitised national age-adjusted curative reference lines of 26.7% for men and 26.9% for women (±0.5 percentage points). `cty:curative:Vantaan_ja_Keravan_hyvinvointialue, bs:coverage:Diagnosis, q:7885b0974f, k16:curative:men:national, k16:curative:women:national`
- Reading the crude 28.9% (95% CI 25.4–32.7) no-treatment-record share as a data-quality signal is an inference, not a finding: since 28.9% is above the 27.5% national value (though its 95% confidence interval includes 27.5%), the low crude 20.3% (95% CI 17.3–23.8) life-prolonging share versus 30.4% nationally may partly reflect unrecorded treatment. `cty:no_treatment_record:Vantaan_ja_Keravan_hyvinvointialue, nat:no_treatment_record, cty:life_prolonging:Vantaan_ja_Keravan_hyvinvointialue, nat:life_prolonging, bs:coverage:Treatment_start`
- A journal article found HILMO diagnoses matched the Cancer Registry for about 90% of most cancer types, but that concerns diagnosis concordance only and says nothing about how completely treatment, referrals, or MDT meetings are recorded. `lit:hilmo_90, q:950a2f797b`
- Public data do not measure symptom onset, referrals, imaging waits, or county wait times for specialist visits and treatment start, while primary care visits are not included in the report's data and occupational health is not mentioned at all. `bs:coverage:Symptoms, bs:coverage:Referral, bs:coverage:Imaging, bs:coverage:First_specialist_visit, bs:coverage:Treatment_start, bs:coverage:Primary_care_occupational_health, q:323de0d90d`

## What should we do first?

**The team recommends auditing stage, drug, and MDT recording completeness, tracking access times using THL 21/2016 definitions, and standardising referrals and diagnostic coordination.** `rec:3, rec:1, rec:2`

- Given Vantaa ja Kerava's crude 0.2% (95% CI 0.0–0.9) recorded MDT share, crude 20.3% (95% CI 17.3–23.8) life-prolonging share, and crude 28.9% (95% CI 25.4–32.7) no-treatment-record share, the team recommends publishing county recording completeness for stage, drug treatment, and MDT coding while a national quality registry with 90% coverage including stage is planned. `rec:3, cty:mdt_recorded:Vantaan_ja_Keravan_hyvinvointialue, cty:life_prolonging:Vantaan_ja_Keravan_hyvinvointialue, cty:no_treatment_record:Vantaan_ja_Keravan_hyvinvointialue, q:950a2f797b, q:4c7a01d84c, q:f07a34a300, q:4a856bd695`
- Because the Health Care Act sets no legal maximum time for a cancer suspicion and Finland lacks a unified pathway monitoring system, the team recommends reporting referral-to-treatment access times and flagging stalled handovers using THL guidance 21/2016 definitions for 16 cancers. `rec:1, law:no_max, q:4e702a20fe, thl:21_2016, q:24169121a4`
- While the roadmap plans national pathways, referral criteria, and coordinator guidance by 2026–2028 (for county adoption by 2029–2031) and the Filha programme's diagnostics recommendation is due before the 2030 mid-term evaluation, the team recommends a standard referral template, a persistent-symptoms referral rule, and a diagnostic contact person, since mentor insight notes weak referrals get lower urgency ratings. `rec:2, q:def306014c, q:c61439b30f, q:abcbb06ae3, q:8f358a9de6, q:614febebf2, mentor:kaisa_referral, q:556431a0c2`

## Review flags (for human review only)

_Flags are for human review only; they never change the brief's status or approve it._

- [low] `how_sure_are_we.details[0]`: Missing stage (~48%) explains why shares cannot be stage-adjusted, not why they are unadjusted for age; also, Kuva 16 is a figure from which the national reference lines were digitised rather than Kuva 16 providing only national reference lines.
- [low] `what_to_do_first.details[2]`: The cited roadmap claims specify 2029–2031 county adoption only for the coordinator guidance (q:abcbb06ae3), not for the national pathways (q:def306014c) or referral criteria (q:c61439b30f), which also specifically apply to five or at least the five most common cancers.

## Claims cited

- `bs:coverage:Diagnosis` (verified locally): Pathway stage 'Diagnosis' is measured in public data: yes (by county: yes (Kuva 7, 10, 13: PNG only)) — keuhkosyoparaportti_2019_2023.html, §4.1, Taulukko 2–4, Kuva 5–13
- `bs:coverage:First_specialist_visit` (verified locally): Pathway stage 'First specialist visit' is measured in public data: partly (by county: no) — keuhkosyoparaportti_2019_2023.html, §3.1, §4.2, Taulukko 5
- `bs:coverage:Imaging` (verified locally): Pathway stage 'Imaging' is measured in public data: partly (by county: partly (Kuva 7, PNG only)) — keuhkosyoparaportti_2019_2023.html, §4.1.1, Taulukko 2, Kuva 5–7
- `bs:coverage:MDT` (verified locally): Pathway stage 'MDT' is measured in public data: partly (by county: yes (Taulukko 11)) — keuhkosyoparaportti_2019_2023.html, §3.3, §4.2, Taulukko 5, 10, 11, 13
- `bs:coverage:Primary_care_occupational_health` (verified locally): Pathway stage 'Primary care / occupational health' is measured in public data: no (by county: no) — keuhkosyoparaportti_2019_2023.html, §3.3
- `bs:coverage:Referral` (verified locally): Pathway stage 'Referral' is measured in public data: no (by county: no) — keuhkosyoparaportti_2019_2023.html, whole report (no relevant data found)
- `bs:coverage:Symptoms` (verified locally): Pathway stage 'Symptoms' is measured in public data: no (by county: no) — keuhkosyoparaportti_2019_2023.html, whole report (no relevant data found)
- `bs:coverage:Treatment_start` (verified locally): Pathway stage 'Treatment start' is measured in public data: partly (by county: yes (type only, Taulukko 11)) — keuhkosyoparaportti_2019_2023.html, §4.2, §4.2.2, Taulukko 6–9, 11, 12, Kuva 14, 17
- `cty:curative:Vantaan_ja_Keravan_hyvinvointialue` (verified locally): Vantaan ja Keravan hyvinvointialue: curative treatment 35.6% (95% CI 31.9–39.6; n=212/595), above vs national 27.0% — keuhkosyoparaportti_2019_2023.html, Taulukko 11
- `cty:life_prolonging:Vantaan_ja_Keravan_hyvinvointialue` (verified locally): Vantaan ja Keravan hyvinvointialue: life-prolonging treatment 20.3% (95% CI 17.3–23.8; n=121/595), below vs national 30.4% — keuhkosyoparaportti_2019_2023.html, Taulukko 11
- `cty:mdt_recorded:Vantaan_ja_Keravan_hyvinvointialue` (verified locally): Vantaan ja Keravan hyvinvointialue: MDT meeting recorded 0.2% (95% CI 0.0–0.9; n=1/595), below vs national 6.0% — keuhkosyoparaportti_2019_2023.html, Taulukko 11
- `cty:no_treatment_record:Vantaan_ja_Keravan_hyvinvointialue` (verified locally): Vantaan ja Keravan hyvinvointialue: no treatment record within 12 months 28.9% (95% CI 25.4–32.7; n=172/595), not distinguishable vs national 27.5% — keuhkosyoparaportti_2019_2023.html, Taulukko 11
- `cty:symptomatic:Vantaan_ja_Keravan_hyvinvointialue` (verified locally): Vantaan ja Keravan hyvinvointialue: symptomatic treatment 36.1% (95% CI 32.4–40.1; n=215/595), not distinguishable vs national 39.5% — keuhkosyoparaportti_2019_2023.html, Taulukko 11
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
- `q:4a856bd695` (verified locally): the registry's data, including stage, allows reliable assessment and comparison of quality and effectiveness, with 90% data coverage — roadmap_2026_2031_fi.pdf, p.60
- `q:4c7a01d84c` (verified locally): nationally uniform recording instructions, and their use, must be ensured — filha_lung_programme_2026_fi.pdf, p.21
- `q:4e702a20fe` (verified locally): Finland has no unified national system to steer the drafting of cancer-specific treatment recommendations, or the implementation and monitoring of care pathways based on them (quality and effectiveness targets/indicators, including access to care, and cancer-specific and generic PROMs). Existing recommendations and pathways, and the targets and indicators to be monitored, are not coordinated nationally. This maintains regional inequality in the availability and effectiveness of cancer care. — strategy_2026_2035_fi.pdf, p.33
- `q:556431a0c2` (verified locally): the patient is referred to specialist care according to local instructions — filha_lung_programme_2026_fi.pdf, p.15
- `q:614febebf2` (verified locally): When (p.24): > “Väliarvio toteutetaan vuonna 2030, ohjelman puolivälissä ja loppuarviointi vuonna 2036. Eri > osa-alueiden suositukset toteutetaan ennen väliarviointia.” — filha_lung_programme_2026_fi.pdf, p.24
- `q:7885b0974f` (verified locally): Report evidence for pathway stage 'Diagnosis' — keuhkosyoparaportti_2019_2023.html, §4.1.3 Levinneisyystiedon kattavuus
- `q:8f358a9de6` (verified locally): p.16: > “Tämän ohjelman yhtenä toimenpiteenä tuotetaan kansallinen suositus keuhkosyöpien diagnostiikasta. Se > sisältää myös lähetekriteerit perusterveydenhuollolle ja suositellut aikarajat erikoissairaanhoitoon > eri diagnostiikan polun vaiheille.” — filha_lung_programme_2026_fi.pdf, p.16
- `q:950a2f797b` (verified locally): Reporting, collection and storage of lung cancer data is currently incomplete. — filha_lung_programme_2026_fi.pdf, p.21
- `q:abcbb06ae3` (verified locally): 2026–2028: guidance on a named doctor, nurse or specialist worker coordinating cancer care. 2029–2031: wellbeing services counties have adopted it. — roadmap_2026_2031_fi.pdf, p.32
- `q:c61439b30f` (verified locally): 2026–2028: standardised referral criteria and symptom-based models included in the national pathways of at least the five most common cancers. — roadmap_2026_2031_fi.pdf, p.53
- `q:def306014c` (verified locally): p.57, timetable: > “2026–2028: Kansalliset hoitoketjukuvaukset tehty viidestä syövästä ja syöpäkohtaiset > hoitoonpääsyajat on määritetty.” — roadmap_2026_2031_fi.pdf, p.57
- `q:f07a34a300` (verified locally): A national cancer care quality registry will be set up alongside THL's Cancer Registry. — roadmap_2026_2031_fi.pdf, p.59
- `rec:1` (recommendation (ours)): Team recommendation 1: Counties report access times using the THL 21/2016 definitions, with handover alerts. Each wellbeing services county reports lung cancer access times (referral → first specialist visit → diagnosis → treatment start) using the definitions in THL's Hoitoonpääsyn seuranta syövän hoidossa (Ohjaus 21/2016). Until national target times exist, flag stalled handovers. — recommendations.md, §1. Counties report access times using the THL 21/2016 definitions, with handover alerts
- `rec:2` (recommendation (ours)): Team recommendation 2: A KYS-style referral template, a persistent-symptoms rule and a named contact. Adopt a standard referral content list and template, modelled on KYS. • Add a rule for primary care: if symptoms persist after a normal X-ray, refer for a pulmonologist assessment. • Name a contact person for the diagnostic phase, from referral to diagnosis. — recommendations.md, §2. A KYS-style referral template, a persistent-symptoms rule and a named contact
- `rec:3` (recommendation (ours)): Team recommendation 3: Report recording completeness per county: stage, drug treatment, MDT coding. Publish, per county, how completely stage, drug treatment and MDT meetings are recorded. Read county ‘gaps’ in these fields as data-quality signals first. — recommendations.md, §3. Report recording completeness per county: stage, drug treatment, MDT coding
- `thl:21_2016` (verified by Hellu): THL Ohjaus 21/2016 defines how cancer access times are recorded, for 16 cancers — pathway_brief.md, 6. Regional pathways compared
