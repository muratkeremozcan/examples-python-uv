# - pivot reshapes long -> wide only when each index/column pair is unique; it cannot aggregate duplicates.
# - pivot_table reshapes and aggregates duplicates via aggfunc (default mean, but you should state it) —
#   use this when you need summary stats or have repeats.

# Extra pivot_table features: multiple agg funcs, multi-index inputs/outputs,
# margins=True for totals, omit values to aggregate all numeric columns.

import pandas as pd

fifa_players = pd.DataFrame(
    {
        "name": [
            "L. Messi",
            "Cristiano Ronaldo",
            "L. Messi",
            "Cristiano Ronaldo",
            "L. Messi",
            "Cristiano Ronaldo",
            "L. Messi",
        ],
        "movement": [
            "shooting",
            "shooting",
            "passing",
            "passing",
            "dribbling",
            "dribbling",
            "dribbling",
        ],
        "overall": [92, 93, 92, 82, 96, 89, 88],
        "attacking": [70, 89, 92, 83, 88, 84, 97],
    }
)
#                name   movement  overall  attacking
# 0           L. Messi   shooting       92         70
# 1  Cristiano Ronaldo   shooting       93         89
# 2           L. Messi    passing       92         92
# 3  Cristiano Ronaldo    passing       82         83
# 4           L. Messi  dribbling       96         88
# 5  Cristiano Ronaldo  dribbling       89         84
# 6           L. Messi  dribbling       88         97

# Pivot works when the pairs are unique (drop one duplicate row to prove it).
fifa_drop = fifa_players.drop(4, axis=0)
print(fifa_drop)
#                 name   movement  overall  attacking
# 0           L. Messi   shooting       92         70
# 1  Cristiano Ronaldo   shooting       93         89
# 2           L. Messi    passing       92         92
# 3  Cristiano Ronaldo    passing       82         83
# 5  Cristiano Ronaldo  dribbling       89         84
# 6           L. Messi  dribbling       88         97

# Pivot fails when the pair repeats (L. Messi/dribbling appears twice).
print("\nPivot with duplicates raises:")
try:
    fifa_players.pivot(index="name", columns="movement")
except ValueError as exc:
    print(exc)
print("\n")


# Use pivot method to get all scores by name and movement
fifa_pivot = fifa_drop.pivot(index="name", columns="movement")
print("pivot:")
print(fifa_pivot)
print("\n")
#                     overall                  attacking
# movement          dribbling passing shooting dribbling passing shooting
# name
# Cristiano Ronaldo        89      82       93        84      83       89
# L. Messi                 88      92       92        97      92       70

# Pivot table handles duplicates because it aggregates.
# Explicit aggfunc shows how duplicates are resolved per column.
fifa_pivot_table = fifa_players.pivot_table(
    index="name", columns="movement", aggfunc="mean"
)
print("pivot_table:")
print(fifa_pivot_table)
print("\n")
#                   attacking                    overall
# movement          dribbling passing shooting dribbling passing shooting
# name
# Cristiano Ronaldo      84.0    83.0     89.0      89.0    82.0     93.0
# L. Messi               92.5    92.0     70.0      92.0    92.0     92.0


# pivot table has additional features like aggfunc, margins, etc.
fifa_pivot_table = fifa_players.pivot_table(
    index="name",
    columns="movement",
    values=["overall", "attacking"],
    aggfunc={"overall": "max", "attacking": "mean"},
    margins=True,  # adds subtotals
)
print("\nPivot table output (aggregated):\n")
print(fifa_pivot_table)
#                    attacking                               overall
# movement           dribbling passing shooting        All dribbling passing shooting All
# name
# Cristiano Ronaldo  84.000000    83.0     89.0  85.333333      89.0    82.0     93.0  93
# L. Messi           92.500000    92.0     70.0  86.750000      96.0    92.0     92.0  96
# All                89.666667    87.5     79.5  86.142857      96.0    92.0     93.0  96
