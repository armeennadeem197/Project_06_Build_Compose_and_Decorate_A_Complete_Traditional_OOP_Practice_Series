📚 Student Class using self in Python
This Python program demonstrates how to use the self keyword within a class to initialize and access object attributes. It defines a Student class that stores a student's name and marks, and includes a method to display the student's information.

🧾 Features
Uses self to refer to instance variables.

Initializes student data via a constructor.

Includes a method to display student details.

Allows input from users to create dynamic student objects.

🧠 Concepts Covered
Object-Oriented Programming (OOP)

The self keyword in Python

Class constructors (__init__)

Creating and using methods

Working with user input

🧑‍💻 Code
class Student:
    def __init__(self, name, marks):
        self.name = name
        self.marks = marks

    def display(self):
        print(f"Name: {self.name}, Marks: {self.marks}")

# Using input to get student details
student = Student(input("Enter your name: "), int(input("Enter your marks: ")))
student.display()
"""
✅ Sample Output
Enter your name: Armeen 
Enter your marks: 95
Name: Armeen, Marks: 95
"""
📂 How to Run
Copy the code into a Python file, e.g., student.py.
Run the file using a Python interpreter:
"""
python student.py
"""
Enter your name and marks when prompted.


📌 Notes
This example is great for beginners to understand how classes work in Python.

You can extend the class to include more attributes like grade, subject, etc.