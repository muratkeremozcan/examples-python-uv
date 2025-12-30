import pandas as pd

# Sample data for a later example (kept in a separate file).
from taxi_data import taxi_owners, taxi_veh

# Key takeaways (inner join, one to one - each key appears once in both tables):
# - "Table" and "DataFrame" mean the same thing here; merging/joining is combining tables.
# - merge() matches rows on a key column; inner join keeps only keys present in both tables.
# - The left DataFrame's columns come first; overlap gets suffixes (default _x/_y).
# - Use suffixes=() to make overlaps readable (e.g., '_ward' vs '_cen').
# - Contrast: in 13_transforming_list_like_column.py, merge() aligned by index to
#   reattach exploded values; here we merge two related tables by a shared key column.

# Local government offices by ward (left table).
wards = pd.DataFrame(
    {
        "ward": [1, 2, 3],
        "alderman": ["Daniel La Spata", "Brian Hopkins", "Pat Dowell"],
        "address": ["123 Main St", "456 Oak St", "789 Pine St"],
        "zip": [60601, 60602, 60603],
    }
)
#    ward         alderman      address    zip
# 0     1  Daniel La Spata  123 Main St  60601
# 1     2    Brian Hopkins   456 Oak St  60602
# 2     3       Pat Dowell  789 Pine St  60603

# Census population by ward (right table).
census = pd.DataFrame(
    {
        "ward": [1, 2, 4],
        "pop_2000": [54991, 54361, 50449],
        "pop_2010": [56178, 54891, 51520],
        "address": ["100 Center Ave", "200 Center Ave", "400 Center Ave"],
        "zip": [60601, 60602, 60604],
    }
)
#    ward  pop_2000  pop_2010         address    zip
# 0     1     54991     56178  100 Center Ave  60601
# 1     2     54361     54891  200 Center Ave  60602
# 2     4     50449     51520  400 Center Ave  60604

# Inner join default behavior; only shows the matching rows (ward 1, 2)
# df1.merge(df2, on="key")
wards_census = wards.merge(census, on="ward")
# print(wards_census)
#    ward         alderman    address_x  zip_x  pop_2000  pop_2010       address_y  zip_y
# 0     1  Daniel La Spata  123 Main St  60601     54991     56178  100 Center Ave  60601
# 1     2    Brian Hopkins   456 Oak St  60602     54361     54891  200 Center Ave  60602

# Control overlapping column names with suffixes.
# df1.merge(df2, on="key", suffixes=("_foo", "_bar"))
wards_census = wards.merge(census, on="ward", suffixes=("_ward", "_cen"))
# print(wards_census)
#    ward         alderman address_ward  zip_ward  pop_2000  pop_2010     address_cen  zip_cen
# 0     1  Daniel La Spata  123 Main St     60601     54991     56178  100 Center Ave    60601
# 1     2    Brian Hopkins   456 Oak St     60602     54361     54891  200 Center Ave    60602
