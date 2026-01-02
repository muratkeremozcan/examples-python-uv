import pandas as pd

# Key takeaways (self join):
# - A self join merges a table to itself to link related rows (sequels, managers, chains).
# - Use left_on/right_on to match different columns within the same table.
# - Inner self join only keeps rows with matches; left self join keeps all originals.
# - suffixes=() clarifies which columns describe the original vs the related row.

# Reuse the licenses data from earlier lessons.
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

# Add a "successor" relationship to mimic sequels.
# Think of successor_id as "the next license in a chain".
licenses_seq = licenses.assign(successor_id=[102, 103, 105, pd.NA, pd.NA])
# print(licenses_seq)
#    license_id business  ward      address successor_id
# 0         101   Cafe A     1   10 Lake St          102
# 1         102   Shop B     1   20 Lake St          103
# 2         103  Diner C     2  30 State St          105
# 3         104  Salon D     1   40 Lake St         <NA>
# 4         105    Gym E     3  50 Park Ave         <NA>

# Inner self join: only rows with a valid successor_id appear.
licenses_inner = licenses_seq.merge(
    licenses_seq,
    left_on="successor_id",
    right_on="license_id",
    suffixes=("_org", "_seq"),
)
# print(licenses_inner)
#    license_id_org business_org  ward_org  address_org successor_id_org  license_id_seq business_seq  ward_seq  address_seq successor_id_seq
# 0             101       Cafe A         1   10 Lake St              102             102       Shop B         1   20 Lake St              103
# 1             102       Shop B         1   20 Lake St              103             103      Diner C         2  30 State St              105
# 2             103      Diner C         2  30 State St              105             105        Gym E         3  50 Park Ave             <NA>

# print(licenses_inner[["license_id_org", "business_org", "business_seq"]])
#    license_id_org business_org business_seq
# 0             101       Cafe A       Shop B
# 1             102       Shop B      Diner C
# 2             103      Diner C        Gym E

# Left self join: keep all originals, even if the successor is missing.
licenses_left = licenses_seq.merge(
    licenses_seq,
    left_on="successor_id",
    right_on="license_id",
    how="left",
    suffixes=("_org", "_seq"),
)

# print(licenses_left)
#    license_id_org business_org  ward_org  address_org successor_id_org  license_id_seq business_seq  ward_seq  address_seq successor_id_seq
# 0             101       Cafe A         1   10 Lake St              102           102.0       Shop B       1.0   20 Lake St              103
# 1             102       Shop B         1   20 Lake St              103           103.0      Diner C       2.0  30 State St              105
# 2             103      Diner C         2  30 State St              105           105.0        Gym E       3.0  50 Park Ave             <NA>
# 3             104      Salon D         1   40 Lake St             <NA>             NaN          NaN       NaN          NaN              NaN
# 4             105        Gym E         3  50 Park Ave             <NA>             NaN          NaN       NaN          NaN              NaN

print(licenses_left[["license_id_org", "business_org", "business_seq"]])
#    license_id_org business_org business_seq
# 0             101       Cafe A       Shop B
# 1             102       Shop B      Diner C
# 2             103      Diner C        Gym E
# 3             104      Salon D          NaN
# 4             105        Gym E          NaN
