###callable() and __call__()
Assignment
Create a class Multiplier with an __init__() method to set a factor.

Define a __call__() method that multiplies an input by the factor.

Test it with callable() and by calling the object like a function.

```
class Multiplier:
    def __init__(self, factor):
        self.factor = factor

    def __call__(self, value):
        return value * self.factor

# Create an object with a factor
double = Multiplier(2)

# Test with callable()
print(callable(double))  # Output: True

# Call the object like a function
print(double(5))  # Output: 10
print(double(10)) # Output: 20

```
Explanation
__init__() sets the multiplication factor when an object is created.

__call__() allows the object to be called like a function.

callable(double) checks if the double object is callable — returns True.

double(5) means multiply 5 by the factor 2 → gives 10.
