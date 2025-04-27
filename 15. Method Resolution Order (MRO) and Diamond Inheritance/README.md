# 💎 Python Diamond Inheritance & Method Resolution Order (MRO)

This example demonstrates how **diamond inheritance** works in Python, along with **Method Resolution Order (MRO)**.

---

## 🧠 What is Diamond Inheritance?

Diamond inheritance occurs when:

- Class `A` is inherited by `B` and `C`
- Both `B` and `C` are inherited by `D`

```
      A
     / \
    B   C
     \ /
      D
```

---

## 🎯 Objective

- Create classes `A`, `B`, and `C`, all with a `show()` method
- Let class `D` inherit from both `B` and `C`
- Observe which `show()` method gets called when called from class `D`
- Print the MRO (Method Resolution Order)

---

## 📂 Code Summary

```python
class A:
    def show(self):
        print("Show from class A")

class B(A):
    def show(self):
        print("Show from class B")

class C(A):
    def show(self):
        print("Show from class C")

class D(B, C):
    pass

d = D()
d.show()

print("Method Resolution Order:", [cls.__name__ for cls in D.__mro__])
```

---

## 🖨️ Output

```
Show from class B
Method Resolution Order: ['D', 'B', 'C', 'A', 'object']
```

---

## 📌 Explanation

Python follows **C3 Linearization (MRO)**, meaning:

- It starts looking from the leftmost parent (`B`) to the right (`C`), then their parents (`A`)
- The method from the first matching class in the MRO is called

So even though both `B` and `C` override `show()`, the method from `B` is called because `B` appears first in `class D(B, C)`.

---

## 🔍 MRO Order

```python
D.__mro__  # ('D', 'B', 'C', 'A', 'object')
```

---

## 📘 Author

Educational Python OOP Example – Learn MRO the easy way! 🚀