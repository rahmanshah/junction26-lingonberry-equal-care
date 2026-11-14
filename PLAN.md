# Build plan (tick as done)

## 0. Setup
- [x] Repo, MIT licence, uv, .env, Gemini smoke test
- [x] Read report tables into CSV (src/read_factsheet.py)
- [x] Tidy county treatment table (src/clean_county.py)

## 1. Data (by Sat 12:00)
- [x] Verify table 10 definitions, denominators and NaN meaning (docs/definitions.md)
- [x] Wilson 95% CIs per county and treatment type (src/add_ci.py)
- [x] Chart: curative vs no-treatment-record share (src/plot_scatter.py)
- [x] Survey data behind charts (docs/chart_data.md): county figures are PNG only
- [x] Digitise Kuva 16 curative, 3 demo counties + national line (src/digitise_kuva16.py)
- [ ] Digitise rest of Kuva 16, Kuva 7, Kuva 13 only if needed
- [x] Blind-spot table v1 from the report (src/build_blind_spots.py, docs/blind_spots.md)
- [x] Blind-spot table: add strategy/roadmap evidence, MOT delays, regional pathways, mentor insights
- [x] Verify strategy p.33, roadmap 3.1.2, named contact, THL 21/2016 (docs/source_verification.md)
- [x] Draft 3 recommendations (docs/recommendations.md)
- [ ] Choose gap metric and demo county (sync 12:00)

## 2. Claim ledger (Sat 12:30-14:00)
- [ ] SQLite schema: claim, value, unit, county, source, table/figure, status
- [ ] Load all numbers used in the brief, with source links

## 3. Gemini pipeline (Sat 13:00-16:00)
- [ ] Extract actions from strategy + roadmap PDFs with verbatim quote and page (Hydrogen)
- [ ] Code check: quote appears on cited page; failures = draft
- [ ] Draft 3 recommendations with Argon, each linked to sources
- [ ] Save all raw model responses to disk

## 4. App (Sat 16:00-18:00)
- [ ] Streamlit: county picker, three questions (where we lag / how sure / what first)
- [ ] Pathway view with gaps and blind spots
- [ ] Limitations panel
- [ ] First end-to-end demo by 18:00

## 5. Polish and deploy (Sat evening)
- [ ] Deploy; README with run steps and sources
- [ ] Clarity test with an outsider

## 6. Submit (Sun before 10:00)
- [ ] Demo recording and 2-minute pitch video
- [ ] Final README, Platform fields, submit