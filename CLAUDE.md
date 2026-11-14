# Lingonberry: Equal Care Across Finland (Junction 2026)

AstraZeneca challenge: show where each Finnish wellbeing services county's lung cancer
pathway lags, how sure we are, and what to do first. Every claim traced to a public source.
Also entered in Google DeepMind's "Best Use of Gemini API".
Build checklist: PLAN.md (tick tasks when done).

## Rules
- Public aggregate data only. No patient-level data, ever.
- Gap figures are computed in our own Python code, never by an LLM.
- Every number in the brief goes into the claim ledger with source, table/figure id and status.
- Never commit `.env`. Never print or log API keys.
- Never modify files in `data/raw/`.
- MIT licence for all code.
- Shah owns the data scripts in `src/`. Pull before changing them; commit after each task.

## Stack and commands
- Python 3.12, managed with uv: `uv add <pkg>`, `uv run python <script>`
- pandas, lxml, pdfplumber, pypdf, pydantic, python-dotenv, streamlit, google-genai
- Gemini (from .env): MODEL_EXTRACT=gemini-4-hydrogen, MODEL_REASON=gemini-4-argon
- Windows / PowerShell

## Data
- Main source: "Keuhkosyöpä Suomessa 2019–2023 – Rekisteripohjainen katsaus
  diagnostiikkaan, hoitopolkuihin ja hoidon laatuun" (Malila, Pitkäniemi, Hermiö,
  Johansson, Seppä, Toikkanen, Andersén; Finnish Cancer Registry). 14,873 cases.
  https://syoparekisteri.fi/assets/themes/ssy3/factsheets/keuhkosyoparaportti.html
  Saved copy: data/raw/keuhkosyoparaportti_2019_2023.html (live site returns 403 to scripts).
  Cite as the live URL, "retrieved 14 Nov 2026".
- Backup source: Malila et al. 2024, "Keuhkosyöpä Suomessa" (2018–2022), data/raw/lung_report_2024.pdf
- src/read_factsheet.py: all HTML tables -> data/processed/factsheet/table_XX.csv
- src/clean_county.py: table 10 (treatment type by county) -> data/processed/county_treatment.csv
  - level = county (22 counties incl. Helsingin kaupunki), area (5 collaborative-area
    subtotals, originally labelled "Yhteistyöalue yhteensä"), empty header and national rows dropped.
  - Checks: n/total reproduces printed share (0 mismatches); 22 counties per treatment type
    except MDT-käsittely (18 in the report; the other 4 are zero counts).
  - Treatment types: Parantava (curative), Jarruttava (life-prolonging), Oireenmukainen
    (symptomatic), Ei hoitotietoa (no treatment record within 12 months), MDT-käsittely
    (MDT meeting coded).
- CSV numbering is 0-based, the report's is 1-based: table_10.csv = Taulukko 11 (county),
  table_05.csv = Taulukko 6, table_04.csv = Taulukko 5. Cite the report's numbers.
- Definitions, denominators, overlap, suppression: docs/definitions.md (verified, with quotes).
- src/add_ci.py: adds MDT n = 0 rows ("0 records reported") and Wilson 95% CIs (ci_low,
  ci_high), national_share, ci_contains_national, vs_national (below / above / not distinguishable).
- src/plot_scatter.py -> outputs/curative_vs_missing.png.
- National totals: Taulukko 6 (curative 27.0% = 4,009 / 14,873, any curative record in
  12 months) and Taulukko 5 (MDT 893; no treatment record 14,873 − 10,784 = 4,089, 27.5%).
  The cover's "Ensivaiheen hoitomuoto, Parantava 24 %" is first treatment (§4.2.2, 3,584).
  Benchmark for county comparisons: 27.0%.
- Regional charts: the county figures (Kuva 7, 13, 16, 20, 23) are PNG images only, so they
  must be digitised. Kuva 18, 19, 22 (survival, national/area) are Plotly JSON with exact values.
  Details: docs/chart_data.md.

## Findings so far (definitions verified; shares crude, not adjusted for age or stage)
- Treatment-type shares overlap and do not sum to 100%. Never present them as a breakdown.
- Curative share: 18.5% (Lappi) to 35.6% (Vantaa–Kerava); national 27.0%.
- With 95% CIs, curative is below national in 7 counties, above in 5, not distinguishable in 10.
- No treatment record: 16.4% (Kymenlaakso) to 43.1% (Varsinais-Suomi); national 27.5%.
  CAVEAT: "Ei hoitotietoa" mixes untreated patients (79% of them died within the year, §4.2.2)
  and treatment that was given but not recorded in HILMO. Never call it "missing data" or
  "untreated"; label it "No treatment record within 12 months".
- Varsinais-Suomi: 43.1% no treatment record and only 9.7% life-prolonging (others ~16–45%)
  -> likely drug treatment not recorded.
- MDT coded: 37.4% Pirkanmaa, 32.4% Etelä-Pohjanmaa, 21.6% Kanta-Häme, ~0–7% elsewhere,
  0.1% Helsinki. Etelä-Karjala, Itä-Uusimaa, Keski-Uusimaa, Pohjois-Karjala: 0 records reported
  (area subtotals prove zero, not suppression). Recording practice, not care: a blind spot.
  Report §3.3: "Erikoissairaanhoidon toimenpiteet viedään HILMO:on vain suorista
  potilaskontakteista, joten saatu tieto ei kuvaa kattavasti moniammatillisen käsittelyn laajuutta."
- County patterns (curative share vs no-treatment-record share):
  - Low curative, good data -> likely real gap: Kymenlaakso (19.3% / 16.4%)
  - Low curative, poor data -> can't tell: Lappi (18.5% / 33.8%), Etelä-Karjala (18.9% / 42.8%)
  - Average curative, worst data -> recording gap: Varsinais-Suomi (24.3% / 43.1%)
  - High curative benchmarks: Vantaa–Kerava, Keski-Uusimaa, Helsinki
- Demo counties (to confirm at 12:00 sync): Kymenlaakso, Etelä-Karjala, Varsinais-Suomi.
- Not adjusted for age or stage: a low curative share is not proof of worse care.

- Age-adjusted curative (Kuva 16, digitised, ±0.5 pp; data/processed/kuva16_curative_digitised.csv,
  src/digitise_kuva16.py): national line 26.7% men / 26.9% women.
  - Kymenlaakso: men 17.9 [13.9–22.9] below; women 22.6 [16.8–29.3] lower but CI overlaps.
  - Etelä-Karjala: men 18.9 [13.5–25.7] below; women 19.8 [13.4–29.0] lower but CI overlaps.
  - Varsinais-Suomi: men 22.7 (CI hidden in dot, upper ≤ ~26.0) borderline below; women 27.4
    [23.1–31.8] not below.

## Open checks
- Kuva 16 for other counties/treatments: digitise only if needed (ledger status
  "digitised from figure").
- Kuva 7 (diagnosis method) and Kuva 13 (stage coverage) by county: PNG stacked bars, digitise.