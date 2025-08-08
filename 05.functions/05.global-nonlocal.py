# Key Takeaways:
# - Use 'global' to modify variables outside the local function scope; otherwise, assignments create local variables.
# - 'nonlocal' works similarly for nested functions, letting you modify variables in an outer but non-global scope.

x = 50


def one():
    x = 10  # local var assignment doesn't effect the global variable (like const in JS)


def two():
    global x  # using the global assignment effects the global variable (like let in JS)
    x = 30


def three():
    x = 100  # local var assignment doesn't effect the global variable (like const in JS)
    print(x)


for func in [one, two, three]:
    func()
    print(x)


##########
# Sometimes your functions will need to modify a variable that is outside of the local scope of that function.
# While it's generally not best practice to do so, it's still good to know
# how in case you need to do it.

call_count = 0


def my_function():
    # Use a keyword that lets us update call_count
    global call_count
    call_count += 1

    print("You've called my_function() {} times!".format(call_count))


for _ in range(10):
    my_function()


######

# def read_files():
#   file_contents = None

#   def save_contents(filename):
#     nonlocal file_contents # nonlocal is like global, but in nested function context
#     if file_contents is None:
#       file_contents = []
#     with open(filename) as fin:
#       file_contents.append(fin.read())

#   for filename in ['1984.txt', 'MobyDick.txt', 'CatsEye.txt']:
#     save_contents(filename)

#   return file_contents

# print('\n'.join(read_files()))
