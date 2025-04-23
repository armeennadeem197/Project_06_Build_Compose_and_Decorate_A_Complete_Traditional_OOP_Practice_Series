🏦 Bank Class: Class Variables and Class Methods in Python
This Python script demonstrates how to use class variables and class methods effectively. It simulates a bank system where the name of the bank is shared across all instances and can be changed using a class method.

🔧 Features
Uses a class variable bank_name to store the name of the bank.

Includes a class method change_bank_name() to update the bank name.

Changes to the class variable reflect across all instances of the class.

🧠 Concepts Covered
Class vs. instance variables

The @classmethod decorator

The cls keyword to access and modify class-level data

Dynamic user input handling

💻 Code Example
"""
class Bank:
    bank_name = "National Bank"  # Class variable

    @classmethod
    def change_bank_name(cls, name):
        cls.bank_name = name  # Modify class variable

# Display initial bank name
print(f"Initial bank name: {Bank.bank_name}")

# Get user input to change bank name
new_name = input("Enter the new bank name: ")
Bank.change_bank_name(new_name)

# Display updated bank name
print(f"Updated bank name: {Bank.bank_name}")
"""
✅ Sample Output
Initial bank name: National Bank
Enter the new bank name: Global Bank
Updated bank name: Global Bank

📂 How to Run
Save the code in a Python file (e.g., bank.py).
Run the file in terminal or any IDE:
"""
python main.py
"""
Enter a new bank name when prompted.

📌 Notes
Class variables are shared across all instances of a class.
Changes made through cls will affect every object referencing that variable.
This pattern is useful for shared configurations or default settings.