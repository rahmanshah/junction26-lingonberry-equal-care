# Kymenlaakso: lung cancer pathway brief

Status: **validated** · gemini-4-argon (thinking HIGH) · 2026-11-14T13:36:57+00:00 · attempts: 2

## Where do we lag?

**Kymenlaakso's crude curative treatment share is 19.3% (95% CI 16.3–22.7; n=114/591) versus 27.0% (4009/14873) nationally, and its 95% confidence interval excludes the national value.** `cty:curative:Kymenlaakson_hyvinvointialue, nat:curative`

- In curative shares digitised from Kuva 16 (precision ±0.5 percentage points), the gap holds after age adjustment for men at 17.9% (95% CI 13.9–22.9) versus 26.7% nationally (the 95% confidence interval excludes the national value), while for women at 22.6% (95% CI 16.8–29.3) versus 26.9% the 95% confidence interval includes it. `k16:curative:men:Kymenlaakson_hyvinvointialue, k16:curative:men:national, k16:curative:women:Kymenlaakson_hyvinvointialue, k16:curative:women:national, fig:age_adjusted_only_kuva16`
- Across overlapping treatment categories where a patient can receive several types, Kymenlaakso has higher crude shares of life-prolonging treatment at 37.6% (95% CI 33.8–41.5; n=222/591) versus 30.4% (4522/14873) nationally and symptomatic treatment at 51.3% (95% CI 47.2–55.3; n=303/591) versus 39.5% (5871/14873) nationally, with each 95% confidence interval excluding the national value. `cty:life_prolonging:Kymenlaakson_hyvinvointialue, nat:life_prolonging, cty:symptomatic:Kymenlaakson_hyvinvointialue, nat:symptomatic`
- A multidisciplinary team (MDT) meeting is recorded for a crude share of 0.5% (95% CI 0.2–1.5; n=3/591) of Kymenlaakso patients versus 6.0% (893/14873) nationally, with the 95% confidence interval excluding the national value, though HILMO MDT codes capture only direct patient contacts and measure recording practice rather than care. `cty:mdt_recorded:Kymenlaakson_hyvinvointialue, nat:mdt_recorded, bs:coverage:MDT, q:39e6ba43a9`

## How sure are we?

**Relatively complete treatment recording is a reasonable inference in Kymenlaakso, but crude county shares lack stage adjustment and public registry data do not measure pathway waiting times.** `cty:no_treatment_record:Kymenlaakson_hyvinvointialue, fig:age_adjusted_only_kuva16, bs:coverage:Diagnosis, bs:coverage:Treatment_start`

- Kymenlaakso's crude share with no treatment record within 12 months—mixing untreated patients and unrecorded treatment—is 16.4% (95% CI 13.7–19.6; n=97/591) versus 27.5% (4089/14873) nationally; its 95% confidence interval excludes the national value (entirely below it), an inference consistent with relatively complete treatment recording that makes a low curative share less likely to be only a recording artefact. `cty:no_treatment_record:Kymenlaakson_hyvinvointialue, nat:no_treatment_record, bs:coverage:Treatment_start`
- The county table's treatment shares are crude and have separate limitations: they are not age-adjusted (county-level age-adjusted shares appear only in Kuva 16 for curative treatment by sex), and separately they cannot be stage-adjusted because stage at diagnosis is missing for about 48% of patients. `fig:age_adjusted_only_kuva16, bs:coverage:Diagnosis, q:7885b0974f`
- A journal article found HILMO diagnoses match the Cancer Registry for about 90% of most cancer types (concerning diagnosis concordance only, not treatment or MDT recording), whereas public data do not measure symptom onset, referral dates, or specialist visit and treatment start dates, primary care visits are not included in the report's data, and occupational health is not mentioned. `lit:hilmo_90, bs:coverage:Symptoms, bs:coverage:Primary_care_occupational_health, q:323de0d90d, bs:coverage:Referral, bs:coverage:First_specialist_visit, bs:coverage:Treatment_start`
- Preliminary, unpublished national figures—which are national averages, not county-specific—report an average of 155 days from symptoms to treatment in Finland (56 days patient delay, 41 days in primary care, and 58 days in specialist care, the longest stage), alongside 107 days in Sweden and 67 days in Denmark. `mot:total_fi, mot:patient, mot:primary, mot:specialist, mot:total_se, mot:total_dk`

## What should we do first?

**To address Kymenlaakso's low crude curative share and MDT recording gaps, the team recommends tracking access times, standardising referrals and diagnostic coordination, and publishing recording completeness.** `rec:1, rec:2, rec:3, cty:curative:Kymenlaakson_hyvinvointialue, bs:coverage:MDT`

- The team recommends reporting access times (referral to specialist visit, diagnosis, and treatment start) using THL Ohjaus 21/2016 definitions (for 16 cancers) and flagging stalled handovers; the Health Care Act sets no maximum time for cancer suspicion, while the STM roadmap (measure 3.1.2) plans national pathway descriptions and cancer-specific access times for five cancers by 2026–2028. `rec:1, thl:21_2016, q:24169121a4, law:no_max, q:ccda20dce9, q:ed87906241, q:def306014c, q:b326e35410`
- The team recommends a KYS-modelled referral template, pulmonologist referral when symptoms persist after a normal X-ray, and a named diagnostic-phase contact; referrals currently follow local instructions, mentor insight notes weak referrals get lower specialist urgency ratings, and the Filha programme's diagnostics recommendation (primary-care referral criteria and recommended time limits) is to be carried out before the 2030 mid-term evaluation. `rec:2, q:556431a0c2, mentor:kaisa_referral, q:29b792498e, q:8f358a9de6, q:432c0e51d6, q:614febebf2`
- The team recommends publishing county recording completeness for stage, drug treatment, and MDT coding to read gaps as data-quality signals; lung cancer data reporting is incomplete and Finland has no cancer quality registry, while the STM roadmap (measure 3.2.1) plans a national quality registry with a 90% data-coverage indicator including stage. `rec:3, q:950a2f797b, q:82d365cd2c, q:47c7e11303, q:f07a34a300, q:4a856bd695, q:f540c706f8`

## Review flags (for human review only)

_Flags are for human review only; they never change the brief's status or approve it._

- none

## Claims cited

- `bs:coverage:Diagnosis` (verified locally): Pathway stage 'Diagnosis' is measured in public data: yes (by county: yes (Kuva 7, 10, 13: PNG only)) — keuhkosyoparaportti_2019_2023.html, §4.1, Taulukko 2–4, Kuva 5–13
- `bs:coverage:First_specialist_visit` (verified locally): Pathway stage 'First specialist visit' is measured in public data: partly (by county: no) — keuhkosyoparaportti_2019_2023.html, §3.1, §4.2, Taulukko 5
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
- `fig:age_adjusted_only_kuva16` (verified locally): In the 2019–2023 report, county-level age-adjusted treatment shares appear only in Kuva 16 (a PNG figure, by sex, with 95% CIs); the county table (Taulukko 11) gives crude shares only — chart_data.md, Summary table; section 'Kuva 16 in detail'
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
- `q:24169121a4` (verified locally): Strategy p.5 (= PDF p.5), “Strategiset tavoitteet”, indicator under “Varmistetaan yhdenvertainen ja vaikuttava syövänhoito”: > “Potilaat pääsevät hoitoon tavoiteaikojen puitteissa” > “ THL (Ohjaus 21/2016). Hoitoonpääsyn seuranta syövän hoidossa.” — strategy_2026_2035_fi.pdf, p.5
- `q:29b792498e` (verified locally): Policy evidence for pathway stage 'Referral' — filha_lung_programme_2026_fi.pdf, p.16
- `q:323de0d90d` (verified locally): Report evidence for pathway stage 'Primary care / occupational health' — keuhkosyoparaportti_2019_2023.html, §3.3 Menetelmät
- `q:39e6ba43a9` (verified locally): Report evidence for pathway stage 'MDT' — keuhkosyoparaportti_2019_2023.html, §3.3 Menetelmät
- `q:432c0e51d6` (verified locally): The upcoming national diagnostics recommendation will include “suositellut aikarajat erikoissairaanhoitoon eri diagnostiikan polun vaiheille” (recommended time limits in specialist care), to be carried out (“toteutetaan”; may mean produced or implemented) before the 2030 mid-term evaluation — filha_lung_programme_2026_fi.pdf, p.16
- `q:47c7e11303` (verified locally): Finland has no quality registry for lung cancer or for any other cancer. — filha_lung_programme_2026_fi.pdf, p.21
- `q:4a856bd695` (verified locally): the registry's data, including stage, allows reliable assessment and comparison of quality and effectiveness, with 90% data coverage — roadmap_2026_2031_fi.pdf, p.60
- `q:556431a0c2` (verified locally): the patient is referred to specialist care according to local instructions — filha_lung_programme_2026_fi.pdf, p.15
- `q:614febebf2` (verified locally): When (p.24): > “Väliarvio toteutetaan vuonna 2030, ohjelman puolivälissä ja loppuarviointi vuonna 2036. Eri > osa-alueiden suositukset toteutetaan ennen väliarviointia.” — filha_lung_programme_2026_fi.pdf, p.24
- `q:7885b0974f` (verified locally): Report evidence for pathway stage 'Diagnosis' — keuhkosyoparaportti_2019_2023.html, §4.1.3 Levinneisyystiedon kattavuus
- `q:82d365cd2c` (verified locally): “Tällä hetkellä keuhkosyöpään liittyvien tietojen raportointi, kerääminen ja tallentaminen on puutteellista”; nationally uniform recording instructions (“yhtenäiset kirjaamisohjeet”) must be ensured — filha_lung_programme_2026_fi.pdf, p.21
- `q:8f358a9de6` (verified locally): p.16: > “Tämän ohjelman yhtenä toimenpiteenä tuotetaan kansallinen suositus keuhkosyöpien diagnostiikasta. Se > sisältää myös lähetekriteerit perusterveydenhuollolle ja suositellut aikarajat erikoissairaanhoitoon > eri diagnostiikan polun vaiheille.” — filha_lung_programme_2026_fi.pdf, p.16
- `q:950a2f797b` (verified locally): Reporting, collection and storage of lung cancer data is currently incomplete. — filha_lung_programme_2026_fi.pdf, p.21
- `q:b326e35410` (verified locally): National pathways with “syöpäkohtaiset hoitoonpääsyajat” for five (unnamed) cancers in 2026–2028, Nordic model — roadmap_2026_2031_fi.pdf, p.57
- `q:ccda20dce9` (verified locally): Finland has no national system steering cancer pathways or their monitoring, “mukaan lukien hoitoonpääsy” — strategy_2026_2035_fi.pdf, p.33
- `q:def306014c` (verified locally): p.57, timetable: > “2026–2028: Kansalliset hoitoketjukuvaukset tehty viidestä syövästä ja syöpäkohtaiset > hoitoonpääsyajat on määritetty.” — roadmap_2026_2031_fi.pdf, p.57
- `q:ed87906241` (verified locally): p.56, heading: > “Toimenpide 3.1.2 Laaditaan syöpäkohtaiset hoitoketjukuvaukset, ja niiden pohjalta sovelletut > alueelliset hoitoketjut, sekä mekanismi niiden ylläpitoon ja hallintaan” — roadmap_2026_2031_fi.pdf, p.56
- `q:f07a34a300` (verified locally): A national cancer care quality registry will be set up alongside THL's Cancer Registry. — roadmap_2026_2031_fi.pdf, p.59
- `q:f540c706f8` (verified locally): A national quality registry is planned; indicator: data incl. stage (“ml. levinneisyystieto”) at 90% coverage — roadmap_2026_2031_fi.pdf, p.60
- `rec:1` (recommendation (ours)): Team recommendation 1: Counties report access times using the THL 21/2016 definitions, with handover alerts. Each wellbeing services county reports lung cancer access times (referral → first specialist visit → diagnosis → treatment start) using the definitions in THL's Hoitoonpääsyn seuranta syövän hoidossa (Ohjaus 21/2016). Until national target times exist, flag stalled handovers. — recommendations.md, §1. Counties report access times using the THL 21/2016 definitions, with handover alerts
- `rec:2` (recommendation (ours)): Team recommendation 2: A KYS-style referral template, a persistent-symptoms rule and a named contact. Adopt a standard referral content list and template, modelled on KYS. • Add a rule for primary care: if symptoms persist after a normal X-ray, refer for a pulmonologist assessment. • Name a contact person for the diagnostic phase, from referral to diagnosis. — recommendations.md, §2. A KYS-style referral template, a persistent-symptoms rule and a named contact
- `rec:3` (recommendation (ours)): Team recommendation 3: Report recording completeness per county: stage, drug treatment, MDT coding. Publish, per county, how completely stage, drug treatment and MDT meetings are recorded. Read county ‘gaps’ in these fields as data-quality signals first. — recommendations.md, §3. Report recording completeness per county: stage, drug treatment, MDT coding
- `thl:21_2016` (verified by Hellu): THL Ohjaus 21/2016 defines how cancer access times are recorded, for 16 cancers — pathway_brief.md, 6. Regional pathways compared
