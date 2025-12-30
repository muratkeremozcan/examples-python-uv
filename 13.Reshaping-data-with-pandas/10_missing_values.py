import pandas as pd

# Missing-data reshaping takeaways tied to this example:
# - unstack can introduce NaNs when a subgroup lacks a churn flag; fill_value avoids that.
# - stack drops all-NaN rows by default; dropna=False keeps empty combos so you can fill them.
# - fillna plugs gaps explicitly (we use 0).

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

# Unstack churn level and fill missing values with zero (avoids NaNs for missing churn rows).
churn = churn.unstack(level="churn", fill_value=0)

# Sort by descending voice mail plan and ascending international plan
churn_sorted = churn.sort_index(
    level=["voice_mail_plan", "international_plan"], ascending=[False, True]
)
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

# Build a column MultiIndex so we can demo stack/dropna=False on real levels.
churn.columns = pd.MultiIndex.from_product(
    [["call"], ["day", "night"], [False, True]], names=["type", "scope", "churn"]
)
# type                                         call
# scope                                         day           night
# churn                                       False  True     False  True
# state international_plan voice_mail_plan
# LA    No                 No               106.818  100.0   96.909  119.0
#                          Yes              100.000    0.0   84.250    0.0
#       Yes                No                78.000   69.0   90.000  104.0
#                          Yes               71.000    0.0  101.000    0.0
# NY    No                 No                90.900   95.0  100.800  101.5
#                          Yes              115.000    0.0  121.000    0.0
#       Yes                No               109.000   87.0   99.000  113.0
#                          Yes              120.000    0.0   78.000    0.0

# Introduce a missing combo to create NaNs after stacking.
churn.loc[("NY", "Yes", "No"), ("call", "day", True)] = pd.NA
# type                                         call
# scope                                         day           night
# churn                                       False  True     False  True
# state international_plan voice_mail_plan
# LA    No                 No               106.818  100.0   96.909  119.0
#                          Yes              100.000    0.0   84.250    0.0
#       Yes                No                78.000   69.0   90.000  104.0
#                          Yes               71.000    0.0  101.000    0.0
# NY    No                 No                90.900   95.0  100.800  101.5
#                          Yes              115.000    0.0  121.000    0.0
#       Yes                No               109.000    NaN   99.000  113.0
#                          Yes              120.000    0.0   78.000    0.0


# Stack scope+churn; dropna=False keeps empty combos, then fill to make gaps explicit.
churn_stacked = churn.stack(level=["scope", "churn"], dropna=False)
churn_filled = churn_stacked.fillna(0)
print(churn_filled)
# type                                                     call
# state international_plan voice_mail_plan scope churn
# LA    No                 No              day   False  106.818
#                                                True   100.000
#                                          night False   96.909
#                                                True   119.000
#                          Yes             day   False  100.000
#                                                True     0.000
#                                          night False   84.250
#                                                True     0.000
#       Yes                No              day   False   78.000
#                                                True    69.000
#                                          night False   90.000
#                                                True   104.000
#                          Yes             day   False   71.000
#                                                True     0.000
#                                          night False  101.000
#                                                True     0.000
# NY    No                 No              day   False   90.900
#                                                True    95.000
#                                          night False  100.800
#                                                True   101.500
#                          Yes             day   False  115.000
#                                                True     0.000
#                                          night False  121.000
#                                                True     0.000
#       Yes                No              day   False  109.000
#                                                True     0.000
#                                          night False   99.000
#                                                True   113.000
#                          Yes             day   False  120.000
#                                                True     0.000
#                                          night False   78.000
#                                                True     0.000
