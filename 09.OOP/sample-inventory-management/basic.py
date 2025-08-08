"""
Inventory Management — minimal version without typing/dataclasses.
- In-memory storage on Product.inventory (ephemeral; resets per process)
- IDs via Product._id_counter
- Methods return status messages matching the main example
"""


class Product:
    # Class-level storage (acts like a tiny in-memory DB)
    inventory = []
    _id_counter = 0

    def __init__(self, product_id, name, category, quantity, price, supplier):
        self.product_id = product_id
        self.name = name
        self.category = category
        self.quantity = quantity
        self.price = price
        self.supplier = supplier

    @classmethod
    def add_product(cls, name, category, quantity, price, supplier):
        """Auto-generate product_id, construct, store, and return status message."""
        cls._id_counter += 1
        new_product = Product(
            cls._id_counter, name, category, quantity, price, supplier
        )
        cls.inventory.append(new_product)
        return "Product added successfully"

    @classmethod
    def update_product(cls, product_id, quantity=None, price=None, supplier=None):
        """Update only provided fields; return status message."""
        for p in cls.inventory:
            if p.product_id == product_id:
                if quantity is not None:
                    p.quantity = quantity
                if price is not None:
                    p.price = price
                if supplier is not None:
                    p.supplier = supplier
                return "Product information updated successfully"
        return "Product not found"

    @classmethod
    def delete_product(cls, product_id):
        """Delete by id; return status message."""
        for i, p in enumerate(cls.inventory):
            if p.product_id == product_id:
                cls.inventory.pop(i)
                return "Product deleted successfully"
        return "Product not found"


class Order:
    def __init__(self, order_id, products=None, customer_info=None):
        # Use None default to avoid sharing one list across all instances
        self.order_id = order_id
        self.products = (
            products if products is not None else []
        )  # list of (product_id, quantity)
        self.customer_info = customer_info

    def place_order(self, product_id, quantity, customer_info=None):
        """Append (product_id, quantity) and return the success message."""
        if customer_info is not None:
            self.customer_info = customer_info
        # Reduce the product's inventory quantity when an order is placed
        for p in Product.inventory:
            if p.product_id == product_id:
                p.quantity -= quantity
                break
        self.products.append((product_id, quantity))
        return f"Order placed successfully. Order ID: {self.order_id}"
