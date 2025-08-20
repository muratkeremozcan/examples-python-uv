# - set_index: Move column(s) to index; creates labeled row access
# - reset_index: Move index back to column(s); restores integer index
# reset_index(drop=True) drops the current index
# - loc: Label-based selection using index/column names
# - iloc: Position-based selection using integer positions
# - sort_index: Sort rows by index labels
# - sort_index(level=...) : sort by index level
# - sort_index(ascending=...) : sort by index level

# df[column_list] → selects columns
# df[boolean_condition] → selects rows
# df.loc[index_values] → selects rows by index labels

from dataframes.temperatures import temperatures

print('\n temperatures: \n')
print(temperatures)

temperatures_ind = temperatures.set_index('city')
print('\n set_index(city): \n')
print(temperatures_ind.head(5))

print('\n reset_index(): \n')
print(temperatures_ind.reset_index().head(5))

print('\n drop the current index, reset_index(drop=True): \n')
print(temperatures_ind.reset_index(drop=True).head(5))

###
cities = ['New York', 'London']
print('\n  df[boolean_condition] → selects rows: \n')
print(temperatures[temperatures['city'].isin(cities)])

print('\n df.loc[index_values] → selects rows by index labels: \n')
print(temperatures_ind.loc[cities])


########
print('\nIndex temperatures by country & city\n')
temperatures_ind = temperatures.set_index(['country','city'])
print(temperatures_ind)

print('\n df.loc[index_values] → selects rows by index labels: \n')
rows_to_keep =  [('United States', 'New York'), ('United Kingdom', 'London')]
print(temperatures_ind.loc[rows_to_keep])

#######
print('\n sort_index() sorts rows by index : \n')
print(temperatures_ind.sort_index())

print('\n sort_index(level=...): \n')
print(temperatures_ind.sort_index(level='city'))

print('\n sort_index(level=..., ascending=...): \n')
print(temperatures_ind.sort_index(level=['country','city'], ascending=[True, False]))

#######
print('\n iloc - Position-based selection using integer positions: \n')
print('First 3 rows and first 2 columns:')
print(temperatures.iloc[0:3, 0:2])

print('\nSpecific rows and columns by position:')
print(temperatures.iloc[[0, 5, 10], [1, 3]])  # rows 0,5,10 and columns 1,3


#######
print('\n iloc - Position-based selection using integer positions: \n')
print('First 3 rows and first 2 columns:')
print(temperatures.iloc[0:3, 0:2])

print('\nSpecific rows and columns by position:')
print(temperatures.iloc[[0, 5, 10], [1, 3]])  # rows 0,5,10 and columns 1,3
