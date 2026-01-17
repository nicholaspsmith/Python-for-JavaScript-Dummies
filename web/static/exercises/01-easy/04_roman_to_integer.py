"""
Roman to Integer
=================

Convert a Roman numeral string to an integer.

Roman numerals: I=1, V=5, X=10, L=50, C=100, D=500, M=1000

Subtraction rules:
- I before V (5) or X (10) means subtract 1 (IV=4, IX=9)
- X before L (50) or C (100) means subtract 10 (XL=40, XC=90)
- C before D (500) or M (1000) means subtract 100 (CD=400, CM=900)

Example:
    Input: "III"     Output: 3
    Input: "LVIII"   Output: 58  (L=50 + V=5 + III=3)
    Input: "MCMXCIV" Output: 1994 (M=1000 + CM=900 + XC=90 + IV=4)

JS to Python Tips:
-----------------
- Dict literal syntax is identical: `{'I': 1, 'V': 5}` (same as JS object).
- String indexing: `s[i]` works the same. `s[-1]` gets the last character.
- Range with index: `for i in range(len(s)):` or `range(len(s) - 1)`.
- String length: `len(s)` instead of `s.length`.
- Comparison: If current value < next value, subtract; otherwise add.

Key insight: Scan left to right. If a smaller value precedes a larger one, subtract it.
"""


def roman_to_int(s: str) -> int:
    """
    Convert a Roman numeral string to an integer.

    Hint: Create a dict mapping Roman chars to values.
    If current char's value < next char's value, subtract it; else add it.
    """
    # Your code here
    ...


# ============= TESTS =============
if __name__ == "__main__":
    print("Running tests...")

    # Test 1: Simple
    assert roman_to_int("III") == 3, "III should be 3"
    print("✓ Test 1 passed: III = 3")

    # Test 2: Subtraction case
    assert roman_to_int("IV") == 4, "IV should be 4"
    print("✓ Test 2 passed: IV = 4")

    # Test 3: Mixed
    assert roman_to_int("LVIII") == 58, "LVIII should be 58"
    print("✓ Test 3 passed: LVIII = 58")

    # Test 4: Complex
    assert roman_to_int("MCMXCIV") == 1994, "MCMXCIV should be 1994"
    print("✓ Test 4 passed: MCMXCIV = 1994")

    # Test 5: Nine
    assert roman_to_int("IX") == 9, "IX should be 9"
    print("✓ Test 5 passed: IX = 9")

    # Test 6: Large number
    assert roman_to_int("MMMCMXCIX") == 3999, "MMMCMXCIX should be 3999"
    print("✓ Test 6 passed: MMMCMXCIX = 3999")

    print("\n🎉 All tests passed!")
