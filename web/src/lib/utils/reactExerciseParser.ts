import type { ParsedReactExercise, ReactExerciseConfig } from '../types';

/**
 * Parse a React exercise folder structure
 *
 * Expected structure:
 * /exercise_folder/
 *   exercise.json     - { title, instructions, dependencies }
 *   App.jsx           - Starter code
 *   App.test.jsx      - Tests (optional)
 *   styles.css        - Styles (optional)
 */
export async function parseReactExercise(
  basePath: string,
  files: Record<string, string>
): Promise<ParsedReactExercise> {
  // Parse exercise.json
  let config: ReactExerciseConfig = {
    title: 'React Exercise',
    instructions: ''
  };

  if (files['exercise.json']) {
    try {
      config = JSON.parse(files['exercise.json']);
    } catch (e) {
      console.error('Failed to parse exercise.json:', e);
    }
  }

  // Get starter code files
  const starterCode: Record<string, string> = {};

  // Add App.jsx (required)
  if (files['App.jsx']) {
    starterCode['/App.jsx'] = files['App.jsx'];
  } else if (files['App.js']) {
    starterCode['/App.js'] = files['App.js'];
  }

  // Add optional files
  if (files['styles.css']) {
    starterCode['/styles.css'] = files['styles.css'];
  }

  // Get test code
  const testCode = files['App.test.jsx'] || files['App.test.js'] || '';

  return {
    title: config.title,
    instructions: config.instructions,
    starterCode,
    testCode,
    dependencies: config.dependencies
  };
}

/**
 * Create the complete file set for Sandpack
 * This includes boilerplate files needed to run React
 */
export function createSandpackFiles(
  userCode: Record<string, string>,
  dependencies?: Record<string, string>
): Record<string, string> {
  const files: Record<string, string> = {
    '/index.js': `
import React from 'react';
import { createRoot } from 'react-dom/client';
import App from './App';

const root = createRoot(document.getElementById('root'));
root.render(<App />);
`.trim(),

    '/index.html': `
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>React Exercise</title>
</head>
<body>
  <div id="root"></div>
</body>
</html>
`.trim(),

    ...userCode
  };

  // Add default styles if not provided
  if (!files['/styles.css']) {
    files['/styles.css'] = `
body {
  font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif;
  margin: 0;
  padding: 20px;
}

* {
  box-sizing: border-box;
}
`.trim();
  }

  return files;
}

/**
 * Get default dependencies for React exercises
 */
export function getDefaultDependencies(): Record<string, string> {
  return {
    'react': '^18.2.0',
    'react-dom': '^18.2.0'
  };
}

/**
 * Merge user dependencies with defaults
 */
export function mergeDependencies(
  userDeps?: Record<string, string>
): Record<string, string> {
  return {
    ...getDefaultDependencies(),
    ...userDeps
  };
}
