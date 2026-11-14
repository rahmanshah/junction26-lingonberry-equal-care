"""Digitise curative (Parantava) age-adjusted shares from Kuva 16 for selected counties.

Kuva 16 in the report is a PNG only (no embedded data, see docs/chart_data.md). This script
reads the image straight from the saved report (read-only), calibrates the x-axis from the
plot's own gridlines (0, 10, ..., 60 %), and measures, per county row:
  - value:   centre of the dot
  - ci_low / ci_high: ends of the CI bar at the bar's centre line (blank if hidden by the dot)
and the dashed national reference line for each panel.

All numbers are read by our own code from pixels. No LLM is involved.
Output: data/processed/kuva16_curative_digitised.csv
QA image: outputs/qa_kuva16_curative.png (marks what was measured; check it by eye).
"""
import base64
import io
import re
from pathlib import Path

import numpy as np
import pandas as pd
from lxml import html
from PIL import Image, ImageDraw

SRC = Path("data/raw/keuhkosyoparaportti_2019_2023.html")
OUT = Path("data/processed/kuva16_curative_digitised.csv")
QA = Path("outputs/qa_kuva16_curative.png")

METHOD = "digitised from Kuva 16"
PRECISION_PP = 0.5
NATIONAL = "Koko maa (national reference line)"
TARGETS = [
    "Kymenlaakson hyvinvointialue",
    "Etelä-Karjalan hyvinvointialue",
    "Varsinais-Suomen hyvinvointialue",
]

# Row order in Kuva 16, top to bottom (as printed on the figure's y-axis; 22 rows).
ROWS = [
    # Etelä-Suomen yhteistyöalue
    "Vantaan ja Keravan hyvinvointialue", "Päijät-Hämeen hyvinvointialue",
    "Länsi-Uudenmaan hyvinvointialue", "Kymenlaakson hyvinvointialue",
    "Keski-Uudenmaan hyvinvointialue", "Itä-Uudenmaan hyvinvointialue",
    "Helsingin kaupunki", "Etelä-Karjalan hyvinvointialue",
    # Itä-Suomen yhteistyöalue
    "Pohjois-Savon hyvinvointialue", "Pohjois-Karjalan hyvinvointialue",
    "Keski-Suomen hyvinvointialue", "Etelä-Savon hyvinvointialue",
    # Länsi-Suomen yhteistyöalue
    "Varsinais-Suomen hyvinvointialue", "Satakunnan hyvinvointialue", "Pohjanmaan hyvinvointialue",
    # Pohjois-Suomen yhteistyöalue
    "Pohjois-Pohjanmaan hyvinvointialue", "Lapin hyvinvointialue",
    "Keski-Pohjanmaan hyvinvointialue", "Kainuun hyvinvointialue",
    # Sisä-Suomen yhteistyöalue
    "Pirkanmaan hyvinvointialue", "Kanta-Hämeen hyvinvointialue", "Etelä-Pohjanmaan hyvinvointialue",
]

# Panels: (sex, x-range of the panel's plot area). Column 1 = Mies/Parantava, column 4 = Nainen/Parantava.
PANELS = {"men": (360, 560), "women": (1045, 1245)}
GRID = (235, 235, 235)        # ggplot panel gridline colour
CURATIVE = (0, 119, 175)      # Parantava series colour


def load_kuva16() -> np.ndarray:
    tree = html.parse(str(SRC))
    for cap in tree.xpath("//figcaption"):
        if re.match(r"Kuva 16:", " ".join(cap.text_content().split())):
            src = cap.getparent().xpath(".//img")[0].get("src")
            data = base64.b64decode(src.split(",", 1)[1])
            return np.array(Image.open(io.BytesIO(data)).convert("RGB")).astype(float)
    raise SystemExit("Kuva 16 not found")


def runs(mask: np.ndarray) -> list[tuple[int, int]]:
    """Start/end indices (inclusive) of consecutive True runs."""
    out, start = [], None
    for i, v in enumerate(mask):
        if v and start is None:
            start = i
        if not v and start is not None:
            out.append((start, i - 1))
            start = None
    if start is not None:
        out.append((start, len(mask) - 1))
    return out


def is_colour(px: np.ndarray, rgb: tuple[int, int, int], tol: float = 4) -> np.ndarray:
    return (np.abs(px - np.array(rgb)).max(axis=-1) <= tol)


def calibrate(im: np.ndarray, x0: int, x1: int, y_probe: int) -> tuple[float, float]:
    """Fit pixel -> percent from the 7 vertical gridlines (0..60 by 10) on a blank scan line."""
    line = is_colour(im[y_probe, x0:x1], GRID)
    centres = [x0 + (a + b) / 2 for a, b in runs(line)]
    assert len(centres) == 7, f"Expected 7 gridlines, found {len(centres)}: {centres}"
    widths = [b - a + 1 for a, b in runs(line)]
    assert min(widths[0::2]) >= max(widths[1::2]), f"Major (0,20,40,60) gridlines should be widest: {widths}"
    slope, intercept = np.polyfit(centres, np.arange(0, 70, 10), 1)
    resid = np.abs(np.polyval([slope, intercept], centres) - np.arange(0, 70, 10)).max()
    # Gridlines are snapped to whole pixels by the renderer (spacing 27.5-29.5 px), so allow ~1 px.
    assert resid < 0.4, f"Gridlines not evenly spaced (max residual {resid:.2f} pp)"
    return slope, intercept


def row_centres(im: np.ndarray, x0: int, x1: int) -> list[float]:
    """y-centres of the 22 category rows = horizontal gridlines in the first block column."""
    # A horizontal gridline is a y where most of the panel width is not white (grey line, or a
    # CI bar drawn over it; bars are centred on their gridline so the run centre is unchanged).
    # Header rules and black x-axis lines are also non-white; keep runs that are partly grey.
    sub = im[:, x0 + 15:x1 - 15]
    frac = (sub.min(axis=-1) < 250).mean(axis=1)
    grey = is_colour(sub, GRID).mean(axis=1)
    ys = [(a + b) / 2 for a, b in runs(frac > 0.5) if grey[a:b + 1].max() > 0.3]
    assert len(ys) == 22, f"Expected 22 row gridlines, found {len(ys)}"
    return ys


def curative_alpha(px: np.ndarray) -> np.ndarray:
    """Per-pixel coverage of the curative blue (handles anti-aliasing against white/grey/black)."""
    a = (px[..., 2] - px[..., 0]) / (CURATIVE[2] - CURATIVE[0])
    return np.clip(a, 0, 1)


def edge(profile: np.ndarray, from_left: bool) -> float | None:
    """Sub-pixel position where coverage crosses 0.5 at the outer end of the mark."""
    idx = np.where(profile >= 0.5)[0]
    if not len(idx):
        return None
    i = idx[0] if from_left else idx[-1]
    j = i - 1 if from_left else i + 1
    if 0 <= j < len(profile):
        a, b = profile[j], profile[i]
        frac = (0.5 - a) / (b - a) if b != a else 0
        return j + frac * (i - j)                  # 0.5-coverage crossing between pixel centres
    return float(i)


def measure_row(im, x0, x1, yc, half_h=14):
    ys = slice(int(yc - half_h), int(yc + half_h) + 1)
    alpha = curative_alpha(im[ys, x0:x1])
    if alpha.sum() < 20:
        return None
    height = alpha.sum(axis=0)                     # vertical coverage per column
    dot_d = height.max()                           # the dot is a circle: tallest column = diameter
    # Centre: midpoint of the chord at 60% of the diameter. The CI bar is thinner than that
    # (~35% of the dot), so it does not shift the chord; a circle's chord is symmetric.
    chord = np.where(height >= 0.6 * dot_d)[0]
    centre_x = x0 + (chord.min() + chord.max()) / 2
    # Bar centre line: the y with the widest blue run
    widest = np.argmax((alpha >= 0.5).sum(axis=1))
    line = alpha[widest]
    left, right = x0 + edge(line, True), x0 + edge(line, False)
    # The CI is readable only if the bar sticks out of the dot on both sides (> 1.5 px).
    r = dot_d / 2
    ci_readable = left < centre_x - r - 1.5 and right > centre_x + r + 1.5
    return {
        "centre_px": centre_x, "left_px": left if ci_readable else None,
        "right_px": right if ci_readable else None,
        "y_px": int(yc - half_h) + widest, "dot_d": dot_d,
    }


def national_line(im, x0, x1, y_top, y_bot):
    """x of the dashed black line: the interior column with the most black pixels (spine excluded)."""
    black = (im[y_top:y_bot, x0:x1].max(axis=-1) < 60)
    counts = black.sum(axis=0)
    counts[:10] = 0                                 # drop the left axis spine
    best = counts.max()
    cols = np.where(counts >= best * 0.8)[0]
    assert cols.max() - cols.min() <= 2, f"Dashed line not unique: {cols + x0}"
    return x0 + cols.mean()


im = load_kuva16()
records, marks = [], []
for sex, (x0, x1) in PANELS.items():
    slope, intercept = calibrate(im, x0, x1, y_probe=160)
    to_pct = lambda px: float(np.polyval([slope, intercept], px))
    ys = row_centres(im, x0, x1)
    nat_px = national_line(im, x0, x1, int(ys[0]) - 40, int(ys[7]) + 40)
    records.append({"county": NATIONAL, "sex": sex, "value": round(to_pct(nat_px), 1),
                    "ci_low": None, "ci_high": None, "note": "dashed national line in this sex's Parantava panel"})
    marks.append(("nat", nat_px, ys[0] - 40, ys[7] + 40))
    for county in TARGETS:
        yc = ys[ROWS.index(county)]
        m = measure_row(im, x0, x1, yc)
        assert m is not None, f"No curative mark for {county} ({sex})"
        rec = {"county": county, "sex": sex, "value": round(to_pct(m["centre_px"]), 1)}
        if m["left_px"] is not None:
            rec.update(ci_low=round(to_pct(m["left_px"]), 1), ci_high=round(to_pct(m["right_px"]), 1),
                       note="")
        else:
            half = (m["dot_d"] / 2) * slope        # dot radius in pp (slope = pp per px)
            rec.update(ci_low=None, ci_high=None,
                       note=f"CI bar hidden inside the dot (half-width < ~{half:.1f} pp)")
        records.append(rec)
        marks.append(("dot", m, county, sex))

df = pd.DataFrame(records)
df["method"] = METHOD
df["precision_pp"] = PRECISION_PP
df = df[["county", "sex", "value", "ci_low", "ci_high", "method", "precision_pp", "note"]]
OUT.parent.mkdir(parents=True, exist_ok=True)
df.to_csv(OUT, index=False, encoding="utf-8")
print(df.to_string(index=False))
print("Saved", OUT)

# Comparison with the national reference line of the same panel
print()
for county in TARGETS:
    parts = []
    for sex in PANELS:
        r = df[(df.county == county) & (df.sex == sex)].iloc[0]
        nat = df[(df.county == NATIONAL) & (df.sex == sex)].iloc[0]["value"]
        # Upper CI bound: read from the bar, or (bar hidden) at most the dot's right edge.
        hidden = pd.isna(r.ci_high)
        upper = r.value + float(re.search(r"< ~([\d.]+)", r.note).group(1)) if hidden else r.ci_high
        if upper + PRECISION_PP < nat:
            verdict = "below, CI excludes national" + (f" (CI hidden in dot, upper <= {upper:.1f})" if hidden else "")
        elif r.value < nat:
            verdict = "below point estimate, CI overlaps national"
        else:
            verdict = "not below"
        parts.append(f"{sex}: {r.value} vs {nat} -> {verdict}")
    print(f"{county}: " + "; ".join(parts))

# QA overlay
img = Image.fromarray(im.astype("uint8"))
draw = ImageDraw.Draw(img)
for mk in marks:
    if mk[0] == "nat":
        _, x, y0, y1 = mk
        draw.line([(x, y0), (x, y1)], fill=(255, 0, 255), width=1)
    else:
        _, m, county, sex = mk
        y = m["y_px"]
        draw.line([(m["centre_px"], y - 12), (m["centre_px"], y + 12)], fill=(255, 0, 0), width=1)
        for k in ("left_px", "right_px"):
            if m[k] is not None:
                draw.line([(m[k], y - 8), (m[k], y + 8)], fill=(255, 140, 0), width=1)
QA.parent.mkdir(parents=True, exist_ok=True)
img.save(QA)
print("QA overlay:", QA)
