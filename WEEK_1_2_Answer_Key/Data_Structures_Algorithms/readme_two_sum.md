# Two Sum Algorithm Learning Exercise

The Two Sum problem is a classic algorithmic challenge: given an array of integers and a target sum, find the indices of two numbers in the array that add up to the target.

I've created two Python scripts for teaching the Two Sum algorithm using the same learning-through-contrast approach:

1. `two_sum_flawed.py` - A deliberately flawed implementation with common mistakes
2. `two_sum_solution.py` - A corrected version demonstrating efficient approaches

## About the Two Sum Problem

The Two Sum problem is a classic algorithmic challenge:
> Given an array of integers and a target sum, find the indices of two numbers in the array that add up to the target.

This problem is commonly used in coding interviews and serves as an excellent introduction to algorithmic optimization and hash table usage.

## Teaching Approach

This exercise helps students understand efficient algorithm implementation by identifying common mistakes in the flawed version and comparing them to optimized solutions. The contrast between the inefficient brute force approach and the optimized hash map solution demonstrates important concepts in algorithm design and analysis.

## Key Learning Objectives

1. Understand time and space complexity trade-offs
2. Learn to use hash maps for efficient lookups
3. Practice proper input validation and edge case handling
4. Recognize and fix common algorithmic errors
5. Compare different solution approaches
6. Develop thorough testing strategies

## What Makes This Exercise Effective

1. **Real-world relevance**: Two Sum is a common interview question and practical algorithm
2. **Clear optimization path**: Shows progression from O(n²) to O(n) solutions
3. **Conceptual foundation**: Introduces hash map-based optimization strategy applicable to many problems
4. **Multiple solution approaches**: Presents different techniques with pros and cons
5. **Comprehensive testing**: Demonstrates thorough verification with diverse test cases

## How To Use These Files

### For Instructors

1. Distribute `two_sum_flawed.py` to students
2. Ask them to:
   - Identify logical errors and inefficiencies
   - Fix the implementation to handle all edge cases
   - Optimize for better time complexity
   - Create comprehensive test cases
3. Use `two_sum_solution.py` as a reference when reviewing solutions
4. Discuss algorithm optimization strategies and trade-offs

### For Students (Different Skill Levels)

**Beginner:**

- Fix basic logical errors in the brute force implementation
- Add proper input validation
- Ensure correct handling of edge cases

**Intermediate:**

- Implement the hash map-based solution
- Analyze and compare time and space complexity
- Create comprehensive test cases

**Advanced:**

- Implement and compare all three approaches (brute force, hash map, two-pointer)
- Analyze trade-offs between solutions
- Extend to related problems (e.g., Three Sum, Four Sum)

## Key Issues in the Flawed Implementation

1. **Inefficient algorithm**: Uses nested loops with O(n²) time complexity
2. **Incorrect loop bounds**: Doesn't check all possible pairs
3. **Missing input validation**: Doesn't handle empty lists or invalid inputs
4. **Index confusion**: Mixes 0-indexed and 1-indexed approaches
5. **Self-pairing bug**: May use the same element twice in `two_sum_alternative`
6. **Inconsistent return values**: Returns different types in different cases
7. **Limited test cases**: Doesn't test edge cases or special scenarios
8. **No proper error handling**: Missing exception handling and proper output

This exercise helps students develop skills in algorithm optimization, debugging, and testing - core competencies for software engineers and particularly valuable for technical interviews.
