"""Fill data/ledger.sqlite from our derived data and verified documents.

Sources loaded:
  1. data/processed/county_treatment.csv     county/area shares + Wilson CIs   (computed)
     + national shares from Taulukko 5/6                                       (computed)
  2. data/processed/kuva16_curative_digitised.csv  age-adjusted curative        (digitised)
  3. data/processed/blind_spots.csv          coverage per pathway stage         (assessed)
     + Finnish quotes in its report_note and policy columns                     (quoted)
  4. docs/source_verification.md, docs/recommendations.md: every Finnish quote (quoted)
  5. docs/pathway_brief.md: MOT delays, regional pathways, law, mentor input, each with a verbatim
     quote from the brief and Hellu's status (BRIEF_CLAIMS below)

Quote locations are not typed by hand: each quote is searched in the local source texts
(src/sources.py) and its location is every page/section where it is found.
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

TREATMENT = {  # Finnish category -> (metric slug, English label)
    "Parantava": ("curative", "curative treatment"),
    "Jarruttava": ("life_prolonging", "life-prolonging treatment"),
    "Oireenmukainen": ("symptomatic", "symptomatic treatment"),
    "Ei hoitotietoa": ("no_treatment_record", "no treatment record within 12 months"),
    "MDT-käsittely": ("mdt_recorded", "MDT meeting recorded"),
}
FINNISH = re.compile(r"[äöåÄÖÅ]")
# A quoted string counts as English (not a source quote) if it has one of these words.
# Finnish "on" and "a" are deliberately absent.
ENGLISH = {"the", "and", "of", "to", "is", "in", "for", "with", "not", "by", "as", "what", "how", "but",
           "does", "are", "was", "be", "it", "an", "at", "pack", "referral", "organisation",
           "timestamps", "published", "verified", "no", "treatment", "record"}


def is_finnish(q: str) -> bool:
    words = re.findall(r"[^\W\d_]+", q.lower())
    return bool(FINNISH.search(q)) or (len(words) >= 2 and not ENGLISH.intersection(words))


def short(county: str) -> str:
    return re.sub(r"\W+", "_", county).strip("_")


def qid(src: str, quote: str) -> str:
    key = sources.normalise(quote).rstrip(".,;:")  # "…ole." and "…ole" are the same quote
    return "q:" + hashlib.sha1((src + key).encode("utf-8")).hexdigest()[:10]


def strip_md(text: str) -> str:
    return re.sub(r"[*`]", "", text).strip()


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
        share = round(n / n_all * 100, 2)
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


# ---------------------------------------------------------------- quotes (shared helper)
def quote_claim(quote: str, claim_text: str, prefer: list[str], cited_in: str) -> dict:
    """A quoted claim. The source and location are found by searching the local texts."""
    quote = quote.strip().strip('"').strip()
    src, labels = sources.find_anywhere(quote, prefer)
    return {
        "id": qid(src or (prefer[0] if prefer else "?"), quote), "claim_text": claim_text,
        "value": None, "unit": None, "county": None, "metric": None,
        "source_doc": src or (prefer[0] if prefer else None),
        "location": "; ".join(labels) if labels else None,
        "quote": quote, "method": "quoted", "status": "verified locally",
        "notes": f"cited in {cited_in}" + ("" if src else "; NOT FOUND in any local source"),
    }


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


def inline_quotes(text: str, single: bool = False) -> list[tuple[str, str, int]]:
    """Finnish quotes in running text: "…" (and '…' if single=True), at least two words.
    Returns (quote, translation-if-given, position)."""
    out = []
    pattern = r'"([^"]{6,})"|\'([^\']{6,})\'' if single else r'"([^"]{6,})"()'
    for m in re.finditer(pattern, text):
        q = m.group(1) or m.group(2)
        if is_finnish(q):
            tr = re.match(r"\s*\(\*([^*]+)\*\)", text[m.end():])
            out.append((q, tr.group(1).strip() if tr else "", m.start()))
    return out


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
            "notes": r.report_note,
        })
        for q, _, _ in inline_quotes(r.report_note):
            rows.append(quote_claim(q, f"Report evidence for blind spot '{r.stage}'", [REPORT],
                                    "data/processed/blind_spots.csv (report_note)"))
        for q, _, pos in inline_quotes(r.policy, single=True):
            rows.append(quote_claim(q, f"Policy evidence for pathway stage '{r.stage}'",
                                    prefer_from(r.policy, before=pos),
                                    "data/processed/blind_spots.csv (policy)"))
    return rows


# ---------------------------------------------------------------- 4. quotes in the docs
def doc_quote_claims(path: str) -> list[dict]:
    lines = Path(path).read_text(encoding="utf-8").splitlines()
    rows, heading = [], ""
    blocks, buf = [], []
    for line in lines + [""]:  # split into blocks; every table row is its own block
        s = line.strip()
        if s.startswith("#"):
            if buf:
                blocks.append(("text", buf, heading))
                buf = []
            heading = s.lstrip("#").strip()
        elif s.startswith("|"):
            if buf:
                blocks.append(("text", buf, heading))
                buf = []
            blocks.append(("row", [s], heading))
        elif not s:
            if buf:
                blocks.append(("text", buf, heading))
                buf = []
        else:
            buf.append(s)

    for i, (kind, blines, head) in enumerate(blocks):
        if kind == "row":
            cells = [c.strip() for c in blines[0].strip("|").split("|")]
            point = strip_md(cells[0])
            prefer = prefer_from(cells[1] if len(cells) > 1 else "") or prefer_from(head)
            for q, _, _ in inline_quotes(cells[0]):
                rows.append(quote_claim(q, point, prefer, path))
            continue
        if all(l.startswith(">") for l in blines):  # blockquote
            body = " ".join(l.lstrip("> ").strip() for l in blines)
            quotes = [q for q in (re.findall(r'"([^"]+)"', body) or [body]) if is_finnish(q)]
            nxt = blocks[i + 1] if i + 1 < len(blocks) else None
            nxt_text = " ".join(nxt[1]) if nxt and nxt[0] == "text" else ""
            translation = nxt_text.split("*")[1] if nxt_text.startswith("*") else ""
            prev = " ".join(blocks[i - 1][1]) if i and blocks[i - 1][0] == "text" else ""
            prefer = prefer_from(prev, before=len(prev)) + prefer_from(head)
            for q in quotes:
                rows.append(quote_claim(q, translation or f"Quote under: {head}", prefer, path))
            continue
        text = " ".join(blines)
        # blockquotes indented inside a list item: "- bullet ... > quote"
        text = re.sub(r"\s>\s", " ", text)
        for q, tr, pos in inline_quotes(text):
            prefer = prefer_from(text, before=pos) + prefer_from(head)
            rows.append(quote_claim(q, tr or strip_md(text)[:300], prefer, path))
    return rows


# ---------------------------------------------------------------- 5. Hellu's brief
# (id, claim_text, value, unit, metric, verbatim quote from the brief, method, status, notes)
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
]


def brief_claims() -> list[dict]:
    rows = []
    for cid, text, value, unit, metric, quote, method, status, notes in BRIEF_CLAIMS:
        labels = sources.find(BRIEF, quote)
        rows.append({
            "id": cid, "claim_text": text, "value": value, "unit": unit, "county": None, "metric": metric,
            "source_doc": BRIEF, "location": "; ".join(labels) if labels else None, "quote": quote,
            "method": method, "status": status, "notes": notes,
        })
    return rows


# ---------------------------------------------------------------- main
def merge_quotes(rows: list[dict]) -> list[dict]:
    """The same quote cited in several places becomes one claim; keep the first claim text."""
    out: dict[str, dict] = {}
    for r in rows:
        if r["id"] in out and r["id"].startswith("q:"):
            cited = r["notes"].split("cited in ", 1)[1].split(";")[0]
            if cited not in out[r["id"]]["notes"]:
                out[r["id"]]["notes"] = out[r["id"]]["notes"].replace(
                    "cited in ", f"cited in {cited}, ", 1)
        else:
            out[r["id"]] = r
    return list(out.values())


def main() -> int:
    rows = (county_claims() + national_claims() + kuva16_claims() + blind_spot_claims()
            + doc_quote_claims("docs/source_verification.md") + doc_quote_claims("docs/recommendations.md")
            + brief_claims())
    rows = merge_quotes(rows)
    con = ledger.create()
    ledger.insert(con, rows)
    con.close()

    print(f"Loaded {len(rows)} claims into {ledger.DB}")
    for field in ("status", "method"):
        print(f"\nClaims per {field}:")
        for k, n in Counter(r[field] for r in rows).most_common():
            print(f"  {k:<18} {n}")
    missing = [r for r in rows if r["method"] in ("quoted", "mentor") and not r["location"]]
    if missing:
        print(f"\n{len(missing)} quotes NOT FOUND in their sources (src/check_claims.py will fail):")
        for r in missing:
            print(f"  {r['id']}  [{r['source_doc']}]  {r['quote'][:110]!r}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
