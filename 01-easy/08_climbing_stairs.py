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
    print("Running tests...")

    # Test 1: Two stairs
    assert climb_stairs(2) == 2, "2 stairs should have 2 ways"
    print("✓ Test 1 passed: n=2 -> 2 ways")

    # Test 2: Three stairs
    assert climb_stairs(3) == 3, "3 stairs should have 3 ways"
    print("✓ Test 2 passed: n=3 -> 3 ways")

    # Test 3: Four stairs
    assert climb_stairs(4) == 5, "4 stairs should have 5 ways"
    print("✓ Test 3 passed: n=4 -> 5 ways")

    # Test 4: One stair
    assert climb_stairs(1) == 1, "1 stair should have 1 way"
    print("✓ Test 4 passed: n=1 -> 1 way")

    # Test 5: Larger number
    assert climb_stairs(10) == 89, "10 stairs should have 89 ways"
    print("✓ Test 5 passed: n=10 -> 89 ways")

    # Test 6: Even larger
    assert climb_stairs(20) == 10946, "20 stairs should have 10946 ways"
    print("✓ Test 6 passed: n=20 -> 10946 ways")

    print("\n🎉 All tests passed!")
