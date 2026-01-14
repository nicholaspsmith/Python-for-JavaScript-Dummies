"""
Exercise 1: Classes Basics
===========================

Python classes are similar to JavaScript ES6 classes with some differences.

JavaScript:
    class Person {
        constructor(name, age) {
            this.name = name;
            this.age = age;
        }
        greet() {
            return `Hello, I'm ${this.name}`;
        }
    }

Python:
    class Person:
        def __init__(self, name, age):
            self.name = name
            self.age = age

        def greet(self):
            return f"Hello, I'm {self.name}"

Key differences:
- __init__ instead of constructor
- 'self' is explicit first parameter (like 'this' but explicit)
- No 'new' keyword: person = Person("Alice", 30)
- Class body is indented, no braces
- Methods must include 'self' as first parameter

EXERCISES:
Complete each exercise below. Run with: python3 01_classes_basics.py
"""


# Exercise 1.1: Basic class definition

class Dog:
    """
    A simple Dog class.

    Attributes:
        name: The dog's name
        breed: The dog's breed
        age: The dog's age in years
    """

    def __init__(self, name, breed, age=1):
        """Initialize a new Dog instance."""
        # Set instance attributes
        # YOUR CODE HERE
        pass

    def bark(self):
        """Return a bark string: "{name} says Woof!" """
        # YOUR CODE HERE
        pass

    def describe(self):
        """Return "{name} is a {age} year old {breed}" """
        # YOUR CODE HERE
        pass


# Exercise 1.2: Class with validation

class BankAccount:
    """
    A bank account with balance validation.

    The balance should never go negative.
    """

    def __init__(self, owner, initial_balance=0):
        """Initialize account. Raise ValueError if initial_balance < 0."""
        # YOUR CODE HERE
        pass

    def deposit(self, amount):
        """
        Deposit amount into account.
        Raise ValueError if amount <= 0.
        Return new balance.
        """
        # YOUR CODE HERE
        pass

    def withdraw(self, amount):
        """
        Withdraw amount from account.
        Raise ValueError if amount <= 0 or if it would make balance negative.
        Return new balance.
        """
        # YOUR CODE HERE
        pass

    def get_balance(self):
        """Return current balance."""
        # YOUR CODE HERE
        pass


# Exercise 1.3: Class attributes vs instance attributes

class Counter:
    """
    A counter with both class and instance tracking.

    class attribute: total_count (shared across all instances)
    instance attribute: count (unique to each instance)
    """

    total_count = 0  # Class attribute - shared by all instances

    def __init__(self):
        """Initialize counter. Increment total_count."""
        self.count = 0  # Instance attribute
        # Also increment the class attribute
        # YOUR CODE HERE
        pass

    def increment(self):
        """Increment both instance count and class total_count."""
        # YOUR CODE HERE
        pass

    def get_count(self):
        """Return instance count."""
        # YOUR CODE HERE
        pass

    @classmethod
    def get_total_count(cls):
        """Return total count across all instances."""
        return cls.total_count

    @classmethod
    def reset_total(cls):
        """Reset the class total_count to 0."""
        # YOUR CODE HERE
        pass


# Exercise 1.4: Properties (getters and setters)
# Python uses @property decorator instead of get/set methods
# JavaScript: get name() { } set name(value) { }

class Circle:
    """
    A circle with radius property and computed properties.
    """

    def __init__(self, radius):
        """Initialize circle. Raise ValueError if radius <= 0."""
        self._radius = None  # Use _prefix for "private" attributes
        self.radius = radius  # This calls the setter

    @property
    def radius(self):
        """Get the radius."""
        return self._radius

    @radius.setter
    def radius(self, value):
        """Set the radius. Raise ValueError if value <= 0."""
        # YOUR CODE HERE
        pass

    @property
    def diameter(self):
        """Return the diameter (radius * 2). Read-only property."""
        # YOUR CODE HERE
        pass

    @property
    def area(self):
        """Return the area (pi * radius^2). Read-only property."""
        # Hint: import math and use math.pi
        # YOUR CODE HERE
        pass


# Exercise 1.5: String representations

class Product:
    """
    A product with nice string representations.

    __str__: Human-readable (for print())
    __repr__: Developer-readable (for debugging)

    JavaScript equivalent: toString()
    """

    def __init__(self, name, price, quantity=0):
        self.name = name
        self.price = price
        self.quantity = quantity

    def __str__(self):
        """Return human-readable string: "Product: {name} - ${price}" """
        # YOUR CODE HERE
        pass

    def __repr__(self):
        """Return developer string: "Product(name='{name}', price={price}, quantity={quantity})" """
        # YOUR CODE HERE
        pass


# Exercise 1.6: Comparison methods

class Temperature:
    """
    A temperature class with comparison support.

    Dunder methods for comparison:
    __eq__: ==
    __lt__: <
    __le__: <=
    __gt__: >
    __ge__: >=
    """

    def __init__(self, celsius):
        self.celsius = celsius

    @property
    def fahrenheit(self):
        """Convert to Fahrenheit."""
        return self.celsius * 9/5 + 32

    def __eq__(self, other):
        """Check equality based on celsius value."""
        if not isinstance(other, Temperature):
            return NotImplemented
        # YOUR CODE HERE
        pass

    def __lt__(self, other):
        """Check if less than."""
        if not isinstance(other, Temperature):
            return NotImplemented
        # YOUR CODE HERE
        pass

    # Once __eq__ and __lt__ are defined, you can use @functools.total_ordering
    # to auto-generate the rest. For practice, let's do __le__ manually:

    def __le__(self, other):
        """Check if less than or equal."""
        if not isinstance(other, Temperature):
            return NotImplemented
        # YOUR CODE HERE
        pass

    def __repr__(self):
        return f"Temperature({self.celsius}°C)"


# Exercise 1.7: Making objects callable

class Multiplier:
    """
    A callable class that multiplies by a factor.

    __call__ makes instances callable like functions.

    mult = Multiplier(3)
    mult(5)  # Returns 15
    """

    def __init__(self, factor):
        self.factor = factor

    def __call__(self, value):
        """Multiply value by factor."""
        # YOUR CODE HERE
        pass


# Exercise 1.8: Container-like behavior

class Inventory:
    """
    An inventory that supports len() and 'in' operator.

    __len__: len(inventory)
    __contains__: "item" in inventory
    __getitem__: inventory["item"]
    """

    def __init__(self):
        self._items = {}

    def add(self, item, quantity=1):
        """Add quantity of item to inventory."""
        self._items[item] = self._items.get(item, 0) + quantity

    def __len__(self):
        """Return total number of unique items."""
        # YOUR CODE HERE
        pass

    def __contains__(self, item):
        """Check if item is in inventory."""
        # YOUR CODE HERE
        pass

    def __getitem__(self, item):
        """Get quantity of item. Return 0 if not found."""
        # YOUR CODE HERE
        pass


# ============= TESTS (Don't modify below) =============
if __name__ == "__main__":
    import math
    print("Running tests...")

    # Test 1.1
    dog = Dog("Buddy", "Golden Retriever", 3)
    assert dog.name == "Buddy"
    assert dog.breed == "Golden Retriever"
    assert dog.age == 3
    assert dog.bark() == "Buddy says Woof!"
    assert dog.describe() == "Buddy is a 3 year old Golden Retriever"
    print("✓ Exercise 1.1 passed")

    # Test 1.2
    account = BankAccount("Alice", 100)
    assert account.get_balance() == 100
    assert account.deposit(50) == 150
    assert account.withdraw(30) == 120
    try:
        account.withdraw(200)
        assert False, "Should raise ValueError"
    except ValueError:
        pass
    print("✓ Exercise 1.2 passed")

    # Test 1.3
    Counter.reset_total()
    c1 = Counter()
    c1.increment()
    c1.increment()
    c2 = Counter()
    c2.increment()
    assert c1.get_count() == 2
    assert c2.get_count() == 1
    assert Counter.get_total_count() == 5  # 2 from __init__ + 3 from increment
    print("✓ Exercise 1.3 passed")

    # Test 1.4
    circle = Circle(5)
    assert circle.radius == 5
    assert circle.diameter == 10
    assert abs(circle.area - 78.54) < 0.01
    circle.radius = 10
    assert circle.diameter == 20
    try:
        circle.radius = -1
        assert False, "Should raise ValueError"
    except ValueError:
        pass
    print("✓ Exercise 1.4 passed")

    # Test 1.5
    product = Product("Widget", 9.99, 100)
    assert str(product) == "Product: Widget - $9.99"
    assert repr(product) == "Product(name='Widget', price=9.99, quantity=100)"
    print("✓ Exercise 1.5 passed")

    # Test 1.6
    t1 = Temperature(20)
    t2 = Temperature(20)
    t3 = Temperature(30)
    assert t1 == t2
    assert t1 < t3
    assert t1 <= t2
    assert t3 > t1
    print("✓ Exercise 1.6 passed")

    # Test 1.7
    mult = Multiplier(3)
    assert mult(5) == 15
    assert mult(10) == 30
    print("✓ Exercise 1.7 passed")

    # Test 1.8
    inv = Inventory()
    inv.add("apple", 5)
    inv.add("banana", 3)
    assert len(inv) == 2
    assert "apple" in inv
    assert "cherry" not in inv
    assert inv["apple"] == 5
    assert inv["cherry"] == 0
    print("✓ Exercise 1.8 passed")

    print("\n🎉 All tests passed! Great job!")
