In this project, you will develop a comprehensive inventory management system for a retail business by applying your knowledge in object-oriented programming (OOP) in Python. Imagine you are working for an e-commerce company called `ShopSmart`, a rapidly growing online retailer that sells a wide range of products, including electronics, clothing, and home goods. As the company expands, efficiently managing inventory becomes crucial to ensure smooth operations and customer satisfaction.

Object-oriented programming (OOP) is a programming paradigm that organizes software design around data or objects rather than functions and logic. OOP allows for modular, reusable, and maintainable code, which is particularly beneficial for complex systems like inventory management systems.

You will define two classes Product and Order, using the implementation requirements detailed below:

Product
Constructor parameter(s): self, product_id, name, category, quantity, price, and supplier.
Class-level variable(s): inventory.
Product class method(s)
add_product()
Parameter(s): cls, name, category, quantity, price, and supplier.
Behavior:
Define the product_id assuming it's auto-generated incrementally, without any duplicate product_id values.
Define a new_product variable that will call the constructor of the Product class.
Return the message "Product added successfully" to know that the product was added successfully.
update_product()
Parameter(s): cls, product_id, quantity, price, and supplier.
quantity, price, and supplier should have default values of None.
Behavior:
Check if the product_id already exists in the inventory.
If product_id exists, check for the given parameters in the method if they have a value and update accordingly the product.
Return either one of these messages: "Product information updated successfully" or "Product not found".
delete_product()
Parameter(s): cls, product_id.
Behavior:
Check in the inventory list if the given product_id was passed as a parameter.
If product_id exists then remove the product from the list.
Return either one of these messages: "Product deleted successfully" or "Product not found".
Order
Constructor parameter(s): self, order_id, products, and customer_info.
customer_info should have a default value of None.
Order method(s)
place_order()
Parameter(s): self, product_id, quantity, and customer_info.
customer_info should have a default value of None.
Behavior:
Append to the products list a tuple containing product_id and quantity.
Assume that each order can only take one product.
Return the message: "Order placed successfully. Order ID: {self.order_id}".

As an example, your code must be able to create products like this:

p1 = Product.add_product("Laptop", "Electronics", 50, 1000, "Supplier A")

Update them like this:

update_p1 = Product.update_product(1, quantity=45, price=950)

Delete them like this:

delete_p1 = Product.delete_product(1)

And, create and place orders like this:

order = Order(order_id=1, products=[])

order_placement = order.place_order(1, 2, customer_info="John Doe")
