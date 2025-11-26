# *args in Python → ...args in JavaScript (rest parameters). Both collect extra
# positional args, into a tuple in Python and an array in JS.
# **kwargs collects keyword args into a dict; JS has no keyword args, but you
# usually pass an object and, if needed, use ... to copy/merge objects.


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

# // JavaScript equivalent
# // function concat1(...args) {
# //   let result = "";
# //   for (const arg of args) {
# //     result += " " + arg;
# //   }
# //   return result;
# // }
# // console.log(concat1("Python", "is", "great!"));


#######
# **kwargs vs *args: ** collects keyword args into a dict. JS doesn’t have
# keyword args; you pass an object (often via destructuring) and can spread it.


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

# // JavaScript-style approach
# // function concat(kwargs) {
# //   let result = "";
# //   for (const value of Object.values(kwargs)) {
# //     result += " " + value;
# //   }
# //   return result;
# // }
# // console.log(concat({ start: "Python", middle: "is", end: "great!" }));
