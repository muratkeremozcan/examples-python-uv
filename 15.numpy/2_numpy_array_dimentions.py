import numpy as np

# Key takeaways (array dimensions):
# - 1D arrays are vectors, 2D arrays are matrices, 3D+ arrays are tensors.
# - shape tells you the size of each dimension (a tuple).
# - flatten() makes a 1D copy; reshape() changes shape without changing data.

# 3D array from nested lists (stacked 2D arrays).
arr_3d = np.array(
    [
        [[1, 2], [3, 4]],
        [[5, 6], [7, 8]],
    ]
)
# print(arr_3d)
# [[[1 2]
#   [3 4]]
#  [[5 6]
#   [7 8]]]
# print(arr_3d.shape)
# (2, 2, 2)

# 4D array: think "grid of 3D blocks".
arr_4d = np.array(
    [[[[1, 2], [3, 4]], [[5, 6], [7, 8]]], [[[9, 10], [11, 12]], [[13, 14], [15, 16]]]]
)
# print(arr_4d.shape)
# (2, 2, 2, 2)

# Vector vs explicit row/column (2D) forms.
vector = np.array([1, 2, 3])
# print(vector)
# [1 2 3]

row_vec = np.array([[1, 2, 3]])
# print(row_vec)
# [[1 2 3]]

col_vec = np.array([[1], [2], [3]])
print(col_vec)
# [[1]
#  [2]
#  [3]]
# print(vector.shape, row_vec.shape, col_vec.shape)

# shape, flatten, reshape.
matrix = np.array([[1, 2, 3], [4, 5, 6]])
print(matrix)
# [[1 2 3]
#  [4 5 6]]
print(matrix.shape)
# (2, 3)
print(matrix.flatten())
# [1 2 3 4 5 6]
print(matrix.reshape((3, 2)))
# [[1 2]
#  [3 4]
#  [5 6]]
