import { createClient, type SupabaseClient, type User } from '@supabase/supabase-js';
import { writable, derived, get } from 'svelte/store';

// Supabase client - initialized lazily
let supabaseClient: SupabaseClient | null = null;

// Auth stores
export const user = writable<User | null>(null);
export const isAuthenticated = derived(user, $user => $user !== null);
export const syncStatus = writable<'idle' | 'syncing' | 'synced' | 'offline' | 'error'>('idle');
export const supabaseConfigured = writable<boolean>(false);

/**
 * Get Supabase configuration from environment
 */
function getConfig(): { url: string; anonKey: string } | null {
  // Check for environment variables (Vite style)
  const url = import.meta.env.PUBLIC_SUPABASE_URL || import.meta.env.VITE_SUPABASE_URL;
  const anonKey = import.meta.env.PUBLIC_SUPABASE_ANON_KEY || import.meta.env.VITE_SUPABASE_ANON_KEY;

  if (url && anonKey) {
    return { url, anonKey };
  }

  return null;
}

/**
 * Initialize the Supabase client
 */
export function initSupabase(): SupabaseClient | null {
  if (supabaseClient) return supabaseClient;

  const config = getConfig();
  if (!config) {
    console.log('Supabase not configured - using local storage only');
    supabaseConfigured.set(false);
    return null;
  }

  supabaseClient = createClient(config.url, config.anonKey, {
    auth: {
      persistSession: true,
      autoRefreshToken: true,
      detectSessionInUrl: true
    }
  });

  supabaseConfigured.set(true);
  return supabaseClient;
}

/**
 * Get the Supabase client (must call initSupabase first)
 */
export function getSupabase(): SupabaseClient | null {
  return supabaseClient;
}

/**
 * Sign in anonymously
 */
export async function signInAnonymously(): Promise<User | null> {
  const client = getSupabase();
  if (!client) return null;

  try {
    syncStatus.set('syncing');

    // Check for existing session first
    const { data: { session } } = await client.auth.getSession();
    if (session?.user) {
      user.set(session.user);
      syncStatus.set('synced');
      return session.user;
    }

    // Create anonymous session
    const { data, error } = await client.auth.signInAnonymously();
    if (error) throw error;

    user.set(data.user);
    syncStatus.set('synced');
    return data.user;
  } catch (error) {
    console.error('Anonymous sign-in failed:', error);
    syncStatus.set('error');
    return null;
  }
}

/**
 * Initialize auth - check for existing session and set up listener
 */
export async function initAuth(): Promise<void> {
  const client = initSupabase();
  if (!client) {
    syncStatus.set('offline');
    return;
  }

  // Listen for auth changes
  client.auth.onAuthStateChange((event, session) => {
    user.set(session?.user ?? null);
    if (session?.user) {
      syncStatus.set('synced');
    }
  });

  // Sign in anonymously if no session
  await signInAnonymously();
}

/**
 * Generate a shareable link for syncing progress across devices
 */
export function getShareableLink(): string | null {
  const currentUser = get(user);
  if (!currentUser) return null;

  const baseUrl = typeof window !== 'undefined' ? window.location.origin : '';
  return `${baseUrl}?sync=${currentUser.id}`;
}

/**
 * Sync with another user's progress via their ID
 */
export async function syncWithUser(userId: string): Promise<boolean> {
  const client = getSupabase();
  if (!client) return false;

  try {
    // This would need a custom RPC or edge function in Supabase
    // For now, we'll store the link target in localStorage and merge on next load
    if (typeof localStorage !== 'undefined') {
      localStorage.setItem('sync-target-user', userId);
    }
    return true;
  } catch (error) {
    console.error('Failed to sync with user:', error);
    return false;
  }
}

/**
 * Get user ID for database operations
 */
export function getUserId(): string | null {
  const currentUser = get(user);
  return currentUser?.id ?? null;
}
