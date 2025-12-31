import pandas as pd

# Key takeaways (merging multiple DataFrames):
# - You can merge more than two tables by chaining merge() calls.
# - Use multiple keys (on=[...]) to avoid bad matches on a single column.
# - Matching on address+zip is safer than either alone.
# - Each merge can add suffixes to clarify overlapping columns.
# - After merging, group and summarize to answer the business question.

# Wards table (local government details).
wards = pd.DataFrame(
    {
        "ward": [1, 2, 3],
        "alderman": ["Daniel La Spata", "Brian Hopkins", "Pat Dowell"],
        "office": ["123 Main St", "456 Oak St", "789 Pine St"],
        "zip": [60601, 60602, 60603],
    }
)
# print(wards)
#    ward         alderman      address    zip
# 0     1  Daniel La Spata  123 Main St  60601
# 1     2    Brian Hopkins   456 Oak St  60602
# 2     3       Pat Dowell  789 Pine St  60603

# Licenses table (business location details).
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
# Add zip to support a safer multi-key merge (address + zip).
licenses_with_zip = licenses.assign(zip=[60601, 60601, 60602, 60601, 60603])
# print(licenses_with_zip)
#    license_id business  ward      address    zip
# 0         101   Cafe A     1   10 Lake St  60601
# 1         102   Shop B     1   20 Lake St  60601
# 2         103  Diner C     2  30 State St  60602
# 3         104  Salon D     1   40 Lake St  60601
# 4         105    Gym E     3  50 Park Ave  60603


# Grants table (taxpayer-funded grants).
grants = pd.DataFrame(
    {
        "grant_id": [9001, 9002, 9003, 9004, 9005],
        "business": ["Cafe A", "Cafe A", "Shop B", "Salon D", "Gym E"],
        "address": [
            "10 Lake St",
            "10 Lake St",
            "20 Lake St",
            "40 Lake St",
            "50 Park Ave",
        ],
        "zip": [60601, 60601, 60601, 60601, 60603],
        "grant": [5000, 3000, 7000, 8000, 6000],
    }
)
# print(grants)
#    grant_id business      address    zip  grant
# 0      9001   Cafe A   10 Lake St  60601   5000
# 1      9002   Cafe A   10 Lake St  60601   3000
# 2      9003   Shop B   20 Lake St  60601   7000
# 3      9004  Salon D   40 Lake St  60601   8000
# 4      9005    Gym E  50 Park Ave  60603   6000


# Step 1: merge grants to licenses on address + zip (avoid bad matches on zip only).
grants_licenses = grants.merge(
    licenses_with_zip, on=["address", "zip"], suffixes=("_grant", "_lic")
)
# print(grants_licenses)
#    grant_id business_grant      address    zip  grant  license_id business_lic  ward
# 0      9001         Cafe A   10 Lake St  60601   5000         101       Cafe A     1
# 1      9002         Cafe A   10 Lake St  60601   3000         101       Cafe A     1
# 2      9003         Shop B   20 Lake St  60601   7000         102       Shop B     1
# 3      9004        Salon D   40 Lake St  60601   8000         104      Salon D     1
# 4      9005          Gym E  50 Park Ave  60603   6000         105        Gym E     3


# Step 2: merge the result to wards on ward.
# (Chaining merges is the pattern for 3+ tables.)
# we can shorten it with variable assignments, or we can use chains using \
# grants_licenses_wards = grants_licenses.merge(wards, on="ward", suffixes=("_biz", "_ward"))
grants_licenses_wards = grants.merge(
    licenses_with_zip, on=["address", "zip"], suffixes=("_grant", "_lic")
).merge(wards, on="ward", suffixes=("_biz", "_ward"))
# print(grants_licenses_wards)
#    grant_id business_grant      address  zip_biz  grant  license_id business_lic  ward         alderman       office  zip_ward
# 0      9001         Cafe A   10 Lake St    60601   5000         101       Cafe A     1  Daniel La Spata  123 Main St     60601
# 1      9002         Cafe A   10 Lake St    60601   3000         101       Cafe A     1  Daniel La Spata  123 Main St     60601
# 2      9003         Shop B   20 Lake St    60601   7000         102       Shop B     1  Daniel La Spata  123 Main St     60601
# 3      9004        Salon D   40 Lake St    60601   8000         104      Salon D     1  Daniel La Spata  123 Main St     60601
# 4      9005          Gym E  50 Park Ave    60603   6000         105        Gym E     3       Pat Dowell  789 Pine St     60603

# Summarize total grant money by ward.
# groupby + agg + sort using the same merge result
ward_totals = (
    grants_licenses_wards.groupby(["alderman", "ward"])
    .agg({"grant": "sum"})
    .sort_values(by=["grant", "ward"], ascending=False)
)
print(ward_totals)
print()
#       grant
# alderman  ward
# Daniel La Spata  1    23000
# Pat Dowell       3     6000

# Filter the merged table and sum grants for a specific slice.
filter_criteria = (
    (grants_licenses_wards["ward"] == 1)
    & (grants_licenses_wards["business_grant"] == "Cafe A")
    & (grants_licenses_wards["zip_biz"] == 60601)
)
print("Filter criteria:")
print(filter_criteria)
print("Sum of grants:")
print(grants_licenses_wards.loc[filter_criteria, "grant"].sum())
