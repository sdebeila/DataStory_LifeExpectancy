# Planning notes (Weeks 8 to 10)

This file keeps the team's proposed planning text for Weeks 8 to 10 in full, as proposed by a team member, so nothing is lost. The decisions that were agreed or built from it now live in the files listed in the table below, which are the ones to read for the current state of the project.

## Where each part lives now

| Planning item | Status | Where it is now |
|---|---|---|
| Intended audience (three proposed personas) | Merged | `README.md` has Sarah (primary), David and Emma. The "researcher or policymaker" persona is kept as a secondary reader who needs the methods, and is served by the "How we did it" and "Limits" sections of `index.qmd` |
| Candidate insights and their priority | Merged | `README.md`, "Insight priority" table |
| Proposed one-sentence main insight | Kept as an alternative | The agreed one-sentence summary is in `README.md`; this wording is a good alternative for the slides |
| Proposed abstract | Kept as an alternative | The agreed abstract (7 sentences, 183 words) is in `README.md` |
| Week 9 story points and visual adjustments | Merged and done | `VISUAL_DRAFTS.md` (status column) |
| Dumbbell chart idea | Done | `visual_dumbbell_expected.png`, in `index.qmd` |
| World map idea | Done (optional) | `visual_map_gap.png` |
| Week 10 storyboard (eight cards) | Merged | `STORYBOARD.md` (ten cards; the "tension" card became part of the Aha card) and `presentation.qmd` |
| Open questions for the group and the instructor | Merged | `STORYBOARD.md`, "Open points for storyframing" |
| Reproducibility and sign-off checklist | Kept below with status | See the checklist at the end of this file |

## The team member's text (unchanged)


> **Working draft for the individual meeting.** This section records proposed audience, insights, visual choices, and storyboard. The group should confirm these decisions together. The analysis below remains based on the original project code and has not been re-run here.

## Week 8 — Audience and main insight

### Intended audience (proposed personas)

1. **Interested university student:** Curious about global inequality and health, but not familiar with regression. Needs a clear explanation of what an income-based prediction means.
2. **Public-health or development practitioner:** Wants to identify countries worth investigating and understand which additional indicators might be relevant. Needs caveats about association versus causation.
3. **Data-literate researcher or policymaker:** Wants transparent definitions, sources, sample restrictions, model assumptions, and uncertainty before interpreting country rankings.

**Audience decision for the presentation:** Prioritize the interested student; provide enough methods and limitations for the other audiences in the written report.

### Candidate insights to discuss and prioritize

| Candidate insight | Evidence planned or already analyzed | Priority for the story |
|---|---|---|
| Life expectancy has increased across world regions, but gaps remain | Regional time-series plot | Context |
| Richer countries tend to have higher life expectancy | GDP–life expectancy scatterplot and fitted trend | Essential setup |
| Some countries have life expectancy above the income-based benchmark | Highlighted scatterplot and actual-versus-expected table | **Main insight / Aha moment** |
| The highlighted countries do not all spend similarly on healthcare relative to income | Healthcare-spending comparison | Supporting investigation |
| Lower child mortality is associated with larger positive life-expectancy gaps | Child-mortality scatterplot | Supporting investigation |
| Sanitation is associated with life-expectancy gaps | Sanitation scatterplot | Supporting investigation |
| Schooling and inequality have limited explanatory power in the available comparisons | Schooling figure and inequality text | Optional / limitations |

**Proposed one-sentence main insight:** In 2022, several countries had life expectancies well above the level predicted by their GDP per capita, suggesting that income is an important but incomplete description of differences in longevity.

**Proposed abstract (for group review):**

Life expectancy generally rises with national income, but countries with similar incomes can experience very different health outcomes. Our data story asks which countries lived longer than their income would suggest in 2022 and what additional indicators might help us understand those differences. Using country-level data from Our World in Data, we compare life expectancy with GDP per capita and fit a benchmark relationship using logarithmic income. We then calculate the difference between observed and benchmark life expectancy for each country and highlight the five largest positive gaps in the analyzed sample. To investigate possible explanations, we examine healthcare expenditure, child mortality, sanitation, schooling, and income inequality relative to income. Our visuals move from the global pattern to the countries that depart from it, before exploring the strengths and limitations of the supporting indicators. The results are descriptive associations, not causal estimates or evidence that any particular policy produced longer lives. The aim is to challenge the assumption that income alone determines longevity and identify questions for further research.

## Week 9 — Visual planning and improvement notes

| Story point | Current visual in this report | Chart role | Adjustment before final presentation |
|---|---|---|---|
| Regional longevity has improved | Regional line chart | Trend | Make the hook concise; use a direct takeaway title |
| Income and longevity are related | GDP versus life expectancy scatterplot | Relationship | Label fitted line clearly; explain log income in plain language |
| Some countries exceed the benchmark | Highlighted scatterplot and table | Outlier / comparison | Verify the top-five labels and add a simple actual-versus-predicted comparison if useful |
| Healthcare spending varies among the five | Horizontal spending comparison | Comparison | Check log-scale bar design and make the 1× benchmark unmistakable |
| Child survival may be relevant | Child mortality versus gap scatterplot | Relationship | Explain that child mortality contributes mechanically to life expectancy |
| Sanitation may be relevant | Sanitation versus gap scatterplot | Relationship | Use cautious language and clarify percentage-point differences |
| Schooling and inequality provide context | Schooling plot and inequality paragraph | Relationship / qualification | Consider moving to appendix if presentation time is limited |

**Possible additional visual:** A dumbbell chart of observed versus income-predicted life expectancy for the five selected countries. This would make the main gap easier to see than the full scatterplot alone. A world map of residuals is another optional extension, not a requirement for the draft.

**Visual quality checks:** Keep units and year visible; use consistent country names and colors; avoid overlapping labels; give each chart a message-based title; verify that each claim is supported by the plotted data; and keep detailed methods in the written report rather than crowding the slides.

## Week 10 — Presentation storyboard (proposed eight cards)

| Order | Story card / proposed slide title | Narrative function | Visual anchor |
|---|---|---|---|
| 1 | **Why do some countries live longer than their income suggests?** | Hook and question | One highlighted country comparison or simple title visual |
| 2 | **People live longer than in 1950, but gaps remain** | Setting | Regional life-expectancy line chart |
| 3 | **Income explains much of the global pattern** | Rising insight | GDP–life expectancy scatterplot |
| 4 | **But the trend does not fit every country** | Tension / transition | Same scatterplot with fitted line and residuals |
| 5 | **Five countries beat the income-based benchmark** | **Aha moment** | Highlighted scatterplot plus gap table or dumbbell chart |
| 6 | **Healthcare spending is not a single explanation** | Investigation | Healthcare-spending comparison |
| 7 | **Child survival and sanitation offer additional clues** | Investigation | One or two carefully selected supporting visuals |
| 8 | **Income matters, but the story is more complex** | Conclusion and next steps | Takeaway summary and limitations |

**Narrative arc:** Hook → global setting → expected income pattern → surprising exceptions → main finding → investigation → cautious conclusion.

**Open questions for the group and Jan:** Which five countries appear when the final data are run? Are the exclusions justified and transparently documented? Should schooling and inequality remain in the presentation or only in the report? Which supporting indicators add genuine insight rather than repeat the main finding? Do we need an additional dumbbell chart?

**After the group approves this storyboard:** Copy the eight story-card titles into the slide deck, create or refine only the visuals needed for those cards, and retain the fuller methodology and secondary analyses in this report.

## Checklist before Friday's individual meeting (status added)

The original checklist is quoted first, then the current status.

## Reproducibility and group sign-off

**Before the Friday review:**

- [ ] Confirm the intended audience and approve the candidate-insight ranking (Week 8).
- [ ] Confirm the abstract accurately summarizes the rendered findings (Week 8).
- [ ] Run every Python chunk using the group's original `data/` folder and inspect the rendered figures (Week 9).
- [ ] Confirm all country names, gaps, denominators, year labels and figure captions match the calculated results (Week 9).
- [ ] Approve the eight storyboard cards and copy their titles into the presentation slide deck (Week 10).
- [ ] Push the QMD, data-access instructions, and any slides to GitHub before Jan's clone.

**Data requirements:** Keep the source CSVs used by the code in a `data/` folder next to this QMD. The file is not self-contained without those datasets. The following files are referenced in the Python analysis: `life-expectancy.csv`, `gdp-per-capita-maddison-project-database.csv`, `annual-healthcare-expenditure-per-capita.csv`, `child-mortality.csv`, `gini-coefficient.csv`, `mean-years-of-schooling-long-run.csv`, and a sanitation CSV whose spelling is handled in the loader.

**Verification status:** The Python calculations and visuals have not been executed during this merge because the accompanying CSVs were not supplied. Group-proposed audience personas, insights and storyboard are planning drafts, not decisions already approved by all members.

### Status

| Item | Status |
|---|---|
| Confirm the intended audience and approve the insight ranking | To confirm as a team (README and `STORYBOARD.md` have a proposal) |
| Confirm the abstract matches the rendered findings | Checked: numbers match the report (161 countries, about 75%, the five countries) |
| Run every Python chunk with the original `data/` folder and inspect the figures | Done on the team's data (26 cells, 11 figures); re-render after the latest `index.qmd` |
| Confirm country names, gaps, denominators, years and captions | Checked against the calculated results |
| Approve the storyboard cards and copy the titles into the slide deck | Cards drafted in `STORYBOARD.md`; titles are in `presentation.qmd`; team approval still needed |
| Push the QMD, data-access instructions and slides to GitHub before the repository is reviewed | To do |
