<script lang="ts">
  import { createEventDispatcher } from 'svelte';
  import { progress, completedCount, currentStreak, bestStreak } from '../stores/progress';
  import { totalExercises } from '../stores/exercises';
  import { pyodideReady, pyodideLoading } from '../stores/pyodide';
  import { syncStatus, supabaseConfigured, getShareableLink } from '../stores/supabase';
  import { theme } from '../stores/theme';

  export let sidebarOpen = false;

  const dispatch = createEventDispatcher();

  $: progressPercent = ($totalExercises > 0)
    ? Math.round(($completedCount / $totalExercises) * 100)
    : 0;

  function toggleSidebar() {
    dispatch('toggleSidebar');
  }

  async function shareProgress() {
    const link = getShareableLink();
    if (link) {
      try {
        await navigator.clipboard.writeText(link);
        alert('Share link copied to clipboard!');
      } catch {
        prompt('Copy this link to share your progress:', link);
      }
    }
  }
</script>

<header>
  <button class="menu-toggle" on:click={toggleSidebar} aria-label="Toggle sidebar">
    {#if sidebarOpen}
      <svg width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2">
        <path d="M18 6L6 18M6 6l12 12"/>
      </svg>
    {:else}
      <svg width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2">
        <path d="M3 12h18M3 6h18M3 18h18"/>
      </svg>
    {/if}
  </button>

  <div class="logo">
    <span class="icon">🐍</span>
    <h1>Python Practice</h1>
  </div>

  <div class="progress-section">
    <div class="progress-bar">
      <div class="progress-fill" style="width: {progressPercent}%"></div>
    </div>
    <span class="progress-text">{$completedCount}/{$totalExercises} completed ({progressPercent}%)</span>
  </div>

  <div class="stats">
    <div class="stat">
      <span class="stat-value">{$currentStreak}</span>
      <span class="stat-label">Streak</span>
    </div>
    <div class="stat">
      <span class="stat-value">{$bestStreak}</span>
      <span class="stat-label">Best</span>
    </div>

    {#if $supabaseConfigured}
      <button
        class="sync-status"
        class:syncing={$syncStatus === 'syncing'}
        class:synced={$syncStatus === 'synced'}
        class:error={$syncStatus === 'error'}
        class:offline={$syncStatus === 'offline'}
        on:click={shareProgress}
        title="Click to copy share link"
      >
        {#if $syncStatus === 'syncing'}
          <span class="spinner"></span>
          <span class="sync-text">Syncing</span>
        {:else if $syncStatus === 'synced'}
          <svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2">
            <path d="M12 2C6.48 2 2 6.48 2 12s4.48 10 10 10 10-4.48 10-10S17.52 2 12 2zm-2 15l-5-5 1.41-1.41L10 14.17l7.59-7.59L19 8l-9 9z"/>
          </svg>
          <span class="sync-text">Synced</span>
        {:else if $syncStatus === 'error'}
          <svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2">
            <circle cx="12" cy="12" r="10"/>
            <path d="M12 8v4M12 16h.01"/>
          </svg>
          <span class="sync-text">Error</span>
        {:else}
          <svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2">
            <path d="M18.36 6.64a9 9 0 11-12.73 0"/>
            <path d="M12 2v10"/>
          </svg>
          <span class="sync-text">Offline</span>
        {/if}
      </button>
    {/if}

    <button class="theme-toggle" on:click={() => theme.toggle()} aria-label="Toggle theme">
      {#if $theme === 'dark'}
        <svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2">
          <circle cx="12" cy="12" r="5"/>
          <line x1="12" y1="1" x2="12" y2="3"/>
          <line x1="12" y1="21" x2="12" y2="23"/>
          <line x1="4.22" y1="4.22" x2="5.64" y2="5.64"/>
          <line x1="18.36" y1="18.36" x2="19.78" y2="19.78"/>
          <line x1="1" y1="12" x2="3" y2="12"/>
          <line x1="21" y1="12" x2="23" y2="12"/>
          <line x1="4.22" y1="19.78" x2="5.64" y2="18.36"/>
          <line x1="18.36" y1="5.64" x2="19.78" y2="4.22"/>
        </svg>
      {:else}
        <svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2">
          <path d="M21 12.79A9 9 0 1 1 11.21 3 7 7 0 0 0 21 12.79z"/>
        </svg>
      {/if}
    </button>

    <div class="pyodide-status" class:ready={$pyodideReady} class:loading={$pyodideLoading}>
      {#if $pyodideLoading}
        <span class="spinner"></span>
        <span class="status-text">Loading Python...</span>
      {:else if $pyodideReady}
        <span class="dot"></span>
        <span class="status-text">Python Ready</span>
      {:else}
        <span class="dot error"></span>
        <span class="status-text">Python Not Loaded</span>
      {/if}
    </div>
  </div>
</header>

<style>
  header {
    display: flex;
    align-items: center;
    justify-content: space-between;
    padding: 0.75rem 1.5rem;
    background: var(--bg-primary);
    border-bottom: 1px solid var(--border-color);
    gap: 1rem;
  }

  .menu-toggle {
    display: none;
    background: none;
    border: none;
    color: var(--text-secondary);
    cursor: pointer;
    padding: 0.5rem;
    border-radius: 4px;
    transition: background 0.15s;
  }

  .menu-toggle:hover {
    background: var(--bg-active);
  }

  .logo {
    display: flex;
    align-items: center;
    gap: 0.5rem;
  }

  .logo .icon {
    font-size: 1.5rem;
  }

  .logo h1 {
    font-size: 1.25rem;
    font-weight: 600;
    color: var(--text-primary);
    margin: 0;
  }

  .progress-section {
    flex: 1;
    max-width: 400px;
    display: flex;
    flex-direction: column;
    gap: 0.25rem;
  }

  .progress-bar {
    height: 8px;
    background: var(--bg-active);
    border-radius: 4px;
    overflow: hidden;
  }

  .progress-fill {
    height: 100%;
    background: linear-gradient(90deg, #4ade80, #22c55e);
    transition: width 0.3s ease;
  }

  .progress-text {
    font-size: 0.75rem;
    color: var(--text-tertiary);
    text-align: center;
  }

  .stats {
    display: flex;
    align-items: center;
    gap: 1rem;
  }

  .stat {
    display: flex;
    flex-direction: column;
    align-items: center;
    gap: 0.125rem;
  }

  .stat-value {
    font-size: 1.25rem;
    font-weight: bold;
    color: #fbbf24;
  }

  .stat-label {
    font-size: 0.625rem;
    color: var(--text-tertiary);
    text-transform: uppercase;
    letter-spacing: 0.05em;
  }

  .sync-status {
    display: flex;
    align-items: center;
    gap: 0.375rem;
    font-size: 0.75rem;
    color: var(--text-tertiary);
    padding: 0.25rem 0.75rem;
    background: var(--bg-hover);
    border: 1px solid var(--border-color);
    border-radius: 999px;
    cursor: pointer;
    transition: all 0.15s;
  }

  .sync-status:hover {
    background: var(--bg-active);
  }

  .sync-status.synced {
    color: #4ade80;
    border-color: #4ade80;
  }

  .sync-status.syncing {
    color: #fbbf24;
    border-color: #fbbf24;
  }

  .sync-status.error {
    color: #f87171;
    border-color: #f87171;
  }

  .sync-status.offline {
    color: var(--text-tertiary);
  }

  .sync-text {
    display: inline;
  }

  .theme-toggle {
    display: flex;
    align-items: center;
    justify-content: center;
    padding: 0.375rem;
    background: var(--bg-hover);
    border: 1px solid var(--border-color);
    border-radius: 6px;
    color: var(--text-tertiary);
    cursor: pointer;
    transition: all 0.15s;
  }

  .theme-toggle:hover {
    background: var(--bg-active);
    color: var(--text-primary);
  }

  .pyodide-status {
    display: flex;
    align-items: center;
    gap: 0.5rem;
    font-size: 0.75rem;
    color: var(--text-tertiary);
    padding: 0.25rem 0.75rem;
    background: var(--bg-hover);
    border-radius: 999px;
  }

  .pyodide-status.ready {
    color: #4ade80;
  }

  .pyodide-status.loading {
    color: #fbbf24;
  }

  .status-text {
    display: inline;
  }

  .dot {
    width: 8px;
    height: 8px;
    border-radius: 50%;
    background: #4ade80;
  }

  .dot.error {
    background: #f87171;
  }

  .spinner {
    width: 12px;
    height: 12px;
    border: 2px solid currentColor;
    border-top-color: transparent;
    border-radius: 50%;
    animation: spin 1s linear infinite;
  }

  @keyframes spin {
    to {
      transform: rotate(360deg);
    }
  }

  /* Tablet */
  @media (max-width: 1024px) {
    .progress-section {
      max-width: 250px;
    }

    .stats {
      gap: 0.75rem;
    }

    .status-text {
      display: none;
    }
  }

  /* Mobile */
  @media (max-width: 768px) {
    header {
      padding: 0.5rem 1rem;
      gap: 0.75rem;
    }

    .menu-toggle {
      display: flex;
      align-items: center;
      justify-content: center;
    }

    .logo h1 {
      font-size: 1rem;
    }

    .logo .icon {
      font-size: 1.25rem;
    }

    .progress-section {
      display: none;
    }

    .stat {
      min-width: 40px;
    }

    .stat-value {
      font-size: 1rem;
    }

    .sync-text {
      display: none;
    }

    .pyodide-status {
      padding: 0.25rem 0.5rem;
    }
  }

  /* Small mobile */
  @media (max-width: 480px) {
    .logo h1 {
      display: none;
    }

    .stat-label {
      display: none;
    }

    .pyodide-status {
      display: none;
    }
  }
</style>
