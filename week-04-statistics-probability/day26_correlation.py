"""
Day 26 — Correlation + Linear Algebra Basics
Goal: compute correlation and covariance, and get comfortable with
vectors/dot products at an intuition level.
"""
import numpy as np
import pandas as pd

# Two related variables: hours studied, exam score
hours_studied = np.array([1, 2, 3, 4, 5, 6, 7, 8])
exam_score = np.array([50, 55, 58, 65, 70, 74, 82, 88])

# Worked example:
correlation = np.corrcoef(hours_studied, exam_score)[0, 1]
print("Pearson correlation:", correlation)

# TODO 1: compute the covariance between hours_studied and exam_score
#         (hint: np.cov() returns a matrix — the covariance you want
#         is the off-diagonal element)
cov_matrix = np.cov(hours_studied, exam_score)
print("covariance:", cov_matrix[0, 1])

# TODO 2: correlation vs causation — construct a THIRD variable that
#         is correlated with exam_score just by coincidence (e.g.
#         np.array([3,3,4,4,5,5,6,6]) representing "cups of coffee",
#         deliberately made to trend upward alongside the scores).
#         Compute its correlation with exam_score. Does a high
#         correlation here mean coffee CAUSES better scores? Write
#         your reasoning as a comment.
coffee_cups = np.array([3,3,4,4,5,5,6,6])
coffee_corr = np.corrcoef(coffee_cups, exam_score)[0,1]
print("coffee score correlation:", coffee_corr)

# TODO 3: negative correlation — construct a variable that trends
#         DOWN as exam_score goes up (e.g. "hours of TV watched").
#         Compute the correlation. What sign do you expect, and does
#         it match?
tv_hours = np.array([8, 7, 6, 6, 5, 4, 3, 2])
tv_corr = np.corrcoef(tv_hours, exam_score)[0, 1]
print("TV-score correlation:", tv_corr)

# TODO 4: zero/near-zero correlation — construct a variable with no
#         real relationship to exam_score (e.g. random shoe sizes).
#         Compute the correlation — is it close to 0?
shoe_sizes = np.array([9, 7, 10, 8, 9, 7, 10, 8])
shoe_corr = np.corrcoef(shoe_sizes, exam_score)[0, 1]
print("Shoe size-score correlation:", shoe_corr)

# ── Linear algebra basics ────────────────────────────────────────
# TODO 5: create two vectors: v1 = np.array([2, 3]), v2 = np.array([4, 1])
#         Compute their dot product using np.dot(v1, v2)
v1 = np.array([2, 3])
v2 = np.array([4, 1])
dot = np.dot(v1, v2)
print("Dot product:", dot)

# TODO 6: create a 2x2 matrix and multiply it by v1 using
#         matrix @ v1 (or np.matmul). What shape is the result?
matrix = np.array([[1, 0], [0, 1]])  # identity, for a clean baseline
result = matrix @ v1
print("Matrix @ v1 shape:", result.shape, "value:", result)

# TODO 7: without doing any heavy math, in your own words: what does
#         the dot product of two vectors intuitively tell you about
#         how "aligned" they are? (No wrong answer here — just write
#         your current intuition; you'll refine it in Week 9+ when
#         this comes back for neural networks.)
#A large positive dot product means the two vectors point in a
# similar direction (well "aligned"); a dot product near zero means
# they're roughly perpendicular / unrelated in direction; a negative
# dot product means they point in more opposite directions.