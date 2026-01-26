<script lang="ts">
  import { onMount } from 'svelte';
  import Header from '$lib/components/Header.svelte';
  import Sidebar from '$lib/components/Sidebar.svelte';
  import ExerciseRouter from '$lib/components/exercise/ExerciseRouter.svelte';
  import { progress } from '$lib/stores/progress';
  import { currentExerciseId, currentExerciseMetadata, getNextExerciseId } from '$lib/stores/exercises';
  import { initPyodide } from '$lib/stores/pyodide';
  import { initSqlJs } from '$lib/stores/sqljs';
  import { initSandpack } from '$lib/stores/sandpack';
  import { initAuth } from '$lib/stores/supabase';

  let sidebarOpen = false;
  let sidebarCollapsed = false;
  let instructionsCollapsed = false;
  let mounted = false;

  onMount(async () => {
    mounted = true;

    // Restore collapsed states
    sidebarCollapsed = localStorage.getItem('sidebarCollapsed') === 'true';
    instructionsCollapsed = localStorage.getItem('instructionsCollapsed') === 'true';

    // Initialize Supabase auth (if configured)
    await initAuth();

    // Initialize progress from localStorage/cloud (restores current exercise)
    await progress.init();

    // Start loading runtimes in background based on current exercise
    initializeRuntimes();
  });

  // Initialize appropriate runtime based on current exercise
  function initializeRuntimes() {
    const runtime = $currentExerciseMetadata?.runtime ?? 'python';

    // Always initialize Python for Code Master exercises
    if (runtime === 'python') {
      initPyodide();
    } else if (runtime === 'sql') {
      initSqlJs();
    } else if (runtime === 'react') {
      initSandpack();
    } else if (runtime === 'typescript') {
      // TypeScript uses Sandpack with TypeScript preset
      initSandpack();
    }
  }

  // Re-initialize runtime when exercise changes
  $: if (mounted && $currentExerciseMetadata) {
    initializeRuntimes();
  }

  function handleExerciseSelect(event: CustomEvent<{ id: string }>) {
    progress.setCurrentExercise(event.detail.id);
  }

  function handleSidebarClose() {
    sidebarOpen = false;
  }

  function handleToggleSidebar() {
    sidebarOpen = !sidebarOpen;
  }

  function handleCodeChange(event: CustomEvent<{ value: string }>) {
    // Track code changes
  }

  function handleCodeSave(event: CustomEvent<{ value: string }>) {
    if ($currentExerciseId) {
      progress.saveCode($currentExerciseId, event.detail.value);
    }
  }

  function handleRun() {
    // Python exercises handle this internally and dispatch 'run' on success
    if ($currentExerciseId) {
      progress.markCompleted($currentExerciseId);
    }
  }

  function handleComplete(event: CustomEvent<{ success: boolean }>) {
    // SQL and React exercises dispatch 'complete' event
    if (event.detail.success && $currentExerciseId) {
      progress.markCompleted($currentExerciseId);
    }
  }

  function handleNext() {
    if (!$currentExerciseId) return;
    const nextId = getNextExerciseId($currentExerciseId);
    if (nextId) {
      progress.setCurrentExercise(nextId);
    }
  }

  function handleToggleSidebarCollapse() {
    sidebarCollapsed = !sidebarCollapsed;
    localStorage.setItem('sidebarCollapsed', String(sidebarCollapsed));
  }

  function handleToggleInstructionsCollapsed() {
    instructionsCollapsed = !instructionsCollapsed;
    localStorage.setItem('instructionsCollapsed', String(instructionsCollapsed));
  }
</script>

<svelte:head>
  <title>Python Practice</title>
  <meta name="viewport" content="width=device-width, initial-scale=1, maximum-scale=1, user-scalable=no" />
</svelte:head>

<div class="app">
  <Header {sidebarOpen} on:toggleSidebar={handleToggleSidebar} />
  <main>
    <Sidebar
      isOpen={sidebarOpen}
      collapsed={sidebarCollapsed}
      on:select={handleExerciseSelect}
      on:close={handleSidebarClose}
      on:toggleCollapse={handleToggleSidebarCollapse}
    />
    <ExerciseRouter
      metadata={$currentExerciseMetadata}
      savedCode={$progress.savedCode[$currentExerciseId ?? '']}
      {instructionsCollapsed}
      on:codeChange={handleCodeChange}
      on:codeSave={handleCodeSave}
      on:run={handleRun}
      on:complete={handleComplete}
      on:next={handleNext}
      on:toggleInstructionsCollapsed={handleToggleInstructionsCollapsed}
    />
  </main>
</div>

<style>
  :global(body) {
    margin: 0;
    padding: 0;
    font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif;
    background: var(--bg-primary);
    color: var(--text-secondary);
    overflow: hidden;
  }

  :global(*) {
    box-sizing: border-box;
  }

  .app {
    display: flex;
    flex-direction: column;
    height: 100vh;
    height: 100dvh; /* Dynamic viewport height for mobile */
    overflow: hidden;
  }

  main {
    flex: 1;
    display: flex;
    overflow: hidden;
    position: relative;
  }

  /* Mobile adjustments */
  @media (max-width: 768px) {
    main {
      flex-direction: column;
    }
  }
</style>
