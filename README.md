# <img src="assets/logo.svg" alt="" height="36"> Lingonberry

**Make the wait visible: a lung cancer pathway brief for every region in Finland.**

22 regions: the 21 wellbeing services counties and the City of Helsinki.

[**Live app**](https://junction26-lingonberry-equal-care-jvssmnbotqefgpxeiyfwjt.streamlit.app/) ·
[**2-minute video**](VIDEO_URL) ·
Junction 2026, AstraZeneca challenge *Equal Care Across Finland*; also entered in Google DeepMind's
*Best Use of Gemini API*.

> **In short**
> - **Problem:** Finland's cancer strategy sets a target for timely access to treatment, but the national lung cancer report publishes no access times for any region. <!-- claims: q:168b4b3443 q:24169121a4 bs:coverage:Referral bs:coverage:First_specialist_visit bs:coverage:Treatment_start -->
> - **What it does:** a brief for each of the 22 regions (where we lag, how sure we are, what to do first), with every sentence linked to its source and the original Finnish quote.
> - **Findings:** Kymenlaakso's crude curative share is 19.3% against 27.0% nationally, with recording that looks relatively complete: likely a real gap. Varsinais-Suomi has the highest share with no treatment record, 43.1% against 27.5%: a care gap or a recording gap? <!-- claims: cty:curative:Kymenlaakson_hyvinvointialue nat:curative cty:no_treatment_record:Kymenlaakson_hyvinvointialue cty:no_treatment_record:Varsinais_Suomen_hyvinvointialue nat:no_treatment_record -->
> - **Gemini:** Argon writes each brief only from ledger claims, code checks IDs, numbers and wording, and Hydrogen flags possible overclaims for human review and translates the Finnish quotes. Gemini writes, the ledger decides.
> - **Try it:** [live app](https://junction26-lingonberry-equal-care-jvssmnbotqefgpxeiyfwjt.streamlit.app/), view-only, no API key needed.

![The Kymenlaakso brief in the app: a header row with the Region picker and the validated-brief status, a verdict headline with a region-versus-Finland chart, the national context, the three brief questions as collapsible sections with their sources behind toggles, and a Read before acting panel](assets/screenshot.png)

## The problem

Finland's cancer strategy sets a target for timely access to treatment: its indicator *Potilaat pääsevät hoitoon tavoiteaikojen puitteissa* (patients access treatment within the target times) is footnoted to THL's access-time definitions, Ohjaus 21/2016 (strategy p.5). <!-- claims: q:168b4b3443 q:24169121a4 -->
Yet the national lung cancer report publishes no access times for any region. <!-- claims: bs:coverage:Referral bs:coverage:First_specialist_visit bs:coverage:Treatment_start -->
No step of the pathway is timed in public data: the report says whether a specialist visit or a treatment happened within 12 months of diagnosis, never how long it took. <!-- claims: bs:coverage:Symptoms bs:coverage:Referral bs:coverage:First_specialist_visit bs:coverage:Treatment_start -->

## What it does

For every region, a one-page brief answers three questions:

- **Where do we lag?** Regional treatment shares against the national figure, with 95% confidence intervals.
- **How sure are we?** What the data can and cannot show: crude shares, recording gaps, unmeasured stages.
- **What to do first?** Our recommendations, tied to measures already in the national plans.

Every sentence links to its ledger claims: source, location, and the original Finnish quote with an
English translation. The app also has a **chart** (curative treatment against *no treatment record*), a
**pathway view** (which stages public data measures, from symptoms to treatment start) and a **How we
verified this** tab.

## Key findings

Shares are crude (not adjusted for age or stage), from the Finnish Cancer Registry's report for 2019–2023 (Taulukko 11), with Wilson 95% confidence intervals computed in our code. <!-- claims: cty:curative:Kymenlaakson_hyvinvointialue -->

**Kymenlaakso: likely a real gap in curative treatment.**

- Curative treatment 19.3% (95% CI 16.3–22.7) against 27.0% nationally: below. <!-- claims: cty:curative:Kymenlaakson_hyvinvointialue nat:curative -->
- Recording looks relatively complete: *no treatment record within 12 months* is 16.4% (13.7–19.6), the lowest of any region, against 27.5% nationally. <!-- claims: cty:no_treatment_record:Kymenlaakson_hyvinvointialue nat:no_treatment_record -->
- Age-adjusted (Kuva 16, read off the figure to ±0.5 pp): men 17.9% (13.9–22.9) against 26.7%, below; women 22.6% (16.8–29.3) against 26.9%, lower but the interval includes the national line. <!-- claims: k16:curative:men:Kymenlaakson_hyvinvointialue k16:curative:men:national k16:curative:women:Kymenlaakson_hyvinvointialue k16:curative:women:national -->

**Varsinais-Suomi: a care gap or a recording gap?**

- *No treatment record* is 43.1% (40.5–45.6), the highest of any region, against 27.5% nationally. <!-- claims: cty:no_treatment_record:Varsinais_Suomen_hyvinvointialue nat:no_treatment_record -->
- Life-prolonging treatment is only 9.7% (8.3–11.4) against 30.4% nationally. Together, this suggests drug treatment is not being recorded (our interpretation). <!-- claims: cty:life_prolonging:Varsinais_Suomen_hyvinvointialue nat:life_prolonging -->
- Crude curative treatment, 24.3% (22.1–26.6), is below the national 27.0%; age-adjusted, women are at 27.4% (23.1–31.8) against 26.9%, not below. <!-- claims: cty:curative:Varsinais_Suomen_hyvinvointialue nat:curative k16:curative:women:Varsinais_Suomen_hyvinvointialue k16:curative:women:national -->

## Our recommendations

These are **the team's own draft recommendations**, not yet reviewed by mentors
([docs/recommendations.md](docs/recommendations.md)). Each builds on a measure already in the national
cancer strategy, its implementation roadmap, or Filha's national lung cancer programme.

**1. Every region reports lung cancer access times using THL's definitions (Ohjaus 21/2016), with alerts for stalled handovers.** Builds on the strategy's access-time indicator (p.5); roadmap measure 3.1.2, cancer-specific access times for five (unnamed) cancers by 2026–2028 (p.57); and Filha's diagnostics recommendation with recommended time limits, to be carried out before the 2030 mid-term evaluation (pp.16, 24). <!-- claims: rec:1 q:24169121a4 q:def306014c q:8f358a9de6 q:614febebf2 -->

**2. A referral template modelled on KYS, a persistent-symptoms rule (refer if symptoms continue after a normal X-ray) and a named contact for the diagnostic phase.** Builds on roadmap measure 2.5.2, standardised referral criteria for at least the five most common cancers by 2026–2028 (pp.52–53); measure 1.2.3, guidance on a named care coordinator by 2026–2028, adopted regionally by 2029–2031 (p.32); and Filha's primary-care referral criteria (p.16). <!-- claims: rec:2 q:9a1cd194f5 q:c61439b30f q:abcbb06ae3 q:29b792498e -->

**3. Publish recording completeness per region for stage, drug treatment and MDT meetings, and read regional gaps in these fields as data-quality signals first.** Builds on roadmap measure 3.1.2, national pathways that define recording and coding practices (p.56); measure 3.2.1, a national cancer quality registry whose data, including stage, is to reach 90% coverage (p.60); and Filha's statement that Finland has no cancer quality registry (p.21). <!-- claims: rec:3 q:990a0d39a0 q:ed87906241 q:4a856bd695 q:47c7e11303 -->

## How Gemini is used

**Gemini writes, the ledger decides.**

- **Argon writes** (`gemini-4-argon`, thinking high). It gets only the ledger claims for one region and
  returns structured sentences, each with the claim IDs it relies on. It computes nothing: every figure
  comes from our own Python code.
- **Code validates** (`validate_brief.py`, `review_brief.py`). A sentence fails if a claim ID is missing
  or not citable, a number is not in its cited claims, a regional share is not called crude, a preliminary
  figure, mentor view or our recommendation is unlabelled, or it overclaims. A failing brief gets one
  retry with the list of problems, then is saved as **DRAFT**.
- **Hydrogen reviews and translates** (`gemini-4-hydrogen`). It reads each sentence against its cited
  claims and flags possible overclaims or missing caveats. Flags are for human review only and never
  approve or change a brief. It also translates the Finnish quotes into English; code checks that every
  number in a quote survives translation.
- **Everything is on disk.** Every raw request and response is in `data/processed/gemini_raw/`.

## How verification works

**In numbers**, written from the ledger and the saved briefs by `src/build_readme.py`:

<!-- generated by src/build_readme.py: do not edit by hand -->

| Claim status | Claims |
|---|---|
| verified locally | 227 |
| verified by Hellu | 17 |
| preliminary | 6 |
| mentor insight | 2 |
| recommendation (ours) | 3 |
| draft | 4 |
| superseded | 2 |
| **Total** | **261** (255 citable in a brief) |

- **101** claims carry a source quote that `check_claims.py` re-finds in its source document.
- **22/22** saved regional briefs pass `validate_brief.py` against the committed ledger.
- **24** sentences flagged by the Hydrogen review for human reading (0 high, 11 medium, 13 low).
- Last full local verification, with all sources present: **14 Nov 2026**, commit `f3d0152`,
  `check_claims.py` passed
  (the committed ledger is the file verified then).

<!-- end generated -->

Every number and quote in a brief is a row in the **claim ledger** (`data/ledger.sqlite`), with its source
document, location (table, figure, page or section), method and status.

- **Numbers are computed in our code, never by a model.** Regional shares and Wilson 95% confidence
  intervals come from the report's published counts; age-adjusted values are read off a report figure
  by code.
- **Quotes are checked verbatim.** `check_claims.py` re-finds every quote in its source PDF or page at the
  stated location, ignoring only line breaks and hyphenation, and fails on any quote it cannot find.
- **Every claim has a status.** *Verified by Hellu* means a teammate read the source in full; *superseded*
  means a verified source contradicted it, and it points to the replacement. Briefs may not cite draft
  or superseded claims.
- **This README is checked too.** `src/build_readme.py` writes the numbers above from the ledger and fails
  if any other number here is not in the ledger claims it cites.

## Limitations

- **Crude shares.** Regional shares are not adjusted for age or stage, and stage at diagnosis is missing for about half of patients. A low curative share is not proof of worse care. <!-- claims: fig:age_adjusted_only_kuva16 bs:coverage:Diagnosis -->
- **Categories overlap.** A patient can have several treatment types, so the shares are not a breakdown and do not add up. <!-- claims: cty:curative:Kymenlaakson_hyvinvointialue -->
- **No treatment record is not "untreated".** It mixes patients who were not treated with treatment that was given but not recorded. <!-- claims: bs:coverage:Treatment_start -->
- **Age adjustment** exists only in Kuva 16, a PNG figure. We read its curative values for three regions (Kymenlaakso, Etelä-Karjala, Varsinais-Suomi), to ±0.5 pp. <!-- claims: fig:age_adjusted_only_kuva16 k16:curative:men:national -->
- **The 155-day figure is preliminary.** Symptoms to first treatment: 155 days in Finland, 107 in Sweden, 67 in Denmark, from an unpublished study reported by Yle MOT (2025). These are national averages, not regional figures. <!-- claims: mot:total_fi mot:total_se mot:total_dk -->
- **MDT coding measures recording practice, not care.** Specialist-care procedures reach the hospital register only from direct patient contacts, so a region with no coded MDT meetings may still hold them. <!-- claims: bs:coverage:MDT -->
- **Mentor insights** are expert views without a written source, and are labelled as such wherever they are used.

## Repo layout

```
src/app.py            Streamlit app (main file for deployment)
src/                  data scripts, claim ledger, Gemini pipeline, checks
data/ledger.sqlite    claim ledger (committed; rebuilt by src/load_claims.py)
data/processed/       tables from the report, CIs, digitised figure values, raw Gemini calls
data/raw/             source documents (not in the repo; see Data sources)
docs/                 definitions, source quotes, blind spots, recommendations, Hellu's brief
outputs/briefs/       saved briefs, review flags and summary for every region
```

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
uv run python src/brief.py Kymenlaakso    # one region: brief + validation + review (Gemini)
uv run python src/generate_all.py         # all 22 regions, with a summary in outputs/briefs/summary.md
uv run python src/build_readme.py         # refresh and check the numbers in this README
```

The raw files in `data/raw/` are not in the repo; see [Data sources](#data-sources) for where to download
them. They are needed to rebuild the ledger and to check quotes, but not to run the app.

### Deploy on Streamlit Community Cloud

- Repository: this repo, branch `main`. **Main file path: `src/app.py`**. Python 3.12.
- Dependencies: `uv.lock` (`requirements.txt` is an export of it: `uv export --no-hashes --no-emit-project`).
- No secrets are needed: the deployed app is view-only. To enable **Regenerate with Gemini**, add
  `GEMINI_API_KEY`, `MODEL_REASON` and `MODEL_EXTRACT` under the app's *Secrets*. The button only
  appears when all three are set.
- Without `data/raw/`, *How we verified this* shows the last local verification from
  `outputs/verification_snapshot.json`, with its time, the commit it describes, and whether the deployed
  ledger is the file that was verified. The check of each regional brief still re-runs live against the
  committed ledger.

After changing data, docs or briefs, refresh the snapshot. Commit first, so the snapshot's commit hash
describes exactly what was verified; then commit the snapshot.

```
uv run python src/write_verification_snapshot.py
```

## Data sources

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

## Design history

After Junction 2026 had ended, a Google DeepMind mentor gave feedback on the project. They said it was
done well and well integrated with Gemini, and that to improve its chances of winning, the UI should be
easier to understand: people should be able to see where to start and where to go next.

We redesigned the app's layout in response. The data, the claim ledger, validation and the Gemini
pipeline did not change. What changed:

- A header row with the Region picker and a validation popover, replacing the sidebar.
- A verdict headline and a region-versus-Finland chart at the top of the Brief.
- Brief sections collapsed, so only the first is open.
- Evidence behind toggles: claim sources, detail sentences and the full list of limitations.
- A ranked dot plot for comparing regions.
- A pathway view with one evidence panel for the selected step.
- A simpler verification tab: three check cards, with the technical details in an expander.
- Start-here and next-step cues: a line under the header and a link to the next tab at the bottom of
  each tab.

## Licence and team

Code: [MIT](LICENSE).

- **Shah**: team lead, data and AI.
- **Hellu**: service design, 20+ years in Finnish healthcare.
