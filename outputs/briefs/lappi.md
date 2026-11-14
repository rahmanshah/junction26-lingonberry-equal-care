# Lappi: lung cancer pathway brief

Status: **validated** · gemini-4-argon (thinking HIGH) · 2026-11-14T13:51:49+00:00 · attempts: 2

## Where do we lag?

**Lapin hyvinvointialue lags nationally in crude curative treatment at 18.5% (95% CI 15.8–21.5; n=131/710) versus 27.0% (4009/14873), with the 95% confidence interval excluding the national value.** `cty:curative:Lapin_hyvinvointialue, nat:curative`

- Across overlapping treatment categories, the crude life-prolonging treatment share is 16.1% (95% CI 13.5–18.9; n=114/710) versus 30.4% (4522/14873) nationally, while the crude symptomatic treatment share is 44.5% (95% CI 40.9–48.2; n=316/710) versus 39.5% (5871/14873), with the 95% confidence intervals excluding the national values. `cty:life_prolonging:Lapin_hyvinvointialue, nat:life_prolonging, cty:symptomatic:Lapin_hyvinvointialue, nat:symptomatic`
- The crude share with no treatment record within 12 months is 33.8% (95% CI 30.4–37.4; n=240/710) compared with 27.5% (4089/14873) nationally, with the 95% confidence interval excluding and sitting above the national value; this category mixes untreated patients and unrecorded treatment. `cty:no_treatment_record:Lapin_hyvinvointialue, nat:no_treatment_record, bs:coverage:Treatment_start`
- The crude share with an MDT meeting recorded is 3.0% (95% CI 1.9–4.5; n=21/710) versus 6.0% (893/14873) nationally, with the 95% confidence interval excluding the national value, though HILMO entries come only from direct patient contacts and measure recording practice rather than care. `cty:mdt_recorded:Lapin_hyvinvointialue, nat:mdt_recorded, bs:coverage:MDT, q:39e6ba43a9`
- Nationally, preliminary unpublished figures show lung cancer care takes 155 days on average from symptoms to treatment in Finland versus 107 days in Sweden and 67 days in Denmark, comprising 56 days of patient delay, 41 days in primary care, and 58 days in specialist care. `mot:total_fi, mot:total_se, mot:total_dk, mot:patient, mot:primary, mot:specialist`

## How sure are we?

**Public registry data leave major uncertainties because county tables report crude shares without age or stage adjustment, cannot separate unrecorded treatment from non-treatment, and omit key pathway timestamps.** `fig:age_adjusted_only_kuva16, bs:coverage:Diagnosis, bs:coverage:Treatment_start`

- Reading the crude 33.8% (95% CI 30.4–37.4; n=240/710) no-treatment-record share within 12 months—whose 95% confidence interval is above the national 27.5% (4089/14873)—as a data-quality signal indicates that low crude treatment shares may partly reflect unrecorded treatment, whereas a journal article finding about 90% HILMO and Cancer Registry concordance applies only to diagnoses. `cty:no_treatment_record:Lapin_hyvinvointialue, nat:no_treatment_record, lit:hilmo_90`
- Taulukko 11 gives crude county shares that are not age-adjusted—age-adjusted county shares appear only in Kuva 16, where only digitised national curative reference lines of 26.7% for men and 26.9% for women (±0.5 percentage points) are available here—and, as a separate limitation, shares cannot be stage-adjusted because stage at diagnosis is missing for about 48% of patients. `fig:age_adjusted_only_kuva16, k16:curative:men:national, k16:curative:women:national, bs:coverage:Diagnosis, q:7885b0974f`
- Public report data do not measure symptom onset, referrals, imaging waits (showing only that about 20% of diagnoses rest on clinical examination such as imaging alone), or dates of specialist visits and treatment start, and primary care visits are not included in the report's data while occupational health is not mentioned. `bs:coverage:Symptoms, bs:coverage:Primary_care_occupational_health, q:323de0d90d, bs:coverage:Imaging, q:5eb155decc, bs:coverage:Referral, bs:coverage:First_specialist_visit, bs:coverage:Treatment_start`

## What should we do first?

**The team recommends auditing recording completeness for stage, drug treatment, and MDT coding, reporting access times using THL 21/2016 definitions with handover alerts, and standardising referrals and diagnostic coordination.** `rec:1, rec:2, rec:3, q:950a2f797b, q:4e702a20fe`

- Given Lappi's crude 33.8% (95% CI 30.4–37.4; n=240/710) 12-month no-treatment-record share, crude 3.0% (95% CI 1.9–4.5; n=21/710) MDT-recorded share across overlapping categories, and incomplete national data reporting, the team recommends publishing county recording completeness for stage, drug treatment, and MDT coding while the STM roadmap (measure 3.2.1) plans a national quality registry with an undated 90% coverage indicator including stage. `rec:3, cty:no_treatment_record:Lapin_hyvinvointialue, cty:mdt_recorded:Lapin_hyvinvointialue, q:950a2f797b, q:82d365cd2c, q:f07a34a300, q:4a856bd695, q:f540c706f8`
- Because the Health Care Act (§52) sets no maximum time for a cancer suspicion, the team recommends reporting access times from referral to treatment start using THL guidance Ohjaus 21/2016 definitions (covering 16 cancers) and flagging stalled handovers while the STM roadmap (measure 3.1.2) plans national pathways with target access times for five cancers by 2026–2028. `rec:1, law:no_max, thl:21_2016, q:24169121a4, q:ed87906241, q:b326e35410, q:def306014c`
- Supported by mentor insight that a weak referral gets a lower urgency rating in specialist care, the team recommends a KYS-style referral template, referring persistent unexplained symptoms after a normal X-ray, and naming a diagnostic-phase contact, while the Filha programme's diagnostics recommendation with primary-care referral criteria is to be carried out before the 2030 mid-term evaluation. `rec:2, mentor:kaisa_referral, q:556431a0c2, q:29b792498e, q:8f358a9de6, q:614febebf2`
- As the team recommends, naming a diagnostic-phase contact person and standardising referrals act early while the STM roadmap plans guidance on a named care-coordinator model by 2026–2028 for county adoption by 2029–2031 without specifying the care phase (measure 1.2.3) and plans standardised referral criteria and symptom-based models by 2026–2028 (measure 2.5.2). `rec:2, q:fc81032a80, q:050ee09ebe, q:abcbb06ae3, q:0780bf74b0, q:37bb4c3b38, q:9a1cd194f5`

## Review flags (for human review only)

_Flags are for human review only; they never change the brief's status or approve it._

- [medium] `what_to_do_first.details[3]`: For STM roadmap measure 2.5.2, the cited claim notes specify that standardised referral criteria and symptom-based models are planned in the national pathways of at least the five most common cancers by 2026–2028 (and for all significant cancers by 2029–2031). Omitting this scope qualifier overstates what is planned by 2026–2028.

## Claims cited

- `bs:coverage:Diagnosis` (verified locally): Pathway stage 'Diagnosis' is measured in public data: yes (by county: yes (Kuva 7, 10, 13: PNG only)) — keuhkosyoparaportti_2019_2023.html, §4.1, Taulukko 2–4, Kuva 5–13
- `bs:coverage:First_specialist_visit` (verified locally): Pathway stage 'First specialist visit' is measured in public data: partly (by county: no) — keuhkosyoparaportti_2019_2023.html, §3.1, §4.2, Taulukko 5
- `bs:coverage:Imaging` (verified locally): Pathway stage 'Imaging' is measured in public data: partly (by county: partly (Kuva 7, PNG only)) — keuhkosyoparaportti_2019_2023.html, §4.1.1, Taulukko 2, Kuva 5–7
- `bs:coverage:MDT` (verified locally): Pathway stage 'MDT' is measured in public data: partly (by county: yes (Taulukko 11)) — keuhkosyoparaportti_2019_2023.html, §3.3, §4.2, Taulukko 5, 10, 11, 13
- `bs:coverage:Primary_care_occupational_health` (verified locally): Pathway stage 'Primary care / occupational health' is measured in public data: no (by county: no) — keuhkosyoparaportti_2019_2023.html, §3.3
- `bs:coverage:Referral` (verified locally): Pathway stage 'Referral' is measured in public data: no (by county: no) — keuhkosyoparaportti_2019_2023.html, whole report (no relevant data found)
- `bs:coverage:Symptoms` (verified locally): Pathway stage 'Symptoms' is measured in public data: no (by county: no) — keuhkosyoparaportti_2019_2023.html, whole report (no relevant data found)
- `bs:coverage:Treatment_start` (verified locally): Pathway stage 'Treatment start' is measured in public data: partly (by county: yes (type only, Taulukko 11)) — keuhkosyoparaportti_2019_2023.html, §4.2, §4.2.2, Taulukko 6–9, 11, 12, Kuva 14, 17
- `cty:curative:Lapin_hyvinvointialue` (verified locally): Lapin hyvinvointialue: curative treatment 18.5% (95% CI 15.8–21.5; n=131/710), below vs national 27.0% — keuhkosyoparaportti_2019_2023.html, Taulukko 11
- `cty:life_prolonging:Lapin_hyvinvointialue` (verified locally): Lapin hyvinvointialue: life-prolonging treatment 16.1% (95% CI 13.5–18.9; n=114/710), below vs national 30.4% — keuhkosyoparaportti_2019_2023.html, Taulukko 11
- `cty:mdt_recorded:Lapin_hyvinvointialue` (verified locally): Lapin hyvinvointialue: MDT meeting recorded 3.0% (95% CI 1.9–4.5; n=21/710), below vs national 6.0% — keuhkosyoparaportti_2019_2023.html, Taulukko 11
- `cty:no_treatment_record:Lapin_hyvinvointialue` (verified locally): Lapin hyvinvointialue: no treatment record within 12 months 33.8% (95% CI 30.4–37.4; n=240/710), above vs national 27.5% — keuhkosyoparaportti_2019_2023.html, Taulukko 11
- `cty:symptomatic:Lapin_hyvinvointialue` (verified locally): Lapin hyvinvointialue: symptomatic treatment 44.5% (95% CI 40.9–48.2; n=316/710), above vs national 39.5% — keuhkosyoparaportti_2019_2023.html, Taulukko 11
- `fig:age_adjusted_only_kuva16` (verified locally): In the 2019–2023 report, county-level age-adjusted treatment shares appear only in Kuva 16 (a PNG figure, by sex, with 95% CIs); the county table (Taulukko 11) gives crude shares only — chart_data.md, Summary table; section 'Kuva 16 in detail'
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
- `q:0780bf74b0` (verified locally): Policy evidence for pathway stage 'Symptoms' — roadmap_2026_2031_fi.pdf, p.52; p.53
- `q:24169121a4` (verified locally): Strategy p.5 (= PDF p.5), “Strategiset tavoitteet”, indicator under “Varmistetaan yhdenvertainen ja vaikuttava syövänhoito”: > “Potilaat pääsevät hoitoon tavoiteaikojen puitteissa” > “ THL (Ohjaus 21/2016). Hoitoonpääsyn seuranta syövän hoidossa.” — strategy_2026_2035_fi.pdf, p.5
- `q:29b792498e` (verified locally): Policy evidence for pathway stage 'Referral' — filha_lung_programme_2026_fi.pdf, p.16
- `q:323de0d90d` (verified locally): Report evidence for pathway stage 'Primary care / occupational health' — keuhkosyoparaportti_2019_2023.html, §3.3 Menetelmät
- `q:37bb4c3b38` (verified locally): Policy evidence for pathway stage 'Referral' — roadmap_2026_2031_fi.pdf, p.52; p.106
- `q:39e6ba43a9` (verified locally): Report evidence for pathway stage 'MDT' — keuhkosyoparaportti_2019_2023.html, §3.3 Menetelmät
- `q:4a856bd695` (verified locally): the registry's data, including stage, allows reliable assessment and comparison of quality and effectiveness, with 90% data coverage — roadmap_2026_2031_fi.pdf, p.60
- `q:4e702a20fe` (verified locally): Finland has no unified national system to steer the drafting of cancer-specific treatment recommendations, or the implementation and monitoring of care pathways based on them (quality and effectiveness targets/indicators, including access to care, and cancer-specific and generic PROMs). Existing recommendations and pathways, and the targets and indicators to be monitored, are not coordinated nationally. This maintains regional inequality in the availability and effectiveness of cancer care. — strategy_2026_2035_fi.pdf, p.33
- `q:556431a0c2` (verified locally): the patient is referred to specialist care according to local instructions — filha_lung_programme_2026_fi.pdf, p.15
- `q:5eb155decc` (verified locally): Report evidence for pathway stage 'Imaging' — keuhkosyoparaportti_2019_2023.html, §4.1.1 Toteamistapa
- `q:614febebf2` (verified locally): When (p.24): > “Väliarvio toteutetaan vuonna 2030, ohjelman puolivälissä ja loppuarviointi vuonna 2036. Eri > osa-alueiden suositukset toteutetaan ennen väliarviointia.” — filha_lung_programme_2026_fi.pdf, p.24
- `q:7885b0974f` (verified locally): Report evidence for pathway stage 'Diagnosis' — keuhkosyoparaportti_2019_2023.html, §4.1.3 Levinneisyystiedon kattavuus
- `q:82d365cd2c` (verified locally): “Tällä hetkellä keuhkosyöpään liittyvien tietojen raportointi, kerääminen ja tallentaminen on puutteellista”; nationally uniform recording instructions (“yhtenäiset kirjaamisohjeet”) must be ensured — filha_lung_programme_2026_fi.pdf, p.21
- `q:8f358a9de6` (verified locally): p.16: > “Tämän ohjelman yhtenä toimenpiteenä tuotetaan kansallinen suositus keuhkosyöpien diagnostiikasta. Se > sisältää myös lähetekriteerit perusterveydenhuollolle ja suositellut aikarajat erikoissairaanhoitoon > eri diagnostiikan polun vaiheille.” — filha_lung_programme_2026_fi.pdf, p.16
- `q:950a2f797b` (verified locally): Reporting, collection and storage of lung cancer data is currently incomplete. — filha_lung_programme_2026_fi.pdf, p.21
- `q:9a1cd194f5` (verified locally): support a smooth transfer to specialist care by defining standardised referral criteria within the national pathways, so that patients with possible cancer symptoms who meet them are directed quickly to diagnostic tests — roadmap_2026_2031_fi.pdf, p.52
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
