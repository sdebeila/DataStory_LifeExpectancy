"""
Three more draft visuals for the data story, using chart types from the Week 9 slides:
  A. Variance / cluster: "At the same income, life expectancy can differ by 20 years" (strip chart)
  B. Change (comparison, slopegraph): life expectancy 2000 -> 2022 for the five countries vs. the typical country
  C. Percentages (composition, waffle): "Only 7 of 161 countries live 5+ years longer than their income predicts"
  D. Calculated metric (comparison, dumbbell): actual vs. expected life expectancy for the five countries

Packages: pandas, numpy, matplotlib
Data (Our World in Data CSVs in data/): life-expectancy.csv, gdp-per-capita-maddison-project-database.csv
Run from the repository root:  python visual_more_drafts.py
"""

from pathlib import Path

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from matplotlib.patches import Rectangle

DATA, OUT = Path("data"), Path("figures")
YEAR = 2022
EXCLUDE = ["Central African Republic", "North Korea", "Syria", "Palestine"]
FIVE = ["Cuba", "Nicaragua", "Bangladesh", "Lebanon", "Cape Verde"]
ORANGE, LIGHT_ORANGE, GREY, BLUE = "#d95f02", "#f2b27a", "#c9c9c9", "#1f4e79"
plt.rcParams.update({"font.size": 11, "axes.spines.top": False, "axes.spines.right": False})
OUT.mkdir(exist_ok=True)


def read_owid(file, name):
    df = pd.read_csv(DATA / file).iloc[:, :4]
    df.columns = ["country", "code", "year", name]
    return df[df["code"].notna() & ~df["code"].astype(str).str.startswith("OWID")]


def titles(fig, ax, title, subtitle):
    ax.set_title(title, loc="left", fontsize=14, fontweight="bold", pad=28)
    ax.text(0, 1.03, subtitle, transform=ax.transAxes, fontsize=10.5, color="#444")


# ---- Data: the 161 countries and the income trend (same method as the report) ----------
life = read_owid("life-expectancy.csv", "life_exp")
gdp = read_owid("gdp-per-capita-maddison-project-database.csv", "gdp_pc")
d = life[life["year"] == YEAR].merge(gdp[gdp["year"] == YEAR], on=["country", "code", "year"])
d = d[d["gdp_pc"] > 0].dropna(subset=["life_exp", "gdp_pc"])
fit = d[~d["country"].isin(EXCLUDE)].copy()
b, a = np.polyfit(np.log10(fit["gdp_pc"]), fit["life_exp"], 1)
fit["expected"] = a + b * np.log10(fit["gdp_pc"])
fit["gap"] = fit["life_exp"] - fit["expected"]
SRC = "Source: Our World in Data (UN WPP; Maddison Project 2023)."

# ===== A. Same income, very different lives (variance / cluster) =========================
band = fit[(fit["gdp_pc"] >= 4000) & (fit["gdp_pc"] <= 6000)]
lo, hi = band["life_exp"].min(), band["life_exp"].max()
fig, ax = plt.subplots(figsize=(8.5, 5.4))
others = band[band["country"] != "Nicaragua"]
ax.scatter(others["gdp_pc"], others["life_exp"], s=80, color=GREY, edgecolor="white", zorder=2)
nic = band[band["country"] == "Nicaragua"].iloc[0]
ax.scatter(nic["gdp_pc"], nic["life_exp"], s=140, color=ORANGE, edgecolor="#222", zorder=3)
ax.annotate(f"Nicaragua ({nic['life_exp']:.1f})", (nic["gdp_pc"], nic["life_exp"]), xytext=(-90, 6),
            textcoords="offset points", ha="center", color=ORANGE, fontweight="bold", fontsize=11)
ax.annotate("", xy=(6150, lo), xytext=(6150, hi), arrowprops=dict(arrowstyle="<->", color="#444", lw=1.3))
ax.text(6230, (lo + hi) / 2, f"About {hi - lo:.0f} years\napart at almost the\nsame income", va="center", fontsize=11, color="#444")
ax.set_xlim(3800, 7200)
ax.set_ylim(50, 80)
ax.set_xlabel("GDP per capita (international dollars, 2011 prices)")
ax.set_ylabel("Life expectancy at birth (years)")
ax.grid(axis="y", ls="--", alpha=0.3)
titles(fig, ax, "At the same income, life expectancy can differ by 20 years",
       f"{len(band)} countries with GDP per capita of 4,000 to 6,000 international dollars, {YEAR}")
fig.text(0.01, 0.01, SRC + " Each dot is one country.", fontsize=7.5, color="#666")
fig.tight_layout(rect=(0, 0.03, 1, 1))
fig.savefig(OUT / "visual_same_income.png", dpi=200, facecolor="white")
plt.close(fig)
print(f"A: {len(band)} countries in the band, {lo:.1f} to {hi:.1f}")

# ===== B. Change since 2000 (slopegraph) ====================================================
l0 = life[life["year"] == 2000][["country", "life_exp"]].rename(columns={"life_exp": "y0"})
l1 = life[life["year"] == 2022][["country", "life_exp"]].rename(columns={"life_exp": "y1"})
s = fit[["country"]].merge(l0, on="country").merge(l1, on="country")
s["chg"] = s["y1"] - s["y0"]
typ_start, typ_chg = s["y0"].median(), s["chg"].median()
rows = s[s["country"].isin(FIVE)].set_index("country").loc[FIVE]


def spread(vals, gap):
    """Nudge label positions apart so they do not overlap."""
    vals = np.array(vals, float)
    order = np.argsort(vals)
    out = vals.copy()
    for k in range(1, len(order)):
        if out[order[k]] - out[order[k - 1]] < gap:
            out[order[k]] = out[order[k - 1]] + gap
    return out


fig, ax = plt.subplots(figsize=(10, 5.8))
names = FIVE + ["Typical country"]
y0 = list(rows["y0"]) + [typ_start]
y1 = list(rows["y1"]) + [typ_start + typ_chg]
for n, a0, a1 in zip(names, y0, y1):
    typ = n == "Typical country"
    ax.plot([0, 1], [a0, a1], color="#777" if typ else ORANGE, lw=2.2, ls="--" if typ else "-", marker="o", ms=6)
l_pos, r_pos = spread(y0, 1.15), spread(y1, 1.15)
for n, a0, a1, lp, rp in zip(names, y0, y1, l_pos, r_pos):
    typ = n == "Typical country"
    col = "#555" if typ else "#222"
    ax.text(-0.03, lp, f"{n}  {a0:.1f}", ha="right", va="center", fontsize=10.5, color=col, fontweight="bold" if not typ else "normal")
    ax.text(1.03, rp, f"{n}  {a1:.1f}  (+{a1 - a0:.1f})", ha="left", va="center", fontsize=10.5, color=col, fontweight="bold" if not typ else "normal")
ax.set_xlim(-0.6, 1.75)
ax.set_ylim(58, 83)
ax.set_xticks([0, 1])
ax.set_xticklabels(["2000", "2022"], fontsize=12)
ax.set_yticks([])
ax.spines[["left", "bottom"]].set_visible(False)
ax.tick_params(length=0)
bang = rows.loc["Bangladesh"]
titles(fig, ax, f"Bangladesh gained {bang['chg']:.0f} years since 2000; the typical country gained {typ_chg:.0f}",
       "Life expectancy at birth in 2000 and 2022 (years gained in brackets)")
fig.text(0.01, 0.01, "Source: Our World in Data (UN WPP). Typical country = median start value and median gain across the 161 countries.",
         fontsize=7.5, color="#666")
fig.tight_layout(rect=(0, 0.03, 1, 1))
fig.savefig(OUT / "visual_change_2000_2022.png", dpi=200, facecolor="white")
plt.close(fig)
print(f"B: typical gain {typ_chg:.1f} years; Bangladesh {bang['chg']:.1f}")

# ===== C. How rare is it? (waffle) ============================================================
g = fit.sort_values("gap", ascending=False).reset_index(drop=True)
n_c, cols = len(g), 14
n_rows = int(np.ceil(n_c / cols))
n_big = int((g["gap"] >= 5).sum())  # countries 5 or more years above the line
fig, ax = plt.subplots(figsize=(9.5, 5.4))
for i in range(n_c):
    r, c = divmod(i, cols)
    colour = ORANGE if i < 5 else (LIGHT_ORANGE if i < n_big else GREY)
    ax.add_patch(Rectangle((c, n_rows - 1 - r), 0.86, 0.86, color=colour))
ax.set_xlim(-0.2, cols + 8.5)
ax.set_ylim(-0.3, n_rows + 0.2)
ax.set_aspect("equal")
ax.axis("off")
near = g.loc[5:n_big - 1, "country"].tolist()
lx = cols + 0.7
ax.add_patch(Rectangle((lx, n_rows - 2.0), 0.6, 0.6, color=ORANGE))
ax.text(lx + 1.0, n_rows - 1.7, f"Our five: {g.loc[4, 'gap']:.1f} to {g.loc[0, 'gap']:.1f}\nyears above expected", va="center", fontsize=10.5)
ax.add_patch(Rectangle((lx, n_rows - 4.2), 0.6, 0.6, color=LIGHT_ORANGE))
ax.text(lx + 1.0, n_rows - 3.9, f"{' and '.join(near)}: almost\ntied with the fifth", va="center", fontsize=10.5)
ax.add_patch(Rectangle((lx, n_rows - 6.4), 0.6, 0.6, color=GREY))
ax.text(lx + 1.0, n_rows - 6.1, f"All other countries ({n_c - n_big})", va="center", fontsize=10.5)
ax.set_title(f"Only {n_big} of {n_c} countries live 5+ years longer than their income predicts",
             loc="left", fontsize=14, fontweight="bold", pad=26)
ax.text(0, 1.02, f"Each square is one country, {YEAR}, ordered from the largest gap", transform=ax.transAxes, fontsize=10.5, color="#444")
fig.text(0.01, 0.01, SRC + " Gap = actual minus expected life expectancy for the country's income.", fontsize=7.5, color="#666")
fig.tight_layout(rect=(0, 0.03, 1, 1))
fig.savefig(OUT / "visual_waffle_rare.png", dpi=200, facecolor="white")
plt.close(fig)
print(f"C: {n_big} of {n_c} countries are 5+ years above; near-ties: {near}")

# ===== D. Actual vs. expected for the five countries (dumbbell) ====================================
dd = fit.nlargest(5, "gap").sort_values("gap")
fig, ax = plt.subplots(figsize=(8.5, 4.8))
yy = np.arange(len(dd))
ax.hlines(yy, dd["expected"], dd["life_exp"], color="#bbbbbb", lw=3.5, zorder=1)
ax.scatter(dd["expected"], yy, s=120, color=BLUE, zorder=2, label="Expected for the country's income")
ax.scatter(dd["life_exp"], yy, s=140, color=ORANGE, zorder=3, label="Actual life expectancy")
for i, (e, act, gp) in enumerate(zip(dd["expected"], dd["life_exp"], dd["gap"])):
    ax.text(act + 0.5, i, f"{act:.1f}  (+{gp:.1f} yrs)", va="center", fontsize=10.5, fontweight="bold", color="#222")
    ax.text(e - 0.5, i, f"{e:.1f}", va="center", ha="right", fontsize=10, color=BLUE)
ax.set_yticks(yy)
ax.set_yticklabels(dd["country"], fontsize=11)
ax.set_xlim(63, 85)
ax.set_xlabel("Life expectancy at birth (years)")
ax.grid(axis="x", ls="--", alpha=0.3)
ax.spines[["left"]].set_visible(False)
ax.tick_params(axis="y", length=0)
ax.legend(loc="upper center", bbox_to_anchor=(0.5, -0.16), frameon=False, fontsize=9.5, ncol=2)
titles(fig, ax, "Five countries live 5 to 7 years longer than their income predicts",
       f"Actual and income-expected life expectancy, {YEAR}")
fig.text(0.01, 0.01, SRC + " Expected = value on the income trend line (161 countries).", fontsize=7.5, color="#666")
fig.tight_layout(rect=(0, 0.03, 1, 1))
fig.savefig(OUT / "visual_dumbbell_expected.png", dpi=200, facecolor="white")
plt.close(fig)
print("D: dumbbell saved")
