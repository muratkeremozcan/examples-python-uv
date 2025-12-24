import pandas as pd
from pandas import json_normalize

# Key takeaways (JSON + json_normalize):
# - JSON is a common interchange format; nested dicts/lists are common in APIs and metadata.
# - pd.json_normalize flattens nested dicts into columns (dot separator by default) -> creates a dataframe
# - sep lets you change the nesting separator (useful for reshaping later).
# - wide_to_long can reshape normalized columns using stubnames/sep/suffix.
# - For list-of-dict fields, record_path points to the list to explode into rows.
# - meta pulls non-record fields into the normalized result.


# JSON example from the lesson: nested "features" dict.
movies = [
    {
        "director": "Woody Allen",
        "producer": "Letty Aronson",
        "features": {"title": "Magic in the Moonlight", "year": 2014},
    },
    {
        "director": "Niki Caro",
        "producer": "Jason Reed",
        "features": {"title": "Mulan", "year": 2020},
    },
]

# Normalize movies and separate the new columns with an underscore.
# Why: we want "features_title" and "features_year" so we can reshape by stubname.
movies_norm = json_normalize(movies, sep="_")
# print(movies_norm)
#       director       producer          features_title  features_year
# 0  Woody Allen  Letty Aronson  Magic in the Moonlight           2014
# 1    Niki Caro     Jason Reed                   Mulan           2020

# Reshape using director and producer as index, create movies from columns starting with "features". 
# This converts feature columns (title/year) into rows.
# pd.wide_to_long(df, stubnames=<prefix>, i=<new index>, j=<new name of the stub>)
movies_long = pd.wide_to_long(
    movies_norm,
    stubnames="features",
    i=["director", "producer"],
    j="movies",
    sep="_",
    suffix="\\w+",
)
# print(movies_long)
#                                                 features
# director    producer      movies                        
# Woody Allen Letty Aronson title   Magic in the Moonlight
#                           year                      2014
# Niki Caro   Jason Reed    title                    Mulan
#                           year                      2020

print(movies_long.reset_index())
#       director       producer movies                features
# 0  Woody Allen  Letty Aronson  title  Magic in the Moonlight
# 1  Woody Allen  Letty Aronson   year                    2014
# 2    Niki Caro     Jason Reed  title                   Mulan
# 3    Niki Caro     Jason Reed   year                    2020

############
# Narrative checkpoint:
# - The default json_normalize() separator is a dot, which is fine for display but
#   less convenient for wide_to_long (it expects a simple prefix + separator pattern).
# - record_path is only for list-of-dict fields; "features" is a dict here, so we
#   flatten it directly and reshape afterward.

# Default output (dot separator) for comparison:
# print(json_normalize(movies))
#       director       producer          features.title  features.year
# 0  Woody Allen  Letty Aronson  Magic in the Moonlight           2014
# 1    Niki Caro     Jason Reed                   Mulan           2020
