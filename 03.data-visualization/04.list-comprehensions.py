# List comprehensions condense for loops into a single line.
# map() is an alternative functional approach to applying operations over iterables.
# Lambda functions make map() more concise but are sometimes less readable than comprehensions.
# Matrix creation can be done using loops, comprehensions, or map().

doctor = ["house", "cuddy", "chase", "thirteen", "wilson"]

# Regular for loop
for doc in doctor:
    print(doc)

# List comprehension version (not ideal for side effects like print)
# [output_if_true | for variable in iterable | if condition]
[print(doc) for doc in doctor]

# Using map() for the same effect
list(map(print, doctor))


##############
# Extract first character from each string

# For loop version
for doc in doctor:
    print(doc[0])

# List comprehension version
# [output_if_true | for variable in iterable | if condition]
[print(doc[0]) for doc in doctor]

# Using map() (functional approach)
list(map(lambda doc: print(doc[0]), doctor))


##############
# Generating a list of squared numbers (0–9)

# List comprehension version
# [output_if_true | for variable in iterable | if condition]
squared_numbers = [i**2 for i in range(10)]
print(squared_numbers)

# Traditional for loop version
squared_numbers_loop = []
for i in range(10):
    squared_numbers_loop.append(i**2)
print(squared_numbers_loop)

# map() version with lambda
squared_numbers_map = list(map(lambda i: i**2, range(10)))
print(squared_numbers_map)


##############
# Creating a simple matrix (5x5) with incremental values in each row

# matrix = [[0, 1, 2, 3, 4],
#           [0, 1, 2, 3, 4],
#           [0, 1, 2, 3, 4],
#           [0, 1, 2, 3, 4],
#           [0, 1, 2, 3, 4]]

# 1 row using list comprehension
# [output_if_true | for variable in iterable | if condition]
print([col for col in range(5)])

# 1 row using a for loop
row_list = []
for col in range(5):
    row_list.append(col)
print(row_list)

# 1 row using map()
row_list_map = list(map(lambda col: col, range(5)))
print(row_list_map)


# Full matrix (5x5)

# List comprehension version
# [output_if_true | for variable in iterable | if condition]
matrix_comp = [[col for col in range(5)] for row in range(5)]
print(matrix_comp)

# map() version (more functional, less readable)
matrix_map = list(map(lambda _: list(map(lambda col: col, range(5))), range(5)))
print(matrix_map)


# For loop version
matrix = []
for col in range(5):  # rows
    row_list = []  # empty list for each row
    for row in range(5):  # columns
        row_list.append(col)  # Append col value to row
    matrix.append(row_list)  # Append the row to the matrix
print(matrix)


# Function versions for creating matrices
# List comprehension version as a function
def matrix_lambda_comp(rows, cols):
    return [[col for col in range(cols)] for row in range(rows)]


print(matrix_lambda_comp(5, 5))

# Using map() as a function


def matrix_lambda_map(rows, cols):
    return list(map(lambda _: list(map(lambda col: col, range(cols))), range(rows)))


print(matrix_lambda_map(5, 5))


# Regular function version
def create_matrix(rows, cols):
    matrix = []
    for col in range(rows):  # rows
        row_list = []  # empty list for each row
        for row in range(cols):  # columns
            row_list.append(col)  # Append col value to row
        matrix.append(row_list)
    return matrix


print(create_matrix(5, 5))
