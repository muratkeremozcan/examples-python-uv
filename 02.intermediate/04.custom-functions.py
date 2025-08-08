# Define a function called clean_string, which takes an argument called text
def clean_string(text):
    # Replace spaces with underscores
    no_spaces = text.replace(" ", "_")
    # Convert to lowercase
    clean_text = no_spaces.lower()
    # Return the final text as an output
    return clean_text


raw_text = "I LoVe dATaCamP"
converted_text = clean_string("I LoVe dATaCamP")

print(converted_text)

# one liner


def clean_string2(text):
    return text.replace(" ", "_").lower()


print(clean_string2(raw_text))

# one liner like arrow function


def clean_string3(text):
    return text.replace(" ", "_").lower()


print(clean_string3(raw_text))


##############

sauce = "not_very_saucy_2023"


# Define the checker function
def checker(submission):
    # Check if the variable and submission match
    if sauce == submission:
        print("Successful!")
    else:
        print("Incorrect")


# Call the function with the correct argument
checker("NOT_VERY_SAUCY_2023")
