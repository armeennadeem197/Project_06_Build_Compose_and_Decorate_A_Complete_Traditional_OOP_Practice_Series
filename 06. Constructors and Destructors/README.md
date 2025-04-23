# 📝 Logger – Constructors and Destructors in Python

This simple Python script demonstrates how to define and use **constructors (`__init__`)** and **destructors (`__del__`)** in a class using a `Logger` example.

---

## 📌 Objective

- Show how an object logs messages when it's **created** and **destroyed**
- Understand Python's **object lifecycle** through constructors and destructors

---

## 📂 Class: `Logger`

### Constructor: `__init__()`
- Runs **automatically** when an object is created
- Prints `"Logger created: Constructor called."`

### Destructor: `__del__()`
- Runs **when the object is deleted** or when Python garbage collects it
- Prints `"Logger destroyed: Destructor called."`

---

## 💻 Example Code

```python
class Logger:
    def __init__(self):
        print("Logger created: Constructor called.")

    def __del__(self):
        print("Logger destroyed: Destructor called.")

# Creating an object
log = Logger()

# Optional: Delete the object manually
del log


🧪 Sample Output
Logger created: Constructor called.
Logger destroyed: Destructor called.

Note: If you don't manually call del log, the destructor will be called automatically when the program ends.

🔍 Notes
Python's destructor is not always guaranteed to be called immediately (especially in some IDEs or interactive environments).

Best used for logging, file closing, or cleanup actions.

✅ Usage
Save the code as main.py

Open your terminal in the same directory

Run it using:
"""
python main.py

"""