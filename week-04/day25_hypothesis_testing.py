"""
Day 25 — Hypothesis Testing
Goal: run and correctly interpret one-sample, two-sample, and paired
t-tests, and understand what a p-value actually tells you.
"""
import numpy as np
from scipy import stats

np.random.seed(42)

# ── One-sample t-test ────────────────────────────────────────────
# Question: is this class's average height different from the
# national average of 165cm?
class_heights = np.random.normal(loc=168, scale=8, size=30)

# Worked example:
t_stat, p_value = stats.ttest_1samp(class_heights, popmean=165)
print("One-sample t-test p-value:", p_value)

# TODO 1: using a significance threshold of 0.05, would you reject
#         the null hypothesis here (i.e., conclude the class really
#         is different from 165cm)? Write your answer as a comment.

# ── Independent two-sample t-test ────────────────────────────────
# TODO 2: generate two independent groups:
#         method_a_scores = np.random.normal(loc=75, scale=10, size=25)
#         method_b_scores = np.random.normal(loc=80, scale=10, size=25)
#         Run stats.ttest_ind(method_a_scores, method_b_scores).
#         Check the p-value — is the difference likely "real" at the
#         0.05 threshold, or could it plausibly be noise?
method_a_scores = np.random.normal(loc=75, scale=10, size=25)
method_b_scores = np.random.normal(loc=80, scale=10, size=25)
t_stat2, p_value2 = stats.ttest_ind(method_a_scores, method_b_scores)
print("two sample t-test p-value:", p_value2)

# TODO 3: re-run TODO 2 with equal_var=False (Welch's t-test instead
#         of Student's). Does the p-value change much? When would you
#         expect this choice to matter more?
t_stat3, p_value3 = stats.ttest_ind(method_a_scores, method_b_scores, equal_var=False )
print("welch's t-test p-value:", p_value3)

# ── Paired t-test ─────────────────────────────────────────────────
# TODO 4: simulate a before/after tutoring scenario — same 20
#         students, scores before and after:
#         before = np.random.normal(loc=70, scale=8, size=20)
#         after = before + np.random.normal(loc=5, scale=3, size=20)
#         Run stats.ttest_rel(before, after).
before = np.random.normal(loc=70, scale=8, size=20)
after = before + np.random.normal(loc=5, scale=3, size=20)
t_stat4, p_value4 = stats.ttest_rel(before, after)
print("Paired t-test p-value:", p_value4)

# ── Type 1 / Type 2 error intuition ──────────────────────────────
# TODO 5: run TODO 2's test 100 times in a loop, regenerating
#         method_a_scores and method_b_scores from the SAME
#         distributions each time (so there's actually NO real
#         difference — same loc, same scale for both).
#         Count how often p < 0.05 anyway. This count is an estimate
#         of your Type 1 error rate — does it land close to 5%?
false_positive_count = 0
n_trials = 100
for _ in range(n_trials):
    a = np.random.normal(loc=75, scale=10, size=25)
    b = np.random.normal(loc=75, scale=10, size=25)
    _, p = stats.ttest_ind(a,b)
    if p < 0.05:
        false_positive_count += 1
print(f"\nFalse positive out of {n_trials} trials with no real difference: {false_positive_count}")
print(f"estimated type 1 error rate: {false_positive_count/n_trials:.3f}")

