# junction26-lingonberry-equal-care
Junction 2026, Team Lingonberry: a cancer care pathway gap brief for each Finnish wellbeing services county, built on public data with every claim traced to its source. Work in progress.

## Run it

Requires Python 3.12 and [uv](https://docs.astral.sh/uv/).

```
uv sync
uv run streamlit run src/app.py
```

The app opens in your browser. It serves the saved briefs in `outputs/briefs/` and the claim ledger
`data/ledger.sqlite`, both in the repo, so **viewing needs no API key**.

To regenerate briefs (the app's **Regenerate with Gemini** button, or the commands below), create a `.env`
file in the repo root. It is gitignored; never commit it.

```
GEMINI_API_KEY=your-key
MODEL_REASON=gemini-4-argon      # writes the briefs
MODEL_EXTRACT=gemini-4-hydrogen  # translates quotes and reviews briefs
```

Pipeline commands, from the repo root:

```
uv run python src/load_claims.py          # rebuild the claim ledger from data and docs
uv run python src/check_claims.py         # verify the ledger (must pass)
uv run python src/translate_quotes.py     # English translations of Finnish quotes (Gemini)
uv run python src/brief.py Kymenlaakso    # one county: brief + validation + review (Gemini)
uv run python src/generate_all.py         # all 22 counties, with a summary in outputs/briefs/summary.md
```

The raw files in `data/raw/` are not in the repo; see [Data](#data) for where to download them. They are
needed to rebuild the ledger and to check quotes, but not to run the app.

## How verification works

Every number and quote in a brief is a row in the **claim ledger** (`data/ledger.sqlite`). Each row has
its source document, location (table, figure, page or section), method and status.

- **Numbers are computed in our code, never by a model.** County shares come from the Cancer Registry
  report's tables, with Wilson 95% confidence intervals from the published counts. Age-adjusted values
  are read off a report figure by code (about ±0.5 percentage points).
- **Quotes are checked verbatim.** `check_claims.py` re-finds every quote in its source PDF or page at the
  stated location, ignoring only line breaks and hyphenation. Quotes in the docs must carry an explicit
  language (`<q lang="fi">`). An unmarked quote, a quote with no language, or a quote that can't be found
  fails the check.
- **Every claim has a status:** verified locally, verified by a teammate, preliminary, mentor insight, our
  recommendation, draft, or superseded (contradicted by a verified source, with a pointer to the
  replacement). Briefs may not cite draft or superseded claims.
- **The model writes, code checks.** Gemini writes each brief only from the claims it is given, and every
  sentence lists the claim IDs it relies on. `validate_brief.py` rejects a sentence with:
  - no claim ID, or an ID that does not exist or may not be cited;
  - a number that is not in its cited claims;
  - a county share not called crude;
  - preliminary figures, mentor views or our recommendations not labelled as such.

  `review_brief.py` rejects overclaiming words and future tense about planned measures. A failing brief
  gets one retry with the list of problems; if it still fails, it is saved as **DRAFT**.
- **A second model reviews; people decide.** Gemini Hydrogen reads each sentence against its cited claims
  and flags possible overreach or missing caveats. Flags are for human review only and never approve or
  change a brief.
- **Everything is on disk.** Every raw model request and response is in `data/processed/gemini_raw/`.

Public aggregate data only. No patient-level data is used anywhere.

## Data

Public aggregate sources only; no patient-level data. Raw files live in `data/raw/`, which is
gitignored. Download them from the URLs below and save them under the names shown.

| Local file (`data/raw/`) | What it is | Source URL |
|---|---|---|
| `keuhkosyoparaportti_2019_2023.html` | Keuhkosyöpä Suomessa 2019–2023, Finnish Cancer Registry: main data source. Saved from the browser, because the live page returns 403 to scripts | https://syoparekisteri.fi/assets/themes/ssy3/factsheets/keuhkosyoparaportti.html |
| `lung_report_2024.pdf` | Malila et al. 2024, Keuhkosyöpä Suomessa (2018–2022): backup source | https://syoparekisteri.fi/assets/files/2024/12/Keuhkosyopa_Suomessa.pdf |
| `strategy_2026_2035_fi.pdf` | Kansallinen syöpästrategia 2026–2035 (STM), Finnish | https://stm.fi/documents/1271139/1329769/Kansallinen_syopastrategia_2026_2035_FINAL.pdf/05ad3c9d-d8ba-a629-3e90-e8d10f4f5bbc?t=1767863923329 <br>Challenge copy: https://files.hackjunction.app/resources/Kansallinen_syopastrategia_2026_2035_FINAL.pdf |
| `roadmap_2026_2031_fi.pdf` | Kansallinen syöpästrategia 2026–2035: Toimeenpanon tiekartta 2026–2031 (STM), Finnish | https://stm.fi/documents/1271139/1359637/Kansallinen_syopastrategia_toimeenpanon_tiekartta_2026_2031.pdf/6e826620-351e-d6b4-5096-4706357adc45?t=1790152929568 <br>Challenge copy: https://files.hackjunction.app/resources/Kansallinen_syopastrategia_toimeenpanon_tiekartta_2026_2031.pdf |
| `source_list_fi.pdf` | "Syöpästrategiat ja syöpädata – linkkikokoelma": the challenge's link list | https://files.hackjunction.app/resources/Sy%C3%B6p%C3%A4strategiat%20ja%20sy%C3%B6p%C3%A4data_linkkikokoelma.pdf |
| `filha_lung_programme_2026_fi.pdf` | Valtakunnallinen keuhkosyöpäohjelma 2026–2035 (Filha ry, working group 18.5.2026, preprint) | https://www.filha.fi/wp-content/uploads/2026/05/Valtakunnallinen-keuhkosyopaohjelma-2026-2035_180526_preprint.pdf |
| `strategy_2026_2035_en.pdf` | National Cancer Strategy 2026–2035, English version: reading aid only; cite the Finnish original. **Optional, not downloaded** | https://www.iccp-portal.org/sites/default/files/2026-02/National_Cancer_Strategy_2026-2035_Finland.pdf |

**There is no separate background pack.** The challenge page's "background pack" link points to the
Finnish strategy itself (`strategy_2026_2035_fi.pdf`).

The Finnish strategy and roadmap are listed with both their official STM link and the copy the
challenge supplied. Verified quotes and page numbers: `docs/source_verification.md`.
