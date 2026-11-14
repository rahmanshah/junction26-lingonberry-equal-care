"""Fill data/ledger.sqlite from our derived data and verified documents.

Sources loaded:
  1. data/processed/county_treatment.csv     county/area shares + Wilson CIs   (computed)
     + national shares from Taulukko 5/6                                       (computed)
  2. data/processed/kuva16_curative_digitised.csv  age-adjusted curative        (digitised)
  3. data/processed/blind_spots.csv          coverage per pathway stage         (assessed)
     + the <q> quotes in its report_note, regional and policy columns
  4. docs/source_verification.md, docs/recommendations.md: every <q> quote
  5. docs/pathway_brief.md: BRIEF_CLAIMS below (MOT delays, regional pathways, law, mentor input,
     superseded statements), each with a verbatim English quote from the brief

Quote language is never guessed. In docs, a source quote is written <q lang="fi">…</q> or
<q lang="en">…</q>; in code, the lang is given explicitly. A <q> without a valid lang is loaded with
quote_lang = NULL and src/check_claims.py fails on it. Straight "…" quotes are not allowed in the
scanned docs at all (check_claims.py fails on them), so nothing is skipped silently.

English <q> quotes in docs refer to Hellu's brief. Each must be contained in a BRIEF_CLAIMS quote;
it is then attached to that claim (and takes its status). An unmatched English quote becomes a
'draft' claim that check_claims.py rejects.

Quote locations are not typed by hand: each quote is searched in the local source texts
(src/sources.py) and its location is every page/section where it is found.
Translations of Finnish quotes come from data/processed/quote_translations.csv
(src/translate_quotes.py) and are stored in quote_en, next to the quote.
Run src/check_claims.py afterwards.
"""
import hashlib
import re
import sys
from collections import Counter
from pathlib import Path

import pandas as pd

import ledger
import sources

REPORT = "data/raw/keuhkosyoparaportti_2019_2023.html"
STRATEGY = "data/raw/strategy_2026_2035_fi.pdf"
ROADMAP = "data/raw/roadmap_2026_2031_fi.pdf"
FILHA = "data/raw/filha_lung_programme_2026_fi.pdf"
BRIEF = "docs/pathway_brief.md"
T5 = Path("data/processed/factsheet/table_04.csv")  # report Taulukko 5
T6 = Path("data/processed/factsheet/table_05.csv")  # report Taulukko 6
TRANSLATIONS = Path("data/processed/quote_translations.csv")
QUOTE_DOCS = ("docs/source_verification.md", "docs/recommendations.md")

TREATMENT = {  # Finnish category -> (metric slug, English label)
    "Parantava": ("curative", "curative treatment"),
    "Jarruttava": ("life_prolonging", "life-prolonging treatment"),
    "Oireenmukainen": ("symptomatic", "symptomatic treatment"),
    "Ei hoitotietoa": ("no_treatment_record", "no treatment record within 12 months"),
    "MDT-käsittely": ("mdt_recorded", "MDT meeting recorded"),
}
# <q lang="xx">body</q>; any other attribute form leaves lang = None (and fails the check).
Q_TAG = re.compile(r'<q(?P<attrs>[^>]*)>(?P<body>.*?)</q>', re.S)
LANG_ATTR = re.compile(r'^\s+lang="(?P<lang>[a-z]{2})"\s*$')


def short(county: str) -> str:
    return re.sub(r"\W+", "_", county).strip("_")


def quote_key(quote: str) -> str:
    """Stable key for a quote's text ("…ole." and "…ole" are the same quote)."""
    return hashlib.sha1(sources.normalise(quote).rstrip(".,;:").encode("utf-8")).hexdigest()[:10]


def qid(src: str, quote: str) -> str:
    return "q:" + hashlib.sha1((src + sources.normalise(quote).rstrip(".,;:")).encode("utf-8")).hexdigest()[:10]


def strip_md(text: str) -> str:
    text = Q_TAG.sub(lambda m: f"“{m.group('body')}”", text)
    return re.sub(r"[*`]", "", text).strip()


def clean_quote(body: str) -> str:
    """Quote text without Markdown blockquote markers and line breaks."""
    return re.sub(r"\s*\n\s*>?\s*", " ", body).strip()


def tag_lang(attrs: str) -> str | None:
    m = LANG_ATTR.match(attrs)
    return m.group("lang") if m and m.group("lang") in ledger.QUOTE_LANGS else None


# ---------------------------------------------------------------- 1. county shares (computed)
def county_claims() -> list[dict]:
    df = pd.read_csv("data/processed/county_treatment.csv")
    rows = []
    for r in df.itertuples():
        slug, label = TREATMENT[r.treatment]
        level = "area subtotal" if r.level == "area" else "county"
        ci = f"95% CI {r.ci_low:.1f}–{r.ci_high:.1f}"
        text = (f"{r.county}: {label} {r.share:.1f}% ({ci}; n={int(r.n)}/{int(r.total)}), "
                f"{r.vs_national} vs national {r.national_share:.1f}%")
        notes = (f"level={level}; n={int(r.n)}; total={int(r.total)}; ci_low={r.ci_low}; "
                 f"ci_high={r.ci_high}; national_share={r.national_share}; vs_national={r.vs_national}; "
                 "share = n/total as printed; Wilson 95% CI computed by src/add_ci.py; crude, not "
                 "age- or stage-adjusted; categories overlap")
        if isinstance(r.note, str) and r.note:
            notes += f"; {r.note} (county absent from the report's MDT rows; area subtotal proves zero)"
        rows.append({
            "id": f"cty:{slug}:{short(r.county)}", "claim_text": text, "value": r.share, "unit": "%",
            "county": r.county, "metric": f"share_{slug}", "source_doc": REPORT,
            "location": "Taulukko 11" + (" (area subtotal)" if r.level == "area" else ""),
            "method": "computed", "status": "verified locally", "notes": notes,
        })
    return rows


def national_claims() -> list[dict]:
    t5 = pd.read_csv(T5, header=[0, 1])
    t6 = pd.read_csv(T6, header=[0, 1])
    tot5 = t5[t5[t5.columns[0]].astype(str).str.strip() == "Yhteensä"].iloc[0]
    tot6 = t6[t6[t6.columns[0]].astype(str).str.strip() == "Yhteensä"].iloc[0]
    n_all = int(tot6[("Potilaita yhteensä", "Lukumäärä")])
    counts = {
        "Parantava": (int(tot6[("Parantava hoito", "Lukumäärä")]), "Taulukko 6"),
        "Jarruttava": (int(tot6[("Jarruttava hoito", "Lukumäärä")]), "Taulukko 6"),
        "Oireenmukainen": (int(tot6[("Oireenmukainen hoito", "Lukumäärä")]), "Taulukko 6"),
        "Ei hoitotietoa": (n_all - int(tot5[("Keuhkosyöpä- toimenpide", "Lukumäärä")]), "Taulukko 5"),
        "MDT-käsittely": (int(tot5[("MDT-käsittely", "Lukumäärä")]), "Taulukko 5"),
    }
    rows = []
    for fi, (n, table) in counts.items():
        slug, label = TREATMENT[fi]
        share = round(n / n_all * 100, 4)  # 4 dp: 26.95 would print as 26.9; 26.9549 prints 27.0 as in the report
        how = ("all patients minus patients with any lung cancer procedure"
               if fi == "Ei hoitotietoa" else "count from the table's total row")
        rows.append({
            "id": f"nat:{slug}", "claim_text": f"Finland: {label} {share:.1f}% ({n}/{n_all}), 2019–2023",
            "value": share, "unit": "%", "county": None, "metric": f"share_{slug}", "source_doc": REPORT,
            "location": table, "method": "computed", "status": "verified locally",
            "notes": f"n={n}; total={n_all}; {how}; national benchmark for county comparisons",
        })
    return rows


# ---------------------------------------------------------------- 2. Kuva 16 (digitised)
def kuva16_claims() -> list[dict]:
    df = pd.read_csv("data/processed/kuva16_curative_digitised.csv")
    rows = []
    for r in df.itertuples():
        national = r.county.startswith("Koko maa")
        ci = (f" (95% CI {r.ci_low:.1f}–{r.ci_high:.1f})" if pd.notna(r.ci_low) else "")
        who = "Finland (national reference line)" if national else r.county
        rows.append({
            "id": f"k16:curative:{r.sex}:{'national' if national else short(r.county)}",
            "claim_text": f"{who}: age-adjusted curative treatment share, {r.sex}, {r.value:.1f}%{ci}",
            "value": r.value, "unit": "%", "county": None if national else r.county,
            "metric": f"age_adjusted_share_curative_{r.sex}", "source_doc": REPORT, "location": "Kuva 16",
            "method": "digitised", "status": "verified locally",
            "notes": "; ".join(x for x in (f"precision ±{r.precision_pp} pp", "src/digitise_kuva16.py",
                                           r.note if isinstance(r.note, str) else "") if x),
        })
    return rows


# ---------------------------------------------------------------- quotes (shared helpers)
DOC_KEYS = (("report", REPORT), ("taulukko", REPORT), ("strategy", STRATEGY),
            ("roadmap", ROADMAP), ("filha", FILHA))


def prefer_from(text: str, before: int | None = None) -> list[str]:
    """Sources named in a text. With `before`, only mentions before that position count, nearest
    first (the document a quote belongs to is usually named just before it); otherwise in order."""
    found = []
    for key, src in DOC_KEYS:
        for m in re.finditer(key, text, re.I):
            if before is None or m.start() < before:
                found.append((m.start(), src))
    found.sort(reverse=before is not None)
    out = []
    for _, s in found:
        if s not in out:
            out.append(s)
    return out


def quote_claim(quote: str, lang: str | None, claim_text: str, prefer: list[str], cited_in: str) -> dict:
    """A quoted claim from a document. Source and location are found by searching the local texts.
    English quotes are searched in Hellu's brief only (that is what they quote)."""
    order = [BRIEF] if lang == "en" else prefer + [s for s in sources.SOURCES if s not in prefer and s != BRIEF]
    src, labels = None, []
    for s in order:
        if Path(s).exists():
            labels = sources.find(s, quote)
            if labels:
                src = s
                break
    src_or_hint = src or (order[0] if order else None)
    return {
        "id": qid(src_or_hint or "?", quote), "claim_text": claim_text,
        "value": None, "unit": None, "county": None, "metric": None,
        "source_doc": src_or_hint, "location": "; ".join(labels) if labels else None,
        "quote": quote, "quote_lang": lang, "method": "quoted",
        # English quotes take their status from the brief claim they belong to (see attach_english)
        "status": "verified locally" if lang == "fi" else "draft",
        "notes": f"cited in {cited_in}" + ("" if src else "; NOT FOUND in any local source")
                 + ("" if lang else "; quote language missing: use <q lang=\"fi\"> or <q lang=\"en\">"),
    }


def q_tags_in(text: str) -> list[tuple[str, str | None, int, int]]:
    """(clean quote, lang, start, end) for every <q> tag in a text."""
    return [(clean_quote(m.group("body")), tag_lang(m.group("attrs")), m.start(), m.end())
            for m in Q_TAG.finditer(text)]


# ---------------------------------------------------------------- 3. blind spots
def blind_spot_claims() -> list[dict]:
    df = pd.read_csv("data/processed/blind_spots.csv").fillna("")
    rows = []
    for r in df.itertuples():
        loc = r.report_source if r.report_source != "none" else "whole report (no relevant data found)"
        rows.append({
            "id": f"bs:coverage:{short(r.stage)}",
            "claim_text": f"Pathway stage '{r.stage}' is measured in public data: {r.measured} "
                          f"(by county: {r.by_county})",
            "value": None, "unit": None, "county": None, "metric": "public_data_coverage",
            "source_doc": REPORT, "location": loc, "method": "assessed", "status": "verified locally",
            "notes": strip_md(r.report_note),
        })
        for column, what in (("report_note", "Report evidence"), ("regional_pathways", "Regional evidence"),
                             ("policy", "Policy evidence")):
            text = getattr(r, column)
            for q, lang, start, _ in q_tags_in(text):
                prefer = [REPORT] if column == "report_note" else prefer_from(text, before=start)
                rows.append(quote_claim(q, lang, f"{what} for pathway stage '{r.stage}'", prefer,
                                        f"data/processed/blind_spots.csv ({column})"))
    return rows


# ---------------------------------------------------------------- 4. quotes in the docs
def doc_quote_claims(path: str) -> list[dict]:
    text = Path(path).read_text(encoding="utf-8")
    rows = []
    for q, lang, start, end in q_tags_in(text):
        line_start = text.rfind("\n", 0, start) + 1
        line_end = text.find("\n", end)
        line = text[line_start:line_end if line_end != -1 else None]
        para_start = text.rfind("\n\n", 0, start) + 2 if text.rfind("\n\n", 0, start) != -1 else 0
        para_end = text.find("\n\n", end)
        para = text[para_start:para_end if para_end != -1 else None]
        headings = re.findall(r"^#+\s*(.+)$", text[:start], re.M)
        heading = headings[-1] if headings else ""

        if line.lstrip().startswith("|"):  # table row: first cell = point, second = source
            cells = [c.strip() for c in line.strip().strip("|").split("|")]
            claim_text = strip_md(cells[0])
            prefer = prefer_from(cells[1] if len(cells) > 1 else "") or prefer_from(heading)
        elif para.lstrip().startswith(">"):  # blockquote: translation is the next italic paragraph
            nxt = text[para_end + 2:].split("\n\n", 1)[0].strip() if para_end != -1 else ""
            claim_text = re.sub(r"\s+", " ", nxt.split("*")[1]) if nxt.startswith("*") else f"Quote under: {heading}"
            prev_end = para_start - 2
            prev = text[text.rfind("\n\n", 0, prev_end) + 2:prev_end] if prev_end > 0 else ""
            prefer = prefer_from(prev, before=len(prev)) + prefer_from(heading)
        else:  # running text: translation may follow as (*...*)
            tr = re.match(r"\s*\(\*([^*]+)\*\)", text[end:])
            claim_text = re.sub(r"\s+", " ", tr.group(1)) if tr else re.sub(r"\s+", " ", strip_md(para))[:300]
            prefer = prefer_from(para, before=start - para_start) + prefer_from(heading)
        rows.append(quote_claim(q, lang, claim_text, prefer, path))
    return rows


# ---------------------------------------------------------------- 5. Hellu's brief
# (id, claim_text, value, unit, metric, verbatim quote from the brief, method, status, notes)
# All quotes here are English (the brief is in English).
BRIEF_CLAIMS = [
    ("mot:total_fi", "Symptoms to first treatment, Finland: 155 days on average", 155, "days",
     "delay_symptoms_to_treatment",
     "On average, lung cancer takes 155 days from first symptoms to treatment in Finland, compared "
     "with 107 in Sweden and 67 in Denmark (preliminary data).", "quoted", "preliminary",
     "original: MOT 'Hitaasti syöpähoitoon' (Yle 2025), preliminary unpublished study; primary author unknown"),
    ("mot:total_se", "Symptoms to first treatment, Sweden: 107 days", 107, "days",
     "delay_symptoms_to_treatment_sweden", "compared with 107 in Sweden", "quoted", "preliminary",
     "original: Yle MOT 2025; primary author unknown"),
    ("mot:total_dk", "Symptoms to first treatment, Denmark: 67 days", 67, "days",
     "delay_symptoms_to_treatment_denmark", "and 67 in Denmark", "quoted", "preliminary",
     "original: Yle MOT 2025; primary author unknown"),
    ("mot:patient", "Patient delay (symptoms to first contact): 56 days", 56, "days", "delay_patient",
     "1. Patient delay (56 days)", "quoted", "preliminary",
     "original: Yle MOT 2025; blind-spot stage: Symptoms (mapping is our assumption)"),
    ("mot:primary", "Primary care interval: 41 days", 41, "days", "delay_primary_care",
     "2. Primary care (41 days)", "quoted", "preliminary",
     "original: Yle MOT 2025; blind-spot stages: Primary care, Imaging, Referral (our mapping)"),
    ("mot:specialist", "Specialist care interval: 58 days, the longest stage", 58, "days",
     "delay_specialist_care", "3. Specialist care (58 days, the longest stage)", "quoted", "preliminary",
     "original: Yle MOT 2025; blind-spot stages: First specialist visit to Treatment start (our mapping)"),
    ("reg:kys_template", "Only KYS lists required referral content and provides a referral template",
     None, None, "regional_pathway",
     "KYS is the only region that lists what a referral must contain (history, medications, pack-years, "
     "asbestos exposure, functional capacity, what the patient has been told) and provides a referral "
     "template.", "quoted", "verified by Hellu", "Hellu read KYS care chain v1.1 (08/2021) in full, 14 Nov; stage: Referral"),
    ("reg:kys_persistent", "KYS: refer persistent unexplained symptoms even if the X-ray is clear",
     None, None, "regional_pathway",
     "persistent unexplained symptoms → refer for pulmonologist assessment even if the X-ray is clear",
     "quoted", "verified by Hellu", "Hellu read KYS care chain in full, 14 Nov; stage: Primary care"),
    ("reg:only_kys_xray", "Only KYS tells primary care what to do with a normal X-ray and continuing symptoms",
     None, None, "regional_pathway",
     "Only KYS tells primary care what to do when the X-ray is normal but symptoms continue.",
     "quoted", "verified by Hellu", "5 regional pathways reviewed, not all 22 areas; stage: Primary care"),
    ("reg:occupational", "OYS and Keski-Suomi name occupational health as a referral source",
     None, None, "regional_pathway",
     "OYS and Keski-Suomi explicitly include occupational health as a referral source.",
     "quoted", "verified by Hellu", "stage: Primary care / occupational health"),
    ("reg:pirha_ct", "Pirha: CT most often within a week", None, None, "regional_pathway",
     'CT "most often within a week"', "quoted", "verified by Hellu", "target/typical time, not a commitment; stage: Imaging"),
    ("reg:pirha_referral", "Pirha: referral handled in 1–2 working days, invitation in 3–4 working days",
     None, None, "regional_pathway",
     'Referral handled "usually within 1–2 working days"; invitation "usually within 3–4 working days"',
     "quoted", "verified by Hellu", "stages: Referral, First specialist visit"),
    ("reg:ks_referral", "Keski-Suomi: referral handled as quickly as possible (no time stated)",
     None, None, "regional_pathway", 'Referral handled "as quickly as possible"', "quoted",
     "verified by Hellu", "stage: Referral"),
    ("reg:ks_target", "Keski-Suomi: lung clinic appointment within 2–3 weeks, at the latest about 1 month",
     None, None, "regional_pathway",
     "target: lung clinic appointment within 2–3 weeks, at the latest about 1 month after the referral arrives",
     "quoted", "verified by Hellu", "stage: First specialist visit"),
    ("reg:ks_tissue", "Keski-Suomi: tissue sample results in about 1–2 weeks", None, None, "regional_pathway",
     "tissue sample results in about 1–2 weeks", "quoted", "verified by Hellu", "stage: Diagnosis"),
    ("reg:pirha_bronch", "Pirha: bronchoscopy results usually within 3–5 days", None, None, "regional_pathway",
     'bronchoscopy results "usually within 3–5 days"', "quoted", "verified by Hellu", "stage: Diagnosis"),
    ("reg:satakunta_study", "Satakunta study: referral to diagnosis just under two months; biggest delay in "
     "specialist care", None, None, "regional_pathway",
     "referral → diagnosis just under two months; biggest delay in specialist care", "quoted",
     "verified by Hellu", "University of Turku regional study; stage: Diagnosis"),
    ("reg:named_contact", "No region names a contact person for the diagnostic phase", None, None,
     "regional_pathway", "no region names a contact person for the diagnostic phase. HUS assigns a nurse "
     "at the first visit", "quoted", "verified by Hellu", "stage: First specialist visit"),
    ("reg:mdt_practice", "MDT practice differs: KYS every patient weekly, Keski-Suomi every new case, HUS "
     "when needed", None, None, "regional_pathway",
     'KYS reviews every patient in a weekly MDT. Keski-Suomi reviews every new case. HUS refers to the MDT '
     'only "when needed".', "quoted", "verified by Hellu", "stage: MDT"),
    ("reg:not_monitored", "No region says whether it meets its stated times", None, None, "regional_pathway",
     "All stated times are targets or typical times, not commitments, and no region says whether it meets them.",
     "quoted", "verified by Hellu", "stage: Treatment start / all"),
    ("law:no_max", "There is no legal maximum time for a cancer suspicion", None, None, "law",
     "there is no legal maximum time for a cancer suspicion", "quoted", "verified by Hellu",
     "Health Care Act §52 and Valvira statement, read by Hellu"),
    ("thl:21_2016", "THL Ohjaus 21/2016 defines how cancer access times are recorded, for 16 cancers",
     16, "cancers", "access_monitoring_definition",
     "defined how cancer access times are recorded for 16 cancers, so that they could be reported nationally",
     "quoted", "verified by Hellu", "in force since 1 Jan 2017; THL document not in data/raw"),
    ("thl:no_report", "No published cancer-specific access-time report was found", None, None,
     "access_monitoring_report", "We found no published cancer-specific access-time report", "quoted",
     "draft", "Hellu's search; 'not published' to confirm with mentors"),
    ("lit:hilmo_90", "HILMO diagnoses match the Cancer Registry for about 90% of most cancer types", 90, "%",
     "hilmo_registry_agreement",
     "hospital discharge register (Hilmo) diagnoses matched the Cancer Registry for about 90% of most "
     "cancer types", "quoted", "verified by Hellu",
     "Ryynänen et al., Lääkärilehti 2019; reliability of referral/first-procedure data still to be confirmed"),
    ("filha:registry", "No lung cancer or other cancer quality registry; Cancer Registry, THL and FICAN are "
     "assessing one, starting with lung cancer", None, None, "quality_registry",
     "Finland has no lung cancer or other cancer quality registry. The Cancer Registry, THL and FICAN are "
     "assessing what registry is needed, starting with lung cancer.", "quoted", "verified locally",
     "Hellu's summary of the Filha programme; confirmed against Filha p.21 (see the Filha p.21 quote claims)"),
    ("alert:returned_7d", "Draft alert: referral returned and no new referral within 7 days", 7, "days",
     "alert_threshold", "No new referral within 7 days → alert", "quoted", "draft",
     "Hellu's draft rule; threshold to confirm with Kaisa"),
    ("alert:first_visit_14d", "Draft alert: referral accepted and no first visit within 14 days", 14, "days",
     "alert_threshold", "No first visit within 14 days → alert", "quoted", "draft",
     "Hellu's draft rule; threshold to confirm with Kaisa"),
    ("mentor:kaisa_referral", "A weak referral gets a lower urgency rating in specialist care", None, None,
     "mentor_insight", "A weak referral gets a lower urgency rating in specialist care.", "mentor",
     "mentor insight", "Kaisa; no written source"),
    ("mentor:hanna_occupational", "Occupational health gets patients to specialist care faster", None, None,
     "mentor_insight", "Occupational health gets patients to specialist care faster (mentor: Hanna).",
     "mentor", "mentor insight", "Hanna; no written source"),
    ("mentor:one_third", "Mentor mention 'One-third split' (meaning and source not yet known)", None, None,
     "mentor_insight", '"One-third split"', "mentor", "draft",
     "listed in the brief as mentor insight, source to confirm with Kaisa; content unknown, so not citable"),
    # Statements in the brief that our verification contradicts (status superseded).
    ("brief:no_lung_guideline", "Lung cancer has no national guideline apart from the 2026 programme "
     "(brief §4, diabetes comparison)", None, None, "national_guideline",
     "National programme since 2026, but no pathway or time targets yet", "quoted", "superseded",
     "SUPERSEDED: Filha p.4 says common diagnostic guidelines exist and Filha cites the Käypä hoito "
     "'Keuhkosyöpä' guideline (2017, ref. 8, p.27); what is missing is national timing guidance. "
     "Superseded by: {Keuhkosyöpien diagnostiikkaan on Suomessa yhteiset ohjeet} {Keuhkosyöpä. Käypä hoito -suositus}"),
    ("brief:referral_organisation", "The Filha programme reports regional variation in diagnostic speed, "
     "referral organisation and surgery volumes", None, None, "regional_variation",
     "It reports large regional variation in diagnostic speed, referral organisation and surgery volumes.",
     "quoted", "superseded",
     "SUPERSEDED: Filha p.4 says 'hoitovastuun järjestämisessä', i.e. organisation of care responsibility, "
     "not referral organisation. Superseded by: {alueellinen vaihtelu diagnoosin nopeudessa}"),
]


def brief_claims() -> list[dict]:
    rows = []
    for cid, text, value, unit, metric, quote, method, status, notes in BRIEF_CLAIMS:
        quote = quote.strip('"') if quote.startswith('"') and quote.endswith('"') else quote
        labels = sources.find(BRIEF, quote)
        rows.append({
            "id": cid, "claim_text": text, "value": value, "unit": unit, "county": None, "metric": metric,
            "source_doc": BRIEF, "location": "; ".join(labels) if labels else None, "quote": quote,
            "quote_lang": "en", "method": method, "status": status, "notes": notes,
        })
    return rows


# ---------------------------------------------------------------- assembly
def merge_quotes(rows: list[dict]) -> list[dict]:
    """The same quote cited in several places becomes one claim; keep the first claim text."""
    out: dict[str, dict] = {}
    for r in rows:
        if r["id"] in out and r.get("quote_lang") != out[r["id"]].get("quote_lang"):
            # Same text, different (or missing) language marker: never merge it away silently.
            r["id"] += f":lang-{r.get('quote_lang') or 'missing'}"
        if r["id"] in out and r["id"].startswith("q:"):
            cited = r["notes"].split("cited in ", 1)[1].split(";")[0]
            if cited not in out[r["id"]]["notes"]:
                out[r["id"]]["notes"] = out[r["id"]]["notes"].replace("cited in ", f"cited in {cited}, ", 1)
        else:
            out[r["id"]] = r
    return list(out.values())


def attach_english(rows: list[dict]) -> list[dict]:
    """English doc quotes belong to a brief claim: attach them to it instead of keeping a separate
    claim. Unmatched ones stay as 'draft' claims, which check_claims.py rejects."""
    brief = [r for r in rows if r["source_doc"] == BRIEF and not r["id"].startswith("q:")]
    out = []
    for r in rows:
        if r["id"].startswith("q:") and r.get("quote_lang") == "en":
            key = sources.normalise(r["quote"])
            owner = next((b for b in brief if key and key in sources.normalise(b["quote"])), None)
            if owner:
                cited = r["notes"].split("cited in ", 1)[1].split(";")[0]
                owner["notes"] += f"; quoted in {cited}"
                continue
            r["notes"] += "; ENGLISH QUOTE NOT LINKED to a brief claim (add it to BRIEF_CLAIMS)"
        out.append(r)
    return out


def resolve_superseded(rows: list[dict]) -> None:
    """Replace {quote prefix} placeholders in superseded notes with the ids of the verified claims."""
    for r in rows:
        if r["status"] != "superseded":
            continue
        def sub(m: re.Match) -> str:
            prefix = sources.normalise(m.group(1))
            hit = [x["id"] for x in rows if x.get("quote") and x["status"] == "verified locally"
                   and x["source_doc"] != BRIEF and sources.normalise(x["quote"]).startswith(prefix)]
            assert hit, f"{r['id']}: no verified claim starts with {m.group(1)!r}"
            return hit[0]
        r["notes"] = re.sub(r"\{([^}]+)\}", sub, r["notes"])


def add_translations(rows: list[dict]) -> int:
    if not TRANSLATIONS.exists():
        return 0
    tr = pd.read_csv(TRANSLATIONS, dtype=str).fillna("")
    by_key = dict(zip(tr["quote_key"], tr["quote_en"]))
    n = 0
    for r in rows:
        if r.get("quote_lang") == "fi" and by_key.get(quote_key(r["quote"])):
            r["quote_en"] = by_key[quote_key(r["quote"])]
            n += 1
    return n


def main() -> int:
    rows = (county_claims() + national_claims() + kuva16_claims() + brief_claims()
            + blind_spot_claims() + [r for d in QUOTE_DOCS for r in doc_quote_claims(d)])
    rows = attach_english(merge_quotes(rows))
    resolve_superseded(rows)
    n_tr = add_translations(rows)
    con = ledger.create()
    ledger.insert(con, rows)
    con.close()

    print(f"Loaded {len(rows)} claims into {ledger.DB} ({n_tr} Finnish quotes with an English translation)")
    for field in ("status", "method", "quote_lang"):
        print(f"\nClaims per {field}:")
        for k, n in Counter(r.get(field) for r in rows).most_common():
            print(f"  {str(k):<18} {n}")
    bad = [r for r in rows if r.get("quote") and (not r["location"] or not r.get("quote_lang")
                                                  or "NOT LINKED" in r["notes"])]
    if bad:
        print(f"\n{len(bad)} quote problems (src/check_claims.py will fail):")
        for r in bad:
            print(f"  {r['id']}  [{r['source_doc']}] lang={r.get('quote_lang')}  {r['quote'][:100]!r}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
