"""Scatter: curative-treatment share vs share with no treatment record, one dot per county.

Reads data/processed/county_treatment.csv (run src/add_ci.py first).
Writes outputs/curative_vs_missing.png.

Error bars are Wilson 95% CIs on both axes. Shares are crude (not adjusted for age
or stage). Treatment categories overlap, so x and y are not parts of one whole.
"""
from pathlib import Path

import matplotlib

matplotlib.use("Agg")
import matplotlib.pyplot as plt
import pandas as pd

SRC = Path("data/processed/county_treatment.csv")
OUT = Path("outputs/curative_vs_missing.png")

# Reference palette (light): chart chrome + first three categorical slots.
SURFACE, INK, INK2, MUTED = "#fcfcfb", "#0b0b0b", "#52514e", "#898781"
GRID, AXIS, OTHER = "#e1e0d9", "#c3c2b7", "#b4b2ab"
HIGHLIGHT = {
    "Kymenlaakson hyvinvointialue": "#2a78d6",
    "Etelä-Karjalan hyvinvointialue": "#eb6834",
    "Varsinais-Suomen hyvinvointialue": "#1baf7a",
}

SHORT = {
    "Etelä-Karjalan hyvinvointialue": "Etelä-Karjala",
    "Helsingin kaupunki": "Helsinki",
    "Itä-Uudenmaan hyvinvointialue": "Itä-Uusimaa",
    "Keski-Uudenmaan hyvinvointialue": "Keski-Uusimaa",
    "Kymenlaakson hyvinvointialue": "Kymenlaakso",
    "Länsi-Uudenmaan hyvinvointialue": "Länsi-Uusimaa",
    "Päijät-Hämeen hyvinvointialue": "Päijät-Häme",
    "Vantaan ja Keravan hyvinvointialue": "Vantaa ja Kerava",
    "Etelä-Savon hyvinvointialue": "Etelä-Savo",
    "Keski-Suomen hyvinvointialue": "Keski-Suomi",
    "Pohjois-Karjalan hyvinvointialue": "Pohjois-Karjala",
    "Pohjois-Savon hyvinvointialue": "Pohjois-Savo",
    "Pohjanmaan hyvinvointialue": "Pohjanmaa",
    "Satakunnan hyvinvointialue": "Satakunta",
    "Varsinais-Suomen hyvinvointialue": "Varsinais-Suomi",
    "Kainuun hyvinvointialue": "Kainuu",
    "Keski-Pohjanmaan hyvinvointialue": "Keski-Pohjanmaa",
    "Lapin hyvinvointialue": "Lappi",
    "Pohjois-Pohjanmaan hyvinvointialue": "Pohjois-Pohjanmaa",
    "Etelä-Pohjanmaan hyvinvointialue": "Etelä-Pohjanmaa",
    "Kanta-Hämeen hyvinvointialue": "Kanta-Häme",
    "Pirkanmaan hyvinvointialue": "Pirkanmaa",
}

# Label offsets in points (dx, dy, horizontal alignment), tuned by eye to avoid collisions.
DEFAULT_OFFSET = (7, 3, "left")
OFFSETS: dict[str, tuple[int, int, str]] = {
    "Etelä-Savon hyvinvointialue": (-6, -8, "right"),
    "Pohjois-Pohjanmaan hyvinvointialue": (6, 7, "left"),
}

df = pd.read_csv(SRC)
cty = df[df["level"] == "county"]
cols = ["county", "share", "ci_low", "ci_high", "national_share"]
x = cty[cty["treatment"] == "Ei hoitotietoa"][cols].set_index("county")
y = cty[cty["treatment"] == "Parantava"][cols].set_index("county")
d = x.merge(y, left_index=True, right_index=True, suffixes=("_x", "_y"))
assert len(d) == 22 and set(d.index) == set(SHORT), "Expected the 22 wellbeing services counties"
nat_x, nat_y = d["national_share_x"].iloc[0], d["national_share_y"].iloc[0]

plt.rcParams.update({"font.family": ["Segoe UI", "DejaVu Sans"], "font.size": 10})
fig, ax = plt.subplots(figsize=(10, 7.2), dpi=200)
fig.patch.set_facecolor(SURFACE)
ax.set_facecolor(SURFACE)

# National reference lines
ax.axhline(nat_y, color=INK2, lw=1.2, ls=(0, (5, 3)), zorder=1)
ax.axvline(nat_x, color=AXIS, lw=1, ls=(0, (2, 3)), zorder=1)

order = [c for c in d.index if c not in HIGHLIGHT] + list(HIGHLIGHT)  # highlights on top
for c in order:
    r = d.loc[c]
    hi = c in HIGHLIGHT
    colour = HIGHLIGHT.get(c, OTHER)
    ax.errorbar(
        r["share_x"], r["share_y"],
        xerr=[[r["share_x"] - r["ci_low_x"]], [r["ci_high_x"] - r["share_x"]]],
        yerr=[[r["share_y"] - r["ci_low_y"]], [r["ci_high_y"] - r["share_y"]]],
        fmt="none", ecolor=colour, elinewidth=1.4 if hi else 1, alpha=0.9 if hi else 0.7,
        capsize=0, zorder=3 if hi else 2,
    )
    ax.scatter(
        r["share_x"], r["share_y"], s=70 if hi else 42, color=colour,
        edgecolor=SURFACE, linewidth=1.5, zorder=5 if hi else 4,
    )
    dx, dy, ha = OFFSETS.get(c, DEFAULT_OFFSET)
    ax.annotate(
        SHORT[c], (r["share_x"], r["share_y"]), xytext=(dx, dy), textcoords="offset points",
        ha=ha, va="center", fontsize=9.5 if hi else 8.5,
        color=INK if hi else INK2, fontweight="bold" if hi else "normal", zorder=6,
        bbox=dict(boxstyle="round,pad=0.15", fc=SURFACE, ec="none", alpha=0.85),
    )

# Reference-line labels (text ink, not series colour)
xmin, xmax = 10, 50
ax.text(xmax - 0.3, nat_y + 0.35, f"Finland: {nat_y:.1f}% received curative treatment",
        ha="right", va="bottom", fontsize=8.5, color=INK2)
ax.text(nat_x + 0.3, 14.3, f"Finland: {nat_x:.1f}%\nno record", ha="left", va="bottom",
        fontsize=8, color=MUTED)

ax.set_xlim(xmin, xmax)
ax.set_ylim(14, 42)
ax.set_xlabel("No treatment record within 12 months (%)", color=INK2, labelpad=8)
ax.set_ylabel("Received curative treatment (%)", color=INK2, labelpad=8)
ax.grid(True, color=GRID, lw=0.6, zorder=0)
ax.set_axisbelow(True)
for side in ("top", "right"):
    ax.spines[side].set_visible(False)
for side in ("left", "bottom"):
    ax.spines[side].set_color(AXIS)
ax.tick_params(colors=MUTED, labelcolor=INK2, length=0, pad=6)

fig.text(0.07, 0.965, "Curative treatment vs no treatment record, by wellbeing services county",
         fontsize=14, fontweight="bold", color=INK, ha="left")
fig.text(0.07, 0.932,
         "New lung cancer patients 2019–2023, 12-month follow-up. Bars: Wilson 95% confidence intervals.",
         fontsize=9.5, color=INK2, ha="left")
fig.text(0.07, 0.02,
         "Crude shares, not adjusted for age or stage. Categories overlap (a patient can have several), so the axes are not "
         "parts of one whole.\n'No treatment record' mixes untreated patients and treatment that was not recorded in HILMO.  "
         "Source: Keuhkosyöpä Suomessa 2019–2023, Taulukko 11 (county), Taulukko 5–6 (national).",
         fontsize=7.5, color=MUTED, ha="left", va="bottom", linespacing=1.5)
fig.subplots_adjust(left=0.07, right=0.97, top=0.9, bottom=0.14)

OUT.parent.mkdir(parents=True, exist_ok=True)
fig.savefig(OUT, facecolor=SURFACE)
print("Saved", OUT)
