# --- GroupBy made simple -----------------------------------------------------
# Mental model: split → apply → combine (index)[values]
# 1) Split rows into groups by key(s) 
# 2) Apply an aggregation per group (sum/mean/count/etc.)
# 3) Combine results into a Series/DataFrame (index = group keys)

import pandas as pd
from dataframes.sales import sales

demo = pd.DataFrame({
    'type': ['A','A','B','B','C'],
    'is_holiday': [False, True, False, False, True],
    'weekly_sales': [100, 120, 80, 140, 60]
})
print("Original dataframe:")
print(demo)
#   type  is_holiday  weekly_sales
# 0    A       False           100
# 1    A        True           120
# 2    B       False            80
# 3    B       False           140
# 4    C        True            60

# 1) Sum per type 
# foo.groupby('row')['value']
print("\nSum per type → Series indexed by 'type':")
sum_by_type = demo.groupby('type')['weekly_sales'].sum()
print(sum_by_type)
# type
# A    220
# B    220
# C     60
# Name: weekly_sales, dtype: int64

# 2) Multiple aggregations per grou
print("\nAggregations per type Multiple aggregations per group → DataFrame with named columns:")
agg_by_type = demo.groupby('type').agg(
    total_sales=('weekly_sales', 'sum'),
    avg_sales=('weekly_sales', 'mean'),
    n_weeks=('weekly_sales', 'size'),
)
print(agg_by_type)
#       total_sales  avg_sales  n_weeks
# type                                 
# A             220      110.0        2
# B             220      110.0        2
# C              60       60.0        1

# 3) Percent share by type
print("\nPercent share by type:")
share_by_type = agg_by_type['total_sales'] / agg_by_type['total_sales'].sum()
print(share_by_type)
# type
# A    0.44
# B    0.44
# C    0.12
# Name: total_sales, dtype: float64

# 4) Two keys
print('\nGroup by two keys → MultiIndex; reset_index() to get normal columns:')
sum_by_type_holiday_demo = (
    demo.groupby(['type', 'is_holiday'])['weekly_sales']
        .sum()
        .reset_index()
)
print(sum_by_type_holiday_demo)
#   type  is_holiday  weekly_sales
# 0    A       False           100
# 1    A        True           120
# 2    B       False           220
# 3    C        True            60


print("\nIf you want columns (not index), use as_index=False:")
sum_by_type_df = demo.groupby('type', as_index=False)['weekly_sales'].sum()
print(sum_by_type_df)
#   type  weekly_sales
# 0    A           220
# 1    B           220
# 2    C            60

# Pitfall: dividing a Python list by a number fails; use a Series
# pd.Series([sales_A, sales_B, sales_C], index=['A','B','C']) / sales_all



#####################################

# Calc total weekly sales
sales_all = sales["weekly_sales"].sum()
# Subset for type A stores, calc total weekly sales
sales_A = sales[sales["type"] == "A"]["weekly_sales"].sum()
sales_B = sales[sales["type"] == "B"]["weekly_sales"].sum()
sales_C = sales[sales["type"] == "C"]["weekly_sales"].sum()

# Get proportion for each type
sales_proportion_by_type = [sales_A, sales_B, sales_C] / sales_all
print(sales_proportion_by_type)

# groupby() instead
sales_by_type = sales.groupby('type')['weekly_sales'].sum()

sales_proportion_by_type = sales_by_type / sales_by_type.sum()
print(sales_proportion_by_type)

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