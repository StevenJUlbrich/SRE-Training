#!/usr/bin/env python3
"""
Flawed Linked List Implementation - Learning Exercise

This module contains a flawed implementation of a singly linked list
with various common mistakes and inefficiencies.

Learning Task:
    - Identify and fix implementation errors
    - Improve error handling and edge cases
    - Enhance performance of operations
    - Correct logic and structural issues

Common issues demonstrated:
    - Incorrect pointer manipulation
    - Memory leaks and dangling references
    - Inefficient traversal
    - Missing edge case handling
    - Inconsistent state management
"""


class Node:
    # Missing docstring
    def __init__(self, data):
        self.data = data  # Inconsistent naming (data vs value)
        self.next = None


# No class-level docstring
class LinkedList:
    def __init__(self):
        self.head = None
        # Not tracking length - will need to recalculate each time

    # Missing is_empty method - would simplify other methods

    def append(self, data):
        # No docstring explaining the method
        new_node = Node(data)

        if self.head is None:
            self.head = new_node
            return

        # Inefficient traversal - always starts from the beginning
        current = self.head
        while current.next:
            current = current.next

        current.next = new_node

    def prepend(self, data):
        # Missing docstring
        new_node = Node(data)

        # Error: doesn't update the head pointer correctly
        # This will lose the rest of the list!
        self.head = new_node
        # Should be: new_node.next = self.head; self.head = new_node

    def delete(self, data):
        # No docstring or return value

        # Missing check for empty list
        current = self.head

        # Special case: deleting the head node
        if current.data == data:
            # Error: doesn't handle the case when the list becomes empty
            self.head = current.next
            return

        # Error: Incorrect traversal logic that can miss the last node
        while current.next and current.next.data != data:
            current = current.next

        # Error: No check if the value was actually found
        # This will cause an error if current.next is None
        current.next = current.next.next
        # Missing return value to indicate success/failure

    def find(self, data):
        # Missing docstring

        # Doesn't handle empty list
        current = self.head

        # Basic logic is correct, but...
        while current:
            if current.data == data:
                # Error: returns data instead of the node
                return current.data
            current = current.next

        # No explicit return None for when value isn't found

    def insert_after(self, target, new_data):
        # No docstring

        # Error: Not reusing the find method
        # Duplicated traversal logic
        current = self.head

        while current:
            if current.data == target:
                # Found the target node
                new_node = Node(new_data)

                # Error: incorrect order of operations
                # This will skip the next node!
                new_node.next = current.next.next
                current.next = new_node
                return True
            current = current.next

        # Missing return value for failure case

    def print_list(self):
        # No docstring
        current = self.head

        # Error: inefficient string concatenation in a loop
        result = ""
        while current:
            # This creates a new string object each iteration
            result += str(current.data) + " -> "
            current = current.next

        # Error: will always have an extra " -> " at the end
        print(result)

    # Missing to_list method - useful for testing

    def get_length(self):
        # No docstring

        # Error: inefficient O(n) calculation every time
        # Should have tracked length as a property
        count = 0
        current = self.head

        while current:
            count += 1
            current = current.next

        return count

    # Missing method to handle reversing the list
    # Missing method to detect cycles
    # No proper __str__ or __repr__ methods


def demo_linked_list():
    # Create a new linked list
    ll = LinkedList()
    print("Created a new linked list")

    # Error: inconsistent naming (append vs add)
    print("\nAdding values 1, 2, 3, 4, 5")
    for i in range(1, 6):
        ll.append(i)

    print("Linked list contents:")
    ll.print_list()

    # Error: using prepend incorrectly
    # This will disconnect the list!
    print("\nPrepending value 0")
    ll.prepend(0)
    print("Linked list contents:")
    ll.print_list()

    # Error: insert_after has a bug that will cause issues
    print("\nInserting value 2.5 after 2")
    ll.insert_after(2, 2.5)
    print("Linked list contents:")
    ll.print_list()

    # Error: find returns the data, not the node
    print("\nFinding value 3")
    found = ll.find(3)
    print(f"Found: {found}")

    # Error: delete method doesn't return success/failure
    print("\nDeleting value 2.5")
    ll.delete(2.5)
    print("Linked list contents:")
    ll.print_list()

    # Error: no to_list method provided
    # Would have to manually convert

    # Try to delete a value that doesn't exist
    # Error: will cause an error due to lack of checking
    print("\nDeleting value 10 (which doesn't exist)")
    try:
        ll.delete(10)
    except:
        print("Error occurred when trying to delete non-existent value")

    print("Final linked list contents:")
    ll.print_list()


# Error: missing if __name__ == "__main__" guard
demo_linked_list()
