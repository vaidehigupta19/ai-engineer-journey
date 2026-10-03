"""
Day 24 — Distributions
Goal: generate, visualize, and recognize the shape of uniform, normal,
binomial, and Poisson distributions.
"""
import numpy as np
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt

# Worked example: uniform distribution (a fair die, 10,000 rolls)
np.random.seed(0)
OUT = "."
die_rolls = np.random.randint(1, 7, size=10000)
plt.figure()
plt.hist(die_rolls, bins=range(1, 8), align="left", rwidth=0.8)
plt.title("")  # keep titles out of the file per style — describe in your notes
plt.savefig("check_uniform.png")


# TODO 1: normal distribution — generate 10,000 samples from a normal
#         distribution with mean=165, std=10 (like the height example)
#         using np.random.normal(). Plot a histogram. Does it look
#         bell-shaped and roughly symmetric?
heights = np.random.normal(loc=165, scale = 10, size = 10000)
plt.figure()
plt.hist(heights, bins=40)
plt.savefig(f"{OUT}/normal.png")


# TODO 2: the 68-95-99.7 rule — using your Day 22 std-dev sample from
#         TODO 1, compute what fraction of your generated values fall
#         within 1 standard deviation of the mean (165 +/- 10).
#         Is it close to 68%? Try 2 std devs (should be ~95%).
within_1std = np.mean(np.abs(heights - 165) <= 10)
within_2std = np.mean(np.abs(heights - 165) <= 20 )
print(f"within 1 std dev: {within_1std:.3f}")
print(f"within 2 std dev: {within_2std:.3f} ")

# TODO 3: binomial distribution — simulate 10,000 experiments of
#         "flip a fair coin 10 times, count the heads" using
#         np.random.binomial(n=10, p=0.5, size=10000). Plot a
#         histogram. Where's the peak? Does it match what you reasoned
#         through by hand (around 5)?
fair_heads = np.random.binomial(n=10, p=0.5, size=10000)
plt.figure()
plt.hist(fair_heads,bins=range(0, 12), align="left", rwidth=0.8)
plt.savefig(f"{OUT}/binomial_fair.png")
print("Fair coin -- most common head count:", np.bincount(fair_heads).argmax())

# TODO 4: biased binomial — repeat TODO 3 but with p=0.9 instead of
#         0.5. Where does the peak shift to now? Does it match your
#         "9 heads beats 10 heads" reasoning from earlier?
biased_heads= np.random.binomial(n=10, p=0.9, size = 10000)
plt.figure()
plt.hist(biased_heads, bins=range(0, 12), align="left", rwidth=0.8)
plt.savefig(f"{OUT}/binomial_biased.png")
print("Biased coin (p=0.9) -- most common head count:", np.bincount(biased_heads).argmax())

# TODO 5: Poisson distribution — simulate 10,000 "hours" of a shop
#         with an average of 4 customers/hour using
#         np.random.poisson(lam=4, size=10000). Plot a histogram.
#         Is the shape symmetric, or does it lean the way you
#         predicted (long tail toward higher counts, hard wall at 0)?
customers = np.random.poisson(lam=4, size=10000)
plt.figure()
plt.hist(customers, bins=range(0, 15), align="left", rwidth=0.8)
plt.savefig(f"{OUT}/poisson.png")
print("poisson skew check -- mean:", customers.mean(), "median:", np.median(customers))

# TODO 6: side-by-side comparison — plot all four distributions
#         (uniform, normal, binomial p=0.5, Poisson) as subplots in
#         one figure so you can visually compare their shapes at a
#         glance. (hint: plt.subplots(2, 2))
fig, axes = plt.subplots(2,2,figsize=(10,8))
axes[0,0].hist(die_rolls, bins=range(1,8), align="left", rwidth=0.8)
axes[0,1].hist(heights, bins=40)
axes[1,0].hist(fair_heads, bins=range(0,12), align="left", rwidth=0.8)
axes[1,1].hist(fair_heads, bins=range(0,12), align="left", rwidth=0.8)
plt.tight_layout()
plt.savefig(f"{OUT}/all_four.png")
print("\nAll charts saved.")