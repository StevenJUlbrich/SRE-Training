#!/usr/bin/env python3
"""
Two Sum Problem - Efficient Implementation

This module demonstrates efficient solutions to the Two Sum problem:
Given an array of integers and a target sum, find the indices of two
numbers in the array that add up to the target.

Key Concepts:
    - Hash map-based efficient lookup
    - Time and space complexity trade-offs
    - Input validation and edge case handling
    - Algorithm optimization techniques
    - Testing and verification

Learning Objectives:
    - Understand how hash maps can improve time complexity
    - Learn to handle edge cases properly
    - Compare different algorithmic approaches
    - Practice implementing efficient solutions
    - Develop thorough testing strategies
"""


def two_sum_brute_force(nums, target):
    """
    Find indices of two numbers that add up to the target using brute force approach.

    Args:
        nums: List of integers
        target: Integer target sum

    Returns:
        List containing the indices of the two numbers that add up to the target,
        or None if no solution exists

    Time Complexity: O(n²) - nested loops checking all pairs
    Space Complexity: O(1) - constant extra space
    """
    # Validate input
    if not isinstance(nums, list) or len(nums) < 2:
        return None

    # Check all possible pairs
    for i in range(len(nums)):
        for j in range(
            i + 1, len(nums)
        ):  # Start from i+1 to avoid using same element twice
            if nums[i] + nums[j] == target:
                return [i, j]

    # No solution found
    return None


def two_sum_optimized(nums, target):
    """
    Find indices of two numbers that add up to the target using hash map for O(n) time.

    Args:
        nums: List of integers
        target: Integer target sum

    Returns:
        List containing the indices of the two numbers that add up to the target,
        or None if no solution exists

    Time Complexity: O(n) - single pass through the array
    Space Complexity: O(n) - storing values in hash map
    """
    # Validate input
    if not isinstance(nums, list) or len(nums) < 2:
        return None

    # Use a hash map to store values and their indices
    num_map = {}

    # Single pass through the array
    for i, num in enumerate(nums):
        # Calculate the complement needed to reach the target
        complement = target - num

        # Check if the complement is already in our map
        if complement in num_map:
            # Found a solution
            return [num_map[complement], i]

        # Store the current number and its index
        num_map[num] = i

    # No solution found
    return None


def two_sum_sorted(nums, target):
    """
    Find indices of two numbers that add up to the target using a two-pointer approach.

    Note: This method requires the input array to be sorted, and returns the indices
    in the sorted array, not the original array.

    Args:
        nums: Sorted list of integers
        target: Integer target sum

    Returns:
        List containing the indices of the two numbers that add up to the target,
        or None if no solution exists

    Time Complexity: O(n) - single pass with two pointers
    Space Complexity: O(1) - constant extra space
    """
    # Validate input
    if not isinstance(nums, list) or len(nums) < 2:
        return None

    # Use two pointers: one from start, one from end
    left, right = 0, len(nums) - 1

    while left < right:
        current_sum = nums[left] + nums[right]

        if current_sum == target:
            # Found a solution
            return [left, right]
        elif current_sum < target:
            # Need a larger sum, move left pointer right
            left += 1
        else:
            # Need a smaller sum, move right pointer left
            right -= 1

    # No solution found
    return None


def test_two_sum():
    """
    Test the Two Sum implementations with various test cases.

    Includes normal cases, edge cases, and special scenarios to
    thoroughly validate the implementations.
    """
    test_cases = [
        # Basic test cases
        {"nums": [2, 7, 11, 15], "target": 9, "expected": [0, 1]},
        {"nums": [3, 2, 4], "target": 6, "expected": [1, 2]},
        {"nums": [3, 3], "target": 6, "expected": [0, 1]},
        # Edge cases
        {"nums": [], "target": 5, "expected": None},
        {"nums": [1], "target": 5, "expected": None},
        {"nums": [1, 2, 3, 4], "target": 10, "expected": None},
        # Special cases
        {"nums": [-1, -2, -3, -4], "target": -7, "expected": [2, 3]},
        {"nums": [0, 0], "target": 0, "expected": [0, 1]},
        {"nums": [5, 0, 5], "target": 10, "expected": [0, 2]},
    ]

    implementations = [
        ("Brute Force", two_sum_brute_force),
        ("Optimized", two_sum_optimized),
    ]

    # Test each implementation against all test cases
    for name, implementation in implementations:
        print(f"\nTesting {name} implementation:")

        for tc in test_cases:
            nums = tc["nums"]
            target = tc["target"]
            expected = tc["expected"]

            try:
                result = implementation(nums, target)

                # Check if the result matches expected
                # Note: For some test cases, there might be multiple valid answers
                if result == expected:
                    print(f"  PASS: {nums}, target={target}, result={result}")
                elif result is not None and expected is not None:
                    # Verify that the result is valid (sums to target)
                    if (
                        len(nums) > 1
                        and 0 <= result[0] < len(nums)
                        and 0 <= result[1] < len(nums)
                    ):
                        if (
                            nums[result[0]] + nums[result[1]] == target
                            and result[0] != result[1]
                        ):
                            print(
                                f"  PASS (alternate solution): {nums}, target={target}, result={result}, expected={expected}"
                            )
                            continue

                    print(
                        f"  FAIL: {nums}, target={target}, result={result}, expected={expected}"
                    )
                else:
                    print(
                        f"  FAIL: {nums}, target={target}, result={result}, expected={expected}"
                    )
            except Exception as e:
                print(f"  ERROR: {nums}, target={target}, exception: {e}")


def demonstrate_two_sum():
    """
    Demonstrate the Two Sum problem and its solutions.

    This function explains the problem, shows different approaches,
    and compares their time and space complexity.
    """
    print("Two Sum Problem Demonstration")
    print("=============================")
    print("Problem: Given an array of integers and a target sum, find the")
    print("indices of two numbers that add up to the target sum.")

    print("\nExample:")
    nums = [2, 7, 11, 15]
    target = 9
    print(f"  Input: nums = {nums}, target = {target}")
    print(f"  Output: {two_sum_optimized(nums, target)}")
    print("  Explanation: nums[0] + nums[1] = 2 + 7 = 9, so we return [0, 1]")

    print("\nApproaches:")
    print("1. Brute Force: Check all pairs of numbers (O(n²) time, O(1) space)")
    print("2. Hash Map: Use a hash map for O(n) lookup (O(n) time, O(n) space)")
    print("3. Two Pointers: For sorted arrays only (O(n) time, O(1) space)")

    print("\nRunning Comprehensive Tests...")
    test_two_sum()


if __name__ == "__main__":
    demonstrate_two_sum()
