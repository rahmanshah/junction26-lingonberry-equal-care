# Keski-Uusimaa: lung cancer pathway brief

Status: **validated** · gemini-4-argon (thinking HIGH) · 2026-11-14T12:49:27+00:00 · attempts: 1

## Where do we lag?

**In crude county shares, Keski-Uusimaa lags the national benchmark only in recorded MDT meetings at 0.0% (95% CI 0.0–0.8; n=0/481) versus 6.0% (893/14873) nationally.** `cty:mdt_recorded:Keski_Uudenmaan_hyvinvointialue, nat:mdt_recorded`

- The 95% confidence interval for the crude MDT meeting share of 0.0% (95% CI 0.0–0.8; n=0/481) excludes the national 6.0% (893/14873), though HILMO MDT codes WZC15/WZC20 are entered only from direct patient contacts and measure recording practice, not care. `cty:mdt_recorded:Keski_Uudenmaan_hyvinvointialue, nat:mdt_recorded, bs:coverage:MDT, q:39e6ba43a9`
- In overlapping treatment categories where a patient can have several treatments, Keski-Uusimaa's crude curative treatment share is 33.7% (95% CI 29.6–38.0; n=162/481), whose 95% confidence interval excludes and lies above the national 27.0% (4009/14873). `cty:curative:Keski_Uudenmaan_hyvinvointialue, nat:curative`
- Across the other overlapping treatment categories, crude life-prolonging treatment is 28.9% (95% CI 25.0–33.1; n=139/481) versus 30.4% (4522/14873) nationally and crude symptomatic treatment is 39.5% (95% CI 35.2–43.9; n=190/481) versus 39.5% (5871/14873) nationally, with 95% confidence intervals that include the national values. `cty:life_prolonging:Keski_Uudenmaan_hyvinvointialue, nat:life_prolonging, cty:symptomatic:Keski_Uudenmaan_hyvinvointialue, nat:symptomatic`
- The crude share with no treatment record within 12 months—which mixes untreated patients and treatment that was not recorded—is 26.4% (95% CI 22.7–30.5; n=127/481), and its 95% confidence interval includes the national 27.5% (4089/14873). `cty:no_treatment_record:Keski_Uudenmaan_hyvinvointialue, nat:no_treatment_record, bs:coverage:Treatment_start`

## How sure are we?

**A journal article shows high diagnosis concordance, but crude county treatment shares lack age and stage adjustment, and public registry data do not measure pathway waiting times.** `lit:hilmo_90, bs:coverage:Diagnosis, bs:coverage:Referral, bs:coverage:Treatment_start`

- The crude county shares have separate limitations: they are not age-adjusted (an age-adjusted value exists only from Kuva 16, for curative treatment, by sex, with digitised national reference lines at ±0.5 percentage points of 26.7% for men and 26.9% for women), and they cannot be stage-adjusted because stage at diagnosis is missing for about 48% of patients. `cty:curative:Keski_Uudenmaan_hyvinvointialue, k16:curative:men:national, k16:curative:women:national, bs:coverage:Diagnosis, q:7885b0974f`
- A journal article reports that HILMO diagnoses match the Cancer Registry for about 90% of most cancer types, concerning diagnosis concordance only and not treatment, referral or MDT recording, while Finland has no cancer quality registry and lung cancer data reporting, collection and storage are incomplete. `lit:hilmo_90, q:47c7e11303, q:950a2f797b`
- Public data do not measure symptoms or referrals, do not include outpatient primary care visits in the report's data or mention occupational health, show imaging only indirectly as clinical diagnosis in approximately 20% of patients, and record specialist visits (93.6% within 12 months, up to 3 months before diagnosis) and treatment type within 12 months without wait times. `bs:coverage:Symptoms, bs:coverage:Referral, bs:coverage:Primary_care_occupational_health, q:323de0d90d, bs:coverage:Imaging, q:5eb155decc, bs:coverage:First_specialist_visit, bs:coverage:Treatment_start`
- Preliminary, unpublished national figures show 155 days on average from symptoms to first treatment in Finland versus 107 in Sweden and 67 in Denmark (56 days patient delay, 41 days primary care, 58 days specialist care as the longest stage), while the Health Care Act sets no legal maximum time for a cancer suspicion. `mot:total_fi, mot:total_se, mot:total_dk, mot:patient, mot:primary, mot:specialist, law:no_max`

## What should we do first?

**The team recommends publishing how completely stage, drug treatment and MDT meetings are recorded, reporting access times using THL 21/2016 guidance, and standardising referrals and diagnostic-phase coordination.** `rec:1, rec:2, rec:3, thl:21_2016, reg:kys_template, q:950a2f797b`

- Given the 0.0% (95% CI 0.0–0.8; n=0/481) crude MDT share and about 48% missing stage nationally, the team recommends publishing per county how completely stage, drug treatment and MDT meetings are recorded—reading gaps as data-quality signals first—while STM roadmap measure 3.2.1 plans a national cancer quality registry (decree updated by 2026–2028; annual reports by 2029–2031 at 90% coverage). `rec:3, cty:mdt_recorded:Keski_Uudenmaan_hyvinvointialue, bs:coverage:Diagnosis, q:f07a34a300, q:4a856bd695, q:950a2f797b`
- Because Finland lacks a national system monitoring access to care, the team recommends reporting referral-to-treatment access times using THL guidance Ohjaus 21/2016 definitions for 16 cancers and flagging stalled handovers while STM roadmap measure 3.1.2 plans national cancer-specific pathway descriptions and access times by 2026–2028 and for all significant cancers by 2029–2031. `rec:1, thl:21_2016, q:4e702a20fe, q:ccda20dce9, q:ed87906241, q:def306014c, q:b326e35410`
- As mentor insight notes a weak referral gets a lower urgency rating and regional pathway documents show only KYS provides a referral template and a clear-X-ray persistent-symptoms rule, the team recommends adopting that template and rule while the Filha programme's diagnostics recommendation (referral criteria and time limits) is to be carried out before the 2030 mid-term evaluation. `rec:2, mentor:kaisa_referral, reg:kys_template, reg:kys_persistent, reg:only_kys_xray, q:29b792498e, q:8f358a9de6, q:614febebf2`
- Because no reviewed regional pathway document names a diagnostic-phase contact person, the team recommends naming a contact from referral to diagnosis while STM roadmap measure 1.2.3 plans guidance on a named care-coordinator model by 2026–2028, which counties adopt by 2029–2031, with the care phase not specified. `rec:2, reg:named_contact, q:fc81032a80, q:abcbb06ae3, q:050ee09ebe`

## Review flags (for human review only)

_Flags are for human review only; they never change the brief's status or approve it._

- [medium] `where_we_lag.headline`: The claim that Keski-Uusimaa lags the national benchmark only in recorded MDT meetings is not supported by the two cited claims, which cover only MDT recording and provide no information about other treatment categories or indicators.
- [medium] `how_sure_are_we.headline`: None of the cited claims mention age adjustment or that county treatment shares are crude, and bs:coverage:Diagnosis states only that curative shares cannot be stage-adjusted rather than all treatment shares.
- [low] `what_to_do_first.details[1]`: Omits that the 2026–2028 milestone in STM roadmap measure 3.1.2 covers only five unnamed cancers, which makes the 2026–2028 target appear broader than the cited claims support.
- [medium] `what_to_do_first.details[2]`: Stating that regional pathway documents show only KYS provides these features omits the scope caveat in reg:only_kys_xray that only 5 regional pathways were reviewed, not all 22 areas.

## Claims cited

- `bs:coverage:Diagnosis` (verified locally): Pathway stage 'Diagnosis' is measured in public data: yes (by county: yes (Kuva 7, 10, 13: PNG only)) — keuhkosyoparaportti_2019_2023.html, §4.1, Taulukko 2–4, Kuva 5–13
- `bs:coverage:First_specialist_visit` (verified locally): Pathway stage 'First specialist visit' is measured in public data: partly (by county: no) — keuhkosyoparaportti_2019_2023.html, §3.1, §4.2, Taulukko 5
- `bs:coverage:Imaging` (verified locally): Pathway stage 'Imaging' is measured in public data: partly (by county: partly (Kuva 7, PNG only)) — keuhkosyoparaportti_2019_2023.html, §4.1.1, Taulukko 2, Kuva 5–7
- `bs:coverage:MDT` (verified locally): Pathway stage 'MDT' is measured in public data: partly (by county: yes (Taulukko 11)) — keuhkosyoparaportti_2019_2023.html, §3.3, §4.2, Taulukko 5, 10, 11, 13
- `bs:coverage:Primary_care_occupational_health` (verified locally): Pathway stage 'Primary care / occupational health' is measured in public data: no (by county: no) — keuhkosyoparaportti_2019_2023.html, §3.3
- `bs:coverage:Referral` (verified locally): Pathway stage 'Referral' is measured in public data: no (by county: no) — keuhkosyoparaportti_2019_2023.html, whole report (no relevant data found)
- `bs:coverage:Symptoms` (verified locally): Pathway stage 'Symptoms' is measured in public data: no (by county: no) — keuhkosyoparaportti_2019_2023.html, whole report (no relevant data found)
- `bs:coverage:Treatment_start` (verified locally): Pathway stage 'Treatment start' is measured in public data: partly (by county: yes (type only, Taulukko 11)) — keuhkosyoparaportti_2019_2023.html, §4.2, §4.2.2, Taulukko 6–9, 11, 12, Kuva 14, 17
- `cty:curative:Keski_Uudenmaan_hyvinvointialue` (verified locally): Keski-Uudenmaan hyvinvointialue: curative treatment 33.7% (95% CI 29.6–38.0; n=162/481), above vs national 27.0% — keuhkosyoparaportti_2019_2023.html, Taulukko 11
- `cty:life_prolonging:Keski_Uudenmaan_hyvinvointialue` (verified locally): Keski-Uudenmaan hyvinvointialue: life-prolonging treatment 28.9% (95% CI 25.0–33.1; n=139/481), not distinguishable vs national 30.4% — keuhkosyoparaportti_2019_2023.html, Taulukko 11
- `cty:mdt_recorded:Keski_Uudenmaan_hyvinvointialue` (verified locally): Keski-Uudenmaan hyvinvointialue: MDT meeting recorded 0.0% (95% CI 0.0–0.8; n=0/481), below vs national 6.0% — keuhkosyoparaportti_2019_2023.html, Taulukko 11
- `cty:no_treatment_record:Keski_Uudenmaan_hyvinvointialue` (verified locally): Keski-Uudenmaan hyvinvointialue: no treatment record within 12 months 26.4% (95% CI 22.7–30.5; n=127/481), not distinguishable vs national 27.5% — keuhkosyoparaportti_2019_2023.html, Taulukko 11
- `cty:symptomatic:Keski_Uudenmaan_hyvinvointialue` (verified locally): Keski-Uudenmaan hyvinvointialue: symptomatic treatment 39.5% (95% CI 35.2–43.9; n=190/481), not distinguishable vs national 39.5% — keuhkosyoparaportti_2019_2023.html, Taulukko 11
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
- `q:29b792498e` (verified locally): Policy evidence for pathway stage 'Referral' — filha_lung_programme_2026_fi.pdf, p.16
- `q:323de0d90d` (verified locally): Report evidence for pathway stage 'Primary care / occupational health' — keuhkosyoparaportti_2019_2023.html, §3.3 Menetelmät
- `q:39e6ba43a9` (verified locally): Report evidence for pathway stage 'MDT' — keuhkosyoparaportti_2019_2023.html, §3.3 Menetelmät
- `q:47c7e11303` (verified locally): Finland has no quality registry for lung cancer or for any other cancer. — filha_lung_programme_2026_fi.pdf, p.21
- `q:4a856bd695` (verified locally): the registry's data, including stage, allows reliable assessment and comparison of quality and effectiveness, with 90% data coverage — roadmap_2026_2031_fi.pdf, p.60
- `q:4e702a20fe` (verified locally): Finland has no unified national system to steer the drafting of cancer-specific treatment recommendations, or the implementation and monitoring of care pathways based on them (quality and effectiveness targets/indicators, including access to care, and cancer-specific and generic PROMs). Existing recommendations and pathways, and the targets and indicators to be monitored, are not coordinated nationally. This maintains regional inequality in the availability and effectiveness of cancer care. — strategy_2026_2035_fi.pdf, p.33
- `q:5eb155decc` (verified locally): Report evidence for pathway stage 'Imaging' — keuhkosyoparaportti_2019_2023.html, §4.1.1 Toteamistapa
- `q:614febebf2` (verified locally): When (p.24): > “Väliarvio toteutetaan vuonna 2030, ohjelman puolivälissä ja loppuarviointi vuonna 2036. Eri > osa-alueiden suositukset toteutetaan ennen väliarviointia.” — filha_lung_programme_2026_fi.pdf, p.24
- `q:7885b0974f` (verified locally): Report evidence for pathway stage 'Diagnosis' — keuhkosyoparaportti_2019_2023.html, §4.1.3 Levinneisyystiedon kattavuus
- `q:8f358a9de6` (verified locally): p.16: > “Tämän ohjelman yhtenä toimenpiteenä tuotetaan kansallinen suositus keuhkosyöpien diagnostiikasta. Se > sisältää myös lähetekriteerit perusterveydenhuollolle ja suositellut aikarajat erikoissairaanhoitoon > eri diagnostiikan polun vaiheille.” — filha_lung_programme_2026_fi.pdf, p.16
- `q:950a2f797b` (verified locally): Reporting, collection and storage of lung cancer data is currently incomplete. — filha_lung_programme_2026_fi.pdf, p.21
- `q:abcbb06ae3` (verified locally): 2026–2028: guidance on a named doctor, nurse or specialist worker coordinating cancer care. 2029–2031: wellbeing services counties have adopted it. — roadmap_2026_2031_fi.pdf, p.32
- `q:b326e35410` (verified locally): National pathways with “syöpäkohtaiset hoitoonpääsyajat” for five (unnamed) cancers in 2026–2028, Nordic model — roadmap_2026_2031_fi.pdf, p.57
- `q:ccda20dce9` (verified locally): Finland has no national system steering cancer pathways or their monitoring, “mukaan lukien hoitoonpääsy” — strategy_2026_2035_fi.pdf, p.33
- `q:def306014c` (verified locally): p.57, timetable: > “2026–2028: Kansalliset hoitoketjukuvaukset tehty viidestä syövästä ja syöpäkohtaiset > hoitoonpääsyajat on määritetty.” — roadmap_2026_2031_fi.pdf, p.57
- `q:ed87906241` (verified locally): p.56, heading: > “Toimenpide 3.1.2 Laaditaan syöpäkohtaiset hoitoketjukuvaukset, ja niiden pohjalta sovelletut > alueelliset hoitoketjut, sekä mekanismi niiden ylläpitoon ja hallintaan” — roadmap_2026_2031_fi.pdf, p.56
- `q:f07a34a300` (verified locally): A national cancer care quality registry will be set up alongside THL's Cancer Registry. — roadmap_2026_2031_fi.pdf, p.59
- `q:fc81032a80` (verified locally): Measure 1.2.3: Create an operating model and guidance for a named worker responsible for coordinating cancer care. — roadmap_2026_2031_fi.pdf, p.32
- `rec:1` (recommendation (ours)): Team recommendation 1: Counties report access times using the THL 21/2016 definitions, with handover alerts. Each wellbeing services county reports lung cancer access times (referral → first specialist visit → diagnosis → treatment start) using the definitions in THL's Hoitoonpääsyn seuranta syövän hoidossa (Ohjaus 21/2016). Until national target times exist, flag stalled handovers. — recommendations.md, §1. Counties report access times using the THL 21/2016 definitions, with handover alerts
- `rec:2` (recommendation (ours)): Team recommendation 2: A KYS-style referral template, a persistent-symptoms rule and a named contact. Adopt a standard referral content list and template, modelled on KYS. • Add a rule for primary care: if symptoms persist after a normal X-ray, refer for a pulmonologist assessment. • Name a contact person for the diagnostic phase, from referral to diagnosis. — recommendations.md, §2. A KYS-style referral template, a persistent-symptoms rule and a named contact
- `rec:3` (recommendation (ours)): Team recommendation 3: Report recording completeness per county: stage, drug treatment, MDT coding. Publish, per county, how completely stage, drug treatment and MDT meetings are recorded. Read county ‘gaps’ in these fields as data-quality signals first. — recommendations.md, §3. Report recording completeness per county: stage, drug treatment, MDT coding
- `reg:kys_persistent` (verified by Hellu): KYS: refer persistent unexplained symptoms even if the X-ray is clear — pathway_brief.md, 6. Regional pathways compared
- `reg:kys_template` (verified by Hellu): Only KYS lists required referral content and provides a referral template — pathway_brief.md, 6. Regional pathways compared
- `reg:named_contact` (verified by Hellu): No region names a contact person for the diagnostic phase — pathway_brief.md, 6. Regional pathways compared
- `reg:only_kys_xray` (verified by Hellu): Only KYS tells primary care what to do with a normal X-ray and continuing symptoms — pathway_brief.md, 6. Regional pathways compared
- `thl:21_2016` (verified by Hellu): THL Ohjaus 21/2016 defines how cancer access times are recorded, for 16 cancers — pathway_brief.md, 6. Regional pathways compared
