import { writable } from 'svelte/store';

export type Theme = 'light' | 'dark';

const STORAGE_KEY = 'python-practice-theme';

function getInitialTheme(): Theme {
  if (typeof localStorage === 'undefined') return 'dark';

  // Check localStorage first
  const stored = localStorage.getItem(STORAGE_KEY);
  if (stored === 'light' || stored === 'dark') {
    return stored;
  }

  // Fall back to system preference
  if (typeof window !== 'undefined' && window.matchMedia) {
    if (window.matchMedia('(prefers-color-scheme: light)').matches) {
      return 'light';
    }
  }

  return 'dark';
}

function createThemeStore() {
  const { subscribe, set, update } = writable<Theme>('dark');

  return {
    subscribe,

    init() {
      const initialTheme = getInitialTheme();
      set(initialTheme);
      applyTheme(initialTheme);
    },

    toggle() {
      update(current => {
        const newTheme: Theme = current === 'dark' ? 'light' : 'dark';
        saveTheme(newTheme);
        applyTheme(newTheme);
        return newTheme;
      });
    },

    set(newTheme: Theme) {
      set(newTheme);
      saveTheme(newTheme);
      applyTheme(newTheme);
    }
  };
}

function saveTheme(theme: Theme) {
  if (typeof localStorage === 'undefined') return;
  localStorage.setItem(STORAGE_KEY, theme);
}

function applyTheme(theme: Theme) {
  if (typeof document === 'undefined') return;
  document.documentElement.setAttribute('data-theme', theme);
}

export const theme = createThemeStore();
