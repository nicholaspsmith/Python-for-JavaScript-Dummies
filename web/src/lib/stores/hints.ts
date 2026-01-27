import { writable } from 'svelte/store';

// Store to track if hints are enabled
export const hintsEnabled = writable(false);

// Initialize the global hints() function
export function initHints() {
  if (typeof window !== 'undefined') {
    (window as any).hints = () => {
      hintsEnabled.set(true);
      console.log('🎯 Hints enabled! You now have access to the Hint button on exercises.');
      console.log('💡 Click "Hint" to get progressive help: starter code → pseudocode → solution');
      return 'Hints are now available!';
    };
  }
}
