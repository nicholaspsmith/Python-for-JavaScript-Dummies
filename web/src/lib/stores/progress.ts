import { writable, derived, get } from 'svelte/store';
import type { Progress } from '../types';
import { getSupabase, getUserId, syncStatus, supabaseConfigured } from './supabase';

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

// Debounce cloud sync to avoid too many requests
let syncTimeout: ReturnType<typeof setTimeout> | null = null;

/**
 * Cancel any pending sync timeout
 */
export function cancelPendingSync(): void {
  if (syncTimeout) {
    clearTimeout(syncTimeout);
    syncTimeout = null;
  }
}

async function syncToCloud(progress: Progress) {
  const client = getSupabase();
  const userId = getUserId();

  if (!client || !userId) return;

  // Debounce sync calls
  if (syncTimeout) {
    clearTimeout(syncTimeout);
  }

  syncTimeout = setTimeout(async () => {
    try {
      syncStatus.set('syncing');

      const { error } = await client
        .from('user_progress')
        .upsert({
          user_id: userId,
          current_exercise: progress.currentExercise,
          completed: progress.completed,
          attempts: progress.attempts,
          streak: progress.streak,
          best_streak: progress.bestStreak,
          saved_code: progress.savedCode
        }, {
          onConflict: 'user_id'
        });

      if (error) throw error;
      syncStatus.set('synced');
    } catch (e) {
      console.error('Failed to sync to cloud:', e);
      syncStatus.set('error');
    }
  }, 1000);
}

async function loadFromCloud(): Promise<Progress | null> {
  const client = getSupabase();
  const userId = getUserId();

  if (!client || !userId) return null;

  try {
    syncStatus.set('syncing');

    const { data, error } = await client
      .from('user_progress')
      .select('*')
      .eq('user_id', userId)
      .single();

    if (error && error.code !== 'PGRST116') { // PGRST116 = no rows found
      throw error;
    }

    syncStatus.set('synced');

    if (data) {
      return {
        currentExercise: data.current_exercise || '1.1',
        completed: data.completed || [],
        attempts: data.attempts || {},
        streak: data.streak || 0,
        bestStreak: data.best_streak || 0,
        savedCode: data.saved_code || {}
      };
    }

    return null;
  } catch (e) {
    console.error('Failed to load from cloud:', e);
    syncStatus.set('error');
    return null;
  }
}

function mergeProgress(local: Progress, cloud: Progress | null): Progress {
  if (!cloud) return local;

  // Merge completed exercises (union)
  const completedSet = new Set([...local.completed, ...cloud.completed]);

  // Merge attempts (take max)
  const attempts: Record<string, number> = { ...local.attempts };
  for (const [id, count] of Object.entries(cloud.attempts)) {
    attempts[id] = Math.max(attempts[id] || 0, count);
  }

  // Merge saved code (prefer cloud if exists, else local)
  const savedCode = { ...local.savedCode, ...cloud.savedCode };

  return {
    currentExercise: cloud.currentExercise || local.currentExercise,
    completed: Array.from(completedSet),
    attempts,
    streak: Math.max(local.streak, cloud.streak),
    bestStreak: Math.max(local.bestStreak, cloud.bestStreak),
    savedCode
  };
}

function createProgressStore() {
  const { subscribe, set, update } = writable<Progress>(defaultProgress);
  let initialized = false;

  return {
    subscribe,

    async init() {
      if (initialized) return;
      initialized = true;

      const localProgress = loadFromStorage();
      set(localProgress);

      // If Supabase is configured, try to load from cloud
      if (get(supabaseConfigured)) {
        const cloudProgress = await loadFromCloud();
        const merged = mergeProgress(localProgress, cloudProgress);

        set(merged);
        saveToStorage(merged);

        // Sync merged data back to cloud
        if (cloudProgress === null || JSON.stringify(merged) !== JSON.stringify(cloudProgress)) {
          await syncToCloud(merged);
        }
      }
    },

    setCurrentExercise(exerciseId: string) {
      update(p => {
        const newProgress = { ...p, currentExercise: exerciseId };
        saveToStorage(newProgress);
        syncToCloud(newProgress);
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
        syncToCloud(newProgress);
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
        syncToCloud(newProgress);
        return newProgress;
      });
    },

    resetStreak() {
      update(p => {
        const newProgress = { ...p, streak: 0 };
        saveToStorage(newProgress);
        syncToCloud(newProgress);
        return newProgress;
      });
    },

    saveCode(exerciseId: string, code: string) {
      update(p => {
        const savedCode = { ...p.savedCode, [exerciseId]: code };
        const newProgress = { ...p, savedCode };
        saveToStorage(newProgress);
        syncToCloud(newProgress);
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
      syncToCloud(defaultProgress);
    },

    // Force reload from cloud
    async refreshFromCloud() {
      const cloudProgress = await loadFromCloud();
      if (cloudProgress) {
        set(cloudProgress);
        saveToStorage(cloudProgress);
      }
    }
  };
}

export const progress = createProgressStore();

// Derived stores for convenience
export const completedCount = derived(progress, $p => $p.completed.length);
export const currentStreak = derived(progress, $p => $p.streak);
export const bestStreak = derived(progress, $p => $p.bestStreak);
export const currentExerciseId = derived(progress, $p => $p.currentExercise);
