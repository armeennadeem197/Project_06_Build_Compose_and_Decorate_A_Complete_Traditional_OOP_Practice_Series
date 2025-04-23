🚗 Car Class with Public Variables and Methods in Python
This Python script demonstrates how to define and access public variables and public methods using a simple Car class. Public members can be accessed directly from outside the class.

🧾 Features
Defines a public variable brand.

Defines a public method Start() to simulate starting the car.

Accepts user input to dynamically create car objects.

🧠 Concepts Covered
Public attributes in Python classes

Method definition and access

Object instantiation and interaction

Using self to assign instance variables

💻 Code Example
"""
class Car:
    def __init__(self, brand):
        self.brand = brand  # Public variable

    def Start(self):
        print(f"{self.brand} is starting...")  # Public method

# Creating an object with user input
my_car = Car(input("Enter the car brand: "))
print("Car Brand:", my_car.brand)
my_car.Start()
"""

✅ Sample Output
Enter the car brand: Toyota
Car Brand: Toyota
Toyota is starting...

📂 How to Run
Save the code in a Python file, e.g., car.py.
Run the file in your terminal or IDE:
"""
python main.py
"""
Enter a car brand name when prompted.

📌 Notes
In Python, all variables and methods are public by default unless specified with a leading underscore (_) or double underscore (__).

You can modify this code to add more attributes like model, color, or year.