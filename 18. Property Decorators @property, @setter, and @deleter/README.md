📚 18. Property Decorators: @property, @setter, and @deleter

Assignment

Create a class Product with a private attribute _price. Use @property to get the price, @price.setter to update it, and @price.deleter to delete it.

Code Explanation

1. Product Class

Private Attribute: _price is a private attribute (by convention, not enforced).

@property: Allows us to access _price as if it were a public attribute.

@setter: Allows controlled modification of _price.

@deleter: Allows deletion of _price with a custom message.

```
class Product:
    def __init__(self, price):
        self._price = price  # Private attribute by convention

    @property
    def price(self):
        print("Getting price...")
        return self._price

    @price.setter
    def price(self, value):
        if value < 0:
            raise ValueError("Price cannot be negative")
        print("Setting price...")
        self._price = value

    @price.deleter
    def price(self):
        print("Deleting price...")
        del self._price
```
Example Usage
```
# Create Product object
item = Product(250)

# Access the price
print(item.price)  # Output: Getting price... → 250

# Update the price
item.price = 300  # Output: Setting price...
print(item.price)  # Output: Getting price... → 300

# Delete the price
del item.price  # Output: Deleting price...
```

Output
```
Getting price...
250
Setting price...
Getting price...
300
Deleting price...
```
Concepts Covered

@property decorator

@setter decorator

@deleter decorator

Private variables

Encapsulation and controlled access

✅ This assignment shows how encapsulation and controlled access to class attributes is done in Python using @property decorators.