# Like range(), enumerate() returns a lazy iterable instead of an actual list.
# Wrapping enumerate() in list() creates a list of tuples, each containing an index and a value.
# enumerate() is useful for looping with an index.
# By default, enumerate() starts at 0, but you can specify another starting index.

# Create a list of strings: mutants
mutants = [
    "charles xavier",
    "bobby drake",
    "kurt wagner",
    "max eisenhardt",
    "kitty pryde",
]

# Printing enumerate() directly just gives a weird iterator object, NOT the values.
print(enumerate(mutants))

# Wrapping it in list() forces evaluation and produces a list of tuples (index, value).
print(list(enumerate(mutants)))

# Convert enumerate to a list of tuples and store it.
mutant_list = list(enumerate(mutants))
print(mutant_list)

# Iterate through enumerate() normally, unpacking the index and value.
for index, value in enumerate(mutants):
    print(index, value)

# Change the starting index to 1 using the start parameter.
for index, value in enumerate(mutants, start=1):
    print(index, value)


####################
# Like enumerate() and range(), zip() returns a lazy iterable, not a list.
# Wrapping zip() in list() forces evaluation, creating a list of tuples where each tuple contains elements from corresponding positions in the input lists.
# zip() is useful for combining multiple iterables element-wise into a single iterable of tuples.
# If iterables are of different lengths, zip() stops at the shortest one (no padding occurs).
# Using *zip() unzips the data, effectively reversing zip().

aliases = ["prof x", "iceman", "nightcrawler", "magneto", "shadowcat"]
powers = [
    "telepathy",
    "thermokinesis",
    "teleportation",
    "magnetokinesis",
    "intangibility",
]

# Wrapping zip() in list() to create a list of tuples.
mutant_data = list(zip(mutants, aliases, powers))
print(mutant_data)

# Creating a zip object (lazy iterator) without forcing evaluation.
mutant_zip = zip(mutants, aliases, powers)
print(mutant_zip)  # Outputs a zip object reference, not the data.

# Iterating through a zip object unpacks values from all three lists.
for value1, value2, value3 in mutant_zip:
    print(value1, value2, value3)

###############
# Creating a zip object from two lists.
z1 = zip(mutants, powers)

# Printing a zip object directly doesn't show values, only memory location.
print(z1)

# Unpacking zip() with * forces evaluation and prints all tuple values.
print(*z1)

# Comparing *zip() vs list(zip()):
print(*zip(mutants, powers))  # Unzipped output (positional args)
print(list(zip(mutants, powers)))  # Fully evaluated list of tuples

# The previous print statement exhausted z1, so recreate it before reuse.
z1 = zip(mutants, powers)

# Unzipping: zip(*z1) reverses zip(), splitting data back into separate lists.
result1, result2 = zip(*z1)
print(result1)  # Should match mutants
print(result2)  # Should match powers

# Verify that the unzipped lists match the original input lists.
print(result1 == tuple(mutants))  # True
print(result2 == tuple(powers))  # True
