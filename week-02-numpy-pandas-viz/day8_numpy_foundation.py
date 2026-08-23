"""
Day 8 - NumPy Fundamentals
"""

import numpy as np

#     1. creating arrays
a = np.array([1,2,3,4,5])
print("array:", a)

grid = np.array([[1,2,3], [4,5,6], [7,8,9]])
print("grid:\n", grid)

lin=np.linspace(0, 1, 10)
print("linspace:", lin)

ar = np.arange(0, 21, 2)
print("arange:",ar)

#     2. Indexing & slicing
print("last two of a:", a[-2:])
print("second row of grid:", grid[1])
print("first column of grid:", grid[:,0])

#     3. Reshaping
flat = np.arange(12)
reshaped = flat.reshape(3,4)
print("reshaped:\n", reshaped)

#     4. Math on arrays
print("sum:", a.sum(), "mean:", a.mean(), "std:", a.std(),
      "min:", a.min(), "max:", a.max())

# axis=1 -> collapse across columns -> one value per row
print("row means of grid:", grid.mean(axis=1))
# axis=0 -> collapse across rows -> one value per column
print("col means of grid:", grid.mean(axis=0))

#     5. Broadcasting
print("a + 10:", a+10)

row_multiplier = np.array([1,2,3])
print("grid * [1,2,3] per row:\n", grid * row_multiplier)