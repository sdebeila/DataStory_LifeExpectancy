# Storyboard: Beating the Odds

Keyword: **LifeExpectancy**. Milestone 4, following the Week 10 storyboarding method (Dykes 2019): Phase A (story points), Phase B (Aha moment, beginning, rising insights, conclusion). The main purpose is to build the story, not the exact visualisations, so the visuals are rough drafts from `index.qmd` and the scripts in this repo.

The storyboard combines two team drafts, a ten-card and an eight-card version (the second is kept in full in `PLANNING_NOTES.md`). The "tension" card ("the trend does not fit every country") is now part of the Aha card.

**Narrative arc:** hook, global setting, expected income pattern, surprising exceptions (Aha), how rare and how fast, investigation of possible explanations, cautious conclusion.

## Phase A: story point cards

The method calls for 6 to 10 cards. Each card is a story point (said in words) with a visual anchor.

| # | Slide title / story point | Visual | Role in the arc | Presenter (proposal) |
|---|---|---|---|---|
| 1 | **Everyone lives longer, but gaps remain.** The Europe-Africa gap fell from about 25 years in 1950 to 15 in 2023. | Regional line chart (`visual4_regions_since_1950.png`) | Setting | Rebeccah |
| 2 | **At the same income, life expectancy can differ by 20 years.** Among 12 countries with incomes of 4,000 to 6,000 dollars, life expectancy ranges from 54 to 74 years; Nicaragua is at the top. | Strip chart (`visual_same_income.png`) | Hook and question | Rebeccah |
| 3 | **Income explains about three quarters of the differences.** | Scatter with the income trend line (`visual1_income_vs_life_expectancy.png`) | Rising insight | Shaleen |
| 4 | **But five countries beat the odds.** Cuba, Nicaragua, Bangladesh, Lebanon and Cape Verde live roughly 5 to 7 years longer than their income predicts. | Highlighted scatter (`visual2_top_overperformers.png`) plus dumbbell (`visual_dumbbell_expected.png`) | **Aha moment** (main insight) | Shaleen |
| 5 | **That is rare.** Only 7 of 161 countries are 5+ years above the trend, and Jordan and Albania are almost tied with the fifth. | Waffle chart (`visual_waffle_rare.png`); optional world map (`visual_map_gap.png`) | Rising insight | Shaleen |
| 6 | **They improved at very different speeds.** Since 2000 Bangladesh gained 12 years, the typical country 5, Cuba 1.7. | Slopegraph (`visual_change_2000_2022.png`) | Rising insight | Lutendo |
| 7 | **Healthcare spending is not a single explanation.** Cuba spends about 4.8 times what its income peers do, Bangladesh about half. | Bar chart of spending relative to income peers (`visual3_spending_vs_income_peers.png`) | Investigation | Lutendo |
| 8 | **Child survival and sanitation offer additional clues, but no single route.** They fit some of the five, not all. | Heatmap: five countries by four factors (`visual_heatmap_factors.png`) | Investigation (the "different routes" finding) | Morné |
| 9 | **Inequality and schooling add little.** The data also has gaps. | Short text, optional small chart (`visual5_gini_vs_gap.png`) | Investigation (short) | Limpo |
| 10 | **Income matters, but the story is more complex.** The exceptions are starting points for questions, not proof of what works. | Takeaway summary and limitations | Conclusion and next steps | Limpo |

Presenters are proposals; every team member presents at least one story point in the final presentation.

## Phase B: the four steps

1. **Aha moment (main insight):** five countries live 5 to 7 years longer than their income predicts, despite very different healthcare spending (card 4). This matches the main insight in `README.md`.
2. **Beginning (setting and hook):** cards 1 and 2. Start from the Europe-Africa gap, then zoom in to countries with the same income and very different lives.
3. **Rising insights (hook to Aha):** card 3 (the expected pattern), then card 4 (the exceptions). After the Aha: cards 5 and 6 (how rare, how fast) and cards 7 to 9 (what might explain it).
4. **Conclude:** card 10, with the limits (association, not cause; one year; uncertain data) and next steps.

Slide order: 1 to 10 as numbered. The written report uses the inverted pyramid (the short version first, then the details), while the slides follow this narrative.

**When the team approves the storyboard:** the card titles go into `presentation.qmd` (done as a draft), and only the visuals needed for these cards are refined; the fuller methods and secondary analyses stay in `index.qmd`.

## Open points for storyframing (to discuss in the individual meeting)

- **Main insight:** is "five countries beat the odds, in different ways" a strong enough Aha moment, given that Bangladesh is not explained by any factor we tested?
- **Five countries:** Jordan (+5.14) and Albania (+5.05) are almost tied with Cape Verde (+5.17). Keep five as examples and say so, or define the group differently?
- **Exclusion rule:** Central African Republic, North Korea, Syria and Palestine are left out because their data is highly uncertain. Is that a reasonable, transparent rule, and is it documented well enough?
- **Supporting indicators:** which add genuine insight and which repeat the main finding? Should schooling and inequality stay in the presentation or only in the report?
- **Data choices:** we use Our World in Data with PPP-adjusted GDP. Using current US-dollar GDP from the World Bank changes the top five (Cuba, Bangladesh and Cape Verde drop out).
- **Missing data:** Nicaragua has no sanitation value; Lebanon and Cape Verde have no schooling value; Cuba has no Gini value. Schooling is for 2020 and partly projected.
- **Cuba's spending estimate** is the least reliable number in the story.
- **Extra visuals:** is the dumbbell chart needed on top of the highlighted scatter? The world map is optional. A women-versus-men chart is an idea only.
- **Which visuals** to keep for the final version, and which to move to an appendix.
