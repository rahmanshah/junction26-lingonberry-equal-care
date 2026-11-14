# Satakunta: lung cancer pathway brief

Status: **validated** · gemini-4-argon (thinking HIGH) · 2026-11-14T13:46:31+00:00 · attempts: 1

## Where do we lag?

**Satakunta's crude MDT recording share of 0.6% (95% CI 0.2–1.5) lags the 6.0% national benchmark, and a Satakunta study found specialist care caused the biggest diagnostic delay.** `cty:mdt_recorded:Satakunnan_hyvinvointialue, nat:mdt_recorded, reg:satakunta_study`

- Across overlapping treatment categories where a patient can have several treatments, Satakunta's crude curative share is 24.5% (95% CI 21.4–27.9; n=167/682), whose 95% confidence interval includes 27.0% (4009/14873) nationally, while crude symptomatic treatment is 29.0% (95% CI 25.8–32.5; n=198/682) versus 39.5% (5871/14873) and crude life-prolonging treatment is 45.0% (95% CI 41.3–48.8; n=307/682) versus 30.4% (4522/14873), with 95% confidence intervals excluding national values. `cty:curative:Satakunnan_hyvinvointialue, nat:curative, cty:symptomatic:Satakunnan_hyvinvointialue, nat:symptomatic, cty:life_prolonging:Satakunnan_hyvinvointialue, nat:life_prolonging`
- Satakunta's crude share of patients with no treatment record within 12 months is 29.8% (95% CI 26.4–33.3; n=203/682) compared with 27.5% (4089/14873) nationally, so its 95% confidence interval includes the national value and is not distinguishable from it; this category mixes untreated patients and treatment that was not recorded. `cty:no_treatment_record:Satakunnan_hyvinvointialue, nat:no_treatment_record, bs:coverage:Treatment_start`
- An MDT meeting is recorded for a crude 0.6% (95% CI 0.2–1.5; n=4/682) of Satakunta patients versus 6.0% (893/14873) nationally, with the 95% confidence interval excluding the national value, but HILMO procedures are entered only from direct patient contacts, so MDT records measure recording practice rather than care. `cty:mdt_recorded:Satakunnan_hyvinvointialue, nat:mdt_recorded, bs:coverage:MDT, q:39e6ba43a9`
- A University of Turku regional study of Satakunta found the biggest delay from referral to diagnosis occurred in specialist care, and preliminary, unpublished national figures show 155 days from symptoms to treatment in Finland versus 107 in Sweden and 67 in Denmark, with 58 days in specialist care, 56 in patient delay, and 41 in primary care. `reg:satakunta_study, mot:total_fi, mot:total_se, mot:total_dk, mot:specialist, mot:patient, mot:primary`

## How sure are we?

**Satakunta's published table figures are crude shares that are not age-adjusted and cannot be stage-adjusted, while public data omit primary care, referrals, and treatment start dates.** `fig:age_adjusted_only_kuva16, bs:coverage:Diagnosis, bs:coverage:Primary_care_occupational_health, bs:coverage:Referral, bs:coverage:Treatment_start`

- The county table (Taulukko 11) gives crude shares that are not age-adjusted, whereas county-level age-adjusted treatment shares appear only in the report's Kuva 16 PNG figure by sex, where digitised national reference lines for curative treatment are 26.7% for men and 26.9% for women, read from the figure at about ±0.5 percentage points. `fig:age_adjusted_only_kuva16, k16:curative:men:national, k16:curative:women:national`
- Separately from age adjustment, the crude county shares cannot be stage-adjusted because stage at diagnosis is missing for about 48% of patients, even though a 2019 Lääkärilehti journal article found that HILMO hospital discharge diagnoses match the Cancer Registry for about 90% of most cancer types. `bs:coverage:Diagnosis, q:7885b0974f, lit:hilmo_90`
- Public report data do not measure symptom onset or referrals, primary care visits are not included in the report's data, occupational health is not mentioned, and imaging appears only indirectly as diagnosis based on clinical findings alone in about 20% of patients rather than imaging wait times. `bs:coverage:Symptoms, bs:coverage:Referral, bs:coverage:Primary_care_occupational_health, q:323de0d90d, bs:coverage:Imaging, q:5eb155decc`
- The report tracks whether a specialist visit occurred within 12 months (93.6% nationally) and which treatment type was recorded within 12 months, but not when specialist visits or treatments started, while Finland has no legal maximum time for a cancer suspicion under the Health Care Act (§52) and no cancer quality registry. `bs:coverage:First_specialist_visit, bs:coverage:Treatment_start, law:no_max, filha:registry, q:47c7e11303`

## What should we do first?

**The team recommends reporting THL 21/2016 access times with handover alerts, adopting a KYS-style referral template and diagnostic contact person, and publishing county stage, drug, and MDT recording.** `rec:1, rec:2, rec:3`

- Because a Satakunta regional study found the biggest diagnostic delay in specialist care, the team recommends reporting access times (referral, first specialist visit, diagnosis, and treatment start) using THL Ohjaus 21/2016 definitions for 16 cancers and flagging stalled handovers while the Filha programme's diagnostics recommendation is to be carried out before the 2030 mid-term evaluation. `rec:1, reg:satakunta_study, thl:21_2016, q:24169121a4, q:8f358a9de6, q:614febebf2, q:432c0e51d6`
- The team recommends adopting a standard referral content list and template modelled on KYS's regional pathway document and a primary-care rule to refer persistent unexplained symptoms for a pulmonologist assessment even after a normal X-ray, as KYS is the only reviewed pathway with these rules and mentor insight notes weak referrals receive lower urgency ratings in specialist care. `rec:2, reg:kys_template, reg:kys_persistent, reg:only_kys_xray, mentor:kaisa_referral`
- The team also recommends naming a contact person for the diagnostic phase from referral to diagnosis because no reviewed regional pathway document names a diagnostic-phase contact, whereas the STM roadmap's measure 1.2.3 plans national guidance on a named care-coordinator model by 2026–2028 and county adoption by 2029–2031 without specifying the care phase. `rec:2, reg:named_contact, q:fc81032a80, q:abcbb06ae3, q:050ee09ebe`
- Given Satakunta's crude recorded MDT share of 0.6% (95% CI 0.2–1.5; n=4/682) versus 6.0% (893/14873) nationally and about 48% missing stage at diagnosis nationally, the team recommends publishing per-county recording of stage, drug treatment, and MDT meetings and reading county gaps in these fields as data-quality signals alongside the Filha programme's call for uniform recording instructions. `rec:3, cty:mdt_recorded:Satakunnan_hyvinvointialue, nat:mdt_recorded, bs:coverage:Diagnosis, q:7885b0974f, q:950a2f797b, q:4c7a01d84c, q:82d365cd2c`

## Review flags (for human review only)

_Flags are for human review only; they never change the brief's status or approve it._

- [medium] `where_we_lag.headline`: Causal overreach: [reg:satakunta_study] states that the biggest delay from referral to diagnosis occurred in specialist care ('biggest delay in specialist care'), not that specialist care caused the delay.

## Claims cited

- `bs:coverage:Diagnosis` (verified locally): Pathway stage 'Diagnosis' is measured in public data: yes (by county: yes (Kuva 7, 10, 13: PNG only)) — keuhkosyoparaportti_2019_2023.html, §4.1, Taulukko 2–4, Kuva 5–13
- `bs:coverage:First_specialist_visit` (verified locally): Pathway stage 'First specialist visit' is measured in public data: partly (by county: no) — keuhkosyoparaportti_2019_2023.html, §3.1, §4.2, Taulukko 5
- `bs:coverage:Imaging` (verified locally): Pathway stage 'Imaging' is measured in public data: partly (by county: partly (Kuva 7, PNG only)) — keuhkosyoparaportti_2019_2023.html, §4.1.1, Taulukko 2, Kuva 5–7
- `bs:coverage:MDT` (verified locally): Pathway stage 'MDT' is measured in public data: partly (by county: yes (Taulukko 11)) — keuhkosyoparaportti_2019_2023.html, §3.3, §4.2, Taulukko 5, 10, 11, 13
- `bs:coverage:Primary_care_occupational_health` (verified locally): Pathway stage 'Primary care / occupational health' is measured in public data: no (by county: no) — keuhkosyoparaportti_2019_2023.html, §3.3
- `bs:coverage:Referral` (verified locally): Pathway stage 'Referral' is measured in public data: no (by county: no) — keuhkosyoparaportti_2019_2023.html, whole report (no relevant data found)
- `bs:coverage:Symptoms` (verified locally): Pathway stage 'Symptoms' is measured in public data: no (by county: no) — keuhkosyoparaportti_2019_2023.html, whole report (no relevant data found)
- `bs:coverage:Treatment_start` (verified locally): Pathway stage 'Treatment start' is measured in public data: partly (by county: yes (type only, Taulukko 11)) — keuhkosyoparaportti_2019_2023.html, §4.2, §4.2.2, Taulukko 6–9, 11, 12, Kuva 14, 17
- `cty:curative:Satakunnan_hyvinvointialue` (verified locally): Satakunnan hyvinvointialue: curative treatment 24.5% (95% CI 21.4–27.9; n=167/682), not distinguishable vs national 27.0% — keuhkosyoparaportti_2019_2023.html, Taulukko 11
- `cty:life_prolonging:Satakunnan_hyvinvointialue` (verified locally): Satakunnan hyvinvointialue: life-prolonging treatment 45.0% (95% CI 41.3–48.8; n=307/682), above vs national 30.4% — keuhkosyoparaportti_2019_2023.html, Taulukko 11
- `cty:mdt_recorded:Satakunnan_hyvinvointialue` (verified locally): Satakunnan hyvinvointialue: MDT meeting recorded 0.6% (95% CI 0.2–1.5; n=4/682), below vs national 6.0% — keuhkosyoparaportti_2019_2023.html, Taulukko 11
- `cty:no_treatment_record:Satakunnan_hyvinvointialue` (verified locally): Satakunnan hyvinvointialue: no treatment record within 12 months 29.8% (95% CI 26.4–33.3; n=203/682), not distinguishable vs national 27.5% — keuhkosyoparaportti_2019_2023.html, Taulukko 11
- `cty:symptomatic:Satakunnan_hyvinvointialue` (verified locally): Satakunnan hyvinvointialue: symptomatic treatment 29.0% (95% CI 25.8–32.5; n=198/682), below vs national 39.5% — keuhkosyoparaportti_2019_2023.html, Taulukko 11
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
- `q:4c7a01d84c` (verified locally): nationally uniform recording instructions, and their use, must be ensured — filha_lung_programme_2026_fi.pdf, p.21
- `q:5eb155decc` (verified locally): Report evidence for pathway stage 'Imaging' — keuhkosyoparaportti_2019_2023.html, §4.1.1 Toteamistapa
- `q:614febebf2` (verified locally): When (p.24): > “Väliarvio toteutetaan vuonna 2030, ohjelman puolivälissä ja loppuarviointi vuonna 2036. Eri > osa-alueiden suositukset toteutetaan ennen väliarviointia.” — filha_lung_programme_2026_fi.pdf, p.24
- `q:7885b0974f` (verified locally): Report evidence for pathway stage 'Diagnosis' — keuhkosyoparaportti_2019_2023.html, §4.1.3 Levinneisyystiedon kattavuus
- `q:82d365cd2c` (verified locally): “Tällä hetkellä keuhkosyöpään liittyvien tietojen raportointi, kerääminen ja tallentaminen on puutteellista”; nationally uniform recording instructions (“yhtenäiset kirjaamisohjeet”) must be ensured — filha_lung_programme_2026_fi.pdf, p.21
- `q:8f358a9de6` (verified locally): p.16: > “Tämän ohjelman yhtenä toimenpiteenä tuotetaan kansallinen suositus keuhkosyöpien diagnostiikasta. Se > sisältää myös lähetekriteerit perusterveydenhuollolle ja suositellut aikarajat erikoissairaanhoitoon > eri diagnostiikan polun vaiheille.” — filha_lung_programme_2026_fi.pdf, p.16
- `q:950a2f797b` (verified locally): Reporting, collection and storage of lung cancer data is currently incomplete. — filha_lung_programme_2026_fi.pdf, p.21
- `q:abcbb06ae3` (verified locally): 2026–2028: guidance on a named doctor, nurse or specialist worker coordinating cancer care. 2029–2031: wellbeing services counties have adopted it. — roadmap_2026_2031_fi.pdf, p.32
- `q:fc81032a80` (verified locally): Measure 1.2.3: Create an operating model and guidance for a named worker responsible for coordinating cancer care. — roadmap_2026_2031_fi.pdf, p.32
- `rec:1` (recommendation (ours)): Team recommendation 1: Counties report access times using the THL 21/2016 definitions, with handover alerts. Each wellbeing services county reports lung cancer access times (referral → first specialist visit → diagnosis → treatment start) using the definitions in THL's Hoitoonpääsyn seuranta syövän hoidossa (Ohjaus 21/2016). Until national target times exist, flag stalled handovers. — recommendations.md, §1. Counties report access times using the THL 21/2016 definitions, with handover alerts
- `rec:2` (recommendation (ours)): Team recommendation 2: A KYS-style referral template, a persistent-symptoms rule and a named contact. Adopt a standard referral content list and template, modelled on KYS. • Add a rule for primary care: if symptoms persist after a normal X-ray, refer for a pulmonologist assessment. • Name a contact person for the diagnostic phase, from referral to diagnosis. — recommendations.md, §2. A KYS-style referral template, a persistent-symptoms rule and a named contact
- `rec:3` (recommendation (ours)): Team recommendation 3: Report recording completeness per county: stage, drug treatment, MDT coding. Publish, per county, how completely stage, drug treatment and MDT meetings are recorded. Read county ‘gaps’ in these fields as data-quality signals first. — recommendations.md, §3. Report recording completeness per county: stage, drug treatment, MDT coding
- `reg:kys_persistent` (verified by Hellu): KYS: refer persistent unexplained symptoms even if the X-ray is clear — pathway_brief.md, 6. Regional pathways compared
- `reg:kys_template` (verified by Hellu): Only KYS lists required referral content and provides a referral template — pathway_brief.md, 6. Regional pathways compared
- `reg:named_contact` (verified by Hellu): No region names a contact person for the diagnostic phase — pathway_brief.md, 6. Regional pathways compared
- `reg:only_kys_xray` (verified by Hellu): Only KYS tells primary care what to do with a normal X-ray and continuing symptoms — pathway_brief.md, 6. Regional pathways compared
- `reg:satakunta_study` (verified by Hellu): Satakunta study: referral to diagnosis just under two months; biggest delay in specialist care — pathway_brief.md, 6. Regional pathways compared
- `thl:21_2016` (verified by Hellu): THL Ohjaus 21/2016 defines how cancer access times are recorded, for 16 cancers — pathway_brief.md, 6. Regional pathways compared
