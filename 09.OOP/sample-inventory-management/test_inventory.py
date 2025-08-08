import main
import pytest


@pytest.fixture(autouse=True)
def reset_inventory():
    # ensure clean state for each test
    main.Product.inventory.clear()
    main.Product._id_counter = 0
    yield
    main.Product.inventory.clear()
    main.Product._id_counter = 0


def test_add_product_increments_and_returns_message():
    msg = main.Product.add_product("Laptop", "Electronics", 10, 999.0, "Supplier A")
    assert msg == "Product added successfully"
    assert len(main.Product.inventory) == 1
    p = main.Product.inventory[0]
    assert p.product_id == 1
    assert (p.name, p.quantity, p.price, p.supplier) == (
        "Laptop",
        10,
        999.0,
        "Supplier A",
    )


def test_update_product_updates_only_provided_fields():
    main.Product.add_product("Laptop", "Electronics", 10, 999.0, "A")
    msg = main.Product.update_product(1, quantity=8, price=950.0)
    assert msg == "Product information updated successfully"
    p = main.Product.inventory[0]
    assert (p.quantity, p.price, p.supplier) == (8, 950.0, "A")


def test_delete_product_removes_item():
    main.Product.add_product("A", "Cat", 5, 10.0, "X")
    main.Product.add_product("B", "Cat", 6, 20.0, "Y")
    msg = main.Product.delete_product(1)
    assert msg == "Product deleted successfully"
    assert len(main.Product.inventory) == 1
    assert main.Product.inventory[0].product_id == 2


def test_place_order_reduces_quantity_and_returns_message():
    main.Product.add_product("Laptop", "Electronics", 10, 999.0, "Supplier A")
    order = main.Order(order_id=42)
    msg = order.place_order(1, 3, customer_info="John Doe")
    assert msg == "Order placed successfully. Order ID: 42"
    assert main.Product.inventory[0].quantity == 7
    assert order.products == [(1, 3)]
    assert order.customer_info == "John Doe"
