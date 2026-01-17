"""
Majority Element
=================

Given an array `nums` of size n, return the majority element.

The majority element is the element that appears more than n/2 times.
You may assume the majority element always exists in the array.

Example:
    Input: nums = [3,2,3]
    Output: 3

    Input: nums = [2,2,1,1,1,2,2]
    Output: 2

JS to Python Tips:
-----------------
- `collections.Counter` is like a specialized dict for counting (no JS equivalent).
  Usage: `from collections import Counter; counts = Counter(nums)`
  Then `counts.most_common(1)` returns [(element, count)] for the most frequent.
- Dict comprehension: `{x: nums.count(x) for x in set(nums)}` (but O(n^2)!).
- Boyer-Moore Voting Algorithm works in O(n) time, O(1) space - no extra data structures!
- `//` is integer division: `len(nums) // 2` (JS uses `Math.floor(len / 2)`).

Boyer-Moore Algorithm:
- Keep a candidate and a count.
- When count is 0, pick current element as new candidate.
- If current equals candidate, increment count; else decrement.
- The majority element will survive because it has more than n/2 occurrences.
"""

from typing import List


def majority_element(nums: List[int]) -> int:
    """
    Find the element that appears more than n/2 times.

    Hint: Use Boyer-Moore Voting: maintain a candidate and count.
    When count hits 0, switch candidate. The majority will always win.

    Or simpler: use collections.Counter and find the most common.
    """
    # Your code here
    ...


# ============= TESTS =============
if __name__ == "__main__":
    _tests_passed = 0
    _tests_failed = 0

    # Test 1: Simple majority
    try:

        assert majority_element([3, 2, 3]) == 3
        print("✓ Test 1 passed: Simple majority")
        _tests_passed += 1
    except AssertionError as e:
        print(f"✗ Test 1 failed: {e}")
        _tests_failed += 1
    except Exception as e:
        print(f"✗ Test 1 error: {e}")
        _tests_failed += 1

    # Test 2: Longer array
    try:

        assert majority_element([2, 2, 1, 1, 1, 2, 2]) == 2
        print("✓ Test 2 passed: Longer array")
        _tests_passed += 1
    except AssertionError as e:
        print(f"✗ Test 2 failed: {e}")
        _tests_failed += 1
    except Exception as e:
        print(f"✗ Test 2 error: {e}")
        _tests_failed += 1

    # Test 3: Single element
    try:

        assert majority_element([1]) == 1
        print("✓ Test 3 passed: Single element")
        _tests_passed += 1
    except AssertionError as e:
        print(f"✗ Test 3 failed: {e}")
        _tests_failed += 1
    except Exception as e:
        print(f"✗ Test 3 error: {e}")
        _tests_failed += 1

    # Test 4: All same
    try:

        assert majority_element([5, 5, 5]) == 5
        print("✓ Test 4 passed: All same")
        _tests_passed += 1
    except AssertionError as e:
        print(f"✗ Test 4 failed: {e}")
        _tests_failed += 1
    except Exception as e:
        print(f"✗ Test 4 error: {e}")
        _tests_failed += 1

    # Test 5: Two elements
    try:

        assert majority_element([1, 1]) == 1
        print("✓ Test 5 passed: Two elements")
        _tests_passed += 1
    except AssertionError as e:
        print(f"✗ Test 5 failed: {e}")
        _tests_failed += 1
    except Exception as e:
        print(f"✗ Test 5 error: {e}")
        _tests_failed += 1

    # Test 6: Large majority
    try:

        assert majority_element([1, 1, 1, 1, 2]) == 1
        print("✓ Test 6 passed: Large majority")
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
