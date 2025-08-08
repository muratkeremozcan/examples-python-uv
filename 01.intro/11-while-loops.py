tickets_sold = 0
max_capacity = 10

while tickets_sold < max_capacity:

    tickets_sold += 1

print("Sold out:", tickets_sold, "tickets sold!")

###########

release_date = 26
current_date = 22

# Create a conditional loop while current_date is less than or equal to release_date
while current_date <= release_date:
    # Promote purchases before the 25th
    if current_date <= 24:
        print("Purchase before the 25th for early access")

    # Check if the date is exactly the 25th
    elif current_date == 25:
        print("Coming soon!")

    # All other dates (26th and beyond)
    else:
        print("Available now!")

    # ✅ Ensure current_date increments to avoid an infinite loop
    current_date += 1
