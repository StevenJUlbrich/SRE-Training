#!/usr/bin/env python3
"""
Flawed Breadth-First Search (BFS) Tree Traversal - Learning Exercise

This module contains a flawed implementation of BFS traversal on a binary tree.
The code contains several errors, inefficiencies, and poor practices.

Learning Task:
    - Identify and fix algorithmic errors and inefficiencies
    - Improve code organization and documentation
    - Enhance error handling and edge cases

Common issues demonstrated:
    - Improper queue usage
    - Incorrect traversal logic
    - Inefficient data structures
    - Poor error handling
    - Missing documentation
"""

# Missing proper imports
import time


# Poor class design - missing proper documentation and validation
class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


# Flawed BFS implementation with several issues
def breadth_first_search(tree_root):
    # Missing check for None input

    result = []

    # Using a list as a queue (inefficient for queue operations)
    queue = [tree_root]

    while len(queue) > 0:
        # Incorrect queue removal (using pop instead of pop(0) for FIFO behavior)
        # This turns it into a stack (LIFO), resulting in DFS, not BFS
        current = queue.pop()

        result.append(current.value)

        # Wrong order of adding children (right before left)
        # This will affect the traversal order
        if current.right:
            queue.append(current.right)

        if current.left:
            queue.append(current.left)

    return result


# Inefficient level tracking implementation
def bfs_get_levels(root):
    if root is None:
        return []

    levels = []
    current_level = []

    # Using lists inefficiently
    queue = [root]
    next_level_queue = []

    while queue:
        # Pop from end (incorrect FIFO behavior)
        node = queue.pop()
        current_level.append(node.value)

        # Adds children to a separate queue
        if node.left:
            next_level_queue.append(node.left)
        if node.right:
            next_level_queue.append(node.right)

        # If current level is processed, move to next level
        if not queue:
            levels.append(current_level)
            # Inefficient copying of the entire queue
            queue = next_level_queue.copy()
            next_level_queue = []
            current_level = []

    return levels


# Poor helper function for creating a sample tree
def create_tree():
    # Hardcoded tree creation without flexibility
    root = Node(1)
    root.left = Node(2)
    root.right = Node(3)
    root.left.left = Node(4)
    root.left.right = Node(5)
    root.right.right = Node(6)

    # Inconsistent with documented example tree
    # Missing node 7 under node 5

    return root


# Inefficient and error-prone tree printing function
def print_tree(root):
    # This doesn't actually print a tree structure
    # It just does a recursive traversal
    if root is None:
        return

    print(root.value, end=" ")

    # Not actually printing a tree structure visually
    print_tree(root.left)
    print_tree(root.right)


# Demonstration function with poor organization
def demo():
    print("BFS Tree Traversal Demo")

    # Unnecessary sleeps in a demo function
    time.sleep(1)

    test_tree = create_tree()

    # Incorrect description - this is actually doing a pre-order DFS due to the bug
    print("BFS Traversal Result:")
    print(breadth_first_search(test_tree))

    time.sleep(1)

    # No error handling if function fails
    print("BFS with levels:")
    levels = bfs_get_levels(test_tree)
    print(levels)

    # No comparison to other traversal methods
    # No explanation of how BFS works or its applications

    # Unnecessary computation that doesn't add value
    print("Number of nodes:", len(breadth_first_search(test_tree)))


# No proper main function encapsulation
demo()
