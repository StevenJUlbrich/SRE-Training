#!/usr/bin/env python3
"""
Breadth-First Search (BFS) Tree Traversal - Data Structures & Algorithms

This module demonstrates BFS traversal on a binary tree using a queue.

Key Concepts:
    - Tree data structure representation
    - Queue-based level-order traversal
    - Iterative BFS implementation

Learning Objectives:
    - Understand how BFS explores nodes level by level
    - Learn to implement BFS using a queue
    - Recognize the time and space complexity of BFS
    - Appreciate the difference between depth-first and breadth-first traversals
"""

from collections import deque


class TreeNode:
    """
    A node in a binary tree.

    Each node contains:
    - A value (val)
    - References to left and right children (or None if no children)
    """

    def __init__(self, val=0, left=None, right=None):
        """
        Initialize a new TreeNode with the given value and children.

        Args:
            val: The data value to be stored in the node (default: 0)
            left: Reference to the left child node (default: None)
            right: Reference to the right child node (default: None)
        """
        self.val = val
        self.left = left
        self.right = right

    def __str__(self):
        """Return a string representation of the node's value."""
        return str(self.val)


def bfs_traversal(root):
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
            (in the worst case, w can be n/2 for a complete binary tree)
    """
    # Handle empty tree
    if not root:
        return []

    # Initialize result list to store node values
    result = []

    # Initialize queue with the root node
    queue = deque([root])

    # Continue until the queue is empty
    while queue:
        # Dequeue the front node
        node = queue.popleft()

        # Process the node (add its value to result)
        result.append(node.val)

        # Enqueue left child if it exists
        if node.left:
            queue.append(node.left)

        # Enqueue right child if it exists
        if node.right:
            queue.append(node.right)

    return result


def bfs_traversal_with_levels(root):
    """
    Perform a BFS traversal that keeps track of the level of each node.

    This variant of BFS organizes the results by tree level.

    Args:
        root: The root node of the binary tree

    Returns:
        list: A list of lists, where each inner list contains the node values at one level

    Time Complexity: O(n) - visits each node exactly once
    Space Complexity: O(w) - where w is the maximum width of the tree
    """
    if not root:
        return []

    result = []
    queue = deque([root])

    while queue:
        # Get the number of nodes at the current level
        level_size = len(queue)
        level_nodes = []

        # Process all nodes at the current level
        for _ in range(level_size):
            node = queue.popleft()
            level_nodes.append(node.val)

            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)

        # Add the current level's nodes to the result
        result.append(level_nodes)

    return result


def build_sample_tree():
    """
    Build a sample binary tree for demonstration.
    
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
    root = TreeNode(1)
    root.left = TreeNode(2)
    root.right = TreeNode(3)
    root.left.left = TreeNode(4)
    root.left.right = TreeNode(5)
    root.right.right = TreeNode(6)
    root.left.right.left = TreeNode(7)

    return root


def demonstrate_bfs():
    """
    Demonstrate BFS traversal on a sample binary tree.
    """
    # Build a sample tree
    tree = build_sample_tree()

    # Print tree structure (simple visualization)
    print("Sample Tree Structure:")
    print("        1       ")
    print("       / \\     ")
    print("      2   3     ")
    print("     / \\   \\   ")
    print("    4   5   6   ")
    print("       /       ")
    print("      7        ")

    # Perform standard BFS traversal
    bfs_result = bfs_traversal(tree)
    print("\nBFS Traversal (flat):")
    print(bfs_result)

    # Perform BFS traversal with level information
    bfs_with_levels = bfs_traversal_with_levels(tree)
    print("\nBFS Traversal (by level):")
    for i, level in enumerate(bfs_with_levels):
        print(f"Level {i}: {level}")

    # Explain how BFS works
    print("\nHow BFS Works:")
    print("1. Start at the root (1)")
    print("2. Visit all nodes at the current level before moving to the next level")
    print("3. Use a queue to keep track of nodes to visit")
    print("   - Nodes are processed in FIFO (First-In-First-Out) order")
    print("4. For each node:")
    print("   - Process the node")
    print("   - Add its children to the queue")

    # Compare to DFS
    print("\nComparing BFS to DFS:")
    print("- BFS explores breadth-wise (level by level)")
    print("- DFS explores depth-wise (following paths to leaves before backtracking)")
    print("- BFS uses a queue, while DFS uses a stack (or recursion)")
    print("- BFS is useful for finding the shortest path, DFS for exploring all paths")


if __name__ == "__main__":
    demonstrate_bfs()
