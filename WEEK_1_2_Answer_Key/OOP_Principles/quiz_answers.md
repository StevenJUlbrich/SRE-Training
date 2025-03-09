# Site Reliability Engineering (SRE) Quiz Answers

## E-commerce OOP Example

1. **What is encapsulation and how is it demonstrated in the `Product` class?**
   - **Answer:** a) Encapsulation is the bundling of data with the methods that operate on that data. It is demonstrated by using private attributes and providing public getter and setter methods.

2. **Which principle is demonstrated by the `OrderItem` class containing a `Product` object?**
   - **Answer:** c) Composition

3. **What is the purpose of the `Order` class in the e-commerce system?**
   - **Answer:** c) To handle the creation and management of orders, including adding items and calculating the total cost.

4. **How does the `Customer` class maintain the relationship between customers and their orders?**
   - **Answer:** b) By storing a list of `Order` objects as an attribute.

5. **What is the purpose of the `demonstrate_ecommerce_oop` function?**
   - **Answer:** b) To provide a sample workflow that showcases the key OOP concepts used in the e-commerce model.

## Singleton Logger Example

6. **What is the Singleton design pattern and how is it implemented in the `Logger` class?**
   - **Answer:** a) The Singleton pattern ensures that only one instance of a class exists. It is implemented using a private constructor and a class method to get the instance.

7. **How does the `Logger` class ensure thread safety?**
   - **Answer:** b) By using a lock for the singleton instance creation and a separate lock for logging operations.

8. **What is the purpose of the `LogLevel` enum in the `Logger` class?**
   - **Answer:** a) To define different log levels and ensure type safety.

9. **How does the `Logger` class prevent direct instantiation?**
   - **Answer:** a) By raising a `RuntimeError` if the constructor is called directly.

10. **What is demonstrated by the `worker_function` in the `Logger` example?**
    - **Answer:** b) How to use the singleton logger in a multi-threaded environment.

## General Concepts

11. **What is the Single Responsibility Principle (SRP) and how is it applied in the provided examples?**
    - **Answer:** a) SRP states that a class should have only one reason to change. It is applied by ensuring each class has a clear, focused purpose.

12. **What is composition and how is it different from inheritance?**
    - **Answer:** c) Composition is the ability to create a new class by including instances of other classes. It is different from inheritance because it does not create a parent-child relationship.

13. **What is type hinting and how does it improve code readability?**
    - **Answer:** b) Type hinting is the process of using special syntax to indicate the types of variables and function return values. It improves code readability by making the code self-documenting and reducing the likelihood of type-related errors.

14. **What is the purpose of the `__str__` method in a class?**
    - **Answer:** a) To define how an object should be converted to a string.

15. **How does the `Order` class handle the cancellation of an order?**
    - **Answer:** b) By setting the order status to "Cancelled" and returning the items to inventory.