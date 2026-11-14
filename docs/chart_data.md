# What data sits behind the report's figures (saved HTML)

Checked by parsing `data/raw/keuhkosyoparaportti_2019_2023.html`. The page is a Quarto/R export.

## Summary

| Figure | Content | Level | Format in page | Extractable? |
|---|---|---|---|---|
| Kuva 6 | Toteamistapa | yhteistyöalue | base64 PNG (1344×960), counts printed on bars | Digitise or read printed counts |
| Kuva 7 | Toteamistapa (6 classes) | **county** | base64 PNG (1344×1728), no numbers | Digitise only |
| Kuva 12 | Levinneisyysluokitus | yhteistyöalue | base64 PNG, counts printed on bars | Digitise or read printed counts |
| Kuva 13 | Levinneisyysluokitus (Ei tietoa / Syre / Stage / Sanallinen / TNM) | **county** | base64 PNG (1344×1728), no numbers | Digitise only |
| Kuva 15 | Age-adjusted treatment shares + 95% CI, by sex | yhteistyöalue | base64 PNG | Digitise only |
| **Kuva 16** | Age-adjusted treatment shares + 95% CI, by sex | **county** | base64 PNG (1728×2304), no numbers | Digitise only |
| Kuva 18 | Age-adjusted 12-month survival, by sex | national | **Plotly JSON** | Yes, exact values |
| Kuva 19 | Survival by sex | yhteistyöalue | **Plotly JSON** (20 traces) | Yes, exact values |
| Kuva 20 | Survival by sex | county | base64 PNG | Digitise only |
| Kuva 22 | Survival by first treatment | yhteistyöalue | **Plotly JSON** (40 traces) | Yes, exact values |
| Kuva 23 | Survival by first treatment | county | base64 PNG | Digitise only |

- The PNGs carry no text metadata and no alt text.
- No hidden table or JSON exists for any PNG figure.
- The 3.6 MB inline script is the Plotly/htmlwidgets library, not data.
- The two files in `keuhkosyoparaportti_2019_2023_files/` are page assets, not data.
- Plotly traces hold `x` (months, in steps of 1/24 year), `y` (survival %) and hover `text` (for example "88.6 %").

## Kuva 16 in detail (age-adjusted county shares)

- **Layout:** 22 counties × {Mies, Nainen} × {Parantava, Jarruttava, Oireenmukainen}. Each cell shows a dot and a thick CI bar, plus a dashed national line. The x-axis runs 0–60%, at roughly 3 px per percentage point.
- **Gaps:**
  - The figure has **no Ei hoitotietoa or MDT panel**.
  - It gives **no combined-sex value**, only Mies and Nainen separately.
  - Kainuu is missing Parantava and Jarruttava for both sexes ("liian pieni ikävakiointiin").
- **Method (§3.3):** direct age standardisation over 4 age groups, using the whole country's patients as the standard population. CIs use the normal approximation.
- **Digitising it:** feasible in our own Python by colour segmentation. Dots and bars are flat colours on known axes. Expected accuracy is about ±0.5 percentage points, and CI ends will be less precise than the dots.
  - 22 × 2 × 3 = 132 cells, less 4 for Kainuu, gives 128 cells.
  - Every value would carry the ledger status "digitised from figure", not "published value".
- **Using it for gap claims:**
  - It can confirm or refute that a crude gap survives age adjustment, for example Kymenlaakso and Etelä-Karjala curative below national, which both sexes appear to show visually.
  - It cannot give a single age-adjusted county figure, because the report publishes no counts by county and age to recompute one.

## Kuva 7 and Kuva 13 (stacked bars)

- Flat colour segments with 0–100% spanning about 770 px. Pixel boundaries give each share to about ±0.2 percentage points.
- County totals from Taulukko 11 then give approximate counts and Wilson CIs.
- The county order matches Taulukko 11, alphabetical within each area. Note that Kuva 16 uses a different order.

## Plotly figures (19, 22)

These are exact and machine-readable, but only by collaborative area, not by county.
