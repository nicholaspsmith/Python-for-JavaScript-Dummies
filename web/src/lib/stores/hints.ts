import { writable } from 'svelte/store';

// Store to track if hints are enabled (enabled by default)
export const hintsEnabled = writable(true);
