import pandas as pd

# Key takeaways (stack/unstack with multiple levels):
# - `swaplevel` changes index level order before reshaping.
# - `unstack` moves row levels to columns.
# - `stack` moves column levels to rows.
# - You can pass a list of levels to move multiple levels at once.
# - Missing combinations create NaN values after `unstack`; use `fillna` if needed.


columns = pd.MultiIndex.from_product(
    [[2019, 2020], ["minutes", "voicemail", "data"]],
    names=["year", "plan"],
)
index = pd.MultiIndex.from_arrays(
    [
        ["churn", "no_churn", "churn", "no_churn"],
        ["California", "California", "New York", "New York"],
        ["Los Angeles", "Los Angeles", "New York", "New York"],
    ],
    names=["exited", "state", "city"],
)
churn = pd.DataFrame(
    [
        [0, 1, 2, 1, 1, 5],
        [0, 1, 3, 1, 0, 2],
        [1, 0, 5, 0, 1, 2],
        [1, 0, 4, 1, 0, 6],
    ],
    index=index,
    columns=columns,
)

# year                               2019                   2020
# plan                            minutes voicemail data minutes voicemail data
# exited   state      city
# churn    California Los Angeles       0         1    2       1         1    5
# no_churn California Los Angeles       0         1    3       1         0    2
# churn    New York   New York          1         0    5       0         1    2
# no_churn New York   New York          1         0    4       1         0    6

# 1) swaplevel to pick which row level moves later: bring city up before unstacking.
churn_swap = churn.swaplevel(0, 2)
# year                               2019                   2020
# plan                            minutes voicemail data minutes voicemail data
# city        state      exited
# Los Angeles California churn          0         1    2       1         1    5
#                        no_churn       0         1    3       1         0    2
# New York    New York   churn          1         0    5       0         1    2
#                        no_churn       1         0    4       1         0    6

# 2) unstack the last index/row level (exited) into columns; city/state stay as rows.
churn_unstack = churn_swap.unstack()
# year                      2019                                               2020
# plan                     minutes            voicemail            data          minutes            voicemail            data
# exited                   churn no_churn     churn no_churn     churn no_churn   churn no_churn     churn no_churn     churn no_churn
# city        state
# Los Angeles California       0        0      1        1         2        3       1        1      		1        0      			5        2
# New York    New York         1        1      0        0         5        4       0        1      		1        0      			2        6

# 3) unstack multiple row levels at once (exited, state) by position.
churn_unstack = churn.unstack(level=[0, 1])
# year              2019                                                                                                                    2020                                                   \
# plan           minutes                               voicemail                                    data                                 minutes                               voicemail
# exited           churn            no_churn               churn            no_churn               churn            no_churn               churn            no_churn               churn
# state       California New York California New York California New York California New York California New York California New York California New York California New York California New York
# city
# Los Angeles        0.0      NaN        0.0      NaN        1.0      NaN        1.0      NaN        2.0      NaN        3.0      NaN        1.0      NaN        1.0      NaN        1.0      NaN
# New York           NaN      1.0        NaN      1.0        NaN      0.0        NaN      0.0        NaN      5.0        NaN      4.0        NaN      0.0        NaN      1.0        NaN      1.0

# 4) stack multiple column levels (plan, year) back into the row index.
churn_py = churn_unstack.stack(level=["plan", "year"])
# exited                          churn            no_churn
# state                      California New York California New York
# city        plan      year
# Los Angeles data      2019        2.0      NaN        3.0      NaN
#                       2020        5.0      NaN        2.0      NaN
#             minutes   2019        0.0      NaN        0.0      NaN
#                       2020        1.0      NaN        1.0      NaN
#             voicemail 2019        1.0      NaN        1.0      NaN
#                       2020        1.0      NaN        0.0      NaN
# New York    data      2019        NaN      5.0        NaN      4.0
#                       2020        NaN      2.0        NaN      6.0
#             minutes   2019        NaN      1.0        NaN      1.0
#                       2020        NaN      0.0        NaN      1.0
#             voicemail 2019        NaN      0.0        NaN      0.0
#                       2020        NaN      1.0        NaN      0.0

# 5) swap column levels to reorder exits vs states on the column side.
churn_switch = churn_py.swaplevel(0, 1, axis=1)
# state                      California New York California New York
# exited                          churn    churn   no_churn no_churn
# city        plan      year
# Los Angeles data      2019        2.0      NaN        3.0      NaN
# 											2020        5.0      NaN        2.0      NaN
# 						minutes   2019        0.0      NaN        0.0      NaN
# 											2020        1.0      NaN        1.0      NaN
# 						voicemail 2019        1.0      NaN        1.0      NaN
# 											2020        1.0      NaN        0.0      NaN
# New York    data      2019        NaN      5.0        NaN      4.0
# 											2020        NaN      2.0        NaN      6.0
# 						minutes   2019        NaN      1.0        NaN      1.0
# 											2020        NaN      0.0        NaN      1.0
# 						voicemail 2019        NaN      0.0        NaN      0.0
# 											2020        NaN      1.0        NaN      0.0

# Missing-data handling on the reshaped output:
# - fill NaNs created by unstack with a default (e.g., 0) if absent combos should be treated as zero.
churn_unstack_filled = churn_unstack.fillna(0)
# year              2019                                                                                                                    2020
# plan           minutes                               voicemail                                    data                                 minutes                               voicemail                                    data
# exited           churn            no_churn               churn            no_churn               churn            no_churn               churn            no_churn               churn            no_churn               churn            no_churn
# state       California New York California New York California New York California New York California New York California New York California New York California New York California New York California New York California New York California New York
# city
# Los Angeles        0.0      0.0        0.0      0.0        1.0      0.0        1.0      0.0        2.0      0.0        3.0      0.0        1.0      0.0        1.0      0.0        1.0      0.0        0.0      0.0        5.0      0.0        2.0      0.0
# New York           0.0      1.0        0.0      1.0        0.0      0.0        0.0      0.0        0.0      5.0        0.0      4.0        0.0      0.0        0.0      1.0        0.0      1.0        0.0      0.0        0.0      2.0        0.0      6.0


# - Keep all possible combinations when stacking: set dropna=False, then fill missing values.
churn_full = churn_unstack.stack(level=["plan", "year"], dropna=False).fillna(0)
print(churn_full)
# exited                          churn            no_churn
# state                      California New York California New York
# city        plan      year
# Los Angeles data      2019        2.0      0.0        3.0      0.0
#                       2020        5.0      0.0        2.0      0.0
#             minutes   2019        0.0      0.0        0.0      0.0
#                       2020        1.0      0.0        1.0      0.0
#             voicemail 2019        1.0      0.0        1.0      0.0
#                       2020        1.0      0.0        0.0      0.0
# New York    data      2019        0.0      5.0        0.0      4.0
#                       2020        0.0      2.0        0.0      6.0
#             minutes   2019        0.0      1.0        0.0      1.0
#                       2020        0.0      0.0        0.0      1.0
#             voicemail 2019        0.0      0.0        0.0      0.0
#                       2020        0.0      1.0        0.0      0.0
