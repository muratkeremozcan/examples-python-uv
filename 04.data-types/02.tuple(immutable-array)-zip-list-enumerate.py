# tuples
# difference with list/array: immutable

# Tuples can be unpacked into multiple variables for better readability.
# zip() combines elements from multiple lists into tuples, making pairwise iteration easier.
# enumerate() tracks position while looping, providing an index along with values.
# Using f-strings allows for cleaner and more readable formatted output.


girl_names = ["Emma", "Olivia", "Ava", "Sophia", "Isabella"]
boy_names = ["Liam", "Noah", "William", "James", "Oliver"]

# zip() returns an iterable (lazy evaluation)
# list() forces the evaluation of the iterable (stores results in memory)
pairs = list(zip(girl_names, boy_names))
print(pairs)


# Like range(), enumerate() returns a lazy iterable instead of an actual list.
# Wrapping enumerate() in list() creates a list of tuples, each containing an index and a value.
# enumerate() is useful for looping with an index.
# By default, enumerate() starts at 0, but you can specify another starting index.
print(enumerate(pairs))
print(list(enumerate(pairs)))

# Iterate over pairs while keeping track of position using enumerate()
for rank, pair in enumerate(pairs):  # or you could say enumerate(pairs, start=0)

    # unpack the tuple
    girl_name, boy_name = pair

    # Print formatted output; print(f'...') is like template literal in JS
    print(f"Rank {rank + 1}: {girl_name} and {boy_name}")

# zip(girl_names, boy_names) → Combines lists into pairs
# enumerate(pairs) → Adds a ranking number
# for rank, pair in enumerate(pairs, start=1) → Loops over ranked pairs


###########
# Careful! A trailing comma (,') in an assignment makes it a tuple!

# Create the normal variable: normal
normal = "simple"  # This is just a normal string

# Create the mistaken variable: error
error = ("trailing comma",)  # The trailing comma makes this a tuple!

# Print the types of the variables
print(type(normal))  # Output: <class 'str'> → It's a normal string
print(type(error))  # Output: <class 'tuple'> → Because of the comma!
