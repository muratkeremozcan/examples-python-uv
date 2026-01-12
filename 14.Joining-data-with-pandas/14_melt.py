import pandas as pd

# Key takeaways (melt):
# - melt() unpivots wide data into long (tall) format.
# - id_vars stay fixed; other columns become rows.
# - value_vars lets you pick which columns to unpivot.
# - var_name/value_name rename the output columns.

# Wide format: years across columns.
social_fin = pd.DataFrame(
    {
        "company": ["Facebook", "Twitter"],
        "2016": [27.6, 2.5],
        "2017": [40.7, 2.4],
        "2018": [55.8, 3.0],
        "2019": [70.7, 3.5],
    }
)
# print(social_fin)
#     company  2016  2017  2018  2019
# 0  Facebook  27.6  40.7  55.8  70.7
# 1   Twitter   2.5   2.4   3.0   3.5


# Basic melt: all non id_vars columns become rows.
fin_long = social_fin.melt(id_vars="company")
# print(fin_long.head())
#     company variable  value
# 0  Facebook     2016   27.6
# 1   Twitter     2016    2.5
# 2  Facebook     2017   40.7
# 3   Twitter     2017    2.4
# 4  Facebook     2018   55.8

# value_vars lets you pick the columns to melt
fin_2018_2017 = social_fin.melt(id_vars="company", value_vars=["2018", "2017"])
print(fin_2018_2017)
#     company variable  value
# 0  Facebook     2018   55.8
# 1   Twitter     2018    3.0
# 2  Facebook     2017   40.7
# 3   Twitter     2017    2.4

# var_name and value_name let you rename the output columns
fin_named = social_fin.melt(
    id_vars="company",
    value_vars=["2018", "2017"],
    var_name="year",
    value_name="dollars",
)
print(fin_named)
#     company  year  dollars
# 0  Facebook  2018     55.8
# 1   Twitter  2018      3.0
# 2  Facebook  2017     40.7
# 3   Twitter  2017      2.4
