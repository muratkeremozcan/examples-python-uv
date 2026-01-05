import pandas as pd

# Key takeaways (left/right join):
# - how="left" keeps all left rows; how="right" keeps all right rows.
# - Non-matches become NaN on the other side.
# - Same merge() syntax as inner joins.

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
# print(wards_census)
#    ward         alderman address_ward  zip_ward  pop_2000  pop_2010     address_cen  zip_cen
# 0     1  Daniel La Spata  123 Main St     60601     54991     56178  100 Center Ave    60601
# 1     2    Brian Hopkins   456 Oak St     60602     54361     54891  200 Center Ave    60602

# left join gets the intersection of the two tables on the key + the remaining left table key (ward 3 in this example)
# df1.merge(df2, on="key", how="left", suffixes=("_foo", "_bar"))
wards_census_left = wards.merge(
    census, on="ward", how="left", suffixes=("_ward", "_cen")
)
# print(wards_census_left)
#    ward         alderman address_ward  zip_ward  pop_2000  pop_2010     address_cen  zip_cen
# 0     1  Daniel La Spata  123 Main St     60601   54991.0   56178.0  100 Center Ave  60601.0
# 1     2    Brian Hopkins   456 Oak St     60602   54361.0   54891.0  200 Center Ave  60602.0
# 2     3       Pat Dowell  789 Pine St     60603       NaN       NaN             NaN      NaN

# right join gets the intersection of the two tables on the key + the remaining right table key (ward 4 in this example)
# df1.merge(df2, on="key", how="right", suffixes=("_foo", "_bar"))
wards_census_right = wards.merge(
    census, on="ward", how="right", suffixes=("_ward", "_cen")
)
# print(wards_census_right)
#    ward         alderman address_ward  zip_ward  pop_2000  pop_2010     address_cen  zip_cen
# 0     1  Daniel La Spata  123 Main St   60601.0     54991     56178  100 Center Ave    60601
# 1     2    Brian Hopkins   456 Oak St   60602.0     54361     54891  200 Center Ave    60602
# 2     4              NaN          NaN       NaN     50449     51520  400 Center Ave    60604


#####
# joining with left and right with different key names
# sometimes we need to join on columns with different names; we can use right_on, left_on

# modification for the demo
census_right_varying_keys = census.rename(columns={"ward": "ward_id"})
# print(census_right_varying_keys)
#    ward_id  pop_2000  pop_2010         address    zip
# 0        1     54991     56178  100 Center Ave  60601
# 1        2     54361     54891  200 Center Ave  60602
# 2        4     50449     51520  400 Center Ave  60604

# df1.merge(df2, on="key", how="right", left_on="some_key", right_on="other_key", suffixes=("_foo", "_bar"))
wards_census_right_varying_keys = wards.merge(
    census_right_varying_keys,
    left_on="ward",
    right_on="ward_id",
    how="right",
    suffixes=("_ward", "_cen"),
)
print(wards_census_right_varying_keys)
#    ward         alderman address_ward  zip_ward  ward_id  pop_2000  pop_2010     address_cen  zip_cen
# 0   1.0  Daniel La Spata  123 Main St   60601.0        1     54991     56178  100 Center Ave    60601
# 1   2.0    Brian Hopkins   456 Oak St   60602.0        2     54361     54891  200 Center Ave    60602
# 2   NaN              NaN          NaN       NaN        4     50449     51520  400 Center Ave    60604
