"""
Heatmap: how do the five countries compare with what is expected for their income?
Rows = the five countries; columns = health spending, child survival, sanitation, schooling.
Orange = more / better than expected for the income; purple = less / worse; grey = no data.

Packages: pandas, numpy, matplotlib
Data (Our World in Data CSVs in data/): life-expectancy, GDP per capita (Maddison),
annual-healthcare-expenditure-per-capita, child-mortality,
share-of-population-with-improved-sanitation-*, mean-years-of-schooling-long-run.
Run from the repository root:  python visual_heatmap_factors.py
"""

from pathlib import Path

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from matplotlib.colors import LinearSegmentedColormap

DATA, OUT = Path("data"), Path("figures")
YEAR, SCHOOL_YEAR = 2022, 2020
EXCLUDE = ["Central African Republic", "North Korea", "Syria", "Palestine"]
FIVE = ["Cuba", "Nicaragua", "Bangladesh", "Lebanon", "Cape Verde"]


def read_owid(file, name):
    df = pd.read_csv(DATA / file).iloc[:, :4]
    df.columns = ["country", "code", "year", name]
    return df[df["code"].notna() & ~df["code"].astype(str).str.startswith("OWID")]


def one_year(df, name, year):
    return df[df["year"] == year][["country", name]]


# ---- 1. The 161 countries and the income trend --------------------------------
life = read_owid("life-expectancy.csv", "life_exp")
gdp = read_owid("gdp-per-capita-maddison-project-database.csv", "gdp_pc")
d = one_year(life, "life_exp", YEAR).merge(one_year(gdp, "gdp_pc", YEAR), on="country")
d = d[(d["gdp_pc"] > 0) & ~d["country"].isin(EXCLUDE)].dropna()

sanitation_file = sorted(DATA.glob("share-of-population-with-improved-sanitation*.csv"))[0].name
factors = {
    "hx": read_owid("annual-healthcare-expenditure-per-capita.csv", "hx"),
    "cm": read_owid("child-mortality.csv", "cm"),
    "san": read_owid(sanitation_file, "san"),
    "sch": read_owid("mean-years-of-schooling-long-run.csv", "sch"),
}
years = {"hx": YEAR, "cm": YEAR, "san": YEAR, "sch": SCHOOL_YEAR}
for key, df in factors.items():
    d = d.merge(one_year(df, key, years[key]), on="country", how="left")


# ---- 2. For each factor: value minus what is expected for the income ----------
def vs_income(df, col, log=False):
    sub = df.dropna(subset=[col])
    sub = sub[sub[col] > 0] if log else sub
    y = np.log10(sub[col]) if log else sub[col]
    b, a = np.polyfit(np.log10(sub["gdp_pc"]), y, 1)
    diff = y - (a + b * np.log10(sub["gdp_pc"]))
    return diff.reindex(df.index)  # NaN where no data


diff = pd.DataFrame({
    "hx": vs_income(d, "hx", log=True),        # log ratio: >0 = spends more than peers
    "cm": -vs_income(d, "cm", log=True),       # sign flipped: >0 = FEWER child deaths than peers
    "san": vs_income(d, "san"),                # >0 = better sanitation than peers
    "sch": vs_income(d, "sch"),                # >0 = more schooling than peers
})
z = (diff - diff.mean()) / diff.std()          # colour: standard deviations from "typical for income"

# ---- 3. Text shown in each cell, in plain units ---------------------------------
def cell_text(country, key):
    r = d[d["country"] == country].iloc[0]
    if pd.isna(r[key]):
        return "no data"
    i = d.index[d["country"] == country][0]
    if key == "hx":
        return f"{10 ** diff.loc[i, 'hx']:.1f}x"
    if key == "cm":
        ratio = 10 ** (-diff.loc[i, "cm"])          # child deaths relative to income peers
        return f"{abs(1 - ratio) * 100:.0f}% " + ("fewer" if ratio < 1 else "more")
    if key == "san":
        v = diff.loc[i, "san"]
        return "typical" if abs(v) < 1 else f"{v:+.0f} pts"
    v = diff.loc[i, "sch"]
    return "typical" if abs(v) < 0.3 else f"{v:+.1f} yrs"


rows = FIVE
cols = ["hx", "cm", "san", "sch"]
col_labels = ["Health spending\nvs. peers", "Child deaths\nvs. peers", "Sanitation\nvs. peers", "Schooling\nvs. peers"]
grid = np.array([[z.loc[d.index[d["country"] == c][0], k] for k in cols] for c in rows], dtype=float)

# ---- 4. Draw -----------------------------------------------------------------
cmap = LinearSegmentedColormap.from_list("pu_or", ["#5e4fa2", "#f7f7f7", "#d95f02"])
cmap.set_bad("#e6e6e6")
fig, ax = plt.subplots(figsize=(9, 5))
im = ax.imshow(np.ma.masked_invalid(grid), cmap=cmap, vmin=-3, vmax=3, aspect="auto")
ax.set_xticks(range(len(cols)), col_labels)
ax.set_yticks(range(len(rows)), rows)
ax.xaxis.tick_top()
ax.tick_params(length=0)
for i, c in enumerate(rows):
    for j, k in enumerate(cols):
        txt = cell_text(c, k)
        dark = (not np.isnan(grid[i, j])) and abs(grid[i, j]) > 1.6
        ax.text(j, i, txt, ha="center", va="center", fontsize=12, fontweight="bold",
                color="white" if dark else ("#777" if txt == "no data" else "#222"))
for s in ax.spines.values():
    s.set_visible(False)
ax.set_xticks(np.arange(-0.5, len(cols)), minor=True)
ax.set_yticks(np.arange(-0.5, len(rows)), minor=True)
ax.grid(which="minor", color="white", lw=3)
ax.tick_params(which="minor", length=0)

cb = fig.colorbar(im, ax=ax, fraction=0.03, pad=0.03, ticks=[-3, 0, 3])
cb.ax.set_yticklabels(["below\nexpected", "typical\nfor income", "above\nexpected"])
cb.outline.set_visible(False)

fig.suptitle("The five countries beat the odds in different ways", x=0.02, ha="left",
             fontsize=15, fontweight="bold")
fig.text(0.02, 0.89, "Each factor compared with countries of similar income, 2022 (schooling: 2020)",
         fontsize=10.5, color="#444")
fig.text(0.02, 0.01, "Source: Our World in Data. Orange = more spending, fewer child deaths, better sanitation or more schooling than countries\n"
         "with a similar income. Spending is a ratio (1.0x = typical). Grey = country not in the data. Schooling is for 2020 (partly projected).",
         fontsize=7.5, color="#666")
fig.tight_layout(rect=(0, 0.07, 1, 0.88))
OUT.mkdir(exist_ok=True)
fig.savefig(OUT / "visual_heatmap_factors.png", dpi=200, facecolor="white")
print(pd.DataFrame({c: [cell_text(c, k) for k in cols] for c in rows}, index=col_labels).T.to_string())
print("Saved figures/visual_heatmap_factors.png")
