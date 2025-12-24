import pandas as pd

# Key takeaways (list-like columns):
# - explode() turns list-like entries in a column into one row per element (index is replicated).
# - You can explode a Series then merge on the index, or explode directly on the DataFrame.

# 1st way: explode a Series, then merge on index
# df2 = df1['feature3'].explode()
# df1[['feature1', 'feature2']].merge(df2, left_index=True, right_index=True)

# 2nd way (simpler): explode the DataFrame directly
# df2 = df1.explode('feature3')  
# df2.reset_index(drop=True, inplace=True)

# 3rd way: if the column is a delimited string, split then explode
# df2 = df1.assign(feature3=df1['feature3'].str.split(',')).explode('feature3')

# - Empty lists explode to NaN; handle new missing values if needed.
# - If lists are stored as delimited strings, split first (e.g., .str.split(',')) then explode.
# - reset_index() after explode if you want a fresh RangeIndex instead of repeated originals.


obesity = pd.DataFrame({
    "country": ["Argentina", "Germany", "Japan", "Norway"],
    "perc_obesity": [21.5, 22.3, 2.5, 23.0],
    "bounds": [[15.4, 31.5], [16.2, 32.4], [1.1, 3.5], [13.1, 33.0]]
})
#      country  perc_obesity        bounds
# 0  Argentina          21.5  [15.4, 31.5]
# 1    Germany          22.3  [16.2, 32.4]
# 2      Japan           2.5    [1.1, 3.5]
# 3     Norway          23.0  [13.1, 33.0]

# 1st way (explode Series, then merge on index)
# df2 = df1['feature3'].explode()
# df1[['feature1', 'feature2']].merge(df2, left_index=True, right_index=True)

# Explode the values of bounds to a separate row
obesity_bounds = obesity["bounds"].explode()
# 0    15.4
# 0    31.5
# 1    16.2
# 1    32.4
# 2     1.1
# 2     3.5
# 3    13.1
# 3    33.0
# Name: bounds, dtype: object

# print(obesity[["country", "perc_obesity"]])
#      country  perc_obesity
# 0  Argentina          21.5
# 1    Germany          22.3
# 2      Japan           2.5
# 3     Norway          23.0

# merge(..., left_index=True, right_index=True) aligns rows by index, 
# so each exploded bound value is paired with the original country/perc_obesity for that index.
obesity_final = obesity[["country", "perc_obesity"]].merge(obesity_bounds, left_index=True, right_index=True)
# print(obesity_final)
#      country  perc_obesity bounds
# 0  Argentina          21.5   15.4
# 0  Argentina          21.5   31.5
# 1    Germany          22.3   16.2
# 1    Germany          22.3   32.4
# 2      Japan           2.5    1.1
# 2      Japan           2.5    3.5
# 3     Norway          23.0   13.1
# 3     Norway          23.0   33.0

############################

# 2nd way (explode DataFrame directly)
# df2 = df1.explode('feature3')  
# df2.reset_index(drop=True, inplace=True)

# Transform the list-like column named bounds  
obesity_explode = obesity.explode('bounds')
# print(obesity_explode)
#      country  perc_obesity bounds
# 0  Argentina          21.5   15.4
# 0  Argentina          21.5   31.5
# 1    Germany          22.3   16.2
# 1    Germany          22.3   32.4
# 2      Japan           2.5    1.1
# 2      Japan           2.5    3.5
# 3     Norway          23.0   13.1
# 3     Norway          23.0   33.0
# (examples-python-poetry) murat@mac e

# Modify obesity_explode by resetting the index 
obesity_explode.reset_index(drop=True, inplace=True) # drop=True, the old index is discarded and a fresh RangeIndex is assigned., inplace=True mutates in place
# print(obesity_explode)
#      country  perc_obesity bounds
# 0  Argentina          21.5   15.4
# 1  Argentina          21.5   31.5
# 2    Germany          22.3   16.2
# 3    Germany          22.3   32.4
# 4      Japan           2.5    1.1
# 5      Japan           2.5    3.5
# 6     Norway          23.0   13.1
# 7     Norway          23.0   33.0

###########################
# 3rd way (if bounds were delimited strings: split then explode)

# sometimes the “list” isn’t a list; it’s a delimited string. 

# If bounds were stored as delimited strings (not lists), you’d first split:
# ex: your column has "11.4-25.5" or "a,b,c" instead of ["11.4", "25.5"], you need to split to get real lists before exploding.
# df.assign(bounds=df['bounds'].str.split('-')).explode('bounds')


# obesity.assign(bounds=obesity['bounds'].str.split('-'))
# print(obesity_split)
#      country  perc_obesity bounds
# 0  Argentina          21.5    NaN
# 1    Germany          22.3    NaN
# 2      Japan           2.5    NaN
# 3     Norway          23.0    NaN

# Transform the column bounds in the obesity DataFrame
obesity_split = obesity.assign(bounds=obesity['bounds'].str.split('-')).explode('bounds')
# print(obesity_split)
#         country  perc_obesity bounds
# 0        France          14.5   11.4
# 0        France          14.5   25.5
# 1        Mexico          25.3   16.2
# 1        Mexico          25.3   32.4
# 2         Spain          12.5    8.1
# 2         Spain          12.5   16.5
# 3  South Africa          11.3    9.1
# 3  South Africa          11.3   20.1
