# Pivot quick guide (why/when + how)
# - Long (tidy): one row per entity-measure pair; best for plotting, grouped stats, model inputs.
# - Wide: one row per entity with many measure columns; useful for time-series columns, quick comparisons, spreadsheet-style scans.
# - Use pivot for long -> wide: pivot(index=<rows>, columns=<new cols>, values=<cell values>); 
# missing combos become NaN; duplicate index+column pairs raise.


import pandas as pd

# Long -> wide pivot example (matches the screenshot)
weight_long = pd.DataFrame(
    {
        "Name": ["John", "Mary", "Mary", "John", "Laura"],
        "Year": [2013, 2013, 2014, 2014, 2014],
        "Weight": [80, 65, 68, 83, 71],
    }
)
#    Name  Year  Weight
# 0  John  2013      80
# 1  Mary  2013      65
# 2  Mary  2014      68
# 3  John  2014      83
# 4  Laura 2014      71

weight_wide = weight_long.pivot(index="Year", columns="Name", values="Weight")
# Name  John  Laura  Mary
# Year                  
# 2013  80.0    NaN  65.0
# 2014  83.0   71.0  68.0

########################

fifa_players = pd.DataFrame(
    {
        "name": [
            "L. Messi",
            "Cristiano Ronaldo",
            "L. Messi",
            "Cristiano Ronaldo",
            "L. Messi",
            "Cristiano Ronaldo",
        ],
        "movement": [
            "shooting",
            "shooting",
            "passing",
            "passing",
            "dribbling",
            "dribbling",
        ],
        "overall": [92, 93, 92, 82, 96, 89],
        "attacking": [70, 89, 92, 83, 88, 84],
    }
)
#                 name   movement  overall  attacking
# 0           L. Messi   shooting       92         70
# 1  Cristiano Ronaldo   shooting       93         89
# 2           L. Messi    passing       92         92
# 3  Cristiano Ronaldo    passing       82         83
# 4           L. Messi  dribbling       96         88
# 5  Cristiano Ronaldo  dribbling       89         84


# Pivot overall: rows=name, cols=movement, cells=overall score
fifa_overall = fifa_players.pivot(index="name", columns="movement", values="overall")
print(fifa_overall)
# movement           dribbling  passing  shooting
# name                                           
# Cristiano Ronaldo         89       82        93
# L. Messi                  96       92        92

# Same idea for attacking scores
fifa_attacking = fifa_players.pivot(index="name", columns="movement", values="attacking")
print(fifa_attacking)
# movement           dribbling  passing  shooting
# name                                           
# Cristiano Ronaldo         84       83        89
# L. Messi                  88       92        70

# Flip perspective: rows=movement, cols=name
fifa_names = fifa_players.pivot(index="movement", columns="name", values="overall")
print(fifa_names)
# name       Cristiano Ronaldo  L. Messi
# movement                              
# dribbling                 89        96
# passing                   82        92
# shooting                  93        92

# Pivot multiple value columns at once → MultiIndex columns (metric, movement)
fifa_over_attack = fifa_players.pivot(
    index="name", columns="movement", values=["overall", "attacking"]
)
print(fifa_over_attack)
#                     overall                  attacking                 
# movement          dribbling passing shooting dribbling passing shooting
# name                                                                   
# Cristiano Ronaldo        89      82       93        84      83       89
# L. Messi                 96      92       92        88      92       70


# Omitting values pivots all remaining columns, also yielding MultiIndex columns
fifa_all = fifa_players.pivot(index="name", columns="movement")
print(fifa_all)
#                    overall                  attacking                 
# movement          dribbling passing shooting dribbling passing shooting
# name                                                                   
# Cristiano Ronaldo        89      82       93        84      83       89
# L. Messi                 96      92       92        88      92       70


# Example of handling duplicates: dropping a row to avoid duplicate (name, movement) pairs
fifa_no_rep = fifa_players.drop(4, axis=0)
print(fifa_no_rep)
#                 name   movement  overall  attacking
# 0           L. Messi   shooting       92         70
# 1  Cristiano Ronaldo   shooting       93         89
# 2           L. Messi    passing       92         92
# 3  Cristiano Ronaldo    passing       82         83
# 5  Cristiano Ronaldo  dribbling       89         84
# 6           L. Messi  dribbling       88         97

# Pivot fifa players to get all scores by name and movement
fifa_pivot = fifa_no_rep.pivot(index="name", columns="movement")
#                     overall                  attacking                 
# movement          dribbling passing shooting dribbling passing shooting
# name                                                                   
# Cristiano Ronaldo        89      82       93        84      83       89
# L. Messi                 88      92       92        97      92       70
