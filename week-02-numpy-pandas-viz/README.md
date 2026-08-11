# Week 2 — NumPy, Pandas & Data Visualization

Part of my [AI Engineer Roadmap](../README.md) — Phase 1: Foundations.

**Duration:** Day 8–14 | **Phase:** Phase 1 – Foundations | **Focus:** Data Analysis Toolkit

## 🎯 Goal for the week
Move from "can write Python" to "can actually work with data" — load, clean, filter, merge, and visualize a real dataset using NumPy, Pandas, Matplotlib, and Seaborn.

## 📅 Day-by-day log

### Day 8 — NumPy Fundamentals
- Arrays: creating, indexing, slicing
- Array operations: `reshape`, `arange`, `linspace`
- Math on arrays: `sum`, `mean`, `std`, `min`, `max`
- Broadcasting basics

### Day 9 — Pandas Part 1 (DataFrames)
- Creating DataFrames from dictionaries and CSVs
- `read_csv()`, `head()`, `tail()`, `shape`, `info()`, `describe()`
- Selecting columns: `df['col']` and `df[['col1','col2']]`
- Selecting rows: `loc[]` and `iloc[]`

### Day 10 — Pandas Part 2 (Filtering + Grouping)
- Filtering: `df[df['col'] > value]`, multiple conditions with `&` / `|`
- `groupby()` + aggregation functions (`sum`, `mean`, `count`)
- `sort_values()`, `value_counts()`
- Handling missing values: `isnull()`, `dropna()`, `fillna()`
- **Practice:** downloaded a CSV from Kaggle, filtered and grouped it

### Day 11 — Pandas Part 3 (Merge + Clean)
- `merge()`: inner, outer, left, right joins
- `concat()`: stacking DataFrames vertically
- `apply()` and lambda functions on columns
- Renaming columns, changing data types
- **Practice:** merged two datasets and cleaned the result

### Day 12 — Data Visualization
- Matplotlib: line plot, bar chart, scatter plot, histogram
- Customizing: titles, labels, legends, colors, figure size
- Seaborn: heatmap, countplot, boxplot, pairplot
- **Practice:** visualized the dataset cleaned on Day 11

### Day 13–14 — Weekend: First EDA Project
- Downloaded a dataset from Kaggle (Titanic / IPL / Netflix / Zomato)
- Performed full EDA: load → clean → explore → visualize → document findings
- Built a Jupyter notebook with markdown headers explaining each step
- Pushed to GitHub with a README explaining what was found

## 🧠 Key takeaways
Data visualization clicked the fastest this week — seeing a chart change immediately after tweaking a parameter made the feedback loop obvious in a way that pure code didn't. NumPy was the shakiest part, especially early on — array indexing and broadcasting are abstract until you've actually seen them misbehave a few times, so a lot of it didn't fully land until I'd used arrays again inside Pandas later in the week. Interesting that the most "visual" topic was the easiest and the most "just math" topic was the hardest.

## ✅ Checkpoint
By the end of this week I could load a CSV, clean it, filter/group data, merge datasets, and create 5+ types of visualizations — roughly 60% of a data scientist's day-to-day work.

## 📂 Files in this folder
| File | Description |
|------|-------------|
| `day8_numpy_basics.py` | NumPy arrays, indexing, math operations |
| `day9_pandas_dataframes.py` | Loading and exploring a DataFrame |
| `day10_filter_group.py` | Filtering + groupby practice |
| `day11_merge_clean.py` | Merging two datasets, cleaning |
| `day12_visualization.py` | Matplotlib + Seaborn plots |
| `eda_project/` | Full EDA notebook + README with findings |
