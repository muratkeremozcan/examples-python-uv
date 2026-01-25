import numpy as np

# Key takeaways (broadcasting):
# - Broadcasting lets arrays of different shapes work together.
# - Compare shapes right-to-left; each pair must match or be 1.
# - Scalars always broadcast; reshape 1D arrays to broadcast by column.

arr = np.array([[0, 1, 2, 3, 4], [5, 6, 7, 8, 9]])
row = np.array([0, 1, 2, 3, 4])

# Broadcast a row across all rows (shapes (2,5) + (5,)).
print(arr + row)
# [[ 0  2  4  6  8]
#  [ 5  7  9 11 13]]

# Incompatible example (will error if run):
# bad = arr + np.array([1, 2])

# Broadcast by column: reshape to (2, 1).
col = np.array([10, 20]).reshape(2, 1)
# print(col)
# [[10]
#  [20]]

print(arr + col)
# [[10 11 12 13 14]
#  [20 21 22 23 24]]

# Other ops broadcast the same way.
print(arr * col)
# [[ 0  2  4  6  8]
#  [10 12 14 16 18]]

print(arr - row)
# [[ 0  0  0  0  0]
#  [ 5  5  5  5  5]]
