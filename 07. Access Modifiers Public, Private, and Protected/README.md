# 👨‍💼 Access Modifiers in Python – Public, Protected, and Private

This project demonstrates how to use **access modifiers** in Python using a class called `Employee`.

---

## 📌 Objective

Learn how Python handles:
- **Public** variables
- **Protected** variables
- **Private** variables

---

## 🏗️ Class: `Employee`

### Attributes:
| Modifier     | Syntax          | Description                                 |
|--------------|------------------|---------------------------------------------|
| Public       | `self.name`      | Accessible from anywhere                    |
| Protected    | `self._salary`   | Convention to restrict access to subclasses |
| Private      | `self.__ssn`     | Name-mangled to prevent direct access       |

### Method:
- `display_info()`: Prints all three attributes correctly from within the class.

---

## 💻 Example Code

```python
class Employee:
    def __init__(self, name, salary, ssn):
        self.name = name         # Public
        self._salary = salary    # Protected
        self.__ssn = ssn         # Private

    def display_info(self):
        print(f"Name: {self.name}")
        print(f"Salary: {self._salary}")
        print(f"SSN: {self.__ssn}")

emp = Employee("John Doe", 150000, "123-45-6789")

# Accessing public variable
print(emp.name)

# Accessing protected variable (allowed, but not recommended)
print(emp._salary)

# Accessing private variable directly (causes error)
try:
    print(emp.__ssn)
except AttributeError as e:
    print(f"Error: {e}")

# Proper access through class method
emp.display_info()

🧪 Output
Employee Name: John Doe
Employee Salary: 150000
Error: 'Employee' object has no attribute '__ssn'
Name: John Doe
Salary: 150000
SSN: 123-45-6789

🧠 Explanation
Public: Open to all

Protected: Accessible, but meant for internal or subclass use

Private: Hidden via name mangling (_ClassName__varname) – should be accessed through methods

✅ Usage
Save as main.py
Run the script:
"""
python main.py

"""
