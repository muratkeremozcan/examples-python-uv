import pandas as pd

# Key takeaways (merge_ordered):
# - pd.merge_ordered() merges ordered/time-series data and sorts by the key.
# - Default join is outer (keeps all keys).
# - fill_method="ffill" forward-fills missing values.

# Stock prices over time (different date ranges).
apple = pd.DataFrame(
    {
        "date": ["2007-02-01", "2007-03-01", "2007-04-01", "2007-06-01"],
        "price": [86.0, 90.5, 94.2, 100.1],
    }
)
# print(apple)
#          date  price
# 0  2007-02-01   86.0
# 1  2007-03-01   90.5
# 2  2007-04-01   94.2
# 3  2007-06-01  100.1


mcd = pd.DataFrame(
    {
        "date": ["2007-01-01", "2007-03-01", "2007-05-01"],
        "price": [52.2, 54.0, 55.5],
    }
)
# print(mcd)
#          date  price
# 0  2007-01-01   52.2
# 1  2007-03-01   54.0
# 2  2007-05-01   55.5

# Ordered merge on date; result is sorted by date.
# merge_ordered() defaults to how="outer", but we set it explicitly here.
stock_prices = pd.merge_ordered(
    apple, mcd, on="date", how="outer", suffixes=("_apple", "_mcd")
)
# print(stock_prices)
#          date  price_apple  price_mcd
# 0  2007-01-01          NaN       52.2
# 1  2007-02-01         86.0        NaN
# 2  2007-03-01         90.5       54.0
# 3  2007-04-01         94.2        NaN
# 4  2007-05-01          NaN       55.5
# 5  2007-06-01        100.1        NaN

# Forward-fill missing values (except the first row of each series).
stock_prices_ffill = pd.merge_ordered(
    apple,
    mcd,
    on="date",
    how="outer",
    suffixes=("_apple", "_mcd"),
    fill_method="ffill",
)
print(stock_prices_ffill)
#          date  price_apple  price_mcd
# 0  2007-01-01          NaN       52.2
# 1  2007-02-01         86.0       52.2
# 2  2007-03-01         90.5       54.0
# 3  2007-04-01         94.2       54.0
# 4  2007-05-01         94.2       55.5
# 5  2007-06-01        100.1       55.5

########################
# 1:1 comparison with standard merge (most comparable: outer join + sort).
#
# merge_ordered() defaults to how="outer"; merge() defaults to how="inner".
# merge_ordered() = outer join + sorted output + optional forward fill.
# merge() = general-purpose join; you must sort/fill manually.
# Net: they're not that different—merge_ordered() mostly packages outer+sort+ffill.

# Standard merge: use how="outer" to match merge_ordered results.
stock_prices_outer = apple.merge(
    mcd, on="date", how="outer", suffixes=("_apple", "_mcd")
)
stock_prices_outer_sorted = stock_prices_outer.sort_values("date")
print(stock_prices_outer_sorted)


# Manual forward fill (same idea as fill_method="ffill").
stock_prices_outer_ffill = stock_prices_outer_sorted.ffill()
print(stock_prices_outer_ffill)
#          date  price_apple  price_mcd
# 0  2007-01-01          NaN       52.2
# 1  2007-02-01         86.0       52.2
# 2  2007-03-01         90.5       54.0
# 3  2007-04-01         94.2       54.0
# 4  2007-05-01         94.2       55.5
# 5  2007-06-01        100.1       55.5
