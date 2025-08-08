import math
import random


def mean(data):
    """Return the arithmetic mean of the data."""
    return sum(data) / len(data) if data else 0


def std(data):
    """Return the standard deviation of the data."""
    m = mean(data)
    variance = sum((x - m) ** 2 for x in data) / len(data) if data else 0
    return math.sqrt(variance)


def minimum(data):
    """Return the minimum value in the data."""
    return min(data) if data else None


def maximum(data):
    """Return the maximum value in the data."""
    return max(data) if data else None


def load_data():
    """
    Simulate loading data.
    In a real application, this function would load your dataset from a file or database.
    Here, we just return a list of numbers.
    """
    return [random.randint(1, 100) for _ in range(20)]


def get_user_input():
    """
    Simulate user input.
    Randomly returns one of the four function names.
    """
    return random.choice(["mean", "std", "minimum", "maximum"])


# Build the function map using the helper functions
function_map = {"mean": mean, "std": std, "minimum": minimum, "maximum": maximum}

data = load_data()
print(data)

func_name = get_user_input()
print(func_name)

# Call the chosen function and pass "data" as an argument
function_map[func_name](data)  # ?


###################################


def has_docstring(func):
    """
    Check to see if the function `func` has a docstring.

    Args:
      func (callable): A function.

    Returns:
      bool: True if func has a docstring, False otherwise.
    """
    return func.__doc__ is not None


# Dummy function definitions for testing
def load_and_plot_data():
    """
    Load and plot data from a file.
    This is a placeholder implementation.
    """
    pass


# Intentionally missing a docstring for testing purposes
def as_2D():
    pass


def log_product():
    """
    Log the product of two numbers.
    This is a placeholder implementation.
    """
    pass


# Check each function for a docstring

# Check load_and_plot_data
if not has_docstring(load_and_plot_data):
    print("load_and_plot_data() doesn't have a docstring!")
else:
    print("load_and_plot_data() looks ok")

# Check as_2D
if not has_docstring(as_2D):
    print("as_2D() doesn't have a docstring!")
else:
    print("as_2D() looks ok")

# Check log_product
if not has_docstring(log_product):
    print("log_product() doesn't have a docstring!")
else:
    print("log_product() looks ok")


######################


def create_math_function(func_name):
    if func_name == "add":

        def add(a, b):
            return a + b

        return add
    elif func_name == "subtract":
        # Define the subtract() function
        def subtract(a, b):
            return a - b

        return subtract
    else:
        print("I don't know that one")


add = create_math_function("add")
print("5 + 2 = {}".format(add(5, 2)))

subtract = create_math_function("subtract")
print("5 - 2 = {}".format(subtract(5, 2)))
