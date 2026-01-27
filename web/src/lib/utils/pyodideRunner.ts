import { getPyodide } from '../stores/pyodide';
import { parseTestOutput, allTestsPassed } from './exerciseParser';
import type { TestResult } from '../types';

interface ErrorInfo {
  type: string;
  message: string;
  line?: number;
  details?: string;
}

/**
 * Parse a Python error message to extract useful information
 */
function parseErrorMessage(errorMessage: string): ErrorInfo {
  const lines = errorMessage.split('\n');

  // Try to find the error type and message
  let errorType = 'Error';
  let message = errorMessage;
  let lineNum: number | undefined;
  let details: string | undefined;

  // Look for common Python errors
  const errorPatterns = [
    { pattern: /SyntaxError:\s*(.+)/, type: 'SyntaxError' },
    { pattern: /IndentationError:\s*(.+)/, type: 'IndentationError' },
    { pattern: /NameError:\s*(.+)/, type: 'NameError' },
    { pattern: /TypeError:\s*(.+)/, type: 'TypeError' },
    { pattern: /ValueError:\s*(.+)/, type: 'ValueError' },
    { pattern: /AttributeError:\s*(.+)/, type: 'AttributeError' },
    { pattern: /IndexError:\s*(.+)/, type: 'IndexError' },
    { pattern: /KeyError:\s*(.+)/, type: 'KeyError' },
    { pattern: /ZeroDivisionError:\s*(.+)/, type: 'ZeroDivisionError' },
  ];

  for (const line of lines) {
    for (const { pattern, type } of errorPatterns) {
      const match = line.match(pattern);
      if (match) {
        errorType = type;
        message = match[1] || line;
        break;
      }
    }
  }

  // Try to find line number - look for "line X" in the traceback
  const lineMatch = errorMessage.match(/line (\d+)/);
  if (lineMatch) {
    lineNum = parseInt(lineMatch[1], 10);
  }

  // For syntax errors, try to extract the problematic code
  // Look for the caret (^) indicator
  const caretIndex = lines.findIndex(l => l.trim().startsWith('^'));
  if (caretIndex > 0) {
    details = lines[caretIndex - 1]?.trim();
  }

  // Create user-friendly messages for common errors
  if (errorType === 'SyntaxError') {
    if (message.includes('expected')) {
      // Already descriptive
    } else if (message.includes('invalid syntax')) {
      message = 'Invalid syntax - check for missing colons, parentheses, or quotes';
    } else if (message.includes('EOL while scanning string')) {
      message = 'Unclosed string - missing closing quote';
    } else if (message.includes('unexpected EOF')) {
      message = 'Unexpected end of code - missing closing bracket or parenthesis';
    }
  } else if (errorType === 'IndentationError') {
    if (message.includes('expected an indented block')) {
      message = 'Expected an indented block after colon (:)';
    } else if (message.includes('unexpected indent')) {
      message = 'Unexpected indentation - check your spacing';
    }
  } else if (errorType === 'NameError') {
    const nameMatch = message.match(/name '(\w+)' is not defined/);
    if (nameMatch) {
      message = `'${nameMatch[1]}' is not defined - check spelling or define it first`;
    }
  }

  return {
    type: errorType,
    message,
    line: lineNum,
    details
  };
}

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
${testCode}
`;

    // Execute the code
    pyodide.runPython(fullCode);

    // Get captured output
    const stdout = pyodide.runPython('_get_output()');
    const stderr = pyodide.runPython('_get_errors()');

    const output = stdout + (stderr ? '\n' + stderr : '');
    const { passed, failed, failedDetails } = parseTestOutput(output);

    return {
      success: allTestsPassed(output),
      output,
      passedTests: passed,
      failedTests: failed,
      failedTestDetails: failedDetails
    };
  } catch (error) {
    // Get any output before the error
    const stdout = pyodide.runPython('_get_output()');
    const stderr = pyodide.runPython('_get_errors()');

    const errorMessage = error instanceof Error ? error.message : String(error);

    // Parse the error to extract useful information
    const errorInfo = parseErrorMessage(errorMessage);

    const output = stdout + (stderr ? '\n' + stderr : '');
    const { passed, failed, failedDetails } = parseTestOutput(output);

    return {
      success: false,
      output,
      error: errorInfo.message,
      errorType: errorInfo.type,
      errorLine: errorInfo.line,
      errorDetails: errorInfo.details,
      passedTests: passed,
      failedTests: failed,
      failedTestDetails: failedDetails
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
    [/(?<!=)===(?!=)|(?<!=)!==(?!=)/g, "Triple equals (===) isn't needed in Python - just use == or !="],
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
    [/!\w/g, "Use 'not' instead of '!' for negation"],
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
