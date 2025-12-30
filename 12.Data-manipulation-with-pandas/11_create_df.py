import pandas as pd

# date					small_sold	large_sold
# '2019-11-03'	10376832		7835071
# '2019-11-10'	10717154		8561348


# a df can be an array of objects (a list of dictionaries)
avocados_list = [
    {"date": "2019-11-03", "small_sold": 10376832, "large_sold": 7835071},
    {"date": "2019-11-10", "small_sold": 10717154, "large_sold": 8561348},
]
print(pd.DataFrame(avocados_list))
print()

# a df can also be an object of arrays
avocados_dict = {
    "date": ["2019-11-03", "2019-11-10"],
    "small_sold": [10376832, 10717154],
    "large_sold": [7835071, 8561348],
}
print(pd.DataFrame(avocados_dict))
