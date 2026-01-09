import pandas as pd

# Key takeaways (query):
# - DataFrame.query() filters rows using a string expression.
# - Use and/or for multiple conditions.
# - Use quotes for text matches and parentheses for grouping.

stocks = pd.DataFrame(
    {
        "date": ["2023-01-01", "2023-01-02", "2023-01-03", "2023-01-04"],
        "nike": [88, 92, 97, 90],
        "disney": [120, 138, 95, 142],
    }
)
# print(stocks)
#          date  nike  disney
# 0  2023-01-01    88     120
# 1  2023-01-02    92     138
# 2  2023-01-03    97      95
# 3  2023-01-04    90     142

# Single condition.
print(stocks.query("nike >= 90"))
#          date  nike  disney
# 1  2023-01-02    92     138
# 2  2023-01-03    97      95
# 3  2023-01-04    90     142

# Multiple conditions with and/or.
print(stocks.query("nike > 90 and disney < 140"))
#          date  nike  disney
# 1  2023-01-02    92     138
# 2  2023-01-03    97      95

print(stocks.query("nike > 96 or disney < 98"))
print()
#          date  nike  disney
# 2  2023-01-03    97      95


# ########################
# Long format example with text filtering.

stocks_long = pd.DataFrame(
    {
        "date": [
            "2023-01-01",
            "2023-01-02",
            "2023-01-03",
            "2023-01-04",
            "2023-01-01",
            "2023-01-02",
            "2023-01-03",
            "2023-01-04",
        ],
        "stock": [
            "disney",
            "disney",
            "disney",
            "disney",
            "nike",
            "nike",
            "nike",
            "nike",
        ],
        "close": [120, 138, 95, 142, 88, 92, 97, 90],
    }
)
# print(stocks_long)
#          date   stock  close
# 0  2023-01-01  disney    120
# 1  2023-01-02  disney    138
# 2  2023-01-03  disney     95
# 3  2023-01-04  disney    142
# 4  2023-01-01    nike     88
# 5  2023-01-02    nike     92
# 6  2023-01-03    nike     97
# 7  2023-01-04    nike     90
# disney rows OR (nike rows with close < 90).
print(stocks_long.query('stock == "disney" or (stock == "nike" and close < 90)'))
#          date   stock  close
# 0  2023-01-01  disney    120
# 1  2023-01-02  disney    138
# 2  2023-01-03  disney     95
# 3  2023-01-04  disney    142
# 4  2023-01-01    nike     88
