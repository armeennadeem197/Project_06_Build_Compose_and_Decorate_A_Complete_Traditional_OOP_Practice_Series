➕ MathUtils Class: Static Methods in Python
This Python script demonstrates the use of a static method with no dependency on class or instance variables. It simulates a simple utility class that performs addition using the @staticmethod decorator.

⚙️ Features
Uses a static method add(a, b) to return the sum of two numbers.

No class-level or instance-level variables used.

Clean and reusable utility function.

🧠 Concepts Covered
Static methods in Python

The @staticmethod decorator

Using a method without self or cls

Taking user input and performing operations

💻 Code Example
"""
class MathUtils:
    @staticmethod
    def add(a, b):
        return a + b

# Get user input
num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))

# Call static method without creating an object
result = MathUtils.add(num1, num2)

# Display the result
print(f"The sum is: {result}")
"""
"""
✅ Sample Output
Enter first number: 5
Enter second number: 7
The sum is: 12
"""
📂 How to Run
Save the code in a file like math_utils.py.
Open a terminal or IDE and run:
"""
python main.py
"""
Enter the numbers when prompted.

📌 Notes
Static methods are best for utility functions that don’t need access to class or instance data.

You can add more utility functions like subtract(), multiply(), or divide() to build a full toolkit.