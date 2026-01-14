#!/usr/bin/env python3
"""
Python Practice CLI
====================

An interactive command-line interface that guides JavaScript developers
through Python exercises with encouragement (and occasional teasing).

Usage:
    python3 cli.py              # Start interactive mode
    python3 cli.py --list       # List all exercises
    python3 cli.py --progress   # Show progress
    python3 cli.py --reset      # Reset progress
"""

import sys
import json
import random
import subprocess
import time
from pathlib import Path
from dataclasses import dataclass
from typing import Optional

# ANSI color codes
class Colors:
    HEADER = '\033[95m'
    BLUE = '\033[94m'
    CYAN = '\033[96m'
    GREEN = '\033[92m'
    YELLOW = '\033[93m'
    RED = '\033[91m'
    BOLD = '\033[1m'
    DIM = '\033[2m'
    RESET = '\033[0m'
    CLEAR = '\033[2J\033[H'  # ANSI clear screen


# ============= Messages =============

WELCOME_MESSAGES = [
    "Welcome, brave JavaScript refugee! Ready to embrace the way of the snake?",
    "Ah, another JS developer seeking enlightenment. Let's begin!",
    "So you've decided to learn a language with REAL integers? Bold move.",
    "Welcome! Don't worry, we won't judge your past npm mistakes here.",
    "Greetings! Leave your semicolons at the door, please.",
]

ENCOURAGEMENT = [
    "You're doing great! Python suits you.",
    "Look at you, writing Pythonic code like a pro!",
    "Excellent work! Your JS habits are fading already.",
    "Fantastic! Guido van Rossum would be proud.",
    "Amazing! You're basically a Python developer now.",
    "Brilliant! Who needs curly braces anyway?",
    "Outstanding! The snake has chosen you.",
    "Perfect! Your indentation is *chef's kiss*.",
    "Wonderful! No 'undefined' in sight!",
    "Superb! You've earned a virtual coffee break.",
]

FIRST_TRY_SUCCESS = [
    "First try?! Are you sure you haven't done this before?",
    "Perfect on the first attempt! Suspicious... very suspicious.",
    "Nailed it! Did you peek at the solutions? (Just kidding... maybe)",
    "Flawless! Your JavaScript shame is being washed away.",
    "First try success! The Python gods smile upon you.",
]

MILD_TEASING = [
    "Oops! That's not quite right. But hey, at least it's not a TypeError from `undefined`.",
    "Not quite! Remember, we use 'True' not 'true'. Python is fancy like that.",
    "Almost! Take another look. I believe in you (mostly).",
    "Hmm, that didn't work. But don't worry, we've all been there.",
    "Nope! But look at the bright side - no callback hell to debug!",
    "Try again! Python errors are actually readable, unlike some languages...",
    "Not yet! Remember: explicit is better than implicit. Read the error!",
    "Oops! Quick, blame it on muscle memory from JavaScript.",
]

MULTIPLE_FAILURES = [
    "Still working on it? That's called persistence! (Or stubbornness. Same thing.)",
    "Having trouble? Remember, there's no shame in reading the hints...",
    "Keep trying! Rome wasn't built in a day, and neither was Django.",
    "You've got this! Though the solutions file is right there, just saying...",
    "Struggling a bit? It's okay, Python's elegance takes time to appreciate.",
    "Still at it? Your dedication is... admirable? Concerning? Both?",
]

GIVING_UP_MESSAGES = [
    "Taking a break? Smart. The code will still be here judging you later.",
    "Stepping away? Good idea. Fresh eyes and all that.",
    "Quitting? That's not quitting, that's 'strategic withdrawal'.",
    "Leaving already? The exercises will miss you. Probably.",
]

COMPLETION_MESSAGES = [
    "YOU DID IT! All exercises complete! You're officially a Python developer!",
    "CONGRATULATIONS! You've completed all exercises! Time to update LinkedIn!",
    "AMAZING! All done! Go forth and write beautiful, Pythonic code!",
    "INCREDIBLE! You've finished everything! No more `npm install` for you!",
]

JS_HABITS_DETECTED = {
    "===": "Ah, triple equals! In Python we just use ==. No type coercion madness here!",
    "const ": "Looking for 'const'? Python doesn't need it. We trust you (sort of).",
    "let ": "No 'let' needed! Just assign directly. Python keeps it simple.",
    "null": "It's 'None' in Python. More elegant, don't you think?",
    "true": "That's 'True' with a capital T. Python is proper like that.",
    "false": "It's 'False' in Python. Yes, capitalized. We're fancy.",
    "console.log": "Looking for console.log? It's just print() here. Simpler!",
    "function ": "We use 'def' for functions. Shorter and sweeter!",
    "=> ": "Arrow functions? Use 'lambda' for simple ones, 'def' for the rest.",
    "{}": "Empty object? In Python that's a dict: {} or dict()",
    "[]": "Arrays are called 'lists' here. Same idea, cooler name.",
    ".length": "It's len() in Python. A function, not a property. Deal with it.",
    ".push(": "Use .append() for lists. Different name, same energy.",
    "&&": "Use 'and' instead of &&. More readable!",
    "||": "Use 'or' instead of ||. English > symbols.",
    "!": "Use 'not' for negation. Python speaks English!",
}


# ============= Data Classes =============

@dataclass
class Exercise:
    """Represents a single exercise file."""
    number: str
    name: str
    path: Path
    category: str
    description: str


@dataclass
class Progress:
    """Tracks user progress."""
    completed: list
    attempts: dict
    current_streak: int
    best_streak: int
    total_time: float


# ============= Core Functions =============

def get_exercises() -> list[Exercise]:
    """Discover all exercise files."""
    exercises = []
    base_path = Path(__file__).parent

    categories = {
        "01-basics": "Python Basics - Variables, Types, Operators",
        "02-collections": "Collections - Lists, Dicts, Tuples, Sets",
        "03-control-flow": "Control Flow - Conditionals, Loops, Comprehensions",
        "04-functions": "Functions - Basics, Args, Kwargs, Lambdas",
        "05-oop": "Object-Oriented Programming - Classes, Inheritance",
        "06-error-handling": "Error Handling - Exceptions, Try/Except",
        "07-modules": "Modules and Imports",
        "08-file-io": "File I/O Operations",
        "09-decorators": "Decorators - Function Wrappers",
        "10-generators": "Generators and Iterators",
        "11-context-managers": "Context Managers - The 'with' Statement",
        "12-type-hints": "Type Hints - Python's TypeScript",
        "13-testing": "Testing with pytest",
    }

    for folder, description in categories.items():
        folder_path = base_path / folder
        if folder_path.exists():
            for file in sorted(folder_path.glob("*.py")):
                exercise_num = f"{folder.split('-')[0]}.{file.stem.split('_')[0]}"
                exercise_name = file.stem.replace("_", " ").title()
                exercises.append(Exercise(
                    number=exercise_num,
                    name=exercise_name,
                    path=file,
                    category=folder,
                    description=description
                ))

    return exercises


def load_progress() -> Progress:
    """Load progress from file."""
    progress_file = Path(__file__).parent / ".progress.json"
    if progress_file.exists():
        data = json.loads(progress_file.read_text())
        return Progress(
            completed=data.get("completed", []),
            attempts=data.get("attempts", {}),
            current_streak=data.get("current_streak", 0),
            best_streak=data.get("best_streak", 0),
            total_time=data.get("total_time", 0.0)
        )
    return Progress([], {}, 0, 0, 0.0)


def save_progress(progress: Progress):
    """Save progress to file."""
    progress_file = Path(__file__).parent / ".progress.json"
    progress_file.write_text(json.dumps({
        "completed": progress.completed,
        "attempts": progress.attempts,
        "current_streak": progress.current_streak,
        "best_streak": progress.best_streak,
        "total_time": progress.total_time
    }, indent=2))


def reset_progress():
    """Reset all progress."""
    progress_file = Path(__file__).parent / ".progress.json"
    if progress_file.exists():
        progress_file.unlink()
    print(f"{Colors.YELLOW}Progress reset! Starting fresh.{Colors.RESET}")


# ============= UI Functions =============

def clear_screen():
    """Clear the terminal screen using ANSI escape codes."""
    print(Colors.CLEAR, end='')


def print_header():
    """Print the CLI header."""
    print(f"""
{Colors.CYAN}{Colors.BOLD}
    ____        __  __                   ____                  __  _
   / __ \\__  __/ /_/ /_  ____  ____     / __ \\_________ ______/ /_(_)_______
  / /_/ / / / / __/ __ \\/ __ \\/ __ \\   / /_/ / ___/ __ `/ ___/ __/ / ___/ _ \\
 / ____/ /_/ / /_/ / / / /_/ / / / /  / ____/ /  / /_/ / /__/ /_/ / /__/  __/
/_/    \\__, /\\__/_/ /_/\\____/_/ /_/  /_/   /_/   \\__,_/\\___/\\__/_/\\___/\\___/
      /____/
{Colors.RESET}
{Colors.DIM}    For JavaScript Developers Who Want to Learn Python{Colors.RESET}
""")


def print_progress_bar(completed: int, total: int, width: int = 40):
    """Print a progress bar."""
    percentage = completed / total if total > 0 else 0
    filled = int(width * percentage)
    bar = "█" * filled + "░" * (width - filled)
    print(f"{Colors.GREEN}[{bar}] {completed}/{total} ({percentage*100:.1f}%){Colors.RESET}")


def detect_js_habits(code: str) -> Optional[str]:
    """Check for JavaScript habits in code and return a teasing message."""
    for pattern, message in JS_HABITS_DETECTED.items():
        if pattern in code:
            return message
    return None


def open_in_editor(filepath: Path):
    """Open file in user's preferred editor."""
    import shutil

    # Try common editors in order of preference
    editors = ['code', 'vim', 'nano', 'vi']

    for editor in editors:
        if shutil.which(editor):
            print(f"\n{Colors.CYAN}Opening {filepath} in {editor}...{Colors.RESET}")
            subprocess.run([editor, str(filepath)])
            return

    # Fallback message
    print(f"\n{Colors.YELLOW}No editor found. Please open manually:{Colors.RESET}")
    print(f"  {filepath}")


def run_exercise(exercise: Exercise, progress: Progress) -> bool:
    """Run an exercise and return True if passed."""
    clear_screen()

    print(f"\n{Colors.HEADER}{Colors.BOLD}═══════════════════════════════════════════════════════════════{Colors.RESET}")
    print(f"{Colors.CYAN}{Colors.BOLD}  Exercise {exercise.number}: {exercise.name}{Colors.RESET}")
    print(f"{Colors.DIM}  {exercise.description}{Colors.RESET}")
    print(f"{Colors.HEADER}{Colors.BOLD}═══════════════════════════════════════════════════════════════{Colors.RESET}\n")

    # Show file path
    print(f"{Colors.DIM}File: {exercise.path}{Colors.RESET}\n")

    # Track attempts
    exercise_key = str(exercise.path)
    if exercise_key not in progress.attempts:
        progress.attempts[exercise_key] = 0

    while True:
        print(f"{Colors.YELLOW}[R]{Colors.RESET} Run tests  {Colors.YELLOW}[E]{Colors.RESET} Edit file  {Colors.YELLOW}[H]{Colors.RESET} Hints  {Colors.YELLOW}[S]{Colors.RESET} Skip  {Colors.YELLOW}[Q]{Colors.RESET} Quit")
        choice = input(f"\n{Colors.BOLD}Your choice: {Colors.RESET}").strip().lower()

        if choice == 'r':
            progress.attempts[exercise_key] += 1
            attempts = progress.attempts[exercise_key]

            print(f"\n{Colors.CYAN}Running tests...{Colors.RESET}\n")
            start_time = time.time()

            result = subprocess.run(
                [sys.executable, str(exercise.path)],
                capture_output=True,
                text=True
            )

            elapsed = time.time() - start_time
            progress.total_time += elapsed

            # Print output
            if result.stdout:
                print(result.stdout)
            if result.stderr:
                print(f"{Colors.RED}{result.stderr}{Colors.RESET}")

            # Check for success
            if result.returncode == 0 and "All tests passed" in result.stdout:
                print(f"\n{Colors.GREEN}{Colors.BOLD}{'─' * 50}{Colors.RESET}")

                if attempts == 1:
                    print(f"{Colors.GREEN}{Colors.BOLD}✓ {random.choice(FIRST_TRY_SUCCESS)}{Colors.RESET}")
                else:
                    print(f"{Colors.GREEN}{Colors.BOLD}✓ {random.choice(ENCOURAGEMENT)}{Colors.RESET}")
                    if attempts > 3:
                        print(f"{Colors.DIM}  (Only took you {attempts} attempts!){Colors.RESET}")

                print(f"{Colors.GREEN}{Colors.BOLD}{'─' * 50}{Colors.RESET}\n")

                # Update progress
                if exercise_key not in progress.completed:
                    progress.completed.append(exercise_key)
                    progress.current_streak += 1
                    if progress.current_streak > progress.best_streak:
                        progress.best_streak = progress.current_streak

                save_progress(progress)
                input(f"{Colors.DIM}Press Enter to continue...{Colors.RESET}")
                return True
            else:
                # Failure - tease them
                print(f"\n{Colors.RED}{'─' * 50}{Colors.RESET}")

                if attempts <= 2:
                    print(f"{Colors.YELLOW}{random.choice(MILD_TEASING)}{Colors.RESET}")
                else:
                    print(f"{Colors.YELLOW}{random.choice(MULTIPLE_FAILURES)}{Colors.RESET}")

                # Check for JS habits in the file
                code = exercise.path.read_text()
                js_habit = detect_js_habits(code)
                if js_habit:
                    print(f"\n{Colors.CYAN}💡 JS Habit Detected: {js_habit}{Colors.RESET}")

                print(f"{Colors.RED}{'─' * 50}{Colors.RESET}\n")
                progress.current_streak = 0
                save_progress(progress)

        elif choice == 'e':
            open_in_editor(exercise.path)

        elif choice == 'h':
            print(f"\n{Colors.CYAN}{'─' * 50}{Colors.RESET}")
            print(f"{Colors.CYAN}{Colors.BOLD}Hints:{Colors.RESET}")
            print(f"  • Read the docstrings carefully - they contain JS comparisons")
            print(f"  • Look for ??? and # YOUR CODE HERE markers")
            print(f"  • Check solutions/README.md for help")
            print(f"  • Run python3 in terminal to experiment interactively")
            print(f"{Colors.CYAN}{'─' * 50}{Colors.RESET}\n")

        elif choice == 's':
            print(f"\n{Colors.YELLOW}Skipping exercise. No shame in coming back later!{Colors.RESET}\n")
            return False

        elif choice == 'q':
            print(f"\n{Colors.YELLOW}{random.choice(GIVING_UP_MESSAGES)}{Colors.RESET}\n")
            return None


def show_menu(exercises: list[Exercise], progress: Progress):
    """Show the main menu."""
    clear_screen()
    print_header()

    # Show welcome message
    print(f"{Colors.GREEN}{random.choice(WELCOME_MESSAGES)}{Colors.RESET}\n")

    # Progress overview
    completed_count = len(progress.completed)
    total_count = len(exercises)

    print(f"{Colors.BOLD}Your Progress:{Colors.RESET}")
    print_progress_bar(completed_count, total_count)

    if progress.current_streak > 0:
        print(f"{Colors.GREEN}🔥 Current streak: {progress.current_streak}{Colors.RESET}")
    if progress.best_streak > 0:
        print(f"{Colors.CYAN}🏆 Best streak: {progress.best_streak}{Colors.RESET}")

    print()

    # Group exercises by category
    current_category = None
    for i, exercise in enumerate(exercises):
        if exercise.category != current_category:
            current_category = exercise.category
            print(f"\n{Colors.HEADER}{Colors.BOLD}{exercise.description}{Colors.RESET}")

        # Check if completed
        is_completed = str(exercise.path) in progress.completed
        status = f"{Colors.GREEN}✓{Colors.RESET}" if is_completed else f"{Colors.DIM}○{Colors.RESET}"

        # Highlight next uncompleted
        prev_completed = str(exercises[i-1].path) in progress.completed if i > 0 else True
        if not is_completed and prev_completed:
            print(f"  {status} {Colors.YELLOW}[{i+1}]{Colors.RESET} {exercise.name} {Colors.YELLOW}← Next{Colors.RESET}")
        else:
            print(f"  {status} {Colors.DIM}[{i+1}]{Colors.RESET} {exercise.name}")

    print(f"\n{Colors.BOLD}Options:{Colors.RESET}")
    print(f"  {Colors.YELLOW}[N]{Colors.RESET} Next uncompleted exercise")
    print(f"  {Colors.YELLOW}[1-{len(exercises)}]{Colors.RESET} Jump to specific exercise")
    print(f"  {Colors.YELLOW}[P]{Colors.RESET} Show detailed progress")
    print(f"  {Colors.YELLOW}[R]{Colors.RESET} Reset progress")
    print(f"  {Colors.YELLOW}[Q]{Colors.RESET} Quit")

    return input(f"\n{Colors.BOLD}Enter choice: {Colors.RESET}").strip().lower()


def show_detailed_progress(exercises: list[Exercise], progress: Progress):
    """Show detailed progress statistics."""
    clear_screen()
    print(f"\n{Colors.HEADER}{Colors.BOLD}═══════════════════════════════════════════════════════════════{Colors.RESET}")
    print(f"{Colors.CYAN}{Colors.BOLD}  Your Python Learning Journey{Colors.RESET}")
    print(f"{Colors.HEADER}{Colors.BOLD}═══════════════════════════════════════════════════════════════{Colors.RESET}\n")

    completed_count = len(progress.completed)
    total_count = len(exercises)

    print(f"{Colors.BOLD}Overall Progress:{Colors.RESET}")
    print_progress_bar(completed_count, total_count)
    print()

    print(f"{Colors.BOLD}Statistics:{Colors.RESET}")
    print(f"  Exercises completed: {Colors.GREEN}{completed_count}{Colors.RESET}/{total_count}")
    print(f"  Current streak: {Colors.GREEN}{progress.current_streak}{Colors.RESET}")
    print(f"  Best streak: {Colors.CYAN}{progress.best_streak}{Colors.RESET}")

    hours = int(progress.total_time // 3600)
    minutes = int((progress.total_time % 3600) // 60)
    print(f"  Time spent: {Colors.CYAN}{hours}h {minutes}m{Colors.RESET}")

    # Per-category breakdown
    print(f"\n{Colors.BOLD}By Category:{Colors.RESET}")
    categories = {}
    for ex in exercises:
        if ex.category not in categories:
            categories[ex.category] = {"total": 0, "completed": 0}
        categories[ex.category]["total"] += 1
        if str(ex.path) in progress.completed:
            categories[ex.category]["completed"] += 1

    for cat, stats in categories.items():
        pct = stats["completed"] / stats["total"] * 100 if stats["total"] > 0 else 0
        bar_width = 20
        filled = int(bar_width * pct / 100)
        bar = "█" * filled + "░" * (bar_width - filled)
        status = f"{Colors.GREEN}Complete!{Colors.RESET}" if pct == 100 else f"{stats['completed']}/{stats['total']}"
        print(f"  {cat}: [{bar}] {status}")

    if completed_count == total_count:
        print(f"\n{Colors.GREEN}{Colors.BOLD}{random.choice(COMPLETION_MESSAGES)}{Colors.RESET}")

    print()
    input(f"{Colors.DIM}Press Enter to continue...{Colors.RESET}")


def main():
    """Main entry point."""
    import argparse

    parser = argparse.ArgumentParser(description="Python Practice CLI")
    parser.add_argument("--list", action="store_true", help="List all exercises")
    parser.add_argument("--progress", action="store_true", help="Show progress")
    parser.add_argument("--reset", action="store_true", help="Reset progress")
    args = parser.parse_args()

    exercises = get_exercises()
    progress = load_progress()

    if args.list:
        print(f"\n{Colors.BOLD}Available Exercises:{Colors.RESET}\n")
        for i, ex in enumerate(exercises, 1):
            status = "✓" if str(ex.path) in progress.completed else " "
            print(f"  [{status}] {i}. {ex.number} - {ex.name}")
        print()
        return

    if args.progress:
        show_detailed_progress(exercises, progress)
        return

    if args.reset:
        reset_progress()
        return

    # Interactive mode
    while True:
        choice = show_menu(exercises, progress)

        if choice == 'q':
            print(f"\n{Colors.CYAN}Happy coding! Come back soon!{Colors.RESET}\n")
            break

        elif choice == 'n':
            # Find next uncompleted
            next_exercise = None
            for ex in exercises:
                if str(ex.path) not in progress.completed:
                    next_exercise = ex
                    break

            if next_exercise:
                result = run_exercise(next_exercise, progress)
                if result is None:  # Quit
                    break
            else:
                print(f"\n{Colors.GREEN}{random.choice(COMPLETION_MESSAGES)}{Colors.RESET}")
                input(f"{Colors.DIM}Press Enter to continue...{Colors.RESET}")

        elif choice == 'p':
            show_detailed_progress(exercises, progress)

        elif choice == 'r':
            confirm = input(f"{Colors.RED}Reset all progress? (yes/no): {Colors.RESET}").strip().lower()
            if confirm == 'yes':
                reset_progress()
                progress = load_progress()

        elif choice.isdigit():
            idx = int(choice) - 1
            if 0 <= idx < len(exercises):
                result = run_exercise(exercises[idx], progress)
                if result is None:  # Quit
                    break
            else:
                print(f"{Colors.RED}Invalid exercise number.{Colors.RESET}")
                time.sleep(1)


if __name__ == "__main__":
    main()
