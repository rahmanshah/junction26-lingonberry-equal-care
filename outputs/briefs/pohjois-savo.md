# Pohjois-Savo: lung cancer pathway brief

Status: **validated** · gemini-4-argon (thinking HIGH) · 2026-11-14T14:03:04+00:00 · attempts: 2

## Where do we lag?

**Pohjois-Savo lags in crude multidisciplinary team recording at 0.2% (95% CI 0.0–0.9) versus 6.0% nationally, which measures recording practice rather than care.** `cty:mdt_recorded:Pohjois_Savon_hyvinvointialue, nat:mdt_recorded, bs:coverage:MDT`

- In the 2019–2023 cohort, the county's crude curative treatment share is 24.5% (95% CI 21.3–28.0; n=157/641) beside 27.0% (4009/14873) nationally, so the 95% confidence interval includes the national value and is not distinguishable from it. `cty:curative:Pohjois_Savon_hyvinvointialue, nat:curative`
- Because treatment categories overlap and a patient can receive several, the county's crude life-prolonging share of 38.7% (95% CI 35.0–42.5; n=248/641) versus 30.4% (4522/14873) nationally and crude symptomatic share of 51.2% (95% CI 47.3–55.0; n=328/641) versus 39.5% (5871/14873) nationally have 95% confidence intervals that exclude and lie above the national benchmarks. `cty:life_prolonging:Pohjois_Savon_hyvinvointialue, nat:life_prolonging, cty:symptomatic:Pohjois_Savon_hyvinvointialue, nat:symptomatic, bs:coverage:Treatment_start`
- The county's crude multidisciplinary team recording share of 0.2% (95% CI 0.0–0.9; n=1/641) has a 95% confidence interval that excludes and lies below the 6.0% (893/14873) national figure, even though the KYS regional pathway document states that KYS reviews every patient weekly, because HILMO captures specialised care procedures only from direct patient contacts. `cty:mdt_recorded:Pohjois_Savon_hyvinvointialue, nat:mdt_recorded, reg:mdt_practice, bs:coverage:MDT, q:39e6ba43a9`
- At the national level, preliminary, unpublished figures show an average of 155 days from symptoms to treatment in Finland alongside 107 days in Sweden and 67 days in Denmark, with patient delay averaging 56 days, primary care 41 days, and specialist care 58 days as the longest stage. `mot:total_fi, mot:total_se, mot:total_dk, mot:patient, mot:primary, mot:specialist`

## How sure are we?

**Pohjois-Savo's crude share with no treatment record within 12 months is 19.3% (95% CI 16.5–22.6) versus 27.5% nationally, consistent with relatively complete recording, though county shares are unadjusted.** `cty:no_treatment_record:Pohjois_Savon_hyvinvointialue, nat:no_treatment_record, fig:age_adjusted_only_kuva16`

- Mixing untreated patients and unrecorded treatment, the crude share with no treatment record within 12 months is 19.3% (95% CI 16.5–22.6; n=124/641), its 95% confidence interval lying below 27.5% (4089/14873) nationally; as an inference, not a finding, this is consistent with relatively complete treatment recording, so a low curative share is less likely to be only a recording artefact. `cty:no_treatment_record:Pohjois_Savon_hyvinvointialue, nat:no_treatment_record, bs:coverage:Treatment_start`
- Taulukko 11 gives crude county shares with separate limitations: they are not age-adjusted (age-adjusted shares appear only in Kuva 16 by sex, with digitised ±0.5 percentage point national curative reference lines at 26.7% for men and 26.9% for women), and separately they cannot be stage-adjusted because stage at diagnosis is missing for about 48% of patients. `fig:age_adjusted_only_kuva16, k16:curative:men:national, k16:curative:women:national, bs:coverage:Diagnosis, q:7885b0974f`
- A journal article found that hospital discharge register (HILMO) diagnoses match the Cancer Registry for about 90% of most cancer types, but this concerns diagnosis concordance only and says nothing about how completely treatment, referrals, or multidisciplinary team meetings are recorded. `lit:hilmo_90`
- Public data do not measure symptoms or referrals by county, primary care visits are not included in the report's data, occupational health is not mentioned, imaging appears only indirectly as clinical-only diagnosis in approximately 20% of patients, and specialist visit (93.6% nationally within 12 months) and treatment records omit exact start dates. `bs:coverage:Symptoms, bs:coverage:Referral, bs:coverage:Primary_care_occupational_health, q:323de0d90d, bs:coverage:Imaging, q:5eb155decc, bs:coverage:First_specialist_visit, bs:coverage:Treatment_start`

## What should we do first?

**The team recommends publishing county recording completeness for stage, drugs, and multidisciplinary meetings, tracking access times under THL guidance Ohjaus 21/2016 with handover alerts, and naming a diagnostic contact.** `rec:1, rec:2, rec:3, thl:21_2016, q:fc81032a80, q:950a2f797b`

- The team recommends publishing county recording completeness for stage, drug treatment, and multidisciplinary coding as data-quality signals, given Pohjois-Savo's crude 0.2% (95% CI 0.0–0.9; n=1/641) multidisciplinary record share versus 6.0% (893/14873) nationally despite the KYS regional pathway document's weekly review rule, about 48% missing stage data, and incomplete national reporting requiring uniform instructions. `rec:3, cty:mdt_recorded:Pohjois_Savon_hyvinvointialue, nat:mdt_recorded, reg:mdt_practice, bs:coverage:Diagnosis, q:7885b0974f, q:950a2f797b, q:4c7a01d84c`
- The team recommends reporting access times using THL guidance Ohjaus 21/2016 definitions with handover alerts, since the Health Care Act sets no maximum time for cancer suspicion, the STM roadmap (measure 3.1.2) plans national pathways and access times for five cancers by 2026–2028, and the Filha programme's diagnostics recommendation is to be carried out before the 2030 mid-term evaluation. `rec:1, thl:21_2016, law:no_max, q:ed87906241, q:def306014c, q:b326e35410, q:8f358a9de6, q:614febebf2`
- The team recommends a KYS-style referral template, a persistent-symptoms referral rule after a normal X-ray—already in the KYS regional pathway document, addressing the mentor insight that weak referrals get lower urgency—and a named diagnostic-phase contact, as no regional pathway document names a diagnostic contact and the STM roadmap (measure 1.2.3) plans coordinator guidance by 2026–2028 for county adoption by 2029–2031. `rec:2, reg:kys_template, reg:kys_persistent, reg:only_kys_xray, mentor:kaisa_referral, reg:named_contact, q:fc81032a80, q:abcbb06ae3, q:050ee09ebe`

## Review flags (for human review only)

_Flags are for human review only; they never change the brief's status or approve it._

- [medium] `how_sure_are_we.details[0]`: The cited claims do not mention curative treatment shares or recording artefacts for curative treatment, and in Pohjois-Savo the curative treatment share (24.5%, 95% CI 21.3–28.0) is not distinguishable from the national share (27.0%), making the reference to 'a low curative share' unsupported by the cited claims and potentially misleading.

## Claims cited

- `bs:coverage:Diagnosis` (verified locally): Pathway stage 'Diagnosis' is measured in public data: yes (by county: yes (Kuva 7, 10, 13: PNG only)) — keuhkosyoparaportti_2019_2023.html, §4.1, Taulukko 2–4, Kuva 5–13
- `bs:coverage:First_specialist_visit` (verified locally): Pathway stage 'First specialist visit' is measured in public data: partly (by county: no) — keuhkosyoparaportti_2019_2023.html, §3.1, §4.2, Taulukko 5
- `bs:coverage:Imaging` (verified locally): Pathway stage 'Imaging' is measured in public data: partly (by county: partly (Kuva 7, PNG only)) — keuhkosyoparaportti_2019_2023.html, §4.1.1, Taulukko 2, Kuva 5–7
- `bs:coverage:MDT` (verified locally): Pathway stage 'MDT' is measured in public data: partly (by county: yes (Taulukko 11)) — keuhkosyoparaportti_2019_2023.html, §3.3, §4.2, Taulukko 5, 10, 11, 13
- `bs:coverage:Primary_care_occupational_health` (verified locally): Pathway stage 'Primary care / occupational health' is measured in public data: no (by county: no) — keuhkosyoparaportti_2019_2023.html, §3.3
- `bs:coverage:Referral` (verified locally): Pathway stage 'Referral' is measured in public data: no (by county: no) — keuhkosyoparaportti_2019_2023.html, whole report (no relevant data found)
- `bs:coverage:Symptoms` (verified locally): Pathway stage 'Symptoms' is measured in public data: no (by county: no) — keuhkosyoparaportti_2019_2023.html, whole report (no relevant data found)
- `bs:coverage:Treatment_start` (verified locally): Pathway stage 'Treatment start' is measured in public data: partly (by county: yes (type only, Taulukko 11)) — keuhkosyoparaportti_2019_2023.html, §4.2, §4.2.2, Taulukko 6–9, 11, 12, Kuva 14, 17
- `cty:curative:Pohjois_Savon_hyvinvointialue` (verified locally): Pohjois-Savon hyvinvointialue: curative treatment 24.5% (95% CI 21.3–28.0; n=157/641), not distinguishable vs national 27.0% — keuhkosyoparaportti_2019_2023.html, Taulukko 11
- `cty:life_prolonging:Pohjois_Savon_hyvinvointialue` (verified locally): Pohjois-Savon hyvinvointialue: life-prolonging treatment 38.7% (95% CI 35.0–42.5; n=248/641), above vs national 30.4% — keuhkosyoparaportti_2019_2023.html, Taulukko 11
- `cty:mdt_recorded:Pohjois_Savon_hyvinvointialue` (verified locally): Pohjois-Savon hyvinvointialue: MDT meeting recorded 0.2% (95% CI 0.0–0.9; n=1/641), below vs national 6.0% — keuhkosyoparaportti_2019_2023.html, Taulukko 11
- `cty:no_treatment_record:Pohjois_Savon_hyvinvointialue` (verified locally): Pohjois-Savon hyvinvointialue: no treatment record within 12 months 19.3% (95% CI 16.5–22.6; n=124/641), below vs national 27.5% — keuhkosyoparaportti_2019_2023.html, Taulukko 11
- `cty:symptomatic:Pohjois_Savon_hyvinvointialue` (verified locally): Pohjois-Savon hyvinvointialue: symptomatic treatment 51.2% (95% CI 47.3–55.0; n=328/641), above vs national 39.5% — keuhkosyoparaportti_2019_2023.html, Taulukko 11
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
- `q:323de0d90d` (verified locally): Report evidence for pathway stage 'Primary care / occupational health' — keuhkosyoparaportti_2019_2023.html, §3.3 Menetelmät
- `q:39e6ba43a9` (verified locally): Report evidence for pathway stage 'MDT' — keuhkosyoparaportti_2019_2023.html, §3.3 Menetelmät
- `q:4c7a01d84c` (verified locally): nationally uniform recording instructions, and their use, must be ensured — filha_lung_programme_2026_fi.pdf, p.21
- `q:5eb155decc` (verified locally): Report evidence for pathway stage 'Imaging' — keuhkosyoparaportti_2019_2023.html, §4.1.1 Toteamistapa
- `q:614febebf2` (verified locally): When (p.24): > “Väliarvio toteutetaan vuonna 2030, ohjelman puolivälissä ja loppuarviointi vuonna 2036. Eri > osa-alueiden suositukset toteutetaan ennen väliarviointia.” — filha_lung_programme_2026_fi.pdf, p.24
- `q:7885b0974f` (verified locally): Report evidence for pathway stage 'Diagnosis' — keuhkosyoparaportti_2019_2023.html, §4.1.3 Levinneisyystiedon kattavuus
- `q:8f358a9de6` (verified locally): p.16: > “Tämän ohjelman yhtenä toimenpiteenä tuotetaan kansallinen suositus keuhkosyöpien diagnostiikasta. Se > sisältää myös lähetekriteerit perusterveydenhuollolle ja suositellut aikarajat erikoissairaanhoitoon > eri diagnostiikan polun vaiheille.” — filha_lung_programme_2026_fi.pdf, p.16
- `q:950a2f797b` (verified locally): Reporting, collection and storage of lung cancer data is currently incomplete. — filha_lung_programme_2026_fi.pdf, p.21
- `q:abcbb06ae3` (verified locally): 2026–2028: guidance on a named doctor, nurse or specialist worker coordinating cancer care. 2029–2031: wellbeing services counties have adopted it. — roadmap_2026_2031_fi.pdf, p.32
- `q:b326e35410` (verified locally): National pathways with “syöpäkohtaiset hoitoonpääsyajat” for five (unnamed) cancers in 2026–2028, Nordic model — roadmap_2026_2031_fi.pdf, p.57
- `q:def306014c` (verified locally): p.57, timetable: > “2026–2028: Kansalliset hoitoketjukuvaukset tehty viidestä syövästä ja syöpäkohtaiset > hoitoonpääsyajat on määritetty.” — roadmap_2026_2031_fi.pdf, p.57
- `q:ed87906241` (verified locally): p.56, heading: > “Toimenpide 3.1.2 Laaditaan syöpäkohtaiset hoitoketjukuvaukset, ja niiden pohjalta sovelletut > alueelliset hoitoketjut, sekä mekanismi niiden ylläpitoon ja hallintaan” — roadmap_2026_2031_fi.pdf, p.56
- `q:fc81032a80` (verified locally): Measure 1.2.3: Create an operating model and guidance for a named worker responsible for coordinating cancer care. — roadmap_2026_2031_fi.pdf, p.32
- `rec:1` (recommendation (ours)): Team recommendation 1: Counties report access times using the THL 21/2016 definitions, with handover alerts. Each wellbeing services county reports lung cancer access times (referral → first specialist visit → diagnosis → treatment start) using the definitions in THL's Hoitoonpääsyn seuranta syövän hoidossa (Ohjaus 21/2016). Until national target times exist, flag stalled handovers. — recommendations.md, §1. Counties report access times using the THL 21/2016 definitions, with handover alerts
- `rec:2` (recommendation (ours)): Team recommendation 2: A KYS-style referral template, a persistent-symptoms rule and a named contact. Adopt a standard referral content list and template, modelled on KYS. • Add a rule for primary care: if symptoms persist after a normal X-ray, refer for a pulmonologist assessment. • Name a contact person for the diagnostic phase, from referral to diagnosis. — recommendations.md, §2. A KYS-style referral template, a persistent-symptoms rule and a named contact
- `rec:3` (recommendation (ours)): Team recommendation 3: Report recording completeness per county: stage, drug treatment, MDT coding. Publish, per county, how completely stage, drug treatment and MDT meetings are recorded. Read county ‘gaps’ in these fields as data-quality signals first. — recommendations.md, §3. Report recording completeness per county: stage, drug treatment, MDT coding
- `reg:kys_persistent` (verified by Hellu): KYS: refer persistent unexplained symptoms even if the X-ray is clear — pathway_brief.md, 6. Regional pathways compared
- `reg:kys_template` (verified by Hellu): Only KYS lists required referral content and provides a referral template — pathway_brief.md, 6. Regional pathways compared
- `reg:mdt_practice` (verified by Hellu): MDT practice differs: KYS every patient weekly, Keski-Suomi every new case, HUS when needed — pathway_brief.md, 6. Regional pathways compared
- `reg:named_contact` (verified by Hellu): No region names a contact person for the diagnostic phase — pathway_brief.md, 6. Regional pathways compared
- `reg:only_kys_xray` (verified by Hellu): Only KYS tells primary care what to do with a normal X-ray and continuing symptoms — pathway_brief.md, 6. Regional pathways compared
- `thl:21_2016` (verified by Hellu): THL Ohjaus 21/2016 defines how cancer access times are recorded, for 16 cancers — pathway_brief.md, 6. Regional pathways compared
