# print()
# max()
# min()
# sum()
# round()
# len()
# sorted()
# help()  gets information about a function

# Call help() directly, it prints its output
help(len)
help(int)

course_ratings = {
    "LLM Concepts": 4.7,
    "Introduction to Data Pipelines": 4.75,
    "AI Ethics": 4.62,
    "Introduction to dbt": 4.81,
}


# Print the number of key-value pairs
num_courses = len(course_ratings)
print(num_courses)

#######

course_completions = [97, 83, 121, 205, 56, 174, 92, 117, 164]

# Use a function to count the number of courses in course_completions,
# storing as num_courses, and print this variable
num_courses = len(course_completions)
print(num_courses)

# Use a function to count the number of characters in most_popular_course,
# storing as title_length, and print the variable.
most_popular_course = "Introduction to dbt"

title_length = len(most_popular_course)
print(title_length)

#############

# Add up and print the total number of course_completions.
print(sum(course_completions))

# Print the largest value in course_completions.
print(max(course_completions))

# Add up the values in course_completions and then divide this by the
# number of elements to get the average.
print(sum(course_completions) / len(course_completions))

# Round the average number of course completions to one decimal place.
print(round(sum(course_completions) / len(course_completions), 1))
