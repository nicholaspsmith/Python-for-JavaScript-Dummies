<script lang="ts">
  import { categories, currentExerciseId } from '../stores/exercises';
  import { progress } from '../stores/progress';
  import { createEventDispatcher } from 'svelte';

  export let isOpen = false;
  export let collapsed = false;

  const dispatch = createEventDispatcher();

  let expandedCategories: Set<string> = new Set();

  // Expand the category of the current exercise by default
  $: {
    const currentMeta = $categories
      .flatMap(c => c.exercises)
      .find(e => e.id === $currentExerciseId);
    if (currentMeta) {
      expandedCategories.add(currentMeta.categoryFolder);
      expandedCategories = expandedCategories;
    }
  }

  function toggleCategory(folder: string) {
    if (expandedCategories.has(folder)) {
      expandedCategories.delete(folder);
    } else {
      expandedCategories.add(folder);
    }
    expandedCategories = expandedCategories;
  }

  function selectExercise(id: string) {
    dispatch('select', { id });
    // Close sidebar on mobile after selection
    dispatch('close');
  }

  function handleBackdropClick() {
    dispatch('close');
  }

  function getStatus(exerciseId: string): 'completed' | 'current' | 'not-started' {
    if ($progress.completed.includes(exerciseId)) return 'completed';
    if (exerciseId === $currentExerciseId) return 'current';
    if ($progress.savedCode[exerciseId]) return 'current'; // Has saved progress
    return 'not-started';
  }
</script>

<!-- Backdrop for mobile -->
{#if isOpen}
  <div class="backdrop" on:click={handleBackdropClick} on:keydown={() => {}} role="button" tabindex="-1"></div>
{/if}

<aside class:open={isOpen} class:collapsed>
  <div class="sidebar-header">
    {#if !collapsed}
      <h2>Exercises</h2>
    {/if}
    <button class="collapse-btn" on:click={() => dispatch('toggleCollapse')} aria-label={collapsed ? 'Expand sidebar' : 'Collapse sidebar'}>
      <svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2">
        {#if collapsed}
          <path d="M9 18l6-6-6-6"/>
        {:else}
          <path d="M15 18l-6-6 6-6"/>
        {/if}
      </svg>
    </button>
    <button class="close-btn" on:click={() => dispatch('close')} aria-label="Close sidebar">
      <svg width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2">
        <path d="M18 6L6 18M6 6l12 12"/>
      </svg>
    </button>
  </div>

  <nav>
    {#if collapsed}
      <!-- Collapsed view: show only exercise IDs -->
      {#each $categories as category}
        {#each category.exercises as exercise}
          {@const status = getStatus(exercise.id)}
          <button
            class="collapsed-item"
            class:completed={status === 'completed'}
            class:current={exercise.id === $currentExerciseId}
            on:click={() => selectExercise(exercise.id)}
            title={exercise.name}
          >
            <span class="collapsed-id">{exercise.id}</span>
          </button>
        {/each}
      {/each}
    {:else}
      {#each $categories as category}
        <div class="category">
          <button
            class="category-header"
            class:expanded={expandedCategories.has(category.folder)}
            on:click={() => toggleCategory(category.folder)}
          >
            <span class="chevron">
              {expandedCategories.has(category.folder) ? '▼' : '▶'}
            </span>
            <span class="category-name">{category.name}</span>
            <span class="category-count">
              {category.exercises.filter(e => $progress.completed.includes(e.id)).length}/{category.exercises.length}
            </span>
          </button>

          {#if expandedCategories.has(category.folder)}
            <ul class="exercise-list">
              {#each category.exercises as exercise}
                {@const status = getStatus(exercise.id)}
                <li>
                  <button
                    class="exercise-item"
                    class:completed={status === 'completed'}
                    class:current={exercise.id === $currentExerciseId}
                    on:click={() => selectExercise(exercise.id)}
                  >
                    <span class="status-icon">
                      {#if status === 'completed'}
                        ✓
                      {:else if exercise.id === $currentExerciseId}
                        →
                      {:else}
                        ○
                      {/if}
                    </span>
                    <span class="exercise-id">{exercise.id}</span>
                    <span class="exercise-name">{exercise.name}</span>
                  </button>
                </li>
              {/each}
            </ul>
          {/if}
        </div>
      {/each}
    {/if}
  </nav>
</aside>

<style>
  .backdrop {
    display: none;
  }

  aside {
    width: 280px;
    min-width: 280px;
    background: var(--bg-primary);
    border-right: 1px solid var(--border-color);
    display: flex;
    flex-direction: column;
    overflow: hidden;
    transition: width 0.2s ease, min-width 0.2s ease;
  }

  aside.collapsed {
    width: 56px;
    min-width: 56px;
  }

  .sidebar-header {
    padding: 1rem;
    border-bottom: 1px solid var(--border-color);
    display: flex;
    align-items: center;
    justify-content: space-between;
  }

  .sidebar-header h2 {
    margin: 0;
    font-size: 0.875rem;
    font-weight: 600;
    color: var(--text-tertiary);
    text-transform: uppercase;
    letter-spacing: 0.05em;
  }

  .collapse-btn {
    display: flex;
    align-items: center;
    justify-content: center;
    background: none;
    border: none;
    color: var(--text-tertiary);
    cursor: pointer;
    padding: 0.25rem;
    border-radius: 4px;
    transition: all 0.15s;
    margin-left: auto;
  }

  .collapse-btn:hover {
    background: var(--bg-active);
    color: var(--text-primary);
  }

  .collapsed .collapse-btn {
    margin: 0 auto;
  }

  .close-btn {
    display: none;
    background: none;
    border: none;
    color: var(--text-tertiary);
    cursor: pointer;
    padding: 0.25rem;
    border-radius: 4px;
    transition: all 0.15s;
  }

  .close-btn:hover {
    background: var(--bg-active);
    color: var(--text-primary);
  }

  nav {
    flex: 1;
    overflow-y: auto;
    padding: 0.5rem;
  }

  .category {
    margin-bottom: 0.25rem;
  }

  .category-header {
    width: 100%;
    display: flex;
    align-items: center;
    gap: 0.5rem;
    padding: 0.5rem 0.75rem;
    background: none;
    border: none;
    color: var(--text-secondary);
    font-size: 0.875rem;
    cursor: pointer;
    border-radius: 4px;
    transition: background 0.15s;
  }

  .category-header:hover {
    background: var(--bg-hover);
  }

  .chevron {
    font-size: 0.625rem;
    color: var(--text-muted);
    width: 12px;
  }

  .category-name {
    flex: 1;
    text-align: left;
    font-weight: 500;
  }

  .category-count {
    font-size: 0.75rem;
    color: var(--text-muted);
  }

  .exercise-list {
    list-style: none;
    margin: 0;
    padding: 0 0 0 1.25rem;
  }

  .exercise-item {
    width: 100%;
    display: flex;
    align-items: center;
    gap: 0.5rem;
    padding: 0.375rem 0.75rem;
    background: none;
    border: none;
    color: var(--text-tertiary);
    font-size: 0.8125rem;
    cursor: pointer;
    border-radius: 4px;
    transition: all 0.15s;
    text-align: left;
  }

  .exercise-item:hover {
    background: var(--bg-hover);
    color: var(--text-secondary);
  }

  .exercise-item.current {
    background: var(--selection-bg);
    color: var(--text-primary);
  }

  .exercise-item.completed {
    color: #4ade80;
  }

  .exercise-item.completed:hover {
    color: #4ade80;
  }

  .status-icon {
    width: 16px;
    text-align: center;
    font-size: 0.75rem;
  }

  .exercise-item.completed .status-icon {
    color: #4ade80;
  }

  .exercise-item.current .status-icon {
    color: #60a5fa;
  }

  .exercise-id {
    font-family: monospace;
    font-size: 0.75rem;
    color: var(--text-muted);
    min-width: 2rem;
  }

  .exercise-item.current .exercise-id {
    color: #93c5fd;
  }

  .exercise-name {
    flex: 1;
    white-space: nowrap;
    overflow: hidden;
    text-overflow: ellipsis;
  }

  /* Collapsed view styles */
  .collapsed-item {
    display: flex;
    align-items: center;
    justify-content: center;
    width: 40px;
    height: 32px;
    margin: 0.125rem auto;
    background: none;
    border: none;
    color: var(--text-tertiary);
    font-size: 0.6875rem;
    font-family: monospace;
    cursor: pointer;
    border-radius: 4px;
    transition: all 0.15s;
  }

  .collapsed-item:hover {
    background: var(--bg-hover);
    color: var(--text-secondary);
  }

  .collapsed-item.current {
    background: var(--selection-bg);
    color: var(--text-primary);
  }

  .collapsed-item.completed {
    color: #4ade80;
  }

  .collapsed-id {
    font-weight: 500;
  }

  /* Tablet */
  @media (max-width: 1024px) {
    aside {
      width: 240px;
      min-width: 240px;
    }
  }

  /* Mobile */
  @media (max-width: 768px) {
    .backdrop {
      display: block;
      position: fixed;
      inset: 0;
      background: rgba(0, 0, 0, 0.5);
      z-index: 40;
    }

    aside {
      position: fixed;
      top: 0;
      left: 0;
      bottom: 0;
      width: 280px;
      min-width: 280px;
      z-index: 50;
      transform: translateX(-100%);
      transition: transform 0.3s ease;
    }

    /* Override collapsed state on mobile */
    aside.collapsed {
      width: 280px;
      min-width: 280px;
    }

    aside.open {
      transform: translateX(0);
    }

    .collapse-btn {
      display: none;
    }

    .close-btn {
      display: flex;
      align-items: center;
      justify-content: center;
    }
  }
</style>
