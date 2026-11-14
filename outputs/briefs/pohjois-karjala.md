# Pohjois-Karjala: lung cancer pathway brief

Status: **validated** · gemini-4-argon (thinking HIGH) · 2026-11-14T12:07:08+00:00 · attempts: 1

## Where do we lag?

**Pohjois-Karjala lags nationally in crude shares of curative treatment (21.4%, 95% CI 18.0–25.1 vs 27.0%) and life-prolonging treatment (23.5%, 95% CI 20.1–27.4 vs 30.4%).** `cty:curative:Pohjois_Karjalan_hyvinvointialue, nat:curative, cty:life_prolonging:Pohjois_Karjalan_hyvinvointialue, nat:life_prolonging`

- In 2019–2023, the county's crude curative treatment share was 21.4% (95% CI 18.0–25.1; n=109/510) vs 27.0% nationally (4009/14873), and its crude life-prolonging treatment share was 23.5% (95% CI 20.1–27.4; n=120/510) vs 30.4% nationally (4522/14873); these 95% confidence intervals exclude the national values. `cty:curative:Pohjois_Karjalan_hyvinvointialue, nat:curative, cty:life_prolonging:Pohjois_Karjalan_hyvinvointialue, nat:life_prolonging`
- The crude symptomatic treatment share was 52.2% (95% CI 47.8–56.5; n=266/510) vs 39.5% nationally (5871/14873), with a 95% confidence interval excluding the national value; treatment categories overlap because a patient can have several treatments within 12 months, and county shares are not adjusted for age or stage. `cty:symptomatic:Pohjois_Karjalan_hyvinvointialue, nat:symptomatic, bs:coverage:Diagnosis, bs:coverage:Treatment_start`
- A multidisciplinary team (MDT) meeting was recorded for a crude 0.0% of patients (95% CI 0.0–0.8; n=0/510) vs 6.0% nationally (893/14873), with the 95% confidence interval excluding the national value, though this indicator measures HILMO recording practice from direct patient contacts rather than actual care. `cty:mdt_recorded:Pohjois_Karjalan_hyvinvointialue, nat:mdt_recorded, bs:coverage:MDT, q:39e6ba43a9`

## How sure are we?

**The low crude curative share is unlikely to be only a recording artefact, but county figures are unadjusted for age or stage and omit pathway waiting times.** `cty:curative:Pohjois_Karjalan_hyvinvointialue, cty:no_treatment_record:Pohjois_Karjalan_hyvinvointialue, bs:coverage:Diagnosis, bs:coverage:Treatment_start`

- The crude share with no treatment record within 12 months (mixing untreated patients and unrecorded treatment) is 22.2% (95% CI 18.8–26.0; n=113/510) vs 27.5% nationally (4089/14873), its 95% CI excluding 27.5%; as an inference, this is consistent with relatively complete treatment recording (not direct evidence), so the low crude curative share is less likely to be only a recording artefact. `cty:no_treatment_record:Pohjois_Karjalan_hyvinvointialue, nat:no_treatment_record, cty:curative:Pohjois_Karjalan_hyvinvointialue, bs:coverage:Treatment_start`
- A journal article found about 90% HILMO–Cancer Registry diagnosis concordance, which says nothing about treatment or MDT recording; moreover, county shares are crude because stage at diagnosis is missing for ~48% of patients nationally and only digitised national age-adjusted curative reference lines from Kuva 16 (men 26.7%, women 26.9%, about ±0.5 percentage points) are available. `lit:hilmo_90, bs:coverage:Diagnosis, q:7885b0974f, k16:curative:men:national, k16:curative:women:national`
- Primary care visits are not included in the report's data and occupational health is not mentioned at all; public data also lack symptom onset, referral dates, imaging dates or waits, and the dates of the first specialist visit and treatment start. `bs:coverage:Primary_care_occupational_health, q:323de0d90d, bs:coverage:Symptoms, bs:coverage:Referral, bs:coverage:Imaging, bs:coverage:First_specialist_visit, bs:coverage:Treatment_start`
- Preliminary, unpublished national figures report an average of 155 days from first symptoms to treatment in Finland (56 days patient delay, 41 days in primary care, and 58 days in specialist care) compared with 107 days in Sweden and 67 days in Denmark, whereas county-level delays remain unmeasured. `mot:total_fi, mot:total_se, mot:total_dk, mot:patient, mot:primary, mot:specialist`

## What should we do first?

**The team recommends reporting THL 21/2016 access times with handover alerts, standardising referrals with a diagnostic contact person, and publishing stage, drug, and MDT recording completeness.** `rec:1, rec:2, rec:3, thl:21_2016, bs:coverage:Diagnosis, bs:coverage:MDT`

- Because the Health Care Act sets no legal maximum time for a cancer suspicion and national target times are only planned (roadmap pathways in 2026–2028; Filha diagnostic time limits due before the 2030 evaluation), the team recommends reporting referral-to-treatment access times using THL Ohjaus 21/2016 definitions for 16 cancers and flagging stalled handovers. `rec:1, law:no_max, thl:21_2016, q:def306014c, q:8f358a9de6, q:614febebf2, q:20d6ca414e`
- Because mentor insight indicates a weak referral gets a lower urgency rating in specialist care, and while the roadmap plans national referral criteria (2026–2028) and care-coordinator guidance (2026–2028, for county adoption in 2029–2031), the team recommends adopting a KYS-style referral template, referring persistent symptoms after a normal X-ray to a pulmonologist, and naming a diagnostic-phase contact person. `rec:2, mentor:kaisa_referral, q:9a1cd194f5, q:c61439b30f, q:fc81032a80, q:abcbb06ae3, q:050ee09ebe`
- Given Pohjois-Karjala's crude recorded MDT share of 0.0% (95% CI 0.0–0.8; n=0/510) vs 6.0% nationally (893/14873) and missing stage for ~48% of patients nationally—while a national quality registry targeting 90% coverage is planned—the team recommends publishing county recording completeness for stage, drug treatment, and MDT coding and reading gaps in these fields as data-quality signals first. `rec:3, cty:mdt_recorded:Pohjois_Karjalan_hyvinvointialue, nat:mdt_recorded, bs:coverage:Diagnosis, q:7885b0974f, q:950a2f797b, q:f07a34a300, q:4a856bd695`

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
- `cty:curative:Pohjois_Karjalan_hyvinvointialue` (verified locally): Pohjois-Karjalan hyvinvointialue: curative treatment 21.4% (95% CI 18.0–25.1; n=109/510), below vs national 27.0% — keuhkosyoparaportti_2019_2023.html, Taulukko 11
- `cty:life_prolonging:Pohjois_Karjalan_hyvinvointialue` (verified locally): Pohjois-Karjalan hyvinvointialue: life-prolonging treatment 23.5% (95% CI 20.1–27.4; n=120/510), below vs national 30.4% — keuhkosyoparaportti_2019_2023.html, Taulukko 11
- `cty:mdt_recorded:Pohjois_Karjalan_hyvinvointialue` (verified locally): Pohjois-Karjalan hyvinvointialue: MDT meeting recorded 0.0% (95% CI 0.0–0.8; n=0/510), below vs national 6.0% — keuhkosyoparaportti_2019_2023.html, Taulukko 11
- `cty:no_treatment_record:Pohjois_Karjalan_hyvinvointialue` (verified locally): Pohjois-Karjalan hyvinvointialue: no treatment record within 12 months 22.2% (95% CI 18.8–26.0; n=113/510), below vs national 27.5% — keuhkosyoparaportti_2019_2023.html, Taulukko 11
- `cty:symptomatic:Pohjois_Karjalan_hyvinvointialue` (verified locally): Pohjois-Karjalan hyvinvointialue: symptomatic treatment 52.2% (95% CI 47.8–56.5; n=266/510), above vs national 39.5% — keuhkosyoparaportti_2019_2023.html, Taulukko 11
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
- `q:4a856bd695` (verified locally): the registry's data, including stage, allows reliable assessment and comparison of quality and effectiveness, with 90% data coverage — roadmap_2026_2031_fi.pdf, p.60
- `q:614febebf2` (verified locally): When (p.24): > “Väliarvio toteutetaan vuonna 2030, ohjelman puolivälissä ja loppuarviointi vuonna 2036. Eri > osa-alueiden suositukset toteutetaan ennen väliarviointia.” — filha_lung_programme_2026_fi.pdf, p.24
- `q:7885b0974f` (verified locally): Report evidence for pathway stage 'Diagnosis' — keuhkosyoparaportti_2019_2023.html, §4.1.3 Levinneisyystiedon kattavuus
- `q:8f358a9de6` (verified locally): p.16: > “Tämän ohjelman yhtenä toimenpiteenä tuotetaan kansallinen suositus keuhkosyöpien diagnostiikasta. Se > sisältää myös lähetekriteerit perusterveydenhuollolle ja suositellut aikarajat erikoissairaanhoitoon > eri diagnostiikan polun vaiheille.” — filha_lung_programme_2026_fi.pdf, p.16
- `q:950a2f797b` (verified locally): Reporting, collection and storage of lung cancer data is currently incomplete. — filha_lung_programme_2026_fi.pdf, p.21
- `q:9a1cd194f5` (verified locally): support a smooth transfer to specialist care by defining standardised referral criteria within the national pathways, so that patients with possible cancer symptoms who meet them are directed quickly to diagnostic tests — roadmap_2026_2031_fi.pdf, p.52
- `q:abcbb06ae3` (verified locally): 2026–2028: guidance on a named doctor, nurse or specialist worker coordinating cancer care. 2029–2031: wellbeing services counties have adopted it. — roadmap_2026_2031_fi.pdf, p.32
- `q:c61439b30f` (verified locally): 2026–2028: standardised referral criteria and symptom-based models included in the national pathways of at least the five most common cancers. — roadmap_2026_2031_fi.pdf, p.53
- `q:def306014c` (verified locally): p.57, timetable: > “2026–2028: Kansalliset hoitoketjukuvaukset tehty viidestä syövästä ja syöpäkohtaiset > hoitoonpääsyajat on määritetty.” — roadmap_2026_2031_fi.pdf, p.57
- `q:f07a34a300` (verified locally): A national cancer care quality registry will be set up alongside THL's Cancer Registry. — roadmap_2026_2031_fi.pdf, p.59
- `q:fc81032a80` (verified locally): Measure 1.2.3: Create an operating model and guidance for a named worker responsible for coordinating cancer care. — roadmap_2026_2031_fi.pdf, p.32
- `rec:1` (recommendation (ours)): Team recommendation 1: Counties report access times using the THL 21/2016 definitions, with handover alerts. Each wellbeing services county reports lung cancer access times (referral → first specialist visit → diagnosis → treatment start) using the definitions in THL's Hoitoonpääsyn seuranta syövän hoidossa (Ohjaus 21/2016). Until national target times exist, flag stalled handovers. — recommendations.md, §1. Counties report access times using the THL 21/2016 definitions, with handover alerts
- `rec:2` (recommendation (ours)): Team recommendation 2: A KYS-style referral template, a persistent-symptoms rule and a named contact. Adopt a standard referral content list and template, modelled on KYS. • Add a rule for primary care: if symptoms persist after a normal X-ray, refer for a pulmonologist assessment. • Name a contact person for the diagnostic phase, from referral to diagnosis. — recommendations.md, §2. A KYS-style referral template, a persistent-symptoms rule and a named contact
- `rec:3` (recommendation (ours)): Team recommendation 3: Report recording completeness per county: stage, drug treatment, MDT coding. Publish, per county, how completely stage, drug treatment and MDT meetings are recorded. Read county ‘gaps’ in these fields as data-quality signals first. — recommendations.md, §3. Report recording completeness per county: stage, drug treatment, MDT coding
- `thl:21_2016` (verified by Hellu): THL Ohjaus 21/2016 defines how cancer access times are recorded, for 16 cancers — pathway_brief.md, 6. Regional pathways compared
