import numpy as np

# Key takeaways (NumPy arrays):
# - Arrays are NumPy's core data structure (n-dimensional grids).
# - Arrays are homogeneous (single dtype), which saves memory and is fast.
# - Build arrays from lists or from scratch (zeros, random, arange).

# Create a 1D array from a list.
arr_1d = np.array([1, 2, 3, 4])
print(arr_1d)
# [1 2 3 4]
print(arr_1d.dtype)
# int64

# Create a 2D array from a list of lists.
arr_2d = np.array([[1, 2, 3], [4, 5, 6]])
print(arr_2d)
# [[1 2 3]
#  [4 5 6]]
print(arr_2d.shape)
# (2, 3)

# Create arrays from scratch.
zeros = np.zeros((5, 3))
print(zeros)

random_vals = np.random.random((2, 3))
print(random_vals)
# [[0.29074843 0.26988676 0.08950504]
#  [0.86968722 0.72350175 0.08762509]]

# arange: start (inclusive), stop (exclusive), step.
seq = np.arange(0, 10, 3)
print(seq)
# [0 3 6 9]
