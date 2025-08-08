# - Use range(start, stop, step) to generate sequences; convert to lists with list(...) or [*...] (unpack/flatten)

# in python:
# •	range, enumerate, map → return iterators (lazy, efficient)  (they don't return an array like in JS)
# 	•	Iterators aren’t lists — they need to be “unpacked” or “materialized” to become list
# - unpack iterators with list(...) or [*...]

# - enumerate (and unpacked enumerate via [*enumerate(...)] / [list(enumerate(...))] / unpacking in comprehensions) attaches indices to elements.
# - [*enumerate(some_var, 1)] quickly converts an enumerate iterator (starting at 1) into a list of tuples (unpack/flatten)
# - Map() applies a function to all items; unpacking the result converts the iterator into a list.

# Create a range object that goes from 0 to 5
nums = range(5)
print(type(nums), "\n")

# convert to lists with list(...) or [*...]
nums_list = list(range(5))
nums_list2 = [
    *range(5),
]
print(
    nums_list,
)
print(nums_list2, "\n")

# range(start, stop, step)
nums_list2 = [*range(1, 12, 2)]
# list(range(..)) same as [*range(..)]
num_list3 = list(range(1, 12, 2))
print(nums_list2)
print(num_list3, "\n")

# enumerate

names = ["Jerry", "Kramer", "Elaine", "George", "Newman"]

# enumerate (and unpacked enumerate via [*enumerate(...)] / [list(enumerate(...))] / unpacking in comprehensions) attaches indices to elements.

indexed_names_0 = []
for i in range(len(names)):
    index_name = (i, names[i])
    indexed_names_0.append(index_name)
print(indexed_names_0)

indexed_names_1 = []
for i, name in enumerate(names):
    index_name = (i, name)  # (0, 'Jerry')...
    indexed_names_1.append(index_name)
print(indexed_names_1)

# using list comprehension
# unpacked into the two variables i (the index) and name
indexed_names_comp_3 = [(i, name) for i, name in enumerate(names)]
print(indexed_names_comp_3)

# Unpack an enumerate object with a starting index of 0 (BEST option)
indexed_names_unpack_4 = [*enumerate(names, 0)]
print(indexed_names_unpack_4)
indexed_names_unpack_5 = list(enumerate(names, 0))
print(indexed_names_unpack_5, "\n")

# map
names = ["Jerry", "Kramer", "Elaine", "George", "Newman"]

# Use map to apply str.upper to each element in names
names_map = map(str.upper, names)
print(names_map)
print(type(names_map))

# Unpack names_map into a list
print([*names_map])
# if you want to 1 step map
print([*map(str.upper, names)])
print(list(map(str.upper, names)))
