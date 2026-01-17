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
    try:

        assert climb_stairs(2) == 2, "2 stairs should have 2 ways"
        print("✓ Test 1 passed: Two stairs")
        _tests_passed += 1
    except AssertionError as e:
        print(f"✗ Test 1 failed: {e}")
        _tests_failed += 1
    except Exception as e:
        print(f"✗ Test 1 error: {e}")
        _tests_failed += 1

    # Test 2: Three stairs
    try:

        assert climb_stairs(3) == 3, "3 stairs should have 3 ways"
        print("✓ Test 2 passed: Three stairs")
        _tests_passed += 1
    except AssertionError as e:
        print(f"✗ Test 2 failed: {e}")
        _tests_failed += 1
    except Exception as e:
        print(f"✗ Test 2 error: {e}")
        _tests_failed += 1

    # Test 3: Four stairs
    try:

        assert climb_stairs(4) == 5, "4 stairs should have 5 ways"
        print("✓ Test 3 passed: Four stairs")
        _tests_passed += 1
    except AssertionError as e:
        print(f"✗ Test 3 failed: {e}")
        _tests_failed += 1
    except Exception as e:
        print(f"✗ Test 3 error: {e}")
        _tests_failed += 1

    # Test 4: One stair
    try:

        assert climb_stairs(1) == 1, "1 stair should have 1 way"
        print("✓ Test 4 passed: One stair")
        _tests_passed += 1
    except AssertionError as e:
        print(f"✗ Test 4 failed: {e}")
        _tests_failed += 1
    except Exception as e:
        print(f"✗ Test 4 error: {e}")
        _tests_failed += 1

    # Test 5: Larger number
    try:

        assert climb_stairs(10) == 89, "10 stairs should have 89 ways"
        print("✓ Test 5 passed: Larger number")
        _tests_passed += 1
    except AssertionError as e:
        print(f"✗ Test 5 failed: {e}")
        _tests_failed += 1
    except Exception as e:
        print(f"✗ Test 5 error: {e}")
        _tests_failed += 1

    # Test 6: Even larger
    try:

        assert climb_stairs(20) == 10946, "20 stairs should have 10946 ways"
        print("✓ Test 6 passed: Even larger")
        _tests_passed += 1
    except AssertionError as e:
        print(f"✗ Test 6 failed: {e}")
        _tests_failed += 1
    except Exception as e:
        print(f"✗ Test 6 error: {e}")
        _tests_failed += 1

    # Summary
    print()
    if _tests_failed == 0:
        print(f"🎉 All {_tests_passed} tests passed!")
    else:
        print(f"❌ {_tests_passed}/{_tests_passed + _tests_failed} tests passed")
