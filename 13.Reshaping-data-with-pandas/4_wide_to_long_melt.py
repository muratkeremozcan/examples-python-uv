import pandas as pd

books_gothic = pd.DataFrame({
    'title': ['Wuthering Heights', 'Frankenstein', 'The Picture of Dorian Gray'],
    'authors': ['Emily Bronte', 'Mary Shelley', 'Oscar Wilde'],
    'num_pages': [322, 189, 187],
    'rating_count': [2155, 2452, 3342],
    'rating': [3.85, 4.31, 4.15],
    'publisher': ['Penguin Books', 'Kaplan Publishing', 'Pearson']
})
# wide format: each variable is a separate column with one row per item (book item vs authors, num_pages, rating_count, rating, publisher)
#                         title       authors  num_pages  rating_count  rating          publisher
# 0           Wuthering Heights  Emily Bronte        322          2155    3.85      Penguin Books
# 1                Frankenstein  Mary Shelley        189          2452    4.31  Kaplan Publishing
# 2  The Picture of Dorian Gray   Oscar Wilde        187          3342    4.15            Pearson
# long/tidy version would stack those measurements into two columns like variable and value (one row per title-variable pair).


# .melt() is the opposite of .pivot()
# .melt(id_vars=<row vars>, value_vars=<col vars>)
gothic_melted = books_gothic.melt(id_vars='title')
#                          title      variable              value
# 0            Wuthering Heights       authors       Emily Bronte
# 1                 Frankenstein       authors       Mary Shelley
# 2   The Picture of Dorian Gray       authors        Oscar Wilde
# 3            Wuthering Heights     num_pages                322
# 4                 Frankenstein     num_pages                189
# 5   The Picture of Dorian Gray     num_pages                187
# 6            Wuthering Heights  rating_count               2155
# 7                 Frankenstein  rating_count               2452
# 8   The Picture of Dorian Gray  rating_count               3342
# 9            Wuthering Heights        rating               3.85
# 10                Frankenstein        rating               4.31
# 11  The Picture of Dorian Gray        rating               4.15
# 12           Wuthering Heights     publisher      Penguin Books
# 13                Frankenstein     publisher  Kaplan Publishing
# 14  The Picture of Dorian Gray     publisher            Pearson

# can use multiple id_vars
gothic_melted_new = books_gothic.melt(id_vars=['title', 'authors', 'publisher'])
#                         title       authors          publisher      variable    value
# 0           Wuthering Heights  Emily Bronte      Penguin Books     num_pages   322.00
# 1                Frankenstein  Mary Shelley  Kaplan Publishing     num_pages   189.00
# 2  The Picture of Dorian Gray   Oscar Wilde            Pearson     num_pages   187.00
# 3           Wuthering Heights  Emily Bronte      Penguin Books  rating_count  2155.00
# 4                Frankenstein  Mary Shelley  Kaplan Publishing  rating_count  2452.00
# 5  The Picture of Dorian Gray   Oscar Wilde            Pearson  rating_count  3342.00
# 6           Wuthering Heights  Emily Bronte      Penguin Books        rating     3.85
# 7                Frankenstein  Mary Shelley  Kaplan Publishing        rating     4.31

# .melt(id_vars=<row vars>, value_vars=<col vars>)
publisher_melted = books_gothic.melt(id_vars=['title', 'authors'], value_vars=['publisher'])
#                         title       authors   variable              value
# 0           Wuthering Heights  Emily Bronte  publisher      Penguin Books
# 1                Frankenstein  Mary Shelley  publisher  Kaplan Publishing
# 2  The Picture of Dorian Gray   Oscar Wilde  publisher            Pearson

rating_melted = books_gothic.melt(id_vars='title', value_vars=['rating', 'rating_count'])
#                         title      variable    value
# 0           Wuthering Heights        rating     3.85
# 1                Frankenstein        rating     4.31
# 2  The Picture of Dorian Gray        rating     4.15
# 3           Wuthering Heights  rating_count  2155.00
# 4                Frankenstein  rating_count  2452.00
# 5  The Picture of Dorian Gray  rating_count  3342.00

books_melted = books_gothic.melt(id_vars=['title', 'authors'], value_vars=['rating', 'rating_count'])
#                         title       authors      variable    value
# 0           Wuthering Heights  Emily Bronte        rating     3.85
# 1                Frankenstein  Mary Shelley        rating     4.31
# 2  The Picture of Dorian Gray   Oscar Wilde        rating     4.15
# 3           Wuthering Heights  Emily Bronte  rating_count  2155.00
# 4                Frankenstein  Mary Shelley  rating_count  2452.00
# 5  The Picture of Dorian Gray   Oscar Wilde  rating_count  3342.00

books_ratings = books_gothic.melt(id_vars=['title', 'authors', 'publisher'], value_vars=['rating', 'rating_count'])
#                         title       authors          publisher      variable    value
# 0           Wuthering Heights  Emily Bronte      Penguin Books        rating     3.85
# 1                Frankenstein  Mary Shelley  Kaplan Publishing        rating     4.31
# 2  The Picture of Dorian Gray   Oscar Wilde            Pearson        rating     4.15
# 3           Wuthering Heights  Emily Bronte      Penguin Books  rating_count  2155.00
# 4                Frankenstein  Mary Shelley  Kaplan Publishing  rating_count  2452.00
# 5  The Picture of Dorian Gray   Oscar Wilde            Pearson  rating_count  3342.00

# .melt(id_vars=<row vars>, value_vars=<col vars>, var_name=<new var name>)
books_ratings = books_gothic.melt(id_vars=['title', 'authors', 'publisher'], value_vars=['rating', 'rating_count'], var_name='feature')
#                         title       authors          publisher        feature    value
# 0           Wuthering Heights  Emily Bronte      Penguin Books        rating     3.85
# 1                Frankenstein  Mary Shelley  Kaplan Publishing        rating     4.31
# 2  The Picture of Dorian Gray   Oscar Wilde            Pearson        rating     4.15
# 3           Wuthering Heights  Emily Bronte      Penguin Books  rating_count  2155.00
# 4                Frankenstein  Mary Shelley  Kaplan Publishing  rating_count  2452.00
# 5  The Picture of Dorian Gray   Oscar Wilde            Pearson  rating_count  3342.00

# .melt(id_vars=<row vars>, value_vars=<col vars>, var_name=<new var name>, value_name=<new value name>)
books_ratings = books_gothic.melt(id_vars=['title', 'authors', 'publisher'], 
                                  value_vars=['rating', 'rating_count'], 
                                  var_name='feature', 
                                  value_name='number')
#                         title       authors          publisher       feature   number
# 0           Wuthering Heights  Emily Bronte      Penguin Books        rating     3.85
# 1                Frankenstein  Mary Shelley  Kaplan Publishing        rating     4.31
# 2  The Picture of Dorian Gray   Oscar Wilde            Pearson        rating     4.15
# 3           Wuthering Heights  Emily Bronte      Penguin Books  rating_count  2155.00
# 4                Frankenstein  Mary Shelley  Kaplan Publishing  rating_count  2452.00
# 5  The Picture of Dorian Gray   Oscar Wilde            Pearson  rating_count  3342.00``