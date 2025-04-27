# 🏷️ Python Class Decorators

This example demonstrates how to use **class decorators** in Python.

---

## 🧠 What is a Class Decorator?

A **class decorator** is a function that takes a class as an argument and modifies or enhances it—typically by adding new methods or behaviors.

---

## 🎯 Objective

- Create a class decorator `add_greeting` that dynamically adds a `greet()` method to a class.
- Apply this decorator to a `Person` class.

---

## 💻 Code Example

```python
# Class decorator
def add_greeting(cls):
    def greet(self):
        return "Hello from Decorator!"
    
    # Add greet method to the class
    cls.greet = greet
    return cls

# Apply the decorator to the Person class
@add_greeting
class Person:
    def __init__(self, name):
        self.name = name

# Create an object of the class
p = Person("Hadiqa")

# Call the dynamically added method
print(p.greet())
```

🖨️ Output
Hello from Decorator!
```
🔍 Explanation
add_greeting is a decorator function that adds a new method greet() to any class it decorates.

The @add_greeting syntax applies this decorator to the Person class.

When an instance of Person is created, it now has access to the greet() method—even though it wasn't originally defined in the class.
```
📌 Use Case
Decorators are useful for:

Adding features without modifying the original class.

Enhancing behavior in a clean, reusable way.