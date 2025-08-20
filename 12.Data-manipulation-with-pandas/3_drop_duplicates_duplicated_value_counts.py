# - drop_duplicates(subset=...) removes duplicate rows (never columns)
# - value_counts(): frequency table for a Series, sorted desc by default
#   • normalize=True → proportions; dropna=False to include NaN
#   • sort=False or ascending=True to control order
#   • bins=... to bucket numeric data
#   • to DataFrame: s.value_counts().rename_axis('value').reset_index(name='count')

from dataframes.sales import sales
import pandas as pd

df = pd.DataFrame({
    "A": [1,1,1,  2,2,2,  3,3,  4,4,  5],
    "B": ["x","x","x", "y","y","y", "z","z", "z","z", "q"],
    "C": [10,10,10, 20,21,20, 30,30, 40,40, 50]
})

print("Original:")
print(df)

# 1) Fully identical rows, keep first (default)
print("\n1) drop_duplicates(): keep first of each fully identical row")
print(df.drop_duplicates())

# 2) Fully identical rows, keep last
print("\n2) drop_duplicates(keep='last'): keep last of each fully identical row")
print(df.drop_duplicates(keep='last'))

# 3) Fully identical rows, drop ALL occurrences of duplicates
print("\n3) drop_duplicates(keep=False): drop every row that has a duplicate (by all cols)")
print(df.drop_duplicates(keep=False))
# → keeps only rows that appear exactly once overall: (A,B,C) = (2,'y',21) and (5,'q',50)

# 4) Duplicates by a SUBSET of columns (A,B), ignoring C differences
print("\n4) drop_duplicates(subset=['A','B']): keep first occurrence per (A,B)")
print(df.drop_duplicates(subset=['A','B']))
# → keeps one row per (A,B) pair, disregarding C

# 5) Subset + keep=False: drop ALL rows for (A,B) pairs that occur >1 time
print("\n5) drop_duplicates(subset=['A','B'], keep=False): only keep (A,B) pairs seen once")
print(df.drop_duplicates(subset=['A','B'], keep=False))
# → only (5,'q',50) remains, because (1,'x'), (2,'y'), (3,'z'), (4,'z') appear multiple times

# 6: see which rows are considered duplicates (boolean mask)
print("\n6) duplicated flags (all columns, keep='first')")
print(df.duplicated())
print("\n7) duplicated on subset (A,B), keep=False")
print(df.duplicated(subset=['A','B'], keep=False))

# 7) value_counts on a categorical Series (B): counts and proportions
print("\n7) value_counts on B: counts")
print(df['B'].value_counts())
print("\n7b) value_counts on B: proportions (normalize=True)")
print(df['B'].value_counts(normalize=True))

# 8) value_counts with bins on numeric Series (C): quick histogram buckets
print("\n8) value_counts(bins=3) on C: numeric bins (unsorted)")
print(df['C'].value_counts(bins=3, sort=False))

# 9) Convert value_counts to a tidy DataFrame
print("\n9) value_counts → DataFrame with named columns")
vc = df['B'].value_counts()
print(vc.rename_axis('B').reset_index(name='count'))


print('\n------------')


# Drop duplicate store/type combinations
store_types = sales.drop_duplicates(subset=['store', 'type'])

# Drop duplicate store/department combinations
store_depts = sales.drop_duplicates(subset=['store', 'department'])

# Subset the rows where is_holiday is True and drop duplicate dates
holiday_dates = sales[sales['is_holiday'] == True].drop_duplicates(subset='date')

# Count the number of stores of each type
store_counts = store_types['type'].value_counts()

# Get the proportion of stores of each type
store_props = store_types['type'].value_counts(normalize=True)

# Count the number of stores for each department and sort
dept_counts_sorted = store_depts['department'].value_counts(sort=True)

# Get the proportion of stores in each department and sort
dept_props_sorted = store_depts['department'].value_counts(sort=True, normalize=True)