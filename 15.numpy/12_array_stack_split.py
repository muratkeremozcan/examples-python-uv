import numpy as np

# Key takeaways (split/stack):
# - np.split breaks a 2D array into equal chunks along rows by default.
# - np.stack adds a new dimension to reassemble chunks.

# 12 months x 3 industries (liquor, restaurant, department).
monthly_sales = np.array(
    [
        [10, 20, 30],
        [11, 21, 31],
        [12, 22, 32],
        [13, 23, 33],
        [14, 24, 34],
        [15, 25, 35],
        [16, 26, 36],
        [17, 27, 37],
        [18, 28, 38],
        [19, 29, 39],
        [20, 30, 40],
        [21, 31, 41],
    ]
)

# Split monthly_sales into quarterly data (4 chunks of 3 rows each).
q1_sales, q2_sales, q3_sales, q4_sales = np.split(monthly_sales, 4)
# print(q1_sales)
# [[10 20 30]
#  [11 21 31]
#  [12 22 32]]

# Stack the four quarterly sales arrays
quarterly_sales = np.stack([q1_sales, q2_sales, q3_sales, q4_sales])
# print(quarterly_sales)
# [
#  [
#   [10 20 30]
#   [11 21 31]
#   [12 22 32]
#  ]
#  [
#   [13 23 33]
#   [14 24 34]
#   [15 25 35]
#  ]
#  [
#   [16 26 36]
#   [17 27 37]
#   [18 28 38]
#  ]
#  [
#   [19 29 39]
#   [20 30 40]
#   [21 31 41]
#  ]
# ]

#######
quarterly_sales2 = np.stack([q1_sales, q2_sales, q3_sales, q4_sales], axis=2)
print(quarterly_sales2)
# [
#  [
#   [10 13 16 19]
#   [20 23 26 29]
#   [30 33 36 39]
#  ]
#  [
#   [11 14 17 20]
#   [21 24 27 30]
#   [31 34 37 40]
#  ]
#  [
#   [12 15 18 21]
#   [22 25 28 31]
#   [32 35 38 41]
#  ]
# ]
