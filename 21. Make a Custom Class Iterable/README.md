21. Make a Custom Class Iterable
---
Assignment
Create a class Countdown that takes a starting number.

Implement __iter__() and __next__() methods to make the object iterable.

In a for-loop, the object should count down to 0.

---
class Countdown:
    def __init__(self, start):
        self.current = start

    def __iter__(self):
        return self  # Return the iterator object itself

    def __next__(self):
        if self.current < 0:
            raise StopIteration
        else:
            number = self.current
            self.current -= 1
            return number

# Test with a for-loop
for num in Countdown(5):
    print(num)

---
Example:
If start = 5, output will be:

```
5
4
3
2
1
0
```
✅ This makes the custom class fully iterable using for loops!


