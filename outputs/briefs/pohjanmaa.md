# Pohjanmaa: lung cancer pathway brief

Status: **validated** · gemini-4-argon (thinking HIGH) · 2026-11-14T13:03:00+00:00 · attempts: 1

## Where do we lag?

**Pohjanmaa's overlapping crude treatment shares do not lag national values, but public data lack county waiting times and crude MDT recording is low.** `cty:curative:Pohjanmaan_hyvinvointialue, cty:life_prolonging:Pohjanmaan_hyvinvointialue, cty:symptomatic:Pohjanmaan_hyvinvointialue, cty:mdt_recorded:Pohjanmaan_hyvinvointialue, bs:coverage:Referral, bs:coverage:Treatment_start`

- Across overlapping treatment categories, Pohjanmaa's crude curative share is 27.8% (95% CI 23.9–32.2; n=125/449) versus 27.0% (4009/14873) nationally and crude symptomatic share is 36.1% (95% CI 31.8–40.6; n=162/449) versus 39.5% (5871/14873), each 95% confidence interval including the national value, while crude life-prolonging treatment is 43.0% (95% CI 38.5–47.6; n=193/449), whose 95% confidence interval excludes 30.4% (4522/14873) nationally. `cty:curative:Pohjanmaan_hyvinvointialue, nat:curative, cty:symptomatic:Pohjanmaan_hyvinvointialue, nat:symptomatic, cty:life_prolonging:Pohjanmaan_hyvinvointialue, nat:life_prolonging`
- Across overlapping categories, Pohjanmaa's crude share with no treatment record within 12 months—which mixes untreated patients and treatment that was not recorded—is 22.9% (95% CI 19.3–27.1; n=103/449), whose 95% confidence interval excludes and lies below 27.5% (4089/14873) nationally, while crude MDT meeting recording—measuring recording practice, not care—is 6.9% (95% CI 4.9–9.6; n=31/449), whose 95% confidence interval includes 6.0% (893/14873) nationally. `cty:no_treatment_record:Pohjanmaan_hyvinvointialue, nat:no_treatment_record, bs:coverage:Treatment_start, cty:mdt_recorded:Pohjanmaan_hyvinvointialue, nat:mdt_recorded, bs:coverage:MDT, q:39e6ba43a9`
- Public data do not measure county waiting times for symptoms, primary care, referral, specialist visits, or treatment start, whereas preliminary, unpublished national averages show lung cancer takes 155 days from symptoms to treatment in Finland versus 107 in Sweden and 67 in Denmark, with 56 days patient delay, 41 days in primary care, and 58 days in specialist care. `bs:coverage:Symptoms, bs:coverage:Primary_care_occupational_health, bs:coverage:Referral, bs:coverage:First_specialist_visit, bs:coverage:Treatment_start, mot:total_fi, mot:total_se, mot:total_dk, mot:patient, mot:primary, mot:specialist`

## How sure are we?

**Pohjanmaa's crude no-treatment-record share suggests relatively complete treatment recording as an inference, but crude county shares lack age and stage adjustment and public data omit key pathway stages.** `cty:no_treatment_record:Pohjanmaan_hyvinvointialue, nat:no_treatment_record, bs:coverage:Diagnosis, bs:coverage:Primary_care_occupational_health`

- As Pohjanmaa's crude 22.9% (95% CI 19.3–27.1; n=103/449) no-treatment-record share has a 95% confidence interval that excludes and lies below 27.5% (4089/14873) nationally, this is consistent—as an inference, not a finding—with relatively complete treatment recording (so a low curative share is less likely to be only a recording artefact), whereas a journal article's about 90% HILMO match covers diagnoses only. `cty:no_treatment_record:Pohjanmaan_hyvinvointialue, nat:no_treatment_record, bs:coverage:Treatment_start, lit:hilmo_90`
- The county shares are crude and have separate limitations: (a) they are not age-adjusted (age-adjusted values exist only from Kuva 16 for curative treatment by sex, digitised from a figure at about ±0.5 percentage points, with national reference lines of 26.7% for men and 26.9% for women); (b) they cannot be stage-adjusted because stage at diagnosis is missing for about 48% of patients. `cty:curative:Pohjanmaan_hyvinvointialue, k16:curative:men:national, k16:curative:women:national, bs:coverage:Diagnosis, q:7885b0974f`
- In the report, primary care visits are not included in the report's data, occupational health is not mentioned, imaging appears only as clinical diagnosis basis in about 20% of patients (not imaging use or waits), HILMO shows whether a specialist visit occurred within 12 months (93.6%) but not when, and HILMO logs MDT codes only from direct patient contacts. `bs:coverage:Primary_care_occupational_health, q:323de0d90d, bs:coverage:Imaging, q:5eb155decc, bs:coverage:First_specialist_visit, bs:coverage:MDT, q:39e6ba43a9`

## What should we do first?

**The team recommends that Pohjanmaa report THL 21/2016 access times with handover alerts, standardise referrals with a diagnostic contact person, and publish stage, drug, and MDT recording completeness.** `rec:1, rec:2, rec:3`

- Because the Health Care Act sets no legal maximum time for a cancer suspicion and national access-time monitoring is lacking, the team recommends reporting access times from referral to treatment start using THL Ohjaus 21/2016 definitions (for 16 cancers) with handover alerts while the STM roadmap (measure 3.1.2) plans cancer-specific pathways and access times by 2026–2028. `rec:1, law:no_max, thl:21_2016, q:ccda20dce9, q:24169121a4, q:def306014c, q:b326e35410`
- Since mentor insight notes a weak referral gets lower urgency, the team recommends a KYS-style referral template, referring persistent symptoms after a normal X-ray (in KYS's regional pathway document), and a diagnostic contact, while the Filha programme's diagnostics recommendation is to be carried out before the 2030 mid-term evaluation and the STM roadmap plans referral criteria (measure 2.5.2) and coordinator guidance (measure 1.2.3) by 2026–2028. `rec:2, mentor:kaisa_referral, reg:kys_template, reg:kys_persistent, reg:only_kys_xray, reg:named_contact, q:29b792498e, q:614febebf2, q:c61439b30f, q:fc81032a80, q:050ee09ebe`
- Because stage is missing for about 48% of patients and Pohjanmaa's crude MDT-recorded share—measuring recording practice, not care—is 6.9% (95% CI 4.9–9.6; n=31/449, whose 95% confidence interval includes 6.0%, 893/14873 nationally), the team recommends publishing county recording completeness for stage, drug treatment, and MDT coding while the STM roadmap (measure 3.2.1) plans a national quality registry (2026–2028 decree; 90%-coverage reports by 2029–2031). `rec:3, bs:coverage:Diagnosis, q:7885b0974f, cty:mdt_recorded:Pohjanmaan_hyvinvointialue, nat:mdt_recorded, bs:coverage:MDT, q:950a2f797b, q:82d365cd2c, q:f07a34a300, q:4a856bd695, q:f540c706f8`

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
- `cty:curative:Pohjanmaan_hyvinvointialue` (verified locally): Pohjanmaan hyvinvointialue: curative treatment 27.8% (95% CI 23.9–32.2; n=125/449), not distinguishable vs national 27.0% — keuhkosyoparaportti_2019_2023.html, Taulukko 11
- `cty:life_prolonging:Pohjanmaan_hyvinvointialue` (verified locally): Pohjanmaan hyvinvointialue: life-prolonging treatment 43.0% (95% CI 38.5–47.6; n=193/449), above vs national 30.4% — keuhkosyoparaportti_2019_2023.html, Taulukko 11
- `cty:mdt_recorded:Pohjanmaan_hyvinvointialue` (verified locally): Pohjanmaan hyvinvointialue: MDT meeting recorded 6.9% (95% CI 4.9–9.6; n=31/449), not distinguishable vs national 6.0% — keuhkosyoparaportti_2019_2023.html, Taulukko 11
- `cty:no_treatment_record:Pohjanmaan_hyvinvointialue` (verified locally): Pohjanmaan hyvinvointialue: no treatment record within 12 months 22.9% (95% CI 19.3–27.1; n=103/449), below vs national 27.5% — keuhkosyoparaportti_2019_2023.html, Taulukko 11
- `cty:symptomatic:Pohjanmaan_hyvinvointialue` (verified locally): Pohjanmaan hyvinvointialue: symptomatic treatment 36.1% (95% CI 31.8–40.6; n=162/449), not distinguishable vs national 39.5% — keuhkosyoparaportti_2019_2023.html, Taulukko 11
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
- `q:24169121a4` (verified locally): Strategy p.5 (= PDF p.5), “Strategiset tavoitteet”, indicator under “Varmistetaan yhdenvertainen ja vaikuttava syövänhoito”: > “Potilaat pääsevät hoitoon tavoiteaikojen puitteissa” > “ THL (Ohjaus 21/2016). Hoitoonpääsyn seuranta syövän hoidossa.” — strategy_2026_2035_fi.pdf, p.5
- `q:29b792498e` (verified locally): Policy evidence for pathway stage 'Referral' — filha_lung_programme_2026_fi.pdf, p.16
- `q:323de0d90d` (verified locally): Report evidence for pathway stage 'Primary care / occupational health' — keuhkosyoparaportti_2019_2023.html, §3.3 Menetelmät
- `q:39e6ba43a9` (verified locally): Report evidence for pathway stage 'MDT' — keuhkosyoparaportti_2019_2023.html, §3.3 Menetelmät
- `q:4a856bd695` (verified locally): the registry's data, including stage, allows reliable assessment and comparison of quality and effectiveness, with 90% data coverage — roadmap_2026_2031_fi.pdf, p.60
- `q:5eb155decc` (verified locally): Report evidence for pathway stage 'Imaging' — keuhkosyoparaportti_2019_2023.html, §4.1.1 Toteamistapa
- `q:614febebf2` (verified locally): When (p.24): > “Väliarvio toteutetaan vuonna 2030, ohjelman puolivälissä ja loppuarviointi vuonna 2036. Eri > osa-alueiden suositukset toteutetaan ennen väliarviointia.” — filha_lung_programme_2026_fi.pdf, p.24
- `q:7885b0974f` (verified locally): Report evidence for pathway stage 'Diagnosis' — keuhkosyoparaportti_2019_2023.html, §4.1.3 Levinneisyystiedon kattavuus
- `q:82d365cd2c` (verified locally): “Tällä hetkellä keuhkosyöpään liittyvien tietojen raportointi, kerääminen ja tallentaminen on puutteellista”; nationally uniform recording instructions (“yhtenäiset kirjaamisohjeet”) must be ensured — filha_lung_programme_2026_fi.pdf, p.21
- `q:950a2f797b` (verified locally): Reporting, collection and storage of lung cancer data is currently incomplete. — filha_lung_programme_2026_fi.pdf, p.21
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
- `reg:kys_persistent` (verified by Hellu): KYS: refer persistent unexplained symptoms even if the X-ray is clear — pathway_brief.md, 6. Regional pathways compared
- `reg:kys_template` (verified by Hellu): Only KYS lists required referral content and provides a referral template — pathway_brief.md, 6. Regional pathways compared
- `reg:named_contact` (verified by Hellu): No region names a contact person for the diagnostic phase — pathway_brief.md, 6. Regional pathways compared
- `reg:only_kys_xray` (verified by Hellu): Only KYS tells primary care what to do with a normal X-ray and continuing symptoms — pathway_brief.md, 6. Regional pathways compared
- `thl:21_2016` (verified by Hellu): THL Ohjaus 21/2016 defines how cancer access times are recorded, for 16 cancers — pathway_brief.md, 6. Regional pathways compared
