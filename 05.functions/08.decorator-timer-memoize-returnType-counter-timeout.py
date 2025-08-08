import signal
import time
from functools import wraps


def timer(func):
    """A decorator that prints how long a function took to run."""

    def wrapper(*args, **kwargs):
        t_start = time.time()

        result = func(*args, **kwargs)

        t_total = time.time() - t_start

        print(f"{func.__name__} took {t_total:.2f}s to run.")

        return result

    return wrapper


# Simulate a slow function by sleeping for 1 second
@timer
def slow_function():
    time.sleep(1)
    return "Finished sleeping"


print(slow_function())

#############


def memoize(func):
    """Store the results of the decorated function for fast lookups."""
    cache = {}

    def wrapper(*args, **kwargs):
        # Convert kwargs to a sorted tuple of key-value pairs.
        kwargs_key = tuple(sorted(kwargs.items()))
        # Combine args and kwargs_key into a single key.
        key = (args, kwargs_key)
        # If the key isn't in the cache, call func and store the result.
        if key not in cache:
            cache[key] = func(*args, **kwargs)

        return cache[key]

    return wrapper


# Example usage for the memoize decorator
# A recursive Fibonacci function that benefits from memoization
@memoize
def fibonacci(n):
    if n <= 1:
        return n
    return fibonacci(n - 1) + fibonacci(n - 2)


print("Fibonacci(10):", fibonacci(10))

#############


def print_return_type(func):
    # Define wrapper(), the decorated function
    def wrapper(*args, **kwargs):
        # Call the function being decorated
        result = func(*args, **kwargs)
        print("{}() returned type {}".format(func.__name__, type(result)))
        return result

    # Return the decorated function
    return wrapper


@print_return_type
def foo(value):
    return value


print(foo(42))
print(foo([1, 2, 3]))
print(foo({"a": 42}))

#############


def counter(func):
    def wrapper(*args, **kwargs):
        wrapper.count += 1
        # Call the function being decorated and return the result
        return func(*args, **kwargs)

    # Set count to 0 to initialize call count for each new decorated function
    wrapper.count = 0
    # Return the new decorated function
    return wrapper


# Decorate foo() with the counter() decorator
@counter
def foo():
    print("calling foo()")


foo()
foo()
print("foo() was called {} times.".format(foo.count))


##########


def timeout(seconds=5):
    """
    Decorator factory that returns a decorator to limit a function's runtime.
    If the function does not complete within 'seconds', a built-in TimeoutError is raised.
    """

    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            def handler(signum, frame):
                raise TimeoutError(
                    f"Function '{func.__name__}' timed out after {seconds} second(s)."
                )

            # Set the alarm
            signal.signal(signal.SIGALRM, handler)
            signal.alarm(seconds)

            try:
                return func(*args, **kwargs)
            finally:
                # Disable the alarm
                signal.alarm(0)

        return wrapper

    return decorator


# Example usage:


@timeout(10)
def slow_operation():
    time.sleep(12)
    return "Finished!"


try:
    print(slow_operation())
except TimeoutError as e:
    print(e)
