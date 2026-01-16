import type { ParsedExercise } from '../types';

/**
 * Parse a Python exercise file into its components
 */
export function parseExercise(content: string): ParsedExercise {
  // Extract docstring (instructions)
  const docstringMatch = content.match(/^("""[\s\S]*?""")/m);
  const instructions = docstringMatch
    ? docstringMatch[1]
        .replace(/^"""\n?/, '')
        .replace(/\n?"""$/, '')
        .trim()
    : '';

  // Find the test section
  const testMarker = 'if __name__ == "__main__":';
  const testIndex = content.indexOf(testMarker);

  let codeTemplate: string;
  let testCode: string;

  if (testIndex !== -1) {
    // Everything between docstring and test marker
    const afterDocstring = docstringMatch
      ? content.slice(docstringMatch[0].length)
      : content;
    const beforeTest = afterDocstring.slice(0, afterDocstring.indexOf(testMarker));
    codeTemplate = beforeTest.trim();

    // Test code (without the if __name__ line itself, just the body)
    const testSection = content.slice(testIndex);
    // Extract the body of the if block
    const lines = testSection.split('\n');
    const testLines: string[] = [];
    let inTest = false;

    for (const line of lines) {
      if (line.includes(testMarker)) {
        inTest = true;
        continue;
      }
      if (inTest) {
        // Remove one level of indentation
        if (line.startsWith('    ')) {
          testLines.push(line.slice(4));
        } else if (line.trim() === '') {
          testLines.push('');
        }
      }
    }
    testCode = testLines.join('\n').trim();
  } else {
    // No test section found
    const afterDocstring = docstringMatch
      ? content.slice(docstringMatch[0].length)
      : content;
    codeTemplate = afterDocstring.trim();
    testCode = '';
  }

  // Replace ??? with ... (Ellipsis) to make it valid Python
  // but keep it visible that something needs to be filled in
  const cleanedTemplate = codeTemplate.replace(/\?\?\?/g, '...');

  return {
    instructions,
    codeTemplate: cleanedTemplate,
    testCode,
    fullContent: content
  };
}

/**
 * Parse test output to extract passed/failed tests
 */
export function parseTestOutput(output: string): { passed: string[]; failed: string[] } {
  const passed: string[] = [];
  const failed: string[] = [];

  const lines = output.split('\n');
  for (const line of lines) {
    // Look for "✓ Exercise X.Y passed"
    const passMatch = line.match(/✓\s*Exercise\s+([\d.]+)\s+passed/i);
    if (passMatch) {
      passed.push(passMatch[1]);
      continue;
    }

    // Look for assertion errors
    const assertMatch = line.match(/AssertionError:\s*(.+)/);
    if (assertMatch) {
      failed.push(assertMatch[1]);
    }
  }

  return { passed, failed };
}

/**
 * Check if output indicates all tests passed
 */
export function allTestsPassed(output: string): boolean {
  return output.includes('All tests passed') || output.includes('🎉');
}

/**
 * Filter output to remove traceback and show cleaner results
 */
export function filterOutput(output: string): string {
  const lines = output.split('\n');
  const filtered: string[] = [];
  let inTraceback = false;

  for (const line of lines) {
    // Start of traceback
    if (line.startsWith('Traceback (most recent call last):')) {
      inTraceback = true;
      continue;
    }

    // End of traceback (AssertionError line) - keep the error message
    if (inTraceback && line.includes('AssertionError:')) {
      const match = line.match(/AssertionError:\s*(.+)/);
      if (match) {
        filtered.push(`✗ ${match[1]}`);
      }
      inTraceback = false;
      continue;
    }

    // Skip lines inside traceback
    if (inTraceback) {
      continue;
    }

    // Keep other lines
    filtered.push(line);
  }

  return filtered.join('\n').trim();
}
