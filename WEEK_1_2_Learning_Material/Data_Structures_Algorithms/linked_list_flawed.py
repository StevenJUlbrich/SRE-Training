#!/usr/bin/env python3
"""
Flawed Linked List Implementation - Data Structures & Algorithms

This module contains a flawed implementation of a singly linked list
with various errors and inefficiencies that need to be identified and fixed.

TASK:
    - Review the code and identify the bugs and inefficiencies
    - Fix the implementation to make it work correctly
    - Consider edge cases and performance issues

Common issues to look for:
    - Missing edge case handling
    - Incorrect pointer manipulation
    - Logical errors in operations
    - Memory leaks or inefficient use of resources
    - Incorrect handling of empty lists
"""


class Node:
    """
    A Node in a singly linked list.

    # ISSUE #1 (HINT): There might be an issue with how nodes are initialized
    """

    def __init__(self, value):
        """Initialize a new Node with the given value."""
        self.value = value
        # Node doesn't have a next pointer initialized


class LinkedList:
    """
    A singly linked list implementation with various operations.

    # ISSUE #2 (HINT): There might be issues with tracking the list state
    """

    def __init__(self):
        """Initialize an empty linked list."""
        self.head = None
        # Not tracking the list length, which could be useful

    def append(self, value):
        """
        Add a new node with the given value to the end of the list.

        # ISSUE #3 (HINT): Check the handling of empty lists
        """
        new_node = Node(value)

        # If the list is empty
        if self.head is None:
            self.head = new_node
            return

        # Find the last node
        current = self.head
        while current.next:  # This will cause an AttributeError
            current = current.next

        # Add the new node at the end
        current.next = new_node

    def prepend(self, value):
        """
        Add a new node with the given value to the beginning of the list.

        # ISSUE #4 (HINT): Check for correct pointer manipulation
        """
        new_node = Node(value)

        # Make the new node the head
        self.head = new_node
        # The new head doesn't point to the old head

    def delete(self, value):
        """
        Delete the first node with the given value from the list.

        # ISSUE #5 (HINT): Check edge cases and return values
        """
        # If the list is empty
        if self.head is None:
            print("Cannot delete from an empty list")
            # Should return a value indicating failure

        # If the head node contains the value
        if self.head.value == value:
            self.head = self.head.next
            return

        # Search for the value in the rest of the list
        current = self.head
        while current.next and current.next.value != value:
            current = current.next

        # If the value was found
        if current.next:
            current.next = current.next.next
        else:
            print(f"Value {value} not found in the list")
            # Should return a value indicating failure

    def reverse(self):
        """
        Reverse the linked list in place.

        # ISSUE #6 (HINT): There's a significant flaw in the reversal logic
        """
        # Initialize pointers
        prev = None
        curr = self.head

        # Reverse the list
        while curr:
            next_temp = curr.next
            curr.next = prev
            # Missing step: updating prev and curr for the next iteration
            curr = next_temp

        # Update the head pointer
        # Missing step: not updating self.head

    def print_list(self):
        """
        Print all values in the linked list.

        # ISSUE #7 (HINT): What happens if the list is empty?
        """
        values = []
        current = self.head

        # Collect all values
        while current:
            values.append(str(current.value))
            current = current.next

        # Print the values
        print(" -> ".join(values))
        # No special handling for empty lists


def demonstrate_linked_list():
    """
    Demonstrate operations on the linked list.

    # ISSUE #8 (HINT): Not all operations are properly demonstrated
    """
    # Create a new linked list
    ll = LinkedList()

    # Add some values
    print("Adding values 1, 2, 3")
    ll.append(1)
    ll.append(2)
    ll.append(3)

    # Print the list
    print("Current list:")
    ll.print_list()

    # Prepend a value
    print("\nPrepending value 0")
    ll.prepend(0)
    print("Current list:")
    ll.print_list()

    # Delete a value
    print("\nDeleting value 2")
    ll.delete(2)
    print("Current list:")
    ll.print_list()

    # Reverse the list
    print("\nReversing the list")
    ll.reverse()
    print("Reversed list:")
    ll.print_list()  # This will not print the correct reversed list


if __name__ == "__main__":
    demonstrate_linked_list()
