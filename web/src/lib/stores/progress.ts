import { writable, derived, get } from 'svelte/store';
import type { Progress } from '../types';

const STORAGE_KEY = 'python-practice-progress';

const defaultProgress: Progress = {
  currentExercise: '1.1',
  completed: [],
  attempts: {},
  streak: 0,
  bestStreak: 0,
  savedCode: {}
};

function loadFromStorage(): Progress {
  if (typeof localStorage === 'undefined') return defaultProgress;

  try {
    const stored = localStorage.getItem(STORAGE_KEY);
    if (stored) {
      return { ...defaultProgress, ...JSON.parse(stored) };
    }
  } catch (e) {
    console.error('Failed to load progress:', e);
  }
  return defaultProgress;
}

function saveToStorage(progress: Progress) {
  if (typeof localStorage === 'undefined') return;

  try {
    localStorage.setItem(STORAGE_KEY, JSON.stringify(progress));
  } catch (e) {
    console.error('Failed to save progress:', e);
  }
}

function createProgressStore() {
  const { subscribe, set, update } = writable<Progress>(defaultProgress);

  return {
    subscribe,

    init() {
      set(loadFromStorage());
    },

    setCurrentExercise(exerciseId: string) {
      update(p => {
        const newProgress = { ...p, currentExercise: exerciseId };
        saveToStorage(newProgress);
        return newProgress;
      });
    },

    markCompleted(exerciseId: string) {
      update(p => {
        const completed = p.completed.includes(exerciseId)
          ? p.completed
          : [...p.completed, exerciseId];
        const streak = p.streak + 1;
        const bestStreak = Math.max(streak, p.bestStreak);

        const newProgress = {
          ...p,
          completed,
          streak,
          bestStreak
        };
        saveToStorage(newProgress);
        return newProgress;
      });
    },

    incrementAttempts(exerciseId: string) {
      update(p => {
        const attempts = {
          ...p.attempts,
          [exerciseId]: (p.attempts[exerciseId] || 0) + 1
        };
        const newProgress = { ...p, attempts };
        saveToStorage(newProgress);
        return newProgress;
      });
    },

    resetStreak() {
      update(p => {
        const newProgress = { ...p, streak: 0 };
        saveToStorage(newProgress);
        return newProgress;
      });
    },

    saveCode(exerciseId: string, code: string) {
      update(p => {
        const savedCode = { ...p.savedCode, [exerciseId]: code };
        const newProgress = { ...p, savedCode };
        saveToStorage(newProgress);
        return newProgress;
      });
    },

    getSavedCode(exerciseId: string): string | undefined {
      return get({ subscribe }).savedCode[exerciseId];
    },

    getAttempts(exerciseId: string): number {
      return get({ subscribe }).attempts[exerciseId] || 0;
    },

    isCompleted(exerciseId: string): boolean {
      return get({ subscribe }).completed.includes(exerciseId);
    },

    reset() {
      set(defaultProgress);
      saveToStorage(defaultProgress);
    }
  };
}

export const progress = createProgressStore();

// Derived stores for convenience
export const completedCount = derived(progress, $p => $p.completed.length);
export const currentStreak = derived(progress, $p => $p.streak);
export const bestStreak = derived(progress, $p => $p.bestStreak);
