<script lang="ts">
  import { onMount } from 'svelte';
  import type { TestResult, FailedTestDetail } from '../types';
  import { filterOutput } from '../utils/exerciseParser';

  export let result: TestResult | null = null;
  export let isRunning: boolean = false;
  export let jsHabits: string[] = [];

  $: failedDetails = result?.failedTestDetails ?? [];

  $: cleanOutput = result?.output ? filterOutput(result.output) : '';

  // Debug: log test result when it changes
  $: if (result) {
    console.log('TestResults received:', {
      success: result.success,
      error: result.error,
      errorType: result.errorType,
      passedTests: result.passedTests?.length,
      failedTests: result.failedTests?.length
    });
  }

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
    {:else if result.error}
      <div class="status syntax-error">
        <span class="icon">⚠️</span>
        <div class="message">
          <strong>{result.errorType || 'Error'}</strong>
          <span>Your code has an error that prevented it from running</span>
        </div>
      </div>
    {:else}
      <div class="status error">
        <span class="icon">❌</span>
        <div class="message">
          <strong>{result.passedTests.length}/{result.passedTests.length + result.failedTests.length} tests passed</strong>
          <span>Fix the failing tests below</span>
        </div>
      </div>
    {/if}

    {#if cleanOutput}
      <div class="console-output">
        <h4>📋 Console Output</h4>
        <pre>{cleanOutput}</pre>
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
        {#each result.failedTests as test, idx}
          {@const detail = failedDetails.find(d => test.includes(`Test ${d.testNum}`))}
          <div class="test-item failed">
            <span class="cross">✗</span>
            {test}
          </div>
          {#if detail}
            <div class="test-table-wrapper">
              <table class="test-table">
                <thead>
                  <tr>
                    <th>Input</th>
                    <th>Expected</th>
                    <th>Your Output</th>
                  </tr>
                </thead>
                <tbody>
                  <tr>
                    <td><code>{detail.input}</code></td>
                    <td><code class="expected">{detail.expected}</code></td>
                    <td><code class="actual">{detail.actual}</code></td>
                  </tr>
                </tbody>
              </table>
            </div>
          {/if}
        {/each}
      </div>
    {/if}

    {#if result.error}
      <div class="error-box">
        {#if result.errorType}
          <div class="error-type">{result.errorType}</div>
        {/if}
        <div class="error-message">
          <code>{result.error}</code>
        </div>
        {#if result.errorLine}
          <div class="error-location">
            Line {result.errorLine}
          </div>
        {/if}
        {#if result.errorDetails}
          <div class="error-code">
            <code>{result.errorDetails}</code>
          </div>
        {/if}
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

  .status.syntax-error {
    background: #422006;
    color: #fbbf24;
  }

  .error-box {
    margin-top: 0.75rem;
    padding: 0.75rem;
    background: #1c1917;
    border: 1px solid #422006;
    border-left: 3px solid #f59e0b;
    border-radius: 6px;
  }

  .error-type {
    font-size: 0.75rem;
    font-weight: 600;
    color: #f59e0b;
    text-transform: uppercase;
    letter-spacing: 0.05em;
    margin-bottom: 0.25rem;
  }

  .error-message {
    font-size: 0.875rem;
    color: #fbbf24;
  }

  .error-message code {
    font-family: 'JetBrains Mono', monospace;
    background: none;
  }

  .error-location {
    margin-top: 0.5rem;
    font-size: 0.75rem;
    color: var(--text-tertiary);
  }

  .error-code {
    margin-top: 0.5rem;
    padding: 0.5rem;
    background: var(--bg-primary);
    border-radius: 4px;
  }

  .error-code code {
    font-family: 'JetBrains Mono', monospace;
    font-size: 0.75rem;
    color: var(--text-secondary);
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

  .test-table-wrapper {
    margin: 0.5rem 0 0.75rem 1.5rem;
    overflow-x: auto;
  }

  .test-table {
    width: 100%;
    border-collapse: collapse;
    font-size: 0.8125rem;
    background: var(--bg-primary);
    border-radius: 6px;
    overflow: hidden;
  }

  .test-table th,
  .test-table td {
    padding: 0.5rem 0.75rem;
    text-align: left;
    border-bottom: 1px solid var(--border-color);
  }

  .test-table th {
    background: var(--bg-tertiary);
    color: var(--text-secondary);
    font-weight: 600;
    font-size: 0.75rem;
    text-transform: uppercase;
    letter-spacing: 0.025em;
  }

  .test-table td {
    vertical-align: top;
  }

  .test-table code {
    font-family: 'JetBrains Mono', monospace;
    font-size: 0.75rem;
    word-break: break-all;
  }

  .test-table code.expected {
    color: #4ade80;
  }

  .test-table code.actual {
    color: #f87171;
  }

  .console-output {
    margin-top: 0.75rem;
    padding: 0.75rem;
    background: var(--bg-primary);
    border-radius: 6px;
    border-left: 3px solid #60a5fa;
  }

  .console-output h4 {
    margin: 0 0 0.5rem 0;
    font-size: 0.8125rem;
    color: #60a5fa;
  }

  .console-output pre {
    margin: 0;
    padding: 0.5rem;
    background: var(--bg-tertiary);
    border-radius: 4px;
    font-size: 0.75rem;
    color: var(--text-secondary);
    overflow-x: auto;
    white-space: pre-wrap;
    word-break: break-word;
    font-family: 'JetBrains Mono', monospace;
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
