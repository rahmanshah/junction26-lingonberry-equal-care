# Recommendations (DRAFT)

> **Status: draft, 14 Nov 2026.** Not yet reviewed by mentors. Each piece of evidence carries its source
> status. Do not quote figures marked *preliminary* or *mentor insight* as established fact.

Status labels used below:
- **verified locally**: we read the source in `data/raw/` ourselves (quotes in `docs/source_verification.md`
  and `docs/definitions.md`), or computed the figure in our own code from it.
- **verified by Hellu, read 14 Nov**: Hellu read the source in full; it is not in the repo.
- **preliminary**: unpublished study reported by Yle MOT (2025); primary author unknown.
- **mentor insight (name)**: expert opinion, no written source.

---

## 1. Counties report access times using the THL 21/2016 definitions, with handover alerts

**What:** each wellbeing services county reports lung cancer access times (referral → first specialist
visit → diagnosis → treatment start) using the definitions in THL's *Hoitoonpääsyn seuranta syövän
hoidossa* (Ohjaus 21/2016). Until national target times exist, flag stalled handovers.

**Draft alert rules** (pathway_brief §8; thresholds to confirm with Kaisa):
- A referral is returned, or more information is requested, and no new referral follows within 7 days.
- A referral is accepted and no first visit follows within 14 days.
- Symptoms are recorded with a normal X-ray, and no referral or follow-up follows within X days.

**Evidence**

| Point | Source | Status |
|---|---|---|
| Finland has no national system steering cancer pathways or their monitoring, <q lang="fi">mukaan lukien hoitoonpääsy</q> | Strategy p.33 | verified locally |
| The strategy's indicator <q lang="fi">Potilaat pääsevät hoitoon tavoiteaikojen puitteissa</q> is footnoted to THL Ohjaus 21/2016 | Strategy p.5 | verified locally |
| National pathways with <q lang="fi">syöpäkohtaiset hoitoonpääsyajat</q> for five (unnamed) cancers in 2026–2028, Nordic model | Roadmap 3.1.2, pp.56–57 | verified locally |
| The public report publishes no referral, first-visit or time-to-treatment data; specialist-phase timing is a blind spot | Report §3.1, §4.2; `docs/blind_spots.md` | verified locally |
| <q lang="fi">Valtakunnallisesti ei ole ollut tarkkaa yhtenäistä ohjeistusta siitä, millä aikataululla diagnostiikan eri osa-alueet tulisi olla tehtyinä</q>; regional variation in diagnostic speed is large. The programme itself sets no day-based targets | Filha programme p.4 | verified locally |
| The upcoming national diagnostics recommendation will include <q lang="fi">suositellut aikarajat erikoissairaanhoitoon eri diagnostiikan polun vaiheille</q> (recommended time limits in specialist care), due before the 2030 mid-term evaluation | Filha programme pp.16, 24 | verified locally |
| The programme lists <q lang="fi">Hoitoonpääsy</q> (access to care) as an indicator but does not define how it is measured; the monitoring it describes uses registry data, hospital surveys and studies | Filha programme pp.18 (Table 2), 22–23 | verified locally |
| THL 21/2016 defines access-time recording for 16 cancers, in force since 1 Jan 2017 | THL Ohjaus 21/2016 | verified by Hellu, read 14 Nov |
| No published cancer-specific access-time report found | Hellu's search | to confirm with mentors |
| HILMO diagnoses match the Cancer Registry for ~90% of most cancers; reliability of referral and first-procedure data still to be confirmed | Ryynänen et al., Lääkärilehti 2019 | verified by Hellu, read 14 Nov |
| No legal maximum time for a cancer suspicion; only the general limits (3 weeks / 3 months / 6 months) | Health Care Act §52, Valvira | verified by Hellu, read 14 Nov |
| Regions state different targets (Keski-Suomi: first visit within ~1 month; Pirha: invitation in 3–4 working days); none says whether it meets them | Regional pathways | verified by Hellu, read 14 Nov |
| Symptoms to treatment: 155 days in Finland vs 107 in Sweden and 67 in Denmark; specialist care is the longest interval (58 days) | Yle MOT 2025 | preliminary |

**Why first:** it uses definitions that already exist (2016) and the indicator the strategy already
names. It also covers the longest and least visible stage. It also gives the Filha programme's
undefined <q lang="fi">Hoitoonpääsy</q> indicator a concrete measurement, ready for when its recommended time limits
arrive (before 2030).

**Caveat:** this depends on whether referral and first-visit timestamps are reliable enough (Lääkärilehti
2019). A pilot county should check that first.

---

## 2. A KYS-style referral template, a persistent-symptoms rule and a named contact

**What:**
- Adopt a standard referral content list and template, modelled on KYS.
- Add a rule for primary care: if symptoms persist after a normal X-ray, refer for a pulmonologist
  assessment.
- Name a contact person for the diagnostic phase, from referral to diagnosis.

**Evidence**

| Point | Source | Status |
|---|---|---|
| Standardised referral criteria and symptom-based models (<q lang="fi">standardoidut lähetekriteerit</q>, <q lang="fi">oirelähtöiset toimintamallit</q>) for at least the five most common cancers by 2026–2028 | Roadmap 2.5.2, pp.52–53 | verified locally |
| Guidance on a named worker coordinating cancer care by 2026–2028, adopted by counties by 2029–2031; the care phase is left open (<q lang="fi">missä hoidon vaiheessa … olisi tärkeintä kohdentaa</q>) | Roadmap 1.2.3, p.32 | verified locally |
| Lung cancer referral criteria for primary care (<q lang="fi">lähetekriteerit perusterveydenhuollolle</q>) will come in the national diagnostics recommendation, before the 2030 mid-term evaluation; work has started | Filha programme pp.3, 16, 20, 24 | verified locally |
| Today, <q lang="fi">potilas lähetetään jatkotutkimuksiin erikoissairaanhoidon yksikköön omien paikallisten ohjeistusten mukaisesti</q> (referral follows local instructions); suspicion typically arises in primary care, occupational health or private care | Filha programme p.15 | verified locally |
| Only KYS lists required referral content (history, medications, pack-years, asbestos, functional capacity, what the patient was told) and provides a template | KYS care chain v1.1 (2021) | verified by Hellu, read 14 Nov |
| Only KYS addresses a normal X-ray with continuing symptoms (refer even if the X-ray is clear) | KYS care chain | verified by Hellu, read 14 Nov |
| No region names a contact person for the diagnostic phase; HUS assigns a nurse at the first visit | Regional pathways | verified by Hellu, read 14 Nov |
| A weak referral gets a lower urgency rating in specialist care | Kaisa | mentor insight (Kaisa) |
| Occupational health gets patients to specialist care faster | Hanna | mentor insight (Hanna) |
| Primary care interval: 41 days | Yle MOT 2025 | preliminary |

**Why:** it acts on the handovers where the patient is most likely to be dropped, before diagnosis, a
stage public data cannot see at all. It is also already in the roadmap (2.5.2, 1.2.3) and the Filha
programme (diagnostics recommendation before 2030). This recommendation proposes doing it now, with an
existing regional model, as a bridge until the national criteria arrive.

**Caveat:** KYS's document is for professionals and the others are for patients, so they are not fully
comparable. Five regions out of 22 were reviewed.

---

## 3. Report recording completeness per county: stage, drug treatment, MDT coding

**What:** publish, per county, how completely stage, drug treatment and MDT meetings are recorded. Read
county ‘gaps’ in these fields as data-quality signals first.

**Evidence** (county figures: report Taulukko 11, Wilson 95% CIs computed in `src/add_ci.py`)

| Point | Source | Status |
|---|---|---|
| Stage at diagnosis is missing for about half of patients: <q lang="fi">levinneisyys toteamishetkellä puuttuu lähes puolelta uusia potilaita</q> | Report §4.1.3, Taulukko 4 | verified locally |
| Varsinais-Suomi: life-prolonging treatment 9.7% [8.3–11.4] vs 30.4% nationally, and no treatment record 43.1% [40.5–45.6] vs 27.5%. The pattern suggests drug treatment is not being recorded | Report Taulukko 11; our CIs | verified locally (interpretation is ours) |
| No treatment record ranges from 16.4% (Kymenlaakso) to 43.1% (Varsinais-Suomi); Etelä-Karjala 42.8% [37.8–48.0]. This mixes untreated patients with unrecorded treatment | Report Taulukko 11; our CIs | verified locally |
| MDT coding: 21.6–37.4% in Sisä-Suomi counties, 0 records in 4 counties. <q lang="fi">…ei kuvaa kattavasti moniammatillisen käsittelyn laajuutta</q> | Report §3.3, Taulukko 11 | verified locally |
| National pathways will define recording and coding practices (<q lang="fi">kirjaamis- ja koodistokäytännöistä</q>) | Roadmap 3.1.2, p.56 | verified locally |
| A national quality registry is planned; indicator: data incl. stage (<q lang="fi">ml. levinneisyystieto</q>) at 90% coverage | Roadmap 3.2.1, pp.59–60 | verified locally |
| <q lang="fi">Keuhkosyövästä tai muistakaan syövistä ei laaturekisteriä Suomessa ole</q>; a study run by the Cancer Registry, THL and FICAN is assessing a cancer quality registry, starting with lung cancer | Filha programme p.21 | verified locally |
| <q lang="fi">Tällä hetkellä keuhkosyöpään liittyvien tietojen raportointi, kerääminen ja tallentaminen on puutteellista</q>; nationally uniform recording instructions (<q lang="fi">yhtenäiset kirjaamisohjeet</q>) must be ensured | Filha programme p.21 | verified locally |
| Strategy target: ≥70% of cancers diagnosed at stage I–II. This cannot be measured while stage is missing for half of patients | Strategy p.5; report §4.1.3 | verified locally |
| KYS reviews every patient in a weekly MDT, Keski-Suomi every new case, HUS only <q lang="en">when needed</q>. MDT practice differs, as well as its coding | Regional pathways | verified by Hellu, read 14 Nov |

**Why:** without complete recording, county comparisons of curative treatment cannot be adjusted for
stage, and ‘no treatment record’ cannot be separated from ‘not treated’. This underpins everything else
in the brief.

---

## Not used (yet)

- <q lang="en">One-third split</q>: mentor insight; source to confirm with Kaisa (pathway_brief §9).

## Corrections to the background brief (from the Filha check)

- The regional variation the programme names is in diagnostic speed, **organisation of care
  responsibility** (<q lang="fi">hoitovastuun järjestämisessä</q>) and surgery volumes, not <q lang="en">referral organisation</q> (p.4).
- Common lung cancer diagnostic guidelines **do** exist (p.4; Käypä hoito ‘Keuhkosyöpä’ 2017, cited as
  ref. 8). What is missing is national guidance on timing.
- The programme **does** list access to care as an indicator (Table 2, p.18), but leaves it undefined.

Page numbers for the Filha programme are printed pages; PDF page = printed + 9. Quotes are in
`docs/source_verification.md`.
