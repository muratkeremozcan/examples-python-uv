import pandas as pd

# Key takeaways (merge_asof):
# - Use it when time-series keys don't line up and you want the closest right-side value.
# - Think: \"latest value as of this time\" (left join on nearest, not exact).
# - Both tables must be sorted by the key column.
# - direction controls which nearest row is picked:
#   - backward (default): last right key ≤ left key
#   - forward: first right key ≥ left key
#   - nearest: closest right key in either direction


# Hourly Visa prices (left table).
visa = pd.DataFrame(
    {
        "date_time": [
            "2017-11-11 09:00",
            "2017-11-11 10:00",
            "2017-11-11 11:00",
            "2017-11-11 12:00",
        ],
        "price": [102.1, 102.8, 103.4, 103.0],
    }
)
# print(visa)
#           date_time  price
# 0  2017-11-11 09:00  102.1
# 1  2017-11-11 10:00  102.8
# 2  2017-11-11 11:00  103.4
# 3  2017-11-11 12:00  103.0

# IBM prices sampled roughly every 5 minutes (right table).
ibm = pd.DataFrame(
    {
        "date_time": [
            "2017-11-11 08:55",
            "2017-11-11 09:05",
            "2017-11-11 09:55",
            "2017-11-11 10:03",
            "2017-11-11 10:55",
        ],
        "price": [149.11, 149.30, 149.25, 149.40, 149.10],
    }
)
# print(ibm)
#           date_time   price
# 0  2017-11-11 08:55  149.11
# 1  2017-11-11 09:05  149.30
# 2  2017-11-11 09:55  149.25
# 3  2017-11-11 10:03  149.40
# 4  2017-11-11 10:55  149.10

# Ensure sorted datetime keys for merge_asof.
visa["date_time"] = pd.to_datetime(visa["date_time"])
ibm["date_time"] = pd.to_datetime(ibm["date_time"])
visa_sorted = visa.sort_values("date_time")
ibm_sorted = ibm.sort_values("date_time")

# Backward (default): last right key <= left key.
visa_ibm_back = pd.merge_asof(
    visa_sorted,
    ibm_sorted,
    on="date_time",
    suffixes=("_visa", "_ibm"),
)
# print(visa_ibm_back)
#             date_time  price_visa  price_ibm
# 0 2017-11-11 09:00:00       102.1     149.11
# 1 2017-11-11 10:00:00       102.8     149.25
# 2 2017-11-11 11:00:00       103.4     149.10
# 3 2017-11-11 12:00:00       103.0     149.10

# Forward: first right key >= left key.
visa_ibm_forward = pd.merge_asof(
    visa_sorted,
    ibm_sorted,
    on="date_time",
    suffixes=("_visa", "_ibm"),
    direction="forward",
)
# print(visa_ibm_forward)
#             date_time  price_visa  price_ibm
# 0 2017-11-11 09:00:00       102.1      149.3
# 1 2017-11-11 10:00:00       102.8      149.4
# 2 2017-11-11 11:00:00       103.4        NaN
# 3 2017-11-11 12:00:00       103.0        NaN

# Nearest: closest key in either direction.
visa_ibm_nearest = pd.merge_asof(
    visa_sorted,
    ibm_sorted,
    on="date_time",
    suffixes=("_visa", "_ibm"),
    direction="nearest",
)
print(visa_ibm_nearest)
print()

########################
# Compare to a standard merge.
#
# Most similar to: left join (keeps all left rows).
# Key distinction: merge_asof matches on the nearest key, not exact equality.

# Exact-match left join (only matches identical timestamps).
visa_ibm_exact = visa_sorted.merge(
    ibm_sorted, on="date_time", how="left", suffixes=("_visa", "_ibm")
)
print(visa_ibm_exact)
#             date_time  price_visa  price_ibm
# 0 2017-11-11 09:00:00       102.1        NaN
# 1 2017-11-11 10:00:00       102.8        NaN
# 2 2017-11-11 11:00:00       103.4        NaN
# 3 2017-11-11 12:00:00       103.0        NaN
