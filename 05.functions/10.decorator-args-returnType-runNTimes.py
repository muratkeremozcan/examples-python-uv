# Key takeaways
# - Decorator factories can accept arguments.

from functools import wraps

# - run_n_times: Runs the decorated function a specified number of times.


def run_n_times(n):
    def decorator(func):
        def wrapper(*args, **kwargs):
            for _ in range(n):
                func(*args, **kwargs)
            return None

        return wrapper

    return decorator


@run_n_times(3)
def sum(a, b):
    print(a + b)


print(sum(1, 2))


#############
# - html: Wraps the function’s return value with custom HTML tags.


def html(open_tag, close_tag):
    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            msg = func(*args, **kwargs)
            return "{}{}{}".format(open_tag, msg, close_tag)

        return wrapper

    return decorator


@html("<b>", "</b>")
def hello(name):
    return "Hello {}!".format(name)


print(hello("Alice"))


@html("<i>", "</i>")
def goodbye(name):
    return "Goodbye {}!".format(name)


print(goodbye("Alice"))


@html("<div>", "</div>")
def hello_goodbye(name):
    return "\n{}\n{}\n".format(hello(name), goodbye(name))


print(hello_goodbye("Alice"))


#######
#  a decorator that will let you tag your functions with an arbitrary list of tags


def tag(*tags):
    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            return func(*args, **kwargs)

        wrapper.tags = tags
        return wrapper

    # Return the new decorator
    return decorator


@tag("test", "this is a tag")
def foo():
    pass


print(foo.tags)

############
# a decorator that returns the return type of a function


def returns(return_type):
    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            result = func(*args, **kwargs)

            assert isinstance(
                result, return_type
            ), f"Expected {return_type}, but got {type(result)}"
            return result

        return wrapper

    return decorator


@returns(list)
def foo(value):
    return value


try:
    print(foo([1, 2, 3]))
except AssertionError:
    print("foo() did not return a dict!")


@returns(dict)
def foo2(value):
    return value


try:
    print(foo2([1, 2, 3]))
except AssertionError:
    print("foo() did not return a dict!")
