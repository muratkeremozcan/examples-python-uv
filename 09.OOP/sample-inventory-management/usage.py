from main import Order, Product

print(Product.add_product("Laptop", "Electronics", 10, 999.0, "Supplier A"))
print(len(Product.inventory), Product.inventory[0].product_id)

order = Order(order_id=1)
print(order.place_order(1, 3, customer_info="John Doe"))

print("Remaining qty:", Product.inventory[0].quantity)  # expect 7
print("Order tuples:", order.products)
