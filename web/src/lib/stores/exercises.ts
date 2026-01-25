import { writable, derived } from 'svelte/store';
import type { ExerciseMetadata, ExerciseManifest, Category, Section, RuntimeType } from '../types';
import { currentExerciseId } from './progress';
import manifest from '../exercises-manifest.json';

// Cast the imported JSON to our type
const exerciseManifest = manifest as ExerciseManifest;

// Store for all exercise metadata
export const exercises = writable<ExerciseMetadata[]>(exerciseManifest.exercises);
export const totalExercises = writable<number>(exerciseManifest.total);

// Re-export currentExerciseId from progress store (it's the source of truth)
export { currentExerciseId };

// Group exercises by category
export const categories = derived(exercises, ($exercises): Category[] => {
  const categoryMap = new Map<string, Category>();

  for (const exercise of $exercises) {
    if (!categoryMap.has(exercise.categoryFolder)) {
      categoryMap.set(exercise.categoryFolder, {
        name: exercise.category,
        folder: exercise.categoryFolder,
        exercises: []
      });
    }
    categoryMap.get(exercise.categoryFolder)!.exercises.push(exercise);
  }

  return Array.from(categoryMap.values()).sort((a, b) =>
    a.folder.localeCompare(b.folder)
  );
});

// Section configurations
const sectionConfig: Record<RuntimeType, { name: string; icon: string }> = {
  python: { name: 'Leetcode (Python)', icon: '🐍' },
  react: { name: 'React', icon: '⚛️' },
  sql: { name: 'SQL', icon: '🗄️' }
};

// Group categories into sections by runtime
export const sections = derived(categories, ($categories): Section[] => {
  const sectionMap = new Map<RuntimeType, Category[]>();

  for (const category of $categories) {
    // Determine runtime from first exercise in category
    const runtime = category.exercises[0]?.runtime ?? 'python';

    if (!sectionMap.has(runtime)) {
      sectionMap.set(runtime, []);
    }
    sectionMap.get(runtime)!.push(category);
  }

  // Convert to Section array with proper ordering
  const orderedRuntimes: RuntimeType[] = ['python', 'react', 'sql'];

  return orderedRuntimes
    .filter(runtime => sectionMap.has(runtime))
    .map(runtime => ({
      name: sectionConfig[runtime].name,
      runtime,
      categories: sectionMap.get(runtime)!
    }));
});

// Get current exercise metadata
export const currentExerciseMetadata = derived(
  [exercises, currentExerciseId],
  ([$exercises, $currentId]) => {
    return $exercises.find(e => e.id === $currentId) || null;
  }
);

/**
 * Get the next exercise ID
 */
export function getNextExerciseId(currentId: string): string | null {
  const allExercises = exerciseManifest.exercises;
  const currentIndex = allExercises.findIndex(e => e.id === currentId);

  if (currentIndex === -1 || currentIndex === allExercises.length - 1) {
    return null;
  }

  return allExercises[currentIndex + 1].id;
}

/**
 * Get the previous exercise ID
 */
export function getPrevExerciseId(currentId: string): string | null {
  const allExercises = exerciseManifest.exercises;
  const currentIndex = allExercises.findIndex(e => e.id === currentId);

  if (currentIndex <= 0) {
    return null;
  }

  return allExercises[currentIndex - 1].id;
}
