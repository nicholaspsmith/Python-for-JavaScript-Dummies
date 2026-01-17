<script lang="ts">
  import { createEventDispatcher } from 'svelte';
  import type { ParsedExercise, ExerciseMetadata, TestResult } from '../types';
  import CodeEditor from './CodeEditor.svelte';
  import TestResults from './TestResults.svelte';
  import { pyodideReady } from '../stores/pyodide';

  export let exercise: ParsedExercise | null = null;
  export let metadata: ExerciseMetadata | null = null;
  export let savedCode: string | undefined = undefined;
  export let testResult: TestResult | null = null;
  export let isRunning: boolean = false;
  export let jsHabits: string[] = [];

  const dispatch = createEventDispatcher();

  let codeEditor: CodeEditor;
  let instructionsExpanded = false;

  $: currentCode = savedCode ?? exercise?.codeTemplate ?? '';

  function handleCodeChange(event: CustomEvent<{ value: string }>) {
    dispatch('codeChange', { value: event.detail.value });
  }

  function handleCodeSave(event: CustomEvent<{ value: string }>) {
    dispatch('codeSave', { value: event.detail.value });
  }

  function handleRun() {
    dispatch('run');
  }

  function handleNext() {
    dispatch('next');
  }

  function handleReset() {
    if (exercise && codeEditor) {
      codeEditor.reset(exercise.codeTemplate);
      dispatch('codeChange', { value: exercise.codeTemplate });
      dispatch('codeSave', { value: exercise.codeTemplate });
    }
  }

  function toggleInstructions() {
    instructionsExpanded = !instructionsExpanded;
  }

  export function getCode(): string {
    return codeEditor?.getValue() || currentCode;
  }
</script>

<div class="exercise-view">
  <!-- Instructions Panel -->
  <div class="instructions-panel" class:expanded={instructionsExpanded}>
    {#if metadata}
      <button class="exercise-header" on:click={toggleInstructions}>
        <div class="header-left">
          <span class="exercise-number">{metadata.id}</span>
          <h2>{metadata.name}</h2>
        </div>
        <div class="header-right">
          <span class="category-badge">{metadata.category}</span>
          <span class="expand-icon">
            {instructionsExpanded ? '▼' : '▶'}
          </span>
        </div>
      </button>
    {/if}

    <div class="instructions-content">
      {#if exercise}
        <pre class="instructions">{exercise.instructions}</pre>
      {:else}
        <div class="loading">Loading exercise...</div>
      {/if}
    </div>
  </div>

  <!-- Editor Panel -->
  <div class="editor-panel">
    <div class="editor-toolbar">
      <div class="toolbar-left">
        <span class="file-icon">📝</span>
        <span class="file-name">{metadata?.filename || 'exercise.py'}</span>
      </div>
      <div class="toolbar-right">
        <button class="btn btn-secondary" on:click={handleReset} disabled={!exercise}>
          Reset
        </button>
        {#if testResult?.success}
          <button
            class="btn btn-success"
            on:click={handleNext}
          >
            Next →
          </button>
        {:else}
          <button
            class="btn btn-primary"
            on:click={handleRun}
            disabled={!$pyodideReady || isRunning || !exercise}
          >
            {#if isRunning}
              Running...
            {:else if !$pyodideReady}
              Loading Python...
            {:else}
              Check Answer
            {/if}
          </button>
        {/if}
      </div>
    </div>

    <div class="editor-wrapper">
      <CodeEditor
        bind:this={codeEditor}
        value={currentCode}
        on:change={handleCodeChange}
        on:save={handleCodeSave}
        on:run={handleRun}
      />
    </div>

    <TestResults result={testResult} {isRunning} {jsHabits} />
  </div>
</div>

<style>
  .exercise-view {
    flex: 1;
    display: flex;
    overflow: hidden;
  }

  .instructions-panel {
    width: 400px;
    min-width: 300px;
    max-width: 500px;
    background: var(--bg-secondary);
    border-right: 1px solid var(--border-color);
    display: flex;
    flex-direction: column;
    overflow: hidden;
  }

  .exercise-header {
    width: 100%;
    padding: 1rem;
    border: none;
    border-bottom: 1px solid var(--border-color);
    background: none;
    display: flex;
    align-items: center;
    justify-content: space-between;
    gap: 0.75rem;
    cursor: default;
    text-align: left;
  }

  .header-left {
    display: flex;
    align-items: center;
    gap: 0.75rem;
    flex: 1;
    min-width: 0;
  }

  .header-right {
    display: flex;
    align-items: center;
    gap: 0.5rem;
  }

  .expand-icon {
    display: none;
    font-size: 0.75rem;
    color: var(--text-tertiary);
  }

  .exercise-number {
    font-size: 0.875rem;
    font-weight: 600;
    color: #60a5fa;
    background: #1e3a5f;
    padding: 0.25rem 0.5rem;
    border-radius: 4px;
    font-family: monospace;
    flex-shrink: 0;
  }

  .exercise-header h2 {
    margin: 0;
    font-size: 1.125rem;
    font-weight: 600;
    color: var(--text-primary);
    white-space: nowrap;
    overflow: hidden;
    text-overflow: ellipsis;
  }

  .category-badge {
    font-size: 0.6875rem;
    color: var(--text-tertiary);
    background: var(--bg-active);
    padding: 0.25rem 0.5rem;
    border-radius: 999px;
    text-transform: uppercase;
    letter-spacing: 0.05em;
    flex-shrink: 0;
  }

  .instructions-content {
    flex: 1;
    overflow-y: auto;
    padding: 1rem;
  }

  .instructions {
    margin: 0;
    font-size: 0.875rem;
    line-height: 1.6;
    color: var(--text-secondary);
    white-space: pre-wrap;
    word-wrap: break-word;
    font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif;
  }

  .loading {
    padding: 2rem;
    text-align: center;
    color: var(--text-tertiary);
  }

  .editor-panel {
    flex: 1;
    display: flex;
    flex-direction: column;
    overflow: hidden;
    background: var(--bg-primary);
  }

  .editor-toolbar {
    display: flex;
    align-items: center;
    justify-content: space-between;
    padding: 0.5rem 1rem;
    background: var(--bg-tertiary);
    border-bottom: 1px solid var(--border-color);
  }

  .toolbar-left {
    display: flex;
    align-items: center;
    gap: 0.5rem;
    color: var(--text-tertiary);
    font-size: 0.875rem;
  }

  .file-icon {
    font-size: 1rem;
  }

  .file-name {
    font-family: monospace;
  }

  .toolbar-right {
    display: flex;
    gap: 0.5rem;
  }

  .btn {
    padding: 0.5rem 1rem;
    border: none;
    border-radius: 4px;
    font-size: 0.875rem;
    font-weight: 500;
    cursor: pointer;
    transition: all 0.15s;
  }

  .btn:disabled {
    opacity: 0.5;
    cursor: not-allowed;
  }

  .btn-secondary {
    background: var(--bg-active);
    color: var(--text-secondary);
  }

  .btn-secondary:hover:not(:disabled) {
    background: var(--bg-hover);
  }

  .btn-primary {
    background: #2563eb;
    color: #fff;
  }

  .btn-primary:hover:not(:disabled) {
    background: #1d4ed8;
  }

  .btn-success {
    background: #22c55e;
    color: #fff;
  }

  .btn-success:hover {
    background: #16a34a;
  }

  .editor-wrapper {
    flex: 1;
    min-height: 0;
  }

  /* Tablet */
  @media (max-width: 1024px) {
    .instructions-panel {
      width: 320px;
      min-width: 280px;
      max-width: 350px;
    }

    .exercise-header h2 {
      font-size: 1rem;
    }
  }

  /* Mobile */
  @media (max-width: 768px) {
    .exercise-view {
      flex-direction: column;
    }

    .instructions-panel {
      width: 100%;
      min-width: 100%;
      max-width: 100%;
      border-right: none;
      border-bottom: 1px solid var(--border-color);
      max-height: none;
      flex-shrink: 0;
    }

    .instructions-panel:not(.expanded) {
      max-height: 60px;
    }

    .instructions-panel:not(.expanded) .instructions-content {
      display: none;
    }

    .exercise-header {
      cursor: pointer;
    }

    .exercise-header:hover {
      background: var(--bg-hover);
    }

    .expand-icon {
      display: block;
    }

    .category-badge {
      display: none;
    }

    .instructions-panel.expanded {
      max-height: 40vh;
    }

    .editor-panel {
      min-height: 0;
      flex: 1;
    }

    .editor-toolbar {
      padding: 0.5rem;
    }

    .toolbar-left {
      display: none;
    }

    .btn {
      padding: 0.5rem 0.75rem;
      font-size: 0.8125rem;
    }
  }
</style>
