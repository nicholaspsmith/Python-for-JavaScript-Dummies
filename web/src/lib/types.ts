// Exercise types

export type RuntimeType = 'python' | 'react' | 'sql';

export interface ExerciseMetadata {
  id: string;
  name: string;
  runtime: RuntimeType;
  category: string;
  categoryFolder: string;
  filename: string;
  path: string;
  description: string;
}

export interface ExerciseManifest {
  generated: string;
  total: number;
  exercises: ExerciseMetadata[];
}

export interface ParsedExercise {
  instructions: string;
  codeTemplate: string;
  testCode: string;
  fullContent: string;
}

export interface TestResult {
  success: boolean;
  output: string;
  error?: string;
  passedTests: string[];
  failedTests: string[];
}

export interface Progress {
  currentExercise: string;
  completed: string[];
  attempts: Record<string, number>;
  streak: number;
  bestStreak: number;
  savedCode: Record<string, string>;
}

export interface Category {
  name: string;
  folder: string;
  exercises: ExerciseMetadata[];
}

// Section grouping for sidebar
export interface Section {
  name: string;
  runtime: RuntimeType;
  categories: Category[];
}

// SQL-specific types
export interface ParsedSQLExercise {
  instructions: string;
  schema: string;
  seedData: string;
  solutionTemplate: string;
  tests: SQLTestConfig;
  fullContent: string;
}

export interface SQLTestConfig {
  type: 'query_result' | 'row_count' | 'column_check';
  expected: unknown;
  ignoreOrder?: boolean;
}

export interface SQLTestResult {
  success: boolean;
  output: string;
  error?: string;
  actualResult?: unknown[];
  expectedResult?: unknown[];
}

// React-specific types
export interface ParsedReactExercise {
  title: string;
  instructions: string;
  starterCode: Record<string, string>;
  testCode: string;
  dependencies?: Record<string, string>;
}

export interface ReactExerciseConfig {
  title: string;
  instructions: string;
  dependencies?: Record<string, string>;
}
