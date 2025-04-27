# 📚 Book Manager in Python

A simple interactive Python program that demonstrates the use of **class methods**, **class variables**, and **object creation**.

This project is designed as part of learning **Object-Oriented Programming (OOP)** in Python — specifically focusing on how to use `@classmethod` and `cls`.

---

## 🔧 Features

- Create books with a name.
- Track the total number of books added.
- Display messages when a new book is added.
- Exit the program gracefully with a summary.

---

## 🧠 Concepts Covered

- `@classmethod` usage
- Class variables (`total_books`)
- Object instantiation inside a class method
- Input handling with a loop

---

## 💡 How It Works

1. The program asks the user to enter book names.
2. Each time a book is added:
   - A new `Book` object is created.
   - The total book count is incremented.
3. When the user types `"exit"`, the program stops and shows the total books created.

---

## 🚀 How to Run

Make sure you have Python installed.

```bash
python main.py


🧪 Sample Output
📖 Welcome to the Book Manager!
Type 'exit' to stop adding books.

Enter book name: Python Basics
📚 Book 'Python Basics' created.
🔢 Total books: 1

Enter book name: OOP in Python
📚 Book 'OOP in Python' created.
🔢 Total books: 2

Enter book name: exit

 Final book count: 2

🚪 Exiting...


✨ Author
Created as part of Python OOP learning by a student practicing concepts hands-on.




