#!/usr/bin/env python3
"""
Flawed E-commerce OOP Implementation - Object-Oriented Programming Principles

This module contains a flawed implementation of a simple e-commerce system.
There are several violations of OOP principles that need to be identified and fixed.

TASK:
    - Review the code and identify OOP principle violations
    - Fix the implementation to follow proper OOP principles
    - Improve encapsulation, responsibility separation, and class relationships

Common issues to look for:
    - Poor encapsulation
    - Violation of Single Responsibility Principle
    - Improper class relationships
    - Missing validation
    - Inefficient or redundant code
"""

# ISSUE #1 (HINT): Missing proper import for decimal handling
# Should use Decimal for monetary values


class Product:
    """
    Represents a product in the e-commerce system.
    
    # ISSUE #2 (HINT): Lacks proper encapsulation
    """
    
    def __init__(self, product_id, name, price, description=""):
        """Initialize a new Product."""
        self.product_id = product_id
        self.name = name
        self.price = price  # ISSUE: Direct attribute access without validation
        self.description = description
        self.inventory_count = 0  # ISSUE: Public attribute for sensitive data
    
    # ISSUE #3 (HINT): Missing validation methods for price and inventory
    
    def display_info(self):
        """Display product information."""
        print(f"Product ID: {self.product_id}")
        print(f"Name: {self.name}")
        print(f"Price: ${self.price}")
        print(f"Description: {self.description}")
        print(f"In Stock: {self.inventory_count}")
        # ISSUE: This method mixes business logic with presentation


class Order:
    """
    Represents an order in the e-commerce system.
    
    # ISSUE #4 (HINT): This class is doing too much (violates Single Responsibility)
    """
    
    def __init__(self, order_id, customer_name, customer_email):
        """Initialize a new Order."""
        self.order_id = order_id
        self.customer_name = customer_name
        self.customer_email = customer_email  # ISSUE: Order shouldn't store customer details
        self.items = []  # List of tuples (product, quantity)
        self.status = "Created"
    
    def add_item(self, product, quantity):
        """Add a product to the order."""
        # ISSUE #5 (HINT): Missing validation and inventory check
        self.items.append((product, quantity))
        
        # ISSUE: Direct manipulation of product inventory without checks
        product.inventory_count -= quantity
    
    def calculate_total(self):
        """Calculate the total cost of the order."""
        total = 0
        for product, quantity in self.items:
            # ISSUE #6 (HINT): Direct attribute access and float for money
            total += product.price * quantity
        return total
    
    def complete_order(self):
        """Complete the order."""
        self.status = "Completed"
        
        # ISSUE: Sends email directly from Order class (too much responsibility)
        self.send_confirmation_email()
    
    def send_confirmation_email(self):
        """Send a confirmation email to the customer."""
        # ISSUE #7 (HINT): This should be in a separate service class
        print(f"Sending confirmation email to {self.customer_email}...")
        # Email sending logic would go here
    
    def cancel_order(self):
        """Cancel the order."""
        # ISSUE #8 (HINT): Incomplete cancellation logic
        self.status = "Cancelled"
        # Missing: Return items to inventory


class Customer:
    """
    Represents a customer in the e-commerce system.
    
    # ISSUE #9 (HINT): Poor relationship with Order class
    """
    
    def __init__(self, customer_id, name, email):
        """Initialize a new Customer."""
        self.customer_id = customer_id
        self.name = name
        self.email = email
        # ISSUE: No way to track customer orders
    
    # ISSUE #10 (HINT): Missing methods to manage customer orders


def demonstrate_ecommerce():
    """
    Demonstrate the e-commerce system.
    
    # ISSUE #11 (HINT): Demonstration code has issues
    """
    # Create some products
    laptop = Product(101, "Laptop", 1200.0, "High-performance laptop")
    mouse = Product(102, "Mouse", 25.5, "Wireless mouse")
    
    # Add inventory
    laptop.inventory_count = 5  # ISSUE: Direct attribute manipulation
    mouse.inventory_count = 20
    
    # Create a customer
    alice = Customer("C001", "Alice Smith", "alice@example.com")
    
    # Create an order
    # ISSUE: Order is created with redundant customer information
    order = Order("ORD-001", alice.name, alice.email)
    
    # Add items to the order
    order.add_item(laptop, 1)
    order.add_item(mouse, 2)
    
    # ISSUE: No connection between customer and order
    
    # Calculate and display the total
    total = order.calculate_total()
    print(f"Order total: ${total}")
    
    # Complete the order
    order.complete_order()
    
    # Display inventory (which may be incorrect due to lack of validation)
    print(f"Laptop inventory: {laptop.inventory_count}")
    print(f"Mouse inventory: {mouse.inventory_count}")


if __name__ == "__main__":
    demonstrate_ecommerce()
