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
- data/raw/ (gitignored; source URLs in README.md; all MD5s unique, checked 14 Nov):
  - keuhkosyoparaportti_2019_2023.html (+ _files folders): main report, saved copy
  - lung_report_2024.pdf: Malila et al. 2024, "Keuhkosyöpä Suomessa" (2018–2022), backup source
  - strategy_2026_2035_fi.pdf (64 pp): Kansallinen syöpästrategia 2026–2035; printed p. = PDF p.
  - roadmap_2026_2031_fi.pdf (111 pp): Toimeenpanon tiekartta 2026–2031; printed p. = PDF p.
  - filha_lung_programme_2026_fi.pdf (38 pp): Valtakunnallinen keuhkosyöpäohjelma 2026–2035
    (Filha ry, 18.5.2026 preprint). Printed p. = PDF p. − 9 (PDF pp.1–9 unnumbered). Cite printed pages.
  - source_list_fi.pdf: challenge link list
  - No English strategy (optional, not downloaded). No background pack exists: the challenge's
    "background pack" link is the Finnish strategy.
- Policy citations (verified, quotes in docs/source_verification.md):
  - Strategy p.33: no national system for cancer recommendations/pathways or their monitoring.
  - Strategy p.5: indicator "Potilaat pääsevät hoitoon tavoiteaikojen puitteissa", footnote
    THL Ohjaus 21/2016 (the roadmap does not cite 21/2016).
  - Roadmap 3.1.2 pp.56–57: national pathways, Nordic model (p.56); five (unnamed) cancers with
    access times by 2026–2028 (p.57).
  - Roadmap 1.2.3 p.32: named-worker care coordination model (care phase not specified).
  - Roadmap 2.5.2 pp.52–53: standardised referral criteria, symptom-based models by 2026–2028.
  - Roadmap 3.2.1 pp.59–60: national cancer quality registry (indicator incl. stage, 90% coverage).
  - Filha p.1 action plan, not a treatment recommendation; p.4 no national timing guidance
    (common diagnostic guidelines exist); pp.16, 24 diagnostics recommendation with primary-care
    referral criteria and recommended time limits, before the 2030 mid-term evaluation; p.21 no
    cancer quality registry; p.18 Table 2 lists "Hoitoonpääsy" as an (undefined) indicator.
- Claim statuses: "verified locally", "verified by Hellu, read 14 Nov", "preliminary"
  (MOT delays), "mentor insight (name)".
- Claim ledger: data/ledger.sqlite (committed, derived), table `claims`. Rebuild with
  `uv run python src/load_claims.py`, then `uv run python src/check_claims.py` (must pass before
  any commit that touches docs or data). Quotes are located automatically in the local sources
  (src/sources.py: whitespace/hyphen-insensitive; PDF pages, columns and table cells). Quotes in
  docs must be verbatim, including inflection and case. Methods: computed / digitised / quoted /
  mentor / assessed; statuses: verified locally / verified by Hellu / preliminary / mentor insight /
  draft / superseded (contradicted by verification; notes name the replacing claims).
- Quote convention in docs/source_verification.md, docs/recommendations.md, docs/blind_spots.md
  (and src/build_blind_spots.py via fi()/en()): a source quote is <q lang="fi">…</q> or
  <q lang="en">…</q>. English quotes are quotes of Hellu's brief and must match a BRIEF_CLAIMS entry
  in src/load_claims.py. Straight "…" quotes are not allowed in these docs (check fails); use ‘…’
  for prose. Briefs may cite only: verified locally, verified by Hellu, preliminary, mentor insight.
- Gemini pipeline (src/gemini.py saves every raw request/response to data/processed/gemini_raw/):
  src/brief.py (MODEL_REASON, thinking HIGH; headline + details per section; claim IDs per sentence)
  -> src/validate_brief.py (hard) + src/review_brief.py code rules (hard: overclaiming words, future
  tense about plans) -> one retry -> DRAFT if still failing; then MODEL_EXTRACT review flags (soft,
  human review only) in outputs/briefs/<county>.review.json. Briefs: outputs/briefs/<county>.json/.md.
- Validation also requires: "crude" in any sentence citing a cty: share; "recommend…" in any sentence
  citing our recommendations (rec:1–3, status "recommendation (ours)", method "proposed", sourced to
  docs/recommendations.md). Code rule: never "occupational health … excluded" (the report does not
  mention it). Review settings: temperature 0, fixed seed, model default thinking (MINIMAL is not
  supported; LOW was not more repeatable). Review output is repeatable in which sentences are flagged,
  not in severity/wording.
- More validation rules: two or more county treatment shares in a sentence require "overlap"; "recording
  looks (relatively) complete" only if the county's no-record vs_national is "below" (95% CI entirely
  below national). Plan claims carry "plan: <document, measure, page, dates>" notes (roadmap vs Filha);
  Filha's diagnostics recommendation is "carried out before the 2030 mid-term evaluation" (Finnish
  'toteutetaan' may mean produced or implemented; never say completed/implemented). The ~20% claim is
  "diagnosed on clinical findings alone (e.g. imaging), not by tissue or cell sample".
- All counties: `uv run python src/generate_all.py` -> outputs/briefs/summary.{json,md};
  `src/compare_flags.py before.json after.json` -> flags_before_after.md (keyword causes).
- PIPELINE FROZEN (14 Nov, after run 3): no more prompt or validation-rule changes unless something
  is wrong. Final run: 22/22 validated; 24 review flags (0 high). History:
  outputs/briefs/flags_before_after.md (runs 1–3).
- App branding: assets/logo.svg, used as the favicon (set_page_config; SVG accepted inside a running
  app) and next to the "Lingonberry" name in the header row. No st.logo, no sidebar. The core message
  (Brief tab, "National context" strip) is defined with its backing claims in src/core_message.py;
  check_claims.py fails if any part is not backed by citable claims.
- App layout (src/app.py):
  - Header row (st.columns): logo + name, Region selectbox (key "region", Finnish A–Ö order), and a
    brief-status st.popover ("Validated brief" / "Draft brief": model, date, attempts, review result,
    Regenerate button). Footer: data source + "Public aggregate data only".
  - Tabs: Brief · Compare regions · Pathway · How we verified this. Stateful (st.tabs key "nav",
    on_change="rerun"): a button switches tabs by setting st.session_state["nav"] in its callback.
  - Brief: verdict hero (from curative vs_national) + region-vs-Finland bar card; "National context"
    strip; three sections as st.expander (first open), details and claim pills behind st.toggle;
    "Read before acting" limitations + glossary. Review flags render only when there are any.
  - Compare regions: ranked dot plot (HTML rows, Wilson CIs), st.segmented_control Curative / No
    treatment record, "clearly differ" toggle (ci_contains_national), all-measures table in an expander.
  - Pathway: computed measured/partly/not-measured count, stage buttons per MOT interval, one evidence
    panel (selected stage in st.session_state["path-stage"]), Finland/Sweden/Denmark chart (preliminary).
  - How we verified this: three check cards, claims-by-method bar, "Technical details" expander.
  - Styling: theme colours in .streamlit/config.toml; all custom CSS in inject_css(). Cards are
    containers keyed "card-…" (white) or "soft-…" (warm panel). Expanders cannot nest: use st.toggle
    for show/hide inside one.
  - Needs Streamlit ≥ 1.56 (tested 1.56–1.67 with AppTest; 1.55 lacks segmented_control(required=),
    ≤1.54 lacks popover(key=)). requirements.txt pins 1.67.0.
- Design history: after Junction 2026 ended, a Google DeepMind mentor said the UI should make it easier to see
  where to start and where to go next; the layout redesign responded (README "Design history"). Docs only.
- Deployment (Streamlit Community Cloud, main file src/app.py): view-only without secrets; the
  Regenerate button (in the header popover) is disabled, with a view-only note, unless GEMINI_API_KEY,
  MODEL_REASON and MODEL_EXTRACT are set (.env or st.secrets). Without data/raw/ the app shows
  outputs/verification_snapshot.json: refresh it with
  src/write_verification_snapshot.py on a clean tree after committing, then commit it.
  requirements.txt = `uv export --no-hashes --format requirements-txt --no-emit-project`.
- README.md: the verification block is generated by `uv run python src/build_readme.py` (claim counts by
  status, briefs valid, review flags, snapshot date); never type those numbers. Every other number in
  README prose needs a `<!-- claims: id … -->` marker on its line and must be in those claims (pages,
  Kuva/Taulukko, measure ids too). The Run it, Deploy and Data sources sections and fenced code are
  skipped; non-finding numbers are in EXEMPT in the script.
  Terminology: README line under the pitch "22 regions: the 21 wellbeing services counties and the City
  of Helsinki", then "22 regions" / "every region" / "regional briefs"; "county" only next to a named
  county. App UI labels and the core message use "region" too (picker "Region"); the generated briefs
  and ledger claim texts still say "county" (not regenerated). build_readme.py fails on generic "county"/"counties" and on any
  "N regions" / "N wellbeing services counties" that differs from counties.FULL (22 / 21). `--check` must pass before committing README, docs or data changes. VIDEO_URL is a placeholder.
- App: `uv run streamlit run src/app.py` (serves saved briefs; "Regenerate with Gemini" runs the
  pipeline live). Smoke test: streamlit.testing.v1.AppTest on src/app.py.
- docs/:
  - definitions.md: report table 11 definitions, denominators, overlap, suppression (quotes)
  - chart_data.md: what data sits behind each report figure (PNG vs Plotly JSON)
  - source_verification.md: strategy, roadmap and Filha quotes with page numbers
  - pathway_brief.md: Hellu's background brief (regional pathways, MOT delays, law)
  - blind_spots.md: pathway stage x measured / MOT / regions / policy (built by
    src/build_blind_spots.py; edit the script, not the .md)
  - recommendations.md: three draft recommendations with evidence status (DRAFT)
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
- src/add_ci.py: adds MDT n = 0 rows ("0 records reported") and Wilson 95% CIs (ci_low,
  ci_high), national_share, ci_contains_national, vs_national (below / above / not distinguishable).
- src/plot_scatter.py -> outputs/curative_vs_missing.png (static chart; not used by the app).
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