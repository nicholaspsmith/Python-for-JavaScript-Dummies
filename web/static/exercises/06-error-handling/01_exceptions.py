"""
Exercise 1: Error Handling
===========================

Python uses try/except instead of JavaScript's try/catch.

JavaScript:
    try {
        // code
    } catch (error) {
        console.log(error.message);
    } finally {
        // cleanup
    }

Python:
    try:
        # code
    except Exception as e:
        print(str(e))
    finally:
        # cleanup

Key differences:
- 'except' instead of 'catch'
- Can catch specific exception types
- 'as e' instead of '(error)'
- 'raise' instead of 'throw'
- 'else' clause runs if no exception occurred

EXERCISES:
Complete each exercise below. Run with: python3 01_exceptions.py
"""


# Exercise 1.1: Basic try/except

def safe_divide(a, b):
    """
    Divide a by b, returning None if division by zero.
    Don't let the function raise an exception.
    """
    # YOUR CODE HERE
    pass


def safe_int(value):
    """
    Convert value to int, returning None if conversion fails.
    """
    # YOUR CODE HERE
    pass


def safe_index(lst, index):
    """
    Get lst[index], returning None if index is out of bounds.
    """
    # YOUR CODE HERE
    pass


# Exercise 1.2: Catching specific exceptions
# Python has a hierarchy of built-in exceptions:
# BaseException
#   └── Exception
#       ├── ValueError
#       ├── TypeError
#       ├── KeyError
#       ├── IndexError
#       └── ...

def parse_config(config_str):
    """
    Parse a config string "key=value" into a tuple (key, value_as_int).

    Handle these cases:
    - If no "=" in string, raise ValueError with "Missing '=' separator"
    - If value is not a valid integer, raise ValueError with "Invalid integer value"
    - If successful, return (key, value_as_int)

    Example:
    parse_config("port=8080") -> ("port", 8080)
    parse_config("invalid") -> ValueError("Missing '=' separator")
    parse_config("port=abc") -> ValueError("Invalid integer value")
    """
    # YOUR CODE HERE
    pass


# Exercise 1.3: Multiple except blocks

def process_data(data, key, index):
    """
    Try to get data[key][index].

    Return different error messages for different failures:
    - KeyError: "Key '{key}' not found"
    - IndexError: "Index {index} out of range"
    - TypeError: "Data is not subscriptable"
    - Any other exception: "Unknown error: {exception}"

    If successful, return the value.
    """
    # YOUR CODE HERE
    pass


# Exercise 1.4: else and finally clauses

def read_number_from_file(filepath):
    """
    Try to read a number from a file.

    - Open the file
    - Read the content
    - Convert to float
    - If successful, return (True, number)
    - If file not found, return (False, "File not found")
    - If conversion fails, return (False, "Invalid number format")
    - Always close the file (hint: finally clause)

    For testing purposes, simulate file operations:
    - If filepath == "valid.txt", content is "42.5"
    - If filepath == "invalid.txt", content is "not a number"
    - If filepath is anything else, raise FileNotFoundError
    """
    # Simulated file content
    file_contents = {
        "valid.txt": "42.5",
        "invalid.txt": "not a number"
    }

    file_handle = None
    try:
        # YOUR CODE HERE
        # Simulate file operations using file_contents dict
        pass
    except FileNotFoundError:
        return (False, "File not found")
    except ValueError:
        return (False, "Invalid number format")
    else:
        # This runs if no exception occurred
        # YOUR CODE HERE
        pass
    finally:
        # Always runs - cleanup goes here
        if file_handle is not None:
            pass  # Would close file in real code


# Exercise 1.5: Raising exceptions

def validate_email(email):
    """
    Validate an email address.
    Raise ValueError with descriptive message if invalid:
    - "Email cannot be empty" if email is empty string
    - "Email must contain @" if no @ symbol
    - "Email must have domain" if nothing after @
    Return True if valid.
    """
    # YOUR CODE HERE
    pass


def validate_age(age):
    """
    Validate age.
    - Raise TypeError if age is not an int
    - Raise ValueError("Age cannot be negative") if age < 0
    - Raise ValueError("Age is unrealistic") if age > 150
    Return True if valid.
    """
    # YOUR CODE HERE
    pass


# Exercise 1.6: Custom exceptions

class ValidationError(Exception):
    """Base exception for validation errors."""
    pass


class PasswordTooShortError(ValidationError):
    """Raised when password is too short."""

    def __init__(self, length, min_length=8):
        self.length = length
        self.min_length = min_length
        super().__init__(
            f"Password is {length} characters, minimum is {min_length}"
        )


class PasswordNoDigitError(ValidationError):
    """Raised when password has no digit."""

    def __init__(self):
        super().__init__("Password must contain at least one digit")


def validate_password(password):
    """
    Validate password:
    - At least 8 characters (raise PasswordTooShortError if not)
    - At least one digit (raise PasswordNoDigitError if not)
    Return True if valid.
    """
    # YOUR CODE HERE
    pass


# Exercise 1.7: Exception chaining

def fetch_user_data(user_id):
    """
    Simulate fetching user data.
    For this exercise:
    - user_id 1 returns {"name": "Alice", "email": "alice@test.com"}
    - user_id 2 returns {"name": "Bob"} (no email)
    - Other IDs raise KeyError
    """
    users = {
        1: {"name": "Alice", "email": "alice@test.com"},
        2: {"name": "Bob"}
    }
    return users[user_id]


def get_user_email(user_id):
    """
    Get user's email by ID.

    Use exception chaining ('raise ... from ...') to provide context:
    - If user not found, raise ValueError("User {id} not found") from KeyError
    - If user has no email, raise ValueError("User {id} has no email") from KeyError
    """
    try:
        # YOUR CODE HERE
        pass
    except KeyError as e:
        # Use 'raise ... from e' to chain exceptions
        # YOUR CODE HERE
        pass


# Exercise 1.8: Context manager with error handling
# Preview of context managers - we'll cover these more later

class ManagedResource:
    """
    A resource that needs cleanup.
    Tracks if it was properly closed.
    """

    def __init__(self, name, should_fail=False):
        self.name = name
        self.should_fail = should_fail
        self.is_open = True
        self.was_closed = False

    def do_work(self):
        """Do some work. Raises RuntimeError if should_fail is True."""
        if self.should_fail:
            raise RuntimeError(f"{self.name} failed!")
        return f"{self.name} completed work"

    def close(self):
        """Close the resource."""
        self.is_open = False
        self.was_closed = True


def use_resource(name, should_fail=False):
    """
    Use a ManagedResource.
    MUST close the resource even if an exception occurs.
    Return the result of do_work() if successful.
    Re-raise any exception after closing.
    """
    resource = ManagedResource(name, should_fail)
    try:
        # YOUR CODE HERE
        pass
    finally:
        # YOUR CODE HERE
        pass


# ============= TESTS (Don't modify below) =============
if __name__ == "__main__":
    print("Running tests...")

    # Test 1.1
    assert safe_divide(10, 2) == 5
    assert safe_divide(10, 0) is None
    assert safe_int("42") == 42
    assert safe_int("abc") is None
    assert safe_index([1, 2, 3], 1) == 2
    assert safe_index([1, 2, 3], 10) is None
    print("✓ Exercise 1.1 passed")

    # Test 1.2
    assert parse_config("port=8080") == ("port", 8080)
    try:
        parse_config("invalid")
        assert False
    except ValueError as e:
        assert "Missing '=' separator" in str(e)
    try:
        parse_config("port=abc")
        assert False
    except ValueError as e:
        assert "Invalid integer value" in str(e)
    print("✓ Exercise 1.2 passed")

    # Test 1.3
    data = {"users": ["Alice", "Bob"]}
    assert process_data(data, "users", 0) == "Alice"
    assert "not found" in process_data(data, "missing", 0)
    assert "out of range" in process_data(data, "users", 10)
    assert "not subscriptable" in process_data(None, "key", 0)
    print("✓ Exercise 1.3 passed")

    # Test 1.4
    assert read_number_from_file("valid.txt") == (True, 42.5)
    assert read_number_from_file("invalid.txt") == (False, "Invalid number format")
    assert read_number_from_file("missing.txt") == (False, "File not found")
    print("✓ Exercise 1.4 passed")

    # Test 1.5
    assert validate_email("test@example.com") == True
    try:
        validate_email("")
        assert False
    except ValueError as e:
        assert "empty" in str(e)
    try:
        validate_email("invalid")
        assert False
    except ValueError as e:
        assert "@" in str(e)
    print("✓ Exercise 1.5 passed")

    # Test 1.6
    assert validate_password("password123") == True
    try:
        validate_password("short1")
        assert False
    except PasswordTooShortError as e:
        assert e.length == 6
    try:
        validate_password("nodigitshere")
        assert False
    except PasswordNoDigitError:
        pass
    print("✓ Exercise 1.6 passed")

    # Test 1.7
    assert get_user_email(1) == "alice@test.com"
    try:
        get_user_email(999)
        assert False
    except ValueError as e:
        assert "not found" in str(e)
        assert e.__cause__ is not None  # Should be chained
    try:
        get_user_email(2)
        assert False
    except ValueError as e:
        assert "no email" in str(e)
    print("✓ Exercise 1.7 passed")

    # Test 1.8
    result = use_resource("test")
    assert "completed" in result
    # Test that resource is closed even on failure
    try:
        use_resource("failing", should_fail=True)
        assert False
    except RuntimeError:
        pass  # Expected
    print("✓ Exercise 1.8 passed")

    print("\n🎉 All tests passed! Great job!")
