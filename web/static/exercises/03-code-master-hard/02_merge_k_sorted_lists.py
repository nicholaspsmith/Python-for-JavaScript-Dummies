"""
Merge k Sorted Lists
=====================

You are given an array of k linked lists, each sorted in ascending order.
Merge all the linked lists into one sorted linked list and return it.

Example:
    Input: lists = [[1,4,5],[1,3,4],[2,6]]
    Output: [1,1,2,3,4,4,5,6]

    Input: lists = []
    Output: []

    Input: lists = [[]]
    Output: []

JS to Python Tips:
-----------------
- `heapq` module provides heap operations (priority queue).
- `heapq.heappush(heap, item)` and `heapq.heappop(heap)`.
- Heap in Python is a min-heap by default (smallest element first).
- Tuples compare element by element, so `(val, id, node)` compares by val first.
  The id is needed as a tiebreaker since ListNode isn't comparable.
- `enumerate()` gives you (index, value) pairs for unique tiebreakers.
- Alternative: Divide and conquer - merge pairs recursively.

Heap Approach O(n log k):
1. Add the first node from each list to a min-heap.
2. Pop the smallest, add it to result.
3. If that node has a next, push next to heap.
4. Repeat until heap is empty.

Since Python's heapq doesn't have a key function, we push tuples:
(node.val, unique_index, node) to ensure proper comparison.

Divide and Conquer O(n log k):
- Pair up lists and merge each pair.
- Repeat until one list remains.
"""

from typing import List, Optional
import heapq


class ListNode:
    def __init__(self, val: int = 0, next: 'ListNode' = None):
        self.val = val
        self.next = next


def merge_k_lists(lists: List[Optional[ListNode]]) -> Optional[ListNode]:
    """
    Merge k sorted linked lists into one sorted list.

    Hint: Use a min-heap. Push (value, index, node) tuples.
    Pop smallest, add to result, push its next if exists.
    The index acts as a tiebreaker for nodes with equal values.
    """
    # Your code here
    ...


# Helper functions for testing
def list_to_linked(arr):
    if not arr:
        return None
    head = ListNode(arr[0])
    current = head
    for val in arr[1:]:
        current.next = ListNode(val)
        current = current.next
    return head


def linked_to_list(head):
    result = []
    while head:
        result.append(head.val)
        head = head.next
    return result


# ============= TESTS =============
if __name__ == "__main__":
    _tests_passed = 0
    _tests_failed = 0

    # Test 1: Three lists
    try:
        lists = [
        list_to_linked([1, 4, 5]),
        list_to_linked([1, 3, 4]),
        list_to_linked([2, 6])
        ]
        result = linked_to_list(merge_k_lists(lists))
        assert result == [1, 1, 2, 3, 4, 4, 5, 6], f"Got {result}"
        print("✓ Test 1 passed: Three lists")
        _tests_passed += 1
    except AssertionError as e:
        print(f"✗ Test 1 failed: {e}")
        _tests_failed += 1
    except Exception as e:
        print(f"✗ Test 1 error: {e}")
        _tests_failed += 1

    # Test 2: Empty input
    try:
        result = linked_to_list(merge_k_lists([]))
        assert result == [], f"Got {result}"
        print("✓ Test 2 passed: Empty input")
        _tests_passed += 1
    except AssertionError as e:
        print(f"✗ Test 2 failed: {e}")
        _tests_failed += 1
    except Exception as e:
        print(f"✗ Test 2 error: {e}")
        _tests_failed += 1

    # Test 3: Single empty list
    try:
        result = linked_to_list(merge_k_lists([None]))
        assert result == [], f"Got {result}"
        print("✓ Test 3 passed: Single empty list")
        _tests_passed += 1
    except AssertionError as e:
        print(f"✗ Test 3 failed: {e}")
        _tests_failed += 1
    except Exception as e:
        print(f"✗ Test 3 error: {e}")
        _tests_failed += 1

    # Test 4: Single list
    try:
        result = linked_to_list(merge_k_lists([list_to_linked([1, 2, 3])]))
        assert result == [1, 2, 3], f"Got {result}"
        print("✓ Test 4 passed: Single list")
        _tests_passed += 1
    except AssertionError as e:
        print(f"✗ Test 4 failed: {e}")
        _tests_failed += 1
    except Exception as e:
        print(f"✗ Test 4 error: {e}")
        _tests_failed += 1

    # Test 5: Two lists
    try:
        lists = [list_to_linked([1, 3, 5]), list_to_linked([2, 4, 6])]
        result = linked_to_list(merge_k_lists(lists))
        assert result == [1, 2, 3, 4, 5, 6], f"Got {result}"
        print("✓ Test 5 passed: Two lists")
        _tests_passed += 1
    except AssertionError as e:
        print(f"✗ Test 5 failed: {e}")
        _tests_failed += 1
    except Exception as e:
        print(f"✗ Test 5 error: {e}")
        _tests_failed += 1

    # Test 6: Some empty lists
    try:
        lists = [None, list_to_linked([1]), None, list_to_linked([2])]
        result = linked_to_list(merge_k_lists(lists))
        assert result == [1, 2], f"Got {result}"
        print("✓ Test 6 passed: Some empty lists")
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
