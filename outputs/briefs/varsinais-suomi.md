# Varsinais-Suomi: lung cancer pathway brief

Status: **validated** · gemini-4-argon (thinking HIGH) · 2026-11-14T12:11:25+00:00 · attempts: 1

## Where do we lag?

**Varsinais-Suomi lags national figures in crude shares of curative, life-prolonging and symptomatic treatment and recorded MDT meetings, while its crude share with no treatment record within 12 months is higher.** `cty:curative:Varsinais_Suomen_hyvinvointialue, cty:life_prolonging:Varsinais_Suomen_hyvinvointialue, cty:symptomatic:Varsinais_Suomen_hyvinvointialue, cty:mdt_recorded:Varsinais_Suomen_hyvinvointialue, cty:no_treatment_record:Varsinais_Suomen_hyvinvointialue`

- In Varsinais-Suomi, the crude curative treatment share is 24.3% (95% CI 22.1–26.6; n=349/1437) versus 27.0% (4009/14873) nationally, and the 95% confidence interval excludes the national value. `cty:curative:Varsinais_Suomen_hyvinvointialue, nat:curative`
- In figures digitised from Kuva 16 (precision ±0.5 percentage points), the age-adjusted curative gap holds for men at 22.7% versus 26.7% nationally (95% confidence interval bar hidden inside the dot, half-width < ~3.3 percentage points), whereas women are at 27.4% (95% CI 23.1–31.8) versus 26.9% nationally, where the 95% confidence interval includes the national value. `k16:curative:men:Varsinais_Suomen_hyvinvointialue, k16:curative:men:national, k16:curative:women:Varsinais_Suomen_hyvinvointialue, k16:curative:women:national`
- The county's crude share is 9.7% (95% CI 8.3–11.4; n=140/1437) versus 30.4% (4522/14873) nationally for life-prolonging treatment and 30.8% (95% CI 28.5–33.3; n=443/1437) versus 39.5% (5871/14873) nationally for symptomatic treatment, with the 95% confidence intervals excluding the national values. `cty:life_prolonging:Varsinais_Suomen_hyvinvointialue, nat:life_prolonging, cty:symptomatic:Varsinais_Suomen_hyvinvointialue, nat:symptomatic`
- The crude share with no treatment record within 12 months is 43.1% (95% CI 40.5–45.6; n=619/1437) versus 27.5% (4089/14873) nationally, and the crude share with an MDT meeting recorded is 1.6% (95% CI 1.1–2.4; n=23/1437) versus 6.0% (893/14873) nationally; the 95% confidence intervals exclude the national values. `cty:no_treatment_record:Varsinais_Suomen_hyvinvointialue, nat:no_treatment_record, cty:mdt_recorded:Varsinais_Suomen_hyvinvointialue, nat:mdt_recorded`

## How sure are we?

**High crude shares with no treatment record suggest unrecorded care may partly explain low treatment figures, while missing stage data and unmeasured pathway dates limit what public data show.** `cty:no_treatment_record:Varsinais_Suomen_hyvinvointialue, bs:coverage:Treatment_start, bs:coverage:Diagnosis, q:7885b0974f`

- Because Varsinais-Suomi's 43.1% crude share with no treatment record within 12 months exceeds the 27.5% national figure and mixes untreated patients with unrecorded care, we infer as a data-quality signal that low crude treatment shares may partly reflect unrecorded treatment, whereas a journal article shows HILMO matches Cancer Registry diagnoses for about 90% of most cancer types. `cty:no_treatment_record:Varsinais_Suomen_hyvinvointialue, nat:no_treatment_record, bs:coverage:Treatment_start, lit:hilmo_90`
- County treatment shares are crude and not adjusted for age or stage because stage at diagnosis is missing for ~48% of new patients, and the 1.6% crude MDT share reflects recording practice rather than care because HILMO captures specialised care procedures only from direct patient contacts. `bs:coverage:Diagnosis, q:7885b0974f, cty:mdt_recorded:Varsinais_Suomen_hyvinvointialue, bs:coverage:MDT, q:39e6ba43a9`
- In public report data, primary care visits are not included in the report's data, occupational health is not mentioned, symptom onset and referrals are unmeasured, imaging appears only as the diagnostic basis in approximately 20% of cases, and specialist visits (93.6% within 12 months) and treatments lack start dates. `bs:coverage:Symptoms, bs:coverage:Primary_care_occupational_health, q:323de0d90d, bs:coverage:Referral, bs:coverage:Imaging, q:5eb155decc, bs:coverage:First_specialist_visit, bs:coverage:Treatment_start`
- Preliminary, unpublished national figures indicate lung cancer takes 155 days on average from first symptoms to first treatment in Finland (56 days patient delay, 41 days primary care interval, and 58 days in specialist care) versus 107 days in Sweden and 67 days in Denmark, but county waiting times are unknown. `mot:total_fi, mot:patient, mot:primary, mot:specialist, mot:total_se, mot:total_dk`

## What should we do first?

**The team recommends auditing stage, drug treatment and MDT recording completeness first, reporting access times using THL guidance 21/2016 definitions, and standardising referrals and diagnostic coordination.** `rec:3, rec:1, rec:2, q:950a2f797b, thl:21_2016, q:37bb4c3b38`

- Given the 43.1% crude share with no treatment record, 9.7% crude life-prolonging share and 1.6% crude MDT share, the team recommends publishing county recording completeness for stage, drug treatment and MDT coding as data-quality signals first, as data reporting is currently incomplete and the roadmap plans a quality registry with 90% coverage. `rec:3, cty:no_treatment_record:Varsinais_Suomen_hyvinvointialue, cty:life_prolonging:Varsinais_Suomen_hyvinvointialue, cty:mdt_recorded:Varsinais_Suomen_hyvinvointialue, q:7885b0974f, q:bfa4196bfd, q:950a2f797b, q:82d365cd2c, q:f540c706f8, q:47c7e11303`
- Because the Health Care Act sets no maximum time for a cancer suspicion and national monitoring is lacking, the team recommends reporting access times from referral to treatment start using THL guidance 21/2016 definitions (16 cancers) with handover alerts, as the roadmap plans national pathways by 2026–2028 and Filha's diagnostics recommendation is due before the 2030 mid-term evaluation. `rec:1, law:no_max, thl:21_2016, q:24169121a4, q:ccda20dce9, q:20d6ca414e, q:def306014c, q:432c0e51d6, q:614febebf2`
- Because referrals follow local instructions and mentor insight notes a weak referral gets lower specialist urgency, the team recommends a standard referral template, a primary-care rule referring persistent symptoms after a normal X-ray to a pulmonologist, and a named diagnostic contact person, while the roadmap plans referral criteria and coordinator guidance by 2026–2028. `rec:2, mentor:kaisa_referral, q:556431a0c2, q:37bb4c3b38, q:c61439b30f, q:29b792498e, q:fc81032a80, q:abcbb06ae3, q:050ee09ebe`

## Review flags (for human review only)

_Flags are for human review only; they never change the brief's status or approve it._

- [medium] `where_we_lag.headline`: Missing required caveat from the cited claims: the listed treatment and recording categories overlap (patients can fall into more than one category), and the county shares are not age- or stage-adjusted.
- [medium] `where_we_lag.details[2]`: Missing required caveat from the cited claims that the treatment categories overlap.
- [medium] `where_we_lag.details[3]`: Missing required caveat from the cited claims that these categories overlap.
- [low] `how_sure_are_we.details[1]`: Imprecise causal wording: missing stage data (~48%) explains why the treatment shares cannot be stage-adjusted, not why Taulukko 11 shares are not age-adjusted (Kuva 16 provides age-adjusted curative shares).
- [low] `how_sure_are_we.details[2]`: Minor imprecision: the cited quote states diagnosis is based on clinical examination alone (such as imaging) in approximately 20% of cases rather than imaging specifically, and the 93.6% specialist visit share is a national figure (no county breakdown) without being labelled as national.
- [medium] `what_to_do_first.details[0]`: Missing required caveat from the cited county claims that the listed categories overlap.

## Claims cited

- `bs:coverage:Diagnosis` (verified locally): Pathway stage 'Diagnosis' is measured in public data: yes (by county: yes (Kuva 7, 10, 13: PNG only)) — keuhkosyoparaportti_2019_2023.html, §4.1, Taulukko 2–4, Kuva 5–13
- `bs:coverage:First_specialist_visit` (verified locally): Pathway stage 'First specialist visit' is measured in public data: partly (by county: no) — keuhkosyoparaportti_2019_2023.html, §3.1, §4.2, Taulukko 5
- `bs:coverage:Imaging` (verified locally): Pathway stage 'Imaging' is measured in public data: partly (by county: partly (Kuva 7, PNG only)) — keuhkosyoparaportti_2019_2023.html, §4.1.1, Taulukko 2, Kuva 5–7
- `bs:coverage:MDT` (verified locally): Pathway stage 'MDT' is measured in public data: partly (by county: yes (Taulukko 11)) — keuhkosyoparaportti_2019_2023.html, §3.3, §4.2, Taulukko 5, 10, 11, 13
- `bs:coverage:Primary_care_occupational_health` (verified locally): Pathway stage 'Primary care / occupational health' is measured in public data: no (by county: no) — keuhkosyoparaportti_2019_2023.html, §3.3
- `bs:coverage:Referral` (verified locally): Pathway stage 'Referral' is measured in public data: no (by county: no) — keuhkosyoparaportti_2019_2023.html, whole report (no relevant data found)
- `bs:coverage:Symptoms` (verified locally): Pathway stage 'Symptoms' is measured in public data: no (by county: no) — keuhkosyoparaportti_2019_2023.html, whole report (no relevant data found)
- `bs:coverage:Treatment_start` (verified locally): Pathway stage 'Treatment start' is measured in public data: partly (by county: yes (type only, Taulukko 11)) — keuhkosyoparaportti_2019_2023.html, §4.2, §4.2.2, Taulukko 6–9, 11, 12, Kuva 14, 17
- `cty:curative:Varsinais_Suomen_hyvinvointialue` (verified locally): Varsinais-Suomen hyvinvointialue: curative treatment 24.3% (95% CI 22.1–26.6; n=349/1437), below vs national 27.0% — keuhkosyoparaportti_2019_2023.html, Taulukko 11
- `cty:life_prolonging:Varsinais_Suomen_hyvinvointialue` (verified locally): Varsinais-Suomen hyvinvointialue: life-prolonging treatment 9.7% (95% CI 8.3–11.4; n=140/1437), below vs national 30.4% — keuhkosyoparaportti_2019_2023.html, Taulukko 11
- `cty:mdt_recorded:Varsinais_Suomen_hyvinvointialue` (verified locally): Varsinais-Suomen hyvinvointialue: MDT meeting recorded 1.6% (95% CI 1.1–2.4; n=23/1437), below vs national 6.0% — keuhkosyoparaportti_2019_2023.html, Taulukko 11
- `cty:no_treatment_record:Varsinais_Suomen_hyvinvointialue` (verified locally): Varsinais-Suomen hyvinvointialue: no treatment record within 12 months 43.1% (95% CI 40.5–45.6; n=619/1437), above vs national 27.5% — keuhkosyoparaportti_2019_2023.html, Taulukko 11
- `cty:symptomatic:Varsinais_Suomen_hyvinvointialue` (verified locally): Varsinais-Suomen hyvinvointialue: symptomatic treatment 30.8% (95% CI 28.5–33.3; n=443/1437), below vs national 39.5% — keuhkosyoparaportti_2019_2023.html, Taulukko 11
- `k16:curative:men:Varsinais_Suomen_hyvinvointialue` (verified locally): Varsinais-Suomen hyvinvointialue: age-adjusted curative treatment share, men, 22.7% — keuhkosyoparaportti_2019_2023.html, Kuva 16
- `k16:curative:men:national` (verified locally): Finland (national reference line): age-adjusted curative treatment share, men, 26.7% — keuhkosyoparaportti_2019_2023.html, Kuva 16
- `k16:curative:women:Varsinais_Suomen_hyvinvointialue` (verified locally): Varsinais-Suomen hyvinvointialue: age-adjusted curative treatment share, women, 27.4% (95% CI 23.1–31.8) — keuhkosyoparaportti_2019_2023.html, Kuva 16
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
- `q:20d6ca414e` (verified locally): “Valtakunnallisesti ei ole ollut tarkkaa yhtenäistä ohjeistusta siitä, millä aikataululla diagnostiikan eri osa-alueet tulisi olla tehtyinä”; regional variation in diagnostic speed is large. The programme itself sets no day-based targets — filha_lung_programme_2026_fi.pdf, p.4
- `q:24169121a4` (verified locally): Strategy p.5 (= PDF p.5), “Strategiset tavoitteet”, indicator under “Varmistetaan yhdenvertainen ja vaikuttava syövänhoito”: > “Potilaat pääsevät hoitoon tavoiteaikojen puitteissa” > “ THL (Ohjaus 21/2016). Hoitoonpääsyn seuranta syövän hoidossa.” — strategy_2026_2035_fi.pdf, p.5
- `q:29b792498e` (verified locally): Policy evidence for pathway stage 'Referral' — filha_lung_programme_2026_fi.pdf, p.16
- `q:323de0d90d` (verified locally): Report evidence for pathway stage 'Primary care / occupational health' — keuhkosyoparaportti_2019_2023.html, §3.3 Menetelmät
- `q:37bb4c3b38` (verified locally): Policy evidence for pathway stage 'Referral' — roadmap_2026_2031_fi.pdf, p.52; p.106
- `q:39e6ba43a9` (verified locally): Report evidence for pathway stage 'MDT' — keuhkosyoparaportti_2019_2023.html, §3.3 Menetelmät
- `q:432c0e51d6` (verified locally): The upcoming national diagnostics recommendation will include “suositellut aikarajat erikoissairaanhoitoon eri diagnostiikan polun vaiheille” (recommended time limits in specialist care), due before the 2030 mid-term evaluation — filha_lung_programme_2026_fi.pdf, p.16
- `q:47c7e11303` (verified locally): Finland has no quality registry for lung cancer or for any other cancer. — filha_lung_programme_2026_fi.pdf, p.21
- `q:556431a0c2` (verified locally): the patient is referred to specialist care according to local instructions — filha_lung_programme_2026_fi.pdf, p.15
- `q:5eb155decc` (verified locally): Report evidence for pathway stage 'Imaging' — keuhkosyoparaportti_2019_2023.html, §4.1.1 Toteamistapa
- `q:614febebf2` (verified locally): When (p.24): > “Väliarvio toteutetaan vuonna 2030, ohjelman puolivälissä ja loppuarviointi vuonna 2036. Eri > osa-alueiden suositukset toteutetaan ennen väliarviointia.” — filha_lung_programme_2026_fi.pdf, p.24
- `q:7885b0974f` (verified locally): Report evidence for pathway stage 'Diagnosis' — keuhkosyoparaportti_2019_2023.html, §4.1.3 Levinneisyystiedon kattavuus
- `q:82d365cd2c` (verified locally): “Tällä hetkellä keuhkosyöpään liittyvien tietojen raportointi, kerääminen ja tallentaminen on puutteellista”; nationally uniform recording instructions (“yhtenäiset kirjaamisohjeet”) must be ensured — filha_lung_programme_2026_fi.pdf, p.21
- `q:950a2f797b` (verified locally): Reporting, collection and storage of lung cancer data is currently incomplete. — filha_lung_programme_2026_fi.pdf, p.21
- `q:abcbb06ae3` (verified locally): 2026–2028: guidance on a named doctor, nurse or specialist worker coordinating cancer care. 2029–2031: wellbeing services counties have adopted it. — roadmap_2026_2031_fi.pdf, p.32
- `q:bfa4196bfd` (verified locally): MDT coding: 21.6–37.4% in Sisä-Suomi counties, 0 records in 4 counties. “…ei kuvaa kattavasti moniammatillisen käsittelyn laajuutta” — keuhkosyoparaportti_2019_2023.html, §3.3 Menetelmät
- `q:c61439b30f` (verified locally): 2026–2028: standardised referral criteria and symptom-based models included in the national pathways of at least the five most common cancers. — roadmap_2026_2031_fi.pdf, p.53
- `q:ccda20dce9` (verified locally): Finland has no national system steering cancer pathways or their monitoring, “mukaan lukien hoitoonpääsy” — strategy_2026_2035_fi.pdf, p.33
- `q:def306014c` (verified locally): p.57, timetable: > “2026–2028: Kansalliset hoitoketjukuvaukset tehty viidestä syövästä ja syöpäkohtaiset > hoitoonpääsyajat on määritetty.” — roadmap_2026_2031_fi.pdf, p.57
- `q:f540c706f8` (verified locally): A national quality registry is planned; indicator: data incl. stage (“ml. levinneisyystieto”) at 90% coverage — roadmap_2026_2031_fi.pdf, p.60
- `q:fc81032a80` (verified locally): Measure 1.2.3: Create an operating model and guidance for a named worker responsible for coordinating cancer care. — roadmap_2026_2031_fi.pdf, p.32
- `rec:1` (recommendation (ours)): Team recommendation 1: Counties report access times using the THL 21/2016 definitions, with handover alerts. Each wellbeing services county reports lung cancer access times (referral → first specialist visit → diagnosis → treatment start) using the definitions in THL's Hoitoonpääsyn seuranta syövän hoidossa (Ohjaus 21/2016). Until national target times exist, flag stalled handovers. — recommendations.md, §1. Counties report access times using the THL 21/2016 definitions, with handover alerts
- `rec:2` (recommendation (ours)): Team recommendation 2: A KYS-style referral template, a persistent-symptoms rule and a named contact. Adopt a standard referral content list and template, modelled on KYS. • Add a rule for primary care: if symptoms persist after a normal X-ray, refer for a pulmonologist assessment. • Name a contact person for the diagnostic phase, from referral to diagnosis. — recommendations.md, §2. A KYS-style referral template, a persistent-symptoms rule and a named contact
- `rec:3` (recommendation (ours)): Team recommendation 3: Report recording completeness per county: stage, drug treatment, MDT coding. Publish, per county, how completely stage, drug treatment and MDT meetings are recorded. Read county ‘gaps’ in these fields as data-quality signals first. — recommendations.md, §3. Report recording completeness per county: stage, drug treatment, MDT coding
- `thl:21_2016` (verified by Hellu): THL Ohjaus 21/2016 defines how cancer access times are recorded, for 16 cancers — pathway_brief.md, 6. Regional pathways compared
