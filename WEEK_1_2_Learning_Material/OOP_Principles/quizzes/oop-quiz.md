# Site Reliability Engineering (SRE) Quiz

## E-commerce OOP Example

1. **What is encapsulation and how is it demonstrated in the `Product` class?**
   - a) Encapsulation is the bundling of data with the methods that operate on that data. It is demonstrated by using private attributes and providing public getter and setter methods.
   - b) Encapsulation is the inheritance of properties from a parent class. It is demonstrated by the `Product` class inheriting from a base class.
   - c) Encapsulation is the ability to create multiple instances of a class. It is demonstrated by creating multiple `Product` objects.
   - d) Encapsulation is the ability to define multiple methods with the same name. It is demonstrated by method overloading in the `Product` class.

2. **Which principle is demonstrated by the `OrderItem` class containing a `Product` object?**
   - a) Inheritance
   - b) Polymorphism
   - c) Composition
   - d) Abstraction

3. **What is the purpose of the `Order` class in the e-commerce system?**
   - a) To manage the inventory of products.
   - b) To represent a customer in the system.
   - c) To handle the creation and management of orders, including adding items and calculating the total cost.
   - d) To provide a user interface for the e-commerce system.

4. **How does the `Customer` class maintain the relationship between customers and their orders?**
   - a) By inheriting from the `Order` class.
   - b) By storing a list of `Order` objects as an attribute.
   - c) By using a database to store order information.
   - d) By using a dictionary to map customer IDs to orders.

5. **What is the purpose of the `demonstrate_ecommerce_oop` function?**
   - a) To demonstrate the use of inheritance in the e-commerce system.
   - b) To provide a sample workflow that showcases the key OOP concepts used in the e-commerce model.
   - c) To test the performance of the e-commerce system.
   - d) To handle user input and process orders in the e-commerce system.

## Singleton Logger Example

6. **What is the Singleton design pattern and how is it implemented in the `Logger` class?**
   - a) The Singleton pattern ensures that only one instance of a class exists. It is implemented using a private constructor and a class method to get the instance.
   - b) The Singleton pattern allows multiple instances of a class to exist. It is implemented using a public constructor.
   - c) The Singleton pattern is used to create a new instance of a class for each thread. It is implemented using thread-local storage.
   - d) The Singleton pattern is used to create a new instance of a class for each request. It is implemented using a factory method.

7. **How does the `Logger` class ensure thread safety?**
   - a) By using a global lock for all logging operations.
   - b) By using a lock for the singleton instance creation and a separate lock for logging operations.
   - c) By using a lock for each log level.
   - d) By using no locks and relying on the Global Interpreter Lock (GIL).

8. **What is the purpose of the `LogLevel` enum in the `Logger` class?**
   - a) To define different log levels and ensure type safety.
   - b) To store log messages.
   - c) To manage the log file.
   - d) To handle exceptions in the logging system.

9. **How does the `Logger` class prevent direct instantiation?**
   - a) By raising a `RuntimeError` if the constructor is called directly.
   - b) By making the constructor private.
   - c) By using a factory method to create instances.
   - d) By using a metaclass to control instance creation.

10. **What is demonstrated by the `worker_function` in the `Logger` example?**
    - a) How to create multiple instances of the `Logger` class.
    - b) How to use the singleton logger in a multi-threaded environment.
    - c) How to handle exceptions in the logging system.
    - d) How to log messages to a file.

## General Concepts

11. **What is the Single Responsibility Principle (SRP) and how is it applied in the provided examples?**
    - a) SRP states that a class should have only one reason to change. It is applied by ensuring each class has a clear, focused purpose.
    - b) SRP states that a class should inherit from only one parent class. It is applied by avoiding multiple inheritance.
    - c) SRP states that a class should have multiple responsibilities. It is applied by combining related functionalities into a single class.
    - d) SRP states that a class should be responsible for creating its own instances. It is applied by using factory methods.

12. **What is composition and how is it different from inheritance?**
    - a) Composition is the ability to create a new class by combining multiple classes. It is different from inheritance because it does not use the `extends` keyword.
    - b) Composition is the ability to create a new class by inheriting from multiple classes. It is different from inheritance because it uses the `implements` keyword.
    - c) Composition is the ability to create a new class by including instances of other classes. It is different from inheritance because it does not create a parent-child relationship.
    - d) Composition is the ability to create a new class by overriding methods of a parent class. It is different from inheritance because it uses the `override` keyword.

13. **What is type hinting and how does it improve code readability?**
    - a) Type hinting is the process of adding comments to describe the types of variables. It improves code readability by providing documentation.
    - b) Type hinting is the process of using special syntax to indicate the types of variables and function return values. It improves code readability by making the code self-documenting and reducing the likelihood of type-related errors.
    - c) Type hinting is the process of using runtime checks to enforce type constraints. It improves code readability by catching errors at runtime.
    - d) Type hinting is the process of using a separate file to define the types of variables. It improves code readability by separating type information from the code.

14. **What is the purpose of the `__str__` method in a class?**
    - a) To define how an object should be converted to a string.
    - b) To define how an object should be compared to another object.
    - c) To define how an object should be copied.
    - d) To define how an object should be serialized to JSON.

15. **How does the `Order` class handle the cancellation of an order?**
    - a) By deleting the order from the system.
    - b) By setting the order status to "Cancelled" and returning the items to inventory.
    - c) By notifying the customer of the cancellation.
    - d) By issuing a refund to the customer.

## Answers

1. a
2. c
3. c
4. b
5. b
6. a
7. b
8. a
9. a
10. b
11. a
12. c
13. b
14. a
15. b