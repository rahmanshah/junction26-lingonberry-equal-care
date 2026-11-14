# Kymenlaakso: lung cancer pathway brief

Status: **validated** · gemini-4-argon (thinking HIGH) · 2026-11-14T12:53:21+00:00 · attempts: 1

## Where do we lag?

**Kymenlaakso’s crude curative treatment share is 19.3% (95% CI 16.3–22.7; n=114/591), where the 95% confidence interval excludes the national 27.0% (4009/14873).** `cty:curative:Kymenlaakson_hyvinvointialue, nat:curative`

- In Kymenlaakso, crude shares are higher than national values for life-prolonging treatment at 37.6% (95% CI 33.8–41.5; n=222/591) versus 30.4% (4522/14873) nationally and for symptomatic treatment at 51.3% (95% CI 47.2–55.3; n=303/591) versus 39.5% (5871/14873) nationally, with 95% confidence intervals excluding the national values in these overlapping treatment categories (a patient can have several). `cty:life_prolonging:Kymenlaakson_hyvinvointialue, nat:life_prolonging, cty:symptomatic:Kymenlaakson_hyvinvointialue, nat:symptomatic`
- After age adjustment in values digitised from Kuva 16 (precision about ±0.5 percentage points), the curative treatment gap holds for men at 17.9% (95% CI 13.9–22.9) versus 26.7% nationally (95% confidence interval excludes the national value), while for women the age-adjusted share is 22.6% (95% CI 16.8–29.3) versus 26.9% nationally (95% confidence interval includes the national value). `k16:curative:men:Kymenlaakson_hyvinvointialue, k16:curative:men:national, k16:curative:women:Kymenlaakson_hyvinvointialue, k16:curative:women:national`
- A multidisciplinary team (MDT) meeting is recorded for a crude share of 0.5% (95% CI 0.2–1.5; n=3/591) of patients in Kymenlaakso versus 6.0% (893/14873) nationally, with the 95% confidence interval excluding the national value, though HILMO only captures procedures from direct patient contacts so MDT records measure recording practice rather than care. `cty:mdt_recorded:Kymenlaakson_hyvinvointialue, nat:mdt_recorded, bs:coverage:MDT, q:39e6ba43a9`

## How sure are we?

**Kymenlaakso’s crude share with no treatment record within 12 months is 16.4% (95% CI 13.7–19.6; n=97/591), where the 95% confidence interval excludes the national 27.5% (4089/14873).** `cty:no_treatment_record:Kymenlaakson_hyvinvointialue, nat:no_treatment_record`

- Because the crude no-treatment-record share mixes untreated patients and unrecorded treatment, having its 95% confidence interval entirely below the national value is consistent—as an inference, not a finding—with relatively complete treatment recording, so a low crude curative share among the overlapping treatment categories is less likely to be only a recording artefact. `cty:no_treatment_record:Kymenlaakson_hyvinvointialue, nat:no_treatment_record, bs:coverage:Treatment_start, cty:curative:Kymenlaakson_hyvinvointialue`
- The county treatment shares are crude and have 2 separate limitations: they are not age-adjusted (an age-adjusted value exists only from Kuva 16, for curative treatment, by sex), and separately they cannot be stage-adjusted because stage at diagnosis is missing for about 48% of patients. `cty:curative:Kymenlaakson_hyvinvointialue, k16:curative:men:Kymenlaakson_hyvinvointialue, k16:curative:women:Kymenlaakson_hyvinvointialue, bs:coverage:Diagnosis, q:7885b0974f`
- A journal article found that HILMO diagnoses match the Cancer Registry for about 90% of most cancer types, which concerns diagnosis concordance only and not treatment or MDT recording, while the report’s public data do not measure symptoms, referrals or treatment start dates, and primary care visits are not included in the report's data. `lit:hilmo_90, bs:coverage:Symptoms, bs:coverage:Referral, bs:coverage:Treatment_start, bs:coverage:Primary_care_occupational_health, q:323de0d90d`
- Public data note clinical-only diagnosis such as imaging in about 20% of patients and specialist visits within 12 months (93.6% nationally) without dates, while preliminary, unpublished national averages—not county figures—show 155 days from symptoms to treatment in Finland (56 patient, 41 primary care, 58 specialist days) versus 107 in Sweden and 67 in Denmark. `bs:coverage:Imaging, q:5eb155decc, bs:coverage:First_specialist_visit, mot:total_fi, mot:total_se, mot:total_dk, mot:patient, mot:primary, mot:specialist`

## What should we do first?

**The team recommends reporting THL 21/2016 access times with handover alerts, standardising referrals with a diagnostic contact person, and publishing county recording completeness for stage, drug treatment and MDT.** `rec:1, rec:2, rec:3`

- The team recommends reporting lung cancer access times (referral, specialist visit, diagnosis, treatment start) using THL guidance Ohjaus 21/2016 definitions for 16 cancers and flagging stalled handovers, as Health Care Act §52 sets no legal maximum time for a cancer suspicion and the STM roadmap's measure 3.1.2 plans national pathway descriptions and target access times by 2026–2028. `rec:1, thl:21_2016, q:24169121a4, law:no_max, q:ed87906241, q:def306014c, q:b326e35410`
- The team recommends a standard referral template, referring persistent symptoms after a normal X-ray to a pulmonologist, and a named diagnostic contact person, as mentor insight notes weak referrals get lower urgency, the Filha programme's diagnostics recommendation is to be carried out before the 2030 mid-term evaluation, and the STM roadmap's measure 1.2.3 plans care-coordinator guidance by 2026–2028. `rec:2, mentor:kaisa_referral, q:29b792498e, q:8f358a9de6, q:614febebf2, q:fc81032a80, q:050ee09ebe, q:abcbb06ae3`
- Given Kymenlaakso’s 0.5% (95% CI 0.2–1.5; n=3/591) crude MDT share versus 6.0% (893/14873) nationally and stage missing for about 48% of patients, the team recommends publishing county recording completeness for stage, drug treatment and MDT coding as data-quality signals while the STM roadmap's measure 3.2.1 plans a quality registry with 90% coverage including stage by 2029–2031. `rec:3, cty:mdt_recorded:Kymenlaakson_hyvinvointialue, nat:mdt_recorded, bs:coverage:Diagnosis, q:7885b0974f, q:950a2f797b, q:f07a34a300, q:4a856bd695, q:f540c706f8`

## Review flags (for human review only)

_Flags are for human review only; they never change the brief's status or approve it._

- [medium] `what_to_do_first.details[0]`: The cited claims for STM roadmap measure 3.1.2 state that national pathway descriptions and cancer-specific access-to-care times by 2026–2028 are planned only for five (unnamed) cancers (with all significant cancers by 2029–2031), so omitting that scope overreaches by implying general or lung-cancer target access times by 2026–2028.
- [low] `what_to_do_first.details[2]`: The cited claims state that under measure 3.2.1 annual reports for at least five cancers are planned by 2029–2031 and that the planned registry has an indicator of 90% coverage including stage, but do not state that 90% coverage will be achieved by 2029–2031.

## Claims cited

- `bs:coverage:Diagnosis` (verified locally): Pathway stage 'Diagnosis' is measured in public data: yes (by county: yes (Kuva 7, 10, 13: PNG only)) — keuhkosyoparaportti_2019_2023.html, §4.1, Taulukko 2–4, Kuva 5–13
- `bs:coverage:First_specialist_visit` (verified locally): Pathway stage 'First specialist visit' is measured in public data: partly (by county: no) — keuhkosyoparaportti_2019_2023.html, §3.1, §4.2, Taulukko 5
- `bs:coverage:Imaging` (verified locally): Pathway stage 'Imaging' is measured in public data: partly (by county: partly (Kuva 7, PNG only)) — keuhkosyoparaportti_2019_2023.html, §4.1.1, Taulukko 2, Kuva 5–7
- `bs:coverage:MDT` (verified locally): Pathway stage 'MDT' is measured in public data: partly (by county: yes (Taulukko 11)) — keuhkosyoparaportti_2019_2023.html, §3.3, §4.2, Taulukko 5, 10, 11, 13
- `bs:coverage:Primary_care_occupational_health` (verified locally): Pathway stage 'Primary care / occupational health' is measured in public data: no (by county: no) — keuhkosyoparaportti_2019_2023.html, §3.3
- `bs:coverage:Referral` (verified locally): Pathway stage 'Referral' is measured in public data: no (by county: no) — keuhkosyoparaportti_2019_2023.html, whole report (no relevant data found)
- `bs:coverage:Symptoms` (verified locally): Pathway stage 'Symptoms' is measured in public data: no (by county: no) — keuhkosyoparaportti_2019_2023.html, whole report (no relevant data found)
- `bs:coverage:Treatment_start` (verified locally): Pathway stage 'Treatment start' is measured in public data: partly (by county: yes (type only, Taulukko 11)) — keuhkosyoparaportti_2019_2023.html, §4.2, §4.2.2, Taulukko 6–9, 11, 12, Kuva 14, 17
- `cty:curative:Kymenlaakson_hyvinvointialue` (verified locally): Kymenlaakson hyvinvointialue: curative treatment 19.3% (95% CI 16.3–22.7; n=114/591), below vs national 27.0% — keuhkosyoparaportti_2019_2023.html, Taulukko 11
- `cty:life_prolonging:Kymenlaakson_hyvinvointialue` (verified locally): Kymenlaakson hyvinvointialue: life-prolonging treatment 37.6% (95% CI 33.8–41.5; n=222/591), above vs national 30.4% — keuhkosyoparaportti_2019_2023.html, Taulukko 11
- `cty:mdt_recorded:Kymenlaakson_hyvinvointialue` (verified locally): Kymenlaakson hyvinvointialue: MDT meeting recorded 0.5% (95% CI 0.2–1.5; n=3/591), below vs national 6.0% — keuhkosyoparaportti_2019_2023.html, Taulukko 11
- `cty:no_treatment_record:Kymenlaakson_hyvinvointialue` (verified locally): Kymenlaakson hyvinvointialue: no treatment record within 12 months 16.4% (95% CI 13.7–19.6; n=97/591), below vs national 27.5% — keuhkosyoparaportti_2019_2023.html, Taulukko 11
- `cty:symptomatic:Kymenlaakson_hyvinvointialue` (verified locally): Kymenlaakson hyvinvointialue: symptomatic treatment 51.3% (95% CI 47.2–55.3; n=303/591), above vs national 39.5% — keuhkosyoparaportti_2019_2023.html, Taulukko 11
- `k16:curative:men:Kymenlaakson_hyvinvointialue` (verified locally): Kymenlaakson hyvinvointialue: age-adjusted curative treatment share, men, 17.9% (95% CI 13.9–22.9) — keuhkosyoparaportti_2019_2023.html, Kuva 16
- `k16:curative:men:national` (verified locally): Finland (national reference line): age-adjusted curative treatment share, men, 26.7% — keuhkosyoparaportti_2019_2023.html, Kuva 16
- `k16:curative:women:Kymenlaakson_hyvinvointialue` (verified locally): Kymenlaakson hyvinvointialue: age-adjusted curative treatment share, women, 22.6% (95% CI 16.8–29.3) — keuhkosyoparaportti_2019_2023.html, Kuva 16
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
- `q:4a856bd695` (verified locally): the registry's data, including stage, allows reliable assessment and comparison of quality and effectiveness, with 90% data coverage — roadmap_2026_2031_fi.pdf, p.60
- `q:5eb155decc` (verified locally): Report evidence for pathway stage 'Imaging' — keuhkosyoparaportti_2019_2023.html, §4.1.1 Toteamistapa
- `q:614febebf2` (verified locally): When (p.24): > “Väliarvio toteutetaan vuonna 2030, ohjelman puolivälissä ja loppuarviointi vuonna 2036. Eri > osa-alueiden suositukset toteutetaan ennen väliarviointia.” — filha_lung_programme_2026_fi.pdf, p.24
- `q:7885b0974f` (verified locally): Report evidence for pathway stage 'Diagnosis' — keuhkosyoparaportti_2019_2023.html, §4.1.3 Levinneisyystiedon kattavuus
- `q:8f358a9de6` (verified locally): p.16: > “Tämän ohjelman yhtenä toimenpiteenä tuotetaan kansallinen suositus keuhkosyöpien diagnostiikasta. Se > sisältää myös lähetekriteerit perusterveydenhuollolle ja suositellut aikarajat erikoissairaanhoitoon > eri diagnostiikan polun vaiheille.” — filha_lung_programme_2026_fi.pdf, p.16
- `q:950a2f797b` (verified locally): Reporting, collection and storage of lung cancer data is currently incomplete. — filha_lung_programme_2026_fi.pdf, p.21
- `q:abcbb06ae3` (verified locally): 2026–2028: guidance on a named doctor, nurse or specialist worker coordinating cancer care. 2029–2031: wellbeing services counties have adopted it. — roadmap_2026_2031_fi.pdf, p.32
- `q:b326e35410` (verified locally): National pathways with “syöpäkohtaiset hoitoonpääsyajat” for five (unnamed) cancers in 2026–2028, Nordic model — roadmap_2026_2031_fi.pdf, p.57
- `q:def306014c` (verified locally): p.57, timetable: > “2026–2028: Kansalliset hoitoketjukuvaukset tehty viidestä syövästä ja syöpäkohtaiset > hoitoonpääsyajat on määritetty.” — roadmap_2026_2031_fi.pdf, p.57
- `q:ed87906241` (verified locally): p.56, heading: > “Toimenpide 3.1.2 Laaditaan syöpäkohtaiset hoitoketjukuvaukset, ja niiden pohjalta sovelletut > alueelliset hoitoketjut, sekä mekanismi niiden ylläpitoon ja hallintaan” — roadmap_2026_2031_fi.pdf, p.56
- `q:f07a34a300` (verified locally): A national cancer care quality registry will be set up alongside THL's Cancer Registry. — roadmap_2026_2031_fi.pdf, p.59
- `q:f540c706f8` (verified locally): A national quality registry is planned; indicator: data incl. stage (“ml. levinneisyystieto”) at 90% coverage — roadmap_2026_2031_fi.pdf, p.60
- `q:fc81032a80` (verified locally): Measure 1.2.3: Create an operating model and guidance for a named worker responsible for coordinating cancer care. — roadmap_2026_2031_fi.pdf, p.32
- `rec:1` (recommendation (ours)): Team recommendation 1: Counties report access times using the THL 21/2016 definitions, with handover alerts. Each wellbeing services county reports lung cancer access times (referral → first specialist visit → diagnosis → treatment start) using the definitions in THL's Hoitoonpääsyn seuranta syövän hoidossa (Ohjaus 21/2016). Until national target times exist, flag stalled handovers. — recommendations.md, §1. Counties report access times using the THL 21/2016 definitions, with handover alerts
- `rec:2` (recommendation (ours)): Team recommendation 2: A KYS-style referral template, a persistent-symptoms rule and a named contact. Adopt a standard referral content list and template, modelled on KYS. • Add a rule for primary care: if symptoms persist after a normal X-ray, refer for a pulmonologist assessment. • Name a contact person for the diagnostic phase, from referral to diagnosis. — recommendations.md, §2. A KYS-style referral template, a persistent-symptoms rule and a named contact
- `rec:3` (recommendation (ours)): Team recommendation 3: Report recording completeness per county: stage, drug treatment, MDT coding. Publish, per county, how completely stage, drug treatment and MDT meetings are recorded. Read county ‘gaps’ in these fields as data-quality signals first. — recommendations.md, §3. Report recording completeness per county: stage, drug treatment, MDT coding
- `thl:21_2016` (verified by Hellu): THL Ohjaus 21/2016 defines how cancer access times are recorded, for 16 cancers — pathway_brief.md, 6. Regional pathways compared
