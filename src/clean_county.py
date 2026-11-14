"""Turn table 10 (treatment type by county) into a tidy, checked dataset."""
from pathlib import Path

import pandas as pd

SRC = Path("data/processed/factsheet/table_10.csv")
OUT = Path("data/processed/county_treatment.csv")

raw = pd.read_csv(SRC)
print("Columns:", list(raw.columns))

df = raw.rename(columns={
    "Hoitomuoto": "treatment",
    "Yhteistyöalue": "area",
    "Hyvinvointialue": "county",
    "Lukumäärä": "n",
    "Yhteensä": "total",
    "Osuus (%)": "share",
})[["treatment", "area", "county", "n", "total", "share"]]

df[["treatment", "area"]] = df[["treatment", "area"]].ffill()


def to_num(s):
    return pd.to_numeric(
        s.astype(str).str.replace("\u00a0", "").str.replace(" ", "").str.replace(",", "."),
        errors="coerce",
    )


for c in ["n", "total", "share"]:
    df[c] = to_num(df[c])


def level(row):
    if row["county"] == row["treatment"] or row["area"] == row["treatment"]:
        return "national"
    if row["county"] == row["area"]:
        return "area"
    return "county"


df["level"] = df.apply(level, axis=1)
print(df["level"].value_counts())

# Check: does n / total reproduce the printed share?
df["share_check"] = (df["n"] / df["total"] * 100).round(1)
bad = df[(df["share_check"] - df["share"]).abs() > 0.15]
print(f"Rows where n/total does not match the printed share: {len(bad)}")
if len(bad):
    print(bad.to_string())

df.to_csv(OUT, index=False, encoding="utf-8")
print("Saved", OUT)

county = df[df["level"] == "county"]
print("\nTreatment types:", county["treatment"].unique())
print("Counties:", county["county"].nunique())

wide = county.pivot_table(index="county", columns="treatment", values="share")
print("\nShare (%) by county and treatment type:")
print(wide.round(1).sort_index().to_string())