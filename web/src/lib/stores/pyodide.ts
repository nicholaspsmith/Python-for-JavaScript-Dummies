import { writable, get } from 'svelte/store';

// Pyodide loading state
export const pyodideReady = writable<boolean>(false);
export const pyodideLoading = writable<boolean>(false);
export const pyodideError = writable<string | null>(null);

// Store the Pyodide instance
let pyodideInstance: any = null;

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
