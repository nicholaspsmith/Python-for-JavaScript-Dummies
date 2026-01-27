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


'''HINTS
{
  "hint1": "def majority_element(nums: List[int]) -> int:\\n    # Use Boyer-Moore voting algorithm\\n    # Track a candidate and a count variable",
  "hint2": "def majority_element(nums: List[int]) -> int:\\n    # 1) Initialize candidate = None, count = 0\\n    # 2) For each num in nums:\\n    #    - If count == 0, set candidate = num\\n    #    - If num == candidate, increment count\\n    #    - Else decrement count\\n    # 3) Return candidate",
  "solution": "def majority_element(nums: List[int]) -> int:\\n    candidate = None\\n    count = 0\\n    for num in nums:\\n        if count == 0:\\n            candidate = num\\n        count += 1 if num == candidate else -1\\n    return candidate"
}
HINTS'''


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
    _t1_input = "nums=[3, 2, 3]"
    _t1_expected = 3
    try:
        result = majority_element([3, 2, 3])
        assert result == _t1_expected, f"Expected {_t1_expected}, got {result}"
        print("✓ Test 1 passed: Simple majority")
        _tests_passed += 1
    except AssertionError as e:
        print(f"✗ Test 1 failed: {e}")
        print(f"__TD__|{_t1_input}|{_t1_expected}|{result}")
        _tests_failed += 1
    except Exception as e:
        print(f"✗ Test 1 error: {e}")
        print(f"__TD__|{_t1_input}|{_t1_expected}|Error: {e}")
        _tests_failed += 1

    # Test 2: Longer array
    _t2_input = "nums=[2, 2, 1, 1, 1, 2, 2]"
    _t2_expected = 2
    try:
        result = majority_element([2, 2, 1, 1, 1, 2, 2])
        assert result == _t2_expected, f"Expected {_t2_expected}, got {result}"
        print("✓ Test 2 passed: Longer array")
        _tests_passed += 1
    except AssertionError as e:
        print(f"✗ Test 2 failed: {e}")
        print(f"__TD__|{_t2_input}|{_t2_expected}|{result}")
        _tests_failed += 1
    except Exception as e:
        print(f"✗ Test 2 error: {e}")
        print(f"__TD__|{_t2_input}|{_t2_expected}|Error: {e}")
        _tests_failed += 1

    # Test 3: Single element
    _t3_input = "nums=[1]"
    _t3_expected = 1
    try:
        result = majority_element([1])
        assert result == _t3_expected, f"Expected {_t3_expected}, got {result}"
        print("✓ Test 3 passed: Single element")
        _tests_passed += 1
    except AssertionError as e:
        print(f"✗ Test 3 failed: {e}")
        print(f"__TD__|{_t3_input}|{_t3_expected}|{result}")
        _tests_failed += 1
    except Exception as e:
        print(f"✗ Test 3 error: {e}")
        print(f"__TD__|{_t3_input}|{_t3_expected}|Error: {e}")
        _tests_failed += 1

    # Test 4: All same
    _t4_input = "nums=[5, 5, 5]"
    _t4_expected = 5
    try:
        result = majority_element([5, 5, 5])
        assert result == _t4_expected, f"Expected {_t4_expected}, got {result}"
        print("✓ Test 4 passed: All same")
        _tests_passed += 1
    except AssertionError as e:
        print(f"✗ Test 4 failed: {e}")
        print(f"__TD__|{_t4_input}|{_t4_expected}|{result}")
        _tests_failed += 1
    except Exception as e:
        print(f"✗ Test 4 error: {e}")
        print(f"__TD__|{_t4_input}|{_t4_expected}|Error: {e}")
        _tests_failed += 1

    # Test 5: Two elements
    _t5_input = "nums=[1, 1]"
    _t5_expected = 1
    try:
        result = majority_element([1, 1])
        assert result == _t5_expected, f"Expected {_t5_expected}, got {result}"
        print("✓ Test 5 passed: Two elements")
        _tests_passed += 1
    except AssertionError as e:
        print(f"✗ Test 5 failed: {e}")
        print(f"__TD__|{_t5_input}|{_t5_expected}|{result}")
        _tests_failed += 1
    except Exception as e:
        print(f"✗ Test 5 error: {e}")
        print(f"__TD__|{_t5_input}|{_t5_expected}|Error: {e}")
        _tests_failed += 1

    # Test 6: Large majority
    _t6_input = "nums=[1, 1, 1, 1, 2]"
    _t6_expected = 1
    try:
        result = majority_element([1, 1, 1, 1, 2])
        assert result == _t6_expected, f"Expected {_t6_expected}, got {result}"
        print("✓ Test 6 passed: Large majority")
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
