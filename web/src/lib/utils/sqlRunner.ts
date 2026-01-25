import { createDatabase } from '../stores/sqljs';
import type { SQLTestConfig, SQLTestResult } from '../types';

interface QueryResult {
  columns: string[];
  values: unknown[][];
}

/**
 * Run SQL query and validate against expected results
 */
export async function runSQLTests(
  userQuery: string,
  schema: string,
  seedData: string,
  testConfig: SQLTestConfig
): Promise<SQLTestResult> {
  let db: any = null;

  try {
    // Create a new in-memory database
    db = createDatabase();

    // Set up schema
    if (schema) {
      db.run(schema);
    }

    // Insert seed data
    if (seedData) {
      db.run(seedData);
    }

    // Run user's query using db.exec
    const results: QueryResult[] = db.exec(userQuery);

    // Validate results based on test type
    switch (testConfig.type) {
      case 'query_result':
        return validateQueryResult(results, testConfig);
      case 'row_count':
        return validateRowCount(results, testConfig);
      case 'column_check':
        return validateColumnCheck(results, testConfig);
      default:
        return {
          success: false,
          output: 'Unknown test type',
          error: `Invalid test type: ${testConfig.type}`
        };
    }
  } catch (error) {
    const errorMessage = error instanceof Error ? error.message : 'Unknown SQL error';
    return {
      success: false,
      output: '',
      error: errorMessage
    };
  } finally {
    if (db) {
      db.close();
    }
  }
}

/**
 * Validate query results match expected output
 */
function validateQueryResult(
  results: QueryResult[],
  testConfig: SQLTestConfig
): SQLTestResult {
  if (results.length === 0) {
    return {
      success: false,
      output: 'Query returned no results',
      error: 'Expected results but got none',
      actualResult: [],
      expectedResult: testConfig.expected as unknown[]
    };
  }

  const result = results[0];
  const actual = result.values;
  const expected = testConfig.expected as unknown[][];

  // Compare results
  let matches = false;

  if (testConfig.ignoreOrder) {
    // Sort both arrays for comparison
    const sortedActual = [...actual].sort((a, b) => JSON.stringify(a).localeCompare(JSON.stringify(b)));
    const sortedExpected = [...expected].sort((a, b) => JSON.stringify(a).localeCompare(JSON.stringify(b)));
    matches = JSON.stringify(sortedActual) === JSON.stringify(sortedExpected);
  } else {
    matches = JSON.stringify(actual) === JSON.stringify(expected);
  }

  if (matches) {
    return {
      success: true,
      output: formatQueryOutput(result),
      actualResult: actual,
      expectedResult: expected
    };
  }

  return {
    success: false,
    output: formatQueryOutput(result),
    error: 'Query results do not match expected output',
    actualResult: actual,
    expectedResult: expected
  };
}

/**
 * Validate query returns expected number of rows
 */
function validateRowCount(
  results: QueryResult[],
  testConfig: SQLTestConfig
): SQLTestResult {
  const expected = testConfig.expected as number;
  const actual = results.length > 0 ? results[0].values.length : 0;

  if (actual === expected) {
    return {
      success: true,
      output: `Query returned ${actual} rows`,
      actualResult: [actual],
      expectedResult: [expected]
    };
  }

  return {
    success: false,
    output: `Query returned ${actual} rows`,
    error: `Expected ${expected} rows but got ${actual}`,
    actualResult: [actual],
    expectedResult: [expected]
  };
}

/**
 * Validate query returns expected columns
 */
function validateColumnCheck(
  results: QueryResult[],
  testConfig: SQLTestConfig
): SQLTestResult {
  const expected = testConfig.expected as string[];
  const actual = results.length > 0 ? results[0].columns : [];

  const matches = JSON.stringify(actual.map(c => c.toLowerCase())) ===
                  JSON.stringify(expected.map(c => c.toLowerCase()));

  if (matches) {
    return {
      success: true,
      output: `Query returned columns: ${actual.join(', ')}`,
      actualResult: actual,
      expectedResult: expected
    };
  }

  return {
    success: false,
    output: `Query returned columns: ${actual.join(', ')}`,
    error: `Expected columns: ${expected.join(', ')}`,
    actualResult: actual,
    expectedResult: expected
  };
}

/**
 * Format query results for display
 */
function formatQueryOutput(result: QueryResult): string {
  if (!result || result.values.length === 0) {
    return 'No results';
  }

  const { columns, values } = result;

  // Calculate column widths
  const widths = columns.map((col, i) => {
    const valueWidths = values.map(row => String(row[i]).length);
    return Math.max(col.length, ...valueWidths);
  });

  // Build table
  const lines: string[] = [];

  // Header
  lines.push(columns.map((col, i) => col.padEnd(widths[i])).join(' | '));
  lines.push(widths.map(w => '-'.repeat(w)).join('-+-'));

  // Rows
  for (const row of values) {
    lines.push(row.map((val, i) => String(val).padEnd(widths[i])).join(' | '));
  }

  return lines.join('\n');
}

/**
 * Run a single SQL query and return raw results
 * Useful for previewing query output
 */
export function runQuery(
  query: string,
  schema: string,
  seedData: string
): { columns: string[]; rows: unknown[][] } | { error: string } {
  let db: any = null;

  try {
    db = createDatabase();

    if (schema) {
      db.run(schema);
    }

    if (seedData) {
      db.run(seedData);
    }

    const results: QueryResult[] = db.exec(query);

    if (results.length === 0) {
      return { columns: [], rows: [] };
    }

    return {
      columns: results[0].columns,
      rows: results[0].values
    };
  } catch (error) {
    return {
      error: error instanceof Error ? error.message : 'Unknown SQL error'
    };
  } finally {
    if (db) {
      db.close();
    }
  }
}
