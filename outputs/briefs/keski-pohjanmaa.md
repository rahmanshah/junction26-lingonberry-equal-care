# Keski-Pohjanmaa: lung cancer pathway brief

Status: **validated** · gemini-4-argon (thinking HIGH) · 2026-11-14T13:08:04+00:00 · attempts: 1

## Where do we lag?

**Keski-Pohjanmaa's crude multidisciplinary team recording share of 1.4% (95% CI 0.4–4.8; n=2/148) is below the 6.0% (893/14873) national value, though this measures recording practice rather than care.** `cty:mdt_recorded:Keski_Pohjanmaan_hyvinvointialue, nat:mdt_recorded, bs:coverage:MDT`

- In Keski-Pohjanmaa, a multidisciplinary team meeting is recorded for a crude share of 1.4% (95% CI 0.4–4.8; n=2/148) compared with 6.0% (893/14873) nationally, with the 95% confidence interval excluding the national value, though these records measure recording practice rather than care because HILMO captures procedures only from direct patient contacts. `cty:mdt_recorded:Keski_Pohjanmaan_hyvinvointialue, nat:mdt_recorded, bs:coverage:MDT, q:39e6ba43a9`
- Because treatment categories overlap, Keski-Pohjanmaa's crude shares are 22.3% (95% CI 16.3–29.7; n=33/148) versus 27.0% (4009/14873) nationally for curative, 32.4% (95% CI 25.4–40.3; n=48/148) versus 30.4% (4522/14873) for life-prolonging, and 46.6% (95% CI 38.8–54.6; n=69/148) versus 39.5% (5871/14873) for symptomatic treatment, with each 95% confidence interval including the national value. `cty:curative:Keski_Pohjanmaan_hyvinvointialue, nat:curative, cty:life_prolonging:Keski_Pohjanmaan_hyvinvointialue, nat:life_prolonging, cty:symptomatic:Keski_Pohjanmaan_hyvinvointialue, nat:symptomatic`
- A crude share of 25.0% (95% CI 18.7–32.5; n=37/148) in Keski-Pohjanmaa has no treatment record within 12 months compared with 27.5% (4089/14873) nationally, where the 95% confidence interval includes the national value and the category mixes untreated patients with unrecorded treatment. `cty:no_treatment_record:Keski_Pohjanmaan_hyvinvointialue, nat:no_treatment_record, bs:coverage:Treatment_start`
- In preliminary, unpublished national figures for Finland, the pathway from symptoms to treatment averages 155 days—with 56 days of patient delay, 41 days in primary care, and 58 days in specialist care—compared with 107 days in Sweden and 67 days in Denmark. `mot:total_fi, mot:patient, mot:primary, mot:specialist, mot:total_se, mot:total_dk`

## How sure are we?

**Public registry data lack stage at diagnosis for about 48% of patients and do not capture primary care visits, referral dates, or treatment start times.** `bs:coverage:Diagnosis, q:7885b0974f, bs:coverage:Primary_care_occupational_health, bs:coverage:Referral, bs:coverage:Treatment_start`

- County figures, like the crude 22.3% (95% CI 16.3–29.7; n=33/148) curative share versus 27.0% (4009/14873) nationally, are not age-adjusted—age-adjusted values exist only from Kuva 16 for curative treatment by sex, with digitised national lines of 26.7% for men and 26.9% for women at ±0.5 percentage points—and separately cannot be stage-adjusted with stage missing for about 48% of patients. `cty:curative:Keski_Pohjanmaan_hyvinvointialue, nat:curative, k16:curative:men:national, k16:curative:women:national, bs:coverage:Diagnosis, q:7885b0974f`
- A journal article found that HILMO hospital discharge diagnoses match the Cancer Registry for about 90% of most cancer types, whereas lung cancer data reporting, collection, and storage are currently incomplete and Finland has no cancer quality registry. `lit:hilmo_90, q:950a2f797b, q:47c7e11303, filha:registry`
- Public report data do not measure symptoms, referral dates, specialist visit timing, or treatment start dates; primary care visits are not included in the report's data, occupational health is not mentioned at all, and imaging appears only indirectly as the clinical basis of diagnosis in about 20% of patients. `bs:coverage:Symptoms, bs:coverage:Referral, bs:coverage:First_specialist_visit, bs:coverage:Treatment_start, bs:coverage:Primary_care_occupational_health, q:323de0d90d, bs:coverage:Imaging, q:5eb155decc`

## What should we do first?

**The team recommends auditing recording completeness for stage, drug treatment, and multidisciplinary meetings, tracking access times using THL 21/2016 definitions, and standardising referrals with a named diagnostic contact.** `rec:3, rec:1, rec:2`

- Given Keski-Pohjanmaa's crude multidisciplinary team recording share of 1.4% (95% CI 0.4–4.8; n=2/148) versus 6.0% (893/14873) nationally and 48% missing stage nationally, the team recommends publishing county recording completeness for stage, drug treatment, and multidisciplinary coding, aligning with the STM roadmap's measure 3.2.1 plan for a quality registry decree by 2026–2028 and 90% coverage by 2029–2031. `rec:3, cty:mdt_recorded:Keski_Pohjanmaan_hyvinvointialue, nat:mdt_recorded, bs:coverage:Diagnosis, q:7885b0974f, q:950a2f797b, q:f07a34a300, q:4a856bd695`
- Because the Health Care Act sets no maximum time for a cancer suspicion and national monitoring is lacking, the team recommends reporting access times and flagging stalled handovers using THL Ohjaus 21/2016 definitions for 16 cancers, while the STM roadmap's measure 3.1.2 plans national pathway descriptions and access times by 2026–2028 and for all significant cancers by 2029–2031. `rec:1, law:no_max, q:4e702a20fe, thl:21_2016, q:ed87906241, q:def306014c, q:b326e35410`
- The team recommends adopting a referral template and referring persistent symptoms after a normal X-ray, as set out in the KYS regional pathway document, since a mentor insight notes weak referrals get lower urgency ratings and the Filha programme's diagnostics recommendation with referral criteria and time limits is to be carried out before the 2030 mid-term evaluation. `rec:2, reg:kys_template, reg:kys_persistent, reg:only_kys_xray, mentor:kaisa_referral, q:29b792498e, q:432c0e51d6, q:614febebf2`
- Because no reviewed regional pathway document names a diagnostic-phase contact person, the team recommends naming a contact from referral to diagnosis, alongside the STM roadmap's measure 2.5.2 plan for standardised referral criteria and symptom-based models by 2026–2028 and measure 1.2.3 plan for named care-coordinator guidance by 2026–2028 and county adoption by 2029–2031. `rec:2, reg:named_contact, q:0780bf74b0, q:37bb4c3b38, q:c61439b30f, q:fc81032a80, q:abcbb06ae3, q:050ee09ebe`

## Review flags (for human review only)

_Flags are for human review only; they never change the brief's status or approve it._

- [low] `how_sure_are_we.details[0]`: The cited claims state that Kuva 16 covers age-adjusted curative treatment by sex, not that age-adjusted values exist only in Kuva 16.
- [low] `how_sure_are_we.details[2]`: The cited claims state that diagnosis is based on clinical examination or findings alone, such as imaging, in about 20% of patients, rather than imaging specifically being the basis in all 20%.
- [medium] `what_to_do_first.details[0]`: The cited claims state that measure 3.2.1 plans annual reports for at least five cancers by 2029–2031 and mentions 90% data coverage, but do not state that 90% coverage is scheduled specifically by 2029–2031; also states 48% missing stage without the qualifier 'about' or 'nearly half'.
- [medium] `what_to_do_first.details[1]`: Omits the scope caveat that measure 3.1.2's 2026–2028 milestone covers only five unnamed cancers, not national pathways and access times in general.
- [medium] `what_to_do_first.details[3]`: Omits the scope caveat that measure 2.5.2's 2026–2028 milestone applies to the national pathways of at least the five most common cancers (with all significant cancers by 2029–2031).

## Claims cited

- `bs:coverage:Diagnosis` (verified locally): Pathway stage 'Diagnosis' is measured in public data: yes (by county: yes (Kuva 7, 10, 13: PNG only)) — keuhkosyoparaportti_2019_2023.html, §4.1, Taulukko 2–4, Kuva 5–13
- `bs:coverage:First_specialist_visit` (verified locally): Pathway stage 'First specialist visit' is measured in public data: partly (by county: no) — keuhkosyoparaportti_2019_2023.html, §3.1, §4.2, Taulukko 5
- `bs:coverage:Imaging` (verified locally): Pathway stage 'Imaging' is measured in public data: partly (by county: partly (Kuva 7, PNG only)) — keuhkosyoparaportti_2019_2023.html, §4.1.1, Taulukko 2, Kuva 5–7
- `bs:coverage:MDT` (verified locally): Pathway stage 'MDT' is measured in public data: partly (by county: yes (Taulukko 11)) — keuhkosyoparaportti_2019_2023.html, §3.3, §4.2, Taulukko 5, 10, 11, 13
- `bs:coverage:Primary_care_occupational_health` (verified locally): Pathway stage 'Primary care / occupational health' is measured in public data: no (by county: no) — keuhkosyoparaportti_2019_2023.html, §3.3
- `bs:coverage:Referral` (verified locally): Pathway stage 'Referral' is measured in public data: no (by county: no) — keuhkosyoparaportti_2019_2023.html, whole report (no relevant data found)
- `bs:coverage:Symptoms` (verified locally): Pathway stage 'Symptoms' is measured in public data: no (by county: no) — keuhkosyoparaportti_2019_2023.html, whole report (no relevant data found)
- `bs:coverage:Treatment_start` (verified locally): Pathway stage 'Treatment start' is measured in public data: partly (by county: yes (type only, Taulukko 11)) — keuhkosyoparaportti_2019_2023.html, §4.2, §4.2.2, Taulukko 6–9, 11, 12, Kuva 14, 17
- `cty:curative:Keski_Pohjanmaan_hyvinvointialue` (verified locally): Keski-Pohjanmaan hyvinvointialue: curative treatment 22.3% (95% CI 16.3–29.7; n=33/148), not distinguishable vs national 27.0% — keuhkosyoparaportti_2019_2023.html, Taulukko 11
- `cty:life_prolonging:Keski_Pohjanmaan_hyvinvointialue` (verified locally): Keski-Pohjanmaan hyvinvointialue: life-prolonging treatment 32.4% (95% CI 25.4–40.3; n=48/148), not distinguishable vs national 30.4% — keuhkosyoparaportti_2019_2023.html, Taulukko 11
- `cty:mdt_recorded:Keski_Pohjanmaan_hyvinvointialue` (verified locally): Keski-Pohjanmaan hyvinvointialue: MDT meeting recorded 1.4% (95% CI 0.4–4.8; n=2/148), below vs national 6.0% — keuhkosyoparaportti_2019_2023.html, Taulukko 11
- `cty:no_treatment_record:Keski_Pohjanmaan_hyvinvointialue` (verified locally): Keski-Pohjanmaan hyvinvointialue: no treatment record within 12 months 25.0% (95% CI 18.7–32.5; n=37/148), not distinguishable vs national 27.5% — keuhkosyoparaportti_2019_2023.html, Taulukko 11
- `cty:symptomatic:Keski_Pohjanmaan_hyvinvointialue` (verified locally): Keski-Pohjanmaan hyvinvointialue: symptomatic treatment 46.6% (95% CI 38.8–54.6; n=69/148), not distinguishable vs national 39.5% — keuhkosyoparaportti_2019_2023.html, Taulukko 11
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
- `q:29b792498e` (verified locally): Policy evidence for pathway stage 'Referral' — filha_lung_programme_2026_fi.pdf, p.16
- `q:323de0d90d` (verified locally): Report evidence for pathway stage 'Primary care / occupational health' — keuhkosyoparaportti_2019_2023.html, §3.3 Menetelmät
- `q:37bb4c3b38` (verified locally): Policy evidence for pathway stage 'Referral' — roadmap_2026_2031_fi.pdf, p.52; p.106
- `q:39e6ba43a9` (verified locally): Report evidence for pathway stage 'MDT' — keuhkosyoparaportti_2019_2023.html, §3.3 Menetelmät
- `q:432c0e51d6` (verified locally): The upcoming national diagnostics recommendation will include “suositellut aikarajat erikoissairaanhoitoon eri diagnostiikan polun vaiheille” (recommended time limits in specialist care), to be carried out (“toteutetaan”; may mean produced or implemented) before the 2030 mid-term evaluation — filha_lung_programme_2026_fi.pdf, p.16
- `q:47c7e11303` (verified locally): Finland has no quality registry for lung cancer or for any other cancer. — filha_lung_programme_2026_fi.pdf, p.21
- `q:4a856bd695` (verified locally): the registry's data, including stage, allows reliable assessment and comparison of quality and effectiveness, with 90% data coverage — roadmap_2026_2031_fi.pdf, p.60
- `q:4e702a20fe` (verified locally): Finland has no unified national system to steer the drafting of cancer-specific treatment recommendations, or the implementation and monitoring of care pathways based on them (quality and effectiveness targets/indicators, including access to care, and cancer-specific and generic PROMs). Existing recommendations and pathways, and the targets and indicators to be monitored, are not coordinated nationally. This maintains regional inequality in the availability and effectiveness of cancer care. — strategy_2026_2035_fi.pdf, p.33
- `q:5eb155decc` (verified locally): Report evidence for pathway stage 'Imaging' — keuhkosyoparaportti_2019_2023.html, §4.1.1 Toteamistapa
- `q:614febebf2` (verified locally): When (p.24): > “Väliarvio toteutetaan vuonna 2030, ohjelman puolivälissä ja loppuarviointi vuonna 2036. Eri > osa-alueiden suositukset toteutetaan ennen väliarviointia.” — filha_lung_programme_2026_fi.pdf, p.24
- `q:7885b0974f` (verified locally): Report evidence for pathway stage 'Diagnosis' — keuhkosyoparaportti_2019_2023.html, §4.1.3 Levinneisyystiedon kattavuus
- `q:950a2f797b` (verified locally): Reporting, collection and storage of lung cancer data is currently incomplete. — filha_lung_programme_2026_fi.pdf, p.21
- `q:abcbb06ae3` (verified locally): 2026–2028: guidance on a named doctor, nurse or specialist worker coordinating cancer care. 2029–2031: wellbeing services counties have adopted it. — roadmap_2026_2031_fi.pdf, p.32
- `q:b326e35410` (verified locally): National pathways with “syöpäkohtaiset hoitoonpääsyajat” for five (unnamed) cancers in 2026–2028, Nordic model — roadmap_2026_2031_fi.pdf, p.57
- `q:c61439b30f` (verified locally): 2026–2028: standardised referral criteria and symptom-based models included in the national pathways of at least the five most common cancers. — roadmap_2026_2031_fi.pdf, p.53
- `q:def306014c` (verified locally): p.57, timetable: > “2026–2028: Kansalliset hoitoketjukuvaukset tehty viidestä syövästä ja syöpäkohtaiset > hoitoonpääsyajat on määritetty.” — roadmap_2026_2031_fi.pdf, p.57
- `q:ed87906241` (verified locally): p.56, heading: > “Toimenpide 3.1.2 Laaditaan syöpäkohtaiset hoitoketjukuvaukset, ja niiden pohjalta sovelletut > alueelliset hoitoketjut, sekä mekanismi niiden ylläpitoon ja hallintaan” — roadmap_2026_2031_fi.pdf, p.56
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
