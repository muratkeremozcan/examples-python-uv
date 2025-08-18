# --- GroupBy made simple -----------------------------------------------------
# Mental model: split → apply → combine
# 1) Split rows into groups by key(s)
# 2) Apply an aggregation per group (sum/mean/count/etc.)
# 3) Combine results into a Series/DataFrame (index = group keys)

import pandas as pd

# Tiny, concrete example
demo = pd.DataFrame({
    'type': ['A','A','B','B','C'],
    'is_holiday': [False, True, False, False, True],
    'weekly_sales': [100, 120, 80, 140, 60]
})
print(demo)

print("\nSum per type → Series indexed by 'type':")
sum_by_type = demo.groupby('type')['weekly_sales'].sum()
print(sum_by_type)

print("\nAggregations per type Multiple aggregations per group → DataFrame with named columns:")
agg_by_type = demo.groupby('type').agg(
    total_sales=('weekly_sales', 'sum'),
    avg_sales=('weekly_sales', 'mean'),
    n_weeks=('weekly_sales', 'size'),
)
print(agg_by_type)

print("\nPercent share by type:")
share_by_type = agg_by_type['total_sales'] / agg_by_type['total_sales'].sum()
print(share_by_type)

print('\nGroup by two keys → MultiIndex; reset_index() to get normal columns:')
sum_by_type_holiday_demo = (
    demo.groupby(['type', 'is_holiday'])['weekly_sales']
        .sum()
        .reset_index()
)
print(sum_by_type_holiday_demo)

print("\nIf you want columns (not index), use as_index=False:")
sum_by_type_df = demo.groupby('type', as_index=False)['weekly_sales'].sum()
print(sum_by_type_df)

# Pitfall: dividing a Python list by a number fails; use a Series
# pd.Series([sales_A, sales_B, sales_C], index=['A','B','C']) / sales_all



from dataframes.sales import sales

# Calc total weekly sales
sales_all = sales["weekly_sales"].sum()
# Subset for type A stores, calc total weekly sales
sales_A = sales[sales["type"] == "A"]["weekly_sales"].sum()
sales_B = sales[sales["type"] == "B"]["weekly_sales"].sum()
sales_C = sales[sales["type"] == "C"]["weekly_sales"].sum()

# Get proportion for each type
sales_propn_by_type = [sales_A, sales_B, sales_C] / sales_all
print(sales_propn_by_type)

# groupby() instead
sales_by_type = sales.groupby('type')['weekly_sales'].sum()

sales_propn_by_type = sales_by_type / sales_by_type.sum()
print(sales_propn_by_type)

#######

import numpy as np

# Group by type and is_holiday; calc total weekly sales
sales_by_type_holiday = sales.groupby(['type', 'is_holiday'])['weekly_sales'].sum()

# For each store type, aggregate weekly_sales: get min, max, mean, and median
sales_stats = sales.groupby('type')['weekly_sales'].agg(['min', 'max', 'mean', 'median'])
print(sales_stats)

# For each store type, aggregate unemployment and fuel_price_usd_per_l: get min, max, mean, and median
unemp_fuel_stats = sales.groupby('type')[['unemployment','fuel_price_usd_per_l']].agg(['min','max','mean','median'])
print(unemp_fuel_stats)