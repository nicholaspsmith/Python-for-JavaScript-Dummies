"""
Longest Substring Without Repeating Characters
================================================

Given a string s, find the length of the longest substring without repeating characters.

Example:
    Input: s = "abcabcbb"
    Output: 3 (The answer is "abc")

    Input: s = "bbbbb"
    Output: 1 (The answer is "b")

    Input: s = "pwwkew"
    Output: 3 (The answer is "wke")

JS to Python Tips:
-----------------
- `set()` is like JS `Set` - O(1) add/remove/lookup.
- Set operations: `seen.add(x)`, `seen.remove(x)`, `x in seen`.
- `seen.discard(x)` removes if present (no error if missing).
- `max(a, b)` instead of `Math.max(a, b)`.
- Sliding window: expand right, shrink left when duplicate found.

Sliding Window Pattern:
- Use two pointers: left (start of window) and right (expanding).
- Use a set to track characters in current window.
- When you find a duplicate, shrink from left until it's removed.
- Track the maximum window size seen.

Dict alternative: Store char -> index for O(1) jump to after duplicate.
"""


def length_of_longest_substring(s: str) -> int:
    """
    Find length of longest substring without repeating characters.

    Hint: Sliding window with a set. Expand right, when duplicate found,
    shrink left until duplicate is removed. Track max length.
    """
    # Your code here
    ...


# ============= TESTS =============
if __name__ == "__main__":
    print("Running tests...")

    # Test 1: Normal case
    assert length_of_longest_substring("abcabcbb") == 3
    print("✓ Exercise 2.1 passed: 'abcabcbb' -> 3")

    # Test 2: All same
    assert length_of_longest_substring("bbbbb") == 1
    print("✓ Exercise 2.2 passed: 'bbbbb' -> 1")

    # Test 3: Repeat in middle
    assert length_of_longest_substring("pwwkew") == 3
    print("✓ Exercise 2.3 passed: 'pwwkew' -> 3")

    # Test 4: Empty string
    assert length_of_longest_substring("") == 0
    print("✓ Exercise 2.4 passed: Empty string -> 0")

    # Test 5: Single char
    assert length_of_longest_substring("a") == 1
    print("✓ Exercise 2.5 passed: Single char -> 1")

    # Test 6: All unique
    assert length_of_longest_substring("abcdef") == 6
    print("✓ Exercise 2.6 passed: All unique -> 6")

    # Test 7: Space character
    assert length_of_longest_substring("a b c") == 3
    print("✓ Exercise 2.7 passed: With spaces")

    print("\n🎉 All tests passed!")
