# Python for JavaScript Developers

A hands-on exercise series designed for experienced JavaScript developers who want to learn Python. Each exercise highlights the differences and similarities between the two languages.

## Prerequisites

- Solid understanding of JavaScript (ES6+)
- Python 3.10+ installed ([download](https://www.python.org/downloads/))
- A code editor (VS Code with Python extension recommended)

## Repository Structure

```
├── 01-basics/           # Syntax, variables, types
├── 02-collections/      # Lists, dicts, tuples, sets
├── 03-control-flow/     # Conditionals, loops, comprehensions
├── 04-functions/        # Args, kwargs, lambdas, scope
├── 05-oop/              # Classes, inheritance, dunder methods
├── 06-error-handling/   # Try/except, custom exceptions
├── 07-modules/          # Imports, packages, virtual environments
├── 08-file-io/          # Reading/writing files
├── 09-decorators/       # Function decorators
├── 10-generators/       # Generators and iterators
├── 11-context-managers/ # The 'with' statement
├── 12-type-hints/       # Static typing in Python
├── 13-testing/          # pytest basics
└── solutions/           # All exercise solutions
```

## How to Use

### Option 1: Interactive CLI (Recommended)

Run the interactive command-line interface for a guided experience:

```bash
python3 cli.py
```

The CLI will:
- Walk you through exercises in order
- Track your progress with streaks and statistics
- Provide encouragement (and occasional teasing when you make mistakes)
- Detect JavaScript habits sneaking into your Python code

CLI options:
```bash
python3 cli.py              # Interactive mode
python3 cli.py --list       # List all exercises
python3 cli.py --progress   # Show detailed progress
python3 cli.py --reset      # Reset progress
```

### Option 2: Manual

1. **Clone this repository**
   ```bash
   git clone <repo-url>
   cd python-practice
   ```

2. **Create a virtual environment** (recommended)
   ```bash
   python3 -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. **Work through exercises in order**
   - Each folder contains numbered exercises
   - Read the comments/docstrings for instructions
   - Run your solution: `python3 exercise_file.py`
   - Check against solutions when done

## Quick Reference: JS → Python

| JavaScript | Python |
|------------|--------|
| `const/let/var` | No keyword needed (or use type hints) |
| `null` | `None` |
| `undefined` | No equivalent (use `None`) |
| `===` | `==` (Python has no type coercion) |
| `true/false` | `True/False` |
| `console.log()` | `print()` |
| `[]` (array) | `[]` (list) |
| `{}` (object) | `{}` (dict) |
| `=>` (arrow fn) | `lambda` |
| `async/await` | `async/await` (similar!) |
| `class` | `class` |
| `this` | `self` (explicit parameter) |
| `import x from 'y'` | `from y import x` |
| `// comment` | `# comment` |
| `{ }` blocks | Indentation (4 spaces) |
| `camelCase` | `snake_case` |

## Running Tests

Some exercises include tests. Run them with:

```bash
pip install pytest
pytest
```

## Tips for JS Developers

1. **Indentation matters** - Python uses indentation instead of braces
2. **No semicolons** - Line endings define statement boundaries
3. **Everything is an object** - Even functions and classes
4. **Explicit is better than implicit** - Python philosophy (see `import this`)
5. **Duck typing** - "If it walks like a duck..."

## Contributing

Found an issue or want to add exercises? PRs welcome!

## License

MIT
