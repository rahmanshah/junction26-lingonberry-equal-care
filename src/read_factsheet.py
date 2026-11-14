"""Read all HTML tables from the 2019–2023 lung cancer report into CSV files."""
from pathlib import Path

import pandas as pd

URL = "data/raw/keuhkosyoparaportti_2019_2023.html"

tables = pd.read_html(URL)
print(f"{len(tables)} tables found")

out = Path("data/processed/factsheet")
out.mkdir(parents=True, exist_ok=True)

for i, t in enumerate(tables):
    print(i, t.shape, list(t.columns)[:6])
    t.to_csv(out / f"table_{i:02d}.csv", index=False, encoding="utf-8")

print("Saved to", out)