class MathUtils:

    @staticmethod
    def add(a, b):
        return a + b

def get_valid_number(prompt):
    while True:
        try:
            return int(input(prompt))
        except ValueError:
            print("❌ Invalid input. Please enter a number.")

# Input with validation
num1 = get_valid_number("Enter first number: ")
num2 = get_valid_number("Enter second number: ")

# Using the static method
result = MathUtils.add(num1, num2)
print(f"The sum is: {result}")
