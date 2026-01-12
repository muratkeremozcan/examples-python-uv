import pandas as pd

# Key takeaways (one-to-many):
# - Same merge syntax as one-to-one.
# - Left rows repeat when the right table has many matches.
# - Row count grows after the merge.

# Ward-level data (one row per ward).
wards = pd.DataFrame(
    {
        "ward": [1, 2, 3],
        "alderman": ["Daniel La Spata", "Brian Hopkins", "Pat Dowell"],
        "address": ["123 Main St", "456 Oak St", "789 Pine St"],
        "zip": [60601, 60602, 60603],
    }
)
# print(wards)
#    ward         alderman      address    zip
# 0     1  Daniel La Spata  123 Main St  60601
# 1     2    Brian Hopkins   456 Oak St  60602
# 2     3       Pat Dowell  789 Pine St  60603
# print(wards.shape) # (3, 4): 3 wards, 4 columns

# License data (many rows per ward).
licenses = pd.DataFrame(
    {
        "license_id": [101, 102, 103, 104, 105],
        "business": ["Cafe A", "Shop B", "Diner C", "Salon D", "Gym E"],
        "ward": [1, 1, 2, 1, 3],
        "address": [
            "10 Lake St",
            "20 Lake St",
            "30 State St",
            "40 Lake St",
            "50 Park Ave",
        ],
    }
)
# print(licenses)
#    license_id business  ward      address
# 0         101   Cafe A     1   10 Lake St
# 1         102   Shop B     1   20 Lake St
# 2         103  Diner C     2   30 State St
# 3         104  Salon D     1   40 Lake St
# 4         105   Gym E      3   50 Park Ave

# One-to-many merge on ward; ward 1 repeats because it has multiple businesses.
wards_licenses = wards.merge(licenses, on="ward")
print(wards_licenses)
# ward         alderman     address_x    zip    license_id  business    address_y
# 0     1  Daniel La Spata  123 Main St  60601         101   Cafe A   10 Lake St
# 1     1  Daniel La Spata  123 Main St  60601         102   Shop B   20 Lake St
# 2     1  Daniel La Spata  123 Main St  60601         104  Salon D   40 Lake St
# 3     2    Brian Hopkins   456 Oak St  60602         103  Diner C   30 State St
# 4     3       Pat Dowell  789 Pine St  60603         105    Gym E   50 Park Ave

print(wards_licenses.shape)  # (5, 7): 5 total rows, 7 columns
print()

#########################
# "Spice" exercise: groupby + agg + sort using the same merge result

# Count how many licenses each ward (or alderman) has in the merged table.
counted_df = wards_licenses.groupby("ward").agg({"license_id": "count"})
# print(counted_df)
# print()
#       license_id
# ward
# 1              3
# 2              1
# 3              1

# # Sort wards by license count (descending).
sorted_df = counted_df.sort_values(by="license_id", ascending=False)
print(sorted_df)
print()


print(sorted_df.head())
