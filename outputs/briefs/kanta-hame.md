# Kanta-Häme: lung cancer pathway brief

Status: **validated** · gemini-4-argon (thinking HIGH) · 2026-11-14T13:13:33+00:00 · attempts: 1

## Where do we lag?

**Kanta-Häme's overlapping crude shares lag nationally in symptomatic treatment (34.2%, 95% CI 30.4–38.3 vs 39.5%) and no treatment record within 12 months (32.1%, 95% CI 28.3–36.1 vs 27.5%).** `cty:symptomatic:Kanta_Hämeen_hyvinvointialue, nat:symptomatic, cty:no_treatment_record:Kanta_Hämeen_hyvinvointialue, nat:no_treatment_record`

- Kanta-Häme's crude share of patients with no treatment record within 12 months is 32.1% (95% CI 28.3–36.1; n=175/546), whose 95% confidence interval excludes and lies above the national 27.5% (4089/14873); this category mixes untreated patients and treatment that was not recorded. `cty:no_treatment_record:Kanta_Hämeen_hyvinvointialue, nat:no_treatment_record, bs:coverage:Treatment_start`
- The crude symptomatic treatment share is 34.2% (95% CI 30.4–38.3; n=187/546), with a 95% confidence interval excluding and falling below the national 39.5% (5871/14873); because these overlapping treatment categories accompany an above-national crude no-treatment-record share (32.1%, 95% CI 28.3–36.1 vs 27.5%), low treatment shares may partly reflect unrecorded treatment. `cty:symptomatic:Kanta_Hämeen_hyvinvointialue, nat:symptomatic, cty:no_treatment_record:Kanta_Hämeen_hyvinvointialue, nat:no_treatment_record`
- Across overlapping treatment categories where a patient can receive several treatments, the crude curative share of 23.4% (95% CI 20.1–27.2; n=128/546) versus 27.0% (4009/14873) nationally and crude life-prolonging share of 32.2% (95% CI 28.4–36.3; n=176/546) versus 30.4% (4522/14873) nationally have 95% confidence intervals that include the national values. `cty:curative:Kanta_Hämeen_hyvinvointialue, nat:curative, cty:life_prolonging:Kanta_Hämeen_hyvinvointialue, nat:life_prolonging`
- The crude share with a recorded MDT meeting is 21.6% (95% CI 18.4–25.3; n=118/546), whose 95% confidence interval excludes and exceeds the national 6.0% (893/14873), but MDT records measure recording practice rather than care because HILMO captures procedures only from direct patient contacts. `cty:mdt_recorded:Kanta_Hämeen_hyvinvointialue, nat:mdt_recorded, bs:coverage:MDT, q:39e6ba43a9`

## How sure are we?

**A journal article shows about 90% diagnosis concordance in HILMO, but table treatment shares lack age and stage adjustment, and public data omit pathway timestamps.** `lit:hilmo_90, bs:coverage:Diagnosis, bs:coverage:Treatment_start`

- County shares such as Kanta-Häme's crude 23.4% (95% CI 20.1–27.2; n=128/546) curative share have separate limitations: they are not age-adjusted—age-adjusted values exist only in Kuva 16 for curative treatment by sex, with digitised national lines at 26.7% for men and 26.9% for women (about ±0.5 percentage points)—and separately cannot be stage-adjusted because stage is missing for about 48% of patients. `cty:curative:Kanta_Hämeen_hyvinvointialue, k16:curative:men:national, k16:curative:women:national, bs:coverage:Diagnosis, q:7885b0974f`
- A journal article reports that HILMO diagnoses match the Cancer Registry for about 90% of most cancer types, concerning diagnosis concordance only rather than treatment, referral, or MDT recording, while Finland has no cancer quality registry and lung cancer data reporting, collection, and storage remain incomplete. `lit:hilmo_90, filha:registry, q:47c7e11303, q:950a2f797b`
- In public data, primary care visits are not included in the report's data and occupational health is not mentioned, symptoms and referrals are unmeasured, imaging appears only indirectly as clinical-only diagnosis in about 20% of cases without waits, and specialist visits (93.6%) and treatments within 12 months lack start dates. `bs:coverage:Symptoms, bs:coverage:Primary_care_occupational_health, q:323de0d90d, bs:coverage:Imaging, q:5eb155decc, bs:coverage:Referral, bs:coverage:First_specialist_visit, bs:coverage:Treatment_start`
- Only preliminary, unpublished national figures describe pathway durations, averaging 155 days from initial symptoms to treatment in Finland compared with 107 days in Sweden and 67 days in Denmark, split into 56 days of patient delay, 41 days in primary care, and 58 days in specialist care. `mot:total_fi, mot:total_se, mot:total_dk, mot:patient, mot:primary, mot:specialist`

## What should we do first?

**The team recommends publishing county recording completeness for stage, drug treatment, and MDT coding, reporting access times using THL 21/2016 definitions with handover alerts, and standardising referrals and diagnostic coordination.** `rec:1, rec:2, rec:3, thl:21_2016`

- Given Kanta-Häme's crude no-treatment-record share of 32.1% (95% CI 28.3–36.1; n=175/546) versus 27.5% (4089/14873) nationally and about 48% missing stage, the team recommends publishing county recording completeness for stage, drug treatment, and MDT coding; the STM roadmap (measure 3.2.1) plans a quality registry decree by 2026–2028 and reports by 2029–2031 at 90% coverage. `rec:3, cty:no_treatment_record:Kanta_Hämeen_hyvinvointialue, nat:no_treatment_record, bs:coverage:Diagnosis, q:7885b0974f, q:950a2f797b, q:82d365cd2c, q:f07a34a300, q:4a856bd695, q:f540c706f8`
- Because the Health Care Act sets no legal maximum time for a cancer suspicion and national access monitoring is lacking, the team recommends reporting access times from referral to treatment start using THL 21/2016 definitions for 16 cancers with handover alerts, while the STM roadmap (measure 3.1.2) plans national pathway descriptions and access times by 2026–2028 and 2029–2031. `rec:1, law:no_max, thl:21_2016, q:ccda20dce9, q:20d6ca414e, q:ed87906241, q:def306014c, q:b326e35410`
- To address the mentor insight that weak referrals receive lower urgency ratings, the team recommends adopting a standard referral template and persistent-symptoms rule after a normal X-ray modelled on KYS's regional pathway document, while the Filha programme's national diagnostics recommendation with primary-care referral criteria and recommended time limits is to be carried out before the 2030 mid-term evaluation. `rec:2, mentor:kaisa_referral, reg:kys_template, reg:kys_persistent, reg:only_kys_xray, q:29b792498e, q:8c9c032c25, q:432c0e51d6, q:614febebf2, q:14dff3e002`
- Because reviewed regional pathway documents name no diagnostic-phase contact person, the team recommends assigning a named contact from referral to diagnosis; at the national level, the STM roadmap plans standardised referral criteria and symptom-based models by 2026–2028 and 2029–2031 (measure 2.5.2) and care-coordinator guidance by 2026–2028 for county adoption by 2029–2031 (measure 1.2.3). `rec:2, reg:named_contact, q:0780bf74b0, q:37bb4c3b38, q:c61439b30f, q:fc81032a80, q:abcbb06ae3, q:050ee09ebe`

## Review flags (for human review only)

_Flags are for human review only; they never change the brief's status or approve it._

- [low] `how_sure_are_we.headline`: The cited claims ([lit:hilmo_90], [bs:coverage:Diagnosis], [bs:coverage:Treatment_start]) support diagnosis concordance, missing stage (~48%, preventing stage adjustment of curative shares), and missing treatment start dates, but none of the cited claims state that table treatment shares lack age adjustment or that pathway timestamps beyond treatment start are omitted.

## Claims cited

- `bs:coverage:Diagnosis` (verified locally): Pathway stage 'Diagnosis' is measured in public data: yes (by county: yes (Kuva 7, 10, 13: PNG only)) — keuhkosyoparaportti_2019_2023.html, §4.1, Taulukko 2–4, Kuva 5–13
- `bs:coverage:First_specialist_visit` (verified locally): Pathway stage 'First specialist visit' is measured in public data: partly (by county: no) — keuhkosyoparaportti_2019_2023.html, §3.1, §4.2, Taulukko 5
- `bs:coverage:Imaging` (verified locally): Pathway stage 'Imaging' is measured in public data: partly (by county: partly (Kuva 7, PNG only)) — keuhkosyoparaportti_2019_2023.html, §4.1.1, Taulukko 2, Kuva 5–7
- `bs:coverage:MDT` (verified locally): Pathway stage 'MDT' is measured in public data: partly (by county: yes (Taulukko 11)) — keuhkosyoparaportti_2019_2023.html, §3.3, §4.2, Taulukko 5, 10, 11, 13
- `bs:coverage:Primary_care_occupational_health` (verified locally): Pathway stage 'Primary care / occupational health' is measured in public data: no (by county: no) — keuhkosyoparaportti_2019_2023.html, §3.3
- `bs:coverage:Referral` (verified locally): Pathway stage 'Referral' is measured in public data: no (by county: no) — keuhkosyoparaportti_2019_2023.html, whole report (no relevant data found)
- `bs:coverage:Symptoms` (verified locally): Pathway stage 'Symptoms' is measured in public data: no (by county: no) — keuhkosyoparaportti_2019_2023.html, whole report (no relevant data found)
- `bs:coverage:Treatment_start` (verified locally): Pathway stage 'Treatment start' is measured in public data: partly (by county: yes (type only, Taulukko 11)) — keuhkosyoparaportti_2019_2023.html, §4.2, §4.2.2, Taulukko 6–9, 11, 12, Kuva 14, 17
- `cty:curative:Kanta_Hämeen_hyvinvointialue` (verified locally): Kanta-Hämeen hyvinvointialue: curative treatment 23.4% (95% CI 20.1–27.2; n=128/546), not distinguishable vs national 27.0% — keuhkosyoparaportti_2019_2023.html, Taulukko 11
- `cty:life_prolonging:Kanta_Hämeen_hyvinvointialue` (verified locally): Kanta-Hämeen hyvinvointialue: life-prolonging treatment 32.2% (95% CI 28.4–36.3; n=176/546), not distinguishable vs national 30.4% — keuhkosyoparaportti_2019_2023.html, Taulukko 11
- `cty:mdt_recorded:Kanta_Hämeen_hyvinvointialue` (verified locally): Kanta-Hämeen hyvinvointialue: MDT meeting recorded 21.6% (95% CI 18.4–25.3; n=118/546), above vs national 6.0% — keuhkosyoparaportti_2019_2023.html, Taulukko 11
- `cty:no_treatment_record:Kanta_Hämeen_hyvinvointialue` (verified locally): Kanta-Hämeen hyvinvointialue: no treatment record within 12 months 32.1% (95% CI 28.3–36.1; n=175/546), above vs national 27.5% — keuhkosyoparaportti_2019_2023.html, Taulukko 11
- `cty:symptomatic:Kanta_Hämeen_hyvinvointialue` (verified locally): Kanta-Hämeen hyvinvointialue: symptomatic treatment 34.2% (95% CI 30.4–38.3; n=187/546), below vs national 39.5% — keuhkosyoparaportti_2019_2023.html, Taulukko 11
- `filha:registry` (verified locally): No lung cancer or other cancer quality registry; Cancer Registry, THL and FICAN are assessing one, starting with lung cancer — pathway_brief.md, 3. National level: a programme, but no pathway or time targets
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
- `q:14dff3e002` (verified locally): Policy evidence for pathway stage 'Referral' — filha_lung_programme_2026_fi.pdf, PDF p.7 (unnumbered); p.15; p.17; p.20; p.21; p.23; p.24
- `q:20d6ca414e` (verified locally): “Valtakunnallisesti ei ole ollut tarkkaa yhtenäistä ohjeistusta siitä, millä aikataululla diagnostiikan eri osa-alueet tulisi olla tehtyinä”; regional variation in diagnostic speed is large. The programme itself sets no day-based targets — filha_lung_programme_2026_fi.pdf, p.4
- `q:29b792498e` (verified locally): Policy evidence for pathway stage 'Referral' — filha_lung_programme_2026_fi.pdf, p.16
- `q:323de0d90d` (verified locally): Report evidence for pathway stage 'Primary care / occupational health' — keuhkosyoparaportti_2019_2023.html, §3.3 Menetelmät
- `q:37bb4c3b38` (verified locally): Policy evidence for pathway stage 'Referral' — roadmap_2026_2031_fi.pdf, p.52; p.106
- `q:39e6ba43a9` (verified locally): Report evidence for pathway stage 'MDT' — keuhkosyoparaportti_2019_2023.html, §3.3 Menetelmät
- `q:432c0e51d6` (verified locally): The upcoming national diagnostics recommendation will include “suositellut aikarajat erikoissairaanhoitoon eri diagnostiikan polun vaiheille” (recommended time limits in specialist care), to be carried out (“toteutetaan”; may mean produced or implemented) before the 2030 mid-term evaluation — filha_lung_programme_2026_fi.pdf, p.16
- `q:47c7e11303` (verified locally): Finland has no quality registry for lung cancer or for any other cancer. — filha_lung_programme_2026_fi.pdf, p.21
- `q:4a856bd695` (verified locally): the registry's data, including stage, allows reliable assessment and comparison of quality and effectiveness, with 90% data coverage — roadmap_2026_2031_fi.pdf, p.60
- `q:5eb155decc` (verified locally): Report evidence for pathway stage 'Imaging' — keuhkosyoparaportti_2019_2023.html, §4.1.1 Toteamistapa
- `q:614febebf2` (verified locally): When (p.24): > “Väliarvio toteutetaan vuonna 2030, ohjelman puolivälissä ja loppuarviointi vuonna 2036. Eri > osa-alueiden suositukset toteutetaan ennen väliarviointia.” — filha_lung_programme_2026_fi.pdf, p.24
- `q:7885b0974f` (verified locally): Report evidence for pathway stage 'Diagnosis' — keuhkosyoparaportti_2019_2023.html, §4.1.3 Levinneisyystiedon kattavuus
- `q:82d365cd2c` (verified locally): “Tällä hetkellä keuhkosyöpään liittyvien tietojen raportointi, kerääminen ja tallentaminen on puutteellista”; nationally uniform recording instructions (“yhtenäiset kirjaamisohjeet”) must be ensured — filha_lung_programme_2026_fi.pdf, p.21
- `q:8c9c032c25` (verified locally): Policy evidence for pathway stage 'Referral' — filha_lung_programme_2026_fi.pdf, p.16
- `q:950a2f797b` (verified locally): Reporting, collection and storage of lung cancer data is currently incomplete. — filha_lung_programme_2026_fi.pdf, p.21
- `q:abcbb06ae3` (verified locally): 2026–2028: guidance on a named doctor, nurse or specialist worker coordinating cancer care. 2029–2031: wellbeing services counties have adopted it. — roadmap_2026_2031_fi.pdf, p.32
- `q:b326e35410` (verified locally): National pathways with “syöpäkohtaiset hoitoonpääsyajat” for five (unnamed) cancers in 2026–2028, Nordic model — roadmap_2026_2031_fi.pdf, p.57
- `q:c61439b30f` (verified locally): 2026–2028: standardised referral criteria and symptom-based models included in the national pathways of at least the five most common cancers. — roadmap_2026_2031_fi.pdf, p.53
- `q:ccda20dce9` (verified locally): Finland has no national system steering cancer pathways or their monitoring, “mukaan lukien hoitoonpääsy” — strategy_2026_2035_fi.pdf, p.33
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
