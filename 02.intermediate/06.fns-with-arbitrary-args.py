# *args in Python → ...args in JavaScript
# *args in Python collects multiple positional arguments into a tuple,
# which is like ...args in JavaScript, which collects arguments into an array.

# and **kwargs is the spread operator ... in JS


# Define a function called concat() that accepts arbitrary arguments called arg
def concat1(*args):
    # Create a variable called result and assign an empty string to it
    result = ""

    # Use a for loop to iterate over each arg in args.
    for arg in args:
        result += " " + arg
    return result


# Call the function
print(concat1("Python", "is", "great!"))

# function concat1(...args) {
#   let result = '';
#   for (const arg of args) {
#     result += ' ' + arg;
#   }
#   return result;
# }
# console.log(concat1("Python", "is", "great!"));


#######
# **kwargs vs *args :  ** auto converts the args into an object
# not really 1:1 with JS; in JS we would convert the args into an object ourselves


# Define concat() as a function that accepts arbitrary keyword arguments called kwargs.
def concat2(**kwargs):
    # Create a variable called result and assign an empty string to it
    result = ""

    # Inside the function, loop over the keyword argument values, using kwarg
    # as the iterator.
    for kwarg in kwargs.values():
        result += " " + kwarg
    return result


print(concat2(start="Python", middle="is", end="great!"))

# function concat(...args) {
#   // we have to convert it to an object
#   const kwargs = Object.assign({}, ...args); // Merge args into a single object
#   let result = '';

#   for (const value of Object.values(kwargs)) {
#     result += ' ' + value;
#   }

#   return result;
# }

# console.log(concat({ start: 'Python', middle: 'is', end: 'great!' }));
