import pandas as pd

# MultiIndex mental model: still a 2D table, but row/column labels are hierarchical,
# letting you represent higher dimensions (country/sex/year) on 2 axes. 
# Stack/unstack just moves one level between rows and columns; each cell is still a single value.

# it's like doing a table within a table (almost like 3D in a 2D)
# because you have index level /rows which is like a meta row
# then hou have columns
# then you have specific values called cells


# Reshaping + stats/grouping cheat sheet:
# - You can chain stack/unstack with aggregations (sum/mean/median/diff) to pivot between tall/wide views before/after computing stats.

# - stack + agg moves a column level into the rows, then aggregates across columns (axis=1) to total by the new row level.

# - unstack + agg moves a row level into columns, then aggregates across columns (axis=1) for per-row-level stats.

# - diff(axis=1, periods=n) compares columns across time/levels after unstacking.

# - Combine with groupby(level=...) to aggregate after reshaping (e.g., stack shop, then groupby shop and sum; groupby year then median).


df = pd.DataFrame({
	"country": ["Argentina", "Argentina", "Argentina", "Argentina", "Japan", "Japan", "Japan", "Japan", "Norway", "Norway", "Norway", "Norway"],
	"biological_sex": ["Male", "Female", "Male", "Female", "Male", "Female", "Male", "Female", "Male", "Female", "Male", "Female"],
	"year": [2005, 2005, 2015, 2015, 2005, 2005, 2015, 2015, 2005, 2005, 2015, 2015],
	"perc_obesity": [21.5, 24.2, 26.8, 28.5, 2.5, 2.6, 4.6, 3.6, 17.6, 18.6, 23.0, 22.2]
})
obesity = df.set_index(["country", "biological_sex", "year"])
# 1) index levels (rows): country, biological_sex, year .
# columns: perc_obesity

#                                perc_obesity
# country   biological_sex year              
# Argentina Male           2005          21.5
#           Female         2005          24.2
#           Male           2015          26.8
#           Female         2015          28.5
# Japan     Male           2005           2.5
#           Female         2005           2.6
#           Male           2015           4.6
#           Female         2015           3.6
# Norway    Male           2005          17.6
#           Female         2005          18.6
#           Male           2015          23.0
#           Female         2015          22.2

# 2. unstack(level=0) moves country from the row index to the columns.
# - New index levels (rows): biological_sex, year
# - New columns: one per country
# - Cells: perc_obesity for that sex/year/country
obesity_unstack_0 = obesity.unstack(level=0)
#                     perc_obesity             
# country                Argentina Japan Norway
# biological_sex year                          
# Female         2005         24.2   2.6   18.6
#                2015         28.5   3.6   22.2
# Male           2005         21.5   2.5   17.6
#                2015         26.8   4.6   23.0

obesity_general = obesity.unstack(level=0).mean(axis=1) # axis=1 means columns (get mean ACROSS)
# biological_sex  year
# Female          2005    15.133
#                 2015    18.100
# Male            2005    13.867
#                 2015    18.133

#  3. unstack(level=1) moves biological_sex to the columns.
#   - New index levels (rows): (country, year)
#   - New columns: Male, Female
#   - Cells: perc_obesity for that country/year/sex
obesity_unstack_1 = obesity.unstack(level=1)
#                perc_obesity      
# biological_sex       Female  Male
# country   year                   
# Argentina 2005         24.2  21.5
#           2015         28.5  26.8
# Japan     2005          2.6   2.5
#           2015          3.6   4.6
# Norway    2005         18.6  17.6
#           2015         22.2  23.0

obesity_mean = obesity.unstack(level=1).mean(axis=1) 
obesity_general = obesity.unstack(level=0).mean(axis=1) # axis=1 means columns (get mean ACROSS)
# country    year
# Argentina  2005    22.85
#            2015    27.65
# Japan      2005     2.55
#            2015     4.10
# Norway     2005    18.10
#            2015    22.60

# 4. unstack(level=2) moves year to the columns.
# - New rows: (country, biological_sex)
# - New columns: 2005, 2015
# - Cells: perc_obesity for that country/sex/year
obesity_unstack_2 = obesity.unstack(level=2)
#                          perc_obesity      
# year                             2005  2015
# country   biological_sex                   
# Argentina Female                 24.2  28.5
#           Male                   21.5  26.8
# Japan     Female                  2.6   3.6
#           Male                    2.5   4.6
# Norway    Female                 18.6  22.2
#           Male                   17.6  23.0

obesity_variation = obesity.unstack(level=2).diff(axis=1)
#                          perc_obesity     
# year                             2005 2015
# country   biological_sex                  
# Argentina Female                  NaN  4.3
#           Male                    NaN  5.3
# Japan     Female                  NaN  1.0
#           Male                    NaN  2.1
# Norway    Female                  NaN  3.6
#           Male                    NaN  5.4

####################

# 1) Start: obesity has row index (country, biological_sex, year) and one column perc_obesity.
# obesity
#                                perc_obesity
# country   biological_sex year              
# Argentina Male           2005          21.5
#           Female         2005          24.2
#           Male           2015          26.8
#           Female         2015          28.5
# Japan     Male           2005           2.5
#           Female         2005           2.6
#           Male           2015           4.6
#           Female         2015           3.6
# Norway    Male           2005          17.6
#           Female         2005          18.6
#           Male           2015          23.0
#           Female         2015          22.2

# 2) obesity.stack(level=0): stacking column level 0 moves the column perc_obesity down into the row index. 
#   Result: a Series indexed by (country, biological_sex, year, 'perc_obesity').
#
# print(obesity.stack(level=0))
# country    biological_sex  year              
# Argentina  Male            2005  perc_obesity    21.5
#            Female          2005  perc_obesity    24.2
#            Male            2015  perc_obesity    26.8
#            Female          2015  perc_obesity    28.5
# Japan      Male            2005  perc_obesity     2.5
#            Female          2005  perc_obesity     2.6
#            Male            2015  perc_obesity     4.6
#            Female          2015  perc_obesity     3.6
# Norway     Male            2005  perc_obesity    17.6
#            Female          2005  perc_obesity    18.6
#            Male            2015  perc_obesity    23.0
#            Female          2015  perc_obesity    22.2

# BTW, stack() moves all columns into the row index. It doesn’t pick one column; it “rowifies” every column label,
# so each original column becomes part of the row index and you end up with a Series.
# so here since there is 1 column, its the same as stack(level=0)

# print(obesity.stack())
# country    biological_sex  year              
# Argentina  Male            2005  perc_obesity    21.5
#            Female          2005  perc_obesity    24.2
#            Male            2015  perc_obesity    26.8
#            Female          2015  perc_obesity    28.5
# Japan      Male            2005  perc_obesity     2.5
#            Female          2005  perc_obesity     2.6
#            Male            2015  perc_obesity     4.6
#            Female          2015  perc_obesity     3.6
# Norway     Male            2005  perc_obesity    17.6
#            Female          2005  perc_obesity    18.6
#            Male            2015  perc_obesity    23.0
#            Female          2015  perc_obesity    22.2


# 3) unstack(level=0) moves the left-most index-level/row (country) from the row index to the columns.
obesity_sum = obesity.stack(level=0).unstack(level=0)
# print(obesity_sum)
# country                           Argentina  Japan  Norway
# biological_sex year                                       
# Female         2005 perc_obesity       24.2    2.6    18.6
#                2015 perc_obesity       28.5    3.6    22.2
# Male           2005 perc_obesity       21.5    2.5    17.6
#                2015 perc_obesity       26.8    4.6    23.0


