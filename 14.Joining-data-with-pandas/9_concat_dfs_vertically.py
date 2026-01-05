import pandas as pd

# Key takeaways (concat vertically):
# - pd.concat stacks rows (grows the table vertically).
# - ignore_index=True resets the index.
# - keys= adds labels (MultiIndex) to track source tables.
# - join="outer" keeps all columns; join="inner" keeps only shared columns.

# Monthly invoice tables with the same columns.
inv_jan = pd.DataFrame(
    {
        "invoice_id": [1, 2],
        "customer": ["Ava", "Bo"],
        "amount": [20, 35],
    }
)
# print(inv_jan)
#    invoice_id customer  amount
# 0           1      Ava      20
# 1           2       Bo      35

inv_feb = pd.DataFrame(
    {
        "invoice_id": [3, 4],
        "customer": ["Cy", "Dee"],
        "amount": [15, 40],
    }
)
# print(inv_feb)
#    invoice_id customer  amount
# 0           3       Cy      15
# 1           4      Dee      40

inv_mar = pd.DataFrame(
    {
        "invoice_id": [5, 6],
        "customer": ["Eli", "Fay"],
        "amount": [25, 30],
    }
)
# print(inv_mar)
#    invoice_id customer  amount
# 0           5      Eli      25
# 1           6      Fay      30

# Basic vertical concat (axis=0 by default).
inv_q1 = pd.concat([inv_jan, inv_feb, inv_mar])
# print(inv_q1)
#    invoice_id customer  amount
# 0           1      Ava      20
# 1           2       Bo      35
# 0           3       Cy      15
# 1           4      Dee      40
# 0           5      Eli      25
# 1           6      Fay      30

# Reset the index if it has no meaning.
inv_q1_reset = pd.concat([inv_jan, inv_feb, inv_mar], ignore_index=True)
# print(inv_q1_reset)
#    invoice_id customer  amount
# 0           1      Ava      20
# 1           2       Bo      35
# 2           3       Cy      15
# 3           4      Dee      40
# 4           5      Eli      25
# 5           6      Fay      30

# Add labels to track the source table (keep ignore_index=False).
inv_q1_labeled = pd.concat([inv_jan, inv_feb, inv_mar], keys=["jan", "feb", "mar"])
# print(inv_q1_labeled)
#          invoice_id customer  amount
# jan 0            1      Ava      20
#     1            2       Bo      35
# feb 0            3       Cy      15
#     1            4      Dee      40
# mar 0            5      Eli      25
#     1            6      Fay      30

# ########################
# Different columns example.

inv_feb_extra = inv_feb.assign(bill_country=["US", "US"])
# print(inv_feb_extra)
#    invoice_id customer  amount bill_country
# 0           3       Cy      15           US
# 1           4      Dee      40           US

# Outer join keeps all columns (bill_country is NaN for Jan/Mar).
inv_all_cols = pd.concat([inv_jan, inv_feb_extra, inv_mar], sort=True, join="outer")
print(inv_all_cols)
#    amount bill_country customer  invoice_id
# 0      20          NaN      Ava           1
# 1      35          NaN       Bo           2
# 0      15           US       Cy           3
# 1      40           US      Dee           4
# 0      25          NaN      Eli           5
# 1      30          NaN      Fay           6

# Inner join keeps only shared columns.
inv_shared_cols = pd.concat([inv_jan, inv_feb_extra, inv_mar], sort=True, join="inner")
print(inv_shared_cols)
#    amount customer  invoice_id
# 0      20      Ava           1
# 1      35       Bo           2
# 0      15       Cy           3
# 1      40      Dee           4
# 0      25      Eli           5
# 1      30      Fay           6
