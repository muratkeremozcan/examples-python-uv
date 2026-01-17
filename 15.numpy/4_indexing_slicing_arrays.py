import numpy as np

# Key takeaways (indexing, slicing, sorting):
# - Indexing is zero-based; 2D uses [row, col].
# - Slicing uses start:stop (stop is excluded) and optional step.
# - Use ':' to select all rows/cols; axis=0 is rows, axis=1 is columns.
# - np.sort sorts along an axis (default is last axis).

arr_1d = np.array([2, 4, 6, 8, 10])
print(arr_1d[0])  # 2
print(arr_1d[1:4])  # [4 6 8]
print(arr_1d[::2])  # [ 2  6 10]
# start:stop:step ; ::2 means start from beginning, go to end, and take every 2nd element

arr_2d = np.array(
    [
        [5, 3, 1, 9],
        [8, 7, 2, 4],
        [6, 0, 3, 5],
    ]
)

# Index a single element (row, col).
print(arr_2d[2, 3])  # 5

# Row and column selection.
print(arr_2d[0])  # [5 3 1 9]
print(arr_2d[:, 3])  # [9 4 5]

# 2D slicing (rows, cols).
print(arr_2d[0:2, 1:3])  # [[3 1]
#  [7 2]]
print(arr_2d[0:3:2, 0:4:2])  # [[5 1]
#  [6 3]]
print()

# Sorting by axis.


# axis=0 sorts top → bottom
# axis=0 = first dimension = rows (downwards)
print(np.sort(arr_2d, axis=0))
# [[5 0 1 4]
#  [6 3 2 5]
#  [8 7 3 9]]
print


# axis=1 sorts left → right
# axis=1 = second dimension = columns (across)
print(np.sort(arr_2d))
# [[1 3 5 9]
#  [2 4 7 8]
#  [0 3 5 6]]
