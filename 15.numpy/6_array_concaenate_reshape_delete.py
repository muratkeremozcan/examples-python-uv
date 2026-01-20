import numpy as np

# Key takeaways (add/remove data):
# - np.concatenate adds rows/cols along an existing axis.
# - Shapes must match on all other axes; dimensions must match.
# - Use reshape() to turn 1D rows/cols into 2D before concatenating.
# - np.delete removes rows/cols; axis=0 rows, axis=1 cols.

classes = np.array(
    [
        [101, 25],
        [102, 30],
        [103, 27],
    ]
)

# Add rows (axis=0 default).
new_rows = np.array([[104, 28], [105, 26]])
classes_more = np.concatenate((classes, new_rows), axis=0)
# print(classes_more)
# [[101  25]
#  [102  30]
#  [103  27]
#  [104  28]
#  [105  26]]

# Add columns (axis=1).
extra_cols = np.array([[3, 1], [4, 2], [3, 1]])
classes_w_extra = np.concatenate((classes, extra_cols), axis=1)
# print(classes_w_extra)
# [[101  25   3   1]
#  [102  30   4   2]
#  [103  27   3   1]]

# Concatenate a single row/column by reshaping 1D -> 2D.
row = np.array([106, 29]).reshape(1, 2)
# [[106 29]]

classes_plus_row = np.concatenate((classes, row), axis=0)
# print(classes_plus_row)
# [[101  25]
#  [102  30]
#  [103  27]
#  [106  29]]

col = np.array([9, 8, 7]).reshape(3, 1)
# [[9]
#  [8]
#  [7]]

classes_plus_col = np.concatenate((classes, col), axis=1)
# print(classes_plus_col)
# [[101 25 9]
#  [102 30 8]
#  [103 27 7]]

# Delete rows/cols with np.delete.
classes_no_row = np.delete(classes, 1, axis=0)
print(classes_no_row)
# [[101 25]
#  [103 27]]

classes_no_col = np.delete(classes, 1, axis=1)
print(classes_no_col)
