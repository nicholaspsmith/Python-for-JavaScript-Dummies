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


def merge_two_lists(list1: ListNode, list2: ListNode) -> ListNode:
    """
    Merge two sorted linked lists and return the merged list's head.

    Hint: Use a dummy node to simplify edge cases.
    Compare values from each list, append the smaller one, advance that pointer.
    """
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
    print("Running tests...")

    # Test 1: Basic merge
    l1 = list_to_linked([1, 2, 4])
    l2 = list_to_linked([1, 3, 4])
    result = linked_to_list(merge_two_lists(l1, l2))
    assert result == [1, 1, 2, 3, 4, 4], f"Expected [1,1,2,3,4,4], got {result}"
    print("✓ Exercise 1.1 passed: Basic merge")

    # Test 2: Empty first list
    l1 = list_to_linked([])
    l2 = list_to_linked([0])
    result = linked_to_list(merge_two_lists(l1, l2))
    assert result == [0], f"Expected [0], got {result}"
    print("✓ Exercise 1.2 passed: Empty first list")

    # Test 3: Both empty
    l1 = list_to_linked([])
    l2 = list_to_linked([])
    result = linked_to_list(merge_two_lists(l1, l2))
    assert result == [], f"Expected [], got {result}"
    print("✓ Exercise 1.3 passed: Both empty")

    # Test 4: Different lengths
    l1 = list_to_linked([1, 2, 3, 4, 5])
    l2 = list_to_linked([2, 4])
    result = linked_to_list(merge_two_lists(l1, l2))
    assert result == [1, 2, 2, 3, 4, 4, 5], f"Expected [1,2,2,3,4,4,5], got {result}"
    print("✓ Exercise 1.4 passed: Different lengths")

    print("\n🎉 All tests passed!")
