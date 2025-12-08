
# - Wide format: 
#   one row per entity, with many feature columns;
#   handy for quick stats and imputation but may hide missing values.
#   if you care about the entity as a whole, go wide.
# - Long format:
#   one row per entity-feature pair (key-value style). 
#   works better for summaries, plotting, and modeling
#   if you care about each feature value separately, go long
  
# - Shape just means rows x columns; 
# - transposing flips axes but is rarely the goal by itself.

# - Core transforms: 
#   wide -> long with pd.melt or pd.wide_to_long; 
#   long -> wide with DataFrame.pivot or pivot_table. 

# set index:                  df.set_index('column_name')
# set index & filter columns: df.set_index('column_name')[['column1', 'column2']]
# Flip rows and columns:      df.set_index('column_name')[['column1', 'column2']].transpose()


import pandas as pd

# FIFA-like wide dataset used throughout the reshaping lessons
fifa_players = pd.DataFrame(
    {
        "name": [
            "Lionel Messi",
            "Cristiano Ronaldo",
            "Neymar da Silva",
            "Jan Oblak",
            "Eden Hazard",
        ],
        "age": [32, 34, 27, 26, 28],
        "height": [170, 187, 175, 188, 175],
        "weight": [72, 83, 68, 87, 74],
        "nationality": ["Argentina", "Portugal", "Brazil", "Slovenia", "Belgium"],
        "club": [
            "FC Barcelona",
            "Juventus",
            "Paris Saint-Germain",
            "Atlético Madrid",
            "Real Madrid",
        ],
    }
)
#                 name  age  height  weight nationality                 club
# 0       Lionel Messi   32     170      72   Argentina         FC Barcelona
# 1  Cristiano Ronaldo   34     187      83    Portugal             Juventus
# 2    Neymar da Silva   27     175      68      Brazil  Paris Saint-Germain
# 3          Jan Oblak   26     188      87    Slovenia      Atlético Madrid
# 4        Eden Hazard   28     175      74     Belgium          Real Madrid


# set index: df.set_index('column_name')
fifa_transpose = fifa_players.set_index('name')
#                    age  height  weight nationality                 club
# name                                                                   
# Lionel Messi        32     170      72   Argentina         FC Barcelona
# Cristiano Ronaldo   34     187      83    Portugal             Juventus
# Neymar da Silva     27     175      68      Brazil  Paris Saint-Germain
# Jan Oblak           26     188      87    Slovenia      Atlético Madrid
# Eden Hazard         28     175      74     Belgium          Real Madrid

# set index & filter columns: df.set_index('column_name')[['column1', 'column2']]
fifa_transpose = fifa_players.set_index('name')[['height', 'weight']]
#                    height  weight
# name                             
# Lionel Messi          170      72
# Cristiano Ronaldo     187      83
# Neymar da Silva       175      68
# Jan Oblak             188      87
# Eden Hazard           175      74

# Flip rows and columns: df.set_index('column_name')[['column1', 'column2']].transpose()
fifa_transpose = fifa_players.set_index('name')[['height', 'weight']].transpose()
# name    Lionel Messi  Cristiano Ronaldo  Neymar da Silva  Jan Oblak  Eden Hazard
# height           170                187              175        188          175
# weight            72                 83               68         87           74