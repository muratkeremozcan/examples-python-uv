import pandas as pd

# - Why MultiIndex: store multidimensional data (e.g., country/age or member/card) in one DataFrame, enabling hierarchical grouping and reshaping.

# MultiIndex mental model: still a 2D table, but row/column labels are hierarchical,
# letting you represent higher dimensions on 2 axes. 
# Stack/unstack just moves one level between rows and columns; each cell is still a single value.

# it's like doing a table within a table (almost like 3D in a 2D)
# because you have index level /rows which is like a meta row
# then you have columns
# then you have specific values called cells


# - MultiIndex basics: create multi-level row/column indexes via 
#   set_index([...]) 
#   pd.MultiIndex.from_arrays(...) 
#   (assign to df.index/df.columns). Works for rows and columns.

# - df.stack() moves the innermost column level to become the innermost row level. 
#   If columns are single-level, stacking collapses them into a Series; if columns are MultiIndex, it returns a DataFrame.

# - df.stack(level=<level_number_or_name>) stacks a specific column level (defaults to last). 
#   Stacked level becomes the lowest row level.

# - MultiIndex DataFrames: can have multi-level rows and columns; 
#   stack operates on the column levels, reshaping between wide/hierarchical layouts and longer forms for analysis.


churn = pd.DataFrame({
	"Area code": [408, 408, 415, 510],
	"total_day_calls": [116, 109, 84, 67],
	"total_day_minutes": [204, 287, 84, 50]
})
#    Area code  total_day_calls  total_day_minutes
# 0        408              116                204
# 1        408              109                287
# 2        415               84                 84
# 3        510               67                 50

# Predefined list to use as index
new_index = [['California', 'California', 'New York', 'Ohio'], 
             ['Los Angeles', 'San Francisco', 'New York', 'Cleveland']]

# 1) Build a row MultiIndex from two arrays (state/city) 
# so that each row has a two-part key instead of a flat integer index.
churn_new = pd.MultiIndex.from_arrays(new_index, names=['state', 'city'])
# MultiIndex([('California',   'Los Angeles'),
#             ('California', 'San Francisco'),
#             (  'New York',      'New York'),
#             (      'Ohio',     'Cleveland')],
#            names=['state', 'city'])

# 2) Attach that MultiIndex to the DataFrame to make row labels meaningful for later reshaping and grouping.
churn.index = churn_new
# here the index-levels/rows are state and city
# the columns are Area code, total_day_calls, total_day_minutes
#                           Area code  total_day_calls  total_day_minutes
# state      city                                                        
# California Los Angeles          408              116                204
#            San Francisco        408              109                287
# New York   New York             415               84                 84
# Ohio       Cleveland            510               67                 50

# 3) stack() moves all column labels into the row index (one level deeper).
churn_stack = churn.stack()
# state       city                            
# California  Los Angeles    Area code            408
#                            total_day_calls      116
#                            total_day_minutes    204
#             San Francisco  Area code            408
#                            total_day_calls      109
#                            total_day_minutes    287
# New York    New York       Area code            415
#                            total_day_calls       84
#                            total_day_minutes     84
# Ohio        Cleveland      Area code            510
#                            total_day_calls       67
#                            total_day_minutes     50
# dtype: int64
# Why: stacking here turns the column labels into another index level 
# so that each state/city/metric is a single key—useful for long-form analyses.

#########################

# Build multi-level columns so we can demonstrate stacking a chosen column level
# instead of the implicit last one. Columns now have levels: time -> feature.
time = ["night", "night", "day", "day"]
feature = ["total calls", "total minutes", "total calls", "total minutes"]
cols = pd.MultiIndex.from_arrays([time, feature], names=["time", "feature"])
churn_multi = pd.DataFrame(
    [
        [116, 204, 85, 107],
        [109, 287, 90, 167],
        [84, 84, 75, 90],
        [67, 50, 67, 110],
    ],
    index=churn_new,
    columns=cols,
)
# time                            night                           day              
# feature                         total calls    total minutes    total calls    total minutes
# state        city                                                     
# California   Los Angeles         116           204              85             107
#              San Francisco       109           287              90             167
# New York     New York             84            84              75             90
# Ohio         Cleveland            67            50              67             110

# 4) Stack a chosen column level: here level=1 (feature) drops into the row index, 
# leaving the remaining column level (time) on top.
churn_stack = churn_multi.stack(level=1)
#                                         day  night
# state      city                                   
# California Los Angeles   total calls     85    116
#                          total minutes  107    204
#            San Francisco total calls     90    109
#                          total minutes  167    287
# New York   New York      total calls     75     84
#                          total minutes   90     84
# Ohio       Cleveland     total calls     67     67
#                          total minutes  110     50

# Stack by the named column level "feature" (same as level=1).
churn_feature = churn_multi.stack(level="feature")
# time                day  night
# state      city                    
# California Los Angeles   total calls     85    116
#                          total minutes  107    204
#            San Francisco total calls     90    109
#                          total minutes  167    287
# New York   New York      total calls     75     84
#                          total minutes   90     84
# Ohio       Cleveland     total calls     67     67
#                          total minutes  110     50

# Stack by the named column level "time" (same as level=0 here).
churn_time = churn_multi.stack(level="time")
# feature                         total calls  total minutes
# state      city          time                                    
# California Los Angeles   night          116            204
#                          day             85            107
#            San Francisco night          109            287
#                          day             90            167
# New York   New York      night           84             84
#                          day             75             90
# Ohio       Cleveland     night           67             50
#                          day             67            110

