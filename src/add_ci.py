"""Add Wilson 95% confidence intervals to county_treatment.csv and compare with national.

- Fills in the 4 counties that have no MDT row in Taulukko 11 as n = 0
  (area subtotals show these are zero counts, not suppressed cells; see docs/definitions.md).
- National reference values are taken from the report's own national tables:
  Taulukko 6 (table_05.csv) for Parantava / Jarruttava / Oireenmukainen,
  Taulukko 5 (table_04.csv) for MDT-käsittely and Ei hoitotietoa
  (= all patients minus patients with any lung cancer procedure).
- ci_contains_national: True when the county's 95% CI includes the national share,
  i.e. the county cannot be distinguished from the national value at this precision.

Run after src/clean_county.py. Safe to re-run.
"""
from math import sqrt
from pathlib import Path

import pandas as pd

PATH = Path("data/processed/county_treatment.csv")
T5 = Path("data/processed/factsheet/table_04.csv")  # report Taulukko 5
T6 = Path("data/processed/factsheet/table_05.csv")  # report Taulukko 6
Z = 1.959963984540054  # two-sided 95%
ZERO_NOTE = "0 records reported"
ADDED_COLS = ["note", "ci_low", "ci_high", "national_share", "ci_contains_national", "vs_national"]


def wilson(n: float, total: float, z: float = Z) -> tuple[float, float]:
    """Wilson score interval for a binomial proportion, returned in percent."""
    if total <= 0:
        return float("nan"), float("nan")
    p = n / total
    denom = 1 + z**2 / total
    centre = (p + z**2 / (2 * total)) / denom
    half = z * sqrt(p * (1 - p) / total + z**2 / (4 * total**2)) / denom
    return max(0.0, centre - half) * 100, min(1.0, centre + half) * 100


def total_row(path: Path) -> pd.Series:
    t = pd.read_csv(path, header=[0, 1])
    first = t.columns[0]
    row = t[t[first].astype(str).str.strip() == "Yhteensä"]
    assert len(row) == 1, f"No unique 'Yhteensä' row in {path}"
    return row.iloc[0]


def national_counts() -> dict[str, tuple[int, int]]:
    t5, t6 = total_row(T5), total_row(T6)
    all_pat = int(t6[("Potilaita yhteensä", "Lukumäärä")])
    assert all_pat == int(t5[("Potilaita yhteensä", "Lukumäärä")])
    any_proc = int(t5[("Keuhkosyöpä- toimenpide", "Lukumäärä")])
    return {
        "Parantava": (int(t6[("Parantava hoito", "Lukumäärä")]), all_pat),
        "Jarruttava": (int(t6[("Jarruttava hoito", "Lukumäärä")]), all_pat),
        "Oireenmukainen": (int(t6[("Oireenmukainen hoito", "Lukumäärä")]), all_pat),
        "Ei hoitotietoa": (all_pat - any_proc, all_pat),
        "MDT-käsittely": (int(t5[("MDT-käsittely", "Lukumäärä")]), all_pat),
    }


df = pd.read_csv(PATH)
# Make re-runs idempotent: remove anything this script added before.
if "note" in df.columns:
    df = df[df["note"] != ZERO_NOTE]
df = df.drop(columns=[c for c in ADDED_COLS if c in df.columns])
df["note"] = ""

# --- Fill missing MDT rows with n = 0 ---------------------------------------
county = df[df["level"] == "county"]
denoms = county[county["treatment"] == "Parantava"][["area", "county", "total"]]
have_mdt = set(county.loc[county["treatment"] == "MDT-käsittely", "county"])
missing = denoms[~denoms["county"].isin(have_mdt)].copy()
missing.insert(0, "treatment", "MDT-käsittely")
missing = missing.assign(n=0.0, share=0.0, level="county", share_check=0.0, note=ZERO_NOTE)
print("Added MDT n = 0 rows for:", sorted(missing["county"]))
df = pd.concat([df, missing], ignore_index=True)

# Area subtotal must equal the sum of its counties for every treatment type.
c = df[df["level"] == "county"].groupby(["treatment", "area"])[["n", "total"]].sum()
a = df[df["level"] == "area"].set_index(["treatment", "area"])[["n", "total"]]
assert (c.sort_index() == a.sort_index()).all().all(), "County rows do not add up to area subtotals"

# --- Wilson CIs and comparison with national --------------------------------
ci = df.apply(lambda r: wilson(r["n"], r["total"]), axis=1, result_type="expand")
df["ci_low"], df["ci_high"] = ci[0].round(2), ci[1].round(2)

nat = national_counts()
nat_share = {k: round(n / tot * 100, 2) for k, (n, tot) in nat.items()}
print("National shares (%):", nat_share)
df["national_share"] = df["treatment"].map(nat_share)
df["ci_contains_national"] = (df["ci_low"] <= df["national_share"]) & (df["national_share"] <= df["ci_high"])
df["vs_national"] = "not distinguishable"
df.loc[df["ci_high"] < df["national_share"], "vs_national"] = "below"
df.loc[df["ci_low"] > df["national_share"], "vs_national"] = "above"

order = {t: i for i, t in enumerate(["Parantava", "Jarruttava", "Oireenmukainen", "Ei hoitotietoa", "MDT-käsittely"])}
lvl = {"county": 0, "area": 1}
df = df.sort_values(
    ["treatment", "area", "level", "county"],
    key=lambda s: s.map(order) if s.name == "treatment" else (s.map(lvl) if s.name == "level" else s),
).reset_index(drop=True)
df.to_csv(PATH, index=False, encoding="utf-8")
print("Saved", PATH, df.shape)

# --- Summary -----------------------------------------------------------------
cty = df[df["level"] == "county"]
print("\nCounties per treatment type:", cty.groupby("treatment").size().to_dict())
summary = cty.pivot_table(index="treatment", columns="vs_national", values="county", aggfunc="count", fill_value=0)
print("\nCounties vs national (95% Wilson CI):")
print(summary.reindex(order.keys()).to_string())
for t in order:
    s = cty[cty["treatment"] == t]
    print(f"\n{t}  (national {nat_share[t]}%)")
    for _, r in s.sort_values("share").iterrows():
        print(f"  {r['county']:<38} {r['share']:5.1f}  [{r['ci_low']:5.1f}, {r['ci_high']:5.1f}]  {r['vs_national']}")
