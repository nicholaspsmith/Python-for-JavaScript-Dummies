<script lang="ts">
  import { createEventDispatcher, onMount } from 'svelte';
  import type { ParsedSQLExercise, ExerciseMetadata, SQLTestResult } from '../../types';
  import CodeEditor from '../CodeEditor.svelte';
  import { sqljsReady, initSqlJs } from '../../stores/sqljs';
  import { parseSQLExercise } from '../../utils/sqlExerciseParser';
  import { runSQLTests, runQuery } from '../../utils/sqlRunner';
  import { hintsEnabled } from '../../stores/hints';

  export let metadata: ExerciseMetadata | null = null;
  export let savedCode: string | undefined = undefined;
  export let instructionsCollapsed: boolean = false;

  const dispatch = createEventDispatcher();

  let codeEditor: CodeEditor;
  let currentExercise: ParsedSQLExercise | null = null;
  let testResult: SQLTestResult | null = null;
  let isRunning = false;
  let instructionsExpanded = false;
  let previewResult: { columns: string[]; rows: unknown[][] } | null = null;
  let previewError: string | null = null;
  let mounted = false;
  let hintLevel = 0;

  $: currentCode = savedCode ?? currentExercise?.solutionTemplate ?? '';
  $: hasHints = !!currentExercise?.hints;
  $: hintsRemaining = 3 - hintLevel;

  // Initialize sql.js on mount
  onMount(() => {
    mounted = true;
    initSqlJs();
  });

  // Load exercise when metadata changes (only on client)
  $: if (mounted && metadata) {
    loadExercise();
  }

  async function loadExercise() {
    if (!metadata) return;

    try {
      const response = await fetch(`/${metadata.path}`);
      const content = await response.text();
      currentExercise = parseSQLExercise(content);
      testResult = null;
      previewResult = null;
      previewError = null;
      hintLevel = 0;
    } catch (error) {
      console.error('Failed to load SQL exercise:', error);
    }
  }

  function handleCodeChange(event: CustomEvent<{ value: string }>) {
    dispatch('codeChange', { value: event.detail.value });
  }

  function handleCodeSave(event: CustomEvent<{ value: string }>) {
    dispatch('codeSave', { value: event.detail.value });
  }

  function handlePreview() {
    if (!currentExercise) return;

    const userCode = codeEditor.getValue();
    const result = runQuery(userCode, currentExercise.schema, currentExercise.seedData);

    if ('error' in result) {
      previewError = result.error;
      previewResult = null;
    } else {
      previewResult = result;
      previewError = null;
    }
  }

  async function handleRun() {
    if (!currentExercise) return;

    isRunning = true;
    testResult = null;
    previewResult = null;
    previewError = null;

    try {
      const userCode = codeEditor.getValue();
      testResult = await runSQLTests(
        userCode,
        currentExercise.schema,
        currentExercise.seedData,
        currentExercise.tests
      );

      if (testResult.success) {
        dispatch('complete', { success: true });
      }
    } catch (error) {
      testResult = {
        success: false,
        output: '',
        error: error instanceof Error ? error.message : 'Unknown error'
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
      codeEditor.reset(currentExercise.solutionTemplate);
      dispatch('codeChange', { value: currentExercise.solutionTemplate });
      dispatch('codeSave', { value: currentExercise.solutionTemplate });
      testResult = null;
      previewResult = null;
      previewError = null;
      hintLevel = 0;
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
    const formattedHint = `\n\n-- === ${hintLabel} ===\n-- ${hintText.split('\n').join('\n-- ')}\n-- === END ${hintLabel} ===`;

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
            <span class="exercise-number sql">{metadata.id}</span>
            {#if !instructionsCollapsed}
              <h2>{metadata.name}</h2>
            {/if}
          </div>
          {#if !instructionsCollapsed}
            <div class="header-right">
              <span class="category-badge sql">{metadata.category}</span>
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
        <span class="file-icon">🗄️</span>
        <span class="file-name">{metadata?.filename || 'query.sql'}</span>
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
        <button
          class="btn btn-secondary"
          on:click={handlePreview}
          disabled={!$sqljsReady || isRunning || !currentExercise}
        >
          Preview
        </button>
        {#if testResult?.success}
          <button class="btn btn-success" on:click={handleNext}>
            Next →
          </button>
        {:else}
          <button
            class="btn btn-primary sql"
            on:click={handleRun}
            disabled={!$sqljsReady || isRunning || !currentExercise}
          >
            {#if isRunning}
              Running...
            {:else if !$sqljsReady}
              Loading SQL...
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
        language="sql"
        on:change={handleCodeChange}
        on:save={handleCodeSave}
        on:run={handleRun}
      />
    </div>

    <div class="results-panel">
      {#if isRunning}
        <div class="status running">
          <span class="spinner"></span>
          Running query...
        </div>
      {:else if testResult}
        {#if testResult.success}
          <div class="status success">
            <span class="icon">🎉</span>
            <div class="message">
              <strong>Correct!</strong>
              <span>Your query returns the expected results.</span>
            </div>
          </div>
        {:else}
          <div class="status error">
            <span class="icon">❌</span>
            <div class="message">
              <strong>Not quite right</strong>
              <span>{testResult.error || 'Query results do not match expected output'}</span>
            </div>
          </div>
        {/if}

        {#if testResult.actualResult}
          <div class="result-table">
            <h4>Your Result:</h4>
            {#if testResult.actualResult.length > 0}
              <div class="table-wrapper">
                <table>
                  <tbody>
                    {#each testResult.actualResult as row}
                      <tr>
                        {#if Array.isArray(row)}
                          {#each row as cell}
                            <td>{cell}</td>
                          {/each}
                        {:else}
                          <td>{row}</td>
                        {/if}
                      </tr>
                    {/each}
                  </tbody>
                </table>
              </div>
            {:else}
              <p class="empty">Your query returned 0 rows</p>
            {/if}
          </div>
        {/if}

        {#if !testResult.success && testResult.expectedResult}
          <div class="result-table expected">
            <h4>Expected:</h4>
            <div class="table-wrapper">
              <table>
                <tbody>
                  {#each testResult.expectedResult as row}
                    <tr>
                      {#if Array.isArray(row)}
                        {#each row as cell}
                          <td>{cell}</td>
                        {/each}
                      {:else}
                        <td>{row}</td>
                      {/if}
                    </tr>
                  {/each}
                </tbody>
              </table>
            </div>
          </div>
        {/if}
      {:else if previewError}
        <div class="status error">
          <span class="icon">⚠️</span>
          <div class="message">
            <strong>SQL Error</strong>
            <span>{previewError}</span>
          </div>
        </div>
      {:else if previewResult}
        <div class="result-table preview">
          <h4>Preview ({previewResult.rows.length} rows):</h4>
          {#if previewResult.rows.length > 0}
            <div class="table-wrapper">
              <table>
                <thead>
                  <tr>
                    {#each previewResult.columns as col}
                      <th>{col}</th>
                    {/each}
                  </tr>
                </thead>
                <tbody>
                  {#each previewResult.rows as row}
                    <tr>
                      {#each row as cell}
                        <td>{cell}</td>
                      {/each}
                    </tr>
                  {/each}
                </tbody>
              </table>
            </div>
          {:else}
            <p class="empty">No results returned</p>
          {/if}
        </div>
      {:else}
        <div class="status idle">
          <span class="icon">💡</span>
          <span>Press <kbd>Cmd</kbd>+<kbd>Enter</kbd> or click "Check Answer" to run tests</span>
        </div>
      {/if}
    </div>
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
    padding: 0.25rem 0.5rem;
    border-radius: 4px;
    font-family: monospace;
    flex-shrink: 0;
  }

  .exercise-number.sql {
    color: #f59e0b;
    background: #451a03;
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

  .category-badge.sql {
    color: #f59e0b;
    background: #451a03;
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

  .btn-primary.sql {
    background: #d97706;
  }

  .btn-primary.sql:hover:not(:disabled) {
    background: #b45309;
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

  .results-panel {
    min-height: 150px;
    max-height: 300px;
    overflow-y: auto;
    background: var(--bg-secondary);
    border-top: 1px solid var(--border-color);
    padding: 1rem;
  }

  .status {
    display: flex;
    align-items: center;
    gap: 0.75rem;
    padding: 0.75rem 1rem;
    border-radius: 6px;
    font-size: 0.875rem;
  }

  .status.running {
    background: var(--bg-tertiary);
    color: #fbbf24;
  }

  .status.success {
    background: var(--success-bg);
    color: #4ade80;
  }

  .status.error {
    background: var(--error-bg);
    color: #f87171;
  }

  .status.idle {
    background: var(--bg-tertiary);
    color: var(--text-tertiary);
  }

  .icon {
    font-size: 1.25rem;
  }

  .message {
    display: flex;
    flex-direction: column;
    gap: 0.25rem;
  }

  .message strong {
    font-weight: 600;
  }

  .message span {
    font-size: 0.8125rem;
    opacity: 0.8;
  }

  .spinner {
    width: 16px;
    height: 16px;
    border: 2px solid #fbbf24;
    border-top-color: transparent;
    border-radius: 50%;
    animation: spin 1s linear infinite;
  }

  @keyframes spin {
    to { transform: rotate(360deg); }
  }

  .result-table {
    margin-top: 1rem;
  }

  .result-table h4 {
    margin: 0 0 0.5rem 0;
    font-size: 0.8125rem;
    color: var(--text-tertiary);
  }

  .result-table.expected h4 {
    color: #4ade80;
  }

  .result-table.preview h4 {
    color: #60a5fa;
  }

  .table-wrapper {
    overflow-x: auto;
  }

  table {
    width: 100%;
    border-collapse: collapse;
    font-family: monospace;
    font-size: 0.8125rem;
  }

  th, td {
    padding: 0.5rem;
    text-align: left;
    border: 1px solid var(--border-color);
  }

  th {
    background: var(--bg-tertiary);
    color: var(--text-secondary);
    font-weight: 600;
  }

  td {
    background: var(--bg-primary);
    color: var(--text-primary);
  }

  .empty {
    color: var(--text-tertiary);
    font-style: italic;
    margin: 0;
  }

  kbd {
    display: inline-block;
    padding: 0.125rem 0.375rem;
    background: var(--bg-active);
    border-radius: 3px;
    font-family: monospace;
    font-size: 0.75rem;
    color: var(--text-secondary);
    border: 1px solid var(--border-color);
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
    }

    .instructions-panel:not(.expanded) {
      max-height: 60px;
    }

    .instructions-panel:not(.expanded) .instructions-content {
      display: none;
    }

    .instructions-panel.expanded {
      max-height: 40vh;
    }

    .expand-icon {
      display: block;
    }

    .category-badge {
      display: none;
    }
  }
</style>
