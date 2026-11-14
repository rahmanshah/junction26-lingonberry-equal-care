# Vantaa ja Kerava: lung cancer pathway brief

Status: **validated** · gemini-4-argon (thinking HIGH) · 2026-11-14T13:38:26+00:00 · attempts: 1

## Where do we lag?

**Across overlapping categories, county crude shares lag nationally for life-prolonging treatment (20.3%, 95% CI 17.3–23.8 vs 30.4%) and recorded MDT meetings (0.2%, 95% CI 0.0–0.9 vs 6.0%).** `cty:life_prolonging:Vantaan_ja_Keravan_hyvinvointialue, nat:life_prolonging, cty:mdt_recorded:Vantaan_ja_Keravan_hyvinvointialue, nat:mdt_recorded`

- The county's crude life-prolonging treatment share is 20.3% (95% CI 17.3–23.8; n=121/595) compared with 30.4% (4522/14873) nationally, and its 95% confidence interval excludes the national value. `cty:life_prolonging:Vantaan_ja_Keravan_hyvinvointialue, nat:life_prolonging`
- An MDT meeting is recorded for a crude share of 0.2% of county patients (95% CI 0.0–0.9; n=1/595) versus 6.0% (893/14873) nationally, with the 95% confidence interval excluding the national value, though HILMO MDT codes measure recording practice from direct patient contacts rather than care. `cty:mdt_recorded:Vantaan_ja_Keravan_hyvinvointialue, nat:mdt_recorded, bs:coverage:MDT, q:39e6ba43a9`
- Because treatment categories overlap and a patient can have several treatments, the county's crude curative share of 35.6% (95% CI 31.9–39.6; n=212/595) has a 95% confidence interval above the national 27.0% (4009/14873), whereas the crude symptomatic share of 36.1% (95% CI 32.4–40.1; n=215/595) includes the national 39.5% (5871/14873) in its 95% confidence interval. `cty:curative:Vantaan_ja_Keravan_hyvinvointialue, nat:curative, cty:symptomatic:Vantaan_ja_Keravan_hyvinvointialue, nat:symptomatic`
- The crude share of patients with no treatment record within 12 months is 28.9% (95% CI 25.4–32.7; n=172/595) compared with 27.5% (4089/14873) nationally, a category whose 95% confidence interval includes the national value and that mixes untreated patients with unrecorded treatment. `cty:no_treatment_record:Vantaan_ja_Keravan_hyvinvointialue, nat:no_treatment_record, bs:coverage:Treatment_start`

## How sure are we?

**County treatment shares in Taulukko 11 are crude—neither age-adjusted nor stage-adjusted—and public registry data do not capture pathway waiting times before or after diagnosis.** `fig:age_adjusted_only_kuva16, bs:coverage:Diagnosis, bs:coverage:Referral, bs:coverage:Treatment_start`

- Taulukko 11 gives crude county shares with separate limitations: they are not age-adjusted (county age-adjusted shares appear only in the Kuva 16 figure, where digitised national curative reference lines at ±0.5 percentage points are 26.7% for men and 26.9% for women), and independently, they cannot be stage-adjusted because stage at diagnosis is missing for about 48% of patients. `fig:age_adjusted_only_kuva16, k16:curative:men:national, k16:curative:women:national, bs:coverage:Diagnosis, q:7885b0974f`
- A journal article found that HILMO diagnoses match the Cancer Registry for about 90% of most cancer types, which supports diagnosis concordance only and says nothing about treatment, referral or MDT recording, while Finland has no cancer quality registry and lung cancer data collection remains incomplete. `lit:hilmo_90, filha:registry, q:47c7e11303, q:950a2f797b`
- In the report, symptoms and referrals are not measured, primary care visits are not included in the report's data, occupational health is not mentioned, imaging appears only indirectly as the diagnosis basis for about 20% of patients, and HILMO records whether a specialist visit (93.6%) or treatment occurred within 12 months but not when it started. `bs:coverage:Symptoms, bs:coverage:Referral, bs:coverage:Primary_care_occupational_health, q:323de0d90d, bs:coverage:Imaging, q:5eb155decc, bs:coverage:First_specialist_visit, bs:coverage:Treatment_start`
- Preliminary, unpublished figures from an MOT study show lung cancer in Finland takes 155 days on average from symptoms to treatment versus 107 days in Sweden and 67 days in Denmark—comprising 56 days of patient delay, 41 days in primary care and 58 days in specialist care—but these preliminary figures are national averages, not county data. `mot:total_fi, mot:total_se, mot:total_dk, mot:patient, mot:primary, mot:specialist`

## What should we do first?

**The team recommends publishing how completely stage, drug treatment and MDT meetings are recorded, tracking access times with THL 21/2016 definitions, and standardising referrals and diagnostic-phase coordination.** `rec:3, rec:1, rec:2, q:950a2f797b, thl:21_2016, q:556431a0c2`

- Given the county's overlapping crude shares for recorded MDT meetings at 0.2% (95% CI 0.0–0.9; n=1/595) versus 6.0% nationally and life-prolonging treatment at 20.3% (95% CI 17.3–23.8; n=121/595) versus 30.4% nationally—alongside missing stage for about 48% of patients and incomplete data collection—the team recommends publishing per county how completely stage, drug treatment and MDT meetings are recorded. `rec:3, cty:mdt_recorded:Vantaan_ja_Keravan_hyvinvointialue, nat:mdt_recorded, cty:life_prolonging:Vantaan_ja_Keravan_hyvinvointialue, nat:life_prolonging, bs:coverage:Diagnosis, q:7885b0974f, bs:coverage:MDT, q:39e6ba43a9, q:950a2f797b, q:82d365cd2c`
- Because the Health Care Act §52 sets no maximum time for a cancer suspicion and Finland lacks national pathway monitoring, the team recommends reporting access times using THL Ohjaus 21/2016 definitions for 16 cancers and flagging stalled handovers while the Filha programme's diagnostics recommendation with specialist-care time limits is to be carried out before the 2030 mid-term evaluation. `rec:1, law:no_max, q:4e702a20fe, q:ccda20dce9, thl:21_2016, q:24169121a4, q:cd51b9d5b6, q:8c9c032c25, q:8f358a9de6, q:614febebf2, q:432c0e51d6`
- The team recommends adopting a referral template and persistent-symptoms rule modelled on KYS's regional pathway document and naming a diagnostic-phase contact person, as local referral practices vary, mentor insight notes weak referrals get lower urgency ratings, and the STM roadmap's measure 1.2.3 plans care-coordinator guidance by 2026–2028 for county adoption by 2029–2031 without specifying the care phase. `rec:2, reg:kys_template, reg:kys_persistent, q:556431a0c2, q:82b59905ad, mentor:kaisa_referral, q:fc81032a80, q:abcbb06ae3, q:050ee09ebe`

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
- `cty:curative:Vantaan_ja_Keravan_hyvinvointialue` (verified locally): Vantaan ja Keravan hyvinvointialue: curative treatment 35.6% (95% CI 31.9–39.6; n=212/595), above vs national 27.0% — keuhkosyoparaportti_2019_2023.html, Taulukko 11
- `cty:life_prolonging:Vantaan_ja_Keravan_hyvinvointialue` (verified locally): Vantaan ja Keravan hyvinvointialue: life-prolonging treatment 20.3% (95% CI 17.3–23.8; n=121/595), below vs national 30.4% — keuhkosyoparaportti_2019_2023.html, Taulukko 11
- `cty:mdt_recorded:Vantaan_ja_Keravan_hyvinvointialue` (verified locally): Vantaan ja Keravan hyvinvointialue: MDT meeting recorded 0.2% (95% CI 0.0–0.9; n=1/595), below vs national 6.0% — keuhkosyoparaportti_2019_2023.html, Taulukko 11
- `cty:no_treatment_record:Vantaan_ja_Keravan_hyvinvointialue` (verified locally): Vantaan ja Keravan hyvinvointialue: no treatment record within 12 months 28.9% (95% CI 25.4–32.7; n=172/595), not distinguishable vs national 27.5% — keuhkosyoparaportti_2019_2023.html, Taulukko 11
- `cty:symptomatic:Vantaan_ja_Keravan_hyvinvointialue` (verified locally): Vantaan ja Keravan hyvinvointialue: symptomatic treatment 36.1% (95% CI 32.4–40.1; n=215/595), not distinguishable vs national 39.5% — keuhkosyoparaportti_2019_2023.html, Taulukko 11
- `fig:age_adjusted_only_kuva16` (verified locally): In the 2019–2023 report, county-level age-adjusted treatment shares appear only in Kuva 16 (a PNG figure, by sex, with 95% CIs); the county table (Taulukko 11) gives crude shares only — chart_data.md, Summary table; section 'Kuva 16 in detail'
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
- `q:24169121a4` (verified locally): Strategy p.5 (= PDF p.5), “Strategiset tavoitteet”, indicator under “Varmistetaan yhdenvertainen ja vaikuttava syövänhoito”: > “Potilaat pääsevät hoitoon tavoiteaikojen puitteissa” > “ THL (Ohjaus 21/2016). Hoitoonpääsyn seuranta syövän hoidossa.” — strategy_2026_2035_fi.pdf, p.5
- `q:323de0d90d` (verified locally): Report evidence for pathway stage 'Primary care / occupational health' — keuhkosyoparaportti_2019_2023.html, §3.3 Menetelmät
- `q:39e6ba43a9` (verified locally): Report evidence for pathway stage 'MDT' — keuhkosyoparaportti_2019_2023.html, §3.3 Menetelmät
- `q:432c0e51d6` (verified locally): The upcoming national diagnostics recommendation will include “suositellut aikarajat erikoissairaanhoitoon eri diagnostiikan polun vaiheille” (recommended time limits in specialist care), to be carried out (“toteutetaan”; may mean produced or implemented) before the 2030 mid-term evaluation — filha_lung_programme_2026_fi.pdf, p.16
- `q:47c7e11303` (verified locally): Finland has no quality registry for lung cancer or for any other cancer. — filha_lung_programme_2026_fi.pdf, p.21
- `q:4e702a20fe` (verified locally): Finland has no unified national system to steer the drafting of cancer-specific treatment recommendations, or the implementation and monitoring of care pathways based on them (quality and effectiveness targets/indicators, including access to care, and cancer-specific and generic PROMs). Existing recommendations and pathways, and the targets and indicators to be monitored, are not coordinated nationally. This maintains regional inequality in the availability and effectiveness of cancer care. — strategy_2026_2035_fi.pdf, p.33
- `q:556431a0c2` (verified locally): the patient is referred to specialist care according to local instructions — filha_lung_programme_2026_fi.pdf, p.15
- `q:5eb155decc` (verified locally): Report evidence for pathway stage 'Imaging' — keuhkosyoparaportti_2019_2023.html, §4.1.1 Toteamistapa
- `q:614febebf2` (verified locally): When (p.24): > “Väliarvio toteutetaan vuonna 2030, ohjelman puolivälissä ja loppuarviointi vuonna 2036. Eri > osa-alueiden suositukset toteutetaan ennen väliarviointia.” — filha_lung_programme_2026_fi.pdf, p.24
- `q:7885b0974f` (verified locally): Report evidence for pathway stage 'Diagnosis' — keuhkosyoparaportti_2019_2023.html, §4.1.3 Levinneisyystiedon kattavuus
- `q:82b59905ad` (verified locally): the organisation of care varies by wellbeing services county — filha_lung_programme_2026_fi.pdf, p.15
- `q:82d365cd2c` (verified locally): “Tällä hetkellä keuhkosyöpään liittyvien tietojen raportointi, kerääminen ja tallentaminen on puutteellista”; nationally uniform recording instructions (“yhtenäiset kirjaamisohjeet”) must be ensured — filha_lung_programme_2026_fi.pdf, p.21
- `q:8c9c032c25` (verified locally): Policy evidence for pathway stage 'Referral' — filha_lung_programme_2026_fi.pdf, p.16
- `q:8f358a9de6` (verified locally): p.16: > “Tämän ohjelman yhtenä toimenpiteenä tuotetaan kansallinen suositus keuhkosyöpien diagnostiikasta. Se > sisältää myös lähetekriteerit perusterveydenhuollolle ja suositellut aikarajat erikoissairaanhoitoon > eri diagnostiikan polun vaiheille.” — filha_lung_programme_2026_fi.pdf, p.16
- `q:950a2f797b` (verified locally): Reporting, collection and storage of lung cancer data is currently incomplete. — filha_lung_programme_2026_fi.pdf, p.21
- `q:abcbb06ae3` (verified locally): 2026–2028: guidance on a named doctor, nurse or specialist worker coordinating cancer care. 2029–2031: wellbeing services counties have adopted it. — roadmap_2026_2031_fi.pdf, p.32
- `q:ccda20dce9` (verified locally): Finland has no national system steering cancer pathways or their monitoring, “mukaan lukien hoitoonpääsy” — strategy_2026_2035_fi.pdf, p.33
- `q:cd51b9d5b6` (verified locally): So: the strategy ties its access-time indicator to the THL 21/2016 definitions. The lung cancer report (§3.3) also used “Hoitoonpääsyn seuranta syövän hoidossa (THL 2016)” to choose its procedure codes. The THL document itself is not in data/raw/, so its content (16 cancers, in force 1 Jan 2017) sta — keuhkosyoparaportti_2019_2023.html, §3.3 Menetelmät
- `q:fc81032a80` (verified locally): Measure 1.2.3: Create an operating model and guidance for a named worker responsible for coordinating cancer care. — roadmap_2026_2031_fi.pdf, p.32
- `rec:1` (recommendation (ours)): Team recommendation 1: Counties report access times using the THL 21/2016 definitions, with handover alerts. Each wellbeing services county reports lung cancer access times (referral → first specialist visit → diagnosis → treatment start) using the definitions in THL's Hoitoonpääsyn seuranta syövän hoidossa (Ohjaus 21/2016). Until national target times exist, flag stalled handovers. — recommendations.md, §1. Counties report access times using the THL 21/2016 definitions, with handover alerts
- `rec:2` (recommendation (ours)): Team recommendation 2: A KYS-style referral template, a persistent-symptoms rule and a named contact. Adopt a standard referral content list and template, modelled on KYS. • Add a rule for primary care: if symptoms persist after a normal X-ray, refer for a pulmonologist assessment. • Name a contact person for the diagnostic phase, from referral to diagnosis. — recommendations.md, §2. A KYS-style referral template, a persistent-symptoms rule and a named contact
- `rec:3` (recommendation (ours)): Team recommendation 3: Report recording completeness per county: stage, drug treatment, MDT coding. Publish, per county, how completely stage, drug treatment and MDT meetings are recorded. Read county ‘gaps’ in these fields as data-quality signals first. — recommendations.md, §3. Report recording completeness per county: stage, drug treatment, MDT coding
- `reg:kys_persistent` (verified by Hellu): KYS: refer persistent unexplained symptoms even if the X-ray is clear — pathway_brief.md, 6. Regional pathways compared
- `reg:kys_template` (verified by Hellu): Only KYS lists required referral content and provides a referral template — pathway_brief.md, 6. Regional pathways compared
- `thl:21_2016` (verified by Hellu): THL Ohjaus 21/2016 defines how cancer access times are recorded, for 16 cancers — pathway_brief.md, 6. Regional pathways compared
