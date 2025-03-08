#!/usr/bin/env python3
"""
Flawed Two Sum Implementation - Data Structures & Algorithms

This module contains a flawed implementation of the Two Sum problem:
Given an array of integers and a target value, find two numbers in the array
that add up to the target and return their indices.

TASK:
    - Review the code and identify the bugs and inefficiencies
    - Fix the implementation to make it work correctly
    - Consider optimizations and improvements

Common issues to look for:
    - Logic errors
    - Inefficient algorithms
    - Edge case handling
    - Incorrect return values
"""


def two_sum(nums, target):
    """
    Find two numbers in the list that add up to the target.

    # ISSUE #1 (HINT): This implementation has inefficient time complexity
    """
    # Attempt to solve the problem
    for i in range(len(nums)):
        # ISSUE #2 (HINT): This doesn't avoid using the same element twice
        for j in range(len(nums)):
            # Check if we've found a pair that adds up to the target
            if nums[i] + nums[j] == target:
                return [i, j]  # Return the indices

    # ISSUE #3 (HINT): What if no solution is found?
    # Function doesn't handle the case where no solution exists


def two_sum_hash(nums, target):
    """
    Find two numbers in the list that add up to the target using a dictionary.

    # ISSUE #4 (HINT): This implementation has flawed logic
    """
    # Create a dictionary to store values
    seen = {}

    # Iterate through the array
    for i, num in enumerate(nums):
        # ISSUE #5 (HINT): The complement calculation and lookup might be incorrect
        # Calculate the complement needed
        complement = target + num  # This is incorrect

        # Look up the complement in the dictionary
        if complement in seen:
            # ISSUE #6 (HINT): The return order might be incorrect
            return [i, seen[complement]]  # Order of indices is swapped

        # Add the current number to the dictionary
        seen[num] = i

    # If no solution is found
    return None  # ISSUE #7 (HINT): Inconsistent return type


def demonstrate_two_sum():
    """
    Demonstrate the two sum implementations.

    # ISSUE #8 (HINT): The test cases might not cover all scenarios
    """
    # Test cases
    nums = [2, 7, 11, 15]
    target = 9

    # Test the regular approach
    result1 = two_sum(nums, target)
    print(f"Regular approach: {result1}")

    # Test the hash table approach
    result2 = two_sum_hash(nums, target)
    print(f"Hash table approach: {result2}")

    # ISSUE #9 (HINT): No test with an empty array or no solution

    # ISSUE #10 (HINT): No performance comparison between approaches


if __name__ == "__main__":
    demonstrate_two_sum()
