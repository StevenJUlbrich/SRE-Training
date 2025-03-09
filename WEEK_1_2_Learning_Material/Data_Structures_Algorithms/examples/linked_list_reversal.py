#!/usr/bin/env python3
"""
Linked List Reversal - Data Structures & Algorithms

This module demonstrates how to reverse a singly linked list using an iterative approach.

Key Concepts:
    - In-place reversal of a linked list
    - Pointer manipulation
    - Time and space complexity analysis

Learning Objectives:
    - Understand the step-by-step process of linked list reversal
    - Learn how to manipulate pointers efficiently
    - Recognize the importance of temporary variables in pointer manipulation
    - Analyze the time and space complexity of the algorithm
"""


class ListNode:
    """
    A node in a singly linked list.

    Each node contains:
    - A value (val)
    - A reference to the next node (or None if it's the last node)
    """

    def __init__(self, val=0, next=None):
        """
        Initialize a new node with the given value and next pointer.

        Args:
            val: The data value to be stored in the node (default: 0)
            next: Reference to the next node (default: None)
        """
        self.val = val
        self.next = next

    def __str__(self):
        """Return a string representation of the node's value."""
        return str(self.val)


class LinkedList:
    """
    A singly linked list implementation with focus on the reversal operation.
    """

    def __init__(self):
        """Initialize an empty linked list with no nodes."""
        self.head = None

    def append(self, val):
        """
        Add a new node with the given value to the end of the list.

        Args:
            val: The value to be stored in the new node

        Time Complexity: O(n) - need to traverse to the end of the list
        """
        if not self.head:
            self.head = ListNode(val)
            return

        current = self.head
        while current.next:
            current = current.next
        current.next = ListNode(val)

    def to_list(self):
        """
        Convert the linked list to a Python list.

        Returns:
            list: A list containing all values in the linked list

        Time Complexity: O(n) - traverses the entire list
        """
        vals = []
        current = self.head
        while current:
            vals.append(current.val)
            current = current.next
        return vals

    def reverse(self):
        """
        Reverse the linked list in place.

        This method reverses the linked list by changing the next pointers of each node.
        The algorithm uses three pointers to keep track of the previous, current, and next nodes.

        Time Complexity: O(n) - traverses the entire list once
        Space Complexity: O(1) - uses constant extra space regardless of list size
        """
        # Initialize three pointers:
        # prev: to keep track of the node before current (starts as None since there's no node before head)
        # curr: to keep track of the current node being processed (starts at head)
        # next_temp: to temporarily store the next node before we change curr.next
        prev = None
        curr = self.head

        # Continue until we've processed all nodes
        while curr:
            # Store next node before we change curr.next
            next_temp = curr.next

            # Reverse the pointer direction: change curr.next to point to prev instead of next
            curr.next = prev

            # Move prev and curr one step forward for the next iteration
            prev = curr
            curr = next_temp

        # After the loop, curr will be None (we've gone past the end of the original list)
        # and prev will be the new head (the original tail)
        self.head = prev


def demonstrate_linked_list_reversal():
    """
    Demonstrate the reversal of a linked list.
    """
    # Create a new linked list
    ll = LinkedList()

    # Add some values
    for i in range(5):  # Values 0-4
        ll.append(i)

    # Print the original list
    print("Original LinkedList:", ll.to_list())

    # Reverse the list
    ll.reverse()

    # Print the reversed list
    print("Reversed LinkedList:", ll.to_list())

    # Reverse the list again to get back the original order
    ll.reverse()
    print("Reversed again (original order):", ll.to_list())


if __name__ == "__main__":
    # Demonstrate the linked list reversal
    demonstrate_linked_list_reversal()

    # Explain visually how the reversal works with a small example
    print("\nVisual explanation of reversal process:")
    print("Consider a linked list: 1 -> 2 -> 3 -> NULL")
    print("\nInitial state:")
    print("prev = NULL, curr = 1, next_temp = ?")

    print("\nIteration 1:")
    print("Store next_temp = 2")
    print("Set curr.next = prev (1 -> NULL)")
    print("Move prev = 1, curr = 2")

    print("\nIteration 2:")
    print("Store next_temp = 3")
    print("Set curr.next = prev (2 -> 1 -> NULL)")
    print("Move prev = 2, curr = 3")

    print("\nIteration 3:")
    print("Store next_temp = NULL")
    print("Set curr.next = prev (3 -> 2 -> 1 -> NULL)")
    print("Move prev = 3, curr = NULL")

    print("\nLoop ends, set head = prev")
    print("Final reversed list: 3 -> 2 -> 1 -> NULL")
