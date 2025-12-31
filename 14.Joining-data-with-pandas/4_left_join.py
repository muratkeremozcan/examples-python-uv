import pandas as pd

# Key takeaways (left join):
# - merge() defaults to an inner join; use how="left" to keep all left rows.
# - Left join returns every row from the left table and only matches from the right.
# - Unmatched right-side columns become NaN (missing data).
# - In one-to-one data, a left join keeps the same row count as the left table.

# Reuse the ward/census story from earlier lessons.
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


# Census is missing ward 3 but includes ward 4 (not in the left table).
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

# regular merge (inner join) gets the intersection of the two tables on the key (ward in this example)
# df1.merge(df2, on="key", suffixes=("_foo", "_bar"))
wards_census = wards.merge(census, on="ward", suffixes=("_ward", "_cen"))
print(wards_census)
#    ward         alderman address_ward  zip_ward  pop_2000  pop_2010     address_cen  zip_cen
# 0     1  Daniel La Spata  123 Main St     60601     54991     56178  100 Center Ave    60601
# 1     2    Brian Hopkins   456 Oak St     60602     54361     54891  200 Center Ave    60602

# left join keeps gets the intersection of the two tables on the key + the remaining left table key (ward 3 in this example)
# left join keeps all wards; ward 3 shows NaNs for missing census data.
# df1.merge(df2, on="key", how="left", suffixes=("_foo", "_bar"))
wards_census_left = wards.merge(
    census, on="ward", how="left", suffixes=("_ward", "_cen")
)
# print(wards_census_left)
#    ward         alderman address_ward  zip_ward  pop_2000  pop_2010     address_cen  zip_cen
# 0     1  Daniel La Spata  123 Main St     60601   54991.0   56178.0  100 Center Ave  60601.0
# 1     2    Brian Hopkins   456 Oak St     60602   54361.0   54891.0  200 Center Ave  60602.0
# 2     3       Pat Dowell  789 Pine St     60603       NaN       NaN             NaN      NaN
