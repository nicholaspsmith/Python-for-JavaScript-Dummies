"""
Add Two Numbers
================

You are given two non-empty linked lists representing two non-negative integers.
The digits are stored in reverse order, and each node contains a single digit.
Add the two numbers and return the sum as a linked list.

Example:
    Input: l1 = [2,4,3], l2 = [5,6,4]
    Output: [7,0,8]
    Explanation: 342 + 465 = 807 (stored in reverse)

    Input: l1 = [9,9,9,9], l2 = [9,9,9,9]
    Output: [8,9,9,9,1]
    Explanation: 9999 + 9999 = 19998

JS to Python Tips:
-----------------
- Integer division: `carry = total // 10` (double slash for floor division).
- Modulo: `digit = total % 10` (same as JS).
- `divmod(total, 10)` returns (quotient, remainder) tuple - Pythonic!
  Example: `carry, digit = divmod(total, 10)`
- Linked list traversal: `while l1 or l2 or carry:` handles all cases.
- Ternary: `val = l1.val if l1 else 0` (JS: `val = l1 ? l1.val : 0`).
- Python's `or` returns first truthy value: `l1 or l2` returns l1 if truthy.

Approach:
- Iterate through both lists simultaneously.
- Add corresponding digits plus any carry.
- Create new node for each digit of result.
- Don't forget the final carry!
"""


class ListNode:
    def __init__(self, val: int = 0, next: 'ListNode' = None):
        self.val = val
        self.next = next


'''HINTS
{
  "hint1": "def add_two_numbers(l1: ListNode, l2: ListNode) -> ListNode:\\n    dummy = ListNode(0)\\n    current = dummy\\n    carry = 0",
  "hint2": "1) Create dummy node and current pointer, set carry=0\\n2) While l1 or l2 or carry:\\n   - Get val1 = l1.val if l1 else 0\\n   - Get val2 = l2.val if l2 else 0\\n   - Calculate total = val1 + val2 + carry\\n   - Create new node with total % 10\\n   - Update carry = total // 10\\n   - Move pointers forward\\n3) Return dummy.next",
  "solution": "def add_two_numbers(l1: ListNode, l2: ListNode) -> ListNode:\\n    dummy = ListNode(0)\\n    current = dummy\\n    carry = 0\\n\\n    while l1 or l2 or carry:\\n        val1 = l1.val if l1 else 0\\n        val2 = l2.val if l2 else 0\\n        total = val1 + val2 + carry\\n\\n        carry, digit = divmod(total, 10)\\n        current.next = ListNode(digit)\\n        current = current.next\\n\\n        if l1:\\n            l1 = l1.next\\n        if l2:\\n            l2 = l2.next\\n\\n    return dummy.next"
}
HINTS'''


def add_two_numbers(l1: ListNode, l2: ListNode) -> ListNode:
    """
    Add two numbers represented as reversed linked lists.

    Hint: Use a dummy head. Iterate while either list has nodes OR there's a carry.
    Use divmod(sum, 10) to get (carry, digit) at each step.
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

    # Test 1: Basic addition
    _t1_input = "l1=[2,4,3], l2=[5,6,4]"
    _t1_expected = [7, 0, 8]
    try:
        l1 = list_to_linked([2, 4, 3])  # 342
        l2 = list_to_linked([5, 6, 4])  # 465
        result = linked_to_list(add_two_numbers(l1, l2))
        assert result == _t1_expected, f"Expected {_t1_expected}, got {result}"
        print("✓ Test 1 passed: Basic addition")
        _tests_passed += 1
    except AssertionError as e:
        print(f"✗ Test 1 failed: {e}")
        print(f"__TD__|{_t1_input}|{_t1_expected}|{result}")
        _tests_failed += 1
    except Exception as e:
        print(f"✗ Test 1 error: {e}")
        print(f"__TD__|{_t1_input}|{_t1_expected}|Error: {e}")
        _tests_failed += 1

    # Test 2: Large numbers with carry
    _t2_input = "l1=[9,9,9,9], l2=[9,9,9,9]"
    _t2_expected = [8, 9, 9, 9, 1]
    try:
        l1 = list_to_linked([9, 9, 9, 9])  # 9999
        l2 = list_to_linked([9, 9, 9, 9])  # 9999
        result = linked_to_list(add_two_numbers(l1, l2))
        assert result == _t2_expected, f"Expected {_t2_expected}, got {result}"
        print("✓ Test 2 passed: Large numbers with carry")
        _tests_passed += 1
    except AssertionError as e:
        print(f"✗ Test 2 failed: {e}")
        print(f"__TD__|{_t2_input}|{_t2_expected}|{result}")
        _tests_failed += 1
    except Exception as e:
        print(f"✗ Test 2 error: {e}")
        print(f"__TD__|{_t2_input}|{_t2_expected}|Error: {e}")
        _tests_failed += 1

    # Test 3: Zeros
    _t3_input = "l1=[0], l2=[0]"
    _t3_expected = [0]
    try:
        l1 = list_to_linked([0])
        l2 = list_to_linked([0])
        result = linked_to_list(add_two_numbers(l1, l2))
        assert result == _t3_expected, f"Expected {_t3_expected}, got {result}"
        print("✓ Test 3 passed: Zeros")
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
    _t4_input = "l1=[9,9], l2=[1]"
    _t4_expected = [0, 0, 1]
    try:
        l1 = list_to_linked([9, 9])
        l2 = list_to_linked([1])
        result = linked_to_list(add_two_numbers(l1, l2))
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
