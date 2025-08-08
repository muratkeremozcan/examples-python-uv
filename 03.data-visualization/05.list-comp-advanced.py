# List comprehensions with conditionals filter or modify data in a single line.
# filter() provides an alternative functional approach to filtering data.
# Dict comprehensions work similarly to list comprehensions but produce dictionaries.
# map() can be used instead of comprehensions, but is often less readable.

# Conditional List Comprehensions
# [output_if_true | for variable in iterable | if condition]

# Given list of names
fellowship = ["frodo", "samwise", "merry", "aragorn", "legolas", "boromir", "gimli"]


# FILTERING: Keep names with 7 or more characters

# List comprehension version (filters out short names)
new_fellowship = [member for member in fellowship if len(member) >= 7]
print(new_fellowship)

# filter() version (functional programming alternative)
new_fellowship_filter = list(filter(lambda member: len(member) >= 7, fellowship))
print(new_fellowship_filter)


# CONDITIONAL MODIFICATION: Keep names with 7+ characters, replace shorter ones with ''

# List comprehension with conditional modification (if you use else, move the conditional to the middle)
# [output_if_true | if condition | else output_if_false | for variable in iterable]
new_fellowship2 = [member if len(member) >= 7 else "" for member in fellowship]
print(new_fellowship2)

# map() version (functional alternative, less readable)
new_fellowship2_map = list(
    map(lambda member: member if len(member) >= 7 else "", fellowship)
)
print(new_fellowship2_map)


########### Dictionary Comprehensions ###########

# DICTIONARY FILTERING: Store names as keys if they are 7+ characters,
# with name length as value

# Dictionary comprehension version
new_fellowship_dict = {member: len(member) for member in fellowship if len(member) >= 7}
print(new_fellowship_dict)

# filter() version for dictionaries (tuple generator + filter)
new_fellowship_filter_dict = dict(
    filter(
        lambda member: len(member[0]) >= 7,
        ((member, len(member)) for member in fellowship),
    )
)
print(new_fellowship_filter_dict)


# CONDITIONAL MODIFICATION IN DICTIONARY: Store name as key, replace short names with ''

# map() version (not very readable)
new_fellowship2_map_dict = dict(
    map(lambda member: (member, member if len(member) >= 7 else ""), fellowship)
)
print(new_fellowship2_map_dict)
