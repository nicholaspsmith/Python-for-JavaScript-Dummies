# Solutions Guide

This document contains hints and solutions for all exercises. Try to complete them yourself first!

## How to Use This Guide

1. Attempt the exercise on your own
2. If stuck, check the hints section
3. Only look at solutions as a last resort
4. Run the tests to verify your solutions

---

## 01-basics

### 01_variables_and_types.py

<details>
<summary>Exercise 1.1 Solution</summary>

```python
greeting = "Hello, Python!"
year = 2024
pi_value = 3.14159
is_learning = True
nothing = None
```
</details>

<details>
<summary>Exercise 1.2 Solution</summary>

```python
string_type = str
int_type = int
float_type = float
bool_type = bool
none_type = type(None)
```
</details>

<details>
<summary>Exercise 1.3 Solution</summary>

```python
converted_int = int(number_string)
truncated_int = int(float_number)
zero_as_bool = bool(some_number)
nonzero_as_bool = bool(non_zero)
```
</details>

<details>
<summary>Exercise 1.4 Solution</summary>

```python
f_string_greeting = f"Hello, {name}!"
multi_line = """Line 1
Line 2
Line 3"""
```
</details>

<details>
<summary>Exercise 1.5 Solution</summary>

```python
stripped = text.strip()
lowered = text.lower()
replaced = text.replace("Python", "JavaScript")
split_list = parts.split(", ")
```
</details>

### 02_operators.py

<details>
<summary>Solutions</summary>

```python
# 2.1
power_result = 2 ** 10
regular_division = 17 / 5
integer_division = 17 // 5
remainder = 17 % 5

# 2.2
int_float_equal = 10 == 10.0  # True
string_int_equal = "5" == 5  # False
not_equal = 10 != 5  # True

# 2.3
and_result = a and b
or_result = a or b
not_result = not a

# 2.4
equal_value = list1 == list2
same_object_1_2 = list1 is list2
same_object_1_3 = list1 is list3
is_none = value is None

# 2.5
three_in_list = 3 in numbers
ten_not_in_list = 10 not in numbers
python_in_message = "Python" in message
name_in_dict = "name" in person
alice_in_dict = "Alice" in person

# 2.6
if (length := len(data)) > 5:
    result_walrus = f"List has {length} items"
```
</details>

---

## 02-collections

### 01_lists.py

<details>
<summary>Solutions</summary>

```python
# 1.1
mixed = [1, "two", 3.0, True, None]
first = mixed[0]
last = mixed[-1]
second_to_last = mixed[-2]

# 1.2
slice_1 = numbers[2:5]
slice_2 = numbers[:3]
slice_3 = numbers[-3:]
every_other = numbers[::2]
reversed_list = numbers[::-1]

# 1.3
fruits.append("cherry")
fruits.insert(0, "apricot")
removed_last = fruits.pop()
removed_first = fruits.pop(0)

# 1.4
concatenated = list_a + list_b
repeated = [1, 2, 3] * 3
length = len(list_a)
contains_two = 2 in list_a

# 1.5
x, y, *remaining = coordinates
first_coord, *_, last_coord = coordinates

# 1.6
sorted_new = sorted(unsorted)
to_sort.sort()
reverse_sorted = sorted(unsorted, reverse=True)
```
</details>

### 02_dictionaries.py

<details>
<summary>Solutions</summary>

```python
# 2.1
person = {"name": "Alice", "age": 30, "city": "New York"}
name = person["name"]
age = person.get("age")
country = person.get("country", "Unknown")

# 2.2
user["role"] = "admin"
user["email"] = "alice@newdomain.com"
removed_username = user.pop("username")

# 2.3
keys = list(inventory.keys())
values = list(inventory.values())
items = list(inventory.items())
has_apples = "apples" in inventory

# 2.4
formatted_scores = [f"{k}: {v}" for k, v in scores.items()]

# 2.5
merged = {**defaults, **user_prefs}

# 2.6
doubled_prices = {k: v * 2 for k, v in prices.items()}
expensive = {k: v for k, v in prices.items() if v >= 0.75}

# 2.7
alice_role = company["employees"]["alice"]["role"]
bob_salary = company["employees"]["bob"]["salary"]
company["employees"]["charlie"] = {"role": "manager", "salary": 90000}
```
</details>

### 03_tuples_sets.py

<details>
<summary>Solutions</summary>

```python
# 3.1
coordinates = (10, 20, 30)
single = (42,)
point = 5, 10

# 3.2
red = rgb[0]
r, g, b = rgb
new_rgb = (200, rgb[1], rgb[2])

# 3.3
locations = {(0, 0): "origin", (10, 20): "point A"}
origin_name = locations[(0, 0)]

# 3.4
Person = namedtuple('Person', ['name', 'age', 'city'])
alice_age = alice.age
alice_city = alice.city

# 3.5
numbers_set = {1, 2, 3, 4, 5}
unique_numbers = set([1, 2, 2, 3, 3, 3, 4])
empty_set = set()

# 3.6
union = set_a | set_b
intersection = set_a & set_b
difference = set_a - set_b
symmetric_diff = set_a ^ set_b

# 3.7
fruits_set.add("cherry")
fruits_set.add("apple")
fruits_set.remove("banana")
has_apple = "apple" in fruits_set

# 3.8
unique_ordered = list(dict.fromkeys(items_with_dupes))
common = set(list1) & set(list2)

# 3.9
even_squares = {x**2 for x in numbers if x % 2 == 0}

# 3.10
frozen = frozenset({1, 2, 3})
```
</details>

---

## 03-control-flow

### 01_conditionals.py

<details>
<summary>Solutions</summary>

```python
def get_grade(score):
    if score >= 90:
        return "A"
    elif score >= 80:
        return "B"
    elif score >= 70:
        return "C"
    elif score >= 60:
        return "D"
    else:
        return "F"

def is_truthy(value):
    return bool(value)

def absolute_value(n):
    return n if n >= 0 else -n

def can_vote(age, is_citizen, is_registered):
    return age >= 18 and is_citizen and is_registered

def can_enter_club(age, has_id, is_vip):
    return (age >= 21 and has_id) or is_vip

def is_valid_percentage(value):
    return 0 <= value <= 100

def is_between(value, low, high):
    return low < value < high

def http_status_message(code):
    match code:
        case 200: return "OK"
        case 201: return "Created"
        case 400: return "Bad Request"
        case 401: return "Unauthorized"
        case 404: return "Not Found"
        case 500: return "Internal Server Error"
        case _: return "Unknown Status"

def describe_point(point):
    match point:
        case (0, 0): return "origin"
        case (0, y): return "on y-axis"
        case (x, 0): return "on x-axis"
        case (x, y) if x == y: return "on diagonal"
        case (x, y): return f"point at ({x}, {y})"

def process_user(user):
    if user is None:
        return "No user provided"
    if "name" not in user:
        return "Invalid user: no name"
    if user["name"] == "":
        return "Invalid user: empty name"
    if not user.get("active", True):
        return "User is inactive"
    return f"Processing: {user['name']}"
```
</details>

### 02_loops.py & 03_comprehensions.py

<details>
<summary>Key Solutions</summary>

```python
# Loops
def sum_to_n(n):
    total = 0
    for i in range(1, n + 1):
        total += i
    return total

def find_index(items, target):
    for index, item in enumerate(items):
        if item == target:
            return index
    return -1

def combine_names(first_names, last_names):
    return [f"{first} {last}" for first, last in zip(first_names, last_names)]

# Comprehensions
squares = [x**2 for x in range(1, 11)]
evens = [x for x in range(1, 21) if x % 2 == 0]
flattened = [item for row in matrix for item in row]
num_to_square = {x: x**2 for x in range(1, 6)}
first_letters = {word[0] for word in words_set}
square_gen = (x**2 for x in range(1, 11))
```
</details>

---

## 04-functions

<details>
<summary>Key Solutions</summary>

```python
def greet(name):
    return f"Hello, {name}!"

def append_to_list(item, lst=None):
    if lst is None:
        lst = []
    lst.append(item)
    return lst

def min_max(numbers):
    if not numbers:
        return (None, None)
    return (min(numbers), max(numbers))

double = lambda x: x * 2
is_positive = lambda x: x > 0
multiply = lambda x, y: x * y

def apply_operation(x, y, operation):
    return operation(x, y)

def make_multiplier(factor):
    def multiplier(x):
        return x * factor
    return multiplier
```
</details>

---

## More Solutions

For remaining exercises, the key patterns are:

### OOP
- Use `super().__init__()` to call parent constructors
- `@property` for getters, `@name.setter` for setters
- `__str__` for human-readable, `__repr__` for debugging

### Error Handling
- `try/except/else/finally` for clean error handling
- `raise ValueError("message")` to raise exceptions
- `raise NewError() from original` for exception chaining

### Decorators
```python
def decorator(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        # before
        result = func(*args, **kwargs)
        # after
        return result
    return wrapper
```

### Generators
```python
def generator():
    yield value  # yields one at a time

# Generator expression
gen = (x**2 for x in range(10))
```

### Context Managers
```python
class MyContext:
    def __enter__(self):
        return self
    def __exit__(self, exc_type, exc_val, exc_tb):
        return False  # Don't suppress exceptions

@contextmanager
def my_context():
    # setup
    yield resource
    # cleanup
```

---

## Running Tests

Each exercise file has built-in tests. Run them with:

```bash
python3 filename.py
```

For pytest exercises:
```bash
pip install pytest
pytest 13-testing/01_pytest_basics.py -v
```

## Need More Help?

1. Read the Python documentation: https://docs.python.org/3/
2. Try the exercise in a Python REPL first
3. Use `print()` statements to debug
4. Check error messages carefully - they're usually helpful!
