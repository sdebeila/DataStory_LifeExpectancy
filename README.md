
# Beating the Odds: Countries That Live Longer Than Their Income Predicts

**Course:** Visual Communication and Data Storytelling  
**Program:** MSc Data Science for Society and Business (MDSSB)  
**University:** Constructor University Bremen  
**Team:** Shaleen Debeila, Rebeccah Kapsekei, Lutendo Mulea, Morné Magerman, Limpo Shawa

## 1. Project Overview

**Does a country need to be wealthy for its people to live longer?**

Income and life expectancy are closely related across countries, but income alone cannot describe every country's experience. Our project investigates how life expectancy varies with GDP per capita in 2022, identifies countries whose life expectancy is higher than an income-based statistical benchmark, and explores whether healthcare expenditure per person is associated with these differences.

In our title, **“predicts” means a fitted statistical estimate, not a forecast of the future.** We use a regression model to estimate the life expectancy associated with each country's income level. A country whose observed life expectancy exceeds that estimate has a **positive gap (residual)**. Such a gap makes the country worth investigating; it does not establish that its healthcare system or policies are better.

### Research Question

**Why do some countries live longer than their income-based benchmark suggests, and is healthcare expenditure associated with those differences?**

We approach this through three questions:

1. How strongly is GDP per capita associated with life expectancy across countries in 2022?
2. Which countries have the largest positive gaps between observed and model-estimated life expectancy?
3. Among countries with available data, is healthcare expenditure per capita associated with these gaps?

## 2. Audience and Communication Goal

The story is intended for **outsiders**: readers without specialist training in statistics or global health. We will use plain-language explanations, annotated figures, and a limited number of indicators rather than technical model output alone.

### Audience Personas

| Persona | Background and interests | What the story should offer |
|---|---|---|
| **Sarah (primary)** | A 32-year-old secondary-school teacher in Nairobi, Kenya, interested in accessible examples of global development | Clear country comparisons and visuals she can use to start classroom discussions about income and health |
| **David** | A 40-year-old public health policy officer in Johannesburg, South Africa | Examples of countries that exceed an income-based benchmark and questions worth investigating further |
| **Emma** | A 24-year-old international relations student in Bremen, Germany | An accessible explanation of global inequalities and why income alone cannot fully describe life expectancy |

### Primary Persona and Setting

Sarah is our primary persona. She encounters the story through an online article or classroom resource and wants to explain why wealthier countries often have higher life expectancy while some countries differ from that general pattern.

The story should help her understand the central comparison without needing to interpret regression coefficients or statistical tests.

### Path to Value

The reader begins with a familiar question: *Does more money mean longer lives?*

The first visualization establishes the relationship between income and life expectancy. The second identifies countries whose observed outcomes exceed the income-based benchmark. The third explores whether healthcare expenditure is associated with those differences.

By the end, Sarah should be able to explain what the data shows, recognize that statistical associations are not proof of causation, and use the examples to encourage further discussion.

## 3. Data Sources and Indicators

Our project focuses on **2022 country-level observations** from the World Bank's [World Development Indicators (WDI)](https://databank.worldbank.org/source/world-development-indicators).

We use three indicators:

| Indicator | World Bank code | Unit | Role |
|---|---|---|---|
| Life expectancy at birth | `SP.DYN.LE00.IN` | Years | Main outcome |
| GDP per capita | `NY.GDP.PCAP.CD` | Current US dollars per person | Income benchmark |
| Current health expenditure per capita | `SH.XPD.CHEX.PC.CD` | Current US dollars per person | Exploratory comparison |

Healthcare expenditure data published through WDI draws on health-sector statistical sources, including WHO.

### Data Retrieval

The latest shared Python/Quarto analysis draft is designed to retrieve 2022 observations directly from the World Bank API.

An earlier version used a merged country-level CSV panel, which may have included values carried forward from previous years. We will not treat those earlier outputs as verified 2022 results.

Before reporting findings, we must validate the API retrieval, country classifications, missing observations, and analytical sample.

## 4. Methodology

Our analysis follows five main steps.

### Step 1: Retrieve and Validate the Data

We obtain 2022 observations for the three selected indicators.

We check:

- Whether observations correspond to 2022.
- Whether regional aggregates and other non-country entries have been excluded.
- Whether country identifiers are unique and consistent.
- Which indicators have missing observations.
- Whether the retrieved values are suitable for comparison.

We will not replace missing 2022 values with observations from earlier years.

### Step 2: Prepare the Analytical Sample

The primary regression will include eligible countries with valid 2022 life expectancy and positive GDP per capita.

We will document the final sample size and any exclusions.

Countries will not be excluded merely because their observations are unusual. Any additional exclusions must be justified using transparent data-quality criteria.

### Step 3: Estimate the Income-Based Benchmark

We use ordinary least squares (OLS) regression to estimate the relationship between life expectancy and the natural logarithm of GDP per capita.

The model is:

\[
\text{Life Expectancy}_i = \beta_0 + \beta_1 \ln(\text{GDP per capita}_i) + \varepsilon_i
\]

The fitted model provides an income-based statistical benchmark for each country.

We will report the number of countries included, the estimated relationship, and the model's explanatory power.

This is a descriptive cross-country model, not a causal estimate.

### Step 4: Calculate Life-Expectancy Gaps

For each country, we calculate:

\[
\text{Gap}_i = \text{Observed Life Expectancy}_i - \text{Predicted Life Expectancy}_i
\]

A **positive gap** means the country's observed life expectancy is higher than the fitted income benchmark.

A **negative gap** means its observed life expectancy is lower than that benchmark.

We will rank countries by these gaps and identify cases worth investigating.

### Step 5: Explore Healthcare Expenditure

We compare healthcare expenditure per capita with the residuals from the same income-based model.

This comparison will use countries with valid healthcare expenditure observations and calculated life-expectancy gaps.

We will report:

- The number of countries included.
- The direction and strength of the association.
- A visualization with a trend line.
- Whether influential observations appear to affect the pattern.

Healthcare expenditure is not a direct measure of healthcare quality, access, or efficiency. An association between spending and residuals would not establish that healthcare expenditure caused longer life expectancy.

## 5. Preliminary Country Examples

Our initial work highlighted five countries:

- **Cuba**
- **Nicaragua**
- **Bangladesh**
- **Lebanon**
- **Cabo Verde (Cape Verde)**

These are **preliminary candidate cases**, not confirmed members of the five countries with the largest positive residuals in the final model.

The original examples were identified using preliminary data and income measures. Their positions must be recalculated using the validated 2022 World Bank dataset.

If a proposed country lacks the necessary data or does not exceed the final benchmark, we will report that transparently rather than forcing it into the results.

## 6. Candidate Insights

The following are **questions and possible insights to investigate**, not verified findings.

1. **Income and longevity:** Countries with higher GDP per capita may generally have higher life expectancy, although the relationship is not expected to be identical across all income levels.

2. **Variation among countries:** Countries with similar income levels may have noticeably different life expectancy outcomes.

3. **Countries above the benchmark:** Some countries may achieve life expectancy above the level estimated from their income alone.

4. **Differences in healthcare spending:** Countries above the benchmark may differ in how much they spend per person on healthcare.

5. **Healthcare expenditure and residuals:** The association between healthcare spending and better-than-predicted life expectancy may be positive, weak, negative, or influenced by particular observations. The direction must be established empirically.

6. **Limits of a single economic indicator:** GDP per capita may provide a useful benchmark without fully describing differences in national health outcomes.

We will prioritize insights supported by the validated analysis and remove or revise any that are not supported.

## 7. One-Sentence Story Summary

**National income provides an important benchmark for life expectancy, but differences between observed and predicted outcomes invite further investigation into whether healthcare expenditure is associated with those gaps.**

## 8. Narrative Abstract

Does a country need to be wealthy for its people to live longer? Across the world, national income and life expectancy are closely connected, yet countries with similar economic resources do not always experience the same health outcomes. Our data story investigates this relationship using 2022 country-level indicators from the World Bank. We first estimate an income-based benchmark for life expectancy and then identify countries whose observed outcomes are higher than the model suggests. Next, we examine whether healthcare expenditure per person is associated with these differences, while acknowledging that spending does not directly measure healthcare quality or access. Through three accessible visualizations, we aim to help readers understand the broad relationship, recognize countries that differ from it, and consider possible explanations. The story does not claim that income or healthcare expenditure causes longer lives; instead, it shows how descriptive data analysis can reveal patterns, exceptions, and questions that deserve further investigation.

## 9. The Three-Part Data Story

Our story is organized around three distinct questions and visualizations.

### Part I: Does Income Relate to Longevity?

**Planned visualization:** A scatterplot of GDP per capita against life expectancy for 2022.

The chart will use a logarithmic income axis and show the fitted regression benchmark.

**Purpose:** Introduce the overall relationship and make differences between countries visible.

### Part II: Which Countries Exceed the Benchmark?

**Planned visualization:** A ranked horizontal bar chart showing countries with the largest positive life-expectancy residuals.

**Purpose:** Identify countries whose observed life expectancy exceeds the income-based estimate and show the size of each gap.

We will distinguish the final ranked countries from the five cases originally proposed during the project pitch.

### Part III: Is Healthcare Expenditure Associated with the Gap?

**Planned visualization:** A scatterplot of healthcare expenditure per capita against life-expectancy residuals, including a trend line.

**Purpose:** Explore whether countries spending more per person on healthcare tend to have larger or smaller residuals.

The chart will identify the sample size, display clear units, and explain important limitations.

These are planned visualizations. Their final interpretation will depend on the validated results.

## 10. Team Members and Responsibilities

| Team member | Proposed responsibility |
|---|---|
| Shaleen Debeila | Data preparation, data coverage, and missing-value checks |
| Rebeccah Kapsekei | README documentation, coordination, and integration |
| Lutendo Mulea | Healthcare expenditure analysis and interpretation |
| Morné Magerman | Python regression, residual analysis, and Quarto implementation |
| Limpo Shawa | Visual design, communication, and storytelling |

Responsibilities are proposed and subject to group confirmation.

All team members contribute to reviewing the analysis, discussing findings, and preparing the final presentation.

## 11. Repository and Reproducibility

The project uses **Python** for statistical analysis and visualization, and **Quarto** for reproducible reporting.

### Repository Files

Important files currently visible in the repository include:

- `README.md` — project documentation.
- `Report.qmd` — Quarto report.
- `presentation.qmd` — presentation source.
- `index.qmd` — Quarto website entry point.
- `data/country_panel_wdi_who.csv` — existing merged data panel.
- `data/compile_indicatorsdata.R` — existing data preparation script.
- `_quarto.yml` — Quarto project configuration.

The presence of older data preparation files does not mean they are necessarily used by the latest Python analysis draft.

### Software Requirements

- [Python](https://www.python.org/)
- [Quarto](https://quarto.org/docs/get-started/)
- Jupyter
- `pandas`
- `numpy`
- `matplotlib`
- `requests`
- `scipy`
- `statsmodels`

Install the Python dependencies:

```bash
python -m pip install pandas numpy matplotlib requests scipy statsmodels jupyter
```

### Render the Report

From the repository's root directory, run:

```bash
quarto render Report.qmd --to html
```

**Important:** `Report.qmd` is the filename currently visible in the repository. The latest API-based draft must be incorporated into the appropriate report file and successfully tested before this command can be treated as a verified reproduction procedure.

### Reproducibility Checks

Before final submission, we will:

1. Validate the World Bank API retrieval for 2022.
2. Exclude regional aggregates using a documented classification rule.
3. Check country identifiers, duplicates, and missing observations.
4. Verify the regression sample and model results.
5. Recalculate country residuals and rankings.
6. Check the healthcare comparison sample and association.
7. Assess influential observations and justified exclusions.
8. Save a validated data extract and record the retrieval date.
9. Confirm that the Quarto report renders successfully.

## 12. Limitations

Our analysis has several limitations.

- **Single-year comparison:** The 2022 cross-section cannot explain how changes over time affect life expectancy.
- **Observational data:** Statistical associations do not establish causation.
- **Income measurement:** GDP per capita in current US dollars is affected by exchange rates and differences in local prices.
- **Healthcare expenditure:** Spending per capita does not directly measure healthcare quality, access, efficiency, or the distribution of services.
- **Missing observations:** Not every country has complete data for all three indicators.
- **Model dependence:** Residuals and rankings depend on the analytical sample and regression specification.
- **Influential observations:** Particular countries may affect the estimated healthcare expenditure association.
- **Unobserved factors:** Education, living conditions, public health measures, demographics, and other factors may contribute to differences in life expectancy but are not directly analyzed in the main model.

These limitations are important when interpreting countries that exceed the income-based benchmark.

## 13. Current Project Status

The project direction and core indicators have been selected.

The latest Python/Quarto draft is intended to retrieve 2022 observations directly from the World Bank API, estimate the income-based regression, calculate residuals, and explore healthcare expenditure.

However, the final analysis has not yet been validated.

### Results Still to Confirm

- The final number of eligible countries in the regression.
- The regression coefficients and model fit.
- The countries with the largest positive life-expectancy gaps.
- The availability of data for the five preliminary country examples.
- The number of countries in the healthcare expenditure comparison.
- The direction and strength of the healthcare expenditure association.
- The sensitivity of results to influential observations and documented exclusions.

Earlier preliminary estimates of life-expectancy gaps, model fit, and healthcare spending ratios will not be presented as final findings unless they are reproduced using the validated analysis.

## 14. Central Message

**National income matters, but it does not tell the whole story of how long people live.**

By comparing observed life expectancy with an income-based benchmark and exploring healthcare expenditure, our project aims to identify meaningful patterns while remaining clear about what the data can and cannot establish.
