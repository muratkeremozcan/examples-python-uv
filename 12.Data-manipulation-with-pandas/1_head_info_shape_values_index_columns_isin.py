from dataframes.homelessness import homelessness 

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



# Display the first few rows to verify
print("First 5 rows of the DataFrame:")
print(homelessness.head())

print('\nInfo (dtypes, non-nulls, memo):')
print(homelessness.info())

print('\nShape (rows, columns):')
print(homelessness.shape)

print('\nDescribe (summary stats like count, mean, std, min, 25%, 50%, 75%, max):')
print(homelessness.describe())

print('\nValues (underlying NumPy 2D array):')
print(homelessness.values)

print('\nColumn (column labels):')
print(homelessness.columns)

print('\nRow (row labels):')
print(homelessness.index)

print('\nsort_values (ascending):')
print(homelessness.sort_values('individuals').head())
print('\nsort_values (descending):')
print(homelessness.sort_values('family_members', ascending=False).head())
print('\nsort_values (by 2 columns using a list/array):')
print(homelessness.sort_values(['region', 'family_members'], ascending=[True, False]).head())

print('\nselecting columns:')
print(homelessness[['individuals']].head())
print(homelessness[['individuals', 'state']].head())

print('\nfiltering rows:')
print(homelessness[homelessness['individuals'] > 10000].head())
print('\n')
print(homelessness[homelessness['region'] == 'Mountain'].head())

print('\ndouble filtering rows (use & (and), | (or), ~ (not) with parentheses):')
print(homelessness[(homelessness['family_members'] > 10000) & (homelessness['region'] == 'Pacific')].head())

print('\nfiltering rows with isin:')
print(homelessness[homelessness['state'].isin(['California', 'Texas', 'Florida'])].head())

print('\nadd new columns (e.g., total, p_homeless):')
homelessness['total'] = homelessness['individuals'] + homelessness['family_members']
homelessness['p_homeless'] = homelessness['total'] / homelessness['state_pop']
print(homelessness.head())

# Create indiv_per_10k col as homeless individuals per 10k state pop
homelessness["indiv_per_10k"] = homelessness["individuals"] / homelessness["state_pop"] * 10000
# filter rows for indiv_per_10k greater than 20, and sort descending
high_homelessness_srt = homelessness[homelessness["indiv_per_10k"] > 20].sort_values('indiv_per_10k', ascending=False)
# From high_homelessness_srt, select the state and indiv_per_10k cols
result = high_homelessness_srt[['state', 'indiv_per_10k']]
