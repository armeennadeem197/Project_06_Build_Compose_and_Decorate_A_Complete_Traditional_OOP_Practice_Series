# Assignment 8 – The `super()` Function in Python OOP

## 🧠 Objective

This assignment demonstrates how to use the `super()` function to call a base class constructor from a derived class in Python.

## 🏗️ Description

We have two classes:

1. **Person** – The base class with a constructor to initialize the `name` attribute.
2. **Teacher** – A subclass of `Person` that adds a new `subject` attribute and uses `super()` to call the `Person` constructor.

## 🧾 Code Summary

```python
class Person:
    def __init__(self, name):
        self.name = name
        print(f"Person created: {self.name}")

class Teacher(Person):
    def __init__(self, name, subject):
        super().__init__(name)
        self.subject = subject
        print(f"Teacher created: {self.name}, Subject: {self.subject}")

✅ Example Usage
teacher = Teacher("Arif Rozani", "Python")
teacher = Teacher("Zia Khan", "Javascript")
teacher = Teacher("Hamzah Syed", "NEXT.js")
teacher = Teacher("Ameen Alam", "Typescript")

💡 Output
Person created: Arif Rozani
Teacher created: Arif Rozani, Subject: Python
Person created: Zia Khan
Teacher created: Zia Khan, Subject: Javascript
Person created: Hamzah Syed
Teacher created: Hamzah Syed, Subject: NEXT.js
Person created: Ameen Alam
Teacher created: Ameen Alam, Subject: Typescript

📚 Learning Outcome
Understand inheritance in Python.

Learn how to use super() to avoid code duplication.

Practice initializing base class properties from a subclass.

