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
    theme cannot: card borders, the header row, the tab look and the dot-plot rows. Layout follows
    design/Lingonberry Redesign v2.dc.html. Cards are containers with a key starting "card" (Streamlit
    turns a key into the CSS class st-key-<key>); "soft" cards use the warmer panel colour."""
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
.st-key-region [data-testid="stWidgetLabel"] {margin: 0; min-height: 0; color: #6F6762;}
[class*="st-key-meta"] button {border-radius: 999px;}
.st-key-meta-ok button {background: #F1F8F2; border-color: #CFE3D4; color: #1F6A36;}
.st-key-meta-draft button {background: #FDF4E7; border-color: #EBCF9F; color: #8A5A12;}
/* Tabs: active tab in ink, not red; the red underline stays */
[data-testid="stTab"][aria-selected="true"] p {color: #1F1B1A; font-weight: 600;}
/* Small type */
.lb-eyebrow {font-family: ui-monospace, "SFMono-Regular", Consolas, monospace; font-size: 12px; letter-spacing: .06em;
  text-transform: uppercase; color: #8A817B;}
/* Footer: right part right-aligned only when the columns sit side by side */
@media (min-width: 640px) {.st-key-foot-right {text-align: right;}}
</style>""", unsafe_allow_html=True)


inject_css()

import base64  # noqa: E402
import hashlib  # noqa: E402
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
HIGHLIGHT, OTHER, INK2 = "#2a78d6", "#b4b2ab", "#52514e"


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


def claim_card(cid: str) -> None:
    c = claims.get(cid)
    with st.container(border=True):
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
    """Model review flags, shown apart from the validated text. They never change the brief."""
    st.divider()
    with st.container(border=True):
        n = len(review["flags"])
        st.subheader(f":material/flag: Flagged for human review ({n})")
        st.caption("Not part of the validated brief. A second model (gemini-4-hydrogen) read each sentence "
                   "against its cited claims and raised these for a person to check. Flags never approve, "
                   "reject or change the brief.")
        if not n:
            st.markdown(":green[:material/check: Nothing flagged]")
        order = {"high": 0, "medium": 1, "low": 2}
        for f in sorted(review["flags"], key=lambda f: order.get(f["severity"], 3)):
            colour, icon = SEVERITY.get(f["severity"], ("gray", ":material/help:"))
            with st.container(border=True):
                st.badge(f["severity"].capitalize(), color=colour, icon=icon)
                st.markdown(f"**{flag_place(f['location'])}**")
                if f.get("sentence") and f["sentence"] != "-":
                    st.markdown(f"> {f['sentence']}")
                st.markdown(f["problem"])


def sentence(s: dict, key: str, headline: bool = False) -> None:
    st.markdown(f"**{s['text']}**" if headline else s["text"])
    picked = st.pills("Claims", s["claim_ids"], key=key, format_func=short_id,
                      label_visibility="collapsed", selection_mode="single")
    if picked:
        claim_card(picked)


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

# Core message: the same on every region page; each part backed by ledger claims (src/core_message.py).
core_parts, core_problems = core_message.resolve(claims)
with st.container(border=True):
    st.markdown(f"#### {core_message.MESSAGE}")
    cols = st.columns(len(core_parts), gap="medium")
    for i, (col, (part, ids)) in enumerate(zip(cols, core_parts)):
        with col:
            st.caption(f"‘{part[:1].upper() + part[1:]}’: backed by")
            picked = st.pills(f"core-{i}", ids, key=f"core-{slug}-{i}", format_func=short_id,
                              label_visibility="collapsed", selection_mode="single")
            if picked:
                claim_card(picked)
    if core_problems:
        st.error("The core message is not fully backed by the ledger: " + "; ".join(core_problems))

# Stateful tabs (key + on_change): st.session_state[NAV] holds the active label, so a button can switch tabs.
NAV = "nav"
TAB_LABELS = ["Brief", "Compare regions", "Pathway", "How we verified this"]
tab_brief, tab_chart, tab_path, tab_verify = st.tabs(TAB_LABELS, key=NAV, on_change="rerun")

# ---------------------------------------------------------------- brief
with tab_brief:
    left, right = st.columns([2.2, 1], gap="large")
    with left:
        if not brief_doc or not brief_doc.get("brief"):
            st.info(f"No saved brief for {short}."
                    + (" Use **Regenerate with Gemini** in the brief menu at the top." if GEMINI_CONFIGURED
                       else ""))
        else:
            if brief_doc["status"] != "validated":
                st.warning("This brief is a **DRAFT**: it failed validation after a retry. "
                           "Problems are listed under *How we verified this*.")
            st.caption("Every sentence cites claims from the ledger. Click a claim to see its source.")
            for s in SECTIONS:
                sec = brief_doc["brief"].get(s) or {}
                with st.container(border=True):
                    st.subheader(TITLES[s])
                    if sec.get("headline"):
                        sentence(sec["headline"], f"{slug}-{s}-h", headline=True)
                    with st.expander("Details", icon=":material/expand_content:"):
                        for i, d in enumerate(sec.get("details") or []):
                            sentence(d, f"{slug}-{s}-{i}")
                            if i < len(sec["details"]) - 1:
                                st.divider()
            if review_doc:
                flagged_for_review(review_doc, brief_doc["brief"])
    with right:
        with st.container(border=True):
            st.subheader(":material/info: Limitations")
            st.markdown(
                "- **Crude shares.** Regional treatment shares are not adjusted for age or stage. "
                "Stage at diagnosis is missing for about half of patients.\n"
                "- **Categories overlap.** A patient can have several treatment types; shares never add up.\n"
                "- **‘No treatment record’** mixes untreated patients and treatment that was not recorded.\n"
                "- **MDT codes** measure recording practice, not whether a team reviewed the patient.\n"
                "- **Age-adjusted values** were read off a report figure (Kuva 16, ±0.5 pp), curative only, by sex.\n"
                "- **Preliminary:** the delay figures (155 days etc.) are from an unpublished study via Yle MOT; "
                "national, not region-specific.\n"
                "- **Mentor insight:** expert views without a written source.\n"
                "- **Regional pathways:** five regions' documents, read by a teammate.\n"
                "- **Our recommendations** (:material/lightbulb:) are the team's own drafts, not yet reviewed "
                "by mentors; each is cited together with its evidence.\n"
                "- Public aggregate data only; no patient-level data.")

# ---------------------------------------------------------------- chart
with tab_chart:
    cty = ct[ct["level"] == "county"]
    x = cty[cty["treatment"] == "Ei hoitotietoa"].set_index("county")
    y = cty[cty["treatment"] == "Parantava"].set_index("county")
    d = pd.DataFrame({
        "county": [counties.SHORT.get(c, c) for c in x.index],
        "no_record": x["share"], "no_record_lo": x["ci_low"], "no_record_hi": x["ci_high"],
        "curative": y.loc[x.index, "share"], "curative_lo": y.loc[x.index, "ci_low"],
        "curative_hi": y.loc[x.index, "ci_high"], "patients": x["total"].astype(int),
    }).reset_index(drop=True)
    d["selected"] = d["county"] == short
    nat_x, nat_y = float(x["national_share"].iloc[0]), float(y["national_share"].iloc[0])

    colour = alt.condition("datum.selected", alt.value(HIGHLIGHT), alt.value(OTHER))
    base = alt.Chart(d)
    xs = alt.Scale(domain=[10, 50])
    ys = alt.Scale(domain=[14, 42])
    tooltip = [alt.Tooltip("county:N", title="Region"),
               alt.Tooltip("curative:Q", title="Curative %", format=".1f"),
               alt.Tooltip("curative_lo:Q", title="  95% CI low", format=".1f"),
               alt.Tooltip("curative_hi:Q", title="  95% CI high", format=".1f"),
               alt.Tooltip("no_record:Q", title="No treatment record %", format=".1f"),
               alt.Tooltip("no_record_lo:Q", title="  95% CI low", format=".1f"),
               alt.Tooltip("no_record_hi:Q", title="  95% CI high", format=".1f"),
               alt.Tooltip("patients:Q", title="New patients 2019–2023")]
    ebx = base.mark_rule(strokeWidth=1.2).encode(x=alt.X("no_record_lo:Q", scale=xs), x2="no_record_hi:Q",
                                                 y="curative:Q", color=colour, opacity=alt.value(0.7))
    eby = base.mark_rule(strokeWidth=1.2).encode(x="no_record:Q", y=alt.Y("curative_lo:Q", scale=ys),
                                                 y2="curative_hi:Q", color=colour, opacity=alt.value(0.7))
    pts = base.mark_circle(stroke="white", strokeWidth=1.5, opacity=1).encode(
        x=alt.X("no_record:Q", scale=xs, title="No treatment record within 12 months (%)"),
        y=alt.Y("curative:Q", scale=ys, title="Received curative treatment (%)"),
        color=colour, size=alt.condition("datum.selected", alt.value(220), alt.value(70)), tooltip=tooltip)
    labels = (
        base.transform_filter("!datum.selected").mark_text(align="left", dx=8, dy=-6, fontSize=11, color=INK2)
        .encode(x="no_record:Q", y="curative:Q", text="county:N")
        + base.transform_filter("datum.selected").mark_text(align="left", dx=10, dy=-8, fontSize=13,
                                                            fontWeight="bold", color="#0b0b0b")
        .encode(x="no_record:Q", y="curative:Q", text="county:N")
    )
    hline = alt.Chart(pd.DataFrame({"y": [nat_y]})).mark_rule(strokeDash=[6, 4], color=INK2).encode(y="y:Q")
    vline = alt.Chart(pd.DataFrame({"x": [nat_x]})).mark_rule(strokeDash=[2, 4], color=OTHER).encode(x="x:Q")
    chart = (ebx + eby + hline + vline + pts + labels).properties(height=560).configure_axis(
        grid=True, gridColor="#e1e0d9", domainColor="#c3c2b7", labelColor=INK2, titleColor=INK2
    ).configure_view(strokeWidth=0)
    st.subheader("Curative treatment vs no treatment record, all 22 regions")
    st.caption(f"Bars: Wilson 95% confidence intervals. Dashed lines: Finland, {nat_y:.1f}% curative and "
               f"{nat_x:.1f}% with no treatment record. {short} is highlighted.")
    st.altair_chart(chart, width="stretch")
    st.caption("Crude shares, not adjusted for age or stage. Treatment categories overlap, so the two axes are "
               "not parts of one whole. ‘No treatment record’ mixes untreated patients and treatment that was not "
               "recorded. Source: report Taulukko 11 (regions), Taulukko 5–6 (national); CIs computed in src/add_ci.py.")
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

# ---------------------------------------------------------------- pathway
with tab_path:
    st.subheader("Which steps of the lung cancer pathway can public data see?")
    st.caption("From symptoms to treatment. Delays are mean days from the MOT study: **preliminary, unpublished**, "
               "national averages (not region-specific).")
    groups =[("Patient delay", "mot:patient"), ("Primary care", "mot:primary"), ("Specialist care", "mot:specialist")]
    # Equal widths: stages stack vertically inside each group, so weighting by stage count only squeezed
    # the one-stage "Patient delay" column (words broke mid-word at 1440px).
    cols = st.columns(len(groups), gap="small")
    for col, (group, cid) in zip(cols, groups):
        with col, st.container(border=True):
            days = claims[cid]["value"]
            st.markdown(f"**{group}**  \n:orange-badge[:material/hourglass_top: {days:.0f} days · preliminary]")
            for r in bs[bs["mot_interval"] == group].itertuples():
                with st.container(border=True):
                    st.markdown(f"**{r.stage}**  \n{MEASURED[r.measured]}")
                    st.caption(f"By region: {r.by_county}")
                    with st.popover("Evidence", icon=":material/search:", width="stretch"):
                        st.markdown(f"**Public data:** {clean(r.report_note)}  \n*Source: report {r.report_source}*")
                        if r.regional_pathways:
                            st.markdown(f"**Regional pathways** (read by a teammate): {clean(r.regional_pathways)}")
                        if r.policy:
                            st.markdown(f"**National policy:** {clean(r.policy)}")
                        if r.mentor_insight:
                            st.markdown(f"**Mentor insight:** {r.mentor_insight}")
    tot = claims["mot:total_fi"]["value"]
    st.markdown(f":orange-badge[:material/hourglass_top: Preliminary] Symptoms to first treatment: **{tot:.0f} days** "
                f"in Finland vs {claims['mot:total_se']['value']:.0f} in Sweden and "
                f"{claims['mot:total_dk']['value']:.0f} in Denmark (Yle MOT 2025, unpublished study).")
    st.caption("Which pathway steps fall in which MOT interval is the team's assumption. Measured status: "
               "src/build_blind_spots.py, from the 2019–2023 report.")

# ---------------------------------------------------------------- verification
with tab_verify:
    st.subheader("How we verified this")
    st.markdown("Every number and quote in the brief is a row in the claim ledger (`data/ledger.sqlite`) with its "
                "source, location, method and status. Gap figures are computed in our own code, never by a model.")
    c1, c2 = st.columns(2, gap="large")
    df = pd.DataFrame(list(claims.values()))
    with c1, st.container(border=True):
        st.markdown("**Claims by status**")
        counts = df["status"].value_counts().reindex(ledger.STATUSES, fill_value=0).reset_index()
        counts.columns = ["status", "claims"]
        st.altair_chart(alt.Chart(counts).mark_bar(color=HIGHLIGHT, cornerRadiusEnd=4).encode(
            x=alt.X("claims:Q", title="Claims"), y=alt.Y("status:N", sort=list(ledger.STATUSES), title=None),
            tooltip=["status", "claims"]).properties(height=200), width="stretch")
        by_method = df["method"].value_counts()
        st.caption("By method: " + " · ".join(f"{k} {v}" for k, v in by_method.items()))
        st.caption("Briefs may cite only: " + ", ".join(ledger.CITABLE) + ".")
    snap = load_snapshot(mtime(SNAPSHOT)) if not RAW_PRESENT else None
    with c2, st.container(border=True):
        st.markdown("**Ledger check** (`src/check_claims.py`)")
        st.caption("Every claim has a source and location; every quote is re-found verbatim in its source; "
                   "every quote has an explicit language; superseded claims name their replacement.")
        if RAW_PRESENT:
            code, out = run_check_claims(mtime(ledger.DB, "docs/source_verification.md", "docs/recommendations.md",
                                               "docs/blind_spots.md"))
            st.markdown(":green[:material/check_circle: All checks passed] (run now)" if code == 0
                        else ":red[:material/cancel: Checks failed] (run now)")
        elif snap is None:
            code, out = None, ""
            st.warning("The source documents are not on this server and no verification snapshot was found.")
        else:
            code, out = snap["check_claims"]["exit_code"], snap["check_claims"]["output"]
            st.markdown((":green[:material/check_circle: All checks passed]" if snap["check_claims"]["passed"]
                         else ":red[:material/cancel: Checks failed]")
                        + f" · **last verified locally on {snapshot_time(snap)}**")
            snapshot_note(snap)
        if out:
            with st.expander("Output"):
                st.code(out, language=None)

    with st.container(border=True):
        st.markdown(f"**Brief check for {short}** (`src/validate_brief.py`)")
        if not brief_doc or not brief_doc.get("brief"):
            st.caption("No saved brief to validate.")
        else:
            if snap is not None:
                rec = snap["validate_brief"].get(short) or {}
                st.markdown((":green[:material/check_circle: Valid]" if rec.get("valid")
                             else f":red[:material/cancel: {len(rec.get('problems', []))} problem(s)]")
                            + f" · last verified locally on {snapshot_time(snap)}")
                for p in rec.get("problems", []):
                    st.markdown(f"- {p}")
            # validate_brief needs only the committed ledger, so it can always be re-run here as well.
            live = validate(brief_doc["brief"], set(brief_doc.get("provided_claim_ids") or []) or None, claims)
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
                n = len(review_doc["flags"])
                st.caption(f"Code rules (overclaiming words, future tense about plans): "
                           f"{len(review_doc['rule_problems'])} problem(s). Model review: {n} flag(s) for "
                           "human review (see the Brief tab); flags never approve or change a brief.")

# ---------------------------------------------------------------- footer
st.divider()
foot_left, foot_right = st.columns(2)
foot_left.caption("Source: Finnish Cancer Registry, Keuhkosyöpä Suomessa 2019–2023")
with foot_right, st.container(key="foot-right"):
    st.caption("Public aggregate data only · no patient-level data · Junction 2026")
