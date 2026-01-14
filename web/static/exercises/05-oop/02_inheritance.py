"""
Exercise 2: Inheritance
========================

Python supports single and multiple inheritance.

JavaScript:
    class Child extends Parent {
        constructor() {
            super();
        }
    }

Python:
    class Child(Parent):
        def __init__(self):
            super().__init__()

Key differences:
- Parent classes listed in parentheses
- super() returns a proxy object (no need to specify parent class)
- Multiple inheritance is supported
- Method Resolution Order (MRO) determines lookup order

EXERCISES:
Complete each exercise below. Run with: python3 02_inheritance.py
"""


# Exercise 2.1: Basic inheritance

class Animal:
    """Base class for all animals."""

    def __init__(self, name, species):
        self.name = name
        self.species = species

    def speak(self):
        """Return generic animal sound."""
        return f"{self.name} makes a sound"

    def describe(self):
        """Return description of animal."""
        return f"{self.name} is a {self.species}"


class Cat(Animal):
    """
    A cat class that inherits from Animal.
    """

    def __init__(self, name, color):
        """Initialize cat with name and color. Species should be "cat"."""
        # Call parent __init__ with super()
        # YOUR CODE HERE
        pass

    def speak(self):
        """Override to return "{name} says Meow!" """
        # YOUR CODE HERE
        pass

    def purr(self):
        """Return "{name} purrs contentedly" """
        # YOUR CODE HERE
        pass


class Bird(Animal):
    """
    A bird class that inherits from Animal.
    """

    def __init__(self, name, can_fly=True):
        """Initialize bird. Species should be "bird"."""
        # YOUR CODE HERE
        pass

    def speak(self):
        """Override to return "{name} says Chirp!" """
        # YOUR CODE HERE
        pass

    def fly(self):
        """Return "{name} flies away" if can_fly, else "{name} cannot fly" """
        # YOUR CODE HERE
        pass


# Exercise 2.2: Calling parent methods with super()

class Vehicle:
    """Base vehicle class."""

    def __init__(self, brand, model, year):
        self.brand = brand
        self.model = model
        self.year = year

    def info(self):
        return f"{self.year} {self.brand} {self.model}"


class ElectricCar(Vehicle):
    """
    Electric car that extends Vehicle with battery info.
    """

    def __init__(self, brand, model, year, battery_capacity):
        """Initialize with vehicle info + battery_capacity (in kWh)."""
        # Call parent __init__ first, then set battery_capacity
        # YOUR CODE HERE
        pass

    def info(self):
        """
        Extend parent info to include battery.
        Return "{parent_info} (Electric, {battery_capacity} kWh)"
        """
        # Use super().info() to get parent info
        # YOUR CODE HERE
        pass


# Exercise 2.3: Abstract base classes (ABCs)
# Python's way of defining interfaces
from abc import ABC, abstractmethod


class Shape(ABC):
    """
    Abstract base class for shapes.
    Cannot be instantiated directly.
    """

    @abstractmethod
    def area(self):
        """Calculate and return the area."""
        pass

    @abstractmethod
    def perimeter(self):
        """Calculate and return the perimeter."""
        pass

    def describe(self):
        """Non-abstract method available to all subclasses."""
        return f"A shape with area {self.area():.2f} and perimeter {self.perimeter():.2f}"


class Rectangle(Shape):
    """
    Rectangle implementation of Shape.
    """

    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self):
        """Return width * height."""
        # YOUR CODE HERE
        pass

    def perimeter(self):
        """Return 2 * (width + height)."""
        # YOUR CODE HERE
        pass


class Circle2(Shape):
    """
    Circle implementation of Shape.
    """

    def __init__(self, radius):
        self.radius = radius

    def area(self):
        """Return pi * radius^2."""
        import math
        # YOUR CODE HERE
        pass

    def perimeter(self):
        """Return 2 * pi * radius (circumference)."""
        import math
        # YOUR CODE HERE
        pass


# Exercise 2.4: Multiple inheritance

class Swimmer:
    """Mixin class for swimming ability."""

    def swim(self):
        return f"{self.name} is swimming"


class Flyer:
    """Mixin class for flying ability."""

    def fly(self):
        return f"{self.name} is flying"


class Duck(Animal, Swimmer, Flyer):
    """
    A duck can do everything: walk, swim, and fly!
    Uses multiple inheritance with mixins.
    """

    def __init__(self, name):
        """Initialize duck. Species should be "duck"."""
        # YOUR CODE HERE
        pass

    def speak(self):
        """Return "{name} says Quack!" """
        # YOUR CODE HERE
        pass


# Exercise 2.5: Method Resolution Order (MRO)
# When a method is called, Python searches classes in a specific order

class A:
    def method(self):
        return "A"


class B(A):
    def method(self):
        return "B"


class C(A):
    def method(self):
        return "C"


class D(B, C):
    """D inherits from both B and C."""
    pass


class E(C, B):
    """E inherits from C first, then B."""
    pass


# Understand MRO:
# D.mro() -> [D, B, C, A, object]
# E.mro() -> [E, C, B, A, object]

# What will these return?
d_result = D().method()  # Should be "B" (B comes before C in MRO)
e_result = E().method()  # Should be "C" (C comes before B in MRO)


# Exercise 2.6: super() with multiple inheritance

class Logger:
    """Mixin that logs initialization."""

    def __init__(self, **kwargs):
        print(f"Logger.__init__ called with {kwargs}")
        super().__init__(**kwargs)


class Validator:
    """Mixin that validates initialization."""

    def __init__(self, **kwargs):
        print(f"Validator.__init__ called with {kwargs}")
        super().__init__(**kwargs)


class Entity:
    """Base entity class."""

    def __init__(self, name, **kwargs):
        print(f"Entity.__init__ called with name={name}, {kwargs}")
        self.name = name
        super().__init__(**kwargs)


class LoggedEntity(Logger, Validator, Entity):
    """
    Entity with logging and validation.
    Demonstrates cooperative multiple inheritance.

    When using super() in multiple inheritance, always use **kwargs
    to pass unused arguments to the next class in the MRO.
    """

    def __init__(self, name, **kwargs):
        super().__init__(name=name, **kwargs)


# Exercise 2.7: isinstance() and issubclass()

def classify_animal(animal):
    """
    Return a classification of the animal:
    - "feline" if it's a Cat
    - "avian" if it's a Bird
    - "waterfowl" if it's a Duck
    - "generic" if it's just an Animal
    - "unknown" if it's not an Animal

    Use isinstance() to check.
    Note: Check more specific types first (Duck is also an Animal)!
    """
    # YOUR CODE HERE
    pass


# ============= TESTS (Don't modify below) =============
if __name__ == "__main__":
    print("Running tests...")

    # Test 2.1
    cat = Cat("Whiskers", "orange")
    assert cat.name == "Whiskers"
    assert cat.species == "cat"
    assert cat.color == "orange"
    assert cat.speak() == "Whiskers says Meow!"
    assert cat.purr() == "Whiskers purrs contentedly"

    bird = Bird("Tweety", can_fly=True)
    assert bird.speak() == "Tweety says Chirp!"
    assert bird.fly() == "Tweety flies away"
    penguin = Bird("Pingu", can_fly=False)
    assert penguin.fly() == "Pingu cannot fly"
    print("✓ Exercise 2.1 passed")

    # Test 2.2
    tesla = ElectricCar("Tesla", "Model 3", 2023, 75)
    assert tesla.battery_capacity == 75
    assert tesla.info() == "2023 Tesla Model 3 (Electric, 75 kWh)"
    print("✓ Exercise 2.2 passed")

    # Test 2.3
    rect = Rectangle(5, 3)
    assert rect.area() == 15
    assert rect.perimeter() == 16
    import math
    circle = Circle2(5)
    assert abs(circle.area() - 78.54) < 0.01
    assert abs(circle.perimeter() - 31.42) < 0.01
    # Verify Shape cannot be instantiated
    try:
        shape = Shape()
        assert False, "Should not be able to instantiate abstract class"
    except TypeError:
        pass
    print("✓ Exercise 2.3 passed")

    # Test 2.4
    duck = Duck("Donald")
    assert duck.speak() == "Donald says Quack!"
    assert duck.swim() == "Donald is swimming"
    assert duck.fly() == "Donald is flying"
    assert duck.describe() == "Donald is a duck"
    print("✓ Exercise 2.4 passed")

    # Test 2.5
    assert d_result == "B", f"Expected 'B' but got '{d_result}'"
    assert e_result == "C", f"Expected 'C' but got '{e_result}'"
    print("✓ Exercise 2.5 passed")

    # Test 2.6
    print("Testing LoggedEntity initialization:")
    entity = LoggedEntity(name="Test")
    assert entity.name == "Test"
    print("✓ Exercise 2.6 passed")

    # Test 2.7
    assert classify_animal(Cat("Test", "black")) == "feline"
    assert classify_animal(Bird("Test")) == "avian"
    assert classify_animal(Duck("Test")) == "waterfowl"
    assert classify_animal(Animal("Test", "unknown")) == "generic"
    assert classify_animal("not an animal") == "unknown"
    print("✓ Exercise 2.7 passed")

    print("\n🎉 All tests passed! Great job!")
