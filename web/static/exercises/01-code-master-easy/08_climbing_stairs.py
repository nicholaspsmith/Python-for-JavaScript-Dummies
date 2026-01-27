"""
Climbing Stairs
================

You are climbing a staircase. It takes n steps to reach the top.
Each time you can either climb 1 or 2 steps.
In how many distinct ways can you climb to the top?

Example:
    Input: n = 2
    Output: 2
    Explanation: (1+1) or (2)

    Input: n = 3
    Output: 3
    Explanation: (1+1+1), (1+2), or (2+1)

    Input: n = 4
    Output: 5
    Explanation: (1+1+1+1), (1+1+2), (1+2+1), (2+1+1), (2+2)

JS to Python Tips:
-----------------
- This is the Fibonacci sequence! ways(n) = ways(n-1) + ways(n-2)
- Python integers have arbitrary precision - no overflow issues like JS Number.
- Simple loop: `for i in range(2, n+1):` (range is exclusive of end).
- Tuple unpacking for swap: `a, b = b, a + b` (no temp variable needed!).
  This is cleaner than JS: `[a, b] = [b, a + b]` but similar idea.
- No semicolons needed. Indentation defines code blocks.

Dynamic Programming approach:
- Base cases: ways(1) = 1, ways(2) = 2
- Recurrence: ways(n) = ways(n-1) + ways(n-2)
- You only need to track the last two values, so O(1) space is possible.
"""


'''HINTS
{
  "hint1": "def climb_stairs(n: int) -> int:\\n    # This is the Fibonacci pattern!\\n    # ways(n) = ways(n-1) + ways(n-2)\\n    # Initialize: prev = 1 (ways to climb 1 stair), curr = 2 (ways to climb 2 stairs)",
  "hint2": "# Pseudocode:\\n# 1. Handle base cases: if n == 1, return 1; if n == 2, return 2\\n# 2. Initialize prev = 1, curr = 2\\n# 3. Loop from 3 to n (inclusive):\\n#    - Update using Fibonacci: prev, curr = curr, prev + curr\\n# 4. Return curr",
  "solution": "def climb_stairs(n: int) -> int:\\n    if n == 1:\\n        return 1\\n    if n == 2:\\n        return 2\\n    prev, curr = 1, 2\\n    for _ in range(3, n + 1):\\n        prev, curr = curr, prev + curr\\n    return curr"
}
HINTS'''


def climb_stairs(n: int) -> int:
    """
    Return the number of distinct ways to climb n stairs.

    Hint: This is Fibonacci! Start with base cases (1 step = 1 way, 2 steps = 2 ways).
    Each step n = sum of ways to reach (n-1) and (n-2).
    Use tuple unpacking: a, b = b, a + b
    """
    # Your code here
    ...


# ============= TESTS =============
if __name__ == "__main__":
    _tests_passed = 0
    _tests_failed = 0

    # Test 1: Two stairs
    _t1_input = "n=2"
    _t1_expected = 2
    try:
        result = climb_stairs(2)
        assert result == _t1_expected, f"Expected {_t1_expected}, got {result}"
        print("✓ Test 1 passed: Two stairs")
        _tests_passed += 1
    except AssertionError as e:
        print(f"✗ Test 1 failed: {e}")
        print(f"__TD__|{_t1_input}|{_t1_expected}|{result}")
        _tests_failed += 1
    except Exception as e:
        print(f"✗ Test 1 error: {e}")
        print(f"__TD__|{_t1_input}|{_t1_expected}|Error: {e}")
        _tests_failed += 1

    # Test 2: Three stairs
    _t2_input = "n=3"
    _t2_expected = 3
    try:
        result = climb_stairs(3)
        assert result == _t2_expected, f"Expected {_t2_expected}, got {result}"
        print("✓ Test 2 passed: Three stairs")
        _tests_passed += 1
    except AssertionError as e:
        print(f"✗ Test 2 failed: {e}")
        print(f"__TD__|{_t2_input}|{_t2_expected}|{result}")
        _tests_failed += 1
    except Exception as e:
        print(f"✗ Test 2 error: {e}")
        print(f"__TD__|{_t2_input}|{_t2_expected}|Error: {e}")
        _tests_failed += 1

    # Test 3: Four stairs
    _t3_input = "n=4"
    _t3_expected = 5
    try:
        result = climb_stairs(4)
        assert result == _t3_expected, f"Expected {_t3_expected}, got {result}"
        print("✓ Test 3 passed: Four stairs")
        _tests_passed += 1
    except AssertionError as e:
        print(f"✗ Test 3 failed: {e}")
        print(f"__TD__|{_t3_input}|{_t3_expected}|{result}")
        _tests_failed += 1
    except Exception as e:
        print(f"✗ Test 3 error: {e}")
        print(f"__TD__|{_t3_input}|{_t3_expected}|Error: {e}")
        _tests_failed += 1

    # Test 4: One stair
    _t4_input = "n=1"
    _t4_expected = 1
    try:
        result = climb_stairs(1)
        assert result == _t4_expected, f"Expected {_t4_expected}, got {result}"
        print("✓ Test 4 passed: One stair")
        _tests_passed += 1
    except AssertionError as e:
        print(f"✗ Test 4 failed: {e}")
        print(f"__TD__|{_t4_input}|{_t4_expected}|{result}")
        _tests_failed += 1
    except Exception as e:
        print(f"✗ Test 4 error: {e}")
        print(f"__TD__|{_t4_input}|{_t4_expected}|Error: {e}")
        _tests_failed += 1

    # Test 5: Larger number
    _t5_input = "n=10"
    _t5_expected = 89
    try:
        result = climb_stairs(10)
        assert result == _t5_expected, f"Expected {_t5_expected}, got {result}"
        print("✓ Test 5 passed: Larger number")
        _tests_passed += 1
    except AssertionError as e:
        print(f"✗ Test 5 failed: {e}")
        print(f"__TD__|{_t5_input}|{_t5_expected}|{result}")
        _tests_failed += 1
    except Exception as e:
        print(f"✗ Test 5 error: {e}")
        print(f"__TD__|{_t5_input}|{_t5_expected}|Error: {e}")
        _tests_failed += 1

    # Test 6: Even larger
    _t6_input = "n=20"
    _t6_expected = 10946
    try:
        result = climb_stairs(20)
        assert result == _t6_expected, f"Expected {_t6_expected}, got {result}"
        print("✓ Test 6 passed: Even larger")
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
