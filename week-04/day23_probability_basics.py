"""
Day 23 — Probability Basics
Goal: basic probability rules, conditional probability, and Bayes'
Theorem — implemented, not just watched.

Same jar setup we reasoned through by hand:
10 marbles total — 7 red (5 striped, 2 solid), 3 blue (1 striped, 2 solid)
"""
import numpy as np
# Worked example: plain probability of red
total = 10
red = 7
p_red = red / total
print("P(red):", p_red)

# TODO 1: compute P(blue). Confirm P(red) + P(blue) == 1
p_blue = 3/10
print("P(blue):", p_blue, "| sum:", p_red + p_blue)

# TODO 2: independent events — imagine a SEPARATE second jar with
#         4 green, 6 yellow (10 total). Compute P(green) for that jar.
#         Then compute P(red AND green) — one marble from each jar.
#         (Hint: for independent events, multiply the individual
#         probabilities — don't just guess, verify why addition would
#         have failed here the way it did in our marble-jar discussion)
p_green = 4/10
p_red_and_green = p_red * p_green
print("P(green):", p_green, "| P(red AND green):", p_red_and_green)

# TODO 3: conditional probability — using the ORIGINAL single jar
#         (7 red: 5 striped, 2 solid | 3 blue: 1 striped, 2 solid):
#         compute P(striped | red) two ways and confirm they match:
#           (a) directly: striped-red count / red count
#           (b) via the formula: P(striped AND red) / P(red)
red_stripped = 5
p_stripped_given_red = red_stripped/total
p_stripped_and_red = red_stripped/total
p_stripped_given_red_formula = p_stripped_given_red/p_red
print("P(stripped|red): ", p_stripped_given_red, "| via formula:", p_stripped_given_red_formula)

# TODO 4: compute P(red | striped) the same two ways — direct count,
#         and via the formula. Confirm it's a DIFFERENT number than
#         P(striped | red) from TODO 3.
total_stripped = 6
p_stripped = total_stripped / total
p_red_given_stripped = red_stripped/total_stripped
p_red_given_stripped_formula = p_stripped_and_red / p_stripped
print("P(red|stripped:)",p_red_given_stripped, "| via formula", p_red_given_stripped_formula)

# TODO 5: Bayes' Theorem — derive P(red | striped) from P(striped | red)
#         instead of recounting marbles:
#         P(red | striped) = P(striped | red) * P(red) / P(striped)
#         Plug in the numbers and confirm it matches TODO 4.
p_red_given_stripped_bayes = (p_stripped_given_red_formula * p_red) / p_stripped
print("P(red|striped) via bayes:", p_red_given_stripped_bayes)

# TODO 6: the medical test scenario — write this one from scratch:
#         disease rate = 1/1000, test catches true cases 99% of the
#         time, false positive rate = 1%. Simulate 1000 people
#         (1 has the disease, 999 don't) and compute:
#           - how many true positives
#           - how many false positives
#           - P(disease | positive test)
#         Compare that number to the "99% accurate" headline figure.
np.random.seed(0)
n_people = 1000
has_disease = np.zeros(n_people, dtype=bool)
has_disease[0] = True

test_positive = np.zeros(n_people, dtype=bool)

test_positive[has_disease] = np.random.rand(has_disease.sum()) < 0.99

healthy = ~has_disease
test_positive[healthy] = np.random.rand(healthy.sum()) < 0.01

true_positives = (test_positive & has_disease).sum()
false_positives = (test_positive & ~has_disease).sum()
total_positive = test_positive.sum()
p_disease_given_positive = true_positives / total_positive
 
print(f"\nTrue positives: {true_positives}, False positives: {false_positives}")
print(f"P(disease | positive test): {p_disease_given_positive:.3f}")
print("Compare to the '99% accurate' headline figure -- worlds apart, "
      "because the disease is rare (base rate fallacy).")