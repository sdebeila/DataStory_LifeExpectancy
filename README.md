# Beating the Odds: Countries That Live Longer Than Their Income Predicts

**Course:** Visual Communication and Data Storytelling
**Program:** MSc Data Science for Society and Business (MDSSB)
**University:** Constructor University Bremen
**Data Story Keyword:** LifeExpectancy
**Team Members:** Shaleen Debeila, Rebeccah Kapsekei, Lutendo Mulea, Morné Magerman, Limpo Shawa

## Project Overview

Does a country's wealth determine how long its people live?

Wealthier countries generally enjoy higher life expectancy, but the relationship is not straightforward. Some countries achieve significantly better health outcomes than their economic resources would suggest.

Our project investigates these exceptions using country-level data from 2022. We examine the relationship between life expectancy, GDP per capita, healthcare expenditure, and income inequality, while considering additional socioeconomic factors that may help explain differences in health outcomes.

Rather than simply showing that richer countries tend to live longer, our data story focuses on five countries that beat the odds and explores what makes their performance interesting.

## Research Question

Why do some countries achieve higher life expectancy than their income levels would predict, and what factors might help explain their better-than-expected outcomes?

Our analysis focuses on three supporting questions:

1. How strongly is national income associated with life expectancy?
2. Which five countries achieve the highest life expectancy relative to their income, and how does their healthcare spending compare?
3. What additional socioeconomic factors might help explain differences in life expectancy?

## Drafting: Audience, Insights, Summary

### Target Audience and Storytelling Approach

**Audience perspective:** Our story takes an outsider perspective, targeting people who are interested in global health and development but do not necessarily have technical backgrounds.

**Target data literacy:** Basic to intermediate.

**Presentation setting:** An accessible public educational talk or online article about global health, development, and inequality.

**Communication goal:** To communicate complex global health patterns through simple visualizations, relatable country comparisons, and clear explanations.

| Persona | Background | Interest and personal connection | Central question |
|---|---|---|---|
| **Sarah (primary)** | 32-year-old secondary school teacher in Nairobi, Kenya | Wants to understand global health inequalities and share meaningful examples with her students. | "Does a country need to be rich for its people to live longer?" |
| **David** | 40-year-old public health policy officer in Johannesburg, South Africa | Interested in identifying countries that achieve strong health outcomes despite limited economic resources. | "Which countries get good results on a small budget, and is spending really the reason?" |
| **Emma** | 24-year-old international relations student in Bremen, Germany | Interested in understanding how global economic inequality relates to health and living conditions. | "Is global inequality in health just a story about money?" |

**Primary persona: Sarah.** Sarah is an educated, curious teacher who follows discussions about global development and inequality. She understands basic charts but is not familiar with advanced statistical methods.

To make our story meaningful to Sarah, we will:
- Use accessible language rather than statistical jargon.
- Focus on one key message per visualization.
- Highlight memorable country comparisons.
- Explain unfamiliar concepts such as GDP per capita.
- Connect global findings to questions relevant to countries such as Kenya.

**Path to value (role of the report for the audience):**
- Sarah can reuse one or two charts and country examples in class discussions.
- David can use the comparison of spending and outcomes as input when thinking about what other countries can teach.
- Emma can build a clearer picture of how wealth, health, and inequality relate.

### Key Insights

Our preliminary analysis and research have identified the following insights:

- **Insight 1: Wealth matters, but it does not tell the whole story.** National income is strongly associated with life expectancy. Our preliminary analysis suggests that income accounts for approximately three-quarters of the observed cross-country variation in life expectancy in 2022 (see Data and Methodology for how this is calculated).
- **Insight 2: Five countries achieve longer lives than their income predicts.** Cuba, Nicaragua, Bangladesh, Lebanon, and Cape Verde appear to achieve life expectancy approximately 5–7 years above income-based expectations.
- **Insight 3: Healthcare spending does not provide a complete explanation.** The five countries have very different healthcare spending levels relative to countries at similar incomes. Preliminary comparisons suggest that Bangladesh spends about half as much as its income peers, while Cuba spends nearly five times as much.
- **Insight 4: Social and environmental conditions may matter.** Child survival appears to account for part of the gap: Cuba, Nicaragua, and Cape Verde have fewer child deaths than their income predicts, while Bangladesh and Lebanon do not. Because child deaths lower life expectancy directly, this is partly built into how life expectancy is calculated. Sanitation and education are still to be tested, and healthcare access is a candidate for which we have not yet identified a suitable dataset.
- **Insight 5: Income inequality alone may not explain the differences.** Preliminary analysis suggests a very weak relationship between the Gini index and countries' deviations from income-based life expectancy expectations. However, missing data (only two of the five countries have a recent value) limits the strength of this conclusion.
- **Insight 6: Global life expectancy has improved, but regional inequalities persist.** Life expectancy has increased substantially across world regions since 1950. The gap between Europe and Africa narrowed from 24.8 years in 1950 to 15.3 years in 2023, but remains considerable.

**Prioritized main insight:**
Five countries achieve life expectancy approximately 5–7 years above what their income would predict, despite substantial differences in healthcare spending.

This finding challenges the idea that national wealth or healthcare expenditure alone determines how long people live. Our story will explore these differences and investigate possible explanations without treating statistical associations as proof of causation.

### Country-Specific Analysis

Our data story focuses on five countries that appear to achieve higher life expectancy than their income would predict, based on our preliminary 2022 analysis. They are the five countries with the largest positive gaps between actual and expected life expectancy after the exclusions described in Data and Methodology.

| Country | Gap vs. income-based expectation (years, preliminary) | Health spending vs. income peers (preliminary) | Focus of investigation |
|---|---|---|---|
| **Cuba** | about +6.6 | about 4.8 times higher | Investigate how healthcare expenditure, child mortality, sanitation, and education relate to its better-than-expected life expectancy. |
| **Nicaragua** | about +5.5 | about 1.6 times higher | Explore which socioeconomic conditions may be associated with its relatively strong life expectancy outcomes. |
| **Bangladesh** | about +5.5 | about half | Examine how the country achieves better-than-expected life expectancy despite relatively limited healthcare expenditure. |
| **Lebanon** | about +5.4 | about 0.8 times | Compare its outcomes with countries at a similar income level, and check whether spending, child survival, or sanitation set it apart. |
| **Cape Verde (Cabo Verde)** | about +5.2 | about the same | Explore the relationship between healthcare spending, education, sanitation, and life expectancy in a small island country. |

Despite a shared gap of roughly 5–7 years, the five countries' healthcare spending differs considerably, suggesting that spending alone may not fully account for their outcomes.

**Factors to investigate.** We will test three measurable indicators against the gap between actual and income-expected life expectancy, across all countries with data (about 160), and use the five countries as illustrations. Five data points alone cannot show an association.
- **Child mortality:** Is lower child mortality, relative to income, associated with being above the income-based expectation? Child deaths lower life expectancy directly, so we treat this as part of the explanation and not as a fully independent factor.
- **Sanitation:** Is better access to sanitation, relative to income, associated with a larger positive gap?
- **Education:** Is longer average schooling, relative to income, associated with a larger positive gap? (Latest available year, which is earlier than 2022.)

All results will be described as associations, not causal explanations.

**Intended audience takeaway.** For Sarah, our primary persona, the central message is that countries with different economic resources and healthcare spending patterns can still achieve relatively strong life expectancy outcomes. By comparing these five countries, we aim to show why understanding longevity requires looking beyond national income alone.

### One-Sentence Story Summary

Five countries live approximately 5–7 years longer than their income would predict. Healthcare spending explains only part of this difference, suggesting that other factors may also play an important role.

### Narrative Abstract

Why do people in some countries live longer than those in countries with similar economic resources? Using 2022 data from Our World in Data covering approximately 165 countries, our project investigates the relationship between national income and life expectancy, revealing that wealth explains much, but not everything, about differences in longevity. Preliminary findings suggest that five countries, Cuba, Nicaragua, Bangladesh, Lebanon, and Cape Verde, achieve life expectancy approximately five to seven years above income-based expectations. Interestingly, their healthcare spending patterns differ substantially, suggesting that expenditure alone may not fully account for these outcomes. We therefore explore whether other socioeconomic conditions, including child survival, sanitation, education, and inequality, are associated with these differences. Through accessible visualizations and country comparisons, our story aims to help a general audience understand why economic prosperity does not always translate into the same health outcomes. Ultimately, we highlight how countries performing above expectations may provide valuable starting points for understanding opportunities to improve population health, while recognizing that observed relationships do not establish causation.

## Data and Methodology

### Data Sources

Our analysis uses publicly available country-level datasets, primarily obtained through Our World in Data.

| Indicator | Source | Purpose |
|---|---|---|
| Life expectancy at birth | UN World Population Prospects via Our World in Data | Measure population longevity |
| GDP per capita | Maddison Project Database 2023 via Our World in Data | Measure national economic resources |
| Healthcare expenditure per capita | WHO / World Bank via Our World in Data | Compare health spending |
| Income inequality (Gini index) | World Bank Poverty and Inequality Platform | Explore income distribution |
| Child mortality | UN Inter-agency Group for Child Mortality Estimation via Our World in Data | Investigate possible explanations (tested) |
| Sanitation, years of schooling | Our World in Data (to be downloaded; latest available year, schooling data is older than 2022) | Investigate possible explanations (to be tested) |

**Main analysis year:** 2022. GDP per capita from the Maddison Project ends in 2022, so 2022 is the latest year with matching data.

**Coverage:** 165 countries have both life expectancy and GDP per capita in 2022; 161 are used to fit the trend (see exclusions below). Coverage is lower for other variables (about 160 for health spending and about 125 for the Gini index).

### Analytical Approach

1. Examine the relationship between GDP per capita and life expectancy.
2. Estimate expected life expectancy from national income. "Expected" is the value on a trend line of life expectancy against the logarithm of GDP per capita, and a country's gap is its actual life expectancy minus the expected value.
3. Identify countries performing above or below those expectations. The five countries are those with the largest positive gaps.
4. Compare healthcare expenditure among the selected countries, relative to what countries at similar income levels spend.
5. Test whether child mortality, sanitation, and years of schooling are associated with the gap between actual and expected life expectancy across all countries with data, using the five countries as illustrations.
6. Translate the findings into clear, accessible visualizations.

**Exclusions:** Central African Republic, North Korea, Syria, and Palestine are excluded from the trend and from the ranking because conflict or limited data makes their life expectancy and income estimates highly uncertain. With these included, income explains about two-thirds of the variation instead of about three-quarters, and North Korea, Syria, and Palestine would appear among the largest gaps. These countries are shown separately in the charts.

All findings will be interpreted as associations rather than causal relationships.

## Data Story Narrative

Our story follows a three-part structure.

**Part 1: The Big Picture. Does wealth buy longer lives?** We introduce the global relationship between GDP per capita and life expectancy and show why national income is an important predictor of population health.

**Part 2: The Surprise. Five countries beating the odds.** We highlight countries that achieve longer life expectancy than expected based on income and compare them with countries at similar economic levels.

**Part 3: Beyond Wealth. What else might matter?** We examine healthcare spending and potential socioeconomic explanations, exploring what the differences might mean for understanding global health inequalities.

**Closing message:** National wealth matters, but it is not the complete story of how long people live.

## Planned Visualizations

- **Global income–life expectancy scatterplot:** illustrating the overall relationship and highlighting the countries that outperform expectations.
- **Country comparison chart:** showing observed versus income-predicted life expectancy.
- **Healthcare spending comparison:** exploring expenditure relative to income peers among the selected countries.
- **Socioeconomic factors visualization:** examining additional indicators where data is available.
- **Historical regional comparison:** providing context on changes in life expectancy and persistent global inequalities.

The main charts are produced in `Report.qmd`: the regional comparison since 1950, the income scatterplot, the five highlighted countries, the healthcare spending comparison, and child mortality against the gap. Visualizations will prioritize readability, clear labels, accessible explanations, and meaningful comparisons.

## Repository Structure and Deliverables

The analysis is written in Python (pandas, numpy, matplotlib) inside a Quarto report, and the project is shared through GitHub.

| File or folder | Description |
|---|---|
| `README.md` | Project overview, audience, insights, and narrative plan |
| `Report.qmd` | News-style written data story with the full, reproducible analysis (Python) |
| `index.qmd` | Website entry page |
| `presentation.qmd` | Quarto RevealJS narrative presentation |
| `data/` | The five Our World in Data files used in the analysis: `life-expectancy.csv`, `gdp-per-capita-maddison-project-database.csv`, `annual-healthcare-expenditure-per-capita.csv`, `child-mortality.csv`, `gini-coefficient.csv` |
| `_quarto.yml` | Website configuration |

**To render the report:** install the packages with `python -m pip install pandas numpy matplotlib jupyter`, then run `quarto render Report.qmd` from the repository root.

**Final deliverables:**
- A reproducible Quarto HTML report presented in news-article form.
- A narrative slide deck using Quarto RevealJS.
- Supporting datasets, analytical code, and visualizations.

## Project Status and Next Steps

**Current stage:** Data story development and refinement.

Our next steps are to:
1. Render and review `Report.qmd`, then move its charts into the presentation.
2. Confirm the final main insight using the analysis.
3. Test sanitation and years of schooling against the gap between actual and expected life expectancy, and report which factors show a clear association. (Child mortality has been tested.)
4. Develop the main visualizations.
5. Draft the news-style report and narrative presentation.
6. Review the story for clarity and accessibility to nontechnical audiences.

## Key Takeaway

Living in a wealthy country generally increases the chances of a longer life, but some countries achieve surprisingly good health outcomes with fewer economic resources. Understanding these differences is the central goal of our data story.
