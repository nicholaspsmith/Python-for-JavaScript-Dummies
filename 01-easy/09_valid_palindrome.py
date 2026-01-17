"""
Valid Palindrome
=================

A phrase is a palindrome if, after converting all uppercase letters to lowercase
and removing all non-alphanumeric characters, it reads the same forward and backward.

Given a string s, return True if it is a palindrome, or False otherwise.

Example:
    Input: s = "A man, a plan, a canal: Panama"
    Output: True ("amanaplanacanalpanama" is a palindrome)

    Input: s = "race a car"
    Output: False

    Input: s = " "
    Output: True (empty string after removing non-alphanumeric)

JS to Python Tips:
-----------------
- `str.lower()` like JS `str.toLowerCase()`.
- `str.isalnum()` checks if char is alphanumeric (no JS equivalent - you'd use regex).
- `char.isalpha()` checks if alphabetic, `char.isdigit()` checks if numeric.
- String building: You CAN use `+=` on strings, but list + join is more efficient:
  `''.join([char for char in s if char.isalnum()])` - this is a list comprehension!
- Two-pointer approach: `left, right = 0, len(s) - 1`.
- Python's `while left < right:` is same as JS.

List comprehension is the Pythonic way to filter and transform:
`[expression for item in iterable if condition]`
"""


def is_palindrome(s: str) -> bool:
    """
    Return True if s is a valid palindrome (ignoring case and non-alphanumeric chars).

    Hint: Either clean the string first with a list comprehension,
    or use two pointers that skip non-alphanumeric characters.
    """
    # Your code here
    ...


# ============= TESTS =============
if __name__ == "__main__":
    print("Running tests...")

    # Test 1: Classic palindrome
    assert is_palindrome("A man, a plan, a canal: Panama") == True
    print("✓ Test 1 passed: Panama palindrome")

    # Test 2: Not a palindrome
    assert is_palindrome("race a car") == False
    print("✓ Test 2 passed: 'race a car' is not a palindrome")

    # Test 3: Empty/whitespace
    assert is_palindrome(" ") == True
    print("✓ Test 3 passed: Whitespace only")

    # Test 4: Single character
    assert is_palindrome("a") == True
    print("✓ Test 4 passed: Single character")

    # Test 5: Numbers included
    assert is_palindrome("0P") == False
    print("✓ Test 5 passed: Alphanumeric comparison")

    # Test 6: Numeric palindrome
    assert is_palindrome("12321") == True
    print("✓ Test 6 passed: Numeric palindrome")

    print("\n🎉 All tests passed!")
