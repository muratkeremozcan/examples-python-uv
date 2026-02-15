import pandas as pd

# Key takeaways (MultiIndex + stack):
# - MultiIndex lets one table carry multiple label levels on rows/columns.
# - `stack()` moves one column level into the row index.
# - `stack(level=...)` lets you choose which column level to move.
# - This is useful when moving between wide and long layouts.


churn = pd.DataFrame(
    {
        "Area code": [408, 408, 415, 510],
        "total_day_calls": [116, 109, 84, 67],
        "total_day_minutes": [204, 287, 84, 50],
    }
)
#    Area code  total_day_calls  total_day_minutes
# 0        408              116                204
# 1        408              109                287
# 2        415               84                 84
# 3        510               67                 50

# Predefined list to use as index
new_index = [
    ["California", "California", "New York", "Ohio"],
    ["Los Angeles", "San Francisco", "New York", "Cleveland"],
]

# 1) Build a row MultiIndex from two arrays (state/city)
# so that each row has a two-part key instead of a flat integer index.
churn_new = pd.MultiIndex.from_arrays(new_index, names=["state", "city"])
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
# Stacking turns column labels into another row index level.
# That gives one key per state/city/metric for long-form analysis.

#########################

# Build multi-level columns so we can stack a specific column level.
# Columns now have levels: time then feature.
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

# 4) stack the level 1 column ('feature') into the rows: rows become (state, city, feature); columns = time
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

# stack the 'feature' column level into the rows: rows become (state, city, feature); columns = time
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
