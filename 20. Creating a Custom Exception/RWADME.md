20. Creating a Custom Exception
Assignment
Create a custom exception called InvalidAgeError.

Write a function check_age(age) that raises this exception if age < 18.

Handle the exception using try...except.

```
# Custom Exception
class InvalidAgeError(Exception):
    def __init__(self, message="Age must be 18 or above."):
        self.message = message
        super().__init__(self.message)

# Function to check age
def check_age(age):
    if age < 18:
        raise InvalidAgeError(f"Invalid age: {age}. Must be 18 or older.")
    else:
        print("Access granted!")

# Test the function
try:
    user_age = int(input("Enter your age: "))
    check_age(user_age)
except InvalidAgeError as e:
    print("Caught an exception:", e)

```
Explanation
---
InvalidAgeError: A custom exception class that inherits from Exception.

check_age(age): Raises InvalidAgeError if the age is less than 18.

Handling: The try...except block catches the custom exception and prints a message.

Input: User is asked to enter their age and based on it, access is granted or an exception is raised.
---
✅ This covers custom exception creation, raising exceptions, and handling them properly!