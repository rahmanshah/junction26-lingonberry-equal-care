# Pohjanmaa: lung cancer pathway brief

Status: **validated** · gemini-4-argon (thinking HIGH) · 2026-11-14T12:11:32+00:00 · attempts: 1

## Where do we lag?

**Pohjanmaa's crude curative treatment share is 27.8% (95% CI 23.9–32.2; n=125/449) versus 27.0% nationally, with the 95% confidence interval including the national value while pathway wait times remain unmeasured.** `cty:curative:Pohjanmaan_hyvinvointialue, nat:curative, bs:coverage:Treatment_start`

- Across overlapping treatment categories where a patient can have several, Pohjanmaa's crude curative share is 27.8% (95% CI 23.9–32.2; n=125/449) versus 27.0% (4009/14873) nationally and crude symptomatic treatment is 36.1% (95% CI 31.8–40.6; n=162/449) versus 39.5% (5871/14873), with each 95% confidence interval including the national value. `cty:curative:Pohjanmaan_hyvinvointialue, nat:curative, cty:symptomatic:Pohjanmaan_hyvinvointialue, nat:symptomatic`
- Pohjanmaa's crude life-prolonging treatment share is 43.0% (95% CI 38.5–47.6; n=193/449), whose 95% confidence interval excludes the national 30.4% (4522/14873) above it, while crude MDT meeting recording is 6.9% (95% CI 4.9–9.6; n=31/449) versus 6.0% (893/14873) nationally, with its 95% confidence interval including the national value. `cty:life_prolonging:Pohjanmaan_hyvinvointialue, nat:life_prolonging, cty:mdt_recorded:Pohjanmaan_hyvinvointialue, nat:mdt_recorded`
- MDT records measure recording practice rather than care because HILMO captures specialist procedures only from direct patient contacts, and while county wait times are unmeasured, preliminary national figures average 155 days from symptoms to treatment in Finland (56 days patient delay, 41 days primary care, 58 days specialist care) versus 107 in Sweden and 67 in Denmark. `bs:coverage:MDT, q:39e6ba43a9, bs:coverage:Treatment_start, mot:total_fi, mot:total_se, mot:total_dk, mot:patient, mot:primary, mot:specialist`

## How sure are we?

**Pohjanmaa's crude 22.9% (95% CI 19.3–27.1; n=103/449) share with no treatment record within 12 months excludes the national 27.5%, while public data lack stage and pathway timestamps.** `cty:no_treatment_record:Pohjanmaan_hyvinvointialue, nat:no_treatment_record, bs:coverage:Diagnosis, bs:coverage:Treatment_start`

- Because the 95% confidence interval for Pohjanmaa's crude 22.9% (95% CI 19.3–27.1; n=103/449) share with no treatment record within 12 months excludes the national 27.5% (4089/14873)—a category mixing untreated patients and unrecorded treatment—we infer this data-quality signal is consistent with relatively complete treatment recording, though not direct evidence of it. `cty:no_treatment_record:Pohjanmaan_hyvinvointialue, nat:no_treatment_record, bs:coverage:Treatment_start`
- All reported county treatment shares are crude and not adjusted for age or stage: stage at diagnosis is missing for ~48% of new patients, and Kuva 16 (digitised from a figure, precision ±0.5 percentage points, for curative treatment only by sex) provides only the national age-adjusted reference lines of 26.7% for men and 26.9% for women. `bs:coverage:Diagnosis, q:7885b0974f, k16:curative:men:national, k16:curative:women:national`
- A 2019 Lääkärilehti journal article found HILMO diagnoses matched the Cancer Registry for about 90% of most cancer types, concerning diagnosis concordance only and not treatment or MDT recording, while public data do not measure symptom onset, referral dates, imaging waits (diagnosis rests on clinical examination alone in approximately 20%), or when treatment started. `lit:hilmo_90, bs:coverage:Symptoms, bs:coverage:Referral, bs:coverage:Imaging, q:5eb155decc, bs:coverage:Treatment_start`
- Outpatient primary care visits are not included in the report's data, occupational health is not mentioned despite mentor insight that occupational health gets patients to specialist care faster and a weak referral gets a lower urgency rating, and HILMO shows 93.6% had a specialist visit within 12 months (up to 3 months pre-diagnosis) without visit dates. `bs:coverage:Primary_care_occupational_health, q:323de0d90d, mentor:hanna_occupational, mentor:kaisa_referral, bs:coverage:First_specialist_visit`

## What should we do first?

**The team recommends reporting THL guidance Ohjaus 21/2016 access times with handover alerts, standardising referrals with a diagnostic contact, and publishing county recording completeness for stage, drug treatment, and MDT.** `rec:1, rec:2, rec:3, thl:21_2016, q:82d365cd2c`

- The team recommends reporting access times from referral to first specialist visit, diagnosis, and treatment start using THL guidance Ohjaus 21/2016 definitions (for 16 cancers) and flagging stalled handovers, because the Health Care Act sets no legal maximum time for cancer suspicion, national pathway access times are planned for 2026–2028, and Filha's diagnostic time limits are due before 2030. `rec:1, thl:21_2016, law:no_max, q:ccda20dce9, q:b326e35410, q:432c0e51d6, q:614febebf2`
- The team recommends a standard referral list and template modelled on the KYS regional pathway document, referring persistent symptoms after a clear X-ray to a pulmonologist, and naming a diagnostic contact person, since referrals follow local instructions, mentor insight notes weak referrals get lower urgency, and national referral criteria and coordinator guidance are planned for 2026–2028 (county adoption 2029–2031). `rec:2, reg:kys_template, reg:kys_persistent, reg:named_contact, mentor:kaisa_referral, q:556431a0c2, q:c61439b30f, q:050ee09ebe, q:abcbb06ae3`
- The team recommends publishing county recording completeness for stage, drug treatment, and MDT coding and reading gaps as data-quality signals, since stage is missing for ~48% of patients nationally, Pohjanmaa's crude MDT recording is 6.9% (95% CI 4.9–9.6; n=31/449; 95% CI includes national 6.0%, 893/14873), data collection is incomplete, and a planned national quality registry targets 90% coverage. `rec:3, bs:coverage:Diagnosis, q:7885b0974f, cty:mdt_recorded:Pohjanmaan_hyvinvointialue, nat:mdt_recorded, q:950a2f797b, q:82d365cd2c, q:f07a34a300, q:4a856bd695, q:f540c706f8`

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
- `q:323de0d90d` (verified locally): Report evidence for pathway stage 'Primary care / occupational health' — keuhkosyoparaportti_2019_2023.html, §3.3 Menetelmät
- `q:39e6ba43a9` (verified locally): Report evidence for pathway stage 'MDT' — keuhkosyoparaportti_2019_2023.html, §3.3 Menetelmät
- `q:432c0e51d6` (verified locally): The upcoming national diagnostics recommendation will include “suositellut aikarajat erikoissairaanhoitoon eri diagnostiikan polun vaiheille” (recommended time limits in specialist care), due before the 2030 mid-term evaluation — filha_lung_programme_2026_fi.pdf, p.16
- `q:4a856bd695` (verified locally): the registry's data, including stage, allows reliable assessment and comparison of quality and effectiveness, with 90% data coverage — roadmap_2026_2031_fi.pdf, p.60
- `q:556431a0c2` (verified locally): the patient is referred to specialist care according to local instructions — filha_lung_programme_2026_fi.pdf, p.15
- `q:5eb155decc` (verified locally): Report evidence for pathway stage 'Imaging' — keuhkosyoparaportti_2019_2023.html, §4.1.1 Toteamistapa
- `q:614febebf2` (verified locally): When (p.24): > “Väliarvio toteutetaan vuonna 2030, ohjelman puolivälissä ja loppuarviointi vuonna 2036. Eri > osa-alueiden suositukset toteutetaan ennen väliarviointia.” — filha_lung_programme_2026_fi.pdf, p.24
- `q:7885b0974f` (verified locally): Report evidence for pathway stage 'Diagnosis' — keuhkosyoparaportti_2019_2023.html, §4.1.3 Levinneisyystiedon kattavuus
- `q:82d365cd2c` (verified locally): “Tällä hetkellä keuhkosyöpään liittyvien tietojen raportointi, kerääminen ja tallentaminen on puutteellista”; nationally uniform recording instructions (“yhtenäiset kirjaamisohjeet”) must be ensured — filha_lung_programme_2026_fi.pdf, p.21
- `q:950a2f797b` (verified locally): Reporting, collection and storage of lung cancer data is currently incomplete. — filha_lung_programme_2026_fi.pdf, p.21
- `q:abcbb06ae3` (verified locally): 2026–2028: guidance on a named doctor, nurse or specialist worker coordinating cancer care. 2029–2031: wellbeing services counties have adopted it. — roadmap_2026_2031_fi.pdf, p.32
- `q:b326e35410` (verified locally): National pathways with “syöpäkohtaiset hoitoonpääsyajat” for five (unnamed) cancers in 2026–2028, Nordic model — roadmap_2026_2031_fi.pdf, p.57
- `q:c61439b30f` (verified locally): 2026–2028: standardised referral criteria and symptom-based models included in the national pathways of at least the five most common cancers. — roadmap_2026_2031_fi.pdf, p.53
- `q:ccda20dce9` (verified locally): Finland has no national system steering cancer pathways or their monitoring, “mukaan lukien hoitoonpääsy” — strategy_2026_2035_fi.pdf, p.33
- `q:f07a34a300` (verified locally): A national cancer care quality registry will be set up alongside THL's Cancer Registry. — roadmap_2026_2031_fi.pdf, p.59
- `q:f540c706f8` (verified locally): A national quality registry is planned; indicator: data incl. stage (“ml. levinneisyystieto”) at 90% coverage — roadmap_2026_2031_fi.pdf, p.60
- `rec:1` (recommendation (ours)): Team recommendation 1: Counties report access times using the THL 21/2016 definitions, with handover alerts. Each wellbeing services county reports lung cancer access times (referral → first specialist visit → diagnosis → treatment start) using the definitions in THL's Hoitoonpääsyn seuranta syövän hoidossa (Ohjaus 21/2016). Until national target times exist, flag stalled handovers. — recommendations.md, §1. Counties report access times using the THL 21/2016 definitions, with handover alerts
- `rec:2` (recommendation (ours)): Team recommendation 2: A KYS-style referral template, a persistent-symptoms rule and a named contact. Adopt a standard referral content list and template, modelled on KYS. • Add a rule for primary care: if symptoms persist after a normal X-ray, refer for a pulmonologist assessment. • Name a contact person for the diagnostic phase, from referral to diagnosis. — recommendations.md, §2. A KYS-style referral template, a persistent-symptoms rule and a named contact
- `rec:3` (recommendation (ours)): Team recommendation 3: Report recording completeness per county: stage, drug treatment, MDT coding. Publish, per county, how completely stage, drug treatment and MDT meetings are recorded. Read county ‘gaps’ in these fields as data-quality signals first. — recommendations.md, §3. Report recording completeness per county: stage, drug treatment, MDT coding
- `reg:kys_persistent` (verified by Hellu): KYS: refer persistent unexplained symptoms even if the X-ray is clear — pathway_brief.md, 6. Regional pathways compared
- `reg:kys_template` (verified by Hellu): Only KYS lists required referral content and provides a referral template — pathway_brief.md, 6. Regional pathways compared
- `reg:named_contact` (verified by Hellu): No region names a contact person for the diagnostic phase — pathway_brief.md, 6. Regional pathways compared
- `thl:21_2016` (verified by Hellu): THL Ohjaus 21/2016 defines how cancer access times are recorded, for 16 cancers — pathway_brief.md, 6. Regional pathways compared
