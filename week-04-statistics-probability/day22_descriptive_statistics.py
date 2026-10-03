"""
Day 22 — Descriptive Statistics
Goal: compute and interpret mean, median, mode, variance, std dev,
range, percentiles, and IQR — and know when mean vs median lies to you.
"""
import numpy as np
import pandas as pd
from scipy import stats

# A skewed dataset on purpose (most values small, one big outlier) —
# same shape as the "pizza night" example: mostly $8-11, one $52
payments = np.array([8, 9, 10, 10, 11, 11, 12, 52])

# Worked example:
print("Mean:", payments.mean())

# TODO 1: compute the median of `payments`
print("Median:", np.median(payments))

# TODO 2: compute the mode (hint: scipy.stats.mode, or pandas .mode())
print("Mode:", stats.mode(payments, keepdims=True).mode[0])

# TODO 3: compute variance and standard deviation
#         (numpy defaults to population variance — pass ddof=1 for
#         sample variance; look up why that distinction exists)
print("Variance:", payments.var(ddof=1))
print("Std dev:", payments.std(ddof=1))

# TODO 4: compute the range (max - min)
print("Range:", payments.max() - payments.min())

# TODO 5: compute the 25th, 50th, and 75th percentiles
#         (hint: np.percentile(payments, [25, 50, 75]))
p25, p50, p75 = np.percentile(payments, [25, 50, 75])

# TODO 6: compute the IQR (75th percentile minus 25th percentile)
#         — this is the "spread of the middle 50%", much less
#         sensitive to the $52 outlier than variance/std dev is
iqr = p75 - p25
print("IQR:", iqr)

# TODO 7: now build a SECOND array with no outlier
payments_no_outlier = np.array([8, 9, 10, 10, 11, 11, 12, 13])
#         Compute mean AND median for both arrays side by side.
#         Which statistic (mean or median) moved more when you removed
#         the outlier? Does that match what you'd expect?
print("With outlier -> mean:", payments.mean(), "| median:", np.median(payments))
print("Without outlier -> mean:", payments_no_outlier.mean(), "| median:", np.median(payments_no_outlier))
