inflation_september = 3.2
inflation_august = 3.5


# Check if September inflation is less than August inflation
if inflation_september < inflation_august:
    print("Inflation decreased")
elif inflation_september > inflation_august:
    print("Inflation increased")
else:
    print("Inflation remained stable")

#########

# Define your requirements
min_num_beds = 2
min_sq_foot = 750
max_rent = 1900

# Property details (example values)
num_beds = 3
sq_foot = 800
rent = 1800


# Check the number of beds
if num_beds < min_num_beds:
    print("Insufficient bedrooms")
# Check square feet
elif sq_foot <= min_sq_foot:
    print("Too small")
# Check the rent
elif rent > max_rent:
    print("Too expensive")
else:
    print("This looks promising!")
