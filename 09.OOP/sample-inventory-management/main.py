"""
Inventory Management (OOP) — commented version.

- Keeps an in-memory product list on Product.inventory (no DB/persistence).
- Auto-generates product_id via Product._id_counter (resets per process).
- Class methods return *status messages* exactly as required by the spec.
- Order.place_order assumes one product per order and does not alter stock.
"""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import ClassVar, List, Optional, Tuple


@dataclass
class Product:
    # Instance fields (match PRD constructor signature)
    product_id: int
    name: str
    category: str
    quantity: int
    price: float
    supplier: str

    # In-memory storage for all Product instances (shared across the class)
    # Simple auto-incrementing source for unique product_id values (resets on restart)
    inventory: ClassVar[List["Product"]] = []
    _id_counter: ClassVar[int] = 0

    @classmethod
    def add_product(
        cls,
        name: str,
        category: str,
        quantity: int,
        price: float,
        supplier: str,
    ) -> str:
        """Auto-generate product_id, construct Product, store, and return success message."""
        # 1) Generate the next unique id (scoped to this process)
        # 2) Construct a Product using the constructor signature
        # 3) Save it to the in-memory inventory list
        # 4) Return the exact success message expected by callers
        # Note: we return a *message* (not the Product) to match the spec.
        cls._id_counter += 1
        new_product = cls(
            product_id=cls._id_counter,
            name=name,
            category=category,
            quantity=quantity,
            price=price,
            supplier=supplier,
        )
        cls.inventory.append(new_product)
        return "Product added successfully"

    @classmethod
    def update_product(
        cls,
        product_id: int,
        quantity: Optional[int] = None,
        price: Optional[float] = None,
        supplier: Optional[str] = None,
    ) -> str:
        """Update only provided fields of the product with the given product_id."""
        # Locate the product by id
        # Update only fields the caller provided (non-None values)
        # If found, return the success message; otherwise, return "Product not found"
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
    def delete_product(cls, product_id: int) -> str:
        """Remove the product with product_id from inventory if present."""
        # Remove the first matching product from the inventory list (if any)
        # Return the exact message depending on whether we found a match
        for idx, p in enumerate(cls.inventory):
            if p.product_id == product_id:
                cls.inventory.pop(idx)
                return "Product deleted successfully"
        return "Product not found"


@dataclass
class Order:
    order_id: int
    # dataclasses.field(...) lets you configure dataclass attributes (defaults, init/repr/compare behavior, etc.)
    # Each tuple is (product_id, quantity); default to an empty list when not provided
    # default_factory=list creates a NEW empty list for each Order instance
    # Avoids the mutable default pitfall of using [] (which would be shared across instances)
    products: List[Tuple[int, int]] = field(default_factory=list)
    # Optional customer metadata carried with the order
    customer_info: Optional[str] = None

    def place_order(
        self,
        product_id: int,
        quantity: int,
        customer_info: Optional[str] = None,
    ) -> str:
        """Append (product_id, quantity) to this order and return the success message."""
        # If provided, store/overwrite the customer info for this order
        # Per spec, treat orders as single-product; we still record a (id, qty) tuple
        # No inventory/stock validation here (intentionally out of scope)
        # Return the exact message including this order's id
        if customer_info is not None:
            self.customer_info = customer_info
        # Reduce the product's inventory quantity when an order is placed
        for p in Product.inventory:
            if p.product_id == product_id:
                p.quantity -= quantity
                break
        # Each order can only take one product (PRD), but we still store the tuple for traceability
        self.products.append((product_id, quantity))
        return f"Order placed successfully. Order ID: {self.order_id}"
