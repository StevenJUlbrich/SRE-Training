#!/usr/bin/env python3
"""
Linked List Example - Data Structures & Algorithms

This module demonstrates the implementation of a singly linked list with various
operations that are commonly performed on linked lists.

Key Concepts:
    - Node structure with value and pointer to next node
    - Traversing a linked list
    - Adding elements (at beginning, end, or specific position)
    - Removing elements
    - Searching for elements
    - Building and manipulating linked lists

Learning Objectives:
    - Understand how linked lists store and link data
    - Learn the mechanics of pointer manipulation
    - Recognize the time complexity of different operations
    - Compare linked list operations to array operations
"""


class Node:
    """
    A Node in a singly linked list.

    Each node contains:
    - A value (data)
    - A reference to the next node (or None if it's the last node)
    """

    def __init__(self, value=None):
        """
        Initialize a new Node with the given value.

        Args:
            value: The data value to be stored in the node
        """
        self.value = value
        self.next = None

    def __str__(self):
        """Return a string representation of the node's value."""
        return str(self.value)


class LinkedList:
    """
    A singly linked list implementation.

    The linked list keeps track of the head node, which is the first node in the list.
    All operations are performed relative to the head.
    """

    def __init__(self):
        """Initialize an empty linked list with no nodes."""
        self.head = None
        self.length = 0

    def is_empty(self):
        """
        Check if the linked list is empty.

        Returns:
            bool: True if the list is empty, False otherwise

        Time Complexity: O(1) - constant time operation
        """
        return self.head is None

    def append(self, value):
        """
        Add a new node with the given value to the end of the list.

        Args:
            value: The value to be stored in the new node

        Time Complexity: O(n) - need to traverse to the end of the list
        """
        new_node = Node(value)

        # If the list is empty, make the new node the head
        if self.is_empty():
            self.head = new_node
        else:
            # Traverse to the end of the list
            current = self.head
            while current.next:
                current = current.next
            # Add the new node at the end
            current.next = new_node

        self.length += 1

    def prepend(self, value):
        """
        Add a new node with the given value to the beginning of the list.

        Args:
            value: The value to be stored in the new node

        Time Complexity: O(1) - constant time operation
        """
        new_node = Node(value)

        # Make the new node point to the current head
        new_node.next = self.head
        # Update the head to be the new node
        self.head = new_node

        self.length += 1

    def delete(self, value):
        """
        Delete the first node with the given value from the list.

        Args:
            value: The value to be removed

        Returns:
            bool: True if a node was deleted, False if the value wasn't found

        Time Complexity: O(n) - may need to traverse the entire list
        """
        # If the list is empty, nothing to delete
        if self.is_empty():
            return False

        # If the head node contains the value to delete
        if self.head.value == value:
            self.head = self.head.next
            self.length -= 1
            return True

        # Search for the value in the rest of the list
        current = self.head
        while current.next and current.next.value != value:
            current = current.next

        # If the value was found
        if current.next:
            current.next = current.next.next
            self.length -= 1
            return True

        # Value not found
        return False

    def find(self, value):
        """
        Find the first node containing the given value.

        Args:
            value: The value to search for

        Returns:
            Node or None: The first node containing the value, or None if not found

        Time Complexity: O(n) - may need to traverse the entire list
        """
        current = self.head

        # Traverse the list looking for the value
        while current and current.value != value:
            current = current.next

        # Return the node if found, otherwise None
        return current

    def insert_after(self, target_value, new_value):
        """
        Insert a new node with new_value after the first node containing target_value.

        Args:
            target_value: The value to search for
            new_value: The value to be inserted

        Returns:
            bool: True if inserted successfully, False if target_value not found

        Time Complexity: O(n) - may need to traverse the entire list
        """
        # Find the node containing the target value
        target_node = self.find(target_value)

        # If target node not found
        if not target_node:
            return False

        # Create a new node with the new value
        new_node = Node(new_value)

        # Insert the new node after the target node
        new_node.next = target_node.next
        target_node.next = new_node

        self.length += 1
        return True

    def print_list(self):
        """
        Print all values in the linked list.

        Time Complexity: O(n) - traverses the entire list
        """
        values = []
        current = self.head

        # Traverse the list and collect values
        while current:
            values.append(str(current.value))
            current = current.next

        # Print the values as a list representation
        print(" -> ".join(values) if values else "Empty list")

    def to_list(self):
        """
        Convert the linked list to a Python list.

        Returns:
            list: A list containing all values in the linked list

        Time Complexity: O(n) - traverses the entire list
        """
        result = []
        current = self.head

        # Traverse the list and collect values
        while current:
            result.append(current.value)
            current = current.next

        return result

    def get_length(self):
        """
        Get the number of nodes in the linked list.

        Returns:
            int: The number of nodes

        Time Complexity: O(1) - constant time since we track the length
        """
        return self.length


def demonstrate_linked_list():
    """
    Demonstrate various operations on a linked list.
    """
    # Create a new linked list
    ll = LinkedList()
    print("Created a new linked list")

    # Append some values
    print("\nAppending values 1, 2, 3, 4, 5")
    for i in range(1, 6):
        ll.append(i)

    # Print the list
    print("Linked list contents:")
    ll.print_list()
    print(f"Length: {ll.get_length()}")

    # Prepend a value
    print("\nPrepending value 0")
    ll.prepend(0)
    print("Linked list contents:")
    ll.print_list()

    # Insert after a value
    print("\nInserting value 2.5 after 2")
    ll.insert_after(2, 2.5)
    print("Linked list contents:")
    ll.print_list()

    # Find a value
    print("\nFinding value 3")
    node = ll.find(3)
    print(f"Found: {node}")

    # Delete a value
    print("\nDeleting value 2.5")
    deleted = ll.delete(2.5)
    print(f"Deleted: {deleted}")
    print("Linked list contents:")
    ll.print_list()

    # Convert to a Python list
    print("\nConverting to a Python list")
    list_representation = ll.to_list()
    print(f"List representation: {list_representation}")

    # Delete head
    print("\nDeleting the head (value 0)")
    ll.delete(0)
    print("Linked list contents:")
    ll.print_list()

    # Try to find a non-existent value
    print("\nFinding value 10 (which doesn't exist)")
    node = ll.find(10)
    print(f"Found: {node}")


if __name__ == "__main__":
    demonstrate_linked_list()
