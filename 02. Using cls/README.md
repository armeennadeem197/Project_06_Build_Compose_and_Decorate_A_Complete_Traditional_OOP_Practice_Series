🔢 Counter Class Using cls in Python
This project showcases the use of class variables and the cls keyword in Python to keep track of how many objects (instances) of a class have been created.

🚀 Features
Tracks the total number of objects created using a class variable.

Uses a class method to access and display the count.

Demonstrates how to use cls for working with class-level data.

🧠 Concepts Covered
Class variables vs. instance variables

@classmethod decorator

The cls keyword for referring to the class

Object instantiation in Python
"""
📄 Code Example
class Counter:
    count = 0  # Class variable to track number of objects

    def __init__(self):
        Counter.count += 1  # Increment count when a new object is created

    @classmethod
    def display_count(cls):
        print(f"Number of objects created: {cls.count}")

# Create instances of Counter
obj1 = Counter()
obj2 = Counter()
obj3 = Counter()
"""
# Display the total number of objects created
Counter.display_count()  # Output: Number of objects created: 3
✅ Sample Output
javascript
Copy
Edit
Number of objects created: 3
📂 How to Run
Copy the code into a Python file, e.g., counter.py.

Run the script in a terminal or IDE:
"""
bash
python counter.py
"""
You’ll see how many objects were created.

📌 Notes
You can modify the script to track other types of events or object types.

This pattern is useful in logging, object pooling, and performance monitoring.