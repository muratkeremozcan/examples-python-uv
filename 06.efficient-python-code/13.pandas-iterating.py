# .iloc is useful for row/column access by position, but not optimal for performance.
# Vectorized NumPy operations are fastest — they operate on full arrays at once and avoid Python loops.

# Vectorization means letting array/dataframe operations run in native C/NumPy/pandas routines over whole columns/arrays at once
# instead of looping in Python row by row.
# You write expressions like arr * 2, df["a"] + df["b"], or np.mean(arr, axis=1) and the library does the per-element work under the hood in compiled code.
# Result: much faster and usually clearer, no explicit Python for-loops.


# Meta: prefer NumPy/pandas vectorization first. If you must loop rows, .itertuples() is the least slow; .apply(axis=1) is convenient but slower.

# Performance ranking (fastest → slowest):
# 1.	✅ NumPy vectorization
# 2.	🟡 .itertuples()
# 3.	🔴 .apply() with axis=1 (convenient, but slow)

# Prefer vectorization when:
# • Working with numeric columns
# • Applying mathematical functions
# • Writing performance-sensitive code
# Use .apply() only when:
# • You need row-wise custom logic that’s hard to vectorize

#  use itertuples rarely, only when:
# •	You must loop row by row (e.g. row-dependent I/O, conditionals, or side effects).
# •	Performance matters more than flexibility (it’s faster than .iterrows()).
# •	Vectorization isn’t possible.


# JS usually gets a pass because most frontend work isn’t CPU-heavy and you’re already in a JIT’d runtime. When you
#   do need speed, you reach for typed arrays/WebGL/wasm or libraries like TensorFlow.js/Lodash—but there’s no built-in
#   NumPy equivalent, so “vectorization” is less idiomatic. In Python’s data stack, these choices matter a lot because
#   pure-Python loops are slow and NumPy/pandas give you compiled paths for big arrays.

import numpy as np
import pandas as pd

baseball_df = pd.DataFrame(
    {
        "Team": ["ARI", "ATL", "BAL", "BOS", "CHC", "PHI", "PIT", "SFG", "STL", "WSA"],
        "League": ["NL", "NL", "AL", "AL", "NL", "NL", "NL", "NL", "NL", "AL"],
        "Year": [2012, 2012, 2012, 2012, 2012, 1962, 1962, 1962, 1962, 1962],
        "RS": [734, 700, 712, 734, 613, 705, 706, 878, 774, 599],  # Runs Scored
        "RA": [688, 600, 705, 806, 759, 759, 626, 690, 664, 716],  # Runs Allowed
        "W": [81, 94, 93, 69, 61, 81, 93, 103, 84, 60],  # Wins
        "G": [162, 162, 162, 162, 162, 161, 161, 165, 163, 162],  # Games
        "Playoffs": [0, 1, 1, 0, 0, 0, 0, 1, 0, 0],
    }
)


def calc_win_perc(wins, games_played):
    win_perc = wins / games_played
    return np.round(win_perc, 2)


win_percs_list = []

for i in range(len(baseball_df)):
    row = baseball_df.iloc[i]

    wins = row["W"]
    games_played = row["G"]

    win_perc = calc_win_perc(wins, games_played)

    win_percs_list.append(win_perc)

baseball_df["WP"] = win_percs_list

print(baseball_df, "\n")

################### (alternative with numpy)
# Let's update this analysis to use arrays instead of the .iloc

win_percs_np = calc_win_perc(baseball_df["W"].values, baseball_df["G"].values)
print(win_percs_np, "\n")

# Append a new column to baseball_df that stores all win percentages
baseball_df["WP"] = win_percs_np
print(baseball_df.head(), "\n")


############
def predict_win_perc(RS, RA):
    prediction = RS**2 / (RS**2 + RA**2)
    return np.round(prediction, 2)


# (approach 1 - slowest)  apply the function to each row of the DataFrame with a lambda function
win_perc_preds_apply = baseball_df.apply(
    lambda row: predict_win_perc(row["RS"], row["RA"]), axis=1
)

# (approach 2 - medium) Use a for loop and .itertuples()
win_perc_preds_loop = []

for row in baseball_df.itertuples():
    runs_scored = row.RS
    runs_allowed = row.RA
    win_perc_pred = predict_win_perc(runs_scored, runs_allowed)
    win_perc_preds_loop.append(win_perc_pred)

print(win_perc_preds_loop, "\n")


# (approach 3 - fastest) # using NumPy
# .values turns the pandas columns into NumPy arrays,
# predict_win_perc runs NumPy ops (RS**2, RA**2, np.round) on those arrays element-wise.
# That combination is the vectorized/NumPy path.
win_perc_preds_np = predict_win_perc(baseball_df["RS"].values, baseball_df["RA"].values)

baseball_df["WP_preds"] = win_perc_preds_np
print(baseball_df.head())
