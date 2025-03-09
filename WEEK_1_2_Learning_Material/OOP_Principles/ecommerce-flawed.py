#!/usr/bin/env python3
"""
Flawed E-commerce OOP Implementation - Learning Exercise

This module contains a flawed implementation of a simple e-commerce system
that demonstrates common mistakes in object-oriented programming.

Learning Task:
    - Identify and fix OOP design and implementation issues
    - Improve encapsulation and data protection
    - Fix relationship modeling between classes
    - Address validation and error handling issues
    - Implement proper OOP principles

Common issues demonstrated:
    - Poor encapsulation
    - Improper inheritance vs. composition
    - Missing validation
    - Inconsistent state management
    - Tight coupling between classes
"""

import datetime

# Missing proper imports for Decimal, missing type hints


# Base class that's not really needed - demonstrates inheritance misuse
class BaseItem:
    """Base class for items in the system."""

    def __init__(self, item_id, name):
        self.id = item_id
        self.name = name


# Product inherits from BaseItem unnecessarily
class Product(BaseItem):
    """Represents a product in the e-commerce system."""

    def __init__(self, product_id, name, price, description=""):
        # Call parent constructor
        super().__init__(product_id, name)

        # No validation for price
        self.price = price  # Public attribute with no protection
        self.description = description
        self.inventory = 0  # Public attribute with no protection

    # No property decorator for encapsulation

    def add_inventory(self, quantity):
        # No validation for negative quantity
        self.inventory += quantity

    def remove_inventory(self, quantity):
        # Improper validation - allows inventory to go negative
        self.inventory -= quantity
        return True  # Always returns True even if there's not enough inventory

    # Missing is_in_stock method

    def __str__(self):
        return f"{self.name} (ID: {self.id}, ${self.price})"


# OrderItem - poorly designed with no validation
class OrderItem:
    """Represents an item in an order."""

    def __init__(self, product, quantity):
        # No validation for quantity
        self.product = product
        self.quantity = quantity
        # Doesn't store the unit price at time of order

    def subtotal(self):
        # Uses current product price, not price at time of order
        return self.product.price * self.quantity

    # Missing __str__ method


# Order - has design flaws and logic issues
class Order:
    """Represents an order in the e-commerce system."""

    # Global counter - breaks encapsulation and creates shared state
    order_counter = 0

    def __init__(self, customer):
        # Generate order ID using class variable
        Order.order_counter += 1
        self.order_id = f"ORD-{Order.order_counter}"

        # Direct reference to Customer object creates tight coupling
        self.customer = customer
        self.items = []
        self.order_date = datetime.datetime.now()
        self.status = "Created"

    def add_item(self, product, quantity):
        # No validation for quantity
        # No check if product has enough inventory

        # Directly modifies product inventory without using product's methods
        product.inventory -= quantity

        # Add item to order
        self.items.append(OrderItem(product, quantity))
        return True

    def total_cost(self):
        total = 0
        for item in self.items:
            # Inefficient calculation - should use item.subtotal()
            total += item.product.price * item.quantity
        return total

    # Missing item_count method

    def complete_order(self):
        self.status = "Completed"
        # Directly accesses and modifies customer's orders
        self.customer.orders.append(self)

    def cancel_order(self):
        if self.status == "Cancelled":
            return

        # Return items to inventory by directly modifying the inventory
        for item in self.items:
            item.product.inventory += item.quantity

        self.status = "Cancelled"

        # Removes itself from customer's orders - creates risk of inconsistent state
        if self in self.customer.orders:
            self.customer.orders.remove(self)

    # Missing proper __str__ method with detailed output


# Customer - poor design and encapsulation
class Customer(BaseItem):  # Unnecessary inheritance
    """Represents a customer in the e-commerce system."""

    def __init__(self, customer_id, name, email):
        super().__init__(customer_id, name)

        # No validation for email format
        self.email = email
        self.orders = []  # Public attribute with no protection

    # Missing place_order method - orders are added directly in Order.complete_order

    def get_order_history(self):
        return self.orders

    def get_total_spent(self):
        # Incorrect calculation - doesn't check for completed orders only
        return sum(order.total_cost() for order in self.orders)

    # Missing __str__ method


# Global function to demonstrate the system - has logical flaws
def demonstrate_ecommerce():
    """Demonstrate the OOP-based e-commerce model with a sample workflow."""

    # Create some products with no proper decimal handling
    laptop = Product(101, "Laptop", 1200.00, "High-performance laptop")
    mouse = Product(102, "Mouse", 25.50, "Wireless mouse")
    headphones = Product(103, "Headphones", 89.99, "Noise-cancelling headphones")

    # Add inventory
    laptop.add_inventory(5)
    mouse.add_inventory(20)
    headphones.add_inventory(10)

    # Create a customer
    alice = Customer("C001", "Alice Smith", "alice@example.com")

    # Create an order with logical inconsistency
    # Order should be associated with customer name, not the customer object
    order_1 = Order(alice)

    # Add items to the order with no error checking
    order_1.add_item(laptop, 1)
    order_1.add_item(mouse, 2)

    # Complete the order - this will automatically add the order to customer
    order_1.complete_order()

    # Create another order
    order_2 = Order(alice)

    # Add items to the second order
    order_2.add_item(headphones, 1)

    # Place the second order
    order_2.complete_order()

    # Cancel the second order
    order_2.cancel_order()

    # Display results with minimal formatting and explanation
    print("Products:")
    print(laptop)
    print(mouse)
    print(headphones)

    print("Customer:")
    print(f"{alice.name} (ID: {alice.id})")
    print(f"Total spent: ${alice.get_total_spent()}")

    print("Orders:")
    for order in alice.orders:
        print(
            f"Order {order.order_id} - Status: {order.status} - Total: ${order.total_cost()}"
        )


# No proper main guard
demonstrate_ecommerce()
