# Week 4 — Statistics & Probability

Part of my [AI Engineer Roadmap](../README.md) — Phase 1: Foundations.

**Duration:** Day 22–28 | **Phase:** Phase 1 – Foundations | **Focus:** Statistics & Probability

## 🎯 Goal for the week
Build the statistical foundation everything downstream (ML metrics, model evaluation, A/B testing, hypothesis-driven experimentation) actually rests on — not just formulas, but *why* each one works the way it does.

## 📅 Day-by-day log

### Day 22 — Descriptive Statistics
- Mean, median, mode
- Variance, standard deviation
- Range, percentiles, IQR
- When to use mean vs median (skewed data / outliers)

### Day 23 — Probability Basics
- Basic probability rules
- Conditional probability
- Bayes' Theorem (the intuition, not just the formula)
- Independent vs dependent events

### Day 24 — Distributions
- Normal distribution (bell curve, 68-95-99.7 rule)
- Binomial distribution
- Poisson distribution
- Uniform distribution
- When to use which distribution

### Day 25 — Hypothesis Testing
- Null hypothesis vs alternative hypothesis
- p-values: what they actually mean
- Type 1 and Type 2 errors
- t-tests: one-sample, two-sample, paired
- Chi-square test (concept)

### Day 26 — Correlation + Linear Algebra Basics
- Correlation vs causation
- Pearson correlation coefficient
- Covariance
- Linear algebra basics: vectors, matrices, dot product (intuition only)

### Day 27–28 — Weekend: Review + Practice
- Built a personal one-page stats cheat sheet — all key formulas and when to use them
- Implemented basic stats in Python: mean, std, correlation using NumPy/Pandas
- Generated a normal distribution with NumPy and plotted it with Matplotlib
- Ran a t-test in Python using `scipy.stats`

## 🧠 Key takeaways
This week helped me understand statistics as a way of making sense of data rather than just memorizing formulas. Descriptive statistics and probability clicked relatively quickly, while hypothesis testing and p-values took a few tries to fully understand. Implementing correlation, distributions, and t-tests in Python made the concepts much clearer because I could see the numbers and results instead of only working with formulas.

## ✅ Checkpoint
**🎉 Phase 1 complete.** By the end of this week I could describe a dataset's center and spread, reason about probability and conditional probability (including Bayes' Theorem), recognize which distribution a situation calls for, run and interpret a hypothesis test, and compute correlation — the statistical foundation Python, Pandas, and SQL now sit on top of.

## 📂 Files in this folder
| File | Description |
|------|-------------|
| `day22_descriptive_stats.py` | Mean, median, mode, variance, std dev, percentiles, IQR |
| `day23_probability_basics.py` | Probability rules, conditional probability, Bayes' Theorem |
| `day24_distributions.py` | Generating and visualizing normal, binomial, Poisson, uniform |
| `day25_hypothesis_testing.py` | One-sample/two-sample/paired t-tests, p-values |
| `day26_correlation_linalg.py` | Pearson correlation, covariance, vectors & dot product |
| `weekend_stats_in_python.py` | Weekend implementation: stats + normal distribution plot + t-test |
| `sql_cheat_sheet.md` *(rename to `stats_cheat_sheet.md`)* | Personal one-page stats reference |
