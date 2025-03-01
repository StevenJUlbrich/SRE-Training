# SRE Week 1–2: Code Examples & Quizzes
# ======================================

"""
This Python file provides illustrative code snippets and mini-project examples for:
1. Data Structures & Algorithms
2. OOP Principles
3. Basic Scripting

In addition, it includes short quiz questions and potential solutions or hints.

Overview:
---------
We cover basic examples demonstrating best practices, practical usage,
and helpful code patterns. Each section ends with a short quiz.

Requiments:
- Python 3.x
- pip install the required libraries if not already installed.
- Open and Read the README.md file for more details.
"""

# 1. Data Structures & Algorithms
# ================================

# Example 1.1: Reverse a Singly Linked List
# -----------------------------------------
# Explanation:
# This snippet uses a simple LinkedList class to create and reverse it.
# Key points:
#   - Node definition
#   - Iterative approach to reversing
#   - Understanding head and pointer manipulations


class ListNode:
    def __init__(self, val: int = 0, next: "ListNode" = None):
        self.val = val
        self.next = next


class LinkedList:
    def __init__(self):
        self.head: ListNode = None

    def append(self, val: int) -> None:
        """Append a new node with the given value to the end of the list."""
        if not self.head:
            self.head = ListNode(val)
        else:
            current = self.head
            while current.next:
                current = current.next
            current.next = ListNode(val)

    def reverse(self) -> None:
        """Reverse the linked list in place."""
        prev = None
        curr = self.head
        while curr:
            next_temp = curr.next
            curr.next = prev
            prev = curr
            curr = next_temp
        self.head = prev

    def to_list(self) -> list:
        """Convert the linked list to a list of values."""
        vals = []
        current = self.head
        while current:
            vals.append(current.val)
            current = current.next
        return vals


def demo_reverse_linked_list():
    ll = LinkedList()
    for i in range(5):
        ll.append(i)
    print("Original LinkedList:", ll.to_list())
    ll.reverse()
    print("Reversed LinkedList:", ll.to_list())


# Example 1.2: Breadth-First Search (BFS) in a Tree
# --------------------------------------------------
# Explanation:
# This example defines a TreeNode with left/right child pointers.
# BFS is implemented using a queue. This approach can be extended to graphs.

from collections import deque


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def bfs_traversal(root: TreeNode) -> list:
    """Perform a breadth-first search traversal on a binary tree."""
    if not root:
        return []
    result = []
    queue = deque([root])
    while queue:
        node = queue.popleft()
        result.append(node.val)
        if node.left:
            queue.append(node.left)
        if node.right:
            queue.append(node.right)
    return result


def demo_bfs_tree():
    # Building a small tree:
    #       1
    #      / \
    #     2   3
    #    / \
    #   4   5
    root = TreeNode(1)
    root.left = TreeNode(2)
    root.right = TreeNode(3)
    root.left.left = TreeNode(4)
    root.left.right = TreeNode(5)

    print("BFS Traversal:", bfs_traversal(root))


# Example 1.3: Two-Sum Problem
# ----------------------------
# Explanation:
# We want to find two numbers in an array that sum to a specific target.
# We solve it using a dictionary (hash map) to achieve O(n) time complexity.


def two_sum(nums: list[int], target: int) -> list[int]:
    """Find two numbers in the list that add up to the target."""
    lookup = {}
    for i, num in enumerate(nums):
        needed = target - num
        if needed in lookup:
            return [lookup[needed], i]
        lookup[num] = i
    return []


def demo_two_sum():
    arr = [2, 7, 11, 15]
    t = 9
    indices = two_sum(arr, t)
    print(f"Indices of elements that sum to {t}:", indices)


# --- Data Structures & Algorithms Quiz Section ---

DSA_QUIZ_QUESTIONS = [
    "1. What is the time complexity of reversing a singly linked list iteratively?",
    "2. Explain the difference between BFS and DFS in terms of their data structures and search order.",
    "3. Describe how a hash map helps solve the two-sum problem in O(n) time.",
    "4. What is the worst-case scenario for quicksort, and why does it happen?",
    "5. Give an example where using a stack data structure makes logical sense in an application.",
]


# 2. Object-Oriented Programming (OOP) Principles
# ================================================

# Example 2.1: Simple OOP-based E-Commerce Model
# ----------------------------------------------
# Explanation:
# We define multiple classes (Product, Order, Customer) showcasing OOP usage.


class Product:
    def __init__(self, product_id: int, name: str, price: float):
        self.product_id = product_id
        self.name = name
        self.price = price


class Order:
    def __init__(self, order_id: str):
        self.order_id = order_id
        self.items: list[tuple[Product, int]] = []

    def add_item(self, product: Product, quantity: int) -> None:
        """Add a product and its quantity to the order."""
        self.items.append((product, quantity))

    def total_cost(self) -> float:
        """Calculate the total cost of the order."""
        total = 0
        for prod, qty in self.items:
            total += prod.price * qty
        return total


class Customer:
    def __init__(self, customer_id: str, name: str):
        self.customer_id = customer_id
        self.name = name
        self.orders: list[Order] = []

    def place_order(self, order: Order) -> None:
        """Place an order for the customer."""
        self.orders.append(order)

    def get_total_spent(self) -> float:
        """Calculate the total amount spent by the customer."""
        return sum(order.total_cost() for order in self.orders)


def demo_e_commerce_oop():
    # Create sample objects
    product_a = Product(101, "Laptop", 1200.0)
    product_b = Product(102, "Mouse", 25.0)

    order_1 = Order("ORDER-0001")
    order_1.add_item(product_a, 1)
    order_1.add_item(product_b, 2)

    customer_1 = Customer("CUST-01", "Alice")
    customer_1.place_order(order_1)

    print("Total cost of order_1:", order_1.total_cost())
    print("Total spent by customer_1:", customer_1.get_total_spent())


# Example 2.2: Logger Singleton
# -----------------------------
# Explanation:
# Demonstrates the Singleton pattern and thread-safety.

import threading


class Logger:
    _instance = None
    _lock = threading.Lock()

    def __init__(self):
        # raise an error if the class is directly instantiated
        if "_created" not in self.__dict__:
            raise RuntimeError("Use get_logger() to create a Logger.")

    @classmethod
    def get_logger(cls):
        with cls._lock:
            if cls._instance is None:
                cls._instance = super(Logger, cls).__new__(cls)
                cls._instance._created = True
        return cls._instance

    def log(self, message: str) -> None:
        """Log a message to the console."""
        print(f"[LOG]: {message}")


def demo_logger_singleton():
    logger1 = Logger.get_logger()
    logger2 = Logger.get_logger()
    print("Are logger1 and logger2 the same instance?", logger1 is logger2)
    logger1.log("This is a singleton logger message.")


# --- OOP Quiz Section ---

OOP_QUIZ_QUESTIONS = [
    "1. Define encapsulation, inheritance, and polymorphism. Provide a one-line example of each.",
    "2. What is the advantage of using the Singleton pattern, and what are its potential drawbacks?",
    "3. Explain the difference between abstract classes and interfaces. When would you choose one over the other?",
    "4. How does the 'open-closed' principle apply to designing extendable classes?",
    "5. Describe a scenario where using composition might be more appropriate than inheritance.",
]


# 3. Basic Scripting
# ===================

# Example 3.1: CLI Tool for Data Parsing (CSV)
# --------------------------------------------
# Explanation:
# This script function processes a CSV file and performs basic filtering.
# This can be adapted for advanced use cases.

import csv
import sys


def filter_csv(
    input_file: str, output_file: str, filter_column: str, filter_value: str
) -> None:
    """Filters rows of a CSV file based on a given column's matching value."""
    with open(input_file, mode="r", newline="", encoding="utf-8") as infile, open(
        output_file, mode="w", newline="", encoding="utf-8"
    ) as outfile:
        reader = csv.DictReader(infile)
        writer = csv.DictWriter(outfile, fieldnames=reader.fieldnames)
        writer.writeheader()
        for row in reader:
            if row[filter_column] == filter_value:
                writer.writerow(row)
    print(
        f"Filtered rows where {filter_column} = {filter_value} have been saved to {output_file}."
    )


# Example 3.2: Log Analysis Script
# --------------------------------
# Explanation:
# This example analyzes a simple log file and prints out the count of each error.

import re


def analyze_logs(log_file: str) -> None:
    """Analyze a log file and print the count of each error."""
    pattern = re.compile(r"ERROR: (.*)")
    error_count = {}

    with open(log_file, "r", encoding="utf-8") as lf:
        for line in lf:
            match = pattern.search(line)
            if match:
                error_msg = match.group(1)
                error_count[error_msg] = error_count.get(error_msg, 0) + 1

    for error_msg, count in error_count.items():
        print(f"{error_msg} occurred {count} times.")


# Example 3.3: Automated Setup Script (Hypothetical)
# --------------------------------------------------
# Explanation:
# This example outlines a function that can install dependencies, set env variables,
# and configure an environment.

import os
import subprocess


def setup_environment() -> None:
    """Set up the environment by installing dependencies and configuring settings."""
    try:
        print("Starting environment setup...")

        # Example: install dependencies
        # In a real scenario, you might read from a requirements.txt or a package list
        subprocess.run(["pip", "install", "requests"], check=True)

        # Example: set an environment variable
        os.environ["MY_APP_MODE"] = "development"
        print("Set MY_APP_MODE=development")

        # Additional tasks: create directories, fetch config files, etc.
        print("Environment setup complete.")
    except subprocess.CalledProcessError as e:
        print(f"An error occurred while installing dependencies: {e}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")


# --- Basic Scripting Quiz Section ---

SCRIPTING_QUIZ_QUESTIONS = [
    "1. Why is error handling important, and what techniques can you use in Python to handle errors gracefully?",
    "2. What are some typical use cases for writing quick Bash/Python scripts in an SRE environment?",
    "3. When working with sensitive credentials in scripts, what security measures should you consider?",
    "4. Demonstrate how you would parse CLI arguments in Python to make a script more user-friendly.",
    "5. Explain the difference between 'scripts' and 'production-quality applications' in terms of best practices.",
]


if __name__ == "__main__":
    # Demonstration calls
    print("\n--- Data Structures & Algorithms Demonstrations ---\n")
    demo_reverse_linked_list()
    demo_bfs_tree()
    demo_two_sum()

    print("\n--- OOP Demonstrations ---\n")
    demo_e_commerce_oop()
    demo_logger_singleton()

    print("\n--- Basic Scripting Demonstrations (Hypothetical) ---\n")
    # filter_csv('input.csv', 'output.csv', 'Status', 'Active')  # Example usage
    # analyze_logs('app.log')
    # setup_environment()

    print("\n--- Quiz Questions ---\n")
    print("Data Structures & Algorithms:")
    for q in DSA_QUIZ_QUESTIONS:
        print("-", q)

    print("\nOOP:")
    for q in OOP_QUIZ_QUESTIONS:
        print("-", q)

    print("\nBasic Scripting:")
    for q in SCRIPTING_QUIZ_QUESTIONS:
        print("-", q)
