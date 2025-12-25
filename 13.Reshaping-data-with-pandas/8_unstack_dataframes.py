
import pandas as pd

# Unstack basics:
# - unstack() is the inverse of stack(): it moves a row level to the column side.
# - default: moves the innermost row level; pick a level via level=<num|name>.
# - works on Series or DataFrames; stack → unstack should round-trip if the index is unique.
# - stack/unstack sort levels; use sort_index if you need a different order.

# Start from a stacked Series (state, city, metric)
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

new_index = [
    ["California", "California", "New York", "Ohio"],
    ["Los Angeles", "San Francisco", "New York", "Cleveland"],
]
churn.index = pd.MultiIndex.from_arrays(new_index, names=["state", "city"])

# here the index-levels/rows are state and city
# the columns are Area code, total_day_calls, total_day_minutes

# print(churn)
#                           Area code  total_day_calls  total_day_minutes
# state      city                                                        
# California Los Angeles          408              116                204
#            San Francisco        408              109                287
# New York   New York             415               84                 84
# Ohio       Cleveland            510               67                 50

# stack() moves all column labels into the row index (one level deeper).
churn_stack = churn.stack() 
# print(churn_stack)
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

# unstack() looks at the row index levels in order: [state, city, <the stacked column labels>]. 
# With no level argument, unstack() moves the last row level (the unnamed one created by stack) back to columns.
churn_unstack = churn_stack.unstack()
# print(churn_unstack)
#                           Area code  total_day_calls  total_day_minutes
# state      city                                                        
# California Los Angeles          408              116                204
#            San Francisco        408              109                287
# New York   New York             415               84                 84
# Ohio       Cleveland            510               67                 50

##########################

# Build MultiIndex columns to demo unstack on DataFrames with column levels.
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
    index=churn.index,
    columns=cols,
)
# print(churn_multi)
# time                            night                           day              
# feature                         total calls    total minutes    total calls    total minutes
# state        city                                                     
# California   Los Angeles         116           204              85             107
#              San Francisco       109           287              90             167
# New York     New York             84            84              75             90
# Ohio         Cleveland            67            50              67             110

# stack the 'feature' column level into the rows: rows become (state, city, feature); columns = time
churn_feature = churn_multi.stack(level="feature")
# print(churn_feature)
# time                                    night  day
# state      city          feature                  
# California Los Angeles   total calls      116   85
#                          total minutes    204  107
#            San Francisco total calls      109   90
#                          total minutes    287  167
# New York   New York      total calls       84   75
#                          total minutes     84   90
# Ohio       Cleveland     total calls       67   67
#                          total minutes     50  110

# Unstack that same level back to columns (inverse of the previous stack).
churn_feature_unstack = churn_feature.unstack(level="feature")
# unstack the same level back to columns (inverse of previous stack)
# print(churn_feature_unstack)
# time                           night                       day              
# feature                  total calls total minutes total calls total minutes
# state      city                                                             
# California Los Angeles           116           204          85           107
#            San Francisco         109           287          90           167
# New York   New York               84            84          75            90
# Ohio       Cleveland              67            50          67           110

# Unstack a different row level: bring "state" (level=0) out to columns.
churn_state_unstack = churn_feature.unstack(level=0)
# unstack a different row level: move 'state' (level=0) to columns instead
# print(churn_state_unstack)
# time                             night                       day                
# state                       California New York  Ohio California New York   Ohio
# city          feature                                                           
# Cleveland     total calls          NaN      NaN  67.0        NaN      NaN   67.0
#               total minutes        NaN      NaN  50.0        NaN      NaN  110.0
# Los Angeles   total calls        116.0      NaN   NaN       85.0      NaN    NaN
#               total minutes      204.0      NaN   NaN      107.0      NaN    NaN
# New York      total calls          NaN     84.0   NaN        NaN     75.0    NaN
#               total minutes        NaN     84.0   NaN        NaN     90.0    NaN
# San Francisco total calls        109.0      NaN   NaN       90.0      NaN    NaN
#               total minutes      287.0      NaN   NaN      167.0      NaN    NaN

# Control sort order if needed.
print(churn_state_unstack.sort_index(ascending=False))
# time                             night                       day                
# state                       California New York  Ohio California New York   Ohio
# city          feature                                                           
# San Francisco total minutes      287.0      NaN   NaN      167.0      NaN    NaN
#               total calls        109.0      NaN   NaN       90.0      NaN    NaN
# New York      total minutes        NaN     84.0   NaN        NaN     90.0    NaN
#               total calls          NaN     84.0   NaN        NaN     75.0    NaN
# Los Angeles   total minutes      204.0      NaN   NaN      107.0      NaN    NaN
#               total calls        116.0      NaN   NaN       85.0      NaN    NaN
# Cleveland     total minutes        NaN      NaN  50.0        NaN      NaN  110.0
#               total calls          NaN      NaN  67.0        NaN      NaN   67.0
