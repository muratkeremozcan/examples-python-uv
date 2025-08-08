# try except (like try catch in JS)
# an error occurs inside the try block, the except block executes instead of crashing the program
# Useful when handling expected errors without terminating execution.


def snake_case(text):
    # Use a keyword allowing you to attempt to run code that cleans text
    try:
        # swap a space for a single underscore in the text argument.
        return text.replace(" ", "_").lower()
    # Run this code if an error occurs
    except BaseException:
        print(
            "The snake_case() function expects a string as an argument, please check the data type provided."
        )
        return None


############################################

# raise  (not like anything in JS)
# immediately stops execution and raises an error.
# Used when you want to enforce strict type checking or conditions.

print(snake_case("User Name 187"))
# print(snake_case2(123))


def snake_case2(text):
    # Check the data type
    if isinstance(text, str):
        return text.replace(" ", "_").lower()

    else:
        raise TypeError(
            "The snake_case() function expects a string as an argument, please check the data type provided."
        )


print(snake_case2("User Name 187"))
# print(snake_case2(123))
