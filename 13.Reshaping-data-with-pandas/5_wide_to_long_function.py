import pandas as pd

# Wide-to-long takeaways:
# - Use pandas.wide_to_long when columns share prefixes + suffixes that encode a variable (e.g., age1990, age2000, weight1990, weight2000).

# - stubnames: list of prefixes to gather; i: new index column(s), j: new name of the stub column;
# - sep: if prefixes and suffixes are split by a character (ratings_2010) declare a separator sep="_"
# - suffix: regex for non-numeric suffixes, like empty space (publication date) suffix=r"\w+"
# - reset_index() takes whatever’s in the index and turns it into a normal column (and gives you a fresh 0,1,2 RangeIndex

golden_age = pd.DataFrame(
    {
        "title": ["The Great Gatsby", "The Short Stories", "To the Lighthouse"],
        "authors": [
            "F. Scott Fitzgerald",
            "Ernest Hemingway",
            "Virginia Woolf",
        ],
        "isbn13": ["9780060098919", "9780684837864", "9780156030472"],
        "isbn10": ["1572702567", "684837862", "156030470"],
        "prefix13": [978, 978, 978],
        "prefix10": [1, 0, 0],
    }
)
#              title              authors         isbn13      isbn10  prefix13  prefix10
# 0   The Great Gatsby  F. Scott Fitzgerald  9780060098919  1572702567       978         1
# 1  The Short Stories     Ernest Hemingway  9780684837864   684837862       978         0
# 2  To the Lighthouse       Virginia Woolf  9780156030472   156030470       978         0

# Reshape wide to long using title as index and version as new name, and extracting isbn prefix
# pd.wide_to_long(df, stubnames=<prefix>, i=<new index>, j=<new name of the stub>)
isbn_long = pd.wide_to_long(golden_age, stubnames="isbn", i="title", j="version")
#                            prefix10              authors  prefix13           isbn
# title             version
# The Great Gatsby  13              1  F. Scott Fitzgerald       978  9780060098919
# The Short Stories 13              0     Ernest Hemingway       978  9780684837864
# To the Lighthouse 13              0       Virginia Woolf       978  9780156030472
# The Great Gatsby  10              1  F. Scott Fitzgerald       978     1572702567
# The Short Stories 10              0     Ernest Hemingway       978      684837862
# To the Lighthouse 10              0       Virginia Woolf       978      156030470

# Reshape wide to long using title and authors as index and version as new name, and prefix as wide column prefix
# pd.wide_to_long(df, stubnames=<prefix>, i=<new index>, j=<new name of the stub>)
prefix_long = pd.wide_to_long(
    golden_age, stubnames="prefix", i=["title", "authors"], j="version"
)
#                                                    isbn10         isbn13  prefix
# title             authors             version
# The Great Gatsby  F. Scott Fitzgerald 13       1572702567  9780060098919     978
#                                       10       1572702567  9780060098919       1
# The Short Stories Ernest Hemingway    13        684837862  9780684837864     978
#                                       10        684837862  9780684837864       0
# To the Lighthouse Virginia Woolf      13        156030470  9780156030472     978
#                                       10        156030470  9780156030472       0

# Reshape wide to long using title and authors as index and version as new name, and prefix and isbn as wide column prefixes
# pd.wide_to_long(df, stubnames=<prefix>, i=<new index>, j=<new name of the stub>)
all_long = pd.wide_to_long(
    golden_age, stubnames=["prefix", "isbn"], i=["title", "authors"], j="version"
)
#                                                prefix           isbn
#                                                        isbn  prefix
# title             authors             version
# The Great Gatsby  F. Scott Fitzgerald 13       9780060098919     978
#                                       10          1572702567       1
# The Short Stories Ernest Hemingway    13       9780684837864     978
#                                       10           684837862       0
# To the Lighthouse Virginia Woolf      13       9780156030472     978
#                                       10           156030470       0

#####################

books_brown = pd.DataFrame(
    {
        "title": ["The Da Vinci Code", "Angels & Demons", "La fortaleza digital"],
        "author": ["Dan Brown", "Dan Brown", "Dan Brown"],
        "language_code": [0, 0, 84],
        "language_name": ["english", "english", "spanish"],
        "publisher_code": [12, 34, 43],
        "publisher_name": ["Random House", "Pocket Books", "Umbriel"],
    }
)

#                   title     author  language_code language_name  publisher_code publisher_name
# 0     The Da Vinci Code  Dan Brown              0       english              12   Random House
# 1       Angels & Demons  Dan Brown              0       english              34   Pocket Books
# 2  La fortaleza digital  Dan Brown             84       spanish              43        Umbriel


# Reshape using author and title as index, code as new name and getting the prefix language and publisher
# Specify underscore as the character that separates the variable names
# Specify that wide columns have a suffix containing words
# pd.wide_to_long(df, stubnames=<prefix>, i=<new index>, j=<new name of the stub>)
the_code_long = pd.wide_to_long(
    books_brown,
    stubnames=["language", "publisher"],
    i=["author", "title"],
    j="code",
    sep="_",
    suffix=r"\w+",
)
#                                     language     publisher
# author    title                code
# Dan Brown The Da Vinci Code    code        0            12
#                                name  english  Random House
#           Angels & Demons      code        0            34
#                                name  english  Pocket Books
#           La fortaleza digital code       84            43
#                                name  spanish       Umbriel


######################

books_hunger = pd.DataFrame(
    {
        "title": ["Los Juegos del Hambre", "Catching Fire", "Il canto della rivolta"],
        "language": ["Spanish", "English", "Italian"],
        "publication date": ["5/25/2010", "5/25/2012", "6/8/2015"],
        "publication number": [2, 6, 4],
        "page number": [374, 391, 390],
    }
).set_index("title")

#                        language publication date  publication number  page number
# title
# Los Juegos del Hambre   Spanish        5/25/2010                   2          374
# Catching Fire           English        5/25/2012                   6          391
# Il canto della rivolta  Italian         6/8/2015                   4          390

# title lives in the index, so wide_to_long can't find it -> KeyError
try:
    pd.wide_to_long(
        books_hunger,
        stubnames=["publication", "page"],
        i=["title", "language"],
        j="feature",
        sep=" ",
        suffix=r"\w+",
    )
except KeyError as exc:
    print(f"KeyError: {exc}")


# reset_index() takes whatever’s in the index and turns it into a normal column (and gives you a fresh 0,1,2 RangeIndex
books_hunger_reset = (
    books_hunger.reset_index()
)  # books_hunger.reset_index(drop=False, inplace=True) if you wanted to mutate books_hunger in place
print("\nAfter reset_index:")
print(books_hunger_reset)
#                     title language publication date  publication number  page number
# 0   Los Juegos del Hambre  Spanish        5/25/2010                   2          374
# 1           Catching Fire  English        5/25/2012                   6          391
# 2  Il canto della rivolta  Italian         6/8/2015                   4          390

publication_features = pd.wide_to_long(
    books_hunger_reset,
    stubnames=["publication", "page"],
    i=["title", "language"],
    j="feature",
    sep=" ",
    suffix=r"\w+",
)
print("\nwide_to_long works once title is a column:")
print(publication_features)
