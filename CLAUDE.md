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
    except MDT-käsittely (18).
  - Treatment types: Parantava (curative), Jarruttava (life-prolonging), Oireenmukainen
    (symptomatic), Ei hoitotietoa (no treatment data), MDT-käsittely (MDT meeting coded).
- National totals: table_05.csv (e.g. curative 27.0%, n = 4,009 / 14,873).
  The report cover says 24% curative first-line treatment: different definition, check before use.
- Regional charts (Kuva 6, 7, stage coverage, ...) are not HTML tables; check the saved page
  source for embedded data before using Gemini to read them.

## Findings so far (unadjusted; definitions still to verify)
- Treatment-type shares overlap and do not sum to 100%. Never present them as a breakdown.
- Curative share: 18.5% (Lappi) to 35.6% (Vantaa–Kerava); national 27.0%.
- No treatment data: 16.4% (Kymenlaakso) to 43.1% (Varsinais-Suomi).
- Varsinais-Suomi: 43.1% no treatment data and only 9.7% life-prolonging (others ~16–45%)
  -> likely drug treatment not recorded.
- MDT coded: 37.4% Pirkanmaa, 32.4% Etelä-Pohjanmaa, 21.6% Kanta-Häme, ~0–7% elsewhere,
  0.1% Helsinki. No MDT row at all for Etelä-Karjala, Itä-Uusimaa, Keski-Uusimaa,
  Pohjois-Karjala. Recording practice, not care: a blind spot.
- County patterns (curative share vs no-treatment-data share):
  - Low curative, good data -> likely real gap: Kymenlaakso (19.3% / 16.4%)
  - Low curative, poor data -> can't tell: Lappi (18.5% / 33.8%), Etelä-Karjala (18.9% / 42.8%)
  - Average curative, worst data -> recording gap: Varsinais-Suomi (24.3% / 43.1%)
  - High curative benchmarks: Vantaa–Kerava, Keski-Uusimaa, Helsinki
- Demo counties (to confirm at 12:00 sync): Kymenlaakso, Etelä-Karjala, Varsinais-Suomi.
- Not adjusted for age or stage: a low curative share is not proof of worse care.

## Open checks
- Definitions and denominators of the table 10 categories (report section 4.2).
- Does the report suppress small numbers? (Missing MDT rows: zero or suppressed?)
- Wilson 95% confidence intervals from counts, before ranking small counties.
- County data behind the charts (diagnosis method, stage coverage).