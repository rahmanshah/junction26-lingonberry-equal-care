# Source verification: strategy, roadmap and Filha programme (Finnish PDFs)

Checked 14 Nov 2026 against the local files in `data/raw/`. Text was extracted with pdfplumber and
read column by column for two-column pages. Quotes are verbatim; hyphenation at line breaks is
removed. Translations are ours.

## Files

| File | What it actually is | Pages | Printed page = PDF index? |
|---|---|---|---|
| `strategy_2026_2035_fi.pdf` | Kansallinen syöpästrategia 2026–2035 (STM) | 64 | Yes (pp.1–2 unnumbered) |
| `roadmap_2026_2031_fi.pdf` | Kansallinen syöpästrategia 2026–2035: Toimeenpanon tiekartta vuosille 2026–2031 | 111 | Yes (p.1 unnumbered) |
| `source_list_fi.pdf` | "Cancer Strategy and Cancer data – pre-pack links" (2 pages of links) | 2 | Yes |
| `filha_lung_programme_2026_fi.pdf` | Valtakunnallinen keuhkosyöpäohjelma 2026–2035 (Filha ry; working group 18.5.2026; preprint) | 38 | **No: printed = PDF − 9.** PDF pp.1–9 (cover, forewords, definitions, summary, contents) are unnumbered; printed p.1 = PDF p.10 |

- **English strategy:** optional and not downloaded; cite the Finnish original.
- **Background pack:** there is none. The challenge's "background pack" link is the Finnish strategy itself.
- The earlier `strategy_2026_2035_en.pdf` and `background_pack_fi.pdf` were byte-identical copies of the
  Finnish strategy and have been deleted.
- All files in `data/raw/` now have unique MD5s.

## a) Strategy p.33: no national system for cancer guidelines and pathways. **Verified.**

Printed p.33 = PDF p.33, section 3.1 "Kansalliset hoitosuositukset ja hoitoketjut ohjaavat
yhdenvertaista, viiveetöntä ja vaikuttavaa hoitoa" (right-hand column):

> "Suomessa ei ole yhtenäistä kansallista järjestelmää, joka ohjaisi syöpäkohtaisten
> hoitosuositusten laatimista sekä niihin perustuvien hoitoketjujen toteutusta ja seurantaa (laatu- ja
> vaikuttavuustavoitteet/indikaattorit, mukaan lukien hoitoonpääsy sekä syöpäkohtaiset ja geneeriset
> PROM-vointimittarit). Olemassa olevia hoitosuosituksia ja -ketjuja sekä seurattavia tavoitteita ja
> indikaattoreita ei koordinoida kansallisella tasolla. Tämä ylläpitää alueellista eriarvoisuutta syövän
> hoidon saatavuudessa ja vaikuttavuudessa."

*Finland has no unified national system to steer the drafting of cancer-specific treatment
recommendations, or the implementation and monitoring of care pathways based on them (quality and
effectiveness targets/indicators, including access to care, and cancer-specific and generic PROMs).
Existing recommendations and pathways, and the targets and indicators to be monitored, are not
coordinated nationally. This maintains regional inequality in the availability and effectiveness of
cancer care.*

Related, the same page lists among its indicators: "Potilaat pääsevät hoitoon tavoiteaikojen
puitteissa." (*Patients access care within the target times.*)

## b) Roadmap measure 3.1.2: national pathways and target times for five cancers, 2026–2028, Nordic model. **Verified, but split across pp.56–57.**

The measure starts on printed p.56 (= PDF p.56). The Nordic model is on p.56, but **the five-cancer,
2026–2028 timetable is on p.57**, not p.56.

p.56, heading:
> "Toimenpide 3.1.2 Laaditaan syöpäkohtaiset hoitoketjukuvaukset, ja niiden pohjalta sovelletut
> alueelliset hoitoketjut, sekä mekanismi niiden ylläpitoon ja hallintaan"

*Measure 3.1.2: Draw up cancer-specific care pathway descriptions, regional pathways adapted from them,
and a mechanism to maintain and manage them.*

p.56, Nordic model:
> "Kansalliset hoitoketjut kuvataan hyödyntäen pohjoismaissa kehitettyjä malleja. Tällaisia ovat Tanskan
> Kræftpakkeforløb, Ruotsin standardiserade vårdförlopp (SVF) ja Norjan Pakkeforløp - kreft, joissa
> kansalliset hoitosuositukset ja standardoidut hoitopolut muodostavat yhtenäisen, kansallisesti johdetun
> kokonaisuuden."

*National pathways are described using models developed in the Nordic countries: Denmark's
Kræftpakkeforløb, Sweden's standardised care pathways (SVF) and Norway's Pakkeforløp – kreft, in which
national recommendations and standardised pathways form a single, nationally led whole.*

p.56, content of pathways:
> "Ketjuissa määritellään ja sovitaan mm. työnjaosta eri toimijoiden välillä, tavoitelluista
> hoitoonpääsyajoista, keskeisistä laatu- ja vaikuttavuusindikaattoreista sekä kirjaamis- ja
> koodistokäytännöistä."

*The pathways define and agree, among other things, the division of work between actors, target access
times, key quality and effectiveness indicators, and recording and coding practices.*

p.57, timetable:
> "2026–2028: Kansalliset hoitoketjukuvaukset tehty viidestä syövästä ja syöpäkohtaiset
> hoitoonpääsyajat on määritetty."

*2026–2028: National pathway descriptions completed for five cancers, and cancer-specific access times
defined.*

p.57, indicator: "Mittari: Potilaat pääsevät hoitoon tavoiteaikojen puitteissa." (*Indicator: patients
access care within the target times.*)

**Note:** the roadmap does not name the five cancers, so it does not say whether lung cancer is one of
them.

## c) Pathway coordinator / named contact, and THL access-time monitoring (Ohjaus 21/2016)

### Named contact: **Found in the roadmap**, measure 1.2.3, p.32. The care phase is not specified.

> "Toimenpide 1.2.3 Luodaan toimintamalli ja ohjeistus syövän hoidon koordinaatiosta vastaavan, nimetyn
> työntekijän mallista"

*Measure 1.2.3: Create an operating model and guidance for a named worker responsible for coordinating
cancer care.*

> "Tärkeintä on että potilas tietää, kenellä on kokonaiskuva hänen hoidostaan, ja miten hän voi tarpeen
> mukaan olla yhteydessä hoitavaan yksikköön."

*The most important thing is that the patient knows who has the overall picture of their care, and how
they can contact the treating unit when needed.*

> "Selvityksessä kartoitetaan, missä hoidon vaiheessa ja mille potilasryhmille hoidon koordinaatiosta
> vastaava työntekijä olisi tärkeintä kohdentaa."

*The review will map at which phase of care, and for which patient groups, a care coordinator is most
important.*

Timetable (p.32): "2026–2028: Ohjeistus syövän hoidon koordinaatiosta vastaavan nimetyn lääkärin,
hoitajan tai erityistyöntekijän mallista. 2029–2031: Hyvinvointialueet ovat ottaneet tämän ohjeistuksen
käyttöön." (*2026–2028: guidance on a named doctor, nurse or specialist worker coordinating cancer care.
2029–2031: wellbeing services counties have adopted it.*)

**So:** a named contact is planned. Whether it covers the **diagnostic phase**, our focus, is left open:
the text lists support needs "hoitojen aikana sekä kuntoutuksessa" (*during treatment and
rehabilitation*).

### THL Ohjaus 21/2016: **not in the roadmap. Cited in the strategy**, p.5.

- The roadmap has no mention of 21/2016 or "Hoitoonpääsyn seuranta syövän hoidossa".
- It names "hoitoonpääsyajat" (*access times*) as an indicator, for example on p.23–24 for poor-prognosis
  cancers, but without the THL definitions.

Strategy p.5 (= PDF p.5), "Strategiset tavoitteet", indicator under "Varmistetaan yhdenvertainen ja
vaikuttava syövänhoito":
> "Potilaat pääsevät hoitoon tavoiteaikojen puitteissa***"
> "*** THL (Ohjaus 21/2016). Hoitoonpääsyn seuranta syövän hoidossa."

*Patients access care within the target times. Footnote: THL (Guidance 21/2016), Monitoring access to
cancer care.*

**So:** the strategy ties its access-time indicator to the THL 21/2016 definitions. The lung cancer
report (§3.3) also used "Hoitoonpääsyn seuranta syövän hoidossa (THL 2016)" to choose its procedure
codes. The THL document itself is not in `data/raw/`, so its content (16 cancers, in force 1 Jan 2017)
stays "verified by Hellu".

## Other roadmap passages used later

**Measure 2.5.2 (pp.52–53): standardised referral criteria.**
- p.52 heading: "Tuetaan sujuvaa siirtymää erikoissairaanhoitoon määrittämällä kansallisiin
  hoitoketjuihin kuuluvat standardoidut lähetekriteerit, joiden täyttyessä mahdollisista syöpäoireista
  kärsivät potilaat ohjataan nopeasti tarvittaviin diagnostisiin tutkimuksiin" (*support a smooth
  transfer to specialist care by defining standardised referral criteria within the national pathways,
  so that patients with possible cancer symptoms who meet them are directed quickly to diagnostic
  tests*).
- p.53 timetable: "2026–2028: Standardoidut lähetekriteerit ja oirelähtöiset toimintamallit sisällytetty
  vähintään viiden yleisimmän syövän kansallisiin hoitoketjukuvauksiin." (*2026–2028: standardised
  referral criteria and symptom-based models included in the national pathways of at least the five most
  common cancers.*)

**Measure 3.2.1 (pp.59–60): national cancer quality registry.**
- p.59: "Perustetaan THL:n Syöpärekisterin yhteyteen kansallinen syövän hoidon laaturekisteri." (*A
  national cancer care quality registry will be set up alongside THL's Cancer Registry.*)
- p.60 indicator: "Laaturekisterin tietopohja (ml. levinneisyystieto) mahdollistaa laadun ja
  vaikuttavuuden luotettavan arvioinnin ja vertailun (tietopohjan kattavuus 90 %)" (*the registry's data,
  including stage, allows reliable assessment and comparison of quality and effectiveness, with 90% data
  coverage*).

## Filha National Lung Cancer Programme 2026–2035 (pathway_brief.md §3)

File: `filha_lung_programme_2026_fi.pdf`. Page numbers below are **printed** pages; PDF page = printed + 9.
The summary ("Tiivistelmä") is on unnumbered PDF p.7. Read in full; Table 2 was also read from the
rendered page, because its text extraction is scrambled.

### a) An action plan, not a treatment recommendation: **verified**, p.1

> "Ohjelman tarkoitus ei ole toimia hoitosuosituksena, vaan luoda toimintasuunnitelma, jolla
> ennaltaehkäistään keuhkosyöpää ja parannetaan potilaan saamaa hoitoa ja sen oikea-aikaisuutta."

*The programme is not meant to serve as a treatment recommendation, but to create an action plan to
prevent lung cancer and improve the care patients receive and its timeliness.*

Also on p.17, its scope: "kattaa koko keuhkosyövän hoitoketju ensioireista palliatiiviseen hoitoon"
(*covers the whole lung cancer care chain from first symptoms to palliative care*).

### b) No day-based targets; no precise national guidance on the timing of diagnostic steps: **verified, with one nuance**, p.4

> "Keuhkosyöpien diagnostiikkaan on Suomessa yhteiset ohjeet, mutta alueellinen vaihtelu diagnoosin
> nopeudessa, hoitovastuun järjestämisessä tai leikkauksien määrässä on suurta. Valtakunnallisesti ei ole
> ollut tarkkaa yhtenäistä ohjeistusta siitä, millä aikataululla diagnostiikan eri osa-alueet tulisi olla
> tehtyinä."

*Finland has common guidelines for lung cancer diagnostics, but regional variation in the speed of
diagnosis, the organisation of care responsibility and the number of operations is large. Nationally
there has been no precise uniform guidance on the timetable within which the different parts of
diagnostics should be completed.*

- **No day-based targets:** confirmed by reading the whole document and searching for time terms (päivä,
  viikko, kuukausi, aikaraja, tavoiteaika). The programme sets no time targets for referral, diagnosis or
  treatment.
- **Nuance:** the same sentence says common diagnostic guidelines **do** exist. What is missing is
  national guidance on *timing*. The programme also cites the Käypä hoito "Keuhkosyöpä" guideline (2017;
  reference 8, p.27).

### c) Primary-care referral criteria in an upcoming diagnostic recommendation, and when: **verified**, pp.3, 16, 24

p.3:
> "Keuhkosyövän oireita ja lähetekriteereitä käsitellään tarkemmin diagnostiikkasuosituksessa, joka
> julkaistaan myöhemmin erillisenä osionaan."

*Lung cancer symptoms and referral criteria are covered in more detail in the diagnostics
recommendation, to be published later as a separate part.*

p.16:
> "Tämän ohjelman yhtenä toimenpiteenä tuotetaan kansallinen suositus keuhkosyöpien diagnostiikasta. Se
> sisältää myös lähetekriteerit perusterveydenhuollolle ja suositellut aikarajat erikoissairaanhoitoon
> eri diagnostiikan polun vaiheille."

*One measure of this programme is a national recommendation on lung cancer diagnostics. It will also
contain referral criteria for primary care and recommended time limits in specialist care for the
different stages of the diagnostic pathway.*

When (p.24):
> "Väliarvio toteutetaan vuonna 2030, ohjelman puolivälissä ja loppuarviointi vuonna 2036. Eri
> osa-alueiden suositukset toteutetaan ennen väliarviointia."

*The mid-term evaluation is in 2030 and the final evaluation in 2036. Recommendations for the
different areas will be completed before the mid-term evaluation.*

p.20 says work on the diagnostics recommendation has already started ("on jo aloitettu työstämään
keuhkosyövän diagnostiikkasuositusta").

**So:** the recommendation is due before the 2030 mid-term evaluation, with no exact date. Besides
referral criteria, it will also bring **recommended time limits**.

### d) No lung cancer or cancer quality registry; Cancer Registry, THL and FICAN assessing: **verified, slightly reworded**, p.21

> "Keuhkosyövästä tai muistakaan syövistä ei laaturekisteriä Suomessa ole."

*Finland has no quality registry for lung cancer or for any other cancer.*

> "Osana Valtakunnallista keuhkosyöpäohjelmaa työryhmän jäsen osallistuu asiantuntijana
> Syöpärekisterin, THL:n ja FICANin hallinnoimaan tutkimukseen syöpien laaturekisteristä. Tutkimuksen
> tavoitteena on selvittää ja arvioida ensimmäisenä keuhkosyöpien hoidon toteutumista ja hoitotuloksia."

*As part of the programme, a working-group member takes part as an expert in a study on a cancer quality
registry run by the Cancer Registry, THL and FICAN. The study aims first to examine and assess how lung
cancer treatment is delivered and its outcomes.*

**Nuance:** the brief's "assessing what registry is needed, starting with lung cancer" is a fair summary.
The text itself describes a research study on a cancer quality registry that looks at lung cancer first.

Also on p.21: "Tällä hetkellä keuhkosyöpään liittyvien tietojen raportointi, kerääminen ja tallentaminen
on puutteellista." (*Reporting, collection and storage of lung cancer data is currently incomplete.*)
And: "Koko valtakunnan yhtenäiset kirjaamisohjeet ja niiden käyttö on tärkeää varmistaa" (*nationally
uniform recording instructions, and their use, must be ensured*).

### e) Monitoring via annual indicators, hospital surveys and survival data, not pathway timestamps: **partly verified; the brief overstates the last part**

- **Annual indicators** (summary, unnumbered PDF p.7): "Tavoitteiden toteutumista seurataan vuosittain
  selkeillä mittareilla, ja tarkastellaan ohjelman puolivälissä tehtävässä väliarviossa sekä ohjelman
  päättyessä." (*Progress is monitored annually with clear indicators, and reviewed at the mid-term
  evaluation and at the end.*) Verified.
- **Hospital surveys** (p.22): "otantakysely keuhkosyöpää hoitaville sairaaloille ohjelman alussa ja
  lopussa" (*a sample survey of hospitals treating lung cancer at the start and end of the programme*).
  Verified.
- **Registry and survival data** (p.23): "Rekisteritietoja hyödynnetään muun muassa keuhkosyövän määrän,
  ennusteen ja hoidon vaikuttavuustietojen seuraamiseen." (*Registry data are used to monitor, among other
  things, the number of lung cancers, prognosis and treatment effectiveness.*) Table 2 (p.18) also lists
  "Rekisteritiedot 1- ja 5-vuotiselossaolosta" (*registry data on 1- and 5-year survival*). Verified.
- **"Not pathway timestamps": overstated.** Table 2 (p.18), under the goal "Yhdenvertainen ja vaikuttava
  hoito jokaiselle asuinpaikasta riippumatta", lists these indicators:

  > "Kysely keuhkosyöpää hoitaville sairaaloille ohjelman alussa ja lopussa; Hoitoonpääsy; suositusten ja
  > ketjujen saatavuus; kansallisesti yhtenäiset tavoitteet ja vaikuttavuuden seurantamittarit on
  > määritelty"

  *Survey of hospitals at the start and end; access to care; availability of recommendations and
  pathways; nationally uniform targets and effectiveness indicators defined.*

  So **access to care ("Hoitoonpääsy") is a listed indicator**. The programme does not say how it will be
  measured: there is no data source, no timestamps and no thresholds. The monitoring text (§4.3, pp.22–23)
  does not mention pathway timestamps.
- **Accurate wording:** "lists access to care as an indicator, but does not define how it is measured;
  the described monitoring relies on registry data, hospital surveys and studies."

### f) Large regional variation in diagnostic speed, referral organisation and surgery volumes: **partly verified; one item mistranslated**, p.4

Quote as in b): "alueellinen vaihtelu diagnoosin nopeudessa, hoitovastuun järjestämisessä tai
leikkauksien määrässä on suurta."

- Diagnostic speed ("diagnoosin nopeudessa"): verified.
- Surgery volumes ("leikkauksien määrässä"): verified.
- "Referral organisation" is **not what it says**. "Hoitovastuun järjestämisessä" means *the organisation
  of care responsibility* (who holds responsibility for treatment).
- Referral is addressed separately, on p.15: "potilas lähetetään jatkotutkimuksiin erikoissairaanhoidon
  yksikköön omien paikallisten ohjeistusten mukaisesti" (*the patient is referred to specialist care
  according to local instructions*). Also on p.15: "Hoidon järjestämisen käytännöt vaihtelevat
  hyvinvointialueittain" (*the organisation of care varies by wellbeing services county*).

### Related mismatch outside §3

- pathway_brief.md §4 (diabetes table) says lung cancer has no national guideline beyond the 2026
  programme.
- The programme says common diagnostic guidelines exist (p.4) and cites the Käypä hoito "Keuhkosyöpä"
  guideline (2017, ref. 8).
- What is missing is national guidance on timing and pathways, not a guideline as such.

## Not verifiable locally (status kept from Hellu's brief)

| Claim | Status |
|---|---|
| THL 21/2016 content (16 cancers, in force 1 Jan 2017) | Verified by Hellu; "no published report" to confirm with mentors |
| Health Care Act §52 time limits, Valvira statement | Verified by Hellu |
| Regional pathways (Keski-Suomi, Pirha, KYS, HUS, OYS, Satakunta) | Verified by Hellu, read 14 Nov |
| MOT delays 56 / 41 / 58 / 155; Sweden 107, Denmark 67 | Preliminary, unpublished (Yle MOT 2025); primary author unknown |
| Referral quality affects triage | Mentor insight (Kaisa) |
| Occupational health is faster | Mentor insight (Hanna) |
