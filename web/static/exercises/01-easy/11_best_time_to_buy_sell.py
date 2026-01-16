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


def max_profit(prices: List[int]) -> int:
    """
    Find the maximum profit from buying and selling once.

    Hint: Track min_price seen so far. At each day, the profit would be
    prices[i] - min_price. Track the maximum of these profits.
    """
    # Your code here
    ...


# ============= TESTS =============
if __name__ == "__main__":
    print("Running tests...")

    # Test 1: Normal case with profit
    assert max_profit([7, 1, 5, 3, 6, 4]) == 5
    print("✓ Exercise 1.1 passed: [7,1,5,3,6,4] -> profit 5")

    # Test 2: Decreasing prices
    assert max_profit([7, 6, 4, 3, 1]) == 0
    print("✓ Exercise 1.2 passed: Decreasing prices -> 0")

    # Test 3: Two elements with profit
    assert max_profit([1, 2]) == 1
    print("✓ Exercise 1.3 passed: [1,2] -> profit 1")

    # Test 4: Two elements no profit
    assert max_profit([2, 1]) == 0
    print("✓ Exercise 1.4 passed: [2,1] -> no profit")

    # Test 5: All same prices
    assert max_profit([3, 3, 3, 3]) == 0
    print("✓ Exercise 1.5 passed: Same prices -> 0")

    # Test 6: Single element
    assert max_profit([5]) == 0
    print("✓ Exercise 1.6 passed: Single element -> 0")

    print("\n🎉 All tests passed!")
