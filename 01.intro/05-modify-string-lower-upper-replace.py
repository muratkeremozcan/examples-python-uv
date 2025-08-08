most_popular_course = "Intro to Embeddings with the OpenAI API"

# Update the first word
most_popular_course = most_popular_course.replace("Intro", "Introduction")

# Swap spaces to underscores throughout the string contained in most_popular_course.
most_popular_course = most_popular_course.replace(" ", "_")

# Update most_popular_course so that it only contains lowercase characters.
most_popular_course = most_popular_course.lower()

print(most_popular_course)

print(most_popular_course.upper())
