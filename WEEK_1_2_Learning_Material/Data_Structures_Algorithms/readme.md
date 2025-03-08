# Data Structures & Algorithms

This directory contains examples and exercises focused on fundamental data structures and algorithms concepts relevant to Site Reliability Engineering (SRE).

## Learning Objectives

By working through these examples and exercises, you will:

1. Understand the implementation and use of linked lists, trees, and hash maps
2. Learn common algorithms like BFS and techniques for solving problems efficiently
3. Develop skills in analyzing time and space complexity
4. Practice debugging and optimizing algorithmic solutions

## Contents

### Examples (Correctly Implemented)

- `examples/linked_list_example.py`: Implementation of a singly linked list with basic operations
- `examples/linked_list_reversal_correct.py`: Correct implementation of in-place linked list reversal
- `examples/bfs_tree_example.py`: Breadth-first search traversal of a binary tree
- `examples/two_sum_example.py`: Efficient solution to the two-sum problem

### Flawed Implementations (For Review)

- `linked_list_flawed.py`: Contains common errors in linked list implementation
- `bfs_tree_flawed.py`: Contains errors in breadth-first search implementation
- `two_sum_flawed.py`: Inefficient or incorrect implementation of the two-sum problem

### Quizzes

- `quizzes/dsa_quiz.md`: Quiz questions on data structures and algorithms concepts

## Instructions

1. Start by reviewing the correctly implemented examples to understand the concepts
2. Then, examine the flawed implementations to identify and fix the issues
   - Look for bugs, inefficiencies, and logical errors
   - The flawed implementations contain comments highlighting areas to focus on
3. After fixing the flawed implementations, compare your solutions with the correct implementations
4. Test your understanding by completing the quiz

## Prerequisites

- Basic Python knowledge
- Understanding of fundamental programming concepts

## Setup

Install required dependencies:

```bash
pip install -r requirements.txt
```

## Additional Resources

- [LeetCode](https://leetcode.com/) for additional algorithm practice
- [Python Data Structures Documentation](https://docs.python.org/3/tutorial/datastructures.html)
- [Introduction to Algorithms](https://mitpress.mit.edu/books/introduction-algorithms-third-edition) by Cormen, Leiserson, Rivest, and Stein

## BFS FLAWED NOTES

### For Students (Different Skill Levels)

**Beginner:**

- Identify why the "BFS" implementation is actually performing a DFS
- Fix the basic queue implementation to use proper FIFO operations
- Correct the order of adding children nodes

**Intermediate:**

- Implement the correct data structure (deque from collections)
- Improve the organization and structure of the code
- Add proper error handling and edge cases

**Advanced:**

- Analyze the time and space complexity
- Enhance the implementation with additional features
- Compare and contrast with other traversal algorithms

## Key Issues in the Flawed Implementation

1. **Using the wrong data structure**: Using a list with `pop()` creates a stack (LIFO) instead of a queue (FIFO)
2. **Incorrect traversal order**: Adding right children before left children
3. **Inefficient level tracking**: Using separate queues and copying entire queues
4. **Poor error handling**: Missing checks for edge cases
5. **Incomplete sample tree**: Not matching the documented structure
6. **Misleading documentation**: Calling a DFS implementation "BFS"
7. **Inefficient operations**: Using list operations for queue functionality
8. **Unnecessary delays**: Adding sleep calls in a demo function
9. **Missing proper explanations**: Lack of educational content about the algorithm

This exercise builds on the same principles as the environment setup exercise but applies them to an algorithmic context, helping students develop both theoretical understanding and practical implementation skills.

## LINKED LIST FLAWED NOTES

## For Students (Different Skill Levels)

**Beginner:**

- Identify and fix basic bugs like the broken prepend method
- Implement missing error checks
- Add proper docstrings and comments

**Intermediate:**

- Fix all pointer manipulation errors
- Implement efficient traversal methods
- Add missing functionality

**Advanced:**

- Implement the advanced operations (reverse, cycle detection)
- Analyze and optimize the time and space complexity
- Add additional linked list operations (e.g., merge, sort)

### Key Issues in the Flawed Implementation

1. **Broken prepend method**: Doesn't connect the new node to the existing list
2. **Incorrect pointer manipulation**: Several methods have bugs in how they update pointers
3. **Missing edge case handling**: Many methods don't check for empty lists or other edge cases
4. **Inefficient operations**: Some methods recalculate values that could be tracked
5. **Inconsistent naming**: Uses both 'data' and 'value' for node contents
6. **Poor string handling**: Uses inefficient string concatenation in loops
7. **Lack of proper returns**: Methods don't consistently indicate success/failure
8. **Missing functionality**: Doesn't implement useful operations like reverse or cycle detection
9. **Memory leaks**: Some operations can create dangling references
10. **Poor error handling**: May raise exceptions when trying to access non-existent nodes

This exercise not only teaches linked list implementation but also reinforces general programming best practices like proper documentation, consistent naming, error handling, and efficiency considerations.