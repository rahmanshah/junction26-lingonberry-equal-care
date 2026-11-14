# Helsinki: lung cancer pathway brief

Status: **validated** · gemini-4-argon (thinking HIGH) · 2026-11-14T12:50:40+00:00 · attempts: 1

## Where do we lag?

**In Helsinki, the crude share of patients with a recorded MDT meeting is 0.1% (95% CI 0.0–0.4; n=1/1486), whose 95% confidence interval excludes the 6.0% (893/14873) national figure.** `cty:mdt_recorded:Helsingin_kaupunki, nat:mdt_recorded`

- Across overlapping treatment categories where a patient can have several, Helsinki's crude curative treatment share is 33.0% (95% CI 30.7–35.5; n=491/1486), whose 95% confidence interval excludes and lies above the 27.0% (4009/14873) national share, while crude life-prolonging treatment is 30.8% (95% CI 28.5–33.1; n=457/1486), whose 95% confidence interval includes the 30.4% (4522/14873) national value. `cty:curative:Helsingin_kaupunki, nat:curative, cty:life_prolonging:Helsingin_kaupunki, nat:life_prolonging`
- In these overlapping treatment categories, Helsinki's crude symptomatic treatment share is 34.5% (95% CI 32.1–37.0; n=513/1486), whose 95% confidence interval excludes and lies below the 39.5% (5871/14873) national figure, while the crude share with no treatment record within 12 months is 29.1% (95% CI 26.8–31.4; n=432/1486), whose 95% confidence interval includes 27.5% (4089/14873) nationally. `cty:symptomatic:Helsingin_kaupunki, nat:symptomatic, cty:no_treatment_record:Helsingin_kaupunki, nat:no_treatment_record`
- In the national registry report, MDT codes measure recording practice rather than care because HILMO entries come only from direct patient contacts, and no treatment record within 12 months mixes untreated patients with unrecorded treatment. `bs:coverage:MDT, q:39e6ba43a9, bs:coverage:Treatment_start`
- Nationally, preliminary unpublished figures show lung cancer takes 155 days on average from first symptoms to first treatment in Finland versus 107 days in Sweden and 67 days in Denmark, comprising 56 days of patient delay, 41 days in primary care, and 58 days in specialist care. `mot:total_fi, mot:total_se, mot:total_dk, mot:patient, mot:primary, mot:specialist`

## How sure are we?

**County treatment shares are crude, are not age-adjusted, and cannot be stage-adjusted because stage at diagnosis is missing for about 48% of patients in the national report.** `bs:coverage:Diagnosis, q:7885b0974f, k16:curative:men:national`

- Helsinki's crude curative share of 33.0% (95% CI 30.7–35.5; n=491/1486) has separate limitations: county table shares are not age-adjusted, and independently they cannot be stage-adjusted because stage at diagnosis is missing for about 48% of patients. `cty:curative:Helsingin_kaupunki, bs:coverage:Diagnosis, q:7885b0974f`
- Age-adjusted values exist only from Kuva 16 for curative treatment by sex, where the national reference lines digitised from the figure are 26.7% for men and 26.9% for women at ±0.5 percentage points precision, and without a county Kuva 16 figure we cannot test whether Helsinki's crude curative difference holds after age adjustment. `k16:curative:men:national, k16:curative:women:national`
- As a data-quality signal, Helsinki's crude share with no treatment record within 12 months is 29.1% (95% CI 26.8–31.4; n=432/1486), whose 95% confidence interval includes the 27.5% (4089/14873) national value, while a 2019 Lääkärilehti journal article found HILMO diagnoses match the Cancer Registry for about 90% of most cancer types, concerning diagnosis concordance only. `cty:no_treatment_record:Helsingin_kaupunki, nat:no_treatment_record, lit:hilmo_90`
- Public data do not measure symptoms or referrals, primary care visits are not included in the report's data and occupational health is not mentioned, imaging appears only indirectly as clinical-only diagnosis in about 20% of patients without wait times, and specialist visit (93.6%) and treatment records within 12 months lack start dates. `bs:coverage:Symptoms, bs:coverage:Referral, bs:coverage:Primary_care_occupational_health, q:323de0d90d, bs:coverage:Imaging, q:5eb155decc, bs:coverage:First_specialist_visit, bs:coverage:Treatment_start`

## What should we do first?

**The team recommends publishing county recording completeness for stage, drug treatment, and MDT coding, reporting access times under THL 21/2016 definitions with handover alerts, and standardising referrals and coordination.** `rec:1, rec:2, rec:3, thl:21_2016`

- Given Helsinki's crude 0.1% (95% CI 0.0–0.4; n=1/1486) MDT-recorded share versus 6.0% (893/14873) nationally and about 48% missing stage nationally, the team recommends publishing county recording completeness for stage, drug treatment, and MDT coding while STM roadmap measure 3.2.1 plans a national quality registry decree by 2026–2028 targeting 90% coverage including stage by 2029–2031. `rec:3, cty:mdt_recorded:Helsingin_kaupunki, nat:mdt_recorded, bs:coverage:Diagnosis, q:950a2f797b, q:f07a34a300, q:4a856bd695, q:f540c706f8`
- Because Health Care Act §52 sets no legal maximum time for a cancer suspicion and Finland lacks national access-time monitoring, the team recommends reporting referral-to-treatment access times under THL Ohjaus 21/2016 definitions (for 16 cancers) and flagging stalled handovers while STM roadmap measure 3.1.2 plans national pathways and access times by 2026–2028 and 2029–2031. `rec:1, law:no_max, q:4e702a20fe, thl:21_2016, q:ed87906241, q:def306014c, q:b326e35410`
- The team recommends adopting a standard referral template and persistent-symptoms rule modelled on the KYS regional pathway document—which directs primary care to refer persistent unexplained symptoms for a pulmonologist assessment even after a normal X-ray—and naming a diagnostic-phase contact person, backed by mentor insight that weak referrals receive lower urgency ratings. `rec:2, reg:kys_template, reg:kys_persistent, reg:only_kys_xray, reg:named_contact, mentor:kaisa_referral`
- While the Filha National Lung Cancer Programme's diagnostics recommendation with primary-care referral criteria and specialist time limits is to be carried out before the 2030 mid-term evaluation, and STM roadmap measures 2.5.2 and 1.2.3 plan standardised referral criteria and care-coordinator guidance by 2026–2028 for county adoption by 2029–2031, the team recommends acting now. `rec:1, rec:2, q:29b792498e, q:8f358a9de6, q:614febebf2, q:432c0e51d6, q:37bb4c3b38, q:c61439b30f, q:fc81032a80, q:abcbb06ae3`

## Review flags (for human review only)

_Flags are for human review only; they never change the brief's status or approve it._

- [medium] `how_sure_are_we.headline`: None of the cited claims state that county treatment shares are crude or not age-adjusted (only a national age-adjusted reference line for men's curative treatment and missing-stage claims are cited), and the cited diagnosis claim states specifically that curative shares cannot be stage-adjusted rather than all county treatment shares.
- [medium] `how_sure_are_we.details[1]`: The cited claims only provide the national age-adjusted reference lines from Kuva 16 for curative treatment by sex; they do not establish that age-adjusted values exist nowhere else in the report, nor do they mention Helsinki, its crude curative difference, or the absence of a county Kuva 16 figure.
- [low] `what_to_do_first.details[0]`: In the cited notes for STM roadmap measure 3.2.1, the 2029–2031 deadline applies to annual reports for at least five cancers, not specifically to the 90% coverage indicator.
- [low] `what_to_do_first.details[3]`: Conflates the timelines of STM roadmap measures 2.5.2 and 1.2.3: county adoption by 2029–2031 applies to measure 1.2.3 (care-coordinator guidance), whereas measure 2.5.2 plans standardised referral criteria in national pathways for at least the five most common cancers by 2026–2028 and all significant cancers by 2029–2031.

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
- `q:29b792498e` (verified locally): Policy evidence for pathway stage 'Referral' — filha_lung_programme_2026_fi.pdf, p.16
- `q:323de0d90d` (verified locally): Report evidence for pathway stage 'Primary care / occupational health' — keuhkosyoparaportti_2019_2023.html, §3.3 Menetelmät
- `q:37bb4c3b38` (verified locally): Policy evidence for pathway stage 'Referral' — roadmap_2026_2031_fi.pdf, p.52; p.106
- `q:39e6ba43a9` (verified locally): Report evidence for pathway stage 'MDT' — keuhkosyoparaportti_2019_2023.html, §3.3 Menetelmät
- `q:432c0e51d6` (verified locally): The upcoming national diagnostics recommendation will include “suositellut aikarajat erikoissairaanhoitoon eri diagnostiikan polun vaiheille” (recommended time limits in specialist care), to be carried out (“toteutetaan”; may mean produced or implemented) before the 2030 mid-term evaluation — filha_lung_programme_2026_fi.pdf, p.16
- `q:4a856bd695` (verified locally): the registry's data, including stage, allows reliable assessment and comparison of quality and effectiveness, with 90% data coverage — roadmap_2026_2031_fi.pdf, p.60
- `q:4e702a20fe` (verified locally): Finland has no unified national system to steer the drafting of cancer-specific treatment recommendations, or the implementation and monitoring of care pathways based on them (quality and effectiveness targets/indicators, including access to care, and cancer-specific and generic PROMs). Existing recommendations and pathways, and the targets and indicators to be monitored, are not coordinated nationally. This maintains regional inequality in the availability and effectiveness of cancer care. — strategy_2026_2035_fi.pdf, p.33
- `q:5eb155decc` (verified locally): Report evidence for pathway stage 'Imaging' — keuhkosyoparaportti_2019_2023.html, §4.1.1 Toteamistapa
- `q:614febebf2` (verified locally): When (p.24): > “Väliarvio toteutetaan vuonna 2030, ohjelman puolivälissä ja loppuarviointi vuonna 2036. Eri > osa-alueiden suositukset toteutetaan ennen väliarviointia.” — filha_lung_programme_2026_fi.pdf, p.24
- `q:7885b0974f` (verified locally): Report evidence for pathway stage 'Diagnosis' — keuhkosyoparaportti_2019_2023.html, §4.1.3 Levinneisyystiedon kattavuus
- `q:8f358a9de6` (verified locally): p.16: > “Tämän ohjelman yhtenä toimenpiteenä tuotetaan kansallinen suositus keuhkosyöpien diagnostiikasta. Se > sisältää myös lähetekriteerit perusterveydenhuollolle ja suositellut aikarajat erikoissairaanhoitoon > eri diagnostiikan polun vaiheille.” — filha_lung_programme_2026_fi.pdf, p.16
- `q:950a2f797b` (verified locally): Reporting, collection and storage of lung cancer data is currently incomplete. — filha_lung_programme_2026_fi.pdf, p.21
- `q:abcbb06ae3` (verified locally): 2026–2028: guidance on a named doctor, nurse or specialist worker coordinating cancer care. 2029–2031: wellbeing services counties have adopted it. — roadmap_2026_2031_fi.pdf, p.32
- `q:b326e35410` (verified locally): National pathways with “syöpäkohtaiset hoitoonpääsyajat” for five (unnamed) cancers in 2026–2028, Nordic model — roadmap_2026_2031_fi.pdf, p.57
- `q:c61439b30f` (verified locally): 2026–2028: standardised referral criteria and symptom-based models included in the national pathways of at least the five most common cancers. — roadmap_2026_2031_fi.pdf, p.53
- `q:def306014c` (verified locally): p.57, timetable: > “2026–2028: Kansalliset hoitoketjukuvaukset tehty viidestä syövästä ja syöpäkohtaiset > hoitoonpääsyajat on määritetty.” — roadmap_2026_2031_fi.pdf, p.57
- `q:ed87906241` (verified locally): p.56, heading: > “Toimenpide 3.1.2 Laaditaan syöpäkohtaiset hoitoketjukuvaukset, ja niiden pohjalta sovelletut > alueelliset hoitoketjut, sekä mekanismi niiden ylläpitoon ja hallintaan” — roadmap_2026_2031_fi.pdf, p.56
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
