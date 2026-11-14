# Lingonberry: Equal Care Across Finland (Junction 2026)

AstraZeneca challenge: show where each Finnish wellbeing services county's lung cancer
pathway lags, how sure we are, and what to do first. Every claim traced to a public source.
Also entered in Google DeepMind's "Best Use of Gemini API".

## Rules
- Public aggregate data only. No patient-level data, ever.
- Gap figures are computed in our own Python code, never by an LLM.
- Every number in the brief goes into the claim ledger with source, table/figure id and status.
- Never commit `.env`. Never print or log API keys.
- MIT licence for all code.

## Stack and commands
- Python 3.12, managed with uv: `uv add <pkg>`, `uv run python <script>`
- pandas, pdfplumber, pypdf, pydantic, python-dotenv, streamlit, google-genai, lxml
- Gemini: MODEL_EXTRACT=gemini-4-hydrogen, MODEL_REASON=gemini-4-argon (from .env)
- Windows / PowerShell

## Data
- Main source: "Keuhkosyöpä Suomessa 2019–2023" (Finnish Cancer Registry / Cancer Society),
  https://syoparekisteri.fi/assets/themes/ssy3/factsheets/keuhkosyoparaportti.html
  Saved copy: data/raw/keuhkosyoparaportti_2019_2023.html (live site returns 403 to scripts)
- src/read_factsheet.py: all HTML tables -> data/processed/factsheet/table_XX.csv
- src/clean_county.py: table 10 (treatment type by county) -> data/processed/county_treatment.csv
  Rows have levels: county / area / national.
- Regional charts (Kuva 6, 7, ...) are not HTML tables yet; check page source for embedded data.
- Backup source: Malila et al. 2024 PDF (2018–2022).

## Findings so far (unverified until definitions are checked)
- Curative share by county: 18.5% (Lappi) to 33.7% (Keski-Uusimaa).
- No treatment data: 16.4% (Kymenlaakso) to 42.8% (Etelä-Karjala).
- MDT coding: 20–37% in a few counties, ~0% elsewhere -> recording practice, a blind spot.
- Treatment-type shares do not sum to 100%: categories overlap. Never present as a breakdown.
- Shares are unadjusted for age and stage.
- Candidate demo county: Etelä-Karjala.

## Open checks
- Definitions and denominators of table 10 categories (report section 4.2).
- Meaning of NaN cells (missing vs suppressed).
- Add 95% confidence intervals from counts.