<script lang="ts">
  import { onMount } from 'svelte';
  import type { TestResult } from '../types';
  import { filterOutput } from '../utils/exerciseParser';

  export let result: TestResult | null = null;
  export let isRunning: boolean = false;
  export let jsHabits: string[] = [];

  $: cleanOutput = result?.output ? filterOutput(result.output) : '';

  let containerHeight = 200;
  let isDragging = false;
  let startY = 0;
  let startHeight = 0;

  function handleMouseDown(e: MouseEvent) {
    isDragging = true;
    startY = e.clientY;
    startHeight = containerHeight;
    document.addEventListener('mousemove', handleMouseMove);
    document.addEventListener('mouseup', handleMouseUp);
    document.body.style.cursor = 'ns-resize';
    document.body.style.userSelect = 'none';
  }

  function handleMouseMove(e: MouseEvent) {
    if (!isDragging) return;
    const delta = startY - e.clientY;
    containerHeight = Math.max(80, Math.min(600, startHeight + delta));
  }

  function handleMouseUp() {
    isDragging = false;
    document.removeEventListener('mousemove', handleMouseMove);
    document.removeEventListener('mouseup', handleMouseUp);
    document.body.style.cursor = '';
    document.body.style.userSelect = '';
  }

  onMount(() => {
    return () => {
      document.removeEventListener('mousemove', handleMouseMove);
      document.removeEventListener('mouseup', handleMouseUp);
    };
  });
</script>

<div class="results-wrapper" style="height: {containerHeight}px">
  <!-- svelte-ignore a11y-no-static-element-interactions -->
  <div
    class="resize-handle"
    on:mousedown={handleMouseDown}
    class:dragging={isDragging}
  >
    <div class="resize-grip"></div>
  </div>
  <div class="results-container">
  {#if isRunning}
    <div class="status running">
      <span class="spinner"></span>
      Running tests...
    </div>
  {:else if result}
    {#if result.success}
      <div class="status success">
        <span class="icon">🎉</span>
        <div class="message">
          <strong>All tests passed!</strong>
          <span>Great job! Keep up the streak!</span>
        </div>
      </div>
    {:else}
      <div class="status error">
        <span class="icon">❌</span>
        <div class="message">
          <strong>Tests failed</strong>
          {#if result.error}
            <span class="error-detail">{result.error}</span>
          {/if}
        </div>
      </div>
    {/if}

    {#if result.passedTests.length > 0 || result.failedTests.length > 0}
      <div class="test-details">
        {#each result.passedTests as test}
          <div class="test-item passed">
            <span class="check">✓</span>
            Test {test} passed
          </div>
        {/each}
        {#each result.failedTests as test}
          <div class="test-item failed">
            <span class="cross">✗</span>
            {test}
          </div>
        {/each}
      </div>
    {/if}

    {#if jsHabits.length > 0}
      <div class="js-habits">
        <h4>🔍 JavaScript habits detected:</h4>
        <ul>
          {#each jsHabits as habit}
            <li>{habit}</li>
          {/each}
        </ul>
      </div>
    {/if}

    {#if cleanOutput && !result.success}
      <details class="output-details" open>
        <summary>Show output</summary>
        <pre class="output">{cleanOutput}</pre>
      </details>
    {/if}
  {:else}
    <div class="status idle">
      <span class="icon">💡</span>
      <span>Press <kbd>Cmd</kbd>+<kbd>Enter</kbd> or click "Check Answer" to run tests</span>
    </div>
  {/if}
  </div>
</div>

<style>
  .results-wrapper {
    display: flex;
    flex-direction: column;
    background: var(--bg-secondary);
    border-top: 1px solid var(--border-color);
    flex-shrink: 0;
  }

  .resize-handle {
    height: 8px;
    cursor: ns-resize;
    display: flex;
    align-items: center;
    justify-content: center;
    background: var(--bg-secondary);
    border-bottom: 1px solid var(--border-color);
    flex-shrink: 0;
  }

  .resize-handle:hover,
  .resize-handle.dragging {
    background: var(--bg-tertiary);
  }

  .resize-grip {
    width: 40px;
    height: 4px;
    background: var(--border-color);
    border-radius: 2px;
  }

  .resize-handle:hover .resize-grip,
  .resize-handle.dragging .resize-grip {
    background: var(--text-tertiary);
  }
  .results-container {
    padding: 1rem;
    background: var(--bg-secondary);
    overflow-y: auto;
    flex: 1;
    min-height: 0;
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

  .error-detail {
    font-family: monospace;
    font-size: 0.75rem !important;
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
    to {
      transform: rotate(360deg);
    }
  }

  .test-details {
    margin-top: 0.75rem;
    display: flex;
    flex-direction: column;
    gap: 0.25rem;
  }

  .test-item {
    display: flex;
    align-items: center;
    gap: 0.5rem;
    padding: 0.375rem 0.75rem;
    font-size: 0.8125rem;
    border-radius: 4px;
  }

  .test-item.passed {
    background: var(--success-bg);
    color: #4ade80;
  }

  .test-item.failed {
    background: var(--error-bg);
    color: #f87171;
  }

  .check {
    color: #4ade80;
  }

  .cross {
    color: #f87171;
  }

  .js-habits {
    margin-top: 1rem;
    padding: 0.75rem;
    background: var(--bg-tertiary);
    border-radius: 6px;
    border-left: 3px solid #fbbf24;
  }

  .js-habits h4 {
    margin: 0 0 0.5rem 0;
    font-size: 0.8125rem;
    color: #fbbf24;
  }

  .js-habits ul {
    margin: 0;
    padding: 0 0 0 1.25rem;
    font-size: 0.8125rem;
    color: var(--text-secondary);
  }

  .js-habits li {
    margin-bottom: 0.25rem;
  }

  .output-details {
    margin-top: 0.75rem;
  }

  .output-details summary {
    cursor: pointer;
    font-size: 0.8125rem;
    color: var(--text-tertiary);
    padding: 0.375rem;
  }

  .output-details summary:hover {
    color: var(--text-secondary);
  }

  .output {
    margin: 0.5rem 0 0 0;
    padding: 0.75rem;
    background: var(--bg-primary);
    border-radius: 4px;
    font-size: 0.75rem;
    color: var(--text-secondary);
    overflow-x: auto;
    white-space: pre-wrap;
    word-break: break-word;
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
</style>
