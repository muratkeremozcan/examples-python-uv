import numpy as np

# Key takeaways (filtering arrays):
# - 1) Make a boolean mask (True/False per element).
# - 2) Use the mask to filter rows/values (fancy indexing).
# - 3) np.where either gives matching indices OR acts like vectorized if/else.

# Simple 1-2-3 example.
nums = np.array([1, 2, 3, 4, 5])
# 1) mask
nums_mask = nums % 2 == 0
print(nums_mask)  # [False  True False  True False]

# 2) filter with mask
nums_even = nums[nums_mask]
print(nums_even)  # [2 4]

# 3) np.where: indices OR pick values
nums_even_idx = np.where(nums_mask)
print(nums_even_idx)  # (array([1, 3]),)

nums_tagged = np.where(nums_mask, nums, 0)
print(nums_tagged)  # [0 2 0 4 0]

#############################


# 2D example: class id + class size.
# [:, 1] selects all rows, column 1 (class size).
classes = np.array(
    [
        [101, 25],
        [102, 30],
        [103, 27],
        [104, 28],
    ]
)
size_even = classes[:, 1] % 2 == 0  # [False  True False  True]
# Use the row mask, then pick column 0 (class id).
print(classes[size_even, 0])  # [102 104]
print()

#############

print("np.where for indices:")

# give me the indexes where(the value is true)
idx = np.where(nums % 2 == 0)
print(idx)  # (array([1, 3]),)  #the trailing comma just means “tuple with one item"

# Use arr[idx] if you want the values at those positions.
print(nums[idx])  # [2 4]

##################

# 2D np.where returns row and column index arrays (one per axis).
sudoku = np.array(
    [
        [5, 3, 0],
        [6, 0, 1],
        [0, 9, 8],
    ]
)
rows, cols = np.where(sudoku == 0)
# give me the 0s indexes
# - (row 0, col 2)
# - (row 1, col 1)
# - (row 2, col 0)
print(rows, cols)
# [0 1 2] [2 1 0]

# np.where(condition, x, y)
# - if cond is True → take from x
# - else → take from y
sudoku_filled = np.where(sudoku == 0, "", sudoku)
print(sudoku_filled)
# [[5 3 ""
#   [6 "" 1]
#   ["" 9 8]]
