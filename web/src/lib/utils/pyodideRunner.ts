import { getPyodide } from '../stores/pyodide';
import { parseTestOutput, allTestsPassed } from './exerciseParser';
import type { TestResult } from '../types';

/**
 * Run Python code with tests and capture output
 */
export async function runTests(userCode: string, testCode: string): Promise<TestResult> {
  const pyodide = getPyodide();

  // Set up stdout/stderr capture
  pyodide.runPython(`
import sys
from io import StringIO

# Capture stdout and stderr
_captured_stdout = StringIO()
_captured_stderr = StringIO()
sys.stdout = _captured_stdout
sys.stderr = _captured_stderr

def _get_output():
    return _captured_stdout.getvalue()

def _get_errors():
    return _captured_stderr.getvalue()

def _reset_capture():
    global _captured_stdout, _captured_stderr
    _captured_stdout = StringIO()
    _captured_stderr = StringIO()
    sys.stdout = _captured_stdout
    sys.stderr = _captured_stderr
`);

  try {
    // Reset capture before running
    pyodide.runPython('_reset_capture()');

    // Combine user code with test code
    // We run the test code directly (not inside if __name__ block)
    const fullCode = `
${userCode}

# Run tests
print("Running tests...")
${testCode}
`;

    // Execute the code
    pyodide.runPython(fullCode);

    // Get captured output
    const stdout = pyodide.runPython('_get_output()');
    const stderr = pyodide.runPython('_get_errors()');

    const output = stdout + (stderr ? '\n' + stderr : '');
    const { passed, failed } = parseTestOutput(output);

    return {
      success: allTestsPassed(output),
      output,
      passedTests: passed,
      failedTests: failed
    };
  } catch (error) {
    // Get any output before the error
    const stdout = pyodide.runPython('_get_output()');
    const stderr = pyodide.runPython('_get_errors()');

    const errorMessage = error instanceof Error ? error.message : String(error);

    // Try to extract useful error info
    let cleanError = errorMessage;

    // Parse Python traceback to find the actual error
    const lines = errorMessage.split('\n');
    const assertionLine = lines.find(l => l.includes('AssertionError'));
    if (assertionLine) {
      cleanError = assertionLine;
    }

    // Check for syntax errors
    const syntaxLine = lines.find(l => l.includes('SyntaxError'));
    if (syntaxLine) {
      cleanError = syntaxLine;
    }

    // Check for name errors (undefined variables)
    const nameLine = lines.find(l => l.includes('NameError'));
    if (nameLine) {
      cleanError = nameLine;
    }

    const output = stdout + (stderr ? '\n' + stderr : '');
    const { passed, failed } = parseTestOutput(output);

    return {
      success: false,
      output,
      error: cleanError,
      passedTests: passed,
      failedTests: [...failed, cleanError]
    };
  } finally {
    // Restore stdout/stderr
    pyodide.runPython(`
sys.stdout = sys.__stdout__
sys.stderr = sys.__stderr__
`);
  }
}

/**
 * Detect JavaScript habits in Python code
 */
export function detectJsHabits(code: string): string[] {
  const habits: string[] = [];

  const jsPatterns: [RegExp, string][] = [
    [/===|!==/g, "Triple equals (===) isn't needed in Python - just use == or !="],
    [/\btrue\b/g, "That's 'True' with a capital T in Python"],
    [/\bfalse\b/g, "That's 'False' with a capital F in Python"],
    [/\bnull\b/g, "It's 'None' in Python, not 'null'"],
    [/\bconsole\.log\b/g, "Use print() instead of console.log()"],
    [/\bconst\s+/g, "No need for 'const' in Python - just assign directly"],
    [/\blet\s+/g, "No need for 'let' in Python - just assign directly"],
    [/\bvar\s+/g, "No need for 'var' in Python - just assign directly"],
    [/\bfunction\s+\w+\s*\(/g, "Use 'def' to define functions in Python"],
    [/=>/g, "Arrow functions? Use 'lambda' or 'def' in Python"],
    [/&&/g, "Use 'and' instead of '&&'"],
    [/\|\|/g, "Use 'or' instead of '||'"],
    [/!/g, "Use 'not' instead of '!' for negation"],
    [/\.length\b/g, "Use len() instead of .length"],
    [/\.push\s*\(/g, "Use .append() instead of .push()"],
    [/\.forEach\s*\(/g, "Use a for loop: 'for item in list:'"],
    [/\.map\s*\(/g, "Use a list comprehension: [f(x) for x in list]"],
    [/\.filter\s*\(/g, "Use a list comprehension: [x for x in list if condition]"]
  ];

  for (const [pattern, message] of jsPatterns) {
    if (pattern.test(code)) {
      habits.push(message);
    }
  }

  return habits;
}
