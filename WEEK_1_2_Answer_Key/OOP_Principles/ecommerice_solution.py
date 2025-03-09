#!/usr/bin/env python3
"""
E-commerce OOP Example - Object-Oriented Programming Principles

This module demonstrates the implementation of a simple e-commerce system
using object-oriented programming (OOP) principles.

Key Concepts:
    - Class structure and relationships
    - Encapsulation of data and behavior
    - Single Responsibility Principle
    - Composition over inheritance
    - Type hinting for improved code readability

Learning Objectives:
    - Understand how to model a domain using OOP
    - Learn to create appropriate class relationships
    - Practice implementing methods with clear responsibilities
    - Recognize proper use of encapsulation
"""

import re
from datetime import datetime
from decimal import Decimal
from typing import Any, Dict, List, Optional


class Product:
    """
    Represents a product in the e-commerce system.

    A product has an ID, name, description, price, and inventory count.
    This class encapsulates all product-specific data and behaviors.
    """

    def __init__(
        self, product_id: int, name: str, price: Decimal, description: str = ""
    ):
        """
        Initialize a new Product.

        Args:
            product_id: Unique identifier for the product
            name: Name of the product
            price: Price of the product as a Decimal
            description: Optional description of the product

        Raises:
            ValueError: If price is negative or name is empty
        """
        if not name:
            raise ValueError("Product name cannot be empty")

        self.product_id = product_id
        self.name = name
        self._price = Decimal("0")  # Initialize with default, will set via property
        self.description = description
        self._inventory_count = 0

        # Use the property setter to ensure validation
        self.price = price

    @property
    def price(self) -> Decimal:
        """Get the product price."""
        return self._price

    @price.setter
    def price(self, new_price: Decimal) -> None:
        """
        Set the product price, ensuring it's not negative.

        Args:
            new_price: New price for the product

        Raises:
            ValueError: If the price is negative
        """
        # Convert to Decimal if it's not already
        if not isinstance(new_price, Decimal):
            new_price = Decimal(str(new_price))

        if new_price < 0:
            raise ValueError("Price cannot be negative")
        self._price = new_price

    @property
    def inventory_count(self) -> int:
        """Get the current inventory count."""
        return self._inventory_count

    def add_inventory(self, quantity: int) -> None:
        """
        Add inventory to the product.

        Args:
            quantity: Amount to add to inventory

        Raises:
            ValueError: If the quantity is negative
        """
        if quantity < 0:
            raise ValueError("Cannot add negative inventory")
        self._inventory_count += quantity

    def remove_inventory(self, quantity: int) -> bool:
        """
        Remove inventory from the product if sufficient quantity is available.

        Args:
            quantity: Amount to remove from inventory

        Returns:
            bool: True if inventory was successfully removed, False if insufficient inventory

        Raises:
            ValueError: If the quantity is negative
        """
        if quantity < 0:
            raise ValueError("Cannot remove negative inventory")

        if quantity > self._inventory_count:
            return False

        self._inventory_count -= quantity
        return True

    def is_in_stock(self) -> bool:
        """
        Check if the product is in stock.

        Returns:
            bool: True if inventory count is greater than 0, False otherwise
        """
        return self._inventory_count > 0

    def __str__(self) -> str:
        """Return a string representation of the product."""
        return f"{self.name} (ID: {self.product_id}, ${float(self._price):.2f})"


class OrderItem:
    """
    Represents an item in an order.

    An order item associates a product with a quantity and calculates the subtotal.
    This demonstrates composition (OrderItem contains a Product) rather than inheritance.
    """

    def __init__(self, product: Product, quantity: int):
        """
        Initialize a new OrderItem.

        Args:
            product: The product being ordered
            quantity: The quantity being ordered

        Raises:
            ValueError: If quantity is less than or equal to 0
        """
        if quantity <= 0:
            raise ValueError("Quantity must be positive")

        self.product = product
        self.quantity = quantity
        self.unit_price = product.price  # Capture the price at time of order

    def subtotal(self) -> Decimal:
        """
        Calculate the subtotal for this order item.

        Returns:
            Decimal: The subtotal (unit price × quantity)
        """
        return self.unit_price * self.quantity

    def __str__(self) -> str:
        """Return a string representation of the order item."""
        return f"{self.quantity} × {self.product.name} @ ${float(self.unit_price):.2f} each"


class Order:
    """
    Represents an order in the e-commerce system.

    An order contains multiple order items and calculates the total cost.
    This class demonstrates the Single Responsibility Principle by focusing only on order management.
    """

    def __init__(self, order_id: str, customer_name: str):
        """
        Initialize a new Order.

        Args:
            order_id: Unique identifier for the order
            customer_name: Name of the customer placing the order
        """
        self.order_id = order_id
        self.customer_name = customer_name
        self.items: List[OrderItem] = []
        self.order_date = datetime.now()
        self.status = "Created"

    def add_item(self, product: Product, quantity: int) -> bool:
        """
        Add a product to the order.

        Args:
            product: The product to add
            quantity: The quantity to order

        Returns:
            bool: True if the item was added successfully, False if insufficient inventory

        Raises:
            ValueError: If quantity is less than or equal to 0
        """
        if quantity <= 0:
            raise ValueError("Quantity must be positive")

        # Check if there's enough inventory and reserve it
        if not product.remove_inventory(quantity):
            return False

        # Add the item to the order
        self.items.append(OrderItem(product, quantity))
        return True

    def total_cost(self) -> Decimal:
        """
        Calculate the total cost of the order.

        Returns:
            Decimal: The total cost (sum of all item subtotals)
        """
        return sum(item.subtotal() for item in self.items)

    def item_count(self) -> int:
        """
        Get the total number of items in the order.

        Returns:
            int: The total number of items
        """
        return sum(item.quantity for item in self.items)

    def complete_order(self) -> None:
        """Mark the order as completed."""
        self.status = "Completed"

    def cancel_order(self) -> None:
        """
        Cancel the order and return items to inventory.

        This method demonstrates how to handle related operations across objects.
        """
        if self.status == "Cancelled":
            return

        # Return items to inventory
        for item in self.items:
            item.product.add_inventory(item.quantity)

        self.status = "Cancelled"

    def __str__(self) -> str:
        """Return a string representation of the order."""
        items_str = "\n".join(f"  - {item}" for item in self.items)
        return (
            f"Order {self.order_id} ({self.status})\n"
            f"Customer: {self.customer_name}\n"
            f"Date: {self.order_date.strftime('%Y-%m-%d %H:%M')}\n"
            f"Items:\n{items_str}\n"
            f"Total: ${float(self.total_cost()):.2f}"
        )


class Customer:
    """
    Represents a customer in the e-commerce system.

    A customer can place multiple orders and retrieve their order history.
    This class demonstrates the principle of maintaining relationships between entities.
    """

    def __init__(self, customer_id: str, name: str, email: str):
        """
        Initialize a new Customer.

        Args:
            customer_id: Unique identifier for the customer
            name: Name of the customer
            email: Email address of the customer

        Raises:
            ValueError: If email format is invalid
        """
        self.customer_id = customer_id
        self.name = name

        # Validate email format
        if not self._is_valid_email(email):
            raise ValueError("Invalid email format")
        self.email = email

        self._orders: List[Order] = []  # Protected attribute

    @staticmethod
    def _is_valid_email(email: str) -> bool:
        """
        Validate email format using a simple regex pattern.

        Args:
            email: Email address to validate

        Returns:
            bool: True if email format is valid, False otherwise
        """
        pattern = r"^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$"
        return re.match(pattern, email) is not None

    def place_order(self, order: Order) -> None:
        """
        Place an order for the customer.

        Args:
            order: The order to place
        """
        self._orders.append(order)

    def get_order_history(self) -> List[Order]:
        """
        Get the customer's order history.

        Returns:
            List[Order]: A list of all orders placed by the customer
        """
        return self._orders.copy()  # Return a copy to prevent direct modification

    def get_total_spent(self) -> Decimal:
        """
        Calculate the total amount spent by the customer.

        Returns:
            Decimal: The sum of all completed order totals
        """
        return sum(
            order.total_cost() for order in self._orders if order.status == "Completed"
        )

    def __str__(self) -> str:
        """Return a string representation of the customer."""
        return f"Customer: {self.name} (ID: {self.customer_id}, Email: {self.email})"


class OrderManager:
    """
    Manages orders and order operations in the e-commerce system.

    This class demonstrates the Single Responsibility Principle by separating
    order management from individual orders and customers.
    """

    def __init__(self):
        """Initialize a new OrderManager with an empty order counter."""
        self._order_counter = 0
        self._orders: Dict[str, Order] = {}

    def create_order(self, customer: Customer) -> Order:
        """
        Create a new order for a customer.

        Args:
            customer: The customer placing the order

        Returns:
            Order: The newly created order
        """
        self._order_counter += 1
        order_id = f"ORD-{self._order_counter:03d}"

        # Create the order
        new_order = Order(order_id, customer.name)
        self._orders[order_id] = new_order

        return new_order

    def complete_order(self, order: Order, customer: Customer) -> None:
        """
        Complete an order and associate it with a customer.

        Args:
            order: The order to complete
            customer: The customer who placed the order
        """
        order.complete_order()
        customer.place_order(order)

    def cancel_order(self, order: Order) -> None:
        """
        Cancel an order.

        Args:
            order: The order to cancel
        """
        order.cancel_order()

    def get_order_by_id(self, order_id: str) -> Optional[Order]:
        """
        Get an order by its ID.

        Args:
            order_id: The ID of the order to retrieve

        Returns:
            Optional[Order]: The order if found, None otherwise
        """
        return self._orders.get(order_id)

    def get_all_orders(self) -> List[Order]:
        """
        Get all orders in the system.

        Returns:
            List[Order]: All orders
        """
        return list(self._orders.values())


def demonstrate_ecommerce_oop():
    """
    Demonstrate the OOP-based e-commerce model with a sample workflow.
    """
    # Create some products
    laptop = Product(101, "Laptop", Decimal("1200.00"), "High-performance laptop")
    mouse = Product(102, "Mouse", Decimal("25.50"), "Wireless mouse")
    headphones = Product(
        103, "Headphones", Decimal("89.99"), "Noise-cancelling headphones"
    )

    # Add inventory
    laptop.add_inventory(5)
    mouse.add_inventory(20)
    headphones.add_inventory(10)

    # Create a customer
    alice = Customer("C001", "Alice Smith", "alice@example.com")

    # Create an order manager
    order_manager = OrderManager()

    # Create an order through the manager
    order_1 = order_manager.create_order(alice)

    # Add items to the order
    order_1.add_item(laptop, 1)
    order_1.add_item(mouse, 2)

    # Complete the order through the manager
    order_manager.complete_order(order_1, alice)

    # Create another order
    order_2 = order_manager.create_order(alice)

    # Add items to the second order
    order_2.add_item(headphones, 1)

    # Complete the second order
    order_manager.complete_order(order_2, alice)

    # Cancel the second order through the manager
    order_manager.cancel_order(order_2)

    # Display results
    print("Product Information:")
    print(f"  {laptop} - In stock: {laptop.inventory_count}")
    print(f"  {mouse} - In stock: {mouse.inventory_count}")
    print(f"  {headphones} - In stock: {headphones.inventory_count}")

    print("\nCustomer Information:")
    print(f"  {alice}")
    print(f"  Total spent: ${float(alice.get_total_spent()):.2f}")

    print("\nOrder Information:")
    print(order_1)
    print("\n" + str(order_2))

    # Explain key OOP concepts used
    print("\nKey OOP Concepts Demonstrated:")
    print(
        "1. Encapsulation: Private attributes with getters/setters (e.g., Product._price)"
    )
    print("2. Composition: Orders contain OrderItems which reference Products")
    print("3. Single Responsibility: Each class has a clear, focused purpose")
    print("4. Interface Design: Methods have clear contracts and error handling")
    print("5. State Management: Order status transitions and inventory tracking")
    print("6. Separation of Concerns: OrderManager handles order operations separately")


if __name__ == "__main__":
    demonstrate_ecommerce_oop()
