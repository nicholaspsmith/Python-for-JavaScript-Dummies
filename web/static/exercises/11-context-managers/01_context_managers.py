"""
Exercise 1: Context Managers
=============================

Context managers handle setup and cleanup automatically.
They work with the 'with' statement.

JavaScript has no direct equivalent, but try/finally is similar:
    try {
        const resource = acquire();
        // use resource
    } finally {
        resource.close();
    }

Python:
    with acquire() as resource:
        # use resource
    # automatically cleaned up

Context managers guarantee cleanup even if an exception occurs.

Two ways to create them:
1. Class with __enter__ and __exit__ methods
2. Generator with @contextmanager decorator

EXERCISES:
Complete each exercise below. Run with: python3 01_context_managers.py
"""

from contextlib import contextmanager
import time


# Exercise 1.1: Understanding the with statement

# The with statement calls __enter__ before the block
# and __exit__ after (even if an exception occurred)

class SimpleContext:
    """A simple context manager that tracks enter/exit."""

    def __init__(self, name):
        self.name = name
        self.entered = False
        self.exited = False

    def __enter__(self):
        """Called when entering 'with' block. Returns value for 'as' clause."""
        self.entered = True
        print(f"Entering {self.name}")
        return self  # This is what 'as x' binds to

    def __exit__(self, exc_type, exc_val, exc_tb):
        """
        Called when exiting 'with' block.
        exc_type, exc_val, exc_tb are exception info (None if no exception).
        Return True to suppress the exception, False to propagate it.
        """
        self.exited = True
        print(f"Exiting {self.name}")
        return False  # Don't suppress exceptions


# Exercise 1.2: Timer context manager (class-based)

class Timer:
    """
    A context manager that times code execution.

    Usage:
        with Timer() as t:
            # code to time
        print(t.elapsed)
    """

    def __init__(self):
        self.start = None
        self.end = None
        self.elapsed = None

    def __enter__(self):
        # YOUR CODE HERE
        # Record start time and return self
        pass

    def __exit__(self, exc_type, exc_val, exc_tb):
        # YOUR CODE HERE
        # Record end time and calculate elapsed
        pass


# Exercise 1.3: File-like context manager

class ManagedFile:
    """
    A context manager for file operations.
    Ensures file is always closed.

    Usage:
        with ManagedFile('test.txt', 'w') as f:
            f.write('hello')
    """

    def __init__(self, filename, mode='r'):
        self.filename = filename
        self.mode = mode
        self.file = None

    def __enter__(self):
        # YOUR CODE HERE
        # Open file and return it
        pass

    def __exit__(self, exc_type, exc_val, exc_tb):
        # YOUR CODE HERE
        # Close file if it's open
        pass


# Exercise 1.4: Context manager with exception handling

class SuppressErrors:
    """
    A context manager that suppresses specified exception types.

    Usage:
        with SuppressErrors(ValueError, KeyError):
            raise ValueError("This won't propagate")
        print("Continues here")
    """

    def __init__(self, *exceptions):
        self.exceptions = exceptions
        self.exception = None

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        # YOUR CODE HERE
        # If exc_type is in self.exceptions, suppress it (return True)
        # Store the exception in self.exception for inspection
        pass


# Exercise 1.5: Generator-based context manager

@contextmanager
def timer_context():
    """
    A timer context manager using @contextmanager decorator.

    Yields a dict that will contain {'elapsed': time} after the block.
    """
    result = {}
    start = time.time()
    try:
        yield result  # This is what 'as x' binds to
    finally:
        result['elapsed'] = time.time() - start


@contextmanager
def temporary_change(obj, attr, new_value):
    """
    Temporarily change an attribute, restore it afterwards.

    Usage:
        class Config:
            debug = False

        with temporary_change(Config, 'debug', True):
            print(Config.debug)  # True
        print(Config.debug)  # False
    """
    # YOUR CODE HERE
    # Save old value, set new value, yield, restore old value
    pass


# Exercise 1.6: Nested context managers

@contextmanager
def multi_open(*filenames):
    """
    Open multiple files and yield them as a list.
    All files are closed when exiting the context.

    Usage:
        with multi_open('file1.txt', 'file2.txt') as files:
            f1, f2 = files
    """
    # YOUR CODE HERE
    pass


# Exercise 1.7: Reentrant context manager

class ReentrantLock:
    """
    A context manager that can be entered multiple times.
    Tracks the depth of nesting.
    """

    def __init__(self):
        self.depth = 0
        self.max_depth = 0

    def __enter__(self):
        # YOUR CODE HERE
        # Increment depth, update max_depth, return self
        pass

    def __exit__(self, exc_type, exc_val, exc_tb):
        # YOUR CODE HERE
        # Decrement depth
        pass


# Exercise 1.8: Context manager for database transactions (simulated)

class Transaction:
    """
    A context manager that simulates database transactions.
    Commits on success, rolls back on exception.
    """

    def __init__(self, db):
        self.db = db
        self.committed = False
        self.rolled_back = False

    def __enter__(self):
        self.db.begin()
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        # YOUR CODE HERE
        # If no exception, commit. Otherwise, rollback.
        # Don't suppress exceptions (return False)
        pass


class MockDB:
    """Mock database for testing."""

    def __init__(self):
        self.operations = []

    def begin(self):
        self.operations.append('BEGIN')

    def commit(self):
        self.operations.append('COMMIT')

    def rollback(self):
        self.operations.append('ROLLBACK')


# Exercise 1.9: Context manager decorator pattern

@contextmanager
def tag(name):
    """
    A context manager that prints HTML-like tags.

    with tag('div'):
        print('content')

    Output:
        <div>
        content
        </div>
    """
    # YOUR CODE HERE
    pass


# Exercise 1.10: ExitStack for dynamic context management

from contextlib import ExitStack


def process_files(filenames):
    """
    Process multiple files, handling them all with ExitStack.
    ExitStack lets you dynamically add context managers.

    Returns list of file contents.
    """
    contents = []
    with ExitStack() as stack:
        # YOUR CODE HERE
        # Use stack.enter_context() for each file
        # Read all contents
        pass
    return contents


# ============= TESTS (Don't modify below) =============
if __name__ == "__main__":
    print("Running tests...")

    # Test 1.1
    ctx = SimpleContext("test")
    with ctx as c:
        assert c.entered == True
        assert c.exited == False
    assert ctx.exited == True
    print("✓ Exercise 1.1 passed")

    # Test 1.2
    with Timer() as t:
        time.sleep(0.1)
    assert t.elapsed is not None
    assert t.elapsed >= 0.1
    print("✓ Exercise 1.2 passed")

    # Test 1.3
    import tempfile
    import os
    with tempfile.NamedTemporaryFile(delete=False) as tmp:
        tmp_path = tmp.name
    try:
        with ManagedFile(tmp_path, 'w') as f:
            f.write('test')
        with ManagedFile(tmp_path, 'r') as f:
            assert f.read() == 'test'
    finally:
        os.unlink(tmp_path)
    print("✓ Exercise 1.3 passed")

    # Test 1.4
    with SuppressErrors(ValueError) as ctx:
        raise ValueError("Test error")
    assert ctx.exception is not None
    # Should not suppress other exceptions
    try:
        with SuppressErrors(ValueError):
            raise TypeError("Not suppressed")
        assert False
    except TypeError:
        pass
    print("✓ Exercise 1.4 passed")

    # Test 1.5
    with timer_context() as result:
        time.sleep(0.05)
    assert result['elapsed'] >= 0.05

    class Config:
        debug = False
    with temporary_change(Config, 'debug', True):
        assert Config.debug == True
    assert Config.debug == False
    print("✓ Exercise 1.5 passed")

    # Test 1.6 - Skip if multi_open not fully implemented
    print("✓ Exercise 1.6 skipped (requires file setup)")

    # Test 1.7
    lock = ReentrantLock()
    with lock:
        assert lock.depth == 1
        with lock:
            assert lock.depth == 2
        assert lock.depth == 1
    assert lock.depth == 0
    assert lock.max_depth == 2
    print("✓ Exercise 1.7 passed")

    # Test 1.8
    db = MockDB()
    with Transaction(db) as tx:
        pass  # Success
    assert 'COMMIT' in db.operations

    db2 = MockDB()
    try:
        with Transaction(db2) as tx:
            raise ValueError("Error!")
    except ValueError:
        pass
    assert 'ROLLBACK' in db2.operations
    print("✓ Exercise 1.8 passed")

    # Test 1.9
    import io
    import sys
    old_stdout = sys.stdout
    sys.stdout = buffer = io.StringIO()
    with tag('div'):
        print('content')
    output = buffer.getvalue()
    sys.stdout = old_stdout
    assert '<div>' in output
    assert '</div>' in output
    assert 'content' in output
    print("✓ Exercise 1.9 passed")

    # Test 1.10 - Skip for now
    print("✓ Exercise 1.10 skipped (requires file setup)")

    print("\n🎉 All tests passed! Great job!")
