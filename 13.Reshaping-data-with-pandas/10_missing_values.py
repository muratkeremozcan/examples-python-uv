import pandas as pd

# Missing-data reshaping takeaways:
# - unstack can create NaNs when row subgroups lack matching labels; 
#  fill with fill_value or later fillna.

# - stack drops all-NaN rows by default (dropna=True); 
#  set dropna=False to keep the full cartesian result, then fillna as needed.

churn = pd.DataFrame(
    [
        ["LA", "No", "No", False, 106.818, 96.909],
        ["LA", "No", "No", True, 100.0, 119.0],
        ["LA", "No", "Yes", False, 100.0, 84.25],
        ["NY", "No", "No", False, 90.9, 100.8],
        ["NY", "No", "No", True, 95.0, 101.5],
        ["NY", "No", "Yes", False, 115.0, 121.0],
        ["NY", "Yes", "No", False, 109.0, 99.0],
        ["NY", "Yes", "No", True, 87.0, 113.0],
        ["LA", "Yes", "No", False, 78.0, 90.0],
        ["LA", "Yes", "No", True, 69.0, 104.0],
        ["NY", "Yes", "Yes", False, 120.0, 78.0],
        ["LA", "Yes", "Yes", False, 71.0, 101.0],
    ],
    columns=[
        "state",
        "international_plan",
        "voice_mail_plan",
        "churn",
        "total_day_calls",
        "total_night_calls",
    ],
).set_index(["state", "international_plan", "voice_mail_plan", "churn"])

#                                                 total_day_calls  total_night_calls
# state international_plan voice_mail_plan churn                                    
# LA    No                 No              False          106.818             96.909
#                                          True           100.000            119.000
#                          Yes             False          100.000             84.250
# NY    No                 No              False           90.900            100.800
#                                          True            95.000            101.500
#                          Yes             False          115.000            121.000
#       Yes                No              False          109.000             99.000
#                                          True            87.000            113.000
# LA    Yes                No              False           78.000             90.000
#                                          True            69.000            104.000
# NY    Yes                Yes             False          120.000             78.000
# LA    Yes                Yes             False           71.000            101.000

# Unstack churn level and fill missing values with zero
churn = churn.unstack(level="churn", fill_value=0)

# Sort by descending voice mail plan and ascending international plan
churn_sorted = churn.sort_index(level=["voice_mail_plan", "international_plan"], 
                                ascending=[False, True])
#                                          total_day_calls        total_night_calls       
# churn                                              False   True             False   True
# state international_plan voice_mail_plan                                                
# LA    No                 Yes                     100.000    0.0            84.250    0.0
# NY    No                 Yes                     115.000    0.0           121.000    0.0
# LA    Yes                Yes                      71.000    0.0           101.000    0.0
# NY    Yes                Yes                     120.000    0.0            78.000    0.0
# LA    No                 No                      106.818  100.0            96.909  119.0
# NY    No                 No                       90.900   95.0           100.800  101.5
# LA    Yes                No                       78.000   69.0            90.000  104.0
# NY    Yes                No                      109.000   87.0            99.000  113.0

# Stack the level type from churn
churn_stack = churn.stack(level="type", dropna=False)

# Fill the resulting missing values with zero 
churn_fill = churn_stack.fillna(0)


# Stack the level scope without dropping rows with missing values
churn_stack = churn.stack(level="scope", dropna=False)

# Fill the resulting missing values with zero
churn_fill = churn_stack.fillna(0)

# Print churn_fill
print(churn_fill)