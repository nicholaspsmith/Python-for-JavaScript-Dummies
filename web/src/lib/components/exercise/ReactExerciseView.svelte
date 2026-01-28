<script lang="ts">
  import { createEventDispatcher, onMount, onDestroy, tick } from 'svelte';
  import type { ExerciseMetadata, ReactExerciseConfig } from '../../types';
  import CodeEditor from '../CodeEditor.svelte';
  import { sandpackReady, initSandpack, loadSandpackClient } from '../../stores/sandpack';
  import { createSandpackFiles, getDefaultDependencies, mergeDependencies } from '../../utils/reactExerciseParser';
  import { hintsEnabled } from '../../stores/hints';

  export let metadata: ExerciseMetadata | null = null;
  export let savedCode: string | undefined = undefined;
  export let instructionsCollapsed: boolean = false;

  const dispatch = createEventDispatcher();

  let codeEditor: CodeEditor;
  let iframeElement: HTMLIFrameElement;
  let sandpackClient: any = null;
  let exerciseConfig: ReactExerciseConfig | null = null;
  let starterCode: string = '';
  let isLoading = true;
  let previewError: string | null = null;
  let instructionsExpanded = false;
  let mounted = false;
  let debounceTimer: ReturnType<typeof setTimeout> | null = null;
  let hintLevel = 0;

  $: currentCode = savedCode ?? starterCode;
  $: hasHints = !!exerciseConfig?.hints;
  $: hintsRemaining = 3 - hintLevel;

  // Initialize Sandpack on mount
  onMount(() => {
    mounted = true;
    initSandpack();
  });

  onDestroy(() => {
    mounted = false;

    if (debounceTimer) {
      clearTimeout(debounceTimer);
      debounceTimer = null;
    }

    if (sandpackClient) {
      sandpackClient.destroy?.();
      sandpackClient = null;
    }

    // Clear iframe reference to help garbage collection
    if (iframeElement) {
      iframeElement.src = 'about:blank';
    }
  });

  // Load exercise when metadata changes (only on client)
  $: if (mounted && metadata && $sandpackReady) {
    loadExercise();
  }

  async function loadExercise() {
    if (!metadata) return;

    isLoading = true;
    previewError = null;
    hintLevel = 0;

    try {
      // Fetch exercise.json
      const configResponse = await fetch(`/${metadata.path}/exercise.json`);
      exerciseConfig = await configResponse.json();

      // Fetch App.jsx
      const codeResponse = await fetch(`/${metadata.path}/App.jsx`);
      starterCode = await codeResponse.text();

      // Wait for DOM to update (iframe to be available)
      await tick();

      // Initialize Sandpack preview
      await initSandpackPreview();
    } catch (error) {
      console.error('Failed to load React exercise:', error);
      previewError = error instanceof Error ? error.message : 'Failed to load exercise';
    } finally {
      isLoading = false;
    }
  }

  async function initSandpackPreview() {
    if (!iframeElement) {
      console.warn('Sandpack: iframe element not available yet, retrying...');
      await tick();
      if (!iframeElement) {
        previewError = 'Preview iframe not available';
        return;
      }
    }

    try {
      // Destroy previous client
      if (sandpackClient) {
        sandpackClient.destroy?.();
      }

      const rawFiles = createSandpackFiles(
        { '/App.jsx': currentCode || starterCode },
        exerciseConfig?.dependencies
      );

      // Convert files to Sandpack format (with code property)
      const files: Record<string, { code: string }> = {};
      for (const [path, code] of Object.entries(rawFiles)) {
        files[path] = { code };
      }

      console.log('Sandpack: initializing with files:', Object.keys(files));

      sandpackClient = await loadSandpackClient(
        iframeElement,
        {
          files,
          entry: '/index.js',
          dependencies: mergeDependencies(exerciseConfig?.dependencies)
        },
        { showOpenInCodeSandbox: false }
      );

      console.log('Sandpack: client initialized successfully');
    } catch (error) {
      console.error('Failed to initialize Sandpack:', error);
      previewError = error instanceof Error ? error.message : 'Failed to initialize preview';
    }
  }

  function handleCodeChange(event: CustomEvent<{ value: string }>) {
    dispatch('codeChange', { value: event.detail.value });

    // Debounce Sandpack preview update (500ms)
    if (debounceTimer) {
      clearTimeout(debounceTimer);
    }

    debounceTimer = setTimeout(() => {
      if (sandpackClient) {
        const rawFiles = createSandpackFiles(
          { '/App.jsx': event.detail.value },
          exerciseConfig?.dependencies
        );

        // Convert files to Sandpack format (with code property)
        const files: Record<string, { code: string }> = {};
        for (const [path, code] of Object.entries(rawFiles)) {
          files[path] = { code };
        }

        sandpackClient.updateSandbox({ files });
      }
    }, 500);
  }

  function handleCodeSave(event: CustomEvent<{ value: string }>) {
    dispatch('codeSave', { value: event.detail.value });
  }

  function handleReset() {
    if (codeEditor && starterCode) {
      codeEditor.reset(starterCode);
      dispatch('codeChange', { value: starterCode });
      dispatch('codeSave', { value: starterCode });
      hintLevel = 0;
    }
  }

  function handleHint() {
    if (!exerciseConfig?.hints || !codeEditor || hintLevel >= 3) return;

    const hints = exerciseConfig.hints;
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

    // Convert escaped newlines to actual newlines
    const unescapedHint = hintText.replace(/\\n/g, '\n');

    // Format hint as a comment block appended to user's code
    const formattedHint = `\n\n{/* === ${hintLabel} ===\n${unescapedHint}\n=== END ${hintLabel} === */}`;

    const newCode = currentCode + formattedHint;
    codeEditor.reset(newCode);
    dispatch('codeChange', { value: newCode });
    dispatch('codeSave', { value: newCode });
  }

  function handleNext() {
    dispatch('next');
  }

  function handleComplete() {
    dispatch('complete', { success: true });
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
            <span class="exercise-number react">{metadata.id}</span>
            {#if !instructionsCollapsed}
              <h2>{metadata.name}</h2>
            {/if}
          </div>
          {#if !instructionsCollapsed}
            <div class="header-right">
              <span class="category-badge react">{metadata.category}</span>
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
        {#if exerciseConfig}
          <pre class="instructions">{exerciseConfig.instructions}</pre>
        {:else if isLoading}
          <div class="loading">Loading exercise...</div>
        {:else}
          <div class="loading">No instructions available</div>
        {/if}
      </div>
    {/if}
  </div>

  <div class="main-panel">
    <div class="editor-panel">
      <div class="editor-toolbar">
        <div class="toolbar-left">
          <span class="file-icon">⚛️</span>
          <span class="file-name">App.jsx</span>
        </div>
        <div class="toolbar-right">
          <button class="btn btn-secondary" on:click={handleReset} disabled={!starterCode}>
            Reset
          </button>
          {#if $hintsEnabled && hasHints && hintsRemaining > 0}
            <button
              class="btn btn-hint"
              on:click={handleHint}
              disabled={!exerciseConfig}
              title={hintLevel === 0 ? 'Get starter code' : hintLevel === 1 ? 'Get pseudocode' : 'Get solution'}
            >
              💡 Hint ({hintsRemaining})
            </button>
          {/if}
          <button class="btn btn-success" on:click={handleComplete}>
            Mark Complete
          </button>
          <button class="btn btn-primary react" on:click={handleNext}>
            Next →
          </button>
        </div>
      </div>

      <div class="editor-wrapper">
        <CodeEditor
          bind:this={codeEditor}
          value={currentCode}
          language="javascript"
          isJsx={true}
          on:change={handleCodeChange}
          on:save={handleCodeSave}
        />
      </div>
    </div>

    <div class="preview-panel">
      <div class="preview-toolbar">
        <span class="preview-title">Preview</span>
        {#if isLoading}
          <span class="loading-indicator">Loading...</span>
        {/if}
      </div>
      <div class="preview-wrapper">
        {#if previewError}
          <div class="preview-error">
            <p>Error: {previewError}</p>
          </div>
        {:else if !$sandpackReady}
          <div class="preview-loading">
            <p>Initializing React preview...</p>
          </div>
        {:else}
          <iframe
            bind:this={iframeElement}
            title="React Preview"
            sandbox="allow-scripts allow-same-origin allow-forms allow-popups allow-modals"
          ></iframe>
        {/if}
      </div>
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
    width: 350px;
    min-width: 280px;
    max-width: 400px;
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

  .exercise-number.react {
    color: #61dafb;
    background: #1a2733;
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

  .category-badge.react {
    color: #61dafb;
    background: #1a2733;
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

  .main-panel {
    flex: 1;
    display: flex;
    flex-direction: column;
    overflow: hidden;
  }

  .editor-panel {
    flex: 1;
    display: flex;
    flex-direction: column;
    overflow: hidden;
    background: var(--bg-primary);
    min-height: 0;
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

  .btn-primary.react {
    background: #0ea5e9;
  }

  .btn-primary.react:hover:not(:disabled) {
    background: #0284c7;
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
    min-height: 200px;
  }

  .preview-panel {
    height: 300px;
    min-height: 200px;
    border-top: 1px solid var(--border-color);
    display: flex;
    flex-direction: column;
  }

  .preview-toolbar {
    display: flex;
    align-items: center;
    justify-content: space-between;
    padding: 0.5rem 1rem;
    background: var(--bg-tertiary);
    border-bottom: 1px solid var(--border-color);
  }

  .preview-title {
    font-size: 0.875rem;
    font-weight: 500;
    color: var(--text-secondary);
  }

  .loading-indicator {
    font-size: 0.75rem;
    color: var(--text-tertiary);
  }

  .preview-wrapper {
    flex: 1;
    background: #fff;
    overflow: hidden;
  }

  :global([data-theme="dark"]) .preview-wrapper {
    background: #1e1e1e;
  }

  .preview-wrapper iframe {
    width: 100%;
    height: 100%;
    border: none;
  }

  /* Invert preview colors in dark mode */
  :global([data-theme="dark"]) .preview-wrapper iframe {
    filter: invert(1) hue-rotate(180deg);
  }

  .preview-error, .preview-loading {
    display: flex;
    align-items: center;
    justify-content: center;
    height: 100%;
    color: var(--text-tertiary);
  }

  .preview-error {
    color: #f87171;
    background: var(--error-bg);
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
      max-height: 30vh;
    }

    .expand-icon {
      display: block;
    }

    .category-badge {
      display: none;
    }
  }
</style>
