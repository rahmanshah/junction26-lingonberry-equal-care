import pandas as pd

df = pd.read_csv("data/processed/factsheet/table_10.csv")
# Merged cells come through as blanks: fill them downwards
df[["Hoitomuoto", "Yhteistyöalue"]] = df[["Hoitomuoto", "Yhteistyöalue"]].ffill()

print(df.head(12).to_string())
print("\nTreatment types:", df["Hoitomuoto"].unique())
print("\nCounties:", df["Hyvinvointialue"].nunique())
print(df["Hyvinvointialue"].unique())