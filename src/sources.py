"""Local source texts for quote checking.

Each source is split into *units* with a location label:
  PDF  -> one unit per page, labelled with the PRINTED page ("p.33"), or "PDF p.7 (unnumbered)";
          each page is searched in three renderings (full text, left+right columns, table cells),
          plus page pairs ("p.17–18") for quotes that run across a page break.
  HTML -> the lung cancer report, one unit per section heading ("§3.3 Menetelmät").
  MD   -> one unit per "## " section of a Markdown file.

Quotes are matched after normalisation: Unicode NFC, soft hyphens and hyphens removed, footnote
markers glued to words removed, Markdown emphasis removed, and ALL whitespace removed. This makes the
match insensitive to line breaks and hyphenation, but still verbatim in letters, digits and case.
A quote containing "…" is split into fragments that must all occur in the same unit.

Extracted text is cached in data/cache/ (gitignored), keyed by the source file's MD5.
"""
from __future__ import annotations

import hashlib
import json
import logging
import re
import unicodedata
from pathlib import Path

logging.getLogger("pdfminer").setLevel(logging.ERROR)

CACHE = Path("data/cache")

# path -> (kind, printed page = PDF page - offset)
SOURCES: dict[str, tuple[str, int]] = {
    "data/raw/keuhkosyoparaportti_2019_2023.html": ("html", 0),
    "data/raw/strategy_2026_2035_fi.pdf": ("pdf", 0),
    "data/raw/roadmap_2026_2031_fi.pdf": ("pdf", 0),
    "data/raw/filha_lung_programme_2026_fi.pdf": ("pdf", 9),
    "docs/pathway_brief.md": ("md", 0),
}
# Pages before this PDF index have no printed number.
FIRST_NUMBERED = {"data/raw/strategy_2026_2035_fi.pdf": 3, "data/raw/roadmap_2026_2031_fi.pdf": 2,
                  "data/raw/filha_lung_programme_2026_fi.pdf": 10}

# Footnote markers glued to a word or closing bracket, e.g. "Kræftpakkeforløb53," or "(SVF)54 ".
_FOOTNOTE = re.compile(r"(?:(?<=[^\W\d_])|(?<=\)))\d{1,2}(?=[\s,.;:)]|$)")
_DROP = re.compile(r"[\s­\-‐‑*`]+")


def normalise(text: str) -> str:
    text = unicodedata.normalize("NFC", text)
    text = text.replace("“", '"').replace("”", '"').replace("’", "'")
    text = _FOOTNOTE.sub("", text)
    return _DROP.sub("", text)


def _md5(path: Path) -> str:
    return hashlib.md5(path.read_bytes()).hexdigest()


def _page_label(src: str, pdf_index: int) -> str:
    offset = SOURCES[src][1]
    if pdf_index < FIRST_NUMBERED.get(src, 1):
        return f"PDF p.{pdf_index} (unnumbered)"
    return f"p.{pdf_index - offset}"


def _extract_pdf(src: str) -> list[dict]:
    import pdfplumber

    units = []
    with pdfplumber.open(src) as pdf:
        for i, page in enumerate(pdf.pages, start=1):
            w, h = page.width, page.height
            full = page.extract_text() or ""
            cols = " ".join((page.crop(box).extract_text() or "")
                            for box in ((0, 0, w / 2, h), (w / 2, 0, w, h)))
            cells = " ".join(c for t in page.extract_tables() for row in t for c in row if c)
            units.append({"label": _page_label(src, i), "variants": [full, cols, cells]})
    return units


def _extract_html(src: str) -> list[dict]:
    from lxml import html

    tree = html.parse(src)
    units, label, buf = [], "front matter", []
    for el in tree.iter("h2", "h3", "h4", "p", "figcaption"):
        text = " ".join(el.text_content().split())
        if el.tag in ("h2", "h3", "h4"):
            units.append({"label": label, "variants": [" ".join(buf)]})
            label, buf = f"§{text}", []
        else:
            buf.append(text)
    units.append({"label": label, "variants": [" ".join(buf)]})
    return units


def _extract_md(src: str) -> list[dict]:
    units, label, buf = [], "top", []
    for line in Path(src).read_text(encoding="utf-8").splitlines():
        if line.startswith("## "):
            units.append({"label": label, "variants": ["\n".join(buf)]})
            label, buf = line[3:].strip(), []
        else:
            buf.append(line)
    units.append({"label": label, "variants": ["\n".join(buf)]})
    return units


def units(src: str) -> list[dict]:
    """Units of a source, with normalised variants. Cached by MD5."""
    if src not in SOURCES:
        raise KeyError(f"Unknown source: {src}")
    path = Path(src)
    if not path.exists():
        raise FileNotFoundError(src)
    kind = SOURCES[src][0]
    if kind == "md":  # small and edited often: never cache
        raw = _extract_md(src)
    else:
        CACHE.mkdir(parents=True, exist_ok=True)
        cache = CACHE / (path.name + ".json")
        digest = _md5(path)
        if cache.exists():
            data = json.loads(cache.read_text(encoding="utf-8"))
            if data.get("md5") == digest:
                return data["units"]
        raw = _extract_pdf(src) if kind == "pdf" else _extract_html(src)
    out = [{"label": u["label"], "norm": [normalise(v) for v in u["variants"]]} for u in raw]
    if kind == "pdf":  # page pairs for quotes crossing a page break (full-text rendering)
        for a, b in zip(raw, raw[1:]):
            pair = f"{a['label']}–{b['label'].removeprefix('p.')}"
            out.append({"label": pair, "norm": [normalise(a["variants"][0] + " " + b["variants"][0])]})
    if kind != "md":
        cache.write_text(json.dumps({"md5": digest, "units": out}, ensure_ascii=False), encoding="utf-8")
    return out


def fragments(quote: str) -> list[str]:
    parts = re.split(r"…|\.\.\.", quote)
    return [normalise(p) for p in parts if normalise(p)]


def find(src: str, quote: str) -> list[str]:
    """Labels of all units containing the quote. Single pages are preferred over page pairs."""
    frags = fragments(quote)
    if not frags:
        return []
    hits = [u["label"] for u in units(src)
            if any(all(f in v for f in frags) for v in u["norm"])]
    singles = [h for h in hits if "–" not in h or SOURCES[src][0] != "pdf"]
    return singles or hits


def find_anywhere(quote: str, prefer: list[str] | None = None) -> tuple[str | None, list[str]]:
    """First source (preferred ones first) that contains the quote, and the matching labels."""
    order = list(prefer or []) + [s for s in SOURCES if s not in (prefer or [])]
    for src in order:
        if not Path(src).exists():
            continue
        labels = find(src, quote)
        if labels:
            return src, labels
    return None, []
