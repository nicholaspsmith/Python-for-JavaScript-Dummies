import { writable, get } from 'svelte/store';
import { browser } from '$app/environment';

// Pyodide loading state
export const pyodideReady = writable<boolean>(false);
export const pyodideLoading = writable<boolean>(false);
export const pyodideError = writable<string | null>(null);

// Store the Pyodide instance
let pyodideInstance: any = null;

// Track if cleanup listener is registered
let cleanupRegistered = false;

/**
 * Initialize Pyodide
 */
export async function initPyodide(): Promise<void> {
  if (pyodideInstance || get(pyodideLoading)) {
    return;
  }

  pyodideLoading.set(true);
  pyodideError.set(null);

  try {
    // Dynamically import Pyodide
    const { loadPyodide } = await import('pyodide');

    pyodideInstance = await loadPyodide({
      indexURL: 'https://cdn.jsdelivr.net/pyodide/v0.29.1/full/'
    });

    pyodideReady.set(true);
    console.log('Pyodide loaded successfully');
  } catch (error) {
    const message = error instanceof Error ? error.message : 'Failed to load Pyodide';
    pyodideError.set(message);
    console.error('Failed to load Pyodide:', error);
    throw error;
  } finally {
    pyodideLoading.set(false);
  }
}

/**
 * Get the Pyodide instance
 */
export function getPyodide(): any {
  if (!pyodideInstance) {
    throw new Error('Pyodide not initialized');
  }
  return pyodideInstance;
}

/**
 * Clean up Pyodide instance and reset state
 */
export function cleanupPyodide(): void {
  if (pyodideInstance) {
    // Pyodide doesn't have a formal destroy method, but we can
    // clear our reference and reset state to allow garbage collection
    pyodideInstance = null;
    pyodideReady.set(false);
    pyodideLoading.set(false);
    pyodideError.set(null);
    console.log('Pyodide cleaned up');
  }
}

/**
 * Register cleanup on page unload (call once on app init)
 */
export function registerPyodideCleanup(): void {
  if (!browser || cleanupRegistered) return;

  cleanupRegistered = true;
  window.addEventListener('beforeunload', () => {
    cleanupPyodide();
  });

  // Also clean up on visibility change to hidden (for mobile)
  document.addEventListener('visibilitychange', () => {
    if (document.visibilityState === 'hidden') {
      // Don't fully clean up on visibility change, just prepare for potential cleanup
      // Full cleanup only on beforeunload
    }
  });
}
