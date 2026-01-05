import pandas as pd

# Key takeaways (merging on indexes):
# - merge() can join on index names.
# - MultiIndex uses a list of index level names.
# - Use left_index/right_index when merging on indexes.

# Reuse a familiar "movies" style table with id as the index.
movies = pd.DataFrame(
    {
        "id": [101, 102, 103],
        "title": ["Cafe A", "Shop B", "Diner C"],
        "popularity": [7.1, 6.4, 5.9],
    }
).set_index("id")
# print(movies)
#        title  popularity
# id
# 101   Cafe A         7.1
# 102   Shop B         6.4
# 103  Diner C         5.9

# Taglines table keyed by the same index name.
taglines = pd.DataFrame(
    {
        "id": [101, 103],
        "tagline": ["Fresh brews", "All-day bites"],
    }
).set_index("id")
# print(taglines)
#            tagline
# id
# 101    Fresh brews
# 103  All-day bites


# Merge on the index name "id" (left join keeps all movies).
# Takeaway: merge() can join on index names, not just columns.
movies_taglines = movies.merge(taglines, on="id", how="left")
# print(movies_taglines)
#        title  popularity        tagline
# id
# 101   Cafe A         7.1    Fresh brews
# 102   Shop B         6.4            NaN
# 103  Diner C         5.9  All-day bites

# ########################
# MultiIndex merge example.

samuel = pd.DataFrame(
    {
        "movie_id": [10, 10, 20],
        "cast_id": [1, 2, 1],
        "role": ["Lead", "Support", "Lead"],
    }
).set_index(["movie_id", "cast_id"])
# print(samuel)
#                      role
# movie_id cast_id
# 10       1           Lead
#          2        Support
# 20       1           Lead

cast = pd.DataFrame(
    {
        "movie_id": [10, 10, 20, 20],
        "cast_id": [1, 3, 1, 2],
        "character": ["Nick", "Dana", "Alex", "Rita"],
    }
).set_index(["movie_id", "cast_id"])
# print(cast)
#                  character
# movie_id cast_id
# 10       1            Nick
#          3            Dana
# 20       1            Alex
#          2            Rita


# Takeaway: MultiIndex merges work like multi-column merges (pass the index level names).
samuel_cast = samuel.merge(cast, on=["movie_id", "cast_id"])
# print(samuel_cast)
#                   role character
# movie_id cast_id
# 10       1        Lead      Nick
# 20       1        Lead      Alex

# ########################
# Index merge with different index names.

movies_to_genres = pd.DataFrame(
    {
        "movie_id": [101, 102, 104],
        "genre": ["Family", "Comedy", "Drama"],
    }
).set_index("movie_id")
# print(movies_to_genres)
#            genre
# movie_id
# 101       Family
# 102       Comedy
# 104        Drama

# Takeaway: When joining on indexes, use left_index/right_index (no left_on/right_on).
movies_genres = movies.merge(
    movies_to_genres,
    left_index=True,
    right_index=True,
    how="left",
)
# print(movies_genres)
#        title  popularity   genre
# id
# 101   Cafe A         7.1  Family
# 102   Shop B         6.4  Comedy
# 103  Diner C         5.9     NaN
