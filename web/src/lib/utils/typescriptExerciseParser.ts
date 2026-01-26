import type { ParsedTypeScriptExercise, TypeScriptExerciseConfig } from '../types';

/**
 * Parse a TypeScript exercise folder structure
 *
 * Expected structure:
 * /exercise_folder/
 *   exercise.json     - { title, instructions }
 *   App.ts            - Starter code
 *   App.test.ts       - Tests (optional, for documentation)
 */
export async function parseTypeScriptExercise(
  basePath: string,
  files: Record<string, string>
): Promise<ParsedTypeScriptExercise> {
  // Parse exercise.json
  let config: TypeScriptExerciseConfig = {
    title: 'TypeScript Exercise',
    instructions: ''
  };

  if (files['exercise.json']) {
    try {
      config = JSON.parse(files['exercise.json']);
    } catch (e) {
      console.error('Failed to parse exercise.json:', e);
    }
  }

  // Get starter code
  const starterCode = files['App.ts'] || '';

  // Get test code (for documentation purposes)
  const testCode = files['App.test.ts'] || '';

  return {
    title: config.title,
    instructions: config.instructions,
    starterCode,
    testCode
  };
}

/**
 * Create the complete file set for Sandpack TypeScript execution
 * This includes boilerplate files needed to run TypeScript with console output
 */
export function createTypeScriptSandpackFiles(
  userCode: string
): Record<string, string> {
  const files: Record<string, string> = {
    '/index.ts': userCode,

    '/index.html': `
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>TypeScript OOP Exercise</title>
  <style>
    body {
      font-family: 'Monaco', 'Menlo', 'Ubuntu Mono', monospace;
      background: #1e1e1e;
      color: #d4d4d4;
      margin: 0;
      padding: 16px;
    }
    .console {
      white-space: pre-wrap;
      word-wrap: break-word;
      line-height: 1.5;
    }
    .log { color: #d4d4d4; }
    .error { color: #f48771; }
    .warn { color: #cca700; }
    .info { color: #75beff; }
    .success { color: #89d185; }
    .separator {
      border-top: 1px solid #3c3c3c;
      margin: 8px 0;
      padding-top: 8px;
    }
  </style>
</head>
<body>
  <div id="console" class="console"></div>
  <script>
    // Capture console output
    const consoleDiv = document.getElementById('console');

    function appendToConsole(type, args) {
      const line = document.createElement('div');
      line.className = type;
      line.textContent = args.map(arg => {
        if (typeof arg === 'object') {
          try {
            return JSON.stringify(arg, null, 2);
          } catch (e) {
            return String(arg);
          }
        }
        return String(arg);
      }).join(' ');
      consoleDiv.appendChild(line);
    }

    const originalConsole = {
      log: console.log,
      error: console.error,
      warn: console.warn,
      info: console.info
    };

    console.log = (...args) => {
      originalConsole.log(...args);
      appendToConsole('log', args);
    };

    console.error = (...args) => {
      originalConsole.error(...args);
      appendToConsole('error', args);
    };

    console.warn = (...args) => {
      originalConsole.warn(...args);
      appendToConsole('warn', args);
    };

    console.info = (...args) => {
      originalConsole.info(...args);
      appendToConsole('info', args);
    };

    // Handle uncaught errors
    window.onerror = (msg, url, line, col, error) => {
      appendToConsole('error', ['Error:', msg]);
      return false;
    };
  </script>
</body>
</html>
`.trim()
  };

  return files;
}

/**
 * Get default dependencies for TypeScript exercises
 */
export function getTypeScriptDependencies(): Record<string, string> {
  return {
    'typescript': '^5.0.0'
  };
}
