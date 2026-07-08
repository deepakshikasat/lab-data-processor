import pandas as pd
from pathlib import Path

root = Path(__file__).resolve().parents[1]
df = pd.read_csv(root / "data/plate_reader.csv")
neg = df[df.role == "negative_control"].absorbance
pos = df[df.role == "positive_control"].absorbance
z_factor = 1 - 3 * (neg.std() + pos.std()) / abs(neg.mean() - pos.mean())
cv = df[df.role == "sample"].groupby(["compound", "dose_uM"]).absorbance.agg(["mean", "std"])
cv["cv_percent"] = 100 * cv["std"] / cv["mean"]
cv.to_csv(root / "outputs/replicate_cv.csv")
pd.DataFrame({"metric": ["z_factor", "median_cv_percent"], "value": [z_factor, cv.cv_percent.median()]}).to_csv(root / "outputs/qc_summary.csv", index=False)
print(f"Z-factor: {z_factor:.2f}")
