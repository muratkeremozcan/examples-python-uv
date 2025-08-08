# Like lists, iterators allow sequential access to data, but they don’t store all values in memory.
# The iter() function converts an iterable into an iterator, allowing it to be used with next().
# Iterators remember their current position and only advance forward.
# Calling next() on an iterator retrieves the next value.
# Once exhausted, an iterator raises a StopIteration error.

# Create a list of strings: flash
flash = ["jay garrick", "barry allen", "wally west", "bart allen"]

# Loop over the list normally and print values
for f in flash:
    print(f)

# Convert the list into an iterator
superhero = iter(flash)

# Manually retrieve values using next()
print(next(superhero))
print(next(superhero))
# print(next(superhero))  # Uncommenting will continue iteration
# print(next(superhero))  # Uncommenting will continue iteration

#############
# range() is an iterator-like object that generates numbers lazily, without storing them.
# The iter() function isn’t necessary for range() because it already
# behaves like an iterator.

# Create an iterator from range(3)
small_value = iter(range(3))

# Retrieve values using next()
print(next(small_value))
# print(next(small_value))  # Uncomment to continue iteration
# print(next(small_value))  # Uncomment to continue iteration

# Looping over range() directly eliminates the need for iter() and next().
for v in range(3):
    print(v)

# Large ranges can be iterated over lazily without memory issues.
googol = iter(range(10**100))

# Print first five values of an extremely large range
print(next(googol))
print(next(googol))
print(next(googol))
print(next(googol))
print(next(googol))

########
# range() is NOT a list by default; it is a lightweight iterable.
# To store its values in memory, use list().
# Useful for generating sequences without taking up memory space.

# Create a range object from 10 to 20
values = range(10, 21)

# Printing a range object directly doesn’t show the numbers.
print(values)

# Convert range to a list explicitly
values_list = list(values)
print(values_list)

# Compute the sum of the range (works directly on range objects)
values_sum = sum(values)
print(values_sum)
