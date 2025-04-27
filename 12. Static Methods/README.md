# 🌡️ Temperature Converter (Celsius to Fahrenheit)

This is a simple Python program that demonstrates the use of a **static method** to convert Celsius to Fahrenheit. It runs interactively in the terminal and handles invalid input gracefully.

---

## ✅ Features

- Converts Celsius to Fahrenheit using a static method
- No need to create class instances
- Accepts user input in a loop
- Handles invalid input with error messages
- Exits cleanly when the user types `"exit"`

---

## 🧠 What You Learn

| Concept             | Explanation |
|---------------------|-------------|
| `@staticmethod`     | Used to define utility methods not dependent on class or instance |
| `float(input())`    | Converts user input into a number |
| `try...except`      | Handles invalid inputs gracefully |
| Conversion Formula  | Fahrenheit = `(Celsius * 9/5) + 32` |

---

## 🔧 How to Run

Make sure you have Python installed. Then run the script from the terminal:

```bash
python main.py

🧪 Example Output
Enter temperature in Celsius (or 'exit' to quit): 0
0.0°C is equal to 32.00°F

Enter temperature in Celsius (or 'exit' to quit): 100
100.0°C is equal to 212.00°F

Enter temperature in Celsius (or 'exit' to quit): hello
⚠️ Please enter a valid number!

Enter temperature in Celsius (or 'exit' to quit): exit
❄️ Goodbye!


