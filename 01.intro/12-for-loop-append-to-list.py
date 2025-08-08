authors = {
    "J.K. Rowling": 15,
    "Stephen King": 65,
    "Agatha Christie": 85,
    "George Orwell": 12,
    "J.R.R. Tolkien": 20,
    "Jane Austen": 6,
    "Leo Tolstoy": 10,
    "Mark Twain": 30,
    "Charles Dickens": 25,
    "F. Scott Fitzgerald": 5,
}

# Create an empty list
authors_below_twenty_five = []

# Loop through the authors dictionary
for key, value in authors.items():

    # Check for values less than 25
    if value < 25:
        # Append the author to the list
        authors_below_twenty_five.append(key)

print(authors_below_twenty_five)


##########
# Given dictionary of genre sales
genre_sales = {
    "Fantasy": 5166000000,
    "Mystery": 3000000000,
    "Science Fiction": 1200000000,
    "Historical Fiction": 80000000,
    "Romance": 2200000000,
}

# Find the maximum and minimum sales dynamically
min_sales = min(genre_sales.values())
max_sales = max(genre_sales.values())

# Loop through the dictionary
for genre, average_sale in genre_sales.items():

    # Filter for the maximum sales value
    if average_sale == max_sales:
        # Print the most popular genre
        print("Most popular genre:", genre)
        print("Average sales:", average_sale)

    # Filter for the minimum sales value
    elif average_sale == min_sales:
        # Print the least popular genre
        print("Least popular genre:", genre)
        print("Average sales:", average_sale)

# Loop through the dictionary
for genre, sale in genre_sales.items():

    # Check if genre is Horror or Mystery
    if genre == "Horror" or genre == "Mystery":
        print(genre, sale)

    # Check if genre is Thriller and sale is at least 3 million
    elif genre == "Thriller" and sale >= 3000000:
        print(genre, sale)
