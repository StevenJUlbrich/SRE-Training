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