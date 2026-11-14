# Table 10 definitions (verified against the report)

Source: "Keuhkosyöpä Suomessa 2019–2023", saved copy `data/raw/keuhkosyoparaportti_2019_2023.html`.

**Numbering:** the report numbers its tables from 1, and our `read_factsheet.py` numbers them from 0.
So `table_10.csv` (treatment by county) is the report's **Taulukko 11** ("…hyvinvointialueittain").
`table_05.csv` is **Taulukko 6** (treatment by year, national).

## a) Category definitions and denominator

| Category | Definition (quote) | Where |
|---|---|---|
| Parantava | "Parantavaan hoitoon on luettu leikkaushoito, stereotaktinen sädehoito, neoadjuvantti-, liitännäis- ja kemosädehoito." / "parantava eli kuratiivistavoitteinen hoito" | 4.2; 3.3 |
| Jarruttava | "jarruttava eli ei-kuratiivinen hoito"; "Jarruttavaa sädehoitoa sai 16 % potilaista, lääkehoitoa 21 % ja jompaakumpaa näistä 31 %." | 3.3; 4.2, Taulukko 8 |
| Oireenmukainen | "Oireenmukainen hoito on joko oireenmukaista sädehoitoa tai käynnille kirjattu palliatiivinen tai saattohoitodiagnoosi Z51.5." | 4.2, Taulukko 9 |
| Ei hoitotietoa | "Kokonaan ilman hoitokirjauksia jäi yhteensä 4089 (27,5 %) potilasta." (no treatment record of any type within 12 months) | 4.2, Kuva 14 |
| MDT-käsittely | "MDT-kirjaukset poimittiin HILMO:sta toimenpidekoodeja WZC15 ja WZC20 käyttäen. … Erikoissairaanhoidon toimenpiteet viedään HILMO:on vain suorista potilaskontakteista, joten saatu tieto ei kuvaa kattavasti moniammatillisen käsittelyn laajuutta." | 3.3 |

Procedure codes for each category: Liite, Taulukko 13.

**Denominator of "Osuus (%)":** the report gives no formula. We infer it from the data:
- `Yhteensä` = all new lung cancer patients (C33–C34, 2019–2023) living in the county. This figure is the same for every treatment type.
- n / Yhteensä reproduces every printed share (`clean_county.py` check).
- Region is assigned by "potilaiden syövän toteamisvuoden alun kotikuntaan" (3.3).
- Area totals sum to 14 774 = 14 873 − 93 (Ahvenanmaa, "ei esitetä aluekohtaisissa tuloksissa pienten lukumäärien takia") − 6 (unknown home municipality, "N 6") (3.3).
- Window: 12 months from the start of follow-up. Follow-up starts at the registry diagnosis date or at a HILMO C33–C34/D38.1 visit up to 3 months earlier (3.1).
- Shares are crude (not age-adjusted). Age-adjusted county shares exist only in the figure Kuva 16 (4.2.1).

## b) Why the categories overlap

- "Ryhmät eivät ole toisiaan poissulkevia." (4.2, under Taulukko 6)
- "Samalla potilaalla voi olla useampia eri hoitomuotoja" (footnote to Taulukko 6; Kuva 2)
- A patient is counted in every category where they have a record within 12 months (for example, curative surgery followed by palliative care).
- Only Ei hoitotietoa is exclusive of the other three.
- National shares sum to 124.4% (27.0 + 30.4 + 39.5 + 27.5). County sums range from 107.9% (Varsinais-Suomi) to 142.7% (Päijät-Häme). Higher sums mean more recorded switching between treatment types.
- Kuva 14 does give an exclusive breakdown: each patient is placed once, by the most curative treatment ("parantava, jarruttava, oireenmukainen ja ei hoitotietoa"). It is national only, by year.

## c) Small-number suppression and the 4 missing MDT rows

- The report never says that small cells are suppressed. It only drops whole regions (Ahvenanmaa) and Kuva 16 bars that are "liian pieni ikävakiointiin".
- Table 11 prints MDT cells with n = 1 (for example Helsinki, Etelä-Savo). So small counts are shown, not hidden.
- The area subtotals show that the 4 counties without an MDT row have **zero** MDT records:
  - Etelä-Suomi: the area MDT count of 9 equals the sum of the listed counties. The missing denominator, 1108, equals Etelä-Karjala 355 + Itä-Uusimaa 272 + Keski-Uusimaa 481.
  - Itä-Suomi: the area MDT count of 26 equals the sum of the listed counties. The missing denominator, 510, equals Pohjois-Karjala.
- **Conclusion:** a missing MDT row means 0 records. It does not mean the cell was suppressed. Reason: rows with n = 0 are left out of the table.

**NaN cells:** the NaNs in `table_10.csv` sit only in the `Hoitomuoto` and `Yhteistyöalue` columns, which were merged cells in the HTML (`clean_county.py` fills them forward), and in the extra column `Unnamed: 6`, a parsing leftover. No count, total or share is NaN.

## d) National 27.0% vs 24%

- **27.0%** = 4009 / 14 873: patients with *any* curative-treatment record within 12 months. "Parantavaan hoitoon ohjautui 4009 potilasta kaikista uusista keuhkosyövistä (27,0 %)" (3.2; Taulukko 6 total row).
- **24%** = 3584 / 14 873 = 24.1%: patients whose *first* treatment was curative. "Hoitopolkuanalyysissä ensivaiheen hoitomuoto oli parantava 3584 potilaalla (24 %)" (4.2.2, Taulukko 12).
- The difference, 425 patients, had another treatment first and curative treatment later.
- The summary rounds the figure in words: "Parantavaa hoitoa … sai runsas neljännes potilaista" and "vain noin neljännes potilaista ohjautui parantavaan hoitoon" (1).
- **Confirmed:** the report's cover image reads "Ensivaiheen hoitomuoto, Parantava 24 %". That is the §4.2.2 first-treatment measure. The saved HTML does not include the cover.
- **For county comparisons, use 27.0% as the national benchmark.** It is the "any curative record" figure, which is how Table 11 counts curative treatment.
