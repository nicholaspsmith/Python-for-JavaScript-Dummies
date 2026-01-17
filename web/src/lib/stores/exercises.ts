import { writable, derived } from 'svelte/store';
import type { ExerciseMetadata, ExerciseManifest, Category } from '../types';
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
