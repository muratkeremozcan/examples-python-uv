import numpy as np

# Key takeaways (NumPy dtypes):
# - NumPy dtypes include both type and bit-size (e.g., int32 vs int64).
# - .dtype tells you the array's data type.
# - dtype= lets you set the type on creation; astype() converts later.
# - Mixed types are coerced to a single dtype (often upcast to string or float).

# Default dtype from data.
ints = np.array([1, 2, 3])
print(ints.dtype)
# int64

floats = np.array([1.0, 2.0, 3.0])
print(floats.dtype)
# float64

strings = np.array(["alpha", "beta", "gamma"])
print(strings.dtype)
# <U5 (Unicode string up to 5 chars)

# Set dtype explicitly at creation.
ints_32 = np.array([1, 2, 3], dtype=np.int32)
print(ints_32.dtype)
# int32

# Convert types after creation.
bools = np.array([True, False, True])
print(bools.astype(np.int64))
# [1 0 1]

# Type coercion with mixed data.
mixed = np.array([1, 2.5, "3"])
print(mixed)
# ['1' '2.5' '3']
print(mixed.dtype)
# <U32 (Unicode string up to 32 chars)
