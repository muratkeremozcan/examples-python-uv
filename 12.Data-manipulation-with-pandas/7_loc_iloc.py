# SLICE = select a continuous range/subset of data
# .loc[] = uses LABELS (index names, column names) - needs sorted index for slicing
# .iloc[] = uses INTEGER POSITIONS (0, 1, 2...) - works like Python lists
# Single index: Slice with strings 'A':'C' (gets A, B, C)
# Multi-index: Slice with tuples ('A', False):('B', True)
# Column slicing: Use : for all rows, then column range
# Both directions: Combine row slice + column slice

import pandas as pd

demo = pd.DataFrame(
    {
        "type": ["A", "A", "B", "B", "C", "C", "D", "D"],
        "is_holiday": [False, True, False, True, False, True, False, True],
        "weekly_sales": [100, 120, 80, 140, 60, 90, 110, 130],
        "temperature": [25, 28, 22, 26, 30, 32, 20, 24],
    }
)

print("Original demo:")
print(demo)

print("\n=== .loc[] examples (LABEL-based) ===")

print("\n1. You can only slice with a SORTED INDEX")
demo_srt = demo.set_index("type").sort_index()
print(demo_srt)

print("\n2. SLICE rows with strings: loc['A':'C'] (gets A, B, C)")
print(demo_srt.loc["A":"C"])

print("\n3. Multi-level index for tuple slicing")
demo_multi = demo.set_index(["type", "is_holiday"]).sort_index()
print(demo_multi)

print("\n4. SLICE with tuples: loc[(A, False):(C, False)] - continuous range")
print(demo_multi.loc[("A", False):("C", False)])

print("\n5. SLICE columns: gets all columns from weekly_sales to temperature")
print(demo_multi.loc[:, "weekly_sales":"temperature"])

print("\n6. SLICE both rows AND columns - subset of both")
print(demo_multi.loc[("A", False):("B", True), "weekly_sales":"temperature"])


################

print("\n=== .iloc[] examples (POSITION-based) ===")

print("\n7. Get single cell by position: row 1, column 2")
print(demo.iloc[1, 2])

print("\n8. Slice first 3 rows by position:")
print(demo.iloc[0:3])

print("\n9. Slice columns 1-2 by position:")
print(demo.iloc[:, 1:3])

print("\n10. Slice both rows AND columns by position:")
print(demo.iloc[0:4, 1:3])

print("\n11. Select specific rows/columns by position:")
print(demo.iloc[[0, 2, 4], [0, 3]])
