import pandas as pd

# Key takeaways (outer join):
# - how="outer" keeps all rows from both tables.
# - Non-matching rows fill missing columns with NaN.
# - Useful for spotting keys that exist in only one table.

# Reuse the ward/census story: wards (left) and census (right).
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

# Outer join keeps ward 3 (only in wards) and ward 4 (only in census).
wards_census_outer = wards.merge(
    census, on="ward", how="outer", suffixes=("_ward", "_cen")
)
print(wards_census_outer)
