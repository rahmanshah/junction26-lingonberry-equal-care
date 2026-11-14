# Kanta-Häme: lung cancer pathway brief

Status: **validated** · gemini-4-argon (thinking HIGH) · 2026-11-14T12:19:40+00:00 · attempts: 2

## Where do we lag?

**In Kanta-Häme, the crude symptomatic treatment share (34.2%) is below the national 39.5%, while the crude share with no treatment record within 12 months (32.1%) is above 27.5% nationally.** `cty:symptomatic:Kanta_Hämeen_hyvinvointialue, nat:symptomatic, cty:no_treatment_record:Kanta_Hämeen_hyvinvointialue, nat:no_treatment_record`

- Kanta-Häme's crude share with no treatment record within 12 months is 32.1% (95% CI 28.3–36.1; n=175/546) versus 27.5% (4089/14873) nationally, and its crude symptomatic treatment share is 34.2% (95% CI 30.4–38.3; n=187/546) versus 39.5% (5871/14873) nationally, with these 95% confidence intervals excluding the national values. `cty:no_treatment_record:Kanta_Hämeen_hyvinvointialue, nat:no_treatment_record, cty:symptomatic:Kanta_Hämeen_hyvinvointialue, nat:symptomatic`
- The county's crude curative treatment share is 23.4% (95% CI 20.1–27.2; n=128/546) compared with 27.0% (4009/14873) nationally, and its crude life-prolonging treatment share is 32.2% (95% CI 28.4–36.3; n=176/546) compared with 30.4% (4522/14873) nationally; each 95% confidence interval includes the national value. `cty:curative:Kanta_Hämeen_hyvinvointialue, nat:curative, cty:life_prolonging:Kanta_Hämeen_hyvinvointialue, nat:life_prolonging`
- Public registry data do not report county waiting times, while preliminary, unpublished national figures show 155 days on average from symptoms to treatment in Finland (versus 107 in Sweden and 67 in Denmark), with 56 days of patient delay, 41 days in primary care and 58 days in specialist care. `bs:coverage:Treatment_start, mot:total_fi, mot:total_se, mot:total_dk, mot:patient, mot:primary, mot:specialist`

## How sure are we?

**Kanta-Häme's crude share with no treatment record within 12 months (32.1% vs 27.5% nationally) is a data-quality signal suggesting lower crude treatment shares may partly reflect unrecorded treatment.** `cty:no_treatment_record:Kanta_Hämeen_hyvinvointialue, nat:no_treatment_record, bs:coverage:Treatment_start`

- Because having no treatment record within 12 months (crude 32.1% vs 27.5% nationally) mixes patients who received no treatment and treatment that was not recorded, we infer that Kanta-Häme's lower crude symptomatic share (34.2% vs 39.5%) may partly reflect unrecorded treatment, while a journal article's ~90% HILMO–Cancer Registry match covers diagnoses only. `cty:no_treatment_record:Kanta_Hämeen_hyvinvointialue, nat:no_treatment_record, cty:symptomatic:Kanta_Hämeen_hyvinvointialue, nat:symptomatic, bs:coverage:Treatment_start, lit:hilmo_90`
- County treatment shares are crude (not adjusted for age or stage): stage at diagnosis is missing for ~48% of new patients, and only national age-adjusted curative reference values (26.7% for men and 26.9% for women, digitised from a figure at about ±0.5 percentage points) are available here. `cty:curative:Kanta_Hämeen_hyvinvointialue, bs:coverage:Diagnosis, q:7885b0974f, k16:curative:men:national, k16:curative:women:national`
- Kanta-Häme's crude recorded MDT share of 21.6% (95% CI 18.4–25.3; n=118/546), whose 95% confidence interval excludes the national 6.0% (893/14873), measures recording practice rather than care because HILMO captures specialist procedures only from direct patient contacts. `cty:mdt_recorded:Kanta_Hämeen_hyvinvointialue, nat:mdt_recorded, bs:coverage:MDT, q:39e6ba43a9`
- Public data do not include symptoms, referrals or outpatient primary care visits, do not mention occupational health, capture imaging only indirectly as the diagnosis basis in approximately 20% of cases, and record whether a specialist visit (93.6% nationally within 12 months) or treatment occurred without county waiting times. `bs:coverage:Symptoms, bs:coverage:Referral, bs:coverage:Primary_care_occupational_health, q:323de0d90d, bs:coverage:Imaging, q:5eb155decc, bs:coverage:First_specialist_visit, bs:coverage:Treatment_start`

## What should we do first?

**The team recommends publishing county recording completeness given Kanta-Häme's 32.1% crude no-treatment-record share, reporting access times using THL 21/2016 definitions, and adopting standard referral rules and diagnostic contacts.** `rec:3, cty:no_treatment_record:Kanta_Hämeen_hyvinvointialue, rec:1, rec:2`

- Because Kanta-Häme's crude no-treatment-record share is 32.1% (vs 27.5% nationally) and national data reporting and stage coverage (~48% missing) are incomplete, the team recommends publishing county recording completeness for stage, drug treatment and MDT coding while a national quality registry (targeting 90% coverage including stage) and uniform recording instructions are planned. `rec:3, cty:no_treatment_record:Kanta_Hämeen_hyvinvointialue, nat:no_treatment_record, bs:coverage:Diagnosis, q:7885b0974f, q:950a2f797b, q:82d365cd2c, q:f07a34a300, q:4a856bd695`
- Since the Health Care Act sets no maximum time for a cancer suspicion, the team recommends reporting access times using THL guidance 21/2016 (defining 16 cancers) with handover alerts while the roadmap plans national pathways and target access times in 2026–2028 and the Filha programme's diagnostics recommendation with specialist care time limits is due before the 2030 mid-term evaluation. `rec:1, law:no_max, thl:21_2016, q:24169121a4, q:b326e35410, q:432c0e51d6, q:614febebf2`
- To address referral and diagnostic delays—where a mentor insight notes that a weak referral receives a lower urgency rating—the team recommends a standard referral template and persistent-symptoms rule (modelled on the KYS regional pathway document) plus a named diagnostic contact, while the roadmap plans national referral criteria and care-coordinator guidance in 2026–2028 (for county adoption in 2029–2031). `rec:2, mentor:kaisa_referral, reg:kys_template, reg:kys_persistent, reg:named_contact, q:c61439b30f, q:abcbb06ae3, q:050ee09ebe`

## Review flags (for human review only)

_Flags are for human review only; they never change the brief's status or approve it._

- [medium] `where_we_lag.details[1]`: Missing required caveat from the cited claims: treatment categories overlap (a patient can receive multiple treatment types, so shares across categories do not sum to 100%).
- [medium] `what_to_do_first.details[1]`: Overreach and minor imprecision: the cited roadmap claim (q:b326e35410) specifies national pathways and target access times in 2026–2028 are planned for five unnamed cancers (so it is not known whether lung cancer is included), and THL guidance 21/2016 defines how cancer access times are recorded for 16 cancers rather than 'defining 16 cancers'.

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
- `q:432c0e51d6` (verified locally): The upcoming national diagnostics recommendation will include “suositellut aikarajat erikoissairaanhoitoon eri diagnostiikan polun vaiheille” (recommended time limits in specialist care), due before the 2030 mid-term evaluation — filha_lung_programme_2026_fi.pdf, p.16
- `q:4a856bd695` (verified locally): the registry's data, including stage, allows reliable assessment and comparison of quality and effectiveness, with 90% data coverage — roadmap_2026_2031_fi.pdf, p.60
- `q:5eb155decc` (verified locally): Report evidence for pathway stage 'Imaging' — keuhkosyoparaportti_2019_2023.html, §4.1.1 Toteamistapa
- `q:614febebf2` (verified locally): When (p.24): > “Väliarvio toteutetaan vuonna 2030, ohjelman puolivälissä ja loppuarviointi vuonna 2036. Eri > osa-alueiden suositukset toteutetaan ennen väliarviointia.” — filha_lung_programme_2026_fi.pdf, p.24
- `q:7885b0974f` (verified locally): Report evidence for pathway stage 'Diagnosis' — keuhkosyoparaportti_2019_2023.html, §4.1.3 Levinneisyystiedon kattavuus
- `q:82d365cd2c` (verified locally): “Tällä hetkellä keuhkosyöpään liittyvien tietojen raportointi, kerääminen ja tallentaminen on puutteellista”; nationally uniform recording instructions (“yhtenäiset kirjaamisohjeet”) must be ensured — filha_lung_programme_2026_fi.pdf, p.21
- `q:950a2f797b` (verified locally): Reporting, collection and storage of lung cancer data is currently incomplete. — filha_lung_programme_2026_fi.pdf, p.21
- `q:abcbb06ae3` (verified locally): 2026–2028: guidance on a named doctor, nurse or specialist worker coordinating cancer care. 2029–2031: wellbeing services counties have adopted it. — roadmap_2026_2031_fi.pdf, p.32
- `q:b326e35410` (verified locally): National pathways with “syöpäkohtaiset hoitoonpääsyajat” for five (unnamed) cancers in 2026–2028, Nordic model — roadmap_2026_2031_fi.pdf, p.57
- `q:c61439b30f` (verified locally): 2026–2028: standardised referral criteria and symptom-based models included in the national pathways of at least the five most common cancers. — roadmap_2026_2031_fi.pdf, p.53
- `q:f07a34a300` (verified locally): A national cancer care quality registry will be set up alongside THL's Cancer Registry. — roadmap_2026_2031_fi.pdf, p.59
- `rec:1` (recommendation (ours)): Team recommendation 1: Counties report access times using the THL 21/2016 definitions, with handover alerts. Each wellbeing services county reports lung cancer access times (referral → first specialist visit → diagnosis → treatment start) using the definitions in THL's Hoitoonpääsyn seuranta syövän hoidossa (Ohjaus 21/2016). Until national target times exist, flag stalled handovers. — recommendations.md, §1. Counties report access times using the THL 21/2016 definitions, with handover alerts
- `rec:2` (recommendation (ours)): Team recommendation 2: A KYS-style referral template, a persistent-symptoms rule and a named contact. Adopt a standard referral content list and template, modelled on KYS. • Add a rule for primary care: if symptoms persist after a normal X-ray, refer for a pulmonologist assessment. • Name a contact person for the diagnostic phase, from referral to diagnosis. — recommendations.md, §2. A KYS-style referral template, a persistent-symptoms rule and a named contact
- `rec:3` (recommendation (ours)): Team recommendation 3: Report recording completeness per county: stage, drug treatment, MDT coding. Publish, per county, how completely stage, drug treatment and MDT meetings are recorded. Read county ‘gaps’ in these fields as data-quality signals first. — recommendations.md, §3. Report recording completeness per county: stage, drug treatment, MDT coding
- `reg:kys_persistent` (verified by Hellu): KYS: refer persistent unexplained symptoms even if the X-ray is clear — pathway_brief.md, 6. Regional pathways compared
- `reg:kys_template` (verified by Hellu): Only KYS lists required referral content and provides a referral template — pathway_brief.md, 6. Regional pathways compared
- `reg:named_contact` (verified by Hellu): No region names a contact person for the diagnostic phase — pathway_brief.md, 6. Regional pathways compared
- `thl:21_2016` (verified by Hellu): THL Ohjaus 21/2016 defines how cancer access times are recorded, for 16 cancers — pathway_brief.md, 6. Regional pathways compared
