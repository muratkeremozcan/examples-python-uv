# key takeaways
# head(n): first n rows (default 5)
# info(): dtypes, non-nulls, memory
# describe(): summary stats like count, mean, std, min, 25%, 50%, 75%, max
# shape: (rows, cols)
# values: underlying NumPy 2D array 
# columns: column labels (Index)
# index: row labels (Index)
# sort_values(col): sort rows; use ascending=False or list/array for multi-col & order
# selecting columns: df[['col']], df[['col1','col2']]
# row filtering: df[df['col'] > x]
# combine filters: use & (and), | (or), ~ (not) with parentheses
# isin(seq): membership filter, e.g., df[df['state'].isin([...])]


import pandas as pd

# Create a DataFrame with the provided data
df = pd.DataFrame({
    'region': [
        'East South Central', 'Pacific', 'Mountain', 'West South Central', 'Pacific',
        'Mountain', 'New England', 'South Atlantic', 'South Atlantic', 'South Atlantic',
        'South Atlantic', 'Pacific', 'Mountain', 'East North Central', 'East North Central',
        'West North Central', 'West North Central', 'East South Central', 'West South Central',
        'New England', 'South Atlantic', 'New England', 'East North Central', 'West North Central',
        'East South Central', 'West North Central', 'Mountain', 'West North Central', 'Mountain',
        'New England', 'Mid-Atlantic', 'Mountain', 'Mid-Atlantic', 'South Atlantic',
        'West North Central', 'East North Central', 'West South Central', 'Pacific',
        'Mid-Atlantic', 'New England', 'South Atlantic', 'West North Central',
        'East South Central', 'West South Central', 'Mountain', 'New England', 'South Atlantic',
        'Pacific', 'South Atlantic', 'East North Central', 'Mountain'
    ],
    'state': [
        'Alabama', 'Alaska', 'Arizona', 'Arkansas', 'California', 'Colorado', 'Connecticut',
        'Delaware', 'District of Columbia', 'Florida', 'Georgia', 'Hawaii', 'Idaho', 'Illinois',
        'Indiana', 'Iowa', 'Kansas', 'Kentucky', 'Louisiana', 'Maine', 'Maryland',
        'Massachusetts', 'Michigan', 'Minnesota', 'Mississippi', 'Missouri', 'Montana',
        'Nebraska', 'Nevada', 'New Hampshire', 'New Jersey', 'New Mexico', 'New York',
        'North Carolina', 'North Dakota', 'Ohio', 'Oklahoma', 'Oregon', 'Pennsylvania',
        'Rhode Island', 'South Carolina', 'South Dakota', 'Tennessee', 'Texas', 'Utah',
        'Vermont', 'Virginia', 'Washington', 'West Virginia', 'Wisconsin', 'Wyoming'
    ],
    'individuals': [
        2570, 1434, 7259, 2280, 109008, 7607, 2280, 708, 3770, 21443, 6943, 4131, 1297, 6752,
        3776, 1711, 1443, 2735, 2540, 1450, 4914, 6811, 5209, 3993, 1024, 3776, 983, 1745, 7058,
        835, 6048, 1949, 39827, 6451, 467, 6929, 2823, 11139, 8163, 747, 3082, 836, 6139, 19199,
        1904, 780, 3928, 16424, 1021, 2740, 434
    ],
    'family_members': [
        864, 582, 2606, 432, 20964, 3250, 1696, 374, 3134, 9587, 2556, 2399, 715, 3891, 1482,
        1038, 773, 953, 519, 1066, 2230, 13257, 3142, 3250, 328, 2107, 422, 676, 486, 615, 3350,
        602, 52070, 2817, 75, 3320, 1048, 3337, 5349, 354, 851, 323, 1744, 6111, 972, 511, 2047,
        5880, 222, 2167, 205
    ],
    'state_pop': [
        4887681, 735139, 7158024, 3009733, 39461588, 5691287, 3571520, 965479, 701547, 21244317,
        10511131, 1420593, 1750536, 12723071, 6695497, 3148618, 2911359, 4461153, 4659690,
        1339057, 6035802, 6882635, 9984072, 5606249, 2981020, 6121623, 1060665, 1925614, 3027341,
        1353465, 8886025, 2092741, 19530351, 10381615, 758080, 11676341, 3940235, 4181886,
        12800922, 1058287, 5084156, 878698, 6771631, 28628666, 3153550, 624358, 8501286, 7523869,
        1804291, 5807406, 577601
    ]
})

# Display the first few rows to verify
print("First 5 rows of the DataFrame:")
print(df.head())

print('\nInfo (dtypes, non-nulls, memo):')
print(df.info())

print('\nShape (rows, columns):')
print(df.shape)

print('\nDescribe (summary stats like count, mean, std, min, 25%, 50%, 75%, max):')
print(df.describe())

print('\nValues (underlying NumPy 2D array):')
print(df.values)

print('\nColumn (column labels):')
print(df.columns)

print('\nRow (row labels):')
print(df.index)

print('\nsort_values (ascending):')
print(df.sort_values('individuals').head())
print('\nsort_values (descending):')
print(df.sort_values('family_members', ascending=False).head())
print('\nsort_values (by 2 columns using a list/array):')
print(df.sort_values(['region', 'family_members'], ascending=[True, False]).head())

print('\nselecting columns:')
print(df[['individuals']].head())
print(df[['individuals', 'state']].head())

print('\nfiltering rows:')
print(df[df['individuals'] > 10000].head())
print('\n')
print(df[df['region'] == 'Mountain'].head())

print('\ndouble filtering rows (use & (and), | (or), ~ (not) with parentheses):')
print(df[(df['family_members'] > 10000) & (df['region'] == 'Pacific')].head())

print('\nfiltering rows with isin:')
print(df[df['state'].isin(['California', 'Texas', 'Florida'])].head())

print('\nadd new columns (e.g., total, p_homeless):')
df['total'] = df['individuals'] + df['family_members']
df['p_homeless'] = df['total'] / df['state_pop']
print(df.head())

# Create indiv_per_10k col as homeless individuals per 10k state pop
df["indiv_per_10k"] = df["individuals"] / df["state_pop"] * 10000
# filter rows for indiv_per_10k greater than 20, and sort descending
high_homelessness_srt = df[df["indiv_per_10k"] > 20].sort_values('indiv_per_10k', ascending=False)
# From high_homelessness_srt, select the state and indiv_per_10k cols
result = high_homelessness_srt[['state', 'indiv_per_10k']]

#                 region                 state  individuals  family_members  state_pop
# 0   East South Central               Alabama       2570.0           864.0    4887681
# 1              Pacific                Alaska       1434.0           582.0     735139
# 2             Mountain               Arizona       7259.0          2606.0    7158024
# 3   West South Central              Arkansas       2280.0           432.0    3009733
# 4              Pacific            California     109008.0         20964.0   39461588
# 5             Mountain              Colorado       7607.0          3250.0    5691287
# 6          New England           Connecticut       2280.0          1696.0    3571520
# 7       South Atlantic              Delaware        708.0           374.0     965479
# 8       South Atlantic  District of Columbia       3770.0          3134.0     701547
# 9       South Atlantic               Florida      21443.0          9587.0   21244317
# 10      South Atlantic               Georgia       6943.0          2556.0   10511131
# 11             Pacific                Hawaii       4131.0          2399.0    1420593
# 12            Mountain                 Idaho       1297.0           715.0    1750536
# 13  East North Central              Illinois       6752.0          3891.0   12723071
# 14  East North Central               Indiana       3776.0          1482.0    6695497
# 15  West North Central                  Iowa       1711.0          1038.0    3148618
# 16  West North Central                Kansas       1443.0           773.0    2911359
# 17  East South Central              Kentucky       2735.0           953.0    4461153
# 18  West South Central             Louisiana       2540.0           519.0    4659690
# 19         New England                 Maine       1450.0          1066.0    1339057
# 20      South Atlantic              Maryland       4914.0          2230.0    6035802
# 21         New England         Massachusetts       6811.0         13257.0    6882635
# 22  East North Central              Michigan       5209.0          3142.0    9984072
# 23  West North Central             Minnesota       3993.0          3250.0    5606249
# 24  East South Central           Mississippi       1024.0           328.0    2981020
# 25  West North Central              Missouri       3776.0          2107.0    6121623
# 26            Mountain               Montana        983.0           422.0    1060665
# 27  West North Central              Nebraska       1745.0           676.0    1925614
# 28            Mountain                Nevada       7058.0           486.0    3027341
# 29         New England         New Hampshire        835.0           615.0    1353465
# 30        Mid-Atlantic            New Jersey       6048.0          3350.0    8886025
# 31            Mountain            New Mexico       1949.0           602.0    2092741
# 32        Mid-Atlantic              New York      39827.0         52070.0   19530351
# 33      South Atlantic        North Carolina       6451.0          2817.0   10381615
# 34  West North Central          North Dakota        467.0            75.0     758080
# 35  East North Central                  Ohio       6929.0          3320.0   11676341
# 36  West South Central              Oklahoma       2823.0          1048.0    3940235
# 37             Pacific                Oregon      11139.0          3337.0    4181886
# 38        Mid-Atlantic          Pennsylvania       8163.0          5349.0   12800922
# 39         New England          Rhode Island        747.0           354.0    1058287
# 40      South Atlantic        South Carolina       3082.0           851.0    5084156
# 41  West North Central          South Dakota        836.0           323.0     878698
# 42  East South Central             Tennessee       6139.0          1744.0    6771631
# 43  West South Central                 Texas      19199.0          6111.0   28628666
# 44            Mountain                  Utah       1904.0           972.0    3153550
# 45         New England               Vermont        780.0           511.0     624358
# 46      South Atlantic              Virginia       3928.0          2047.0    8501286
# 47             Pacific            Washington      16424.0          5880.0    7523869
# 48      South Atlantic         West Virginia       1021.0           222.0    1804291
# 49  East North Central             Wisconsin       2740.0          2167.0    5807406
# 50            Mountain               Wyoming        434.0           205.0     577601