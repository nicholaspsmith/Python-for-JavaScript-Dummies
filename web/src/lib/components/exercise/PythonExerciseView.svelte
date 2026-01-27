<script lang="ts">
  import { createEventDispatcher, onMount } from 'svelte';
  import type { ParsedExercise, ExerciseMetadata, TestResult } from '../../types';
  import CodeEditor from '../CodeEditor.svelte';
  import TestResults from '../TestResults.svelte';
  import { pyodideReady } from '../../stores/pyodide';
  import { hintsEnabled } from '../../stores/hints';
  import { parseExercise } from '../../utils/exerciseParser';
  import { runTests, detectJsHabits } from '../../utils/pyodideRunner';

  export let metadata: ExerciseMetadata | null = null;
  export let savedCode: string | undefined = undefined;
  export let instructionsCollapsed: boolean = false;

  const dispatch = createEventDispatcher();

  let codeEditor: CodeEditor;
  let currentExercise: ParsedExercise | null = null;
  let testResult: TestResult | null = null;
  let isRunning = false;
  let jsHabits: string[] = [];
  let instructionsExpanded = false;
  let mounted = false;
  let hintLevel = 0; // 0 = no hints, 1 = starter code, 2 = pseudocode, 3 = solution

  onMount(() => {
    mounted = true;
  });

  $: currentCode = savedCode ?? currentExercise?.codeTemplate ?? '';
  $: hasHints = !!currentExercise?.hints;
  $: hintsRemaining = 3 - hintLevel;

  // Load exercise when metadata changes (only on client)
  $: if (mounted && metadata) {
    loadExercise();
  }

  async function loadExercise() {
    if (!metadata) return;

    try {
      const response = await fetch(`/${metadata.path}`);
      const content = await response.text();
      currentExercise = parseExercise(content);
      testResult = null;
      jsHabits = [];
      hintLevel = 0; // Reset hints when loading new exercise
    } catch (error) {
      console.error('Failed to load Python exercise:', error);
    }
  }

  function handleCodeChange(event: CustomEvent<{ value: string }>) {
    dispatch('codeChange', { value: event.detail.value });
  }

  function handleCodeSave(event: CustomEvent<{ value: string }>) {
    dispatch('codeSave', { value: event.detail.value });
  }

  async function handleRun() {
    if (!currentExercise) return;

    isRunning = true;
    testResult = null;

    try {
      const userCode = codeEditor.getValue();
      jsHabits = detectJsHabits(userCode);
      testResult = await runTests(userCode, currentExercise.testCode);

      if (testResult.success) {
        dispatch('run');
      }
    } catch (error) {
      testResult = {
        success: false,
        output: '',
        error: error instanceof Error ? error.message : 'Unknown error',
        passedTests: [],
        failedTests: []
      };
    } finally {
      isRunning = false;
    }
  }

  function handleNext() {
    dispatch('next');
  }

  function handleReset() {
    if (currentExercise && codeEditor) {
      codeEditor.reset(currentExercise.codeTemplate);
      dispatch('codeChange', { value: currentExercise.codeTemplate });
      dispatch('codeSave', { value: currentExercise.codeTemplate });
      hintLevel = 0; // Reset hints when resetting code
    }
  }

  function handleHint() {
    if (!currentExercise?.hints || !codeEditor || hintLevel >= 3) return;

    const hints = currentExercise.hints;
    const currentCode = codeEditor.getValue();
    hintLevel++;

    let hintText: string;
    let hintLabel: string;

    if (hintLevel === 1) {
      hintLabel = 'HINT 1 - Starter code';
      hintText = hints.hint1;
    } else if (hintLevel === 2) {
      hintLabel = 'HINT 2 - Pseudocode';
      hintText = hints.hint2;
    } else {
      hintLabel = 'SOLUTION';
      hintText = hints.solution;
    }

    // Format hint as a comment block appended to user's code
    const formattedHint = `\n\n# === ${hintLabel} ===\n# ${hintText.split('\n').join('\n# ')}\n# === END ${hintLabel} ===`;

    const newCode = currentCode + formattedHint;
    codeEditor.reset(newCode);
    dispatch('codeChange', { value: newCode });
    dispatch('codeSave', { value: newCode });
  }

  function toggleInstructions() {
    instructionsExpanded = !instructionsExpanded;
  }

  function toggleInstructionsCollapsed() {
    dispatch('toggleInstructionsCollapsed');
  }

  export function getCode(): string {
    return codeEditor?.getValue() || currentCode;
  }
</script>

<div class="exercise-view">
  <div class="instructions-panel" class:expanded={instructionsExpanded} class:collapsed={instructionsCollapsed}>
    {#if metadata}
      <div class="exercise-header">
        <button class="header-content" on:click={toggleInstructions}>
          <div class="header-left">
            <span class="exercise-number">{metadata.id}</span>
            {#if !instructionsCollapsed}
              <h2>{metadata.name}</h2>
            {/if}
          </div>
          {#if !instructionsCollapsed}
            <div class="header-right">
              <span class="category-badge">{metadata.category}</span>
              <span class="expand-icon">
                {instructionsExpanded ? '▼' : '▶'}
              </span>
            </div>
          {/if}
        </button>
        <button class="collapse-btn" on:click={toggleInstructionsCollapsed} aria-label={instructionsCollapsed ? 'Expand instructions' : 'Collapse instructions'}>
          <svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2">
            {#if instructionsCollapsed}
              <path d="M9 18l6-6-6-6"/>
            {:else}
              <path d="M15 18l-6-6 6-6"/>
            {/if}
          </svg>
        </button>
      </div>
    {/if}

    {#if !instructionsCollapsed}
      <div class="instructions-content">
        {#if currentExercise}
          <pre class="instructions">{currentExercise.instructions}</pre>
        {:else}
          <div class="loading">Loading exercise...</div>
        {/if}
      </div>
    {/if}
  </div>

  <div class="editor-panel">
    <div class="editor-toolbar">
      <div class="toolbar-left">
        <span class="file-icon">🐍</span>
        <span class="file-name">{metadata?.filename || 'exercise.py'}</span>
      </div>
      <div class="toolbar-right">
        <button class="btn btn-secondary" on:click={handleReset} disabled={!currentExercise}>
          Reset
        </button>
        {#if $hintsEnabled && hasHints && hintsRemaining > 0}
          <button
            class="btn btn-hint"
            on:click={handleHint}
            disabled={!currentExercise}
            title={hintLevel === 0 ? 'Get starter code' : hintLevel === 1 ? 'Get pseudocode' : 'Get solution'}
          >
            💡 Hint ({hintsRemaining})
          </button>
        {/if}
        {#if testResult?.success}
          <button class="btn btn-success" on:click={handleNext}>
            Next →
          </button>
        {:else}
          <button
            class="btn btn-primary"
            on:click={handleRun}
            disabled={!$pyodideReady || isRunning || !currentExercise}
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
        language="python"
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
    transition: width 0.2s ease, min-width 0.2s ease, max-width 0.2s ease;
  }

  .instructions-panel.collapsed {
    width: 56px;
    min-width: 56px;
    max-width: 56px;
  }

  .exercise-header {
    width: 100%;
    padding: 0.75rem;
    border: none;
    border-bottom: 1px solid var(--border-color);
    background: none;
    display: flex;
    align-items: center;
    justify-content: space-between;
    gap: 0.5rem;
  }

  .header-content {
    display: flex;
    align-items: center;
    justify-content: space-between;
    flex: 1;
    min-width: 0;
    background: none;
    border: none;
    cursor: default;
    text-align: left;
    padding: 0;
    gap: 0.75rem;
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
    flex-shrink: 0;
  }

  .collapse-btn:hover {
    background: var(--bg-active);
    color: var(--text-primary);
  }

  .collapsed .exercise-header {
    flex-direction: column;
    padding: 0.5rem;
  }

  .collapsed .header-content {
    justify-content: center;
  }

  .collapsed .collapse-btn {
    margin-top: 0.5rem;
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

  .btn-hint {
    background: #f59e0b;
    color: #fff;
  }

  .btn-hint:hover:not(:disabled) {
    background: #d97706;
  }

  .editor-wrapper {
    flex: 1;
    min-height: 0;
  }

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
