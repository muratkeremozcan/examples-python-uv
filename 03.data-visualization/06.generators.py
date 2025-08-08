# List comprehensions store all elements in memory immediately (eager evaluation).
# Generator expressions produce elements on demand (lazy evaluation, memory efficient).
# Generators can be created using expressions (x for x in iterable) or functions with yield.
# Once a generator is exhausted, you must recreate it to iterate again.

# List of strings
fellowship = ["frodo", "samwise", "merry", "aragorn", "legolas", "boromir", "gimli"]

# LIST COMPREHENSION VS GENERATOR EXPRESSION
# [output_if_true | for variable in iterable | if condition]
# (output_if_true | for variable in iterable | if condition)

# List comprehension: stores all elements in memory immediately
fellow1 = [member for member in fellowship if len(member) >= 7]
print(fellow1)

# Generator expression: produces elements on demand when iterated over (saving memory)
fellow2 = (member for member in fellowship if len(member) >= 7)
print(fellow2)  # Just prints the generator object

# Converting generator to list forces evaluation
print(list(fellow2))  # Converts generator output to a list

##########

# GENERATOR THAT PRODUCES VALUES FROM 0 TO 30
# A generator that lazily produces numbers 0 to 30
result = (num for num in range(0, 31))

# Fetching values using next()
print(next(result))  # 0
print(next(result))  # 1
print(next(result))  # 2
print(next(result))  # 3
print(next(result))  # 4

# The generator is now at position 5, and will continue from there
for value in result:
    print(value)  # Prints remaining values up to 30


#############
# Python has two types of generators:
# 	1.	Generator Expression → Uses () with list comprehension syntax.
# 	2.	Generator Function → Uses yield inside a function.


# GENERATOR FOR STRING LENGTHS


# Create a list of strings: lannister
lannister = ["cersei", "jaime", "tywin", "tyrion", "joffrey"]

# Generator expression: lazily computes string lengths
# If you use a list comprehension instead of a generator expression for lengths, the main difference would be memory usage and evaluation strategy
# Generator expression is useful for large datasets. List comprehension is
# faster for small lists, since accessing elements is instantaneous.
lengths = (len(person) for person in lannister)

# Iterating over generator to fetch values
for value in lengths:
    print(value)  # Prints lengths of each name


#############

# GENERATOR FUNCTION EXAMPLE


# Define generator function get_lengths
def get_lengths(input_list):
    """Generator function that yields the
    length of the strings in input_list."""

    # Yield the length of a string one at a time
    for person in input_list:
        yield len(
            person
        )  # Instead of returning all at once, it lazily yields one-by-one


# Calling the generator function and iterating over it
for value in get_lengths(lannister):
    print(
        value
    )  # Prints the lengths of names, just like the generator expression above
