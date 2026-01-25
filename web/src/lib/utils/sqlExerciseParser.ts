import type { ParsedSQLExercise, SQLTestConfig } from '../types';

/**
 * Parse a SQL exercise file into its components
 *
 * Expected format:
 * /*
 * Exercise Title
 * ==============
 * Instructions here...
 * * /
 *
 * -- ============= SCHEMA =============
 * CREATE TABLE ...
 *
 * -- ============= DATA =============
 * INSERT INTO ...
 *
 * -- ============= SOLUTION TEMPLATE =============
 * SELECT ...
 *
 * /*TESTS
 * { "type": "query_result", "expected": [...] }
 * TESTS* /
 */
export function parseSQLExercise(content: string): ParsedSQLExercise {
  // Extract instructions from the initial comment block
  const instructionsMatch = content.match(/^\/\*([\s\S]*?)\*\//);
  let instructions = '';
  if (instructionsMatch) {
    instructions = instructionsMatch[1].trim();
  }

  // Extract schema section
  const schemaMatch = content.match(/-- ============= SCHEMA =============([\s\S]*?)(?=-- =============|\/\*TESTS|$)/);
  let schema = '';
  if (schemaMatch) {
    schema = schemaMatch[1].trim();
  }

  // Extract data section
  const dataMatch = content.match(/-- ============= DATA =============([\s\S]*?)(?=-- =============|\/\*TESTS|$)/);
  let seedData = '';
  if (dataMatch) {
    seedData = dataMatch[1].trim();
  }

  // Extract solution template section
  const templateMatch = content.match(/-- ============= SOLUTION TEMPLATE =============([\s\S]*?)(?=\/\*TESTS|$)/);
  let solutionTemplate = '';
  if (templateMatch) {
    solutionTemplate = templateMatch[1].trim();
  }

  // Extract tests section
  const testsMatch = content.match(/\/\*TESTS([\s\S]*?)TESTS\*\//);
  let tests: SQLTestConfig = { type: 'query_result', expected: [] };
  if (testsMatch) {
    try {
      tests = JSON.parse(testsMatch[1].trim());
    } catch (e) {
      console.error('Failed to parse SQL tests:', e);
    }
  }

  return {
    instructions,
    schema,
    seedData,
    solutionTemplate,
    tests,
    fullContent: content
  };
}

/**
 * Filter user-visible output from SQL exercise content
 * Removes the test configuration section
 */
export function filterSQLOutput(content: string): string {
  // Remove the TESTS block
  return content.replace(/\/\*TESTS[\s\S]*?TESTS\*\//, '').trim();
}
