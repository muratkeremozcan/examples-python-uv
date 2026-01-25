import numpy as np

# Key takeaways (vectorized ops):
# - NumPy uses vectorized operations (fast C loops under the hood).
# - Scalars broadcast across arrays (add/multiply every element at once).
# - Element-wise ops work between arrays of the same shape.
# - np.vectorize wraps Python functions for element-wise use (convenience, not speed).

arr = np.array([1, 2, 3, 4])

# Scalar operations (broadcasting).
print(arr + 3)  # [4 5 6 7]
print(arr * 2)  # [2 4 6 8]

# Element-wise operations between arrays.
other = np.array([10, 20, 30, 40])
print(arr + other)  # [11 22 33 44]
print(arr * other)  # [10 40 90 160]

# Vectorized boolean mask.
mask = arr > 2
print(mask)  # [False False  True  True]
print(arr[mask])  # [3 4]

# Vectorize a Python function (len) for element-wise use.
words = np.array(["hi", "team", "np"])
# np.vectorize wraps Python functions for element-wise use
len_vec = np.vectorize(len)
print(len_vec(words) > 2)
