# junction26-lingonberry-equal-care
Junction 2026, Team Lingonberry: a cancer care pathway gap brief for each Finnish wellbeing services county, built on public data with every claim traced to its source. Work in progress.

## Run the app

```
uv sync
uv run streamlit run src/app.py
```

The app shows the saved, validated briefs in `outputs/briefs/` and every claim behind them
(`data/ledger.sqlite`). It needs no API key for this. **Regenerate with Gemini** runs the live
pipeline and needs `GEMINI_API_KEY`, `MODEL_REASON` and `MODEL_EXTRACT` in `.env`.

Pipeline, from the repo root:

```
uv run python src/load_claims.py          # rebuild the claim ledger
uv run python src/check_claims.py         # every claim sourced, every quote re-found verbatim
uv run python src/translate_quotes.py     # English translations of Finnish quotes (Gemini)
uv run python src/brief.py Kymenlaakso    # brief + validation + review (Gemini)
```

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
