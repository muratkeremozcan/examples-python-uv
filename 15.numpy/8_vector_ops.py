import numpy as np

# Key takeaways (vectorized ops):
# - NumPy uses vectorized operations (fast C loops under the hood).
# - Scalars broadcast across arrays (add/multiply every element at once).
# - Elementwise ops work between arrays of the same shape.
# - np.vectorize wraps Python functions for elementwise use (convenience, not speed).

arr = np.array([1, 2, 3, 4])

# Scalar operations (broadcasting).
print(arr + 3)
print(arr * 2)

# Elementwise operations between arrays.
other = np.array([10, 20, 30, 40])
print(arr + other)
print(arr * other)

# Vectorized boolean mask.
mask = arr > 2
print(mask)
print(arr[mask])

# Vectorize a Python function (len) for elementwise use.
words = np.array(["hi", "team", "np"])
len_vec = np.vectorize(len)
print(len_vec(words) > 2)
