# Assignment 9 – Abstract Classes and Methods in Python

## 🧠 Objective

This assignment demonstrates how to use the `abc` (Abstract Base Classes) module in Python to define an abstract class and implement it using a subclass.

## 🏗️ Description

We define an abstract class `Shape` that has one abstract method `area()`. Then we create a concrete class `Rectangle` that inherits from `Shape` and implements the `area()` method.

### Key Concepts:
- `ABC` from `abc`: Used to create abstract base classes.
- `@abstractmethod`: A decorator that marks a method as abstract.
- Subclasses must override all abstract methods or they cannot be instantiated.

## 🧾 Code Summary

```python
from abc import ABC, abstractmethod

class Shape(ABC):
    @abstractmethod
    def area(self):
        pass

class Rectangle(Shape):
    def __init__(self, width, height):
        self.width = float(width)
        self.height = float(height)

    def area(self):
        return self.width * self.height

✅ Example Usage
width = input("Enter width: ")
height = input("Enter height: ")
rectangle = Rectangle(width, height)

print(f"Area of rectangle: {rectangle.area()}")
💡 Sample Output
Enter width: 5
Enter height: 4
Area of rectangle: 20.0

📚 Learning Outcome
Understand how abstract base classes work in Python.

Practice enforcing method implementation in child classes using @abstractmethod.

Learn how to model real-world behaviors with abstract classes.