# Define clean_text, which has two arguments: text, and lower,
# with the latter having a default value of True
raw_text = "I LoVe dATaCamP"


def clean_text(text, lower=True):
    """Swap spaces to underscores and convert text to lowercase."""  # single line docstring
    if not lower:
        return text.replace(" ", "_")
    else:
        return text.replace(" ", "_").lower()


print(clean_text.__doc__)
help(clean_text)  # only prints to the console, not wolf
print(clean_text(raw_text))


# Re-define clean_text with arguments of text followed by remove,
# with the latter having a default value of None.


def clean_text_remove(text, remove=None):
    """
    Remove a specific substring from text and convert it to lowercase.

    Args:
        text (str): The input string to clean.
        remove (Optional[str]): The substring to remove. If None, no removal occurs. Defaults to None.

    Returns:
        str: The cleaned text with the specified substring removed and converted to lowercase.
    """
    if remove is not None:
        return text.replace(remove, "").lower()
    else:
        return text.lower()


print(clean_text_remove(raw_text, "L"))

# named arguments option: different to JS, in Python we can specify the arg names if we want
# In JS we can only do this with objects
print(clean_text_remove(text=raw_text, remove="L"))


#####################
# Define convert_data_structure with two arguments: data and data_type,
# where the latter has a default value of "list".


def convert_data_structure(data, data_type="list"):
    """
    Convert a data structure to a list, tuple, or set.

    Args:
          data (list, tuple, or set): A data structure to be converted.
      data_type (str): String representing the type of structure to convert data to.

    Returns:
          data (list, tuple, or set): Converted data structure.
    """
    # Add a condition to check if data_type is "tuple"
    if data_type == "tuple":
        data = tuple(data)

    # Else if data_type is set, convert to a set
    elif data_type == "set":
        data = set(data)

    else:
        data = list(data)

    return data


some_data = {"a", 1, "b", 2, "c", 3}

# Call the function to convert to a set
print(convert_data_structure(some_data, data_type="set"))
