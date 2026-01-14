"""
Exercise 1: File I/O
=====================

Python file operations are more straightforward than Node.js.

Node.js:
    const fs = require('fs');
    const data = fs.readFileSync('file.txt', 'utf-8');
    // or with promises
    const data = await fs.promises.readFile('file.txt', 'utf-8');

Python:
    with open('file.txt', 'r') as f:
        data = f.read()

Key differences:
- Python uses 'with' statement for automatic cleanup
- 'open()' returns a file object
- Modes: 'r' (read), 'w' (write), 'a' (append), 'rb'/'wb' (binary)
- Context manager handles closing automatically

EXERCISES:
Complete each exercise below. Run with: python3 01_file_operations.py
"""

import os
import json
from pathlib import Path

# Create a temp directory for our exercises
TEMP_DIR = Path(__file__).parent / "temp_files"
TEMP_DIR.mkdir(exist_ok=True)


# Exercise 1.1: Writing text files

def write_text_file(filepath, content):
    """
    Write content to a text file.
    Create the file if it doesn't exist, overwrite if it does.
    """
    # Use 'with open(filepath, "w") as f:'
    # YOUR CODE HERE
    pass


def append_to_file(filepath, content):
    """
    Append content to a text file.
    Create the file if it doesn't exist.
    """
    # Use mode 'a' for append
    # YOUR CODE HERE
    pass


# Exercise 1.2: Reading text files

def read_text_file(filepath):
    """
    Read and return entire file content as a string.
    Return None if file doesn't exist.
    """
    # YOUR CODE HERE
    pass


def read_lines(filepath):
    """
    Read file and return a list of lines (without newline characters).
    Return empty list if file doesn't exist.
    """
    # Hint: f.readlines() or f.read().splitlines()
    # YOUR CODE HERE
    pass


def read_first_n_lines(filepath, n):
    """
    Read and return the first n lines of a file.
    """
    # This is more memory efficient for large files
    # YOUR CODE HERE
    pass


# Exercise 1.3: Working with JSON files

def save_json(filepath, data):
    """
    Save data to a JSON file with nice formatting.
    Use indent=2 for readability.
    """
    # YOUR CODE HERE
    pass


def load_json(filepath):
    """
    Load and return data from a JSON file.
    Return None if file doesn't exist or JSON is invalid.
    """
    # YOUR CODE HERE
    pass


def update_json(filepath, updates):
    """
    Load JSON file, update with new key-value pairs, and save.
    If file doesn't exist, create it with just the updates.
    """
    # YOUR CODE HERE
    pass


# Exercise 1.4: File existence and info

def file_info(filepath):
    """
    Return a dict with file information:
    {
        "exists": bool,
        "size": int (bytes, or None if doesn't exist),
        "is_file": bool,
        "is_dir": bool
    }
    """
    # Use os.path or Path methods
    # YOUR CODE HERE
    pass


# Exercise 1.5: Working with paths (pathlib)
# pathlib is the modern way to handle paths in Python

def join_paths(*parts):
    """
    Join path parts using pathlib.
    Return as a Path object.
    """
    # Use Path and / operator
    # YOUR CODE HERE
    pass


def get_file_extension(filepath):
    """
    Return the file extension (including the dot).
    Example: "document.txt" -> ".txt"
    """
    # YOUR CODE HERE
    pass


def change_extension(filepath, new_ext):
    """
    Change file extension.
    Example: change_extension("doc.txt", ".md") -> Path("doc.md")
    """
    # Use Path.with_suffix()
    # YOUR CODE HERE
    pass


# Exercise 1.6: Directory operations

def list_files(directory, pattern="*"):
    """
    List files in directory matching pattern.
    Return list of Path objects.
    Pattern examples: "*.txt", "*.py", "*"
    """
    # Use Path.glob()
    # YOUR CODE HERE
    pass


def create_directory(path):
    """
    Create directory (and parent directories if needed).
    Don't raise error if already exists.
    """
    # YOUR CODE HERE
    pass


# Exercise 1.7: Reading file in chunks (memory efficient)

def count_words_in_large_file(filepath):
    """
    Count total words in a file, reading line by line.
    This is memory efficient for large files.
    """
    # Don't use f.read() - iterate over file object directly
    # YOUR CODE HERE
    pass


def find_in_file(filepath, search_term):
    """
    Find all lines containing search_term.
    Return list of (line_number, line_content) tuples.
    Line numbers start at 1.
    """
    # YOUR CODE HERE
    pass


# Exercise 1.8: Binary files

def copy_file(source, destination):
    """
    Copy a file (works for both text and binary).
    Read in chunks to handle large files.
    """
    chunk_size = 8192  # 8KB chunks

    # Use 'rb' and 'wb' modes for binary read/write
    # YOUR CODE HERE
    pass


# Exercise 1.9: Context manager cleanup guarantee

def safe_write(filepath, content):
    """
    Write to file with guaranteed cleanup.
    Even if an error occurs, the file should be properly closed.

    The 'with' statement guarantees this automatically.
    Return True if successful, False if any error occurred.
    """
    # YOUR CODE HERE
    pass


# ============= TESTS (Don't modify below) =============
if __name__ == "__main__":
    print("Running tests...")

    # Test 1.1
    test_file = TEMP_DIR / "test.txt"
    write_text_file(test_file, "Hello, World!")
    assert test_file.read_text() == "Hello, World!"
    append_to_file(test_file, "\nSecond line")
    assert "Second line" in test_file.read_text()
    print("✓ Exercise 1.1 passed")

    # Test 1.2
    write_text_file(test_file, "Line 1\nLine 2\nLine 3")
    assert read_text_file(test_file) == "Line 1\nLine 2\nLine 3"
    assert read_text_file(TEMP_DIR / "nonexistent.txt") is None
    assert read_lines(test_file) == ["Line 1", "Line 2", "Line 3"]
    assert read_first_n_lines(test_file, 2) == ["Line 1", "Line 2"]
    print("✓ Exercise 1.2 passed")

    # Test 1.3
    json_file = TEMP_DIR / "data.json"
    save_json(json_file, {"name": "Alice", "age": 30})
    loaded = load_json(json_file)
    assert loaded["name"] == "Alice"
    update_json(json_file, {"city": "NYC"})
    updated = load_json(json_file)
    assert updated["city"] == "NYC"
    assert updated["name"] == "Alice"
    print("✓ Exercise 1.3 passed")

    # Test 1.4
    info = file_info(test_file)
    assert info["exists"] == True
    assert info["is_file"] == True
    assert info["size"] > 0
    info2 = file_info(TEMP_DIR / "nope.txt")
    assert info2["exists"] == False
    print("✓ Exercise 1.4 passed")

    # Test 1.5
    assert join_paths("a", "b", "c") == Path("a/b/c")
    assert get_file_extension("document.txt") == ".txt"
    assert change_extension("doc.txt", ".md") == Path("doc.md")
    print("✓ Exercise 1.5 passed")

    # Test 1.6
    files = list_files(TEMP_DIR, "*.txt")
    assert len(files) >= 1
    new_dir = TEMP_DIR / "subdir"
    create_directory(new_dir)
    assert new_dir.exists()
    print("✓ Exercise 1.6 passed")

    # Test 1.7
    write_text_file(test_file, "one two three\nfour five\nsix")
    assert count_words_in_large_file(test_file) == 6
    write_text_file(test_file, "Line 1 has test\nLine 2\nLine 3 has test")
    found = find_in_file(test_file, "test")
    assert len(found) == 2
    assert found[0][0] == 1  # Line 1
    assert found[1][0] == 3  # Line 3
    print("✓ Exercise 1.7 passed")

    # Test 1.8
    source = TEMP_DIR / "source.txt"
    dest = TEMP_DIR / "dest.txt"
    write_text_file(source, "Copy this content")
    copy_file(source, dest)
    assert dest.read_text() == "Copy this content"
    print("✓ Exercise 1.8 passed")

    # Test 1.9
    assert safe_write(TEMP_DIR / "safe.txt", "Safe content") == True
    print("✓ Exercise 1.9 passed")

    # Cleanup
    import shutil
    shutil.rmtree(TEMP_DIR)

    print("\n🎉 All tests passed! Great job!")
