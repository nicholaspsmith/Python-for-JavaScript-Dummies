"""
Merge Two Sorted Lists
=======================

Merge two sorted linked lists into one sorted list. The list should be made by
splicing together the nodes of the first two lists.

You're given the heads of two sorted linked lists `list1` and `list2`.
Return the head of the merged sorted list.

Example:
    Input: list1 = [1,2,4], list2 = [1,3,4]
    Output: [1,1,2,3,4,4]

    Input: list1 = [], list2 = [0]
    Output: [0]

JS to Python Tips:
-----------------
- Python classes use `class Name:` (no parentheses needed for no inheritance).
- Constructor is `def __init__(self, args):` (not `constructor()`).
- All instance methods take `self` as first parameter (like implicit `this`).
- `None` is Python's `null`. Check with `if node is None:` or `if not node:`.
- No `new` keyword: just call `ListNode(5)` to create an instance.
- Linked list patterns are the same as JS - track pointers and reassign .next.

The dummy node pattern is useful: create a dummy head, build the list, return dummy.next.
"""


class ListNode:
    def __init__(self, val: int = 0, next: 'ListNode' = None):
        self.val = val
        self.next = next


'''HINTS
{
  "hint1": "def merge_two_lists(list1: ListNode, list2: ListNode) -> ListNode:\\n    # Create a dummy node to simplify list building\\n    dummy = ListNode()\\n    current = dummy\\n    # Your code here: compare and link nodes\\n    ...",
  "hint2": "def merge_two_lists(list1: ListNode, list2: ListNode) -> ListNode:\\n    # 1. Create dummy node and current pointer\\n    # 2. While both list1 and list2 have nodes:\\n    #    - Compare list1.val and list2.val\\n    #    - Link current.next to the smaller node\\n    #    - Advance that list's pointer\\n    #    - Advance current pointer\\n    # 3. Link remaining nodes (one list may have leftovers)\\n    # 4. Return dummy.next (skip the dummy head)\\n    ...",
  "solution": "def merge_two_lists(list1: ListNode, list2: ListNode) -> ListNode:\\n    dummy = ListNode()\\n    current = dummy\\n    \\n    while list1 and list2:\\n        if list1.val <= list2.val:\\n            current.next = list1\\n            list1 = list1.next\\n        else:\\n            current.next = list2\\n            list2 = list2.next\\n        current = current.next\\n    \\n    # Append remaining nodes\\n    current.next = list1 if list1 else list2\\n    \\n    return dummy.next"
}
HINTS'''


def merge_two_lists(list1: ListNode, list2: ListNode) -> ListNode:
    """Merge two sorted linked lists and return the merged list's head."""
    # Your code here
    ...


# Helper functions for testing
def list_to_linked(arr):
    """Convert a Python list to a linked list."""
    if not arr:
        return None
    head = ListNode(arr[0])
    current = head
    for val in arr[1:]:
        current.next = ListNode(val)
        current = current.next
    return head


def linked_to_list(head):
    """Convert a linked list to a Python list."""
    result = []
    while head:
        result.append(head.val)
        head = head.next
    return result


# ============= TESTS =============
if __name__ == "__main__":
    _tests_passed = 0
    _tests_failed = 0

    # Test 1: Basic merge
    _t1_input = "list1=[1,2,4], list2=[1,3,4]"
    _t1_expected = [1, 1, 2, 3, 4, 4]
    try:
        l1 = list_to_linked([1, 2, 4])
        l2 = list_to_linked([1, 3, 4])
        result = linked_to_list(merge_two_lists(l1, l2))
        assert result == _t1_expected, f"Expected {_t1_expected}, got {result}"
        print("✓ Test 1 passed: Basic merge")
        _tests_passed += 1
    except AssertionError as e:
        print(f"✗ Test 1 failed: {e}")
        print(f"__TD__|{_t1_input}|{_t1_expected}|{result}")
        _tests_failed += 1
    except Exception as e:
        print(f"✗ Test 1 error: {e}")
        print(f"__TD__|{_t1_input}|{_t1_expected}|Error: {e}")
        _tests_failed += 1

    # Test 2: Empty first list
    _t2_input = "list1=[], list2=[0]"
    _t2_expected = [0]
    try:
        l1 = list_to_linked([])
        l2 = list_to_linked([0])
        result = linked_to_list(merge_two_lists(l1, l2))
        assert result == _t2_expected, f"Expected {_t2_expected}, got {result}"
        print("✓ Test 2 passed: Empty first list")
        _tests_passed += 1
    except AssertionError as e:
        print(f"✗ Test 2 failed: {e}")
        print(f"__TD__|{_t2_input}|{_t2_expected}|{result}")
        _tests_failed += 1
    except Exception as e:
        print(f"✗ Test 2 error: {e}")
        print(f"__TD__|{_t2_input}|{_t2_expected}|Error: {e}")
        _tests_failed += 1

    # Test 3: Both empty
    _t3_input = "list1=[], list2=[]"
    _t3_expected = []
    try:
        l1 = list_to_linked([])
        l2 = list_to_linked([])
        result = linked_to_list(merge_two_lists(l1, l2))
        assert result == _t3_expected, f"Expected {_t3_expected}, got {result}"
        print("✓ Test 3 passed: Both empty")
        _tests_passed += 1
    except AssertionError as e:
        print(f"✗ Test 3 failed: {e}")
        print(f"__TD__|{_t3_input}|{_t3_expected}|{result}")
        _tests_failed += 1
    except Exception as e:
        print(f"✗ Test 3 error: {e}")
        print(f"__TD__|{_t3_input}|{_t3_expected}|Error: {e}")
        _tests_failed += 1

    # Test 4: Different lengths
    _t4_input = "list1=[1,2,3,4,5], list2=[2,4]"
    _t4_expected = [1, 2, 2, 3, 4, 4, 5]
    try:
        l1 = list_to_linked([1, 2, 3, 4, 5])
        l2 = list_to_linked([2, 4])
        result = linked_to_list(merge_two_lists(l1, l2))
        assert result == _t4_expected, f"Expected {_t4_expected}, got {result}"
        print("✓ Test 4 passed: Different lengths")
        _tests_passed += 1
    except AssertionError as e:
        print(f"✗ Test 4 failed: {e}")
        print(f"__TD__|{_t4_input}|{_t4_expected}|{result}")
        _tests_failed += 1
    except Exception as e:
        print(f"✗ Test 4 error: {e}")
        print(f"__TD__|{_t4_input}|{_t4_expected}|Error: {e}")
        _tests_failed += 1

    # Summary
    print()
    if _tests_failed == 0:
        print(f"🎉 All {_tests_passed} tests passed!")
    else:
        print(f"❌ {_tests_passed}/{_tests_passed + _tests_failed} tests passed")
