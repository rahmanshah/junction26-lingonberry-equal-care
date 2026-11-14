# Kymenlaakso: lung cancer pathway brief

Status: **validated** · gemini-4-argon (thinking HIGH) · 2026-11-14T12:03:53+00:00 · attempts: 1

## Where do we lag?

**Kymenlaakso lags national levels in crude curative treatment at 19.3% (95% CI 16.3–22.7) versus 27.0% and crude MDT recording at 0.5% (95% CI 0.2–1.5) versus 6.0%.** `cty:curative:Kymenlaakson_hyvinvointialue, nat:curative, cty:mdt_recorded:Kymenlaakson_hyvinvointialue, nat:mdt_recorded`

- The county's crude curative treatment share, which is not adjusted for age or stage, is 19.3% (95% CI 16.3–22.7; n=114/591) alongside the national 27.0% (4009/14873), and the 95% confidence interval excludes the national value. `cty:curative:Kymenlaakson_hyvinvointialue, nat:curative, bs:coverage:Diagnosis`
- In figures digitised from Kuva 16 with precision ±0.5 percentage points, the age-adjusted curative share gap holds for men at 17.9% (95% CI 13.9–22.9) versus 26.7% nationally, as the 95% confidence interval excludes the dashed national reference line, whereas for women at 22.6% (95% CI 16.8–29.3) versus 26.9% nationally, the 95% confidence interval includes it. `k16:curative:men:Kymenlaakson_hyvinvointialue, k16:curative:men:national, k16:curative:women:Kymenlaakson_hyvinvointialue, k16:curative:women:national`
- Across overlapping treatment categories that are not mutually exclusive, Kymenlaakso's crude shares exceed national values for life-prolonging treatment at 37.6% (95% CI 33.8–41.5; n=222/591) versus 30.4% (4522/14873) and symptomatic treatment at 51.3% (95% CI 47.2–55.3; n=303/591) versus 39.5% (5871/14873), with each 95% confidence interval excluding the national value. `cty:life_prolonging:Kymenlaakson_hyvinvointialue, nat:life_prolonging, cty:symptomatic:Kymenlaakson_hyvinvointialue, nat:symptomatic`
- Crude MDT meeting recording is 0.5% (95% CI 0.2–1.5; n=3/591) compared with 6.0% (893/14873) nationally, with the 95% confidence interval excluding the national value, though HILMO captures specialist procedures only from direct patient contacts so this measures recording practice rather than care. `cty:mdt_recorded:Kymenlaakson_hyvinvointialue, nat:mdt_recorded, bs:coverage:MDT, q:39e6ba43a9`

## How sure are we?

**A crude 16.4% (95% CI 13.7–19.6) share with no treatment record versus 27.5% nationally suggests Kymenlaakso's curative gap is not only a recording artefact, though stage is unmeasured.** `cty:no_treatment_record:Kymenlaakson_hyvinvointialue, nat:no_treatment_record, bs:coverage:Diagnosis`

- Kymenlaakso's crude share with no treatment record within 12 months—mixing patients who had no treatment and unrecorded treatment—is 16.4% (95% CI 13.7–19.6; n=97/591) versus 27.5% (4089/14873) nationally (95% CI excludes the national value); read as a data-quality signal, this inference is consistent with relatively complete treatment recording, making a recording artefact less likely. `cty:no_treatment_record:Kymenlaakson_hyvinvointialue, nat:no_treatment_record, bs:coverage:Treatment_start`
- However, this signal is not direct evidence of complete treatment capture—a journal article finding that HILMO matches the Cancer Registry for about 90% of most cancer types concerns diagnosis concordance only—and missing stage at diagnosis for a large share of patients nationally prevents stage adjustment. `lit:hilmo_90, bs:coverage:Diagnosis, q:7885b0974f`
- Public data also leave early pathway stages unseen: symptom onset is unmeasured, outpatient primary care visits are not included in the report's data, occupational health is unmentioned, imaging appears only indirectly as the basis of diagnosis in approximately 20% of cases, and referral, specialist visit, and treatment start dates are absent. `bs:coverage:Symptoms, bs:coverage:Primary_care_occupational_health, q:323de0d90d, bs:coverage:Imaging, q:5eb155decc, bs:coverage:Referral, bs:coverage:First_specialist_visit, bs:coverage:Treatment_start`
- Preliminary, unpublished national figures average 155 days from symptoms to treatment in Finland versus 107 in Sweden and 67 in Denmark—with 56 days of patient delay, 41 days in primary care, and 58 days in specialist care, the longest stage—while the Health Care Act sets no legal maximum time for a cancer suspicion. `mot:total_fi, mot:total_se, mot:total_dk, mot:patient, mot:primary, mot:specialist, law:no_max`

## What should we do first?

**The team recommends reporting lung cancer access times using THL 21/2016 definitions, adopting standardised referrals and diagnostic coordination, and publishing county recording completeness for stage, drugs, and MDT.** `rec:1, rec:2, rec:3, thl:21_2016, q:950a2f797b`

- The team recommends reporting lung cancer access times across referral, specialist visit, diagnosis, and treatment start using THL guidance Ohjaus 21/2016 definitions and flagging stalled handovers, as Finland currently lacks unified national access monitoring while the roadmap plans cancer-specific access times in 2026–2028 and the Filha programme's diagnostics recommendation is due before the 2030 mid-term evaluation. `rec:1, thl:21_2016, q:24169121a4, q:ccda20dce9, q:def306014c, q:432c0e51d6, q:614febebf2`
- The team recommends adopting a standard referral template and a persistent-symptoms referral rule after a normal X-ray—as set out in KYS's regional pathway document—plus a named diagnostic-phase contact person, since mentor insight notes weak referrals receive lower specialist urgency and the roadmap plans standardised referral criteria and care-coordinator guidance in 2026–2028 for county adoption in 2029–2031. `rec:2, reg:kys_template, reg:kys_persistent, mentor:kaisa_referral, q:c61439b30f, q:abcbb06ae3, q:050ee09ebe`
- Given Kymenlaakso's 0.5% (95% CI 0.2–1.5; n=3/591) crude MDT recording share versus 6.0% (893/14873) nationally and incomplete national lung cancer data storage, the team recommends publishing county recording completeness for stage, drug treatment, and MDT coding while the roadmap plans a national quality registry targeting 90% data coverage including stage alongside uniform recording instructions. `rec:3, cty:mdt_recorded:Kymenlaakson_hyvinvointialue, nat:mdt_recorded, q:950a2f797b, q:82d365cd2c, q:f07a34a300, q:4a856bd695`

## Review flags (for human review only)

_Flags are for human review only; they never change the brief's status or approve it._

- [low] `how_sure_are_we.headline`: Claim [bs:coverage:Diagnosis] states that stage at diagnosis is missing for nearly half (~48%) of new patients, preventing stage adjustment, rather than being completely unmeasured.
- [medium] `what_to_do_first.details[2]`: The sentence attributes uniform recording instructions to what the Cancer strategy implementation roadmap plans, whereas [q:82d365cd2c] is from the Filha National Lung Cancer Programme 2026–2035 and states that uniform recording instructions must be ensured.

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
- `q:c61439b30f` (verified locally): 2026–2028: standardised referral criteria and symptom-based models included in the national pathways of at least the five most common cancers. — roadmap_2026_2031_fi.pdf, p.53
- `q:ccda20dce9` (verified locally): Finland has no national system steering cancer pathways or their monitoring, “mukaan lukien hoitoonpääsy” — strategy_2026_2035_fi.pdf, p.33
- `q:def306014c` (verified locally): p.57, timetable: > “2026–2028: Kansalliset hoitoketjukuvaukset tehty viidestä syövästä ja syöpäkohtaiset > hoitoonpääsyajat on määritetty.” — roadmap_2026_2031_fi.pdf, p.57
- `q:f07a34a300` (verified locally): A national cancer care quality registry will be set up alongside THL's Cancer Registry. — roadmap_2026_2031_fi.pdf, p.59
- `rec:1` (recommendation (ours)): Team recommendation 1: Counties report access times using the THL 21/2016 definitions, with handover alerts. Each wellbeing services county reports lung cancer access times (referral → first specialist visit → diagnosis → treatment start) using the definitions in THL's Hoitoonpääsyn seuranta syövän hoidossa (Ohjaus 21/2016). Until national target times exist, flag stalled handovers. — recommendations.md, §1. Counties report access times using the THL 21/2016 definitions, with handover alerts
- `rec:2` (recommendation (ours)): Team recommendation 2: A KYS-style referral template, a persistent-symptoms rule and a named contact. Adopt a standard referral content list and template, modelled on KYS. • Add a rule for primary care: if symptoms persist after a normal X-ray, refer for a pulmonologist assessment. • Name a contact person for the diagnostic phase, from referral to diagnosis. — recommendations.md, §2. A KYS-style referral template, a persistent-symptoms rule and a named contact
- `rec:3` (recommendation (ours)): Team recommendation 3: Report recording completeness per county: stage, drug treatment, MDT coding. Publish, per county, how completely stage, drug treatment and MDT meetings are recorded. Read county ‘gaps’ in these fields as data-quality signals first. — recommendations.md, §3. Report recording completeness per county: stage, drug treatment, MDT coding
- `reg:kys_persistent` (verified by Hellu): KYS: refer persistent unexplained symptoms even if the X-ray is clear — pathway_brief.md, 6. Regional pathways compared
- `reg:kys_template` (verified by Hellu): Only KYS lists required referral content and provides a referral template — pathway_brief.md, 6. Regional pathways compared
- `thl:21_2016` (verified by Hellu): THL Ohjaus 21/2016 defines how cancer access times are recorded, for 16 cancers — pathway_brief.md, 6. Regional pathways compared
