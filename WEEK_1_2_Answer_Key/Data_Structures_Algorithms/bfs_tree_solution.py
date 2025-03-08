#!/usr/bin/env python3
"""
Breadth-First Search (BFS) Tree Traversal - Corrected Implementation

This module demonstrates the proper implementation of BFS traversal on a binary tree,
correcting the issues found in the flawed version.

Key Concepts:
    - Tree data structure representation
    - Queue-based level-order traversal
    - Iterative BFS implementation
    - Proper error handling and edge cases

Learning Objectives:
    - Understand how BFS explores nodes level by level
    - Learn to implement BFS correctly using a queue
    - Recognize common mistakes in BFS implementations
    - Appreciate the importance of using appropriate data structures
"""

from collections import deque  # Proper import for efficient queue operations


class TreeNode:
    """
    A node in a binary tree.

    Each node contains:
    - A value stored in the node
    - References to left and right children (or None if no children)
    """

    def __init__(self, value=0):
        """
        Initialize a new TreeNode with the given value.

        Args:
            value: The data value to be stored in the node (default: 0)
        """
        self.value = value
        self.left = None
        self.right = None

    def __str__(self):
        """Return a string representation of the node's value."""
        return str(self.value)


def breadth_first_search(root):
    """
    Perform a breadth-first search (BFS) traversal on a binary tree.

    BFS visits nodes level by level, from top to bottom, left to right.
    It uses a queue to keep track of nodes to visit next.

    Args:
        root: The root node of the binary tree

    Returns:
        list: A list of node values in level-order (BFS order)

    Time Complexity: O(n) - visits each node exactly once
    Space Complexity: O(w) - where w is the maximum width of the tree
    """
    # Handle empty tree case
    if root is None:
        return []

    # Initialize result list to store node values
    result = []

    # Initialize queue with the root node
    # Using deque for O(1) append and popleft operations
    queue = deque([root])

    # Continue until the queue is empty
    while queue:
        # Dequeue the front node (FIFO behavior)
        current = queue.popleft()

        # Process the node (add its value to result)
        result.append(current.value)

        # Enqueue left child first, then right (correct order for left-to-right BFS)
        if current.left:
            queue.append(current.left)

        if current.right:
            queue.append(current.right)

    return result


def bfs_with_levels(root):
    """
    Perform a BFS traversal that separates nodes by their level in the tree.

    This function organizes nodes into lists based on their depth in the tree.

    Args:
        root: The root node of the binary tree

    Returns:
        list: A list of lists, where each inner list contains the node values at one level

    Time Complexity: O(n) - visits each node exactly once
    Space Complexity: O(w) - where w is the maximum width of the tree
    """
    # Handle empty tree case
    if root is None:
        return []

    # Initialize result list to store levels
    levels = []

    # Initialize queue with the root node
    queue = deque([root])

    # Continue until the queue is empty
    while queue:
        # Get the number of nodes at the current level
        level_size = len(queue)
        current_level = []

        # Process all nodes at the current level
        for _ in range(level_size):
            # Dequeue the front node
            node = queue.popleft()

            # Add the node's value to the current level
            current_level.append(node.value)

            # Enqueue children for the next level
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)

        # Add the current level's nodes to the result
        levels.append(current_level)

    return levels


def create_sample_tree():
    """
    Create a sample binary tree for demonstration.
    
    Returns a tree with the following structure:
            1
           / \
          2   3
         / \   \
        4   5   6
           /
          7
    
    Returns:
        TreeNode: The root node of the sample tree
    """
    # Create the tree nodes
    root = TreeNode(1)
    root.left = TreeNode(2)
    root.right = TreeNode(3)
    root.left.left = TreeNode(4)
    root.left.right = TreeNode(5)
    root.right.right = TreeNode(6)
    root.left.right.left = TreeNode(7)  # Include all nodes from the example

    return root


def print_tree_structure():
    """Print a visual representation of the sample tree structure."""
    print("Sample Tree Structure:")
    print("        1       ")
    print("       / \\     ")
    print("      2   3     ")
    print("     / \\   \\   ")
    print("    4   5   6   ")
    print("       /       ")
    print("      7        ")


def demonstrate_bfs():
    """
    Demonstrate BFS traversal on a sample binary tree.

    This function:
    1. Creates a sample tree
    2. Performs BFS traversal
    3. Shows the results with explanation
    4. Compares to other traversal methods
    """
    # Create a sample tree
    tree = create_sample_tree()

    # Print the tree structure
    print_tree_structure()

    try:
        # Perform BFS traversal
        print("\nBFS Traversal Result:")
        bfs_result = breadth_first_search(tree)
        print(bfs_result)

        # Show BFS traversal with levels
        print("\nBFS Traversal by Level:")
        levels = bfs_with_levels(tree)
        for i, level in enumerate(levels):
            print(f"Level {i}: {level}")

        # Explain how BFS works
        print("\nHow BFS Works:")
        print("1. Start at the root node (1)")
        print(
            "2. Explore all neighbors at the current level before moving to the next level"
        )
        print("3. Use a queue to maintain the correct traversal order")
        print("4. For each node:")
        print("   - Process the node")
        print("   - Add its unvisited neighbors to the queue")

        # Compare with other traversal methods
        print("\nComparison with Other Traversals:")
        print("- BFS explores level-by-level (breadth-first)")
        print("- DFS explores branch-by-branch (depth-first)")
        print("- BFS uses a queue, DFS uses a stack or recursion")
        print("- BFS is useful for finding shortest paths and level-order operations")

    except Exception as e:
        print(f"An error occurred during demonstration: {e}")


if __name__ == "__main__":
    demonstrate_bfs()
