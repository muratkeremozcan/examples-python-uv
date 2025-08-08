user_ids = [
    "T42YG4KTK",
    "VTQ39IDQ0",
    "CRL11YUWX",
    "K6Y5URXLR",
    "V4XCBER7V",
    "IOGQWC61K",
]

# Loop through user_ids
for user_id in user_ids:
    print(user_id)

# JS array: for of
# JS object: for in

#################

# Create the tickets_sold variable
tickets_sold = 0

# Create the max_capacity variable
max_capacity = 30

# Loop through a range up to and including max_capacity's value
for tickets in range(1, max_capacity + 1):
    # Add one to tickets_sold in each iteration
    tickets_sold += 1

# Print the final statement once all tickets are sold
print("Sold out:", tickets_sold, "tickets sold!")


#################

# Given dictionary of courses
courses = {
    "LLM Concepts": "AI",
    "Introduction to Data Pipelines": "Data Engineering",
    "AI Ethics": "AI",
    "Introduction to dbt": "Data Engineering",
    "Writing Efficient Python Code": "Programming",
    "Introduction to Docker": "Programming",
}

# Loop through the dictionary's keys and values
# items() makes the object an array of arrays (kind of)
for key, value in courses.items():

    # Check if the value is "AI"
    if value == "AI":
        print(key, "is an AI course")

    # Check if the value is "Programming"
    elif value == "Programming":
        print(key, "is a Programming course")

    # Otherwise, print that it is a "Data Engineering" course
    else:
        print(key, "is a Data Engineering course")
