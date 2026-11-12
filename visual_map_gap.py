"""
Spatial chart (choropleth): where do people live longer than their income predicts?
Each country is coloured by its life expectancy gap (actual minus expected for its income), 2022.
The five countries are marked and labelled.

Packages: pandas, numpy, matplotlib (the map outlines are a small GeoJSON file that the script
downloads once into data/ from Natural Earth; no extra mapping packages are needed).
Data (Our World in Data CSVs in data/): life-expectancy.csv, gdp-per-capita-maddison-project-database.csv
Run from the repository root:  python visual_map_gap.py
"""

import json
import urllib.request
from pathlib import Path

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from matplotlib.cm import ScalarMappable
from matplotlib.collections import PatchCollection
from matplotlib.colors import LinearSegmentedColormap, TwoSlopeNorm
from matplotlib.patches import Polygon

DATA, OUT = Path("data"), Path("figures")
YEAR = 2022
EXCLUDE = ["Central African Republic", "North Korea", "Syria", "Palestine"]
GEO_URL = ("https://raw.githubusercontent.com/nvkelso/natural-earth-vector/master/"
           "geojson/ne_110m_admin_0_countries.geojson")
GEO_FILE = DATA / "ne_110m_admin_0_countries.geojson"
ORANGE = "#d95f02"
# marker positions (longitude, latitude) and label offsets in points; Cape Verde is too small
# to appear in the 110m outlines, so all five are drawn as dots
FIVE = {"Cuba": (-79.0, 21.6, (-30, 32)), "Nicaragua": (-85.0, 12.9, (-60, -34)),
        "Bangladesh": (90.3, 23.8, (55, -34)), "Lebanon": (35.9, 33.9, (-25, 42)),
        "Cape Verde": (-23.6, 15.1, (-45, 30))}


def read_owid(file, name):
    df = pd.read_csv(DATA / file).iloc[:, :4]
    df.columns = ["country", "code", "year", name]
    return df[df["code"].notna() & ~df["code"].astype(str).str.startswith("OWID")]


# ---- 1. The gap for each country --------------------------------------------
life = read_owid("life-expectancy.csv", "life_exp")
gdp = read_owid("gdp-per-capita-maddison-project-database.csv", "gdp_pc")
d = life[life["year"] == YEAR].merge(gdp[gdp["year"] == YEAR], on=["country", "code", "year"])
d = d[d["gdp_pc"] > 0].dropna(subset=["life_exp", "gdp_pc"])
fit = d[~d["country"].isin(EXCLUDE)].copy()
slope, intercept = np.polyfit(np.log10(fit["gdp_pc"]), fit["life_exp"], 1)
fit["gap"] = fit["life_exp"] - (intercept + slope * np.log10(fit["gdp_pc"]))
gap = fit.set_index("code")["gap"]
excluded_codes = set(d[d["country"].isin(EXCLUDE)]["code"])

# ---- 2. Country outlines (downloaded once) ------------------------------------
if not GEO_FILE.exists():
    DATA.mkdir(exist_ok=True)
    print("Downloading country outlines (about 1 MB)...")
    urllib.request.urlretrieve(GEO_URL, GEO_FILE)
with open(GEO_FILE, encoding="utf-8") as fh:
    features = json.load(fh)["features"]


def outer_rings(geometry):
    if geometry["type"] == "Polygon":
        return [geometry["coordinates"][0]]
    return [poly[0] for poly in geometry["coordinates"]]


# ---- 3. Draw the map -----------------------------------------------------------
cmap = LinearSegmentedColormap.from_list("pu_or", ["#5e4fa2", "#f7f7f7", ORANGE])
norm = TwoSlopeNorm(vmin=-8, vcenter=0, vmax=8)  # gaps beyond +/-8 years share the end colours
fig, ax = plt.subplots(figsize=(11, 6))
for feat in features:
    code = feat["properties"]["ADM0_A3"]
    if feat["properties"]["NAME"] == "Antarctica":
        continue
    if code in gap.index:
        colour = cmap(norm(np.clip(gap[code], -8, 8)))
    elif code in excluded_codes:
        colour = "#cfcfcf"   # left out because the data is highly uncertain
    else:
        colour = "#ececec"   # no data
    patches = [Polygon(np.array(r), closed=True) for r in outer_rings(feat["geometry"])]
    ax.add_collection(PatchCollection(patches, facecolor=colour, edgecolor="white", linewidth=0.4))

for name, (lon, lat, off) in FIVE.items():
    g = fit.loc[fit["country"] == name, "gap"].iloc[0]
    ax.plot(lon, lat, "o", ms=7, mfc=ORANGE, mec="#222", mew=1.2, zorder=5)
    ax.annotate(f"{name} (+{g:.1f})", (lon, lat), xytext=off, textcoords="offset points",
                ha="center", va="bottom" if off[1] >= 0 else "top", fontsize=9.5, fontweight="bold",
                color="#222", zorder=6,
                bbox=dict(boxstyle="round,pad=0.2", fc="white", ec="none", alpha=0.85),
                arrowprops=dict(arrowstyle="-", color="#222", lw=0.8, shrinkA=0, shrinkB=3))

ax.set_xlim(-170, 180)
ax.set_ylim(-58, 85)
ax.set_aspect("equal")
ax.axis("off")

cb = fig.colorbar(ScalarMappable(norm=norm, cmap=cmap), ax=ax, orientation="horizontal",
                  fraction=0.04, pad=0.02, aspect=40, ticks=[-8, -4, 0, 4, 8])
cb.ax.set_xticklabels(["8+ years\nbelow", "4 years\nbelow", "as expected\nfor income", "4 years\nabove", "8+ years\nabove"])
cb.outline.set_visible(False)

fig.suptitle("Where do people live longer than their income predicts?", x=0.02, ha="left",
             fontsize=15, fontweight="bold")
fig.text(0.02, 0.905, f"Life expectancy gap = actual minus expected for the country's income, {YEAR}. "
         "Dots mark the five largest gaps.", fontsize=10, color="#444")
fig.text(0.02, 0.01, "Source: Our World in Data (UN WPP; Maddison Project 2023); outlines: Natural Earth. "
         "Light grey = no data; darker grey = left out because the data is highly uncertain.",
         fontsize=7.5, color="#666")
fig.tight_layout(rect=(0, 0.03, 1, 0.9))
OUT.mkdir(exist_ok=True)
fig.savefig(OUT / "visual_map_gap.png", dpi=200, facecolor="white")
print("Saved figures/visual_map_gap.png")
