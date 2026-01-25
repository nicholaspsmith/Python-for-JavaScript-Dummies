import { writable, get } from 'svelte/store';

// sql.js loading state
export const sqljsReady = writable<boolean>(false);
export const sqljsLoading = writable<boolean>(false);
export const sqljsError = writable<string | null>(null);

// Store the sql.js instance (SQL constructor)
let SQLConstructor: any = null;

/**
 * Initialize sql.js
 */
export async function initSqlJs(): Promise<void> {
  if (SQLConstructor || get(sqljsLoading)) {
    return;
  }

  sqljsLoading.set(true);
  sqljsError.set(null);

  try {
    // Dynamically import sql.js
    const initSqlJs = (await import('sql.js')).default;

    // Initialize with the WASM file from CDN
    SQLConstructor = await initSqlJs({
      locateFile: (file: string) => `https://sql.js.org/dist/${file}`
    });

    sqljsReady.set(true);
    console.log('sql.js loaded successfully');
  } catch (error) {
    const message = error instanceof Error ? error.message : 'Failed to load sql.js';
    sqljsError.set(message);
    console.error('Failed to load sql.js:', error);
    throw error;
  } finally {
    sqljsLoading.set(false);
  }
}

/**
 * Create a new in-memory database
 */
export function createDatabase(): any {
  if (!SQLConstructor) {
    throw new Error('sql.js not initialized');
  }
  return new SQLConstructor.Database();
}

/**
 * Get the SQL constructor for advanced usage
 */
export function getSQLConstructor(): any {
  if (!SQLConstructor) {
    throw new Error('sql.js not initialized');
  }
  return SQLConstructor;
}
