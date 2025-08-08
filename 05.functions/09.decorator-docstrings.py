# Key Takeaways:
# - Using @wraps(func) lets you use docstring for the function being wrapped
# - Using __doc__ lets you access or print a function's documentation,
# - using .__wrapped can help us call the original function instead of the decorated one

import time
from functools import wraps


def add_hello(func):
    # makes it so that the docstring in print_sum works
    @wraps(func)
    def wrapper(*args, **kwargs):
        print("Hello")
        return func(*args, **kwargs)

    return wrapper


@add_hello
def print_sum(a, b):
    """Adds two numbers and prints the sum"""
    print(a + b)


print_sum(10, 20)
print_sum_docstring = print_sum.__doc__
print(print_sum_docstring)


###################


def check_inputs(*args, **kwargs):
    """Ensures that no positional or keyword argument is None."""
    for arg in args:
        if arg is None:
            raise ValueError("None value found in positional arguments!")
    for key, value in kwargs.items():
        if value is None:
            raise ValueError(f"None value found for keyword argument '{key}'!")


def check_outputs(result):
    """Ensures that the result is not None and is a list."""
    if result is None:
        raise ValueError("Function output is None!")
    # For example, if we expect a list:
    if not isinstance(result, list):
        raise ValueError("Function output is not a list!")


def check_everything(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        check_inputs(*args, **kwargs)

        result = func(*args, **kwargs)
        check_outputs(result)

        return result

    return wrapper


@check_everything
def duplicate(my_list):
    """Return a new list that repeats the input twice"""
    return my_list + my_list


t_start = time.time()
duplicated_list = duplicate(list(range(50)))
t_end = time.time()
decorated_time = t_end - t_start

t_start = time.time()
# Call the original function instead of the decorated one
duplicated_list = duplicate.__wrapped__(list(range(50)))
t_end = time.time()
undecorated_time = t_end - t_start

print("Decorated time: {:.5f}s".format(decorated_time))
print("Undecorated time: {:.5f}s".format(undecorated_time))
