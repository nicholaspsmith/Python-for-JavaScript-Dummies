<script lang="ts">
  import { progress, completedCount, currentStreak, bestStreak } from '../stores/progress';
  import { totalExercises } from '../stores/exercises';
  import { pyodideReady, pyodideLoading } from '../stores/pyodide';

  $: progressPercent = ($totalExercises > 0)
    ? Math.round(($completedCount / $totalExercises) * 100)
    : 0;
</script>

<header>
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
    <div class="pyodide-status" class:ready={$pyodideReady} class:loading={$pyodideLoading}>
      {#if $pyodideLoading}
        <span class="spinner"></span> Loading Python...
      {:else if $pyodideReady}
        <span class="dot"></span> Python Ready
      {:else}
        <span class="dot error"></span> Python Not Loaded
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
    background: #1e1e1e;
    border-bottom: 1px solid #333;
    gap: 2rem;
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
    color: #fff;
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
    background: #333;
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
    color: #888;
    text-align: center;
  }

  .stats {
    display: flex;
    align-items: center;
    gap: 1.5rem;
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
    color: #888;
    text-transform: uppercase;
    letter-spacing: 0.05em;
  }

  .pyodide-status {
    display: flex;
    align-items: center;
    gap: 0.5rem;
    font-size: 0.75rem;
    color: #888;
    padding: 0.25rem 0.75rem;
    background: #2a2a2a;
    border-radius: 999px;
  }

  .pyodide-status.ready {
    color: #4ade80;
  }

  .pyodide-status.loading {
    color: #fbbf24;
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
    border: 2px solid #fbbf24;
    border-top-color: transparent;
    border-radius: 50%;
    animation: spin 1s linear infinite;
  }

  @keyframes spin {
    to {
      transform: rotate(360deg);
    }
  }
</style>
