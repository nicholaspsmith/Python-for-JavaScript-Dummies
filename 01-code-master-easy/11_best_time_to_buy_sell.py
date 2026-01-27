"""
Best Time to Buy and Sell Stock
================================

You are given an array `prices` where prices[i] is the price of a stock on day i.

You want to maximize profit by choosing a single day to buy and a different day
in the future to sell. Return the maximum profit. If no profit is possible, return 0.

Example:
    Input: prices = [7,1,5,3,6,4]
    Output: 5
    Explanation: Buy on day 2 (price=1), sell on day 5 (price=6), profit = 6-1 = 5.

    Input: prices = [7,6,4,3,1]
    Output: 0
    Explanation: Prices only decrease, no profitable transaction possible.

JS to Python Tips:
-----------------
- `float('inf')` is Python's Infinity (like JS `Infinity` or `Number.POSITIVE_INFINITY`).
- `min()` and `max()` are built-in functions: `min(a, b)` instead of `Math.min(a, b)`.
- No Math object needed - Python has built-in min/max/abs/sum/etc.
- Track minimum seen so far, and at each step calculate potential profit.

One-pass solution:
- Track the minimum price seen so far (your best buying opportunity).
- At each price, calculate profit if selling today.
- Keep track of maximum profit seen.
"""

from typing import List


'''HINTS
{
  "hint1": "def max_profit(prices: List[int]) -> int:\\n    # Track the minimum price seen so far\\n    # Track the maximum profit we can achieve\\n    # One pass through the array is sufficient",
  "hint2": "# Pseudocode:\\n# 1. Handle edge cases: empty list or single element returns 0\\n# 2. Initialize min_price = prices[0], max_profit = 0\\n# 3. For each price in prices:\\n#    - Update min_price = min(min_price, price)\\n#    - Update max_profit = max(max_profit, price - min_price)\\n# 4. Return max_profit",
  "solution": "def max_profit(prices: List[int]) -> int:\\n    if len(prices) < 2:\\n        return 0\\n    \\n    min_price = prices[0]\\n    max_profit = 0\\n    \\n    for price in prices:\\n        min_price = min(min_price, price)\\n        max_profit = max(max_profit, price - min_price)\\n    \\n    return max_profit"
}
HINTS'''


def max_profit(prices: List[int]) -> int:
    """Find the maximum profit from buying and selling once."""
    # Your code here
    ...


# ============= TESTS =============
if __name__ == "__main__":
    _tests_passed = 0
    _tests_failed = 0

    # Test 1: Normal case with profit
    _t1_input = "prices=[7,1,5,3,6,4]"
    _t1_expected = 5
    try:
        result = max_profit([7, 1, 5, 3, 6, 4])
        assert result == _t1_expected, f"Expected {_t1_expected}, got {result}"
        print("✓ Test 1 passed: Normal case with profit")
        _tests_passed += 1
    except AssertionError as e:
        print(f"✗ Test 1 failed: {e}")
        print(f"__TD__|{_t1_input}|{_t1_expected}|{result}")
        _tests_failed += 1
    except Exception as e:
        print(f"✗ Test 1 error: {e}")
        print(f"__TD__|{_t1_input}|{_t1_expected}|Error: {e}")
        _tests_failed += 1

    # Test 2: Decreasing prices
    _t2_input = "prices=[7,6,4,3,1]"
    _t2_expected = 0
    try:
        result = max_profit([7, 6, 4, 3, 1])
        assert result == _t2_expected, f"Expected {_t2_expected}, got {result}"
        print("✓ Test 2 passed: Decreasing prices")
        _tests_passed += 1
    except AssertionError as e:
        print(f"✗ Test 2 failed: {e}")
        print(f"__TD__|{_t2_input}|{_t2_expected}|{result}")
        _tests_failed += 1
    except Exception as e:
        print(f"✗ Test 2 error: {e}")
        print(f"__TD__|{_t2_input}|{_t2_expected}|Error: {e}")
        _tests_failed += 1

    # Test 3: Two elements with profit
    _t3_input = "prices=[1,2]"
    _t3_expected = 1
    try:
        result = max_profit([1, 2])
        assert result == _t3_expected, f"Expected {_t3_expected}, got {result}"
        print("✓ Test 3 passed: Two elements with profit")
        _tests_passed += 1
    except AssertionError as e:
        print(f"✗ Test 3 failed: {e}")
        print(f"__TD__|{_t3_input}|{_t3_expected}|{result}")
        _tests_failed += 1
    except Exception as e:
        print(f"✗ Test 3 error: {e}")
        print(f"__TD__|{_t3_input}|{_t3_expected}|Error: {e}")
        _tests_failed += 1

    # Test 4: Two elements no profit
    _t4_input = "prices=[2,1]"
    _t4_expected = 0
    try:
        result = max_profit([2, 1])
        assert result == _t4_expected, f"Expected {_t4_expected}, got {result}"
        print("✓ Test 4 passed: Two elements no profit")
        _tests_passed += 1
    except AssertionError as e:
        print(f"✗ Test 4 failed: {e}")
        print(f"__TD__|{_t4_input}|{_t4_expected}|{result}")
        _tests_failed += 1
    except Exception as e:
        print(f"✗ Test 4 error: {e}")
        print(f"__TD__|{_t4_input}|{_t4_expected}|Error: {e}")
        _tests_failed += 1

    # Test 5: All same prices
    _t5_input = "prices=[3,3,3,3]"
    _t5_expected = 0
    try:
        result = max_profit([3, 3, 3, 3])
        assert result == _t5_expected, f"Expected {_t5_expected}, got {result}"
        print("✓ Test 5 passed: All same prices")
        _tests_passed += 1
    except AssertionError as e:
        print(f"✗ Test 5 failed: {e}")
        print(f"__TD__|{_t5_input}|{_t5_expected}|{result}")
        _tests_failed += 1
    except Exception as e:
        print(f"✗ Test 5 error: {e}")
        print(f"__TD__|{_t5_input}|{_t5_expected}|Error: {e}")
        _tests_failed += 1

    # Test 6: Single element
    _t6_input = "prices=[5]"
    _t6_expected = 0
    try:
        result = max_profit([5])
        assert result == _t6_expected, f"Expected {_t6_expected}, got {result}"
        print("✓ Test 6 passed: Single element")
        _tests_passed += 1
    except AssertionError as e:
        print(f"✗ Test 6 failed: {e}")
        print(f"__TD__|{_t6_input}|{_t6_expected}|{result}")
        _tests_failed += 1
    except Exception as e:
        print(f"✗ Test 6 error: {e}")
        print(f"__TD__|{_t6_input}|{_t6_expected}|Error: {e}")
        _tests_failed += 1

    # Summary
    print()
    if _tests_failed == 0:
        print(f"🎉 All {_tests_passed} tests passed!")
    else:
        print(f"❌ {_tests_passed}/{_tests_passed + _tests_failed} tests passed")
