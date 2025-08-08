# .iterrows()  lets you loop through a DataFrame row by row

import pandas as pd

pit_df = pd.DataFrame(
    {
        "Team": ["PIT"] * 5,
        "League": ["NL"] * 5,
        "Year": [2012, 2011, 2010, 2009, 2008],
        "RS": [651, 610, 587, 636, 735],  # Runs Scored
        "RA": [674, 712, 866, 768, 884],  # Runs Allowed
        "W": [79, 72, 57, 62, 67],  # Wins
        "G": [162, 162, 162, 161, 162],  # Games
        "Playoffs": [0, 0, 0, 0, 0],
    }
)
# print(pit_df)
#   Team League  Year   RS   RA   W    G  Playoffs
# 0  PIT     NL  2012  651  674  79  162         0
# 1  PIT     NL  2011  610  712  72  162         0
# 2  PIT     NL  2010  587  866  57  162         0
# 3  PIT     NL  2009  636  768  62  161         0
# 4  PIT     NL  2008  735  884  67  162         0


# Iterate over pit_df and print each row
for index, row in pit_df.iterrows():
    print(index)
    print(row)

# 0
# Team         PIT
# League        NL
# Year        2012
# RS           651
# RA           674
# W             79
# G            162
# Playoffs       0
# Name: 0, dtype: object

# 1
# Team         PIT
# League        NL
# Year        2011
# RS           610
# RA           712
# W             72
# G            162
# Playoffs       0
# Name: 1, dtype: object

for row_tuple in pit_df.iterrows():
    print(row_tuple)


print("\n --------------------")
# (0, Team         PIT
# League        NL
# Year        2012
# RS           651
# RA           674
# W             79
# G            162
# Playoffs       0
# Name: 0, dtype: object)

# (1, Team         PIT
# League        NL
# Year        2011
# RS           610
# RA           712
# W             72
# G            162
# Playoffs       0
# Name: 1, dtype: object)


##############################################

giants_df = pd.DataFrame(
    {
        "Team": ["SFG"] * 5,
        "League": ["NL"] * 5,
        "Year": [2012, 2011, 2010, 2009, 2008],
        "RS": [718, 570, 697, 657, 640],  # Runs Scored
        "RA": [649, 578, 583, 611, 759],  # Runs Allowed
        "W": [94, 86, 92, 88, 72],  # Wins
        "G": [162, 162, 162, 162, 162],  # Games
        "Playoffs": [1, 0, 1, 0, 0],
    }
)

#   Team League  Year   RS   RA   W    G  Playoffs
# 0  SFG     NL  2012  718  649  94  162         1
# 1  SFG     NL  2011  570  578  86  162         0
# 2  SFG     NL  2010  697  583  92  162         1
# 3  SFG     NL  2009  657  611  88  162         0
# 4  SFG     NL  2008  640  759  72  162         0

run_diffs = []

for index, row in giants_df.iterrows():
    runs_scored = row["RS"]
    runs_allowed = row["RA"]
    run_diff = runs_scored - runs_allowed
    run_diffs.append(run_diff)

giants_df["RD"] = run_diffs
print(giants_df)
#   Team League  Year   RS   RA   W    G  Playoffs   RD
# 0  SFG     NL  2012  718  649  94  162         1   69
# 1  SFG     NL  2011  570  578  86  162         0   -8
# 2  SFG     NL  2010  697  583  92  162         1  114
# 3  SFG     NL  2009  657  611  88  162         0   46
# 4  SFG     NL  2008  640  759  72  162         0 -119
