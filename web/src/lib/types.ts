// Exercise types

export interface ExerciseMetadata {
  id: string;
  name: string;
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
