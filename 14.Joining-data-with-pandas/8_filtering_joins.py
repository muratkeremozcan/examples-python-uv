import pandas as pd

# Key takeaways (filtering joins):
# - Mutating joins combine columns; filtering joins filter rows based on matches.
# - Semi join keeps left rows that have a match in the right table (left columns only).
# - Anti join keeps left rows that do NOT have a match in the right table.
# - pandas has no direct semi/anti join, but merge + isin/indicator reproduces them.

# - Merge the left and right tables on key column using an inner join.
# - Use .isin() to check if left keys appear in the merged result (Boolean Series).
# - Subset the rows of the left table.


# Reuse the ward/census data to demonstrate filtering joins.
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

census = pd.DataFrame(
    {
        "ward": [1, 2, 4],
        "pop_2000": [54991, 54361, 50449],
        "pop_2010": [56178, 54891, 51520],
        "address": ["100 Center Ave", "200 Center Ave", "400 Center Ave"],
        "zip": [60601, 60602, 60604],
    }
)
# print(census)
#    ward  pop_2000  pop_2010         address    zip
# 0     1     54991     56178  100 Center Ave  60601
# 1     2     54361     54891  200 Center Ave  60602
# 2     4     50449     51520  400 Center Ave  60604

########
# Semi join: Filter rows from left table based on matches in right table.

wards_census = wards.merge(census, on="ward")  # default is how='inner'
# print(wards_census)
#    ward         alderman    address_x  zip_x  pop_2000  pop_2010       address_y  zip_y
# 0     1  Daniel La Spata  123 Main St  60601     54991     56178  100 Center Ave  60601
# 1     2    Brian Hopkins   456 Oak St  60602     54361     54891  200 Center Ave  60602

# ward values that matched in both tables.

ward_matches = wards_census["ward"]  # wards.merge(census, on="ward")["ward"]
# print(ward_matches)
# 0    1
# 1    2
top_wards = wards[wards["ward"].isin(ward_matches)]
# print(top_wards)
#    ward         alderman      address    zip
# 0     1  Daniel La Spata  123 Main St  60601
# 1     2    Brian Hopkins   456 Oak St  60602

# Note: With unique keys, semi join and inner join return the same left rows.
# The difference shows up when the right table has multiple matches per key.
licenses = pd.DataFrame(
    {
        "license_id": [101, 102, 103, 104],
        "business": ["Cafe A", "Shop B", "Diner C", "Salon D"],
        "ward": [1, 1, 2, 1],
    }
)
# print(licenses)
#    license_id business  ward
# 0         101   Cafe A     1
# 1         102   Shop B     1
# 2         103  Diner C     2
# 3         104  Salon D     1

wards_licenses = wards.merge(licenses, on="ward")  # duplicates ward 1
# print(wards_licenses)
#    ward         alderman      address    zip  license_id business
# 0     1  Daniel La Spata  123 Main St  60601         101   Cafe A
# 1     1  Daniel La Spata  123 Main St  60601         102   Shop B
# 2     1  Daniel La Spata  123 Main St  60601         104  Salon D
# 3     2    Brian Hopkins   456 Oak St  60602         103  Diner C
ward_matches_many = wards_licenses["ward"]
top_wards_many = wards[wards["ward"].isin(ward_matches_many)]
# print(wards_licenses[["ward", "business"]])
# print(top_wards_many)
#    ward         alderman      address    zip
# 0     1  Daniel La Spata  123 Main St  60601
# 1     2    Brian Hopkins   456 Oak St  60602

# ########################
# Anti join: Keep rows from left table that do NOT have a match in the right table.

# indicator=True adds a _merge column showing whether each row matched (both/left_only/right_only).
wards_census_left = wards.merge(census, on="ward", how="left", indicator=True)
# print(wards_census_left)
#    ward         alderman    address_x  zip_x  pop_2000  pop_2010       address_y    zip_y     _merge
# 0     1  Daniel La Spata  123 Main St  60601   54991.0   56178.0  100 Center Ave  60601.0       both
# 1     2    Brian Hopkins   456 Oak St  60602   54361.0   54891.0  200 Center Ave  60602.0       both
# 2     3       Pat Dowell  789 Pine St  60603       NaN       NaN             NaN      NaN  left_only

# keep rows that only appear in the left table.
# .loc[rows, cols], the second argument picks which columns to return.
#
missing_ward_ids = wards_census_left.loc[
    wards_census_left["_merge"] == "left_only", "ward"
]
missing_wards = wards[wards["ward"].isin(missing_ward_ids)]
# print(missing_wards)
# 	ward    alderman      address    zip
# 2     3  Pat Dowell  789 Pine St  60603
