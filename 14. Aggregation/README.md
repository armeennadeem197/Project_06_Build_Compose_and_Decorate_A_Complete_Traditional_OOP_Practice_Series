# 🧩 Aggregation in Python – Department & Employee Example

This project demonstrates the concept of **Aggregation** in Python using classes `Employee` and `Department`.

---

## 🧠 What is Aggregation?

**Aggregation** is a type of association where one class contains a reference to another class but both can exist independently.

> 🔹 "Has-a" relationship  
> 🔹 Objects are loosely coupled  
> 🔹 Useful in modular system design

---

## 🎯 Objective

Create:

- `Employee` class: Contains employee details like name and ID
- `Department` class: Holds references to multiple Employee objects

---

## ✅ Features

- Employees are created independently of departments
- A department can add multiple employees using aggregation
- You can display all employees of a department

---

## 💻 Example Code

```python
emp1 = Employee("Armeen Nadeem", 101)
emp2 = Employee("Ali", 102)

dept = Department("Software Development")
dept.add_employee(emp1)
dept.add_employee(emp2)

dept.show_employees()
```

---

## 🖨️ Output

```
Department: Software Development
Employee Name: Hadiqa Gohar, ID: 101
Employee Name: Tahira Rajput, ID: 102
```

---

## 🔍 Why Aggregation?

- Reusability: Same `Employee` can belong to different `Department`s
- Loose Coupling: If `Department` is deleted, `Employee` objects still exist
- Real-world Modeling: Just like real organizations

---

## 📂 Project Structure

```
aggregation_example/
├── main.py
└── README.md
```

---

## 📘 Author

Educational Python OOP Example – Made Simple and Clear! 🚀