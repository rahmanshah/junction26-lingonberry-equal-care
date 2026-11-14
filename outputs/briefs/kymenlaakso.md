# Kymenlaakso: lung cancer pathway brief

Status: **validated** · gemini-4-argon (thinking HIGH) · 2026-11-14T11:27:43+00:00 · attempts: 1

## Where do we lag?

**Kymenlaakso lags national benchmarks in crude curative treatment at 19.3% (95% CI 16.3–22.7) versus 27.0% and recorded MDT meetings at 0.5% (95% CI 0.2–1.5) versus 6.0%.** `cty:curative:Kymenlaakson_hyvinvointialue, nat:curative, cty:mdt_recorded:Kymenlaakson_hyvinvointialue, nat:mdt_recorded`

- Crude curative treatment, which is not adjusted for age or stage, was 19.3% (95% CI 16.3–22.7; n=114/591) in Kymenlaakso compared with 27.0% (4009/14873) nationally, and its 95% confidence interval excludes the national value. `cty:curative:Kymenlaakson_hyvinvointialue, nat:curative, bs:coverage:Diagnosis`
- In figures digitised from Kuva 16 for curative treatment only, by sex (precision ±0.5 percentage points), the gap holds after age adjustment for men at 17.9% (95% CI 13.9–22.9) versus 26.7% nationally (95% CI excludes 26.7%), whereas for women at 22.6% (95% CI 16.8–29.3) versus 26.9% the 95% confidence interval includes the national value. `k16:curative:men:Kymenlaakson_hyvinvointialue, k16:curative:men:national, k16:curative:women:Kymenlaakson_hyvinvointialue, k16:curative:women:national`
- Across overlapping treatment categories where a patient can receive several types, crude shares exceeded national values, with 95% confidence intervals excluding national benchmarks for life-prolonging treatment at 37.6% (95% CI 33.8–41.5; n=222/591) versus 30.4% (4522/14873) and symptomatic treatment at 51.3% (95% CI 47.2–55.3; n=303/591) versus 39.5% (5871/14873). `cty:life_prolonging:Kymenlaakson_hyvinvointialue, nat:life_prolonging, cty:symptomatic:Kymenlaakson_hyvinvointialue, nat:symptomatic`
- An MDT meeting was recorded for 0.5% (95% CI 0.2–1.5; n=3/591) of patients versus 6.0% (893/14873) nationally, with the 95% confidence interval excluding the national value, though HILMO captures procedures only from direct patient contacts so this measures recording practice rather than care. `cty:mdt_recorded:Kymenlaakson_hyvinvointialue, nat:mdt_recorded, bs:coverage:MDT, q:39e6ba43a9`

## How sure are we?

**A below-national no-treatment-record share suggests the curative gap is not only a recording artefact, though missing stage data and unmeasured pathway waits leave causes unclear.** `cty:no_treatment_record:Kymenlaakson_hyvinvointialue, nat:no_treatment_record, bs:coverage:Diagnosis, q:7885b0974f, bs:coverage:Treatment_start`

- The crude share with no treatment record within 12 months, mixing untreated patients and unrecorded treatment, was 16.4% (95% CI 13.7–19.6; n=97/591) versus 27.5% (4089/14873) nationally (95% CI excludes 27.5%); as an inference, this data-quality signal is consistent with relatively complete treatment recording (though not direct evidence of it), making the low curative share less likely to be only a recording artefact. `cty:no_treatment_record:Kymenlaakson_hyvinvointialue, nat:no_treatment_record, bs:coverage:Treatment_start`
- Although a journal article found that HILMO diagnoses match the Cancer Registry for about 90% of most cancer types (which concerns diagnosis concordance only and not treatment, referral or MDT recording), Finland has no cancer quality registry and stage at diagnosis is widely missing nationally, preventing stage adjustment of county shares. `lit:hilmo_90, filha:registry, q:47c7e11303, bs:coverage:Diagnosis, q:7885b0974f`
- Public registry data do not measure symptom onset, exclude outpatient primary care and occupational health visits, omit referral dates, capture imaging only when it is the sole basis of diagnosis (in about 20% of cases nationally), and show whether specialist visits or treatments occurred within 12 months but not when they started. `bs:coverage:Symptoms, bs:coverage:Primary_care_occupational_health, q:323de0d90d, bs:coverage:Referral, bs:coverage:Imaging, q:5eb155decc, bs:coverage:First_specialist_visit, bs:coverage:Treatment_start`
- Preliminary, unpublished national figures report an average of 155 days from symptoms to initial treatment in Finland—comprising 56 days of patient delay, 41 days in primary care, and 58 days in specialist care—compared with 107 days in Sweden and 67 days in Denmark, though these preliminary national averages are not county-specific. `mot:total_fi, mot:total_se, mot:total_dk, mot:patient, mot:primary, mot:specialist`

## What should we do first?

**Kymenlaakso can track pathway access times using THL 21/2016 definitions, standardise primary care referrals and diagnostic coordination, and audit MDT and stage recording completeness.** `thl:21_2016, q:556431a0c2, reg:kys_template, cty:mdt_recorded:Kymenlaakson_hyvinvointialue, bs:coverage:Diagnosis`

- Because the Health Care Act sets no maximum wait for a cancer suspicion and Finland lacks uniform diagnostic timetables, Kymenlaakso can track access times using THL Ohjaus 21/2016 guidance (covering 16 cancers) with handover alerts while the roadmap plans national target times by 2026–2028 and Filha's diagnostics guideline is due before the 2030 evaluation. `law:no_max, q:971b2f468f, thl:21_2016, q:24169121a4, q:def306014c, q:8f358a9de6, q:614febebf2`
- Because mentor insight notes that a weak referral receives a lower urgency rating in specialist care, Kymenlaakso can update its local referral instructions with a required-content template and a rule to refer persistent unexplained symptoms despite a clear X-ray, as in the KYS regional pathway document, while the roadmap plans national referral criteria in 2026–2028. `mentor:kaisa_referral, q:556431a0c2, reg:kys_template, reg:kys_persistent, q:9a1cd194f5, q:c61439b30f`
- Assigning a named contact person for the diagnostic phase—which none of the reviewed regional pathway documents include—gives patients a clear contact point while the national roadmap maps which care stage to target and plans care-coordinator guidance in 2026–2028 for counties to adopt in 2029–2031. `reg:named_contact, q:fc81032a80, q:74a8cee731, q:e31448e9c9, q:abcbb06ae3`
- Kymenlaakso can also audit and report how completely it records stage at diagnosis and MDT meetings—currently logged in HILMO for 0.5% (95% CI 0.2–1.5; n=3/591) of patients versus 6.0% (893/14873) nationally—aligning with national plans for uniform recording instructions and a cancer quality registry targeting 90% coverage including stage. `cty:mdt_recorded:Kymenlaakson_hyvinvointialue, nat:mdt_recorded, bs:coverage:MDT, bs:coverage:Diagnosis, q:7885b0974f, q:950a2f797b, q:4c7a01d84c, q:990a0d39a0, q:f07a34a300, q:4a856bd695`

## Review flags (for human review only)

_Flags are for human review only; they never change the brief's status or approve it._

- [medium] `where_we_lag.details[3]`: Missing caveat: cty:mdt_recorded:Kymenlaakson_hyvinvointialue notes that the 0.5% share is crude (not age- or stage-adjusted), which is omitted here.
- [low] `how_sure_are_we.details[2]`: Minor overreach/imprecision: bs:coverage:Primary_care_occupational_health notes that primary care visits are excluded while occupational health is not mentioned in the report (rather than explicitly stated as excluded), and bs:coverage:Imaging / q:5eb155decc state that clinical examination alone (such as imaging) is the basis of diagnosis in about 20% of cases, not exclusively imaging alone.
- [medium] `what_to_do_first.headline`: Unsupported detail: none of the claims cited for this sentence mention diagnostic coordination.
- [medium] `what_to_do_first.details[0]`: Unsupported detail: none of the cited claims mention handover alerts.
- [medium] `what_to_do_first.details[3]`: Missing caveat: cty:mdt_recorded:Kymenlaakson_hyvinvointialue notes that the 0.5% share is crude (not age- or stage-adjusted), which is omitted here.

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
- `filha:registry` (verified locally): No lung cancer or other cancer quality registry; Cancer Registry, THL and FICAN are assessing one, starting with lung cancer — pathway_brief.md, 3. National level: a programme, but no pathway or time targets
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
- `q:323de0d90d` (verified locally): Report evidence for pathway stage 'Primary care / occupational health' — keuhkosyoparaportti_2019_2023.html, §3.3 Menetelmät
- `q:39e6ba43a9` (verified locally): Report evidence for pathway stage 'MDT' — keuhkosyoparaportti_2019_2023.html, §3.3 Menetelmät
- `q:47c7e11303` (verified locally): Finland has no quality registry for lung cancer or for any other cancer. — filha_lung_programme_2026_fi.pdf, p.21
- `q:4a856bd695` (verified locally): the registry's data, including stage, allows reliable assessment and comparison of quality and effectiveness, with 90% data coverage — roadmap_2026_2031_fi.pdf, p.60
- `q:4c7a01d84c` (verified locally): nationally uniform recording instructions, and their use, must be ensured — filha_lung_programme_2026_fi.pdf, p.21
- `q:556431a0c2` (verified locally): the patient is referred to specialist care according to local instructions — filha_lung_programme_2026_fi.pdf, p.15
- `q:5eb155decc` (verified locally): Report evidence for pathway stage 'Imaging' — keuhkosyoparaportti_2019_2023.html, §4.1.1 Toteamistapa
- `q:614febebf2` (verified locally): When (p.24): > “Väliarvio toteutetaan vuonna 2030, ohjelman puolivälissä ja loppuarviointi vuonna 2036. Eri > osa-alueiden suositukset toteutetaan ennen väliarviointia.” — filha_lung_programme_2026_fi.pdf, p.24
- `q:74a8cee731` (verified locally): The most important thing is that the patient knows who has the overall picture of their care, and how they can contact the treating unit when needed. — roadmap_2026_2031_fi.pdf, p.32
- `q:7885b0974f` (verified locally): Report evidence for pathway stage 'Diagnosis' — keuhkosyoparaportti_2019_2023.html, §4.1.3 Levinneisyystiedon kattavuus
- `q:8f358a9de6` (verified locally): p.16: > “Tämän ohjelman yhtenä toimenpiteenä tuotetaan kansallinen suositus keuhkosyöpien diagnostiikasta. Se > sisältää myös lähetekriteerit perusterveydenhuollolle ja suositellut aikarajat erikoissairaanhoitoon > eri diagnostiikan polun vaiheille.” — filha_lung_programme_2026_fi.pdf, p.16
- `q:950a2f797b` (verified locally): Reporting, collection and storage of lung cancer data is currently incomplete. — filha_lung_programme_2026_fi.pdf, p.21
- `q:971b2f468f` (verified locally): Finland has common guidelines for lung cancer diagnostics, but regional variation in the speed of diagnosis, the organisation of care responsibility and the number of operations is large. Nationally there has been no precise uniform guidance on the timetable within which the different parts of diagnostics should be completed. — filha_lung_programme_2026_fi.pdf, p.4
- `q:990a0d39a0` (verified locally): Policy evidence for pathway stage 'MDT' — roadmap_2026_2031_fi.pdf, p.56
- `q:9a1cd194f5` (verified locally): support a smooth transfer to specialist care by defining standardised referral criteria within the national pathways, so that patients with possible cancer symptoms who meet them are directed quickly to diagnostic tests — roadmap_2026_2031_fi.pdf, p.52
- `q:abcbb06ae3` (verified locally): 2026–2028: guidance on a named doctor, nurse or specialist worker coordinating cancer care. 2029–2031: wellbeing services counties have adopted it. — roadmap_2026_2031_fi.pdf, p.32
- `q:c61439b30f` (verified locally): 2026–2028: standardised referral criteria and symptom-based models included in the national pathways of at least the five most common cancers. — roadmap_2026_2031_fi.pdf, p.53
- `q:def306014c` (verified locally): p.57, timetable: > “2026–2028: Kansalliset hoitoketjukuvaukset tehty viidestä syövästä ja syöpäkohtaiset > hoitoonpääsyajat on määritetty.” — roadmap_2026_2031_fi.pdf, p.57
- `q:e31448e9c9` (verified locally): The review will map at which phase of care, and for which patient groups, a care coordinator is most important. — roadmap_2026_2031_fi.pdf, p.32
- `q:f07a34a300` (verified locally): A national cancer care quality registry will be set up alongside THL's Cancer Registry. — roadmap_2026_2031_fi.pdf, p.59
- `q:fc81032a80` (verified locally): Measure 1.2.3: Create an operating model and guidance for a named worker responsible for coordinating cancer care. — roadmap_2026_2031_fi.pdf, p.32
- `reg:kys_persistent` (verified by Hellu): KYS: refer persistent unexplained symptoms even if the X-ray is clear — pathway_brief.md, 6. Regional pathways compared
- `reg:kys_template` (verified by Hellu): Only KYS lists required referral content and provides a referral template — pathway_brief.md, 6. Regional pathways compared
- `reg:named_contact` (verified by Hellu): No region names a contact person for the diagnostic phase — pathway_brief.md, 6. Regional pathways compared
- `thl:21_2016` (verified by Hellu): THL Ohjaus 21/2016 defines how cancer access times are recorded, for 16 cancers — pathway_brief.md, 6. Regional pathways compared
