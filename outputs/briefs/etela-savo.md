# Etelä-Savo: lung cancer pathway brief

Status: **validated** · gemini-4-argon (thinking HIGH) · 2026-11-14T12:07:56+00:00 · attempts: 1

## Where do we lag?

**Etelä-Savo lags in crude MDT recording at 0.2% (95% CI 0.0–1.2) versus 6.0% nationally, while crude curative treatment is 23.4% (95% CI 19.8–27.6) versus 27.0%.** `cty:mdt_recorded:Etelä_Savon_hyvinvointialue, nat:mdt_recorded, cty:curative:Etelä_Savon_hyvinvointialue, nat:curative`

- In Etelä-Savo, the crude curative treatment share is 23.4% (95% CI 19.8–27.6; n=105/448) alongside the national value of 27.0% (4009/14873), meaning the 95% confidence interval includes the national value. `cty:curative:Etelä_Savon_hyvinvointialue, nat:curative`
- Overlapping treatment categories—where a patient can receive several treatments—show higher crude shares than national values for life-prolonging treatment at 36.4% (95% CI 32.1–40.9; n=163/448) versus 30.4% (4522/14873) and symptomatic treatment at 46.2% (95% CI 41.6–50.8; n=207/448) versus 39.5% (5871/14873), with 95% confidence intervals excluding the national values. `cty:life_prolonging:Etelä_Savon_hyvinvointialue, nat:life_prolonging, cty:symptomatic:Etelä_Savon_hyvinvointialue, nat:symptomatic`
- The crude share with an MDT meeting recorded is 0.2% (95% CI 0.0–1.2; n=1/448) versus 6.0% (893/14873) nationally, with the 95% confidence interval excluding the national value, although HILMO procedure codes only capture direct patient contacts and therefore measure recording practice rather than care. `cty:mdt_recorded:Etelä_Savon_hyvinvointialue, nat:mdt_recorded, bs:coverage:MDT, q:39e6ba43a9`
- The crude share with no treatment record within 12 months—which mixes untreated patients and unrecorded treatment—is 23.2% (95% CI 19.5–27.3; n=104/448) versus 27.5% (4089/14873) nationally, with the 95% confidence interval excluding the national value. `cty:no_treatment_record:Etelä_Savon_hyvinvointialue, nat:no_treatment_record, bs:coverage:Treatment_start`

## How sure are we?

**Public registry data lack stage at diagnosis for many patients, preventing stage adjustment, and do not measure county wait times from symptoms, primary care, or referral to treatment start.** `bs:coverage:Diagnosis, q:7885b0974f, bs:coverage:Symptoms, bs:coverage:Primary_care_occupational_health, bs:coverage:Referral, bs:coverage:Treatment_start`

- As an inference rather than a finding, Etelä-Savo's crude 23.2% (95% CI 19.5–27.3; n=104/448) share with no treatment record within 12 months—below 27.5% (4089/14873) nationally—acts as a data-quality signal consistent with relatively complete treatment recording (not direct evidence of it), so the crude 23.4% (95% CI 19.8–27.6; n=105/448) curative share is less likely to be only a recording artefact. `cty:no_treatment_record:Etelä_Savon_hyvinvointialue, nat:no_treatment_record, cty:curative:Etelä_Savon_hyvinvointialue`
- A journal article read by a teammate found HILMO diagnoses match the Cancer Registry for about 90% of most cancer types (covering diagnosis concordance only, not treatments), while county treatment shares are crude—unadjusted for age or stage—and Kuva 16 provides only digitised national age-adjusted curative reference lines (about ±0.5 percentage points) of 26.7% for men and 26.9% for women. `lit:hilmo_90, bs:coverage:Diagnosis, q:7885b0974f, k16:curative:men:national, k16:curative:women:national`
- In the national report, outpatient primary care visits are not included in the data, occupational health is not mentioned, imaging appears only partly as the diagnostic basis in approximately 20% of cases, and county-level timestamps for symptoms, referrals, first specialist visits, and treatment start are absent. `bs:coverage:Symptoms, bs:coverage:Primary_care_occupational_health, q:323de0d90d, bs:coverage:Imaging, q:5eb155decc, bs:coverage:Referral, bs:coverage:First_specialist_visit, bs:coverage:Treatment_start`
- Preliminary, unpublished national figures show 155 days on average from symptoms to treatment in Finland (versus 107 in Sweden and 67 in Denmark), including 56 days of patient delay, 41 days in primary care, and 58 days in specialist care, while mentor insight notes weak referrals lower specialist urgency ratings and occupational health reaches specialist care faster. `mot:total_fi, mot:total_se, mot:total_dk, mot:patient, mot:primary, mot:specialist, mentor:kaisa_referral, mentor:hanna_occupational`

## What should we do first?

**The team recommends reporting access times using THL 21/2016 definitions with handover alerts, standardising referrals with a named diagnostic contact, and auditing MDT, stage, and drug recording completeness.** `rec:1, rec:2, rec:3, thl:21_2016, q:950a2f797b`

- The team recommends reporting access times (referral to first specialist visit, diagnosis, and treatment start) using THL Ohjaus 21/2016 definitions for 16 cancers and flagging stalled handovers, as the Health Care Act sets no maximum time for cancer suspicion, roadmap pathway target times are planned for 2026–2028, and Filha's diagnostics recommendation is due before the 2030 evaluation. `rec:1, thl:21_2016, law:no_max, q:24169121a4, q:ccda20dce9, q:def306014c, q:b326e35410, q:20d6ca414e, q:432c0e51d6, q:614febebf2`
- The team recommends a standard referral template, a primary-care rule referring persistent symptoms after a normal X-ray to a pulmonologist, and a named diagnostic contact, since referrals follow local instructions, mentor insight notes weak referrals lower urgency ratings, and national referral criteria and coordinator guidance are only planned for 2026–2028 (with county adoption in 2029–2031). `rec:2, q:556431a0c2, q:1b9eaf2217, mentor:kaisa_referral, q:37bb4c3b38, q:0780bf74b0, q:c61439b30f, q:29b792498e, q:fc81032a80, q:abcbb06ae3, q:050ee09ebe`
- Given Etelä-Savo's crude MDT recording share of 0.2% (95% CI 0.0–1.2; n=1/448) versus 6.0% (893/14873) nationally and incomplete national stage data, the team recommends publishing county recording completeness for stage, drug treatment, and MDT coding as data-quality signals while a national quality registry (targeting 90% coverage including stage) is planned alongside THL's Cancer Registry. `rec:3, cty:mdt_recorded:Etelä_Savon_hyvinvointialue, nat:mdt_recorded, bs:coverage:MDT, q:7885b0974f, q:950a2f797b, q:82d365cd2c, q:47c7e11303, q:f07a34a300, q:4a856bd695, q:f540c706f8, q:990a0d39a0`

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
- `cty:curative:Etelä_Savon_hyvinvointialue` (verified locally): Etelä-Savon hyvinvointialue: curative treatment 23.4% (95% CI 19.8–27.6; n=105/448), not distinguishable vs national 27.0% — keuhkosyoparaportti_2019_2023.html, Taulukko 11
- `cty:life_prolonging:Etelä_Savon_hyvinvointialue` (verified locally): Etelä-Savon hyvinvointialue: life-prolonging treatment 36.4% (95% CI 32.1–40.9; n=163/448), above vs national 30.4% — keuhkosyoparaportti_2019_2023.html, Taulukko 11
- `cty:mdt_recorded:Etelä_Savon_hyvinvointialue` (verified locally): Etelä-Savon hyvinvointialue: MDT meeting recorded 0.2% (95% CI 0.0–1.2; n=1/448), below vs national 6.0% — keuhkosyoparaportti_2019_2023.html, Taulukko 11
- `cty:no_treatment_record:Etelä_Savon_hyvinvointialue` (verified locally): Etelä-Savon hyvinvointialue: no treatment record within 12 months 23.2% (95% CI 19.5–27.3; n=104/448), below vs national 27.5% — keuhkosyoparaportti_2019_2023.html, Taulukko 11
- `cty:symptomatic:Etelä_Savon_hyvinvointialue` (verified locally): Etelä-Savon hyvinvointialue: symptomatic treatment 46.2% (95% CI 41.6–50.8; n=207/448), above vs national 39.5% — keuhkosyoparaportti_2019_2023.html, Taulukko 11
- `k16:curative:men:national` (verified locally): Finland (national reference line): age-adjusted curative treatment share, men, 26.7% — keuhkosyoparaportti_2019_2023.html, Kuva 16
- `k16:curative:women:national` (verified locally): Finland (national reference line): age-adjusted curative treatment share, women, 26.9% — keuhkosyoparaportti_2019_2023.html, Kuva 16
- `law:no_max` (verified by Hellu): There is no legal maximum time for a cancer suspicion — pathway_brief.md, 5. What the law guarantees (Health Care Act, §52)
- `lit:hilmo_90` (verified by Hellu): HILMO diagnoses match the Cancer Registry for about 90% of most cancer types — pathway_brief.md, 6. Regional pathways compared
- `mentor:hanna_occupational` (mentor insight): Occupational health gets patients to specialist care faster — pathway_brief.md, 7. Where patients get stuck
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
- `q:0780bf74b0` (verified locally): Policy evidence for pathway stage 'Symptoms' — roadmap_2026_2031_fi.pdf, p.52; p.53
- `q:1b9eaf2217` (verified locally): - Diagnostic speed (“diagnoosin nopeudessa”): verified. - Surgery volumes (“leikkauksien määrässä”): verified. - ‘Referral organisation’ is not what it says. The phrase “hoitovastuun järjestämisessä” means the organisation of care responsibility (who holds responsibility for treatment). - Referral i — filha_lung_programme_2026_fi.pdf, p.4
- `q:20d6ca414e` (verified locally): “Valtakunnallisesti ei ole ollut tarkkaa yhtenäistä ohjeistusta siitä, millä aikataululla diagnostiikan eri osa-alueet tulisi olla tehtyinä”; regional variation in diagnostic speed is large. The programme itself sets no day-based targets — filha_lung_programme_2026_fi.pdf, p.4
- `q:24169121a4` (verified locally): Strategy p.5 (= PDF p.5), “Strategiset tavoitteet”, indicator under “Varmistetaan yhdenvertainen ja vaikuttava syövänhoito”: > “Potilaat pääsevät hoitoon tavoiteaikojen puitteissa” > “ THL (Ohjaus 21/2016). Hoitoonpääsyn seuranta syövän hoidossa.” — strategy_2026_2035_fi.pdf, p.5
- `q:29b792498e` (verified locally): Policy evidence for pathway stage 'Referral' — filha_lung_programme_2026_fi.pdf, p.16
- `q:323de0d90d` (verified locally): Report evidence for pathway stage 'Primary care / occupational health' — keuhkosyoparaportti_2019_2023.html, §3.3 Menetelmät
- `q:37bb4c3b38` (verified locally): Policy evidence for pathway stage 'Referral' — roadmap_2026_2031_fi.pdf, p.52; p.106
- `q:39e6ba43a9` (verified locally): Report evidence for pathway stage 'MDT' — keuhkosyoparaportti_2019_2023.html, §3.3 Menetelmät
- `q:432c0e51d6` (verified locally): The upcoming national diagnostics recommendation will include “suositellut aikarajat erikoissairaanhoitoon eri diagnostiikan polun vaiheille” (recommended time limits in specialist care), due before the 2030 mid-term evaluation — filha_lung_programme_2026_fi.pdf, p.16
- `q:47c7e11303` (verified locally): Finland has no quality registry for lung cancer or for any other cancer. — filha_lung_programme_2026_fi.pdf, p.21
- `q:4a856bd695` (verified locally): the registry's data, including stage, allows reliable assessment and comparison of quality and effectiveness, with 90% data coverage — roadmap_2026_2031_fi.pdf, p.60
- `q:556431a0c2` (verified locally): the patient is referred to specialist care according to local instructions — filha_lung_programme_2026_fi.pdf, p.15
- `q:5eb155decc` (verified locally): Report evidence for pathway stage 'Imaging' — keuhkosyoparaportti_2019_2023.html, §4.1.1 Toteamistapa
- `q:614febebf2` (verified locally): When (p.24): > “Väliarvio toteutetaan vuonna 2030, ohjelman puolivälissä ja loppuarviointi vuonna 2036. Eri > osa-alueiden suositukset toteutetaan ennen väliarviointia.” — filha_lung_programme_2026_fi.pdf, p.24
- `q:7885b0974f` (verified locally): Report evidence for pathway stage 'Diagnosis' — keuhkosyoparaportti_2019_2023.html, §4.1.3 Levinneisyystiedon kattavuus
- `q:82d365cd2c` (verified locally): “Tällä hetkellä keuhkosyöpään liittyvien tietojen raportointi, kerääminen ja tallentaminen on puutteellista”; nationally uniform recording instructions (“yhtenäiset kirjaamisohjeet”) must be ensured — filha_lung_programme_2026_fi.pdf, p.21
- `q:950a2f797b` (verified locally): Reporting, collection and storage of lung cancer data is currently incomplete. — filha_lung_programme_2026_fi.pdf, p.21
- `q:990a0d39a0` (verified locally): Policy evidence for pathway stage 'MDT' — roadmap_2026_2031_fi.pdf, p.56
- `q:abcbb06ae3` (verified locally): 2026–2028: guidance on a named doctor, nurse or specialist worker coordinating cancer care. 2029–2031: wellbeing services counties have adopted it. — roadmap_2026_2031_fi.pdf, p.32
- `q:b326e35410` (verified locally): National pathways with “syöpäkohtaiset hoitoonpääsyajat” for five (unnamed) cancers in 2026–2028, Nordic model — roadmap_2026_2031_fi.pdf, p.57
- `q:c61439b30f` (verified locally): 2026–2028: standardised referral criteria and symptom-based models included in the national pathways of at least the five most common cancers. — roadmap_2026_2031_fi.pdf, p.53
- `q:ccda20dce9` (verified locally): Finland has no national system steering cancer pathways or their monitoring, “mukaan lukien hoitoonpääsy” — strategy_2026_2035_fi.pdf, p.33
- `q:def306014c` (verified locally): p.57, timetable: > “2026–2028: Kansalliset hoitoketjukuvaukset tehty viidestä syövästä ja syöpäkohtaiset > hoitoonpääsyajat on määritetty.” — roadmap_2026_2031_fi.pdf, p.57
- `q:f07a34a300` (verified locally): A national cancer care quality registry will be set up alongside THL's Cancer Registry. — roadmap_2026_2031_fi.pdf, p.59
- `q:f540c706f8` (verified locally): A national quality registry is planned; indicator: data incl. stage (“ml. levinneisyystieto”) at 90% coverage — roadmap_2026_2031_fi.pdf, p.60
- `q:fc81032a80` (verified locally): Measure 1.2.3: Create an operating model and guidance for a named worker responsible for coordinating cancer care. — roadmap_2026_2031_fi.pdf, p.32
- `rec:1` (recommendation (ours)): Team recommendation 1: Counties report access times using the THL 21/2016 definitions, with handover alerts. Each wellbeing services county reports lung cancer access times (referral → first specialist visit → diagnosis → treatment start) using the definitions in THL's Hoitoonpääsyn seuranta syövän hoidossa (Ohjaus 21/2016). Until national target times exist, flag stalled handovers. — recommendations.md, §1. Counties report access times using the THL 21/2016 definitions, with handover alerts
- `rec:2` (recommendation (ours)): Team recommendation 2: A KYS-style referral template, a persistent-symptoms rule and a named contact. Adopt a standard referral content list and template, modelled on KYS. • Add a rule for primary care: if symptoms persist after a normal X-ray, refer for a pulmonologist assessment. • Name a contact person for the diagnostic phase, from referral to diagnosis. — recommendations.md, §2. A KYS-style referral template, a persistent-symptoms rule and a named contact
- `rec:3` (recommendation (ours)): Team recommendation 3: Report recording completeness per county: stage, drug treatment, MDT coding. Publish, per county, how completely stage, drug treatment and MDT meetings are recorded. Read county ‘gaps’ in these fields as data-quality signals first. — recommendations.md, §3. Report recording completeness per county: stage, drug treatment, MDT coding
- `thl:21_2016` (verified by Hellu): THL Ohjaus 21/2016 defines how cancer access times are recorded, for 16 cancers — pathway_brief.md, 6. Regional pathways compared
