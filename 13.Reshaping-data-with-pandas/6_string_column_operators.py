import pandas as pd

# String tools cheat sheet and where each is used below:
# - str.split(delim, expand=True): break text into pieces
# - str.get(i): grab one piece from a split
# - str.cat(other, sep): join strings/columns/lists
# - expand=True: makes split return separate columns



books_dys = pd.DataFrame({
	'title': ['Fahrenheit 451-1953', '1984-1949', 'Brave New World-1932'],
	'year': [1953, 1949, 1932],
	'num_pages': [186, 268, 123],
	'average_rating': [4.10, 4.31, 4.30],
	'ratings_count': [23244, 14353, 23535]
})
#                       year  num_pages  average_rating  ratings_count
# title                                                               
# Fahrenheit 451-1953   1953        186            4.10          23244
# 1984-1949             1949        268            4.31          14353
# Brave New World-1932  1932        123            4.30          23535


# - str.split(delim, expand=True): break text into pieces
# 1) Split the title on the hyphen so we can drop the year part.
books_dys.index = books_dys.index.str.split('-')
#                          year  num_pages  average_rating  ratings_count
# title                                                                  
# [Fahrenheit 451, 1953]   1953        186            4.10          23244
# [1984, 1949]             1949        268            4.31          14353
# [Brave New World, 1932]  1932        123            4.30          23535

# books_dys.index = books_dys.index.str.split('-', expand=True)
#                  0                1    year  num_pages  average_rating  ratings_count
# title                                                                                
# Fahrenheit 451   1953             1953     186            4.10          23244
# 1984             1949             1949     268            4.31          14353
# Brave New World  1932             1932     123            4.30          23535


# - str.get(i): grab one piece from a split
# 2) Keep only the title part (first element of the split).
books_dys.index = books_dys.index.str.get(0)
#                     year  num_pages  average_rating  ratings_count
# title                                                              
# Fahrenheit 451       1953        186            4.10          23244
# 1984                 1949        268            4.31          14353
# Brave New World      1932        123            4.30          23535

# - str.cat(other, sep): join strings/columns/lists
# 3) Append author names from a list to make the index more informative.
author_list = ['Ray Bradbury', 'George Orwell', 'Aldous Huxley']
books_dys.index = books_dys.index.str.cat(author_list, sep='-')
#                                  year  num_pages  average_rating  ratings_count
# title                                                                          
# Fahrenheit 451 - Ray Bradbury    1953        186            4.10          23244
# 1984 - George Orwell             1949        268            4.31          14353
# Brave New World - Aldous Huxley  1932        123            4.30          23535
print(books_dys)


######################


books_dys_cols = pd.DataFrame(
    {
        "title": ["Fahrenheit 451", "1984", "Brave New World"],
        "subtitle": [
            "Firemen and censorship",
            "Big Brother watches",
            "Soma and control",
        ],
        "authors": [
            "Ray Bradbury/Joseph Mugnaini",
            "George Orwell/None",
            "Aldous Huxley/None",
        ],
        "goodreads": [4.1, 4.3, 4.2],
        "amazon": [4.0, 4.2, 4.1],
    }
)
#              title                subtitle                     authors             goodreads  amazon
# 0   Fahrenheit 451  Firemen and censorship      Ray Bradbury/Joseph Mugnaini       4.1        4.0
# 1            1984     Big Brother watches                 George Orwell/None       4.3        4.2
# 2  Brave New World         Soma and control               Aldous Huxley/None       4.2        4.1

# Concatenate title + subtitle to make a fuller label (same str.cat idea).
books_dys_cols["full_title"] = books_dys_cols["title"].str.cat(
    books_dys_cols["subtitle"], sep=" – "
)
print(books_dys_cols)
#              title                subtitle                     authors             goodreads  amazon                             full_title
# 0   Fahrenheit 451  Firemen and censorship      Ray Bradbury/Joseph Mugnaini       4.1        4.0   Fahrenheit 451 – Firemen and censorship
# 1            1984     Big Brother watches                 George Orwell/None       4.3        4.2            1984 – Big Brother watches
# 2  Brave New World         Soma and control               Aldous Huxley/None       4.2        4.1         Brave New World – Soma and control

# Split authors into writer and collaborator (expand=True makes two columns).
books_dys_cols[["writer", "collaborator"]] = books_dys_cols["authors"].str.split(
    "/", expand=True
)
print(books_dys_cols)
#              title                subtitle                     authors             goodreads  amazon                             full_title       writer         collaborator
# 0   Fahrenheit 451  Firemen and censorship      Ray Bradbury/Joseph Mugnaini       4.1        4.0   Fahrenheit 451 – Firemen and censorship      Ray Bradbury    Joseph Mugnaini
# 1            1984     Big Brother watches                 George Orwell/None       4.3        4.2            1984 – Big Brother watches          George Orwell               None
# 2  Brave New World         Soma and control               Aldous Huxley/None       4.2        4.1         Brave New World – Soma and control     Aldous Huxley               None

# Melt ratings into a long format: source column + rating column.
# .melt(id_vars=<row vars>, value_vars=<col vars>, var_name=<new var name>, value_name=<new value name>)
books_dys_long = books_dys_cols.melt(
    id_vars=["full_title", "writer"],
    value_vars=["goodreads", "amazon"],
    var_name="source",
    value_name="rating",
)
print(books_dys_long)
#                              full_title          writer          source        rating
# 0   Fahrenheit 451 – Firemen and censorship      Ray Bradbury    goodreads     4.1
# 1             1984 – Big Brother watches         George Orwell   goodreads     4.3
# 2          Brave New World – Soma and control    Aldous Huxley   goodreads     4.2
# 3   Fahrenheit 451 – Firemen and censorship      Ray Bradbury    amazon        4.0
# 4             1984 – Big Brother watches         George Orwell   amazon        4.2
# 5          Brave New World – Soma and control    Aldous Huxley   amazon        4.1
