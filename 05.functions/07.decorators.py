# Key Takeaways:
# - Decorators wrap functions to modify their behavior without altering their code.
# - They allow you to intercept and modify arguments or outputs of the decorated function.
# - The @decorator syntax provides a concise, readable way to apply decorators.


# the decorator
def double_args(func):
    def wrapper(a, b):
        return func(a * 2, b * 2)

    return wrapper


def multiply(a, b):
    return a * b


multiplyD = double_args(multiply)
multiplyD(1, 5)  # ?

# decorator version


@double_args
def multiplyD(a, b):
    return a * b


multiplyD(1, 5)  # ?


##########################


# the decorator
def print_args(func):
    # *args captures any extra positional arguments (the “regular” ones), and **kwargs captures any extra named (keyword) arguments
    def wrapper(*args, **kwargs):
        print("Called with arguments:", args, kwargs)
        return func(*args, **kwargs)

    return wrapper


def my_function(a, b, c):
    print(a + b + c)


my_functionD = print_args(my_function)

my_function(1, 2, 3)

# decorator version


@print_args
def my_function2(a, b, c):
    print(a + b + c)


my_function2(4, 5, 6)


###########################


def print_before_and_after(func):
    def wrapper(*args):
        print("Before {}".format(func.__name__))
        # Call the function being decorated with *args
        func(*args)
        print("After {}".format(func.__name__))

    # Return the nested function
    return wrapper


@print_before_and_after
def multiply(a, b):
    print(a * b)


multiply(5, 10)
