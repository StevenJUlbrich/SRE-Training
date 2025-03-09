#!/usr/bin/env python3
"""
Flawed Two Sum Implementation - Algorithms Practice

This module contains a flawed implementation of the Two Sum problem.
The task is to find indices of two numbers that add up to a target sum.

Learning Task:
    - Identify algorithmic inefficiencies
    - Spot logical errors and edge cases
    - Improve time and space complexity
    - Fix bugs in implementation

Common issues demonstrated:
    - Inefficient brute force approach
    - Incorrect handling of edge cases
    - Off-by-one errors
    - Improper return values
    - Missing validation
"""


# Inefficient brute force implementation
def two_sum(nums, target):
    # No input validation for empty lists or non-numeric values

    # Incorrect loop bounds - doesn't check all combinations
    for i in range(len(nums) - 1):
        # Only checks adjacent elements, missing many valid pairs
        j = i + 1

        # Checks only one pair per outer loop iteration
        if nums[i] + nums[j] == target:
            # Found a pair that sums to target
            # Return the indices incorrectly (0-indexed vs 1-indexed confusion)
            return [i + 1, j + 1]

    # No return value if no solution is found
    # Should return None or empty list or raise an exception


# Alternative inefficient implementation
def two_sum_alternative(nums, target):
    # Incorrect handling for empty list
    if len(nums) == 0:
        # Should return None or empty list or raise an exception
        return "Error: Empty list provided"

    # Inefficient nested loops (O(n²) time complexity)
    for i in range(len(nums)):
        # Bug: includes comparing an element with itself
        for j in range(len(nums)):
            # Should skip when i == j to avoid using the same element twice

            # Check if pair sums to target
            if nums[i] + nums[j] == target:
                # Incorrect validation before returning
                # Doesn't check if i and j are the same index
                return [i, j]

    # Correct handling for no solution, but inconsistent return type
    return "No solution found"


# Function to test the implementation
def test_two_sum():
    # Limited test cases, missing edge cases
    test_cases = [
        {"nums": [2, 7, 11, 15], "target": 9, "expected": [0, 1]},
        # Missing test cases for:
        # - Empty list
        # - No solution
        # - Multiple possible solutions
        # - Negative numbers
        # - Duplicate numbers
    ]

    for tc in test_cases:
        nums = tc["nums"]
        target = tc["target"]
        expected = tc["expected"]

        # Test the main implementation
        result = two_sum(nums, target)

        # Incorrect comparison - doesn't consider order of indices
        # Also doesn't handle case when two_sum returns None
        if result == expected:
            print(f"PASS: two_sum({nums}, {target}) = {result}")
        else:
            print(f"FAIL: two_sum({nums}, {target}) = {result}, expected {expected}")


# Call the test function without proper main guard
test_two_sum()
