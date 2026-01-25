<script lang="ts">
  import { createEventDispatcher } from 'svelte';
  import type { ExerciseMetadata, TestResult } from '../../types';
  import PythonExerciseView from './PythonExerciseView.svelte';
  import SqlExerciseView from './SqlExerciseView.svelte';
  import ReactExerciseView from './ReactExerciseView.svelte';

  export let metadata: ExerciseMetadata | null = null;
  export let savedCode: string | undefined = undefined;
  export let instructionsCollapsed: boolean = false;

  const dispatch = createEventDispatcher();

  // Forward events from child views
  function handleCodeChange(event: CustomEvent<{ value: string }>) {
    dispatch('codeChange', event.detail);
  }

  function handleCodeSave(event: CustomEvent<{ value: string }>) {
    dispatch('codeSave', event.detail);
  }

  function handleRun() {
    dispatch('run');
  }

  function handleNext() {
    dispatch('next');
  }

  function handleToggleInstructionsCollapsed() {
    dispatch('toggleInstructionsCollapsed');
  }

  function handleComplete(event: CustomEvent<{ success: boolean }>) {
    dispatch('complete', event.detail);
  }

  // Determine which view to render based on runtime
  $: runtime = metadata?.runtime ?? 'python';
</script>

{#if !metadata}
  <div class="loading">
    <p>Select an exercise to get started...</p>
  </div>
{:else if runtime === 'python'}
  <PythonExerciseView
    {metadata}
    {savedCode}
    {instructionsCollapsed}
    on:codeChange={handleCodeChange}
    on:codeSave={handleCodeSave}
    on:run={handleRun}
    on:next={handleNext}
    on:toggleInstructionsCollapsed={handleToggleInstructionsCollapsed}
  />
{:else if runtime === 'sql'}
  <SqlExerciseView
    {metadata}
    {savedCode}
    {instructionsCollapsed}
    on:codeChange={handleCodeChange}
    on:codeSave={handleCodeSave}
    on:complete={handleComplete}
    on:next={handleNext}
    on:toggleInstructionsCollapsed={handleToggleInstructionsCollapsed}
  />
{:else if runtime === 'react'}
  <ReactExerciseView
    {metadata}
    {savedCode}
    {instructionsCollapsed}
    on:codeChange={handleCodeChange}
    on:codeSave={handleCodeSave}
    on:complete={handleComplete}
    on:next={handleNext}
    on:toggleInstructionsCollapsed={handleToggleInstructionsCollapsed}
  />
{:else}
  <div class="unsupported">
    <p>Unsupported exercise type: {runtime}</p>
  </div>
{/if}

<style>
  .loading, .unsupported {
    display: flex;
    align-items: center;
    justify-content: center;
    height: 100%;
    color: var(--text-tertiary);
  }
</style>
