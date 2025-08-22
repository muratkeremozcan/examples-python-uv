import pandas as pd

demo = pd.DataFrame({
    'type': ['A','A','B','B','C','C','D','D'],
    'is_holiday': [False, True, False, True, False, True, False, True],
    'weekly_sales': [100, 120, 80, 140, 60, 90, 110, 130],
    'temperature': [25, 28, 22, 26, 30, 32, 20, 24]
})

print("Original data:")
print(demo)

# Create pivot table: type & is_holiday as rows, weekly_sales as values
pivot = demo.pivot_table(values='weekly_sales', index=['type', 'is_holiday'])
print("\nPivot table:")
print(pivot)

# Slice by type A to C
print("\nSlice types B to C:")
print(pivot.loc['B':'C'])

# Slice specific combinations
print("\nSlice from (A, False) to (B, True):")
print(pivot.loc[('A', False):('B', True)])


# axis=0 = rows (goes DOWN)
# axis=1 = columns (goes ACROSS)

# Calculate mean across types (axis=0)
print("\naxis=0 = rows (goes DOWN):")
print(pivot.mean(axis=0))

# Calculate mean across holiday status (axis=1) 
print("\naxis=1 = columns (goes ACROSS):")
print(pivot.mean(axis=1))
