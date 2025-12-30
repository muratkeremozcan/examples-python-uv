# Pivot Table vs GroupBy — quick compare
# - groupby: split→apply→combine; returns Series/DF indexed by keys; great for pipelines.
# - pivot_table: groupby + unstack; 2D layout via index/columns/values; great for reports.
# - Extras in pivot_table: columns=..., margins=True (totals), fill_value=..., observed=True.
# - Prefer groupby for multi-column NamedAgg and further chaining; pivot_table for matrix-style output.

import pandas as pd

# Same tiny demo used in 4_groupby.py
demo = pd.DataFrame(
    {
        "type": ["A", "A", "B", "B", "C"],
        "is_holiday": [False, True, False, False, True],
        "weekly_sales": [100, 120, 80, 140, 60],
    }
)

print("Original demo:")
print(demo)
#   type  is_holiday  weekly_sales
# 0    A       False           100
# 1    A        True           120
# 2    B       False            80
# 3    B       False           140
# 4    C        True            60

# 1) Sum per type (equivalent to: demo.groupby('type')['weekly_sales'].sum())
# (foo, row, value)
print("\nSum per type (pivot_table):")
sum_by_type = pd.pivot_table(demo, index="type", values="weekly_sales", aggfunc="sum")
print(sum_by_type)
#       weekly_sales
# type
# A              220
# B              220
# C               60

# 2) Multiple aggregations per group (flatten MultiIndex columns afterward)
print("\nAggregations per type (pivot_table with multiple agg funcs):")
agg_by_type = pd.pivot_table(
    demo, index="type", values="weekly_sales", aggfunc=["sum", "mean", "count"]
)
agg_by_type.columns = [
    "total_sales",
    "avg_sales",
    "n_weeks",
]  # flatten & rename for readability
print(agg_by_type)
#       total_sales  avg_sales  n_weeks
# type
# A             220      110.0        2
# B             220      110.0        2
# C              60       60.0        1

# 3) Percent share by type (using the single-agg table)
print("\nPercent share by type:")
share_by_type = sum_by_type["weekly_sales"] / sum_by_type["weekly_sales"].sum()
print(share_by_type)
# type
# A    0.44
# B    0.44
# C    0.12
# Name: weekly_sales, dtype: float64

# 4) Two keys → spread second key into columns (matrix layout)
print("\nTwo keys → index='type', columns='is_holiday', values='weekly_sales':")
agg_by_type_holiday = pd.pivot_table(
    demo,
    index="type",
    columns="is_holiday",
    values="weekly_sales",
    aggfunc="sum",
    fill_value=0,  # fill missing combos
    margins=True,  # add totals row/column
)
print(agg_by_type_holiday)
# is_holiday  False  True  All
# type
# A             100   120  220
# B             220     0  220
# C               0    60   60
# All           320   180  500

# 5) Want columns instead of index? Reset index (similar to groupby(..., as_index=False))
print("\nAs columns (not index): reset_index():")
print(sum_by_type.reset_index())
#   type  weekly_sales
# 0    A           220
# 1    B           220
# 2    C            60


# Notes:
# - groupby equivalent for #4 is: demo.groupby(['type','is_holiday'])['weekly_sales'].sum().unstack(fill_value=0)
# - pivot_table can take dict or list of aggfuncs; groupby.agg supports NamedAgg for many input columns.


##########

import numpy as np
from dataframes.sales import sales

# sales_by_type_holiday = sales.groupby(['type', 'is_holiday'])['weekly_sales'].sum()
sales_by_type_holiday = pd.pivot_table(
    sales, index=["type", "is_holiday"], values="weekly_sales", aggfunc="sum"
)

# sales.groupby('type')['weekly_sales'].agg(['min', 'max', 'mean', 'median'])
sales_stats = pd.pivot_table(
    sales, index="type", values="weekly_sales", aggfunc=["min", "max", "mean", "median"]
)
sales_stats.columns = ["min", "max", "mean", "median"]
print(sales_stats)

# sales.groupby('type')[['unemployment','fuel_price_usd_per_l']].agg(['min','max','mean','median'])
unemp_fuel_stats = pd.pivot_table(
    sales,
    index="type",
    values=["unemployment", "fuel_price_usd_per_l"],
    aggfunc=["min", "max", "mean", "median"],
)
# The result has MultiIndex columns: (value, aggfunc) pairs
# We need to flatten them properly
unemp_fuel_stats.columns = [f"{col[0]}_{col[1]}" for col in unemp_fuel_stats.columns]
print(unemp_fuel_stats)
