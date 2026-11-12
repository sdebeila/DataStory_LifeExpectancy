"""
Beating the Odds: Countries That Live Longer Than Their Income Predicts
Draft visual for Week 09: life expectancy vs. GDP per capita (2022),
with the five countries furthest above the income trend highlighted.

Packages: pandas, numpy, matplotlib
Data (Our World in Data, "Full data (CSV)" download), saved in data/:
  - life-expectancy.csv
  - gdp-per-capita-maddison-project-database.csv
Run from the repository root:  python visual_beating_the_odds.py
"""

from pathlib import Path

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from matplotlib.ticker import FuncFormatter

DATA = Path("data")
OUT = Path("figures")
YEAR = 2022
N_TOP = 5

# Conflict-affected or closed economies with highly uncertain estimates.
# Left out of the trend line and the ranking, but still drawn as hollow markers.
EXCLUDE = ["Central African Republic", "North Korea", "Syria", "Palestine"]


def read_owid(path, value_name):
    """OWID CSVs have Entity, Code, Year, <value>; keep the first four columns."""
    df = pd.read_csv(path).iloc[:, :4]
    df.columns = ["country", "code", "year", value_name]
    # drop regions and aggregates (no ISO code, or OWID_ codes)
    return df[df["code"].notna() & ~df["code"].astype(str).str.startswith("OWID")]


# ---- 1. Load and join (2022 only, no values carried forward) --------------
life = read_owid(DATA / "life-expectancy.csv", "life_exp")
gdp = read_owid(DATA / "gdp-per-capita-maddison-project-database.csv", "gdp_pc")

d = life[life["year"] == YEAR].merge(
    gdp[gdp["year"] == YEAR], on=["country", "code", "year"]
)
d = d[d["gdp_pc"] > 0].dropna(subset=["life_exp", "gdp_pc"])
print(f"Countries with both values in {YEAR}: {len(d)}")

# ---- 2. Income trend: life expectancy ~ log10(GDP per capita) -------------
fit = d[~d["country"].isin(EXCLUDE)].copy()
slope, intercept = np.polyfit(np.log10(fit["gdp_pc"]), fit["life_exp"], 1)
fit["predicted"] = intercept + slope * np.log10(fit["gdp_pc"])
fit["gap"] = fit["life_exp"] - fit["predicted"]  # actual minus predicted

ss_res = ((fit["life_exp"] - fit["predicted"]) ** 2).sum()
ss_tot = ((fit["life_exp"] - fit["life_exp"].mean()) ** 2).sum()
print(f"Countries used for the trend: {len(fit)}, R-squared = {1 - ss_res / ss_tot:.2f}")

top = fit.nlargest(N_TOP, "gap")
print(top[["country", "life_exp", "predicted", "gap"]].round(1).to_string(index=False))

excluded = d[d["country"].isin(EXCLUDE) & (d["country"] != "Central African Republic")]

# ---- 3. Plot ---------------------------------------------------------------
x_line = np.logspace(np.log10(d["gdp_pc"].min() * 0.9), np.log10(d["gdp_pc"].max() * 1.1), 200)

fig, ax = plt.subplots(figsize=(9, 6.4))
ax.scatter(fit["gdp_pc"], fit["life_exp"], s=28, color="#b0b0b0", alpha=0.85, lw=0)
ax.scatter(excluded["gdp_pc"], excluded["life_exp"], s=34,
           facecolors="none", edgecolors="#9a9a9a", lw=1)
ax.plot(x_line, intercept + slope * np.log10(x_line), color="#1f4e79", lw=2)
ax.scatter(top["gdp_pc"], top["life_exp"], s=90, color="#d95f02", zorder=3)

# label centres (points from each dot), chosen by hand so labels and leader lines do not overlap
offsets = {"Cuba": (-60, 34), "Lebanon": (45, 40), "Cape Verde": (70, -42),
           "Nicaragua": (-110, 22), "Bangladesh": (-90, -40)}
for _, r in top.iterrows():
    dx, dy = offsets.get(r["country"], (0, 30))
    ax.annotate(f"{r['country']} (+{r['gap']:.1f})", (r["gdp_pc"], r["life_exp"]),
                xytext=(dx, dy), textcoords="offset points", ha="center",
                va="bottom" if dy >= 0 else "top",
                color="#d95f02", fontweight="bold", fontsize=10,
                arrowprops=dict(arrowstyle="-", color="#d95f02", lw=1,
                                relpos=(0.5, 0.0) if dy >= 0 else (0.5, 1.0),
                                shrinkA=2, shrinkB=4))

ax.set_xscale("log")
ax.set_ylim(45, 90)
ax.set_xlim(d["gdp_pc"].min() * 0.8, d["gdp_pc"].max() * 1.2)
ax.xaxis.set_major_formatter(FuncFormatter(lambda v, _: f"${v:,.0f}"))
ax.set_xlabel("GDP per capita (international-$, 2011 prices, log scale)")
ax.set_ylabel("Life expectancy at birth (years)")
ax.grid(axis="y", ls="--", alpha=0.3)
for side in ("top", "right"):
    ax.spines[side].set_visible(False)

ax.set_title("Countries that beat the odds", loc="left", fontsize=15, fontweight="bold", pad=30)
ax.text(0, 1.03, f"Five countries furthest above the income trend, 2022 ({len(fit)} countries; gap in years vs. expected)",
        transform=ax.transAxes, fontsize=11, color="#444")
ax.text(0.99, 0.03, "Blue line: life expectancy expected for each income.\nOrange: the five countries furthest above it. Hollow: left out (data very uncertain).",
        transform=ax.transAxes, ha="right", va="bottom", fontsize=8.5, color="#444",
        bbox=dict(boxstyle="round,pad=0.4", fc="white", ec="#ddd"))
fig.text(0.01, 0.01,
         "Source: Our World in Data (UN WPP; Maddison Project 2023). Hollow markers: conflict-affected or closed economies with\n"
         "uncertain data, excluded from the trend. Central African Republic (18.8 years) is off the chart and also excluded.",
         fontsize=7.5, color="#666", va="bottom")
fig.tight_layout(rect=(0, 0.07, 1, 1))

OUT.mkdir(exist_ok=True)
fig.savefig(OUT / "visual2_top_overperformers.png", dpi=200, facecolor="white")
print("Saved figures/visual2_top_overperformers.png")
