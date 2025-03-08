#!/usr/bin/env python3
"""
Flawed Breadth-First Search (BFS) Implementation - Data Structures & Algorithms

This module contains a flawed implementation of BFS traversal on a binary tree.
There are several errors and inefficiencies that need to be identified and fixed.

TASK:
    - Review the code and identify the bugs and inefficiencies
    - Fix the implementation to make it work correctly
    - Consider edge cases and improvements

Common issues to look for:
    - Incorrect data structure usage
    - Missing edge case handling
    - Logic errors in the traversal algorithm
    - Inefficient implementation
"""

# ISSUE #1 (HINT): The import might be incorrect or missing
# We need a data structure to implement BFS properly
import queue  # This is not the best choice for BFS


class TreeNode:
    """
    A node in a binary tree.
    """

    def __init__(self, val=0, left=None, right=None):
        """Initialize a new TreeNode with the given value and children."""
        self.val = val
        self.left = left
        self.right = right


def bfs_traversal(root):
    """
    Perform a breadth-first search traversal on a binary tree.

    # ISSUE #2 (HINT): The edge case handling might be incorrect or missing
    """
    # Try to handle empty tree - but this is not sufficient
    if root is None:
        return

    result = []

    # ISSUE #3 (HINT): Using the wrong data structure for BFS
    # A queue should be used for BFS, but this implementation uses a regular queue module
    q = queue.Queue()
    q.put(root)

    # ISSUE #4 (HINT): The traversal logic might have problems
    while not q.empty():
        # Get the front node
        node = q.get()

        # Add its value to result
        result.append(node.val)

        # ISSUE #5 (HINT): The order of adding children might be incorrect
        # In BFS, we typically process left child first then right child
        if node.right:  # Adding right child first
            q.put(node.right)

        if node.left:  # Adding left child second
            q.put(node.left)

    # ISSUE #6 (HINT): What if we want to return the result?
    # The function doesn't return anything
    print("BFS Traversal:", result)


def build_sample_tree():
    """
    Build a sample binary tree for demonstration.

    Returns:
        TreeNode: The root node of the sample tree
    """
    # ISSUE #7 (HINT): The tree construction might be incorrect
    # This creates a tree, but not in the expected way
    root = TreeNode(1)
    root.left = TreeNode(2)
    root.right = TreeNode(3)
    root.left.left = TreeNode(4)
    root.left.right = TreeNode(5)
    # Missing additional nodes compared to the example

    return root


def demonstrate_bfs():
    """
    Demonstrate BFS traversal on a sample binary tree.

    # ISSUE #8 (HINT): The demonstration might not handle all cases or might be incomplete
    """
    # Build a sample tree
    tree = build_sample_tree()

    # Perform BFS traversal
    bfs_traversal(tree)

    # ISSUE #9 (HINT): What about testing with an empty tree?
    # No test with an empty tree

    # ISSUE #10 (HINT): What about testing with a single node tree?
    # No test with a single node tree


if __name__ == "__main__":
    demonstrate_bfs()
