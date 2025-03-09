# Object-Oriented Programming Principles

This directory contains examples and exercises focused on Object-Oriented Programming (OOP) principles relevant to Site Reliability Engineering (SRE).

## Learning Objectives

By working through these examples and exercises, you will:

1. Understand the core principles of OOP: encapsulation, inheritance, polymorphism, and abstraction
2. Learn to implement design patterns such as Singleton
3. Practice designing systems using OOP principles
4. Recognize common anti-patterns and how to avoid them

## Contents

### Examples (Correctly Implemented)

- `examples/ecommerce_example.py`: An OOP-based e-commerce model demonstrating class relationships
- `examples/singleton_logger_example.py`: Implementation of the Singleton pattern for a thread-safe logger

### Flawed Implementations (For Review)

- `ecommerce_flawed.py`: Contains errors in OOP implementation of the e-commerce model
- `singleton_logger_flawed.py`: Contains flaws in the Singleton pattern implementation

### Quizzes

- `quizzes/oop_quiz.md`: Quiz questions on OOP principles and patterns

## Instructions

1. Start by reviewing the correctly implemented examples to understand the OOP concepts
2. Then, examine the flawed implementations to identify and fix the issues
   - Look for violations of OOP principles
   - Identify incorrect implementations of design patterns
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

- [Python OOP Documentation](https://docs.python.org/3/tutorial/classes.html)
- [Design Patterns: Elements of Reusable Object-Oriented Software](https://en.wikipedia.org/wiki/Design_Patterns) by Gamma, Helm, Johnson, and Vlissides
- [Clean Code](https://www.oreilly.com/library/view/clean-code-a/9780136083238/) by Robert C. Martin

## Ecommerce Flaw Review

### For Students (Different Skill Levels)

**Beginner:**

- Focus on fixing basic encapsulation issues
- Add proper validation for inputs
- Fix obvious bugs in methods like `remove_inventory`

**Intermediate:**

- Address inheritance vs. composition issues
- Improve error handling and validation
- Implement proper state management between objects

**Advanced:**

- Redesign class relationships completely
- Add an `OrderManager` class to separate concerns
- Implement additional design patterns
- Add comprehensive validation and error handling

## Key Issues in the Flawed Implementation

1. **Poor encapsulation**: Public attributes with no protection or validation
2. **Inappropriate inheritance**: `BaseItem` class adds unnecessary complexity
3. **Missing validation**: Many methods don't validate their inputs
4. **Inconsistent state management**: Direct modification of related objects' state
5. **Tight coupling**: Direct references between objects create brittle relationships
6. **Inefficient implementations**: Methods duplicate logic that could be reused
7. **Improper error handling**: Many operations assume success without checking
8. **Logical flaws**: Operations like inventory management have bugs
9. **Missing methods**: Some important operations are not implemented
10. **Global state**: Class-level counter for order IDs creates shared state issues

## Additional Enhancements in the Solution

The corrected implementation includes several improvements:

1. **Added OrderManager**: Demonstrates separation of concerns
2. **Email validation**: Shows proper input validation
3. **Consistent return types**: Methods return appropriate types
4. **Protected attributes**: Uses underscore prefix to indicate protected status
5. **Proper use of properties**: For controlled access to attributes
6. **Comprehensive error handling**: Raises specific exceptions with clear messages
7. **Type hints**: Improves code readability and IDE support
8. **Defensive programming**: Methods check preconditions and handle edge cases

This exercise reinforces fundamental OOP principles while providing practical experience in designing a realistic system with multiple interacting classes.


## For Students (Different Skill Levels) Singleton Logger

**Beginner:**

- Identify the basic Singleton implementation issues
- Fix the inconsistent logger access methods
- Implement proper class methods

**Intermediate:**

- Add thread safety mechanisms
- Implement proper encapsulation
- Add validation for inputs

**Advanced:**

- Implement the double-checked locking pattern
- Add comprehensive error handling
- Create additional features like log rotation or filtering

## Key Issues in the Flawed Implementation Singleton Logger

1. **Improper Singleton implementation**: Instance method instead of class method
2. **Inconsistent access patterns**: Multiple ways to get the logger instance
3. **Thread safety problems**: Missing locks for concurrent access
4. **Direct instantiation**: No prevention mechanism
5. **Poor encapsulation**: Public attributes instead of protected ones
6. **Inconsistent log methods**: Some methods reuse code, others don't
7. **String-based log levels**: Using strings instead of enums
8. **No validation**: Missing input validation
9. **Global variable usage**: Creates confusion about the proper access point
10. **Inefficient log operations**: Not thread-safe for log modifications

## Additional Enhancements in the Solution Singleton Logger

The corrected implementation includes several improvements:

1. **Double-checked locking**: Optimizes performance while maintaining thread safety
2. **Proper enum usage**: Type-safe log levels
3. **Protected attributes**: Uses proper naming convention
4. **Thorough validation**: Validates all inputs
5. **Consistent method design**: All log methods use the same internal approach
6. **Thread-safe operations**: Uses locks for all shared state modifications
7. **Defensive copying**: Returns copies of internal state to prevent modification

This exercise helps students understand not just the mechanics of implementing the Singleton pattern, but also the broader principles of thread safety, encapsulation, and consistent API design.
