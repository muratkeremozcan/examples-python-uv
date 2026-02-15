# Key takeaways (wide/long + indexing):
# - Wide format keeps variables in separate columns.
# - Long format keeps one value per row with identifier columns.
# - Convert wide to long with `melt` or `wide_to_long`.
# - Convert long to wide with `pivot` or `pivot_table`.
# - `set_index` makes a column the row label for easier lookup/slicing.


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
fifa_transpose = fifa_players.set_index("name")
#                    age  height  weight nationality                 club
# name
# Lionel Messi        32     170      72   Argentina         FC Barcelona
# Cristiano Ronaldo   34     187      83    Portugal             Juventus
# Neymar da Silva     27     175      68      Brazil  Paris Saint-Germain
# Jan Oblak           26     188      87    Slovenia      Atlético Madrid
# Eden Hazard         28     175      74     Belgium          Real Madrid

# set index & filter columns: df.set_index('column_name')[['column1', 'column2']]
fifa_transpose = fifa_players.set_index("name")[["height", "weight"]]
#                    height  weight
# name
# Lionel Messi          170      72
# Cristiano Ronaldo     187      83
# Neymar da Silva       175      68
# Jan Oblak             188      87
# Eden Hazard           175      74

# Flip rows and columns: df.set_index('column_name')[['column1', 'column2']].transpose()
fifa_transpose = fifa_players.set_index("name")[["height", "weight"]].transpose()
# name    Lionel Messi  Cristiano Ronaldo  Neymar da Silva  Jan Oblak  Eden Hazard
# height           170                187              175        188          175
# weight            72                 83               68         87           74
