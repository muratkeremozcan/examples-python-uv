# get docstring by fn.__doc__ or

import inspect


def count_letter(content, letter):
    """Count the number of times `letter` appears in `content`.

    :param content: The string to search
    :type content: str
    :param letter: The letter to search for (must be a single character)
    :type letter: str
    :return: The number of times `letter` appears in `content`
    :rtype: int
    :raises ValueError: If `letter` is not a single character string

    >>> count_letter("hello", "l")
    2
    """
    if (not isinstance(letter, str)) or len(letter) != 1:
        raise ValueError("`letter` must be a single character string.")
    return len([char for char in content if char == letter])


# using .__doc__
docstring = count_letter.__doc__

border = "#" * 28
print("{}\n{}\n{}".format(border, docstring, border))

# using inspect.getdoc
docstring2 = inspect.getdoc(count_letter)
print("{}\n{}\n{}".format(border, docstring2, border))


# custom fn
def build_tooltip(function):
    """Create a tooltip for any function that shows the function's docstring.

    :param function: The function we want a tooltip for
    :type function: callable
    :return: Formatted string containing the function's docstring
    :rtype: str

    >>> type(build_tooltip(count_letter))
    <class 'str'>
    """
    # Get the docstring for the "function" argument by using inspect
    docstring = inspect.getdoc(function)
    # docstring = function.__doc__ # same thing
    border = "#" * 28
    return "{}\n{}\n{}".format(border, docstring, border)


print(build_tooltip(count_letter))
print(build_tooltip(range))
print(build_tooltip(print))


########
text = "hello world"
letter = "l"

print(count_letter(text, letter))
