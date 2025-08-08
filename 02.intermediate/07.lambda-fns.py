sale_price = 29.99

# Define the add_tax lambda function to multiply the argument provided to it, x, by 1.2.


def add_tax(x):
    return x * 1.2


# Call the lambda function
print(add_tax(sale_price))

# Call a lambda function adding 20% to sale_price
print((lambda x: x * 1.2)(sale_price))


###############
sales_prices = [29.99, 9.95, 14.50, 39.75, 60.00]

# Create add_taxes, which multiplies each value in sales_prices by 20%
add_taxes = map(lambda x: x * 1.2, sales_prices)

# print a list using add_taxes to update values in sales_prices
print(list(add_taxes))
