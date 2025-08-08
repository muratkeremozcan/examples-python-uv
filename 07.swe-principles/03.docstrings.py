import re


def tokenize(text, regex=r"[a-zA-z]+"):
    """Split text into tokens using a regular expression

    :param text: text to be tokenized
    :param regex: regular expression used to match tokens using re.findall
    :return: a list of resulting tokens

    >>> tokenize('the rain in spain')
    ['the', 'rain', 'in', 'spain']
    """
    return re.findall(regex, text, flags=re.IGNORECASE)


# Print the docstring
# help(tokenize)

text_sample = "The quick brown fox jumps over the lazy dog!"
tokens = tokenize(text_sample)
print(f"Original text: {text_sample}")
print(f"Tokenized: {tokens}")


# __doc__ attribute
# What it does: Direct access to the raw docstring text
# Pros: Simple, direct access to the exact string
# Cons:
# Preserves all indentation (which can make output messy)
# Doesn't handle inheritance (if a subclass doesn't have a docstring, __doc__ just returns None)
# Best for: Programmatic access when you need the exact string

# 2. inspect.getdoc()
# What it does: Cleans up the docstring by:
# Removing excess indentation
# Finding inherited docstrings
# Pros:
# Returns cleaner text that's better for display
# Handles inheritance (if a class doesn't have a docstring, it checks parent classes)
# Cons: Requires importing the inspect module
# Best for: User-facing displays and tools that process docstrings

# 3. help()
# What it does: Provides comprehensive, formatted help including:
# Function/class/module signature
# Cleaned-up docstring
# Additional information about parameters, return types, etc.
# Pros: Most complete information in a human-readable format
# Cons: Not easily programmatically parsable
# Best for: Interactive use at the console, human readers
