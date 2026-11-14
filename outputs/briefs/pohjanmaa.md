# Pohjanmaa: lung cancer pathway brief

Status: **validated** · gemini-4-argon (thinking HIGH) · 2026-11-14T13:46:42+00:00 · attempts: 2

## Where do we lag?

**With overlapping treatment categories, Pohjanmaa's crude 12-month no-treatment-record share is 22.9% (95% CI 19.3–27.1) versus 27.5% nationally and crude MDT recording is 6.9% (95% CI 4.9–9.6) versus 6.0% nationally.** `cty:no_treatment_record:Pohjanmaan_hyvinvointialue, nat:no_treatment_record, cty:mdt_recorded:Pohjanmaan_hyvinvointialue, nat:mdt_recorded`

- Across overlapping treatment categories, Pohjanmaa's crude curative treatment share is 27.8% (95% CI 23.9–32.2; n=125/449) versus 27.0% (4009/14873) nationally and its crude symptomatic treatment share is 36.1% (95% CI 31.8–40.6; n=162/449) versus 39.5% (5871/14873) nationally, with each 95% confidence interval including the national value. `cty:curative:Pohjanmaan_hyvinvointialue, nat:curative, cty:symptomatic:Pohjanmaan_hyvinvointialue, nat:symptomatic`
- In overlapping treatment categories, Pohjanmaa's crude life-prolonging treatment share is 43.0% (95% CI 38.5–47.6; n=193/449), whose 95% confidence interval excludes the national 30.4% (4522/14873), while crude MDT recording is 6.9% (95% CI 4.9–9.6; n=31/449), whose 95% confidence interval includes the national 6.0% (893/14873) and measures recording practice rather than care. `cty:life_prolonging:Pohjanmaan_hyvinvointialue, nat:life_prolonging, cty:mdt_recorded:Pohjanmaan_hyvinvointialue, nat:mdt_recorded, bs:coverage:MDT`
- A crude 22.9% (95% CI 19.3–27.1; n=103/449) of Pohjanmaa patients have no treatment record within 12 months versus 27.5% (4089/14873) nationally, while preliminary national averages show 155 days from symptoms to treatment in Finland (56 days patient delay, 41 days primary care, 58 days specialist care) versus 107 days in Sweden and 67 days in Denmark. `cty:no_treatment_record:Pohjanmaan_hyvinvointialue, nat:no_treatment_record, mot:total_fi, mot:total_se, mot:total_dk, mot:patient, mot:primary, mot:specialist`

## How sure are we?

**Pohjanmaa's crude 22.9% (95% CI 19.3–27.1) no-treatment-record share versus 27.5% nationally suggests relatively complete recording by inference, but county shares are crude and key stages lack data.** `cty:no_treatment_record:Pohjanmaan_hyvinvointialue, nat:no_treatment_record, fig:age_adjusted_only_kuva16, bs:coverage:Diagnosis, bs:coverage:Referral`

- Because 'no treatment record within 12 months' mixes untreated patients and unrecorded treatment, Pohjanmaa's crude 22.9% (95% CI 19.3–27.1; n=103/449) having a 95% confidence interval entirely below the national 27.5% (4089/14873) is consistent with relatively complete treatment recording as an inference, not a finding, while a journal article's 90% HILMO concordance concerns diagnoses only. `cty:no_treatment_record:Pohjanmaan_hyvinvointialue, nat:no_treatment_record, bs:coverage:Treatment_start, lit:hilmo_90`
- The county shares in Taulukko 11 are crude and not age-adjusted; in the 2019–2023 report, county-level age-adjusted shares appear only in Kuva 16 (by sex, with 95% CIs), where the digitised national curative reference lines are 26.7% for men and 26.9% for women (±0.5 percentage points), with no digitised county value for Pohjanmaa. `fig:age_adjusted_only_kuva16, k16:curative:men:national, k16:curative:women:national`
- As a separate limitation from age adjustment, the crude county shares cannot be stage-adjusted because stage at diagnosis is missing for about 48% of patients, and HILMO records specialist procedures only from direct patient contacts, so MDT figures do not comprehensively describe multidisciplinary review. `bs:coverage:Diagnosis, q:7885b0974f, bs:coverage:MDT, q:39e6ba43a9`
- Public data do not measure symptoms, referrals, county first specialist visits (93.6% nationally within 12 months) or treatment start dates; primary care visits are not included in the report's data, occupational health is unmentioned, and imaging appears only indirectly where diagnosis rests on clinical examination alone in approximately 20% of patients. `bs:coverage:Symptoms, bs:coverage:Referral, bs:coverage:First_specialist_visit, bs:coverage:Treatment_start, bs:coverage:Primary_care_occupational_health, q:323de0d90d, bs:coverage:Imaging, q:5eb155decc`

## What should we do first?

**The team recommends tracking THL 21/2016 access times with handover alerts, standardising referrals and diagnostic contacts, and publishing county recording completeness for stage, drug treatment and MDT coding.** `rec:1, rec:2, rec:3, thl:21_2016, q:950a2f797b`

- Because the Health Care Act sets no legal maximum time for a cancer suspicion and national access-time monitoring is lacking, the team recommends reporting referral-to-treatment access times using THL guidance Ohjaus 21/2016 definitions (for 16 cancers) and flagging stalled handovers while the STM roadmap (measure 3.1.2) plans cancer-specific access times for five cancers by 2026–2028. `rec:1, law:no_max, q:4e702a20fe, q:ccda20dce9, thl:21_2016, q:def306014c, q:b326e35410`
- Because referrals follow local instructions and mentor insight notes weak referrals get lower urgency ratings, the team recommends a referral template and persistent-symptoms rule after a normal X-ray, modelled on KYS's regional pathway document, while the Filha programme's diagnostics recommendation (with primary-care referral criteria and recommended time limits) is to be carried out before the 2030 mid-term evaluation. `rec:2, q:556431a0c2, mentor:kaisa_referral, reg:kys_template, reg:kys_persistent, reg:only_kys_xray, q:29b792498e, q:8f358a9de6, q:614febebf2`
- Because reviewed regional pathway documents name no contact person for the diagnostic phase, the team recommends naming a diagnostic contact person from referral to diagnosis, while the STM roadmap plans standardised referral criteria and symptom-based models (measure 2.5.2) and guidance on a named care-coordinator model (measure 1.2.3) by 2026–2028, with county adoption by 2029–2031. `rec:2, reg:named_contact, q:0780bf74b0, q:37bb4c3b38, q:c61439b30f, q:fc81032a80, q:050ee09ebe, q:abcbb06ae3`
- With crude MDT recording at 6.9% (95% CI 4.9–9.6; n=31/449) versus 6.0% (893/14873) nationally and stage missing for about 48% of patients, the team recommends publishing county recording completeness for stage, drug treatment and MDT coding while data reporting is incomplete and the STM roadmap (measure 3.2.1) plans a quality registry (decree update by 2026–2028, annual reports by 2029–2031). `rec:3, cty:mdt_recorded:Pohjanmaan_hyvinvointialue, nat:mdt_recorded, bs:coverage:Diagnosis, q:7885b0974f, q:950a2f797b, q:82d365cd2c, q:f07a34a300`

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
- `q:29b792498e` (verified locally): Policy evidence for pathway stage 'Referral' — filha_lung_programme_2026_fi.pdf, p.16
- `q:323de0d90d` (verified locally): Report evidence for pathway stage 'Primary care / occupational health' — keuhkosyoparaportti_2019_2023.html, §3.3 Menetelmät
- `q:37bb4c3b38` (verified locally): Policy evidence for pathway stage 'Referral' — roadmap_2026_2031_fi.pdf, p.52; p.106
- `q:39e6ba43a9` (verified locally): Report evidence for pathway stage 'MDT' — keuhkosyoparaportti_2019_2023.html, §3.3 Menetelmät
- `q:4e702a20fe` (verified locally): Finland has no unified national system to steer the drafting of cancer-specific treatment recommendations, or the implementation and monitoring of care pathways based on them (quality and effectiveness targets/indicators, including access to care, and cancer-specific and generic PROMs). Existing recommendations and pathways, and the targets and indicators to be monitored, are not coordinated nationally. This maintains regional inequality in the availability and effectiveness of cancer care. — strategy_2026_2035_fi.pdf, p.33
- `q:556431a0c2` (verified locally): the patient is referred to specialist care according to local instructions — filha_lung_programme_2026_fi.pdf, p.15
- `q:5eb155decc` (verified locally): Report evidence for pathway stage 'Imaging' — keuhkosyoparaportti_2019_2023.html, §4.1.1 Toteamistapa
- `q:614febebf2` (verified locally): When (p.24): > “Väliarvio toteutetaan vuonna 2030, ohjelman puolivälissä ja loppuarviointi vuonna 2036. Eri > osa-alueiden suositukset toteutetaan ennen väliarviointia.” — filha_lung_programme_2026_fi.pdf, p.24
- `q:7885b0974f` (verified locally): Report evidence for pathway stage 'Diagnosis' — keuhkosyoparaportti_2019_2023.html, §4.1.3 Levinneisyystiedon kattavuus
- `q:82d365cd2c` (verified locally): “Tällä hetkellä keuhkosyöpään liittyvien tietojen raportointi, kerääminen ja tallentaminen on puutteellista”; nationally uniform recording instructions (“yhtenäiset kirjaamisohjeet”) must be ensured — filha_lung_programme_2026_fi.pdf, p.21
- `q:8f358a9de6` (verified locally): p.16: > “Tämän ohjelman yhtenä toimenpiteenä tuotetaan kansallinen suositus keuhkosyöpien diagnostiikasta. Se > sisältää myös lähetekriteerit perusterveydenhuollolle ja suositellut aikarajat erikoissairaanhoitoon > eri diagnostiikan polun vaiheille.” — filha_lung_programme_2026_fi.pdf, p.16
- `q:950a2f797b` (verified locally): Reporting, collection and storage of lung cancer data is currently incomplete. — filha_lung_programme_2026_fi.pdf, p.21
- `q:abcbb06ae3` (verified locally): 2026–2028: guidance on a named doctor, nurse or specialist worker coordinating cancer care. 2029–2031: wellbeing services counties have adopted it. — roadmap_2026_2031_fi.pdf, p.32
- `q:b326e35410` (verified locally): National pathways with “syöpäkohtaiset hoitoonpääsyajat” for five (unnamed) cancers in 2026–2028, Nordic model — roadmap_2026_2031_fi.pdf, p.57
- `q:c61439b30f` (verified locally): 2026–2028: standardised referral criteria and symptom-based models included in the national pathways of at least the five most common cancers. — roadmap_2026_2031_fi.pdf, p.53
- `q:ccda20dce9` (verified locally): Finland has no national system steering cancer pathways or their monitoring, “mukaan lukien hoitoonpääsy” — strategy_2026_2035_fi.pdf, p.33
- `q:def306014c` (verified locally): p.57, timetable: > “2026–2028: Kansalliset hoitoketjukuvaukset tehty viidestä syövästä ja syöpäkohtaiset > hoitoonpääsyajat on määritetty.” — roadmap_2026_2031_fi.pdf, p.57
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
