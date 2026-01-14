# Python for JavaScript Developers

A hands-on exercise series designed for experienced JavaScript developers who want to learn Python. Each exercise highlights the differences and similarities between the two languages, with built-in tests to verify your solutions.

## What's Included

- **20 exercises** covering Python fundamentals through advanced topics
- **Side-by-side comparisons** of JavaScript and Python syntax
- **Built-in tests** that run when you execute each exercise file
- **Solutions** for when you get stuck (but try first!)
- **Claude Code integration** for an interactive, guided learning experience

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

### Option 1: Claude Code (Recommended)

If you have [Claude Code](https://claude.ai/claude-code) installed, use the `/practice` command for the best experience:

```bash
claude
# Then type: /practice
```

The `/practice` skill provides:
- **Guided progression** through all 20 exercises
- **Progress tracking** with streaks and statistics
- **Instant feedback** when you run tests
- **Helpful hints** without giving away answers
- **JS habit detection** - it'll catch when you accidentally write `===` instead of `==`
- **Encouraging (and playfully teasing) tutor** personality

Commands:
| Command | Description |
|---------|-------------|
| `/practice` | Show current exercise and progress |
| `/practice list` | List all exercises with completion status |
| `/practice [n]` | Jump to exercise number n |
| `/practice hint` | Get a hint for the current exercise |
| `/practice run` | Run tests for current exercise |
| `/practice solution` | Show solution (try not to peek!) |

### Option 2: Interactive CLI

Run the standalone command-line interface:

```bash
python3 cli.py
```

CLI options:
```bash
python3 cli.py              # Interactive mode
python3 cli.py --list       # List all exercises
python3 cli.py --progress   # Show detailed progress
python3 cli.py --reset      # Reset progress
```

### Option 3: Manual

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

This project is licensed under the **PolyForm Noncommercial License 1.0.0**.

You are free to:
- Use, modify, and fork this project for personal or educational purposes
- Share your modifications with others

You may not:
- Sell this software or any derivative works
- Include this code in commercial products

See [LICENSE](LICENSE) for full details.
