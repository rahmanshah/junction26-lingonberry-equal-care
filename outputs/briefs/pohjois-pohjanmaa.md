# Pohjois-Pohjanmaa: lung cancer pathway brief

Status: **validated** · gemini-4-argon (thinking HIGH) · 2026-11-14T13:10:14+00:00 · attempts: 1

## Where do we lag?

**Pohjois-Pohjanmaa lags nationally in its crude curative treatment share of 23.6% (95% CI 21.1–26.3; n=248/1050) versus 27.0% (4009/14873) across Finland.** `cty:curative:Pohjois_Pohjanmaan_hyvinvointialue, nat:curative`

- The county's crude curative treatment share is 23.6% (95% CI 21.1–26.3; n=248/1050), and its 95% confidence interval excludes the national value of 27.0% (4009/14873). `cty:curative:Pohjois_Pohjanmaan_hyvinvointialue, nat:curative`
- Because treatment categories overlap and a patient can receive several types, the county's crude life-prolonging share is 37.4% (95% CI 34.5–40.4; n=393/1050), whose 95% confidence interval excludes the national 30.4% (4522/14873), while crude symptomatic treatment is 38.8% (95% CI 35.9–41.7; n=407/1050), whose 95% confidence interval includes the national 39.5% (5871/14873). `cty:life_prolonging:Pohjois_Pohjanmaan_hyvinvointialue, nat:life_prolonging, cty:symptomatic:Pohjois_Pohjanmaan_hyvinvointialue, nat:symptomatic`
- Furthermore, 25.0% (95% CI 22.5–27.8; n=263/1050) of patients have a crude share of no treatment record within 12 months, whose 95% confidence interval includes the national value of 27.5% (4089/14873) and is not distinguishable from it; this category mixes untreated patients and unrecorded treatment. `cty:no_treatment_record:Pohjois_Pohjanmaan_hyvinvointialue, nat:no_treatment_record, bs:coverage:Treatment_start`
- A multidisciplinary team (MDT) meeting is recorded for a crude share of 1.1% (95% CI 0.7–2.0; n=12/1050) of county patients, whose 95% confidence interval excludes the national value of 6.0% (893/14873), although HILMO MDT codes capture only direct patient contacts and measure recording practice rather than care. `cty:mdt_recorded:Pohjois_Pohjanmaan_hyvinvointialue, nat:mdt_recorded, bs:coverage:MDT, q:39e6ba43a9`

## How sure are we?

**HILMO diagnosis concordance is about 90% in a 2019 journal article, but public report data lack age and stage adjustments (about 48% missing stage) and pathway wait timestamps.** `lit:hilmo_90, bs:coverage:Diagnosis, q:7885b0974f, bs:coverage:Referral, bs:coverage:Treatment_start`

- County shares are crude and not age-adjusted; age-adjusted values exist only in Kuva 16 for curative treatment by sex, with dashed national lines digitised from the figure (±0.5 percentage points) at 26.7% for men and 26.9% for women, and no county Kuva 16 value to test if the crude 23.6% (95% CI 21.1–26.3; n=248/1050) vs 27.0% (4009/14873) gap holds. `cty:curative:Pohjois_Pohjanmaan_hyvinvointialue, nat:curative, k16:curative:men:national, k16:curative:women:national`
- As a separate limitation, crude county treatment shares cannot be stage-adjusted because stage at diagnosis is missing for about 48% of new patients, and while a 2019 Lääkärilehti journal article found HILMO diagnoses matched the Cancer Registry for about 90% of most cancer types, that finding covers diagnosis concordance only. `bs:coverage:Diagnosis, q:7885b0974f, lit:hilmo_90`
- Public report data do not measure symptom onset, referral dates, imaging waits (recording imaging only indirectly as the diagnosis basis in about 20% of patients), or when specialist visits or treatments occur, while primary care visits are not included in the report's data and occupational health is not mentioned. `bs:coverage:Symptoms, bs:coverage:Primary_care_occupational_health, q:323de0d90d, bs:coverage:Imaging, q:5eb155decc, bs:coverage:Referral, bs:coverage:First_specialist_visit, bs:coverage:Treatment_start`
- Preliminary, unpublished national figures from a 2025 Yle MOT study report an average of 155 days from initial symptoms to treatment in Finland versus 107 days in Sweden and 67 days in Denmark—comprising 56 days of patient delay, 41 days in primary care, and 58 days in specialist care—but no county-specific wait data exist. `mot:total_fi, mot:total_se, mot:total_dk, mot:patient, mot:primary, mot:specialist`

## What should we do first?

**The team recommends tracking THL 21/2016 access times with handover alerts, standardising primary-care referrals and diagnostic contacts, and publishing county stage, drug and MDT recording quality.** `rec:1, rec:2, rec:3, thl:21_2016, q:556431a0c2, q:82d365cd2c`

- Because Health Care Act §52 sets no legal maximum time for a cancer suspicion and the Filha programme's diagnostics recommendation with recommended time limits is to be carried out before the 2030 mid-term evaluation, the team recommends reporting referral, specialist visit, diagnosis and treatment start access times using THL guidance Ohjaus 21/2016 (16 cancers) and flagging stalled handovers. `rec:1, law:no_max, thl:21_2016, q:432c0e51d6, q:614febebf2`
- Given mentor insight that a weak referral gets a lower urgency rating and while STM roadmap measure 1.2.3 plans named care-coordinator guidance by 2026–2028 (adopted by counties by 2029–2031) without specifying the care phase, the team recommends adopting a standard referral template and persistent-symptoms rule after a clear X-ray, modelled on KYS's regional pathway document, plus a named diagnostic-phase contact. `rec:2, mentor:kaisa_referral, q:050ee09ebe, q:abcbb06ae3, reg:kys_template, reg:kys_persistent`
- Because Pohjois-Pohjanmaa's crude recorded MDT share is 1.1% (95% CI 0.7–2.0; n=12/1050) versus 6.0% (893/14873) nationally—measuring recording practice, not care—and stage is missing for about 48% of patients while national data reporting is incomplete, the team recommends publishing per-county stage, drug treatment and MDT coding and reading county gaps in these fields as data-quality signals. `rec:3, cty:mdt_recorded:Pohjois_Pohjanmaan_hyvinvointialue, nat:mdt_recorded, bs:coverage:MDT, bs:coverage:Diagnosis, q:7885b0974f, q:950a2f797b, q:82d365cd2c`

## Review flags (for human review only)

_Flags are for human review only; they never change the brief's status or approve it._

- [medium] `how_sure_are_we.headline`: The claim that public report data lack age adjustments is not supported by any of the cited claims (which cover diagnosis concordance, stage missingness, referral, and treatment start only), and overreaches since Kuva 16 of the public report does include age-adjusted curative treatment figures by sex (though not county values for Pohjois-Pohjanmaa).

## Claims cited

- `bs:coverage:Diagnosis` (verified locally): Pathway stage 'Diagnosis' is measured in public data: yes (by county: yes (Kuva 7, 10, 13: PNG only)) — keuhkosyoparaportti_2019_2023.html, §4.1, Taulukko 2–4, Kuva 5–13
- `bs:coverage:First_specialist_visit` (verified locally): Pathway stage 'First specialist visit' is measured in public data: partly (by county: no) — keuhkosyoparaportti_2019_2023.html, §3.1, §4.2, Taulukko 5
- `bs:coverage:Imaging` (verified locally): Pathway stage 'Imaging' is measured in public data: partly (by county: partly (Kuva 7, PNG only)) — keuhkosyoparaportti_2019_2023.html, §4.1.1, Taulukko 2, Kuva 5–7
- `bs:coverage:MDT` (verified locally): Pathway stage 'MDT' is measured in public data: partly (by county: yes (Taulukko 11)) — keuhkosyoparaportti_2019_2023.html, §3.3, §4.2, Taulukko 5, 10, 11, 13
- `bs:coverage:Primary_care_occupational_health` (verified locally): Pathway stage 'Primary care / occupational health' is measured in public data: no (by county: no) — keuhkosyoparaportti_2019_2023.html, §3.3
- `bs:coverage:Referral` (verified locally): Pathway stage 'Referral' is measured in public data: no (by county: no) — keuhkosyoparaportti_2019_2023.html, whole report (no relevant data found)
- `bs:coverage:Symptoms` (verified locally): Pathway stage 'Symptoms' is measured in public data: no (by county: no) — keuhkosyoparaportti_2019_2023.html, whole report (no relevant data found)
- `bs:coverage:Treatment_start` (verified locally): Pathway stage 'Treatment start' is measured in public data: partly (by county: yes (type only, Taulukko 11)) — keuhkosyoparaportti_2019_2023.html, §4.2, §4.2.2, Taulukko 6–9, 11, 12, Kuva 14, 17
- `cty:curative:Pohjois_Pohjanmaan_hyvinvointialue` (verified locally): Pohjois-Pohjanmaan hyvinvointialue: curative treatment 23.6% (95% CI 21.1–26.3; n=248/1050), below vs national 27.0% — keuhkosyoparaportti_2019_2023.html, Taulukko 11
- `cty:life_prolonging:Pohjois_Pohjanmaan_hyvinvointialue` (verified locally): Pohjois-Pohjanmaan hyvinvointialue: life-prolonging treatment 37.4% (95% CI 34.5–40.4; n=393/1050), above vs national 30.4% — keuhkosyoparaportti_2019_2023.html, Taulukko 11
- `cty:mdt_recorded:Pohjois_Pohjanmaan_hyvinvointialue` (verified locally): Pohjois-Pohjanmaan hyvinvointialue: MDT meeting recorded 1.1% (95% CI 0.7–2.0; n=12/1050), below vs national 6.0% — keuhkosyoparaportti_2019_2023.html, Taulukko 11
- `cty:no_treatment_record:Pohjois_Pohjanmaan_hyvinvointialue` (verified locally): Pohjois-Pohjanmaan hyvinvointialue: no treatment record within 12 months 25.0% (95% CI 22.5–27.8; n=263/1050), not distinguishable vs national 27.5% — keuhkosyoparaportti_2019_2023.html, Taulukko 11
- `cty:symptomatic:Pohjois_Pohjanmaan_hyvinvointialue` (verified locally): Pohjois-Pohjanmaan hyvinvointialue: symptomatic treatment 38.8% (95% CI 35.9–41.7; n=407/1050), not distinguishable vs national 39.5% — keuhkosyoparaportti_2019_2023.html, Taulukko 11
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
- `q:323de0d90d` (verified locally): Report evidence for pathway stage 'Primary care / occupational health' — keuhkosyoparaportti_2019_2023.html, §3.3 Menetelmät
- `q:39e6ba43a9` (verified locally): Report evidence for pathway stage 'MDT' — keuhkosyoparaportti_2019_2023.html, §3.3 Menetelmät
- `q:432c0e51d6` (verified locally): The upcoming national diagnostics recommendation will include “suositellut aikarajat erikoissairaanhoitoon eri diagnostiikan polun vaiheille” (recommended time limits in specialist care), to be carried out (“toteutetaan”; may mean produced or implemented) before the 2030 mid-term evaluation — filha_lung_programme_2026_fi.pdf, p.16
- `q:556431a0c2` (verified locally): the patient is referred to specialist care according to local instructions — filha_lung_programme_2026_fi.pdf, p.15
- `q:5eb155decc` (verified locally): Report evidence for pathway stage 'Imaging' — keuhkosyoparaportti_2019_2023.html, §4.1.1 Toteamistapa
- `q:614febebf2` (verified locally): When (p.24): > “Väliarvio toteutetaan vuonna 2030, ohjelman puolivälissä ja loppuarviointi vuonna 2036. Eri > osa-alueiden suositukset toteutetaan ennen väliarviointia.” — filha_lung_programme_2026_fi.pdf, p.24
- `q:7885b0974f` (verified locally): Report evidence for pathway stage 'Diagnosis' — keuhkosyoparaportti_2019_2023.html, §4.1.3 Levinneisyystiedon kattavuus
- `q:82d365cd2c` (verified locally): “Tällä hetkellä keuhkosyöpään liittyvien tietojen raportointi, kerääminen ja tallentaminen on puutteellista”; nationally uniform recording instructions (“yhtenäiset kirjaamisohjeet”) must be ensured — filha_lung_programme_2026_fi.pdf, p.21
- `q:950a2f797b` (verified locally): Reporting, collection and storage of lung cancer data is currently incomplete. — filha_lung_programme_2026_fi.pdf, p.21
- `q:abcbb06ae3` (verified locally): 2026–2028: guidance on a named doctor, nurse or specialist worker coordinating cancer care. 2029–2031: wellbeing services counties have adopted it. — roadmap_2026_2031_fi.pdf, p.32
- `rec:1` (recommendation (ours)): Team recommendation 1: Counties report access times using the THL 21/2016 definitions, with handover alerts. Each wellbeing services county reports lung cancer access times (referral → first specialist visit → diagnosis → treatment start) using the definitions in THL's Hoitoonpääsyn seuranta syövän hoidossa (Ohjaus 21/2016). Until national target times exist, flag stalled handovers. — recommendations.md, §1. Counties report access times using the THL 21/2016 definitions, with handover alerts
- `rec:2` (recommendation (ours)): Team recommendation 2: A KYS-style referral template, a persistent-symptoms rule and a named contact. Adopt a standard referral content list and template, modelled on KYS. • Add a rule for primary care: if symptoms persist after a normal X-ray, refer for a pulmonologist assessment. • Name a contact person for the diagnostic phase, from referral to diagnosis. — recommendations.md, §2. A KYS-style referral template, a persistent-symptoms rule and a named contact
- `rec:3` (recommendation (ours)): Team recommendation 3: Report recording completeness per county: stage, drug treatment, MDT coding. Publish, per county, how completely stage, drug treatment and MDT meetings are recorded. Read county ‘gaps’ in these fields as data-quality signals first. — recommendations.md, §3. Report recording completeness per county: stage, drug treatment, MDT coding
- `reg:kys_persistent` (verified by Hellu): KYS: refer persistent unexplained symptoms even if the X-ray is clear — pathway_brief.md, 6. Regional pathways compared
- `reg:kys_template` (verified by Hellu): Only KYS lists required referral content and provides a referral template — pathway_brief.md, 6. Regional pathways compared
- `thl:21_2016` (verified by Hellu): THL Ohjaus 21/2016 defines how cancer access times are recorded, for 16 cancers — pathway_brief.md, 6. Regional pathways compared
