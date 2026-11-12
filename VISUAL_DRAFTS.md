# Visual drafts (Milestone 3)

For each insight, a visual draft and notes for the final version. Checked against the Week 9 materials: story point types, chart type categories, data variations, and the three peer-review questions (which story points does the visual make, what could be added to foster it, is it a good chart type).

All drafts are produced by `index.qmd` and the scripts in this repo (`visual_beating_the_odds.py`, `visual_more_drafts.py`, `visual_heatmap_factors.py`, `visual_map_gap.py`).

## Audit

| Insight / role | Visual draft | Story point type | Chart type (category) | Data variation | Status | Notes for the final version |
|---|---|---|---|---|---|---|
| Hook: same income, very different lives | `visual_same_income.png` | Cluster, variance | Strip chart (Distribution) | Variance | **New** | Keep Nicaragua as the only labelled country. Check the 12-country count after any change to the exclusions. |
| Setting: everyone lives longer, gaps remain (Insight 6) | `visual4_regions_since_1950.png` | Change over time, zoom out | Line (Trend) | Change | **Fixed** (Europe and Oceania share one label) | Add small arrows or a shaded band for the Europe-Africa gap; keep the 1950 start. |
| Insight 1: income explains about 75% | `visual1_income_vs_life_expectancy.png` | Relationship | Scatter (Relationship) | Totals, context (trend line) | Draft | Add "161 countries" to the subtitle and a plain-language note on the trend line, as in the highlighted version. |
| Insight 2: five countries beat the odds | `visual2_top_overperformers.png` | Outlier | Scatter (Relationship) | Calculated metric (gap), context | **Fixed** (key explaining line, dots, hollow markers; n in subtitle; leader lines no longer cross labels) | Consider an inset listing the gaps; keep four hollow markers explained. |
| Insight 2: actual vs. expected | `visual_dumbbell_expected.png` | Compare and contrast | Dumbbell (Comparison) | Calculated metric (gap) | **New** (suggested in the team planning notes) | Makes the main gap easier to read than the full scatter; decide whether to show both on the Aha slide. |
| Insight 2: how rare | `visual_waffle_rare.png` | Compare and contrast | Waffle (Composition) | Percentages | **New** | Check the near-ties (Jordan, Albania) if the exclusion rule changes. |
| Insight 2: where in the world | `visual_map_gap.png` | Cluster, outlier | Choropleth (Spatial) | Calculated metric (gap) | Draft, optional | Small countries barely show, so keep the dots and labels; maybe drop from the slides. |
| Insight 6 / change: speed of improvement | `visual_change_2000_2022.png` | Change over time, compare and contrast | Slopegraph (Comparison) | Change | **New** | Possibly add Jordan or Albania for contrast. |
| Insight 3: not just health spending | `visual3_spending_vs_income_peers.png` | Compare and contrast | Bar (Comparison) | Calculated metric (ratio) | **Fixed** (axis tick labels cleaned; Cuba label no longer cut off) | Mark Cuba's estimate as uncertain on the chart itself. |
| Insight 4: child survival, sanitation, schooling | `visual_heatmap_factors.png` | Compare and contrast, relationship | XY heatmap (Relationship) | Calculated metrics | Draft | Keep grey cells for missing data. Possibly add child mortality and sanitation scatters in an appendix. |
| Insight 5: inequality explains little | `visual5_gini_vs_gap.png` | Relationship | Scatter (Relationship) | Variance | Draft, appendix | Two of the five have a recent Gini value, so keep this short. |
| Optional: gender gap | not made | Compare and contrast | Pyramid-style bars (Distribution) | Totals | Idea | Needs the "women vs. men" Our World in Data file. |

## Class categories we do not use

- **Flow** (funnel, Sankey): no natural fit for this story.
- **Intersection, project forward, drill down**: not used. A "drill down" could be a deeper look at one country, such as Bangladesh, if time allows.

## What we changed after the review

- Labels: leader lines now start at the edge of the label, so they no longer cross the text; Europe and Oceania share one label in the regional chart.
- Axes: the spending chart no longer shows cluttered minor tick labels, and the Cuba label fits.
- Context: the main scatter has a short key (what the line, orange dots, and hollow markers mean) and the sample size.
- New draft visuals for story points that were missing: variance (strip chart), percentages (waffle), and change (slopegraph).

## Team planning notes for Week 9: status

From the team planning notes (`PLANNING_NOTES.md`).

| Adjustment noted | Status |
|---|---|
| Regional chart: concise hook, direct takeaway title | Title in the slides states the takeaway ("Everyone lives longer, but gaps remain") |
| Scatter: label the fitted line, explain log income in plain language | Done on the highlighted scatter (key box); the plain-language explanation of log income is in the slide notes and the report text |
| Highlighted scatter: verify the top-five labels, add an actual-versus-predicted comparison | Labels verified against the calculated results; dumbbell chart added |
| Spending chart: check the log-scale design, make 1x unmistakable | Axis cleaned; the 1x line is drawn. To do: label "1x = typical for income" on the chart itself |
| Child mortality: explain it contributes mechanically to life expectancy | In the report text |
| Sanitation: cautious language, clarify percentage points | In the report text; axis says percentage points |
| Schooling and inequality: consider an appendix | Moved to a short slide (card 9) |
| Possible extras: dumbbell chart, world map | Both made |
| Quality checks: units and year visible, consistent names and colours, no overlapping labels, message-based titles | Overlaps fixed; titles in the standalone scripts state the message; the report uses captions |
