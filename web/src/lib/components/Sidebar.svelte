<script lang="ts">
  import { categories, currentExerciseId } from '../stores/exercises';
  import { progress } from '../stores/progress';
  import { createEventDispatcher } from 'svelte';

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
  }

  function getStatus(exerciseId: string): 'completed' | 'current' | 'not-started' {
    if ($progress.completed.includes(exerciseId)) return 'completed';
    if (exerciseId === $currentExerciseId) return 'current';
    if ($progress.savedCode[exerciseId]) return 'current'; // Has saved progress
    return 'not-started';
  }
</script>

<aside>
  <div class="sidebar-header">
    <h2>Exercises</h2>
  </div>

  <nav>
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
  </nav>
</aside>

<style>
  aside {
    width: 280px;
    min-width: 280px;
    background: #1e1e1e;
    border-right: 1px solid #333;
    display: flex;
    flex-direction: column;
    overflow: hidden;
  }

  .sidebar-header {
    padding: 1rem;
    border-bottom: 1px solid #333;
  }

  .sidebar-header h2 {
    margin: 0;
    font-size: 0.875rem;
    font-weight: 600;
    color: #888;
    text-transform: uppercase;
    letter-spacing: 0.05em;
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
    color: #ccc;
    font-size: 0.875rem;
    cursor: pointer;
    border-radius: 4px;
    transition: background 0.15s;
  }

  .category-header:hover {
    background: #2a2a2a;
  }

  .chevron {
    font-size: 0.625rem;
    color: #666;
    width: 12px;
  }

  .category-name {
    flex: 1;
    text-align: left;
    font-weight: 500;
  }

  .category-count {
    font-size: 0.75rem;
    color: #666;
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
    color: #888;
    font-size: 0.8125rem;
    cursor: pointer;
    border-radius: 4px;
    transition: all 0.15s;
    text-align: left;
  }

  .exercise-item:hover {
    background: #2a2a2a;
    color: #ccc;
  }

  .exercise-item.current {
    background: #264f78;
    color: #fff;
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
    color: #666;
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
</style>
