# Etelä-Pohjanmaa: lung cancer pathway brief

Status: **validated** · gemini-4-argon (thinking HIGH) · 2026-11-14T13:57:35+00:00 · attempts: 2

## Where do we lag?

**Etelä-Pohjanmaa's crude symptomatic treatment share is 28.1% (95% CI 24.5–32.1; n=152/540), where the 95% confidence interval excludes the national 39.5% (5871/14873) and lies below it.** `cty:symptomatic:Etelä_Pohjanmaan_hyvinvointialue, nat:symptomatic`

- Across overlapping treatment categories where a patient can have several treatments, the crude curative share is 30.6% (95% CI 26.8–34.6; n=165/540), whose 95% confidence interval includes the national 27.0% (4009/14873), while the crude life-prolonging share is 40.4% (95% CI 36.3–44.6; n=218/540), whose 95% confidence interval excludes the national 30.4% (4522/14873) and lies above it. `cty:curative:Etelä_Pohjanmaan_hyvinvointialue, nat:curative, cty:life_prolonging:Etelä_Pohjanmaan_hyvinvointialue, nat:life_prolonging`
- For the crude share with no treatment record within 12 months, Etelä-Pohjanmaa is at 25.7% (95% CI 22.2–29.6; n=139/540), whose 95% confidence interval includes the national 27.5% (4089/14873), and this category mixes untreated patients and unrecorded treatment. `cty:no_treatment_record:Etelä_Pohjanmaan_hyvinvointialue, nat:no_treatment_record, bs:coverage:Treatment_start`
- Etelä-Pohjanmaa's crude share with an MDT meeting recorded is 32.4% (95% CI 28.6–36.5; n=175/540), whose 95% confidence interval excludes the national 6.0% (893/14873) and lies above it, though HILMO procedure codes are entered only from direct patient contacts and therefore measure recording practice rather than care. `cty:mdt_recorded:Etelä_Pohjanmaan_hyvinvointialue, nat:mdt_recorded, bs:coverage:MDT, q:39e6ba43a9`
- While public data do not measure county wait times from symptoms, referrals, or treatment start, preliminary, unpublished national averages show 155 days from symptoms to treatment in Finland versus 107 days in Sweden and 67 days in Denmark, comprising 56 days of patient delay, 41 days in primary care, and 58 days in specialist care. `bs:coverage:Symptoms, bs:coverage:Referral, bs:coverage:Treatment_start, mot:total_fi, mot:total_se, mot:total_dk, mot:patient, mot:primary, mot:specialist`

## How sure are we?

**County treatment shares in Taulukko 11 are crude: they lack age adjustment and separately cannot be stage-adjusted because stage at diagnosis is missing for about 48% of patients.** `fig:age_adjusted_only_kuva16, bs:coverage:Diagnosis, q:7885b0974f`

- In the 2019–2023 report, county-level age-adjusted treatment shares appear only in Kuva 16 (a PNG figure, by sex, with 95% CIs), where the digitised national age-adjusted curative reference lines are 26.7% for men and 26.9% for women (±0.5 percentage points), whereas Taulukko 11 gives only crude county shares. `fig:age_adjusted_only_kuva16, k16:curative:men:national, k16:curative:women:national`
- A journal article found that hospital discharge register (HILMO) diagnoses match the Cancer Registry for about 90% of most cancer types, which concerns diagnosis concordance only and not treatment, referral, or MDT recording, while overall lung cancer data reporting, collection, and storage remain incomplete and Finland has no cancer quality registry. `lit:hilmo_90, q:950a2f797b, q:47c7e11303, filha:registry`
- Public report data do not measure symptom onset or referral dates, outpatient primary care visits are not included in the report's data, occupational health is not mentioned at all, and imaging appears only indirectly as diagnosis based on clinical examination alone, such as imaging, in approximately 20% of patients without imaging waits. `bs:coverage:Symptoms, bs:coverage:Referral, bs:coverage:Primary_care_occupational_health, q:323de0d90d, bs:coverage:Imaging, q:5eb155decc`
- The report tracks whether a specialist visit occurs within 12 months (93.6% nationally) and treatment type within 12 months, but not county visit or treatment start dates, while mentor insight indicates that a weak referral gets a lower urgency rating in specialist care and occupational health gets patients to specialist care faster. `bs:coverage:First_specialist_visit, bs:coverage:Treatment_start, mentor:kaisa_referral, mentor:hanna_occupational`

## What should we do first?

**The team recommends reporting THL 21/2016 access times with handover alerts, standardising referrals with a diagnostic-phase contact, and publishing per-county coding coverage for stage, drug treatment, and MDT meetings.** `rec:1, rec:2, rec:3, q:24169121a4, q:556431a0c2, q:950a2f797b`

- Because the Health Care Act sets no legal maximum time for a cancer suspicion and national access-time monitoring is lacking, the team recommends reporting access times using THL guidance 21/2016 definitions (for 16 cancers) with handover alerts, while the STM roadmap (measure 3.1.2) plans national pathway descriptions and target access times for five cancers by 2026–2028. `rec:1, law:no_max, thl:21_2016, q:4e702a20fe, q:ccda20dce9, q:ed87906241, q:def306014c, q:b326e35410`
- Since referrals follow local instructions and mentor insight notes weak referrals get lower urgency ratings, the team recommends a standard referral template, a persistent-symptoms referral rule after a normal X-ray, and a diagnostic-phase contact, while the Filha programme's diagnostics recommendation with primary-care referral criteria and recommended time limits is to be carried out before the 2030 mid-term evaluation. `rec:2, q:556431a0c2, mentor:kaisa_referral, q:8f358a9de6, q:29b792498e, q:8c9c032c25, q:614febebf2, q:14dff3e002`
- To support the team's recommendation for standardised referrals and a named diagnostic-phase contact, the STM roadmap plans standardised referral criteria and symptom-based models in national pathways for at least the five most common cancers by 2026–2028 (measure 2.5.2), plus care-coordinator guidance by 2026–2028 for county adoption by 2029–2031 while mapping which care phase to target (measure 1.2.3). `rec:2, q:0780bf74b0, q:37bb4c3b38, q:9a1cd194f5, q:c61439b30f, q:fc81032a80, q:e31448e9c9, q:abcbb06ae3, q:050ee09ebe`
- Because stage is missing for about 48% of patients nationally and MDT codes capture only direct patient contacts—with Etelä-Pohjanmaa's crude MDT-recorded share at 32.4% (95% CI 28.6–36.5; n=175/540) versus 6.0% (893/14873) nationally—the team recommends publishing per-county stage, drug treatment, and MDT coding coverage while the STM roadmap (measure 3.2.1) plans a quality registry decree update by 2026–2028. `rec:3, bs:coverage:Diagnosis, q:7885b0974f, bs:coverage:MDT, q:39e6ba43a9, cty:mdt_recorded:Etelä_Pohjanmaan_hyvinvointialue, nat:mdt_recorded, q:f07a34a300`

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
- `cty:curative:Etelä_Pohjanmaan_hyvinvointialue` (verified locally): Etelä-Pohjanmaan hyvinvointialue: curative treatment 30.6% (95% CI 26.8–34.6; n=165/540), not distinguishable vs national 27.0% — keuhkosyoparaportti_2019_2023.html, Taulukko 11
- `cty:life_prolonging:Etelä_Pohjanmaan_hyvinvointialue` (verified locally): Etelä-Pohjanmaan hyvinvointialue: life-prolonging treatment 40.4% (95% CI 36.3–44.6; n=218/540), above vs national 30.4% — keuhkosyoparaportti_2019_2023.html, Taulukko 11
- `cty:mdt_recorded:Etelä_Pohjanmaan_hyvinvointialue` (verified locally): Etelä-Pohjanmaan hyvinvointialue: MDT meeting recorded 32.4% (95% CI 28.6–36.5; n=175/540), above vs national 6.0% — keuhkosyoparaportti_2019_2023.html, Taulukko 11
- `cty:no_treatment_record:Etelä_Pohjanmaan_hyvinvointialue` (verified locally): Etelä-Pohjanmaan hyvinvointialue: no treatment record within 12 months 25.7% (95% CI 22.2–29.6; n=139/540), not distinguishable vs national 27.5% — keuhkosyoparaportti_2019_2023.html, Taulukko 11
- `cty:symptomatic:Etelä_Pohjanmaan_hyvinvointialue` (verified locally): Etelä-Pohjanmaan hyvinvointialue: symptomatic treatment 28.1% (95% CI 24.5–32.1; n=152/540), below vs national 39.5% — keuhkosyoparaportti_2019_2023.html, Taulukko 11
- `fig:age_adjusted_only_kuva16` (verified locally): In the 2019–2023 report, county-level age-adjusted treatment shares appear only in Kuva 16 (a PNG figure, by sex, with 95% CIs); the county table (Taulukko 11) gives crude shares only — chart_data.md, Summary table; section 'Kuva 16 in detail'
- `filha:registry` (verified locally): No lung cancer or other cancer quality registry; Cancer Registry, THL and FICAN are assessing one, starting with lung cancer — pathway_brief.md, 3. National level: a programme, but no pathway or time targets
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
- `q:14dff3e002` (verified locally): Policy evidence for pathway stage 'Referral' — filha_lung_programme_2026_fi.pdf, PDF p.7 (unnumbered); p.15; p.17; p.20; p.21; p.23; p.24
- `q:24169121a4` (verified locally): Strategy p.5 (= PDF p.5), “Strategiset tavoitteet”, indicator under “Varmistetaan yhdenvertainen ja vaikuttava syövänhoito”: > “Potilaat pääsevät hoitoon tavoiteaikojen puitteissa” > “ THL (Ohjaus 21/2016). Hoitoonpääsyn seuranta syövän hoidossa.” — strategy_2026_2035_fi.pdf, p.5
- `q:29b792498e` (verified locally): Policy evidence for pathway stage 'Referral' — filha_lung_programme_2026_fi.pdf, p.16
- `q:323de0d90d` (verified locally): Report evidence for pathway stage 'Primary care / occupational health' — keuhkosyoparaportti_2019_2023.html, §3.3 Menetelmät
- `q:37bb4c3b38` (verified locally): Policy evidence for pathway stage 'Referral' — roadmap_2026_2031_fi.pdf, p.52; p.106
- `q:39e6ba43a9` (verified locally): Report evidence for pathway stage 'MDT' — keuhkosyoparaportti_2019_2023.html, §3.3 Menetelmät
- `q:47c7e11303` (verified locally): Finland has no quality registry for lung cancer or for any other cancer. — filha_lung_programme_2026_fi.pdf, p.21
- `q:4e702a20fe` (verified locally): Finland has no unified national system to steer the drafting of cancer-specific treatment recommendations, or the implementation and monitoring of care pathways based on them (quality and effectiveness targets/indicators, including access to care, and cancer-specific and generic PROMs). Existing recommendations and pathways, and the targets and indicators to be monitored, are not coordinated nationally. This maintains regional inequality in the availability and effectiveness of cancer care. — strategy_2026_2035_fi.pdf, p.33
- `q:556431a0c2` (verified locally): the patient is referred to specialist care according to local instructions — filha_lung_programme_2026_fi.pdf, p.15
- `q:5eb155decc` (verified locally): Report evidence for pathway stage 'Imaging' — keuhkosyoparaportti_2019_2023.html, §4.1.1 Toteamistapa
- `q:614febebf2` (verified locally): When (p.24): > “Väliarvio toteutetaan vuonna 2030, ohjelman puolivälissä ja loppuarviointi vuonna 2036. Eri > osa-alueiden suositukset toteutetaan ennen väliarviointia.” — filha_lung_programme_2026_fi.pdf, p.24
- `q:7885b0974f` (verified locally): Report evidence for pathway stage 'Diagnosis' — keuhkosyoparaportti_2019_2023.html, §4.1.3 Levinneisyystiedon kattavuus
- `q:8c9c032c25` (verified locally): Policy evidence for pathway stage 'Referral' — filha_lung_programme_2026_fi.pdf, p.16
- `q:8f358a9de6` (verified locally): p.16: > “Tämän ohjelman yhtenä toimenpiteenä tuotetaan kansallinen suositus keuhkosyöpien diagnostiikasta. Se > sisältää myös lähetekriteerit perusterveydenhuollolle ja suositellut aikarajat erikoissairaanhoitoon > eri diagnostiikan polun vaiheille.” — filha_lung_programme_2026_fi.pdf, p.16
- `q:950a2f797b` (verified locally): Reporting, collection and storage of lung cancer data is currently incomplete. — filha_lung_programme_2026_fi.pdf, p.21
- `q:9a1cd194f5` (verified locally): support a smooth transfer to specialist care by defining standardised referral criteria within the national pathways, so that patients with possible cancer symptoms who meet them are directed quickly to diagnostic tests — roadmap_2026_2031_fi.pdf, p.52
- `q:abcbb06ae3` (verified locally): 2026–2028: guidance on a named doctor, nurse or specialist worker coordinating cancer care. 2029–2031: wellbeing services counties have adopted it. — roadmap_2026_2031_fi.pdf, p.32
- `q:b326e35410` (verified locally): National pathways with “syöpäkohtaiset hoitoonpääsyajat” for five (unnamed) cancers in 2026–2028, Nordic model — roadmap_2026_2031_fi.pdf, p.57
- `q:c61439b30f` (verified locally): 2026–2028: standardised referral criteria and symptom-based models included in the national pathways of at least the five most common cancers. — roadmap_2026_2031_fi.pdf, p.53
- `q:ccda20dce9` (verified locally): Finland has no national system steering cancer pathways or their monitoring, “mukaan lukien hoitoonpääsy” — strategy_2026_2035_fi.pdf, p.33
- `q:def306014c` (verified locally): p.57, timetable: > “2026–2028: Kansalliset hoitoketjukuvaukset tehty viidestä syövästä ja syöpäkohtaiset > hoitoonpääsyajat on määritetty.” — roadmap_2026_2031_fi.pdf, p.57
- `q:e31448e9c9` (verified locally): The review will map at which phase of care, and for which patient groups, a care coordinator is most important. — roadmap_2026_2031_fi.pdf, p.32
- `q:ed87906241` (verified locally): p.56, heading: > “Toimenpide 3.1.2 Laaditaan syöpäkohtaiset hoitoketjukuvaukset, ja niiden pohjalta sovelletut > alueelliset hoitoketjut, sekä mekanismi niiden ylläpitoon ja hallintaan” — roadmap_2026_2031_fi.pdf, p.56
- `q:f07a34a300` (verified locally): A national cancer care quality registry will be set up alongside THL's Cancer Registry. — roadmap_2026_2031_fi.pdf, p.59
- `q:fc81032a80` (verified locally): Measure 1.2.3: Create an operating model and guidance for a named worker responsible for coordinating cancer care. — roadmap_2026_2031_fi.pdf, p.32
- `rec:1` (recommendation (ours)): Team recommendation 1: Counties report access times using the THL 21/2016 definitions, with handover alerts. Each wellbeing services county reports lung cancer access times (referral → first specialist visit → diagnosis → treatment start) using the definitions in THL's Hoitoonpääsyn seuranta syövän hoidossa (Ohjaus 21/2016). Until national target times exist, flag stalled handovers. — recommendations.md, §1. Counties report access times using the THL 21/2016 definitions, with handover alerts
- `rec:2` (recommendation (ours)): Team recommendation 2: A KYS-style referral template, a persistent-symptoms rule and a named contact. Adopt a standard referral content list and template, modelled on KYS. • Add a rule for primary care: if symptoms persist after a normal X-ray, refer for a pulmonologist assessment. • Name a contact person for the diagnostic phase, from referral to diagnosis. — recommendations.md, §2. A KYS-style referral template, a persistent-symptoms rule and a named contact
- `rec:3` (recommendation (ours)): Team recommendation 3: Report recording completeness per county: stage, drug treatment, MDT coding. Publish, per county, how completely stage, drug treatment and MDT meetings are recorded. Read county ‘gaps’ in these fields as data-quality signals first. — recommendations.md, §3. Report recording completeness per county: stage, drug treatment, MDT coding
- `thl:21_2016` (verified by Hellu): THL Ohjaus 21/2016 defines how cancer access times are recorded, for 16 cancers — pathway_brief.md, 6. Regional pathways compared
