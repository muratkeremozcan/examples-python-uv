# 	.apply() is used to apply a function to a dataframe
# axis=0: vertical, down the DataFrame → column-wise result
# axis=1: horizontal, across the DataFrame → row-wise result
# [['a', 'b']].apply to select certain columns

import numpy as np
import pandas as pd

rays_df = pd.DataFrame(
    {
        "RS": [697, 707, 802, 803, 774],  # Runs Scored
        "RA": [577, 614, 649, 754, 671],  # Runs Allowed
        "W": [90, 91, 96, 84, 97],  # Wins
        "Playoffs": [0, 1, 1, 0, 1],  # Playoffs indicator
    },
    index=[2012, 2011, 2010, 2009, 2008],
)  # Year as index


#        RS   RA   W  Playoffs
# 2012  697  577  90         0
# 2011  707  614  91         1
# 2010  802  649  96         1
# 2009  803  754  84         0
# 2008  774  671  97         1


# axis=0: vertical, down the DataFrame → column-wise result
stat_totals = rays_df.apply(sum, axis=0)
print(stat_totals)

# axis=1: horizontal, across the DataFrame → row-wise result
# [['RS', 'RA']] → selects just those two columns
total_runs_scored = rays_df[["RS", "RA"]].apply(sum, axis=1)

########


# use a lambda instead of "sum"
def text_playoffs(num_playoffs):
    if num_playoffs == 1:
        return "Yes"
    else:
        return "No"


textual_playoffs = rays_df.apply(lambda row: text_playoffs(row["Playoffs"]), axis=1)


#############

dbacks_df = pd.DataFrame(
    {
        "Team": ["ARI"] * 15,
        "League": ["NL"] * 15,
        "Year": [
            2012,
            2011,
            2010,
            2009,
            2008,
            2007,
            2006,
            2005,
            2004,
            2003,
            2002,
            2001,
            2000,
            1999,
            1998,
        ],
        "RS": [
            734,
            731,
            713,
            720,
            720,
            712,
            773,
            696,
            615,
            717,
            819,
            818,
            792,
            908,
            665,
        ],
        "RA": [
            688,
            662,
            836,
            782,
            706,
            732,
            788,
            856,
            899,
            685,
            674,
            677,
            754,
            676,
            812,
        ],
        "W": [81, 94, 65, 70, 82, 90, 76, 77, 51, 84, 98, 92, 85, 100, 65],
        "G": [162] * 15,
        "Playoffs": [0, 1, 0, 0, 0, 1, 0, 0, 0, 0, 1, 1, 0, 1, 0],
    }
)

#    Team League  Year   RS   RA    W    G  Playoffs
# 0   ARI     NL  2012  734  688   81  162         0
# 1   ARI     NL  2011  731  662   94  162         1
# 2   ARI     NL  2010  713  836   65  162         0
# 3   ARI     NL  2009  720  782   70  162         0
# 4   ARI     NL  2008  720  706   82  162         0
# 5   ARI     NL  2007  712  732   90  162         1
# 6   ARI     NL  2006  773  788   76  162         0
# 7   ARI     NL  2005  696  856   77  162         0
# 8   ARI     NL  2004  615  899   51  162         0
# 9   ARI     NL  2003  717  685   84  162         0
# 10  ARI     NL  2002  819  674   98  162         1
# 11  ARI     NL  2001  818  677   92  162         1
# 12  ARI     NL  2000  792  754   85  162         0
# 13  ARI     NL  1999  908  676  100  162         1
# 14  ARI     NL  1998  665  812   65  162         0


# print the first 5 rows
print(dbacks_df.head(5))


def calc_win_percentage(wins, games_played):
    win_percentage = wins / games_played
    return np.round(win_percentage, 2)


# apply the function to each row of the DataFrame with a lambda function
win_percentages = dbacks_df.apply(
    lambda row: calc_win_percentage(row["W"], row["G"]), axis=1
)

# append a new column to dbacks_df
dbacks_df["WP"] = win_percentages
print(dbacks_df, "\n")

# Filter data based on new column: where WP is greater than 0.50
print(dbacks_df[dbacks_df["WP"] >= 0.50])
