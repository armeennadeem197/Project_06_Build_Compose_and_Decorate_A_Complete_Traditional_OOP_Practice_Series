# 🛠️ Python Function Decorators

This example demonstrates how to use **function decorators** in Python.

---

## 🧠 What is a Function Decorator?

A **decorator** is a function that wraps another function to modify or extend its behavior without changing the function's code directly.

In this example, we will create a decorator `log_function_call` that prints a message before a function is executed.

---

## 🎯 Objective

- Create a decorator function `log_function_call` to log the function call.
- Apply the decorator to a function `say_hello()` that prints a greeting.

---

## 📂 Code Summary

```python
# Decorator function
def log_function_call(func):
    def wrapper():
        print("Function is being called")
        return func()
    return wrapper

# Apply the decorator using @ syntax
@log_function_call
def say_hello():
    print("Hello, Armeen!")

# Call the decorated function
say_hello()
```

---

## 🖨️ Output

```
Function is being called
Hello, Hadiqa!
```

---

## 📌 Explanation

- `log_function_call` is a decorator that takes a function `func` as an argument.
- Inside, it defines `wrapper()`, which prints a message before calling the original `func`.
- The `@log_function_call` syntax applies the decorator to `say_hello`.

---

## 📘 Author

Educational Python Decorator Example – Learn the power of decorators! 🚀