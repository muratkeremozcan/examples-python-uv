import pandas as pd

# A package is a collection of modules organized in a directory that contains a special file: __init__.py (like index.ts)
# This tells Python that the directory should be treated as a package.

sales = {
    "user_id": ["KM37", "PR19", "YU88", "JB18", "LP65", "HJ11", "PR19", "IJ54"],
    "date": [
        "01/05/2024",
        "01/05/2024",
        "01/06/2024",
        "01/06/2024",
        "01/06/2024",
        "01/06/2024",
        "01/07/2024",
        "01/07/2024",
    ],
    "order_value": [197.75, 208.21, 134.99, 317.81, 201.3, 157.87, 99.99, 124.5],
}

# Convert sales to a pandas DataFrame
sales_dict_df = pd.DataFrame(sales)

# Preview the first five rows
print(sales_dict_df.head())
print(sales_dict_df)

#############

sales_df = pd.read_csv("sales.csv")

# Subset sales_df on the "order_value" column, then call the .mean()
# method to find the average order value.
print(sales_df["order_value"].mean())

# Subset sales_df on the "order_value" column, then call the .sum() method
# to find the total value of all orders.
print(sales_df["order_value"].sum())


########
# simple dataframe example
# data frame vs list/array dict/obj

data = ["Apple", "Banana", "Cherry"]


print(pd.DataFrame(data))
# 0
# 0 Apple
# 1 Banana
# 2 Cherry

print(pd.DataFrame(data, columns=["Fruits"]))
# Fruits
# 0 Apple
# 1 Banana
# 2 Cherry

data2 = [["Apple", 10], ["Banana", 15], ["Cherry", 20]]

print(pd.DataFrame(data2))
# 0 1
# 0 Apple 10
# 1 Banana 15
# 2 Cherry 20

print(pd.DataFrame(data2, columns=["Fruits", "Amount"]))
# Fruits Amount
# 0 Apple 10
# 1 Banana 15
# 2 Cherry 20

# A dict/obj dataframe looks the same
data3 = {"Apple": 10, "Banana": 15, "Cherry": 20}
print(pd.DataFrame(data3.items()))
# 0 1
# 0 Apple 10
# 1 Banana 15
# 2 Cherry 20
