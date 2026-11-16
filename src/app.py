"""Lingonberry: Equal Care Across Finland. Streamlit app.

Run with:  uv run streamlit run src/app.py

Shows, for one region (a wellbeing services county or the City of Helsinki), the saved validated brief
(outputs/briefs/<slug>.json), every claim behind it (data/ledger.sqlite), a regional comparison chart, the pathway blind spots and how
the numbers were verified. "Regenerate with Gemini" runs the live pipeline (brief + validate + review).
Public aggregate data only: no patient-level data is read or shown anywhere.
"""
import json
import os
import re
import sqlite3
import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
os.chdir(ROOT)  # all pipeline paths are relative to the repo root
sys.path.insert(0, str(ROOT / "src"))

import streamlit as st  # noqa: E402

LOGO = ROOT / "assets" / "logo.svg"
# First Streamlit call. Inside a running app Streamlit turns a local .svg path into an SVG data URI for
# the favicon (checked in the test harness), so no PNG is needed. The logo is shown only next to the
# sidebar title, not with st.logo.
st.set_page_config(page_title="Lingonberry", page_icon=str(LOGO), layout="wide")


def inject_css() -> None:
    """All custom CSS, in one place. Colours come from the theme (.streamlit/config.toml); this adds what the
    theme cannot: card borders (#E9E4E0, 12px radius), the header row, the tab look, the pathway stage
    buttons and the dot-plot rows (an HTML grid; below 640px the name and value sit above the track).
    Cards are containers with a key starting "card" (Streamlit turns a key into the CSS class
    st-key-<key>); "soft" cards use the warmer panel colour."""
    st.markdown("""<style>
[data-testid="stMainBlockContainer"] {max-width: 1180px; padding-top: 2.5rem; padding-bottom: 2rem;}
/* Claim pills sit in one no-wrap row by default, so long claim IDs ran past narrow columns: wrap them. */
div[data-testid="stButtonGroup"] div:has(> button) {flex-wrap: wrap !important; overflow-x: visible !important;
  row-gap: .4rem;}
/* Cards */
[class*="st-key-card"] {border: 1px solid #E9E4E0 !important; border-radius: 12px !important; background: #FFFFFF;}
[class*="st-key-soft"] {border: 1px solid #ECE6E1 !important; border-radius: 12px !important; background: #FBF8F5;}
[data-testid="stExpander"] details {border-color: #E9E4E0; border-radius: 12px; background: #FFFFFF;}
/* Header row */
.lb-brand {display: flex; align-items: center; gap: 10px; flex-wrap: wrap;}
.lb-brand b {font-size: 1.15rem; letter-spacing: -0.01em;}
.lb-brand span {font-size: .82rem; color: #6F6762;}
.st-key-region [data-testid="stSelectbox"] {display: flex; flex-direction: row; align-items: center; gap: .5rem;}
.st-key-region [data-testid="stSelectbox"] > div {flex: 1; min-width: 0;}
.st-key-region [data-testid="stWidgetLabel"] {margin: 0 .25rem 0 0; min-height: 0; color: #6F6762; gap: .25rem;}
[class*="st-key-meta"] button {border-radius: 999px;}
.st-key-meta-ok button {background: #F1F8F2; border-color: #CFE3D4; color: #1F6A36;}
.st-key-meta-draft button {background: #FDF4E7; border-color: #EBCF9F; color: #8A5A12;}
/* Tabs: active tab in ink, not red; the red underline stays */
[data-testid="stTab"][aria-selected="true"] p {color: #1F1B1A; font-weight: 600;}
/* Pathway: stage buttons left-aligned; the selected one gets a dark border */
[class*="st-key-stage"] button {justify-content: flex-start; text-align: left; background: #FBF9F7;
  border-color: #E9E4E0; border-radius: 8px;}
[class*="st-key-stage"] button > div {justify-content: flex-start; width: 100%;}
[class*="st-key-stagesel-"] button {background: #FFFFFF; border: 1.5px solid #1F1B1A;}
/* Small type */
.lb-eyebrow {font-family: ui-monospace, "SFMono-Regular", Consolas, monospace; font-size: 12px; letter-spacing: .06em;
  text-transform: uppercase; color: #8A817B;}
/* Brief hero */
.lb-verdict {margin: .6rem 0 0; font-size: clamp(1.9rem, 4vw, 2.4rem); line-height: 1.14; letter-spacing: -0.02em;
  font-weight: 600; color: #1F1B1A; text-wrap: pretty;}
.lb-lede {margin: .9rem 0 1rem; font-size: 1rem; line-height: 1.55; color: #5A524D; max-width: 560px;}
.st-key-go-pathway button p, [class*="st-key-next-"] button p,
[class*="st-key-next-"] button span {color: #B3263A; font-weight: 500;}
/* Brief sections: expander title larger, like the design's question cards */
[data-testid="stExpander"] summary strong {font-size: 1.1rem; font-weight: 600;}
[data-testid="stExpander"] summary {padding-top: .8rem; padding-bottom: .8rem;}
/* Compare regions: ranked dot plot (HTML rows from dot_plot_html) and its legend */
.lb-dp {display: flex; flex-direction: column; gap: 2px;}
.lb-dp-row {display: grid; grid-template-columns: clamp(80px, 28%, 150px) minmax(0, 1fr) 46px; align-items: center;
  gap: 12px;
  padding: 5px 8px; border-radius: 6px; font-size: 13px; color: #5A524D;}
.lb-dp-row.sel {background: #FBF0F1; color: #1F1B1A; font-weight: 600;}
.lb-dp-name {overflow: hidden; text-overflow: ellipsis; white-space: nowrap;}
.lb-dp-val {text-align: right; font-variant-numeric: tabular-nums;}
.lb-dp-track {position: relative; height: 18px;}
.lb-dp-nat {position: absolute; top: -6px; bottom: -6px; border-left: 1.5px dashed #B9B0AA;}
.lb-dp-ci {position: absolute; top: 8px; height: 2px; border-radius: 1px; background: #DDD6D1;}
.lb-dp-dot {position: absolute; top: 4px; width: 10px; height: 10px; margin-left: -5px; border-radius: 50%;
  background: #C9C1BB; border: 1.5px solid #FFFFFF; box-sizing: border-box;}
.lb-dp-row.clear .lb-dp-ci {background: #A59C96;}
.lb-dp-row.clear .lb-dp-dot {background: #5A524D;}
.lb-dp-row.sel .lb-dp-ci, .lb-dp-row.sel .lb-dp-dot {background: #B3263A;}
.lb-dp-axis {padding-top: 8px;}
.lb-dp-ticks {display: flex; justify-content: space-between; font-size: 11px; color: #8A817B;
  border-top: 1px solid #F1EDEA; padding-top: 6px; font-family: ui-monospace, Consolas, monospace;}
@media (max-width: 640px) {  /* phones: name and value on one line, the full-width track below */
  .lb-dp-row {grid-template-columns: minmax(0, 1fr) 46px; grid-template-areas: "name val" "track track"; row-gap: 2px;}
  .lb-dp-name {grid-area: name;} .lb-dp-val {grid-area: val;} .lb-dp-track, .lb-dp-ticks {grid-area: track;}
  .lb-dp-axis > div:empty {display: none;}
}
.lb-legend {display: flex; gap: 6px 18px; flex-wrap: wrap; font-size: 12px; color: #6F6762; margin-bottom: .6rem;}
.lb-legend span {display: flex; align-items: center; gap: 6px;}
.lb-legend i {width: 10px; height: 10px; border-radius: 50%; display: inline-block;}
.lb-legend i.sel {background: #B3263A;} .lb-legend i.clear {background: #5A524D;}
.lb-legend i.unclear {background: #C9C1BB;}
/* Footer: right part right-aligned only when the columns sit side by side */
@media (min-width: 640px) {.st-key-foot-right {text-align: right;}}
</style>""", unsafe_allow_html=True)


inject_css()

import base64  # noqa: E402
import hashlib  # noqa: E402
import html  # noqa: E402
from datetime import datetime  # noqa: E402

import altair as alt  # noqa: E402
import pandas as pd  # noqa: E402
from dotenv import load_dotenv  # noqa: E402

import core_message  # noqa: E402
import counties  # noqa: E402
import ledger  # noqa: E402
import sources  # noqa: E402
from validate_brief import SECTIONS, validate  # noqa: E402

# ---------------------------------------------------------------- deployment mode
# Gemini settings come from .env locally, or from Streamlit secrets on a host. Viewing needs none.
GEMINI_SETTINGS = ("GEMINI_API_KEY", "MODEL_REASON", "MODEL_EXTRACT")
load_dotenv()
try:
    for _k in GEMINI_SETTINGS:
        if _k in st.secrets and not os.environ.get(_k):
            os.environ[_k] = str(st.secrets[_k])
except Exception:  # noqa: BLE001 - no secrets file at all is the normal case for viewers
    pass
GEMINI_CONFIGURED = all(os.environ.get(k) for k in GEMINI_SETTINGS)
# data/raw/ is not in the repo; without it check_claims.py cannot re-find quotes, so the app shows the
# last locally recorded results instead (outputs/verification_snapshot.json).
RAW_SOURCES = [p for p in sources.SOURCES if p.startswith("data/raw/")]
RAW_PRESENT = all(Path(p).exists() for p in RAW_SOURCES)
SNAPSHOT = Path("outputs/verification_snapshot.json")

LOGO_URI = "data:image/svg+xml;base64," + base64.b64encode(LOGO.read_bytes()).decode("ascii")

BRIEFS = Path("outputs/briefs")
TITLES = {"where_we_lag": "Where do we lag?", "how_sure_are_we": "How sure are we?",
          "what_to_do_first": "What should we do first?"}
SOURCE_NAMES = {
    "keuhkosyoparaportti_2019_2023.html": "Finnish Cancer Registry: Keuhkosyöpä Suomessa 2019–2023",
    "strategy_2026_2035_fi.pdf": "National Cancer Strategy 2026–2035 (STM)",
    "roadmap_2026_2031_fi.pdf": "Cancer strategy implementation roadmap 2026–2031 (STM)",
    "filha_lung_programme_2026_fi.pdf": "Filha National Lung Cancer Programme 2026–2035",
    "pathway_brief.md": "Team background brief (Hellu)",
}
STATUS_STYLE = {  # (badge colour, icon) — icon + label, never colour alone
    "verified locally": ("green", ":material/verified:"),
    "verified by Hellu": ("blue", ":material/person_check:"),
    "preliminary": ("orange", ":material/hourglass_top:"),
    "mentor insight": ("violet", ":material/forum:"),
    ledger.RECOMMENDATION: ("primary", ":material/lightbulb:"),
    "draft": ("gray", ":material/edit_note:"),
    "superseded": ("red", ":material/block:"),
}
MEASURED = {"yes": (":green[:material/check_circle: Measured]"),
            "partly": (":orange[:material/remove_circle: Partly measured]"),
            "no": (":red[:material/cancel: Not measured]")}


# ---------------------------------------------------------------- data (cached by file mtime)
def mtime(*paths: str | Path) -> float:
    return sum(Path(p).stat().st_mtime for p in paths if Path(p).exists())


@st.cache_data
def load_claims(_m: float) -> dict[str, dict]:
    con = sqlite3.connect(ledger.DB)
    con.row_factory = sqlite3.Row
    out = {r["id"]: dict(r) for r in con.execute("SELECT * FROM claims")}
    con.close()
    return out


@st.cache_data
def load_csv(path: str, _m: float) -> pd.DataFrame:
    return pd.read_csv(path)


@st.cache_data
def load_brief(slug: str, _m: float) -> tuple[dict | None, dict | None]:
    b, r = BRIEFS / f"{slug}.json", BRIEFS / f"{slug}.review.json"
    brief = json.loads(b.read_text(encoding="utf-8")) if b.exists() else None
    rev = json.loads(r.read_text(encoding="utf-8")) if r.exists() else None
    return brief, rev


@st.cache_data(show_spinner="Running src/check_claims.py…")
def run_check_claims(_m: float) -> tuple[int, str]:
    p = subprocess.run([sys.executable, "src/check_claims.py"], capture_output=True, text=True,
                       encoding="utf-8", env={**os.environ, "PYTHONIOENCODING": "utf-8"})
    return p.returncode, (p.stdout + p.stderr).strip()


@st.cache_data
def load_snapshot(_m: float) -> dict | None:
    return json.loads(SNAPSHOT.read_text(encoding="utf-8")) if SNAPSHOT.exists() else None


def snapshot_time(snap: dict) -> str:
    return snap["written_at"].replace("T", " ").replace("+00:00", " UTC")


def snapshot_note(snap: dict) -> None:
    """Where the snapshot comes from, and whether the deployed ledger is the one that was verified."""
    same = hashlib.md5(ledger.DB.read_bytes()).hexdigest() == snap["ledger_md5"]
    st.caption(f"The source documents (data/raw/) are not on this server, so this is the result recorded by "
               f"`src/write_verification_snapshot.py` at commit `{snap['commit'][:7]}`"
               + (" (with uncommitted changes)" if snap["commit_dirty"] else "") + ". "
               + ("The ledger served here is the same file that was verified."
                  if same else "**The ledger served here differs from the one that was verified.**"))


claims = load_claims(mtime(ledger.DB))
ct = load_csv("data/processed/county_treatment.csv", mtime("data/processed/county_treatment.csv"))
bs = load_csv("data/processed/blind_spots.csv", mtime("data/processed/blind_spots.csv")).fillna("")
cty = ct[ct["level"] == "county"]

# Plain-language definitions for non-expert readers. Based on docs/definitions.md (report §3.3, §4.2);
# they are explanations, not ledger claims, so they carry no figures.
GLOSSARY = {
    "pp": "Percentage points: the plain difference between two percentages. For example, if one rate is 30% "
          "and another is 25%, the gap is 5 percentage points.",
    "95% CI": "95% confidence interval: the range the true share is likely to lie in, given how many patients "
              "a region has. If a region's range includes Finland's value, the data cannot tell them apart.",
    "Curative treatment": "Treatment that aims to cure the cancer: surgery, stereotactic radiotherapy, or "
                          "chemotherapy and radiotherapy given before, after or together with them. A patient "
                          "counts if they have any curative-treatment record within 12 months.",
    "No treatment record": "No record of any lung cancer treatment within 12 months. This mixes patients who "
                           "were not treated and treatment that was given but not recorded, so it does not "
                           "mean ‘untreated’.",
    "Crude share": "The plain percentage of all new patients in a region. It is not adjusted for differences "
                   "in age or cancer stage, so a lower share is not by itself proof of worse care.",
    "MDT": "Multidisciplinary team meeting, where specialists discuss a patient together. Only some meetings "
           "are recorded in the national register, so MDT figures show recording practice, not how many "
           "patients were discussed.",
    "Ledger": "Our list of every number and quote used in this app, each with its source document, page or "
              "table, and how it was checked (data/ledger.sqlite).",
}
# vs_national (src/add_ci.py): verdict headline and badge colour. "below"/"above" = 95% CI entirely below/above.
VERDICT = {
    "below": ("A smaller share of patients here receives curative treatment than across Finland.", "red"),
    "above": ("A larger share of patients here receives curative treatment than across Finland.", "green"),
    "not distinguishable": ("Curative treatment here is not clearly different from Finland.", "gray"),
}
LINGON, FINLAND_GREY, TRACK = "#B3263A", "#B9B0AA", "#F1EDEA"


def region_measure(full_name: str, treatment: str) -> pd.Series:
    """One row of county_treatment.csv: a region's share, 95% CI and national share for one measure."""
    return cty[(cty["county"] == full_name) & (cty["treatment"] == treatment)].iloc[0]


def signed_pp(v: float) -> str:
    return f"{v:+.1f} pp".replace("-", "−")


def clean(text: str) -> str:
    """Render <q lang="…"> quote markers as typographic quotes."""
    return re.sub(r'<q lang="[a-z]{2}">(.*?)</q>', r"“\1”", text)


def source_name(c: dict) -> str:
    doc = (c.get("source_doc") or "").split("/")[-1]
    return SOURCE_NAMES.get(doc, doc)


def short_id(cid: str) -> str:
    return cid.replace("_hyvinvointialue", "").replace("_kaupunki", "")


def status_badge(status: str) -> None:
    colour, icon = STATUS_STYLE.get(status, ("gray", ":material/help:"))
    st.badge(status, color=colour, icon=icon)


def claim_card(cid: str, key: str) -> None:
    """One claim with its source and quote. `key` must be unique on the page (it styles the card)."""
    c = claims.get(cid)
    with st.container(border=True, key=f"card-claim-{key}"):
        if c is None:
            st.error(f"Claim {cid} is not in the ledger.")
            return
        st.markdown(f"**{c['claim_text']}**")
        status_badge(c["status"])
        if c["status"] == ledger.RECOMMENDATION:
            st.markdown(":primary[:material/lightbulb: **Our recommendation** · the team's own draft proposal, "
                        "not evidence. Its evidence is cited separately in the same sentence.]")
        st.caption(f"`{cid}` · method: {c['method']} · source: {source_name(c)} · location: {c['location']}")
        if c.get("quote"):
            lang = {"fi": "Finnish original", "en": "Quoted from the team brief"}.get(c["quote_lang"], "Quote")
            st.markdown(f"*{lang}:*")
            st.markdown("> " + c["quote"].replace("\n", " "))
            if c.get("quote_en"):
                st.markdown("*English translation (machine translation, gemini-4-hydrogen; check against the original):*")
                st.markdown("> " + c["quote_en"])
        if c.get("notes"):
            st.caption(f"Notes: {c['notes']}")


SEVERITY = {"high": ("red", ":material/error:"), "medium": ("orange", ":material/warning:"),
            "low": ("gray", ":material/info:")}


def flag_place(location: str) -> str:
    """'how_sure_are_we.details[2]' -> 'How sure are we? · detail 3'."""
    m = re.match(r"(\w+)\.(headline|details\[(\d+)\])", location)
    if not m:
        return location
    part = "headline" if m.group(2) == "headline" else f"detail {int(m.group(3)) + 1}"
    return f"{TITLES.get(m.group(1), m.group(1))} · {part}"


def flagged_for_review(review: dict, brief: dict) -> None:
    """Model review flags, shown apart from the validated text. They never change the brief.
    Called only when there are flags; "nothing flagged" is shown in the header popover."""
    with st.container(border=True, key="card-flags"):
        n = len(review["flags"])
        st.subheader(f":material/flag: Flagged for human review ({n})")
        st.caption("Not part of the validated brief. A second model (gemini-4-hydrogen) read each sentence "
                   "against its cited claims and raised these for a person to check. Flags never approve, "
                   "reject or change the brief.")
        order = {"high": 0, "medium": 1, "low": 2}
        for i, f in enumerate(sorted(review["flags"], key=lambda f: order.get(f["severity"], 3))):
            colour, icon = SEVERITY.get(f["severity"], ("gray", ":material/help:"))
            with st.container(border=True, key=f"card-flag-{i}"):
                st.badge(f["severity"].capitalize(), color=colour, icon=icon)
                st.markdown(f"**{flag_place(f['location'])}**")
                if f.get("sentence") and f["sentence"] != "-":
                    st.markdown(f"> {f['sentence']}")
                st.markdown(f["problem"])


def claim_pills(ids: list[str], key: str) -> None:
    """Claim IDs as pills; clicking one opens its claim card."""
    picked = st.pills("Claims", ids, key=key, format_func=short_id, label_visibility="collapsed",
                      selection_mode="single")
    if picked:
        claim_card(picked, key)


def go_to_tab(label: str) -> None:
    """Button callback: switch the stateful tabs (key NAV) to `label`."""
    st.session_state[NAV] = label


def unique(ids) -> list[str]:
    return list(dict.fromkeys(ids))


def finnish_order(name: str) -> str:
    """Sort key for Finnish alphabetical order (å, ä, ö after z)."""
    return name.lower().translate(str.maketrans({"å": "{", "ä": "|", "ö": "}"}))


def generated_on(iso: str) -> str:
    """'2026-11-14T13:36:57+00:00' -> '14 Nov 2026'."""
    d = datetime.fromisoformat(iso)
    return f"{d.day} {d:%b %Y}"


def regenerate_button() -> None:
    """Regenerate with Gemini: disabled, with the reason, when no API key is configured."""
    if not GEMINI_CONFIGURED:
        st.caption(":material/visibility: View-only: showing saved, validated briefs. Live regeneration needs "
                   "a Gemini API key, which this deployment does not have.")
    if st.button("Regenerate with Gemini", icon=":material/refresh:", width="stretch",
                 disabled=not GEMINI_CONFIGURED,
                 help="Runs the live pipeline: brief (gemini-4-argon) → validate → review (gemini-4-hydrogen). "
                      "Takes a few minutes and uses API quota."):
        with st.status(f"Generating a brief for {short}…", expanded=True) as box:
            try:
                import brief as brief_pipeline
                st.write("Calling the model, validating, reviewing…")
                doc = brief_pipeline.run(short)
                box.update(label=f"Done: {doc['status']} after {doc['attempts']} attempt(s)", state="complete")
                st.cache_data.clear()
                st.rerun()
            except SystemExit as e:
                box.update(label="Could not run the pipeline", state="error")
                st.error(str(e))
            except Exception as e:  # noqa: BLE001 - show any pipeline failure to the user
                box.update(label="Pipeline failed", state="error")
                st.exception(e)


def brief_status(brief_doc: dict | None, review_doc: dict | None) -> None:
    """Header popover: how the saved brief was made, its review result, and the Regenerate button."""
    if brief_doc and brief_doc["status"] == "validated":
        label, icon, key = "Validated brief", ":material/check:", "meta-ok"
    elif brief_doc:
        label, icon, key = "Draft brief", ":material/warning:", "meta-draft"
    else:
        label, icon, key = "No saved brief", ":material/info:", "meta-none"
    with st.popover(label, icon=icon, key=key):
        if brief_doc:
            n = brief_doc["attempts"]
            st.markdown(f"Written by {brief_doc['model']} (thinking: {brief_doc['thinking_level'].lower()}) on "
                        f"{generated_on(brief_doc['generated_at'])}, after {n} attempt{'s' if n != 1 else ''}.")
            if brief_doc["status"] != "validated":
                st.badge("DRAFT: failed validation", color="orange", icon=":material/warning:")
            if review_doc:
                flags = len(review_doc["flags"])
                st.markdown(":green[:material/check: Nothing flagged by the second-model review]" if not flags
                            else f":orange[:material/flag: {flags} flag{'s' if flags != 1 else ''} for human "
                                 "review], listed on the Brief tab")
        else:
            st.markdown("No saved brief for this region yet.")
        regenerate_button()


# ---------------------------------------------------------------- header
names = sorted(counties.FULL, key=finnish_order)
h_brand, h_region, h_meta = st.columns([4, 2.4, 1.5], vertical_alignment="center")
with h_brand:
    st.markdown(f'<div class="lb-brand"><img src="{LOGO_URI}" width="28" height="28" alt="Lingonberry logo">'
                '<b>Lingonberry</b><span>Lung cancer care across Finland</span></div>', unsafe_allow_html=True)
with h_region:
    short = st.selectbox("Region", names, index=names.index("Kymenlaakso"), key="region",
                         help="21 wellbeing services counties and the City of Helsinki")
full = counties.FULL[short]
slug = counties.slug(short)
brief_doc, review_doc = load_brief(slug, mtime(BRIEFS / f"{slug}.json", BRIEFS / f"{slug}.review.json"))
with h_meta:
    brief_status(brief_doc, review_doc)

# ---------------------------------------------------------------- brief tab parts
# Limitations: the original wording, split into (bold lead, rest). The first three show by default (as in the
# design); the delay figure is read from the ledger. "Public aggregate data only" moved to the page footer.
LIMITATIONS = [
    ("Crude shares.", "Regional treatment shares are not adjusted for age or stage. "
                      "Stage at diagnosis is missing for about half of patients."),
    ("Preliminary:", f"the delay figures ({claims['mot:total_fi']['value']:.0f} days etc.) are from an "
                     "unpublished study via Yle MOT; national, not region-specific."),
    ("Our recommendations", "(:material/lightbulb:) are the team's own drafts, not yet reviewed by mentors; "
                            "each is cited together with its evidence."),
    ("Categories overlap.", "A patient can have several treatment types; shares never add up."),
    ("‘No treatment record’", "mixes untreated patients and treatment that was not recorded."),
    ("MDT codes", "measure recording practice, not whether a team reviewed the patient."),
    ("Age-adjusted values", "were read off a report figure (Kuva 16, ±0.5 pp), curative only, by sex."),
    ("Mentor insight:", "expert views without a written source."),
    ("Regional pathways:", "five regions' documents, read by a teammate."),
]
LIMITS_SHOWN = 3


def hero_chart(region: str, row: pd.Series, nat: float) -> alt.LayerChart:
    """Region vs Finland curative share: two bars, the region's Wilson 95% CI as a bracket, values at the end."""
    hi = float(row["ci_high"])
    track_end = max(40.0, -(-max(hi, nat) // 5) * 5)  # bar track, in % (0–40 as in the design, wider if needed)
    xmax = track_end * 1.3  # the right part holds the value labels, right-aligned at xmax (fits at 390px)
    d = pd.DataFrame({
        "who": [region, "Finland"], "share": [float(row["share"]), nat],
        "lo": [float(row["ci_low"]), None], "hi": [hi, None], "colour": [LINGON, FINLAND_GREY],
        "label": [f"{row['share']:.1f}%", f"{nat:.1f}%"], "end": [xmax, xmax], "track": [track_end, track_end]})
    y = alt.Y("who:N", sort=[region, "Finland"], title=None,
              axis=alt.Axis(domain=False, ticks=False, labelFontSize=14, labelColor="#1F1B1A", labelPadding=10,
                            labelLimit=140))
    xs = alt.Scale(domain=[0, xmax], nice=False)
    base = alt.Chart(d)
    tip = [alt.Tooltip("who:N", title="Region"), alt.Tooltip("share:Q", title="Curative %", format=".1f"),
           alt.Tooltip("lo:Q", title="95% CI low", format=".1f"), alt.Tooltip("hi:Q", title="95% CI high", format=".1f")]
    track = base.mark_bar(color=TRACK, size=14, cornerRadius=3).encode(
        y=y, x=alt.X("track:Q", scale=xs, axis=None))
    bars = base.mark_bar(size=14, cornerRadius=3).encode(
        y=y, x=alt.X("share:Q", scale=xs, axis=None), color=alt.Color("colour:N", scale=None), tooltip=tip)
    ci = base.transform_filter("isValid(datum.lo)")
    bracket = (ci.mark_rule(color="#1F1B1A", strokeWidth=1.5).encode(y=y, x=alt.X("lo:Q", scale=xs), x2="hi:Q")
               + ci.mark_tick(color="#1F1B1A", thickness=1.5, size=22, orient="vertical").encode(y=y, x="lo:Q")
               + ci.mark_tick(color="#1F1B1A", thickness=1.5, size=22, orient="vertical").encode(y=y, x="hi:Q"))
    labels = base.mark_text(align="right", fontSize=16, fontWeight=600, color="#1F1B1A").encode(
        y=y, x=alt.X("end:Q", scale=xs), text="label:N")
    return ((track + bars + bracket + labels).properties(height=90, background="transparent")
            .configure_view(strokeWidth=0, fill=None))


def hero(region: str, full_name: str) -> None:
    """Verdict headline (from vs_national) and the region-vs-Finland bar card."""
    row = region_measure(full_name, "Parantava")
    nat = round(float(row["national_share"]), 1)
    gap = round(float(row["share"]) - nat, 1)  # rounded national value, so the badge matches the bars
    verdict, colour = VERDICT[row["vs_national"]]
    left, right = st.columns([1.15, 1], gap="large", vertical_alignment="bottom")
    with left:
        st.markdown(f'<div class="lb-eyebrow">{region} · new patients 2019–2023</div>'
                    f'<div class="lb-verdict" role="heading" aria-level="1">{verdict}</div>'
                    '<div class="lb-lede">Shares are crude, not adjusted for age or stage. Read a gap as a signal '
                    'to investigate, not proof of worse care.</div>', unsafe_allow_html=True)
    with right, st.container(border=True, key="card-hero"):
        with st.container(horizontal=True, horizontal_alignment="distribute", vertical_alignment="center"):
            st.caption("Curative treatment share")
            st.badge(f"{signed_pp(gap)} vs Finland", color=colour)
        st.altair_chart(hero_chart(region, row, nat), width="stretch")
        reach = ("It overlaps the national value." if row["ci_contains_national"]
                 else "It doesn't reach the national value.")
        st.caption(f"The black bracket is the 95% confidence interval ({row['ci_low']:.1f}–{row['ci_high']:.1f}%). "
                   f"{reach} Source: report Taulukko 11 (region), Taulukko 6 (Finland).")


def national_context(region_slug: str) -> None:
    """The core message as one strip; its backing claims behind a toggle. Same on every region page; each part
    is backed by ledger claims (src/core_message.py)."""
    core_parts, core_problems = core_message.resolve(claims)
    with st.container(border=True, key="soft-context"):
        label, text, link = st.columns([1.1, 6, 1.5], vertical_alignment="top")
        label.markdown('<div class="lb-eyebrow" style="padding-top:3px">National context</div>',
                       unsafe_allow_html=True)
        with text:
            st.markdown(core_message.MESSAGE)
            n = len(unique(i for _, ids in core_parts for i in ids))
            if st.toggle(f"Show {n} sources", key=f"core-src-{region_slug}"):
                for i, (part, ids) in enumerate(core_parts):
                    st.caption(f"‘{part[:1].upper() + part[1:]}’: backed by")
                    claim_pills(ids, f"core-{region_slug}-{i}")
        link.button("See the pathway →", type="tertiary", key="go-pathway", on_click=go_to_tab,
                    args=("Pathway",))
        if core_problems:
            st.error("The core message is not fully backed by the ledger: " + "; ".join(core_problems))


def section_summary(section: str, sec: dict, full_name: str) -> str:
    """One-line expander summary, computed from the data (never model text)."""
    if section == "where_we_lag":
        r = region_measure(full_name, "Parantava")
        return f"Curative share {r['share']:.1f}% vs {r['national_share']:.1f}% nationally"
    if section == "how_sure_are_we":
        r = region_measure(full_name, "Ei hoitotietoa")
        return f"Recording check: no treatment record {r['share']:.1f}% vs {r['national_share']:.1f}% nationally"
    sents = [sec.get("headline") or {}] + (sec.get("details") or [])
    n = len({c for s in sents for c in s.get("claim_ids", []) if c.startswith("rec:")})
    return f"{n} recommended action{'s' if n != 1 else ''} (team drafts)"


def brief_sections(doc: dict, region_slug: str, full_name: str) -> None:
    """The three brief sections as expanders (first open). Sentences are shown verbatim; details and the claim
    pills sit behind toggles (no expander may be nested in another)."""
    for k, s in enumerate(SECTIONS):
        sec = doc.get(s) or {}
        head, details = sec.get("headline"), sec.get("details") or []
        label = f":gray[0{k + 1}]  **{TITLES[s]}** :gray[· {section_summary(s, sec, full_name)}]"
        with st.expander(label, expanded=k == 0):
            body = st.container()
            with st.container(horizontal=True, gap="medium"):
                show_details = bool(details) and st.toggle(
                    f"Show {len(details)} detail{'s' if len(details) != 1 else ''}", key=f"det-{region_slug}-{s}")
                shown = ([("h", head)] if head else []) + (
                    [(str(i), d) for i, d in enumerate(details)] if show_details else [])
                n = len(unique(c for _, x in shown for c in x["claim_ids"]))
                show_src = st.toggle(f"Show {n} sources", key=f"src-{region_slug}-{s}")
            with body:
                for j, (tag, x) in enumerate(shown):
                    if j:
                        st.divider()
                    st.markdown(x["text"])
                    if show_src:
                        claim_pills(x["claim_ids"], f"{region_slug}-{s}-{tag}")


def read_before_acting(region_slug: str) -> None:
    with st.container(border=True, key="soft-limits"):
        st.markdown("**Read before acting**")
        show_all = st.session_state.get(f"limits-{region_slug}", False)
        for lead, rest in LIMITATIONS if show_all else LIMITATIONS[:LIMITS_SHOWN]:
            st.markdown(f"**{lead}** {rest}")
        st.toggle(f"Show all {len(LIMITATIONS)}", key=f"limits-{region_slug}")
    with st.expander("Glossary: pp, CI, MDT, curative", icon=":material/menu_book:"):
        st.markdown("\n".join(f"- **{term}:** {text}" for term, text in GLOSSARY.items()))


# ---------------------------------------------------------------- compare tab parts
COMPARE = {  # segmented-control label -> (title, Taulukko 11 treatment type)
    "Curative": ("Curative treatment share, by region", "Parantava"),
    "No treatment record": ("Patients with no treatment record, by region", "Ei hoitotietoa"),
}


def dot_plot_html(rows: pd.DataFrame, selected: str, nat: float) -> str:
    """Ranked dot plot as HTML rows (styles in inject_css): point = crude share, line = Wilson 95% CI, dashed
    line = Finland. Dark grey = CI excludes Finland's value, light grey = it includes it."""
    top = max(50.0, -(-float(rows["ci_high"].max()) // 10) * 10)
    pos = lambda v: f"{float(v) / top * 100:.2f}%"  # noqa: E731
    out = []
    for r in rows.sort_values("share", ascending=False).itertuples():
        cls = "sel" if r.name == selected else ("unclear" if r.ci_contains_national else "clear")
        verdict = {"below": "below Finland", "above": "above Finland"}.get(r.vs_national, "not distinguishable")
        name = html.escape(r.name)
        out.append(
            f'<div class="lb-dp-row {cls}" title="{name}: {r.share:.1f}% (95% CI {r.ci_low:.1f}–{r.ci_high:.1f}), '
            f'{verdict}"><div class="lb-dp-name">{name}</div><div class="lb-dp-track">'
            f'<div class="lb-dp-nat" style="left:{pos(nat)}"></div>'
            f'<div class="lb-dp-ci" style="left:{pos(r.ci_low)};width:{pos(r.ci_high - r.ci_low)}"></div>'
            f'<div class="lb-dp-dot" style="left:{pos(r.share)}"></div></div>'
            f'<div class="lb-dp-val">{r.share:.1f}%</div></div>')
    ticks = "".join(f"<span>{t}{'%' if t in (0, int(top)) else ''}</span>" for t in range(0, int(top) + 1, 10))
    out.append(f'<div class="lb-dp-row lb-dp-axis"><div></div><div class="lb-dp-ticks">{ticks}</div><div></div></div>')
    return '<div class="lb-dp">' + "".join(out) + "</div>"


# ---------------------------------------------------------------- pathway tab parts
PATH_STAGE = "path-stage"  # session_state key: the stage whose evidence is shown
PATH_GROUPS = [("Patient delay", "mot:patient"), ("Primary care", "mot:primary"),
               ("Specialist care", "mot:specialist")]
MEASURED_ICON = {"yes": ":green[:material/check_circle:]", "partly": ":orange[:material/remove_circle:]",
                 "no": ":red[:material/cancel:]"}
MEASURED_LABEL = {"yes": "Measured", "partly": "Partly measured", "no": "Not measured"}
MEASURED_SHORT = {"yes": ":green[:material/check_circle: {n} measured]",
                  "partly": ":orange[:material/remove_circle: {n} partly]",
                  "no": ":red[:material/cancel: {n} not measured]"}


def pick_stage(stage: str) -> None:
    """Stage-button callback: show this stage's evidence."""
    st.session_state[PATH_STAGE] = stage


def stage_evidence(r) -> None:
    """One evidence panel for the selected pathway stage: 2–4 columns, only the sources that say something."""
    with st.container(border=True, key="card-evidence"):
        st.markdown(f"#### {r.stage}")
        st.markdown(f"{MEASURED[r.measured]} · by region: {r.by_county}")
        parts = [("Public data", f"{clean(r.report_note)}  \n*Source: report {r.report_source}*")]
        if r.regional_pathways:
            parts.append(("Regional pathways (read by a teammate)", clean(r.regional_pathways)))
        if r.policy:
            parts.append(("National policy", clean(r.policy)))
        if r.mentor_insight:
            parts.append(("Mentor insight", r.mentor_insight))
        for col, (label, text) in zip(st.columns(len(parts), gap="medium"), parts):
            col.markdown(f'<div class="lb-eyebrow">{label}</div>', unsafe_allow_html=True)
            col.markdown(text)


def nordic_chart() -> alt.Chart:
    """Symptoms to first treatment, Finland vs Sweden vs Denmark (MOT claims: preliminary)."""
    d = pd.DataFrame({"country": ["Finland", "Sweden", "Denmark"],
                      "days": [claims[f"mot:total_{c}"]["value"] for c in ("fi", "se", "dk")],
                      "colour": [LINGON, FINLAND_GREY, FINLAND_GREY]})
    d["label"] = d["days"].map(lambda v: f"{v:.0f} days")
    top = float(d["days"].max()) * 1.3  # right part holds the labels
    y = alt.Y("country:N", sort=None, title=None,
              axis=alt.Axis(domain=False, ticks=False, labelFontSize=14, labelColor="#1F1B1A", labelPadding=10))
    xs = alt.Scale(domain=[0, top], nice=False)
    bars = alt.Chart(d).mark_bar(size=12, cornerRadius=3).encode(
        y=y, x=alt.X("days:Q", scale=xs, axis=None), color=alt.Color("colour:N", scale=None),
        tooltip=[alt.Tooltip("country:N", title="Country"), alt.Tooltip("days:Q", title="Mean days")])
    labels = alt.Chart(d.assign(end=top)).mark_text(align="right", fontSize=14, color="#1F1B1A").encode(
        y=y, x=alt.X("end:Q", scale=xs), text="label:N")
    return ((bars + labels).properties(height=110, background="transparent")
            .configure_view(strokeWidth=0, fill=None))


# ---------------------------------------------------------------- verification tab parts
CHECK_STATE = {"ok": ":green[:material/check_circle: {result}]", "warn": ":orange[:material/flag: {result}]",
               "fail": ":red[:material/cancel: {result}]", "na": ":gray[:material/remove: {result}]"}
METHOD_COLOURS = {"computed": LINGON, "quoted": "#D67A85", "assessed": "#8A817B", "digitised": FINLAND_GREY,
                  "mentor": "#C58A2A", "proposed": "#5A524D"}


def method_bar(methods: pd.Series) -> alt.Chart:
    """All ledger claims as one stacked bar, by method (legend drawn in HTML so it wraps on phones)."""
    d = methods.rename_axis("method").reset_index(name="claims")
    d["order"] = range(len(d))
    d["colour"] = d["method"].map(lambda m: METHOD_COLOURS.get(m, FINLAND_GREY))
    return alt.Chart(d).mark_bar(size=14, stroke="#FFFFFF", strokeWidth=2).encode(
        x=alt.X("sum(claims):Q", stack="zero", axis=None, scale=alt.Scale(nice=False)),
        color=alt.Color("colour:N", scale=None), order=alt.Order("order:Q"),
        tooltip=[alt.Tooltip("method:N", title="Method"), alt.Tooltip("claims:Q", title="Claims")],
    ).properties(height=24, background="transparent").configure_view(strokeWidth=0, fill=None)


# ---------------------------------------------------------------- where to start, where to go next
NEXT_STEP = {  # tab -> (button label, destination tab); the last tab leads back to the Brief
    "Brief": ("Next: Compare regions — how does this region rank?", "Compare regions"),
    "Compare regions": ("Next: Pathway — which steps can public data see?", "Pathway"),
    "Pathway": ("Next: How we verified this — where does each number come from?", "How we verified this"),
    "How we verified this": ("Back to the Brief", "Brief"),
}


def next_step(tab: str) -> None:
    """Quiet link-style button at the bottom of a tab that switches to the next one."""
    label, dest = NEXT_STEP[tab]
    back = dest == "Brief"
    with st.container(horizontal=True, horizontal_alignment="right"):
        st.button(label, type="tertiary", key=f"next-{TAB_LABELS.index(tab)}", on_click=go_to_tab, args=(dest,),
                  icon=":material/arrow_back:" if back else ":material/arrow_forward:",
                  icon_position="left" if back else "right")


st.caption("Start with the **Brief**: it is the summary. The other tabs hold the data behind it.")

# Stateful tabs (key + on_change): st.session_state[NAV] holds the active label, so a button can switch tabs.
NAV = "nav"
TAB_LABELS = ["Brief", "Compare regions", "Pathway", "How we verified this"]
tab_brief, tab_chart, tab_path, tab_verify = st.tabs(TAB_LABELS, key=NAV, on_change="rerun")

# ---------------------------------------------------------------- brief
with tab_brief:
    hero(short, full)
    national_context(slug)
    left, right = st.columns([2.2, 1], gap="large")
    with left:
        if not brief_doc or not brief_doc.get("brief"):
            st.info(f"No saved brief for {short}."
                    + (" Use **Regenerate with Gemini** in the brief menu at the top." if GEMINI_CONFIGURED
                       else ""))
        else:
            if brief_doc["status"] != "validated":
                st.warning("This brief is a **DRAFT**: it failed validation after a retry. "
                           "Problems are listed under *How we verified this → Technical details*.")
            brief_sections(brief_doc["brief"], slug, full)
            if review_doc and review_doc["flags"]:
                flagged_for_review(review_doc, brief_doc["brief"])
    with right:
        read_before_acting(slug)
    next_step("Brief")

# ---------------------------------------------------------------- chart
with tab_chart:
    head, controls = st.columns([3, 2], gap="large", vertical_alignment="bottom")
    with controls:
        measure = st.segmented_control("Measure", list(COMPARE), default="Curative", required=True,
                                       key="cmp-measure", label_visibility="collapsed")
        only_differ = st.toggle("Only regions that clearly differ from Finland", key="cmp-differ",
                                help="Regions whose 95% confidence interval does not include Finland's value.")
    title, treatment = COMPARE[measure]
    rows = cty[cty["treatment"] == treatment].assign(name=lambda t: t["county"].map(counties.SHORT))
    nat = float(rows["national_share"].iloc[0])
    if only_differ:
        rows = rows[~rows["ci_contains_national"] | (rows["county"] == full)]
    with head:
        st.subheader(title)
        st.caption(f"Ranked, with 95% confidence intervals. The dashed line is Finland ({nat:.1f}%). "
                   f"Showing {len(rows)} of {len(cty['county'].unique())} regions.")
    with st.container(border=True, key="card-dotplot"):
        st.markdown(dot_plot_html(rows, short, nat), unsafe_allow_html=True)
    st.markdown('<div class="lb-legend"><span><i class="sel"></i>Selected region</span>'
                '<span><i class="clear"></i>Clearly differs from Finland</span>'
                '<span><i class="unclear"></i>Not distinguishable</span></div>', unsafe_allow_html=True)
    st.caption("Crude shares, not adjusted for age or stage. Treatment categories overlap. ‘No treatment record’ "
               "mixes untreated patients and treatment that was not recorded. Source: report Taulukko 11 "
               "(regions), Taulukko 5–6 (national); CIs computed in src/add_ci.py.")
    with st.expander(f"{short}: all treatment measures vs Finland"):
        sel = cty[cty["county"] == full][["treatment", "share", "ci_low", "ci_high", "national_share",
                                          "vs_national", "n", "total"]].copy()
        sel["treatment"] = sel["treatment"].map({
            "Parantava": "Curative", "Jarruttava": "Life-prolonging", "Oireenmukainen": "Symptomatic",
            "Ei hoitotietoa": "No treatment record", "MDT-käsittely": "MDT meeting recorded"})
        st.dataframe(sel.rename(columns={"treatment": "Measure", "share": "Region %", "ci_low": "95% CI low",
                                         "ci_high": "95% CI high", "national_share": "Finland %",
                                         "vs_national": "vs Finland", "n": "Patients", "total": "All patients"}),
                     hide_index=True, width="stretch",
                     column_config={"Finland %": st.column_config.NumberColumn(format="%.1f")})
    next_step("Compare regions")

# ---------------------------------------------------------------- pathway
with tab_path:
    counts = bs["measured"].value_counts()
    st.subheader("Public data sees only part of the pathway")
    st.markdown(f"Of {len(bs)} steps from symptoms to treatment: "
                f"{MEASURED_SHORT['yes'].format(n=counts.get('yes', 0))}, "
                f"{MEASURED_SHORT['partly'].format(n=counts.get('partly', 0))}, "
                f"{MEASURED_SHORT['no'].format(n=counts.get('no', 0))}. Select a step for the evidence.")
    if PATH_STAGE not in st.session_state or st.session_state[PATH_STAGE] not in set(bs["stage"]):
        measured = bs[bs["measured"] == "yes"]["stage"]
        st.session_state[PATH_STAGE] = measured.iloc[0] if len(measured) else bs["stage"].iloc[0]
    # Equal widths: stages stack vertically inside each group, so weighting by stage count only squeezed
    # the one-stage "Patient delay" column (words broke mid-word at 1440px).
    cols = st.columns(len(PATH_GROUPS), gap="small")
    for col, (group, cid) in zip(cols, PATH_GROUPS):
        with col:
            days = claims[cid]["value"]
            st.markdown(f"**{group}** :orange-badge[:material/hourglass_top: {days:.0f} days · preliminary]")
            for r in bs[bs["mot_interval"] == group].itertuples():
                chosen = r.stage == st.session_state[PATH_STAGE]
                st.button(f"{MEASURED_ICON[r.measured]} {r.stage}", key=f"stage{'sel' if chosen else ''}-{r.Index}",
                          width="stretch", on_click=pick_stage, args=(r.stage,),
                          help=MEASURED_LABEL[r.measured])
    stage_evidence(bs[bs["stage"] == st.session_state[PATH_STAGE]].iloc[0])
    with st.container(border=True, key="soft-nordic"):
        with st.container(horizontal=True, horizontal_alignment="distribute", vertical_alignment="center"):
            st.markdown("**Symptoms to first treatment**")
            st.markdown(":orange[:material/hourglass_top: Preliminary · Yle MOT 2025, unpublished]")
        st.altair_chart(nordic_chart(), width="stretch")
    st.caption("Delays are mean days from the MOT study: **preliminary, unpublished**, national averages (not "
               "region-specific). Which pathway steps fall in which MOT interval is the team's assumption. "
               "Measured status: src/build_blind_spots.py, from the 2019–2023 report.")
    next_step("Pathway")

# ---------------------------------------------------------------- verification
with tab_verify:
    st.subheader("Every number traces to a source")
    st.markdown("Every number and quote in the brief is a row in the claim ledger (`data/ledger.sqlite`) with its "
                "source, location, method and status. Gap figures are computed in our own code, never by a model.")
    df = pd.DataFrame(list(claims.values()))
    snap = load_snapshot(mtime(SNAPSHOT)) if not RAW_PRESENT else None

    # Results first (each computed once), then three summary cards, then the details.
    if RAW_PRESENT:
        code, out = run_check_claims(mtime(ledger.DB, "docs/source_verification.md", "docs/recommendations.md",
                                           "docs/blind_spots.md"))
        ledger_ok, ledger_when = code == 0, "Run now on this server."
    elif snap is None:
        code, out, ledger_ok, ledger_when = None, "", None, "No source documents or snapshot on this server."
    else:
        code, out = snap["check_claims"]["exit_code"], snap["check_claims"]["output"]
        ledger_ok, ledger_when = snap["check_claims"]["passed"], f"Last verified locally on {snapshot_time(snap)}."
    has_brief = bool(brief_doc and brief_doc.get("brief"))
    # validate_brief needs only the committed ledger, so it can always be re-run here.
    live = (validate(brief_doc["brief"], set(brief_doc.get("provided_claim_ids") or []) or None, claims)
            if has_brief else [])
    n_flags = len(review_doc["flags"]) if review_doc else None

    cards = [
        ("Ledger check", "ok" if ledger_ok else ("na" if ledger_ok is None else "fail"),
         "All checks passed" if ledger_ok else ("Not available" if ledger_ok is None else "Checks failed"),
         ledger_when),
        (f"Brief check · {short}", "na" if not has_brief else ("fail" if live else "ok"),
         "No saved brief" if not has_brief else (f"{len(live)} problem(s)" if live else "Valid now"),
         "Re-checked live against the committed ledger."),
        ("Second-model review", "na" if n_flags is None else ("warn" if n_flags else "ok"),
         "Not run" if n_flags is None else f"{n_flags} flag{'s' if n_flags != 1 else ''}",
         "Flags go to a person; they never change the brief."),
    ]
    for i, (col, (name, state, result, detail)) in enumerate(zip(st.columns(3, gap="small"), cards)):
        with col, st.container(border=True, key=f"card-check-{i}"):
            st.caption(name)
            st.markdown(f"#### {CHECK_STATE[state].format(result=result)}")
            st.caption(detail)

    with st.container(border=True, key="card-methods"):
        with st.container(horizontal=True, horizontal_alignment="distribute", vertical_alignment="center"):
            st.markdown(f"**{len(df)} claims in the ledger, by method**")
            st.caption("`data/ledger.sqlite`")
        methods = df["method"].value_counts()
        st.altair_chart(method_bar(methods), width="stretch")
        st.markdown('<div class="lb-legend">' + "".join(
            f'<span><i style="background:{METHOD_COLOURS.get(m, FINLAND_GREY)};border-radius:2px"></i>'
            f"{html.escape(m)} <b>{n}</b></span>" for m, n in methods.items()) + "</div>", unsafe_allow_html=True)

    with st.expander("Technical details: scripts, snapshot, raw responses", icon=":material/terminal:"):
        st.markdown("**Ledger check** (`src/check_claims.py`)")
        st.caption("Every claim has a source and location; every quote is re-found verbatim in its source; "
                   "every quote has an explicit language; superseded claims name their replacement.")
        if RAW_PRESENT:
            st.markdown(":green[:material/check_circle: All checks passed] (run now)" if code == 0
                        else ":red[:material/cancel: Checks failed] (run now)")
        elif snap is None:
            st.warning("The source documents are not on this server and no verification snapshot was found.")
        else:
            st.markdown((":green[:material/check_circle: All checks passed]" if snap["check_claims"]["passed"]
                         else ":red[:material/cancel: Checks failed]")
                        + f" · **last verified locally on {snapshot_time(snap)}**")
            snapshot_note(snap)
        if out and st.toggle("Show check output", key="check-output"):
            st.code(out, language=None)

        st.divider()
        st.markdown("**Claims by status**")
        counts = df["status"].value_counts().reindex(ledger.STATUSES, fill_value=0).reset_index()
        counts.columns = ["status", "claims"]
        st.altair_chart(alt.Chart(counts).mark_bar(color=LINGON, cornerRadiusEnd=4).encode(
            x=alt.X("claims:Q", title="Claims"), y=alt.Y("status:N", sort=list(ledger.STATUSES), title=None),
            tooltip=["status", "claims"]).properties(height=200, background="transparent"), width="stretch")
        st.caption("Briefs may cite only: " + ", ".join(ledger.CITABLE) + ".")

        st.divider()
        st.markdown(f"**Brief check for {short}** (`src/validate_brief.py`)")
        if not has_brief:
            st.caption("No saved brief to validate.")
        else:
            if snap is not None:
                rec = snap["validate_brief"].get(short) or {}
                st.markdown((":green[:material/check_circle: Valid]" if rec.get("valid")
                             else f":red[:material/cancel: {len(rec.get('problems', []))} problem(s)]")
                            + f" · last verified locally on {snapshot_time(snap)}")
                for p in rec.get("problems", []):
                    st.markdown(f"- {p}")
            if not live:
                st.markdown(":green[:material/check_circle: Valid now]: re-checked against the committed ledger. "
                            "Every sentence cites existing, citable claims, and every number matches its cited "
                            "claims.")
            else:
                st.markdown(f":red[:material/cancel: {len(live)} problem(s) against the current ledger]")
                for p in live:
                    st.markdown(f"- {p}")
            st.caption(f"At generation: {brief_doc['status']} after {brief_doc['attempts']} attempt(s); "
                       f"{len(brief_doc['problems'])} problem(s) remaining. Raw model responses: "
                       + ", ".join(f"`{Path(p).name}`" for p in brief_doc.get("raw_responses", [])))
            if review_doc:
                st.caption(f"Code rules (overclaiming words, future tense about plans): "
                           f"{len(review_doc['rule_problems'])} problem(s). Model review: {n_flags} flag(s) for "
                           "human review (see the Brief tab); flags never approve or change a brief.")
    next_step("How we verified this")

# ---------------------------------------------------------------- footer
st.divider()
foot_left, foot_right = st.columns(2)
foot_left.caption("Source: Finnish Cancer Registry, Keuhkosyöpä Suomessa 2019–2023")
with foot_right, st.container(key="foot-right"):
    st.caption("Public aggregate data only · no patient-level data · Junction 2026")
