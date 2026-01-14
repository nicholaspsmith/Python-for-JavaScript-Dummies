<script lang="ts">
  import { onMount } from 'svelte';
  import Header from '$lib/components/Header.svelte';
  import Sidebar from '$lib/components/Sidebar.svelte';
  import ExerciseView from '$lib/components/ExerciseView.svelte';
  import { progress } from '$lib/stores/progress';
  import { currentExerciseId, currentExerciseMetadata } from '$lib/stores/exercises';
  import { initPyodide } from '$lib/stores/pyodide';
  import { initAuth } from '$lib/stores/supabase';
  import { parseExercise } from '$lib/utils/exerciseParser';
  import { runTests, detectJsHabits } from '$lib/utils/pyodideRunner';
  import type { ParsedExercise, TestResult } from '$lib/types';

  let exerciseView: ExerciseView;
  let currentExercise: ParsedExercise | null = null;
  let testResult: TestResult | null = null;
  let isRunning = false;
  let jsHabits: string[] = [];
  let sidebarOpen = false;

  onMount(async () => {
    mounted = true;

    // Initialize Supabase auth (if configured)
    await initAuth();

    // Initialize progress from localStorage/cloud
    await progress.init();

    // Start loading Pyodide in background
    initPyodide();

    // Load current exercise
    if ($currentExerciseId) {
      await loadExercise($currentExerciseId);
    }
  });

  let mounted = false;

  async function loadExercise(id: string) {
    if (!mounted) return;

    const metadata = $currentExerciseMetadata;
    if (!metadata) return;

    try {
      // metadata.path is like "exercises/01-basics/01_variables_and_types.py"
      const response = await fetch(`/${metadata.path}`);
      const content = await response.text();
      currentExercise = parseExercise(content);
      testResult = null;
      jsHabits = [];
    } catch (error) {
      console.error('Failed to load exercise:', error);
    }
  }

  // Reactively load exercise when currentExerciseId changes (only after mount)
  $: if (mounted && $currentExerciseId) {
    loadExercise($currentExerciseId);
  }

  function handleExerciseSelect(event: CustomEvent<{ id: string }>) {
    currentExerciseId.set(event.detail.id);
    progress.setCurrentExercise(event.detail.id);
  }

  function handleSidebarClose() {
    sidebarOpen = false;
  }

  function handleToggleSidebar() {
    sidebarOpen = !sidebarOpen;
  }

  function handleCodeChange(event: CustomEvent<{ value: string }>) {
    // Just track in memory for now
  }

  function handleCodeSave(event: CustomEvent<{ value: string }>) {
    if ($currentExerciseId) {
      progress.saveCode($currentExerciseId, event.detail.value);
    }
  }

  async function handleRun() {
    if (!currentExercise || !$currentExerciseId) return;

    isRunning = true;
    testResult = null;

    try {
      const userCode = exerciseView.getCode();

      // Check for JS habits
      jsHabits = detectJsHabits(userCode);

      // Run the tests
      testResult = await runTests(userCode, currentExercise.testCode);

      // Update progress if successful
      if (testResult.success) {
        progress.markCompleted($currentExerciseId);
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
      on:select={handleExerciseSelect}
      on:close={handleSidebarClose}
    />
    <ExerciseView
      bind:this={exerciseView}
      exercise={currentExercise}
      metadata={$currentExerciseMetadata}
      savedCode={$progress.savedCode[$currentExerciseId ?? '']}
      {testResult}
      {isRunning}
      {jsHabits}
      on:codeChange={handleCodeChange}
      on:codeSave={handleCodeSave}
      on:run={handleRun}
    />
  </main>
</div>

<style>
  :global(body) {
    margin: 0;
    padding: 0;
    font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif;
    background: #1e1e1e;
    color: #d4d4d4;
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
