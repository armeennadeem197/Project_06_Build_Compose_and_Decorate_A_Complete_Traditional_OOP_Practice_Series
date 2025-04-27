# 🚗 Car & Engine - Composition in Python

This project demonstrates the concept of **Composition** in Object-Oriented Programming (OOP) using Python.

Composition means one class contains an instance of another class — i.e., **"has-a" relationship**.  
In this example, a `Car` **has an** `Engine`.

---

## ✅ Objective

- Create two classes: `Engine` and `Car`
- Use **composition** by passing an `Engine` object into the `Car` constructor
- Call `Engine`'s methods from inside the `Car` object

---

## 📘 What is Composition?

**Composition** in OOP means:
> Ek class ke andar doosri class ka object use kiya jata hai.

For example:
```python
class Car:
    def __init__(self, engine):
        self.engine = engine  # Car HAS an Engine

🧠 Learning Outcomes

Concept	Description
Composition	One class contains another
Method Calling	Access one class’s method from another
Reusability	Engine class reusable in other vehicles
Clean Structure	Clear separation of concerns

🧪 Code Example
class Engine:
    def start(self):
        return "Engine started!"

    def stop(self):
        return "Engine stopped."

class Car:
    def __init__(self, engine):
        self.engine = engine

    def start_car(self):
        return self.engine.start()

    def stop_car(self):
        return self.engine.stop()

# Usage
my_engine = Engine()
my_car = Car(my_engine)

print(my_car.start_car())  # Engine started!
print(my_car.stop_car())   # Engine stopped.

🔁 Output
Engine started!
Engine stopped.
