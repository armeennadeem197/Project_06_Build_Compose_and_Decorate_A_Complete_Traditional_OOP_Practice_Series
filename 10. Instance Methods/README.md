# Assignment 10 – Instance Methods in Python

## 🧠 Objective

This assignment helps understand how to define and use instance methods in a class. It focuses on creating methods that operate on individual instances of a class.

## 🏗️ Description

We define a class `Dog` with two instance variables:
- `name`: The name of the dog
- `breed`: The breed of the dog

An instance method `bark()` is used to print a friendly message using the dog's name and breed.

## 🧾 Code Summary

```python
class Dog:
    def __init__(self, name, breed):
        self.name = name
        self.breed = breed

    def bark(self):
        print(f"{self.name} says Woof! Woof!")
        print(f"{self.name} is a {self.breed} Breed.")

✅ Example Usage
dog = Dog(input("Enter dog's name: "), input("Enter dog's breed: "))
dog.bark()

💡 Sample Output
Enter dog's name: Rocky
Enter dog's breed: German Shepherd
Rocky says Woof! Woof!
Rocky is a German Shepherd Breed.

📚 Learning Outcome
Learn how to use instance methods to interact with object data.

Understand how constructors (__init__) initialize object state.

Practice using self to refer to the current object’s data.