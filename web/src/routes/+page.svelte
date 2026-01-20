<script lang="ts">
  import { onMount } from 'svelte';
  import Header from '$lib/components/Header.svelte';
  import Sidebar from '$lib/components/Sidebar.svelte';
  import ExerciseView from '$lib/components/ExerciseView.svelte';
  import { progress } from '$lib/stores/progress';
  import { currentExerciseId, currentExerciseMetadata, getNextExerciseId } from '$lib/stores/exercises';
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
  let sidebarCollapsed = false;
  let instructionsCollapsed = false;

  onMount(async () => {
    mounted = true;

    // Restore collapsed states
    sidebarCollapsed = localStorage.getItem('sidebarCollapsed') === 'true';
    instructionsCollapsed = localStorage.getItem('instructionsCollapsed') === 'true';

    // Initialize Supabase auth (if configured)
    await initAuth();

    // Initialize progress from localStorage/cloud (restores current exercise)
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
      // metadata.path is like "exercises/01-easy/01_two_sum.py"
      const response = await fetch(`/${metadata.path}`);
      const content = await response.text();
      currentExercise = parseExercise(content);
      testResult = null;
      jsHabits = [];

      // Check for stale saved code from old exercise format
      const savedCode = $progress.savedCode[id];
      if (savedCode && isStaleCode(savedCode, currentExercise.codeTemplate)) {
        progress.saveCode(id, currentExercise.codeTemplate);
      }
    } catch (error) {
      console.error('Failed to load exercise:', error);
    }
  }

  // Detect if saved code is from old exercise format
  function isStaleCode(savedCode: string, template: string): boolean {
    // Old exercises started with "# Exercise" comments
    if (savedCode.trimStart().startsWith('# Exercise')) return true;
    // Old exercises had "# ===" separators at the start
    if (savedCode.trimStart().startsWith('# ===')) return true;
    // Saved code contains TESTS separator (should have been stripped)
    if (savedCode.includes('# ============= TESTS =============')) return true;
    // Check if the template's function definition exists in saved code
    const funcMatch = template.match(/^def\s+(\w+)/m);
    if (funcMatch && !savedCode.includes(`def ${funcMatch[1]}`)) return true;
    return false;
  }

  // Reactively load exercise when currentExerciseId changes (only after mount)
  $: if (mounted && $currentExerciseId) {
    loadExercise($currentExerciseId);
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
    <ExerciseView
      bind:this={exerciseView}
      exercise={currentExercise}
      metadata={$currentExerciseMetadata}
      savedCode={$progress.savedCode[$currentExerciseId ?? '']}
      {testResult}
      {isRunning}
      {jsHabits}
      {instructionsCollapsed}
      on:codeChange={handleCodeChange}
      on:codeSave={handleCodeSave}
      on:run={handleRun}
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
