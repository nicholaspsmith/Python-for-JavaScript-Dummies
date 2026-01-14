<script lang="ts">
  import { onMount, onDestroy, createEventDispatcher } from 'svelte';
  import type * as Monaco from 'monaco-editor';

  export let value: string = '';
  export let language: string = 'python';
  export let readOnly: boolean = false;

  const dispatch = createEventDispatcher();

  let container: HTMLDivElement;
  let editor: Monaco.editor.IStandaloneCodeEditor | null = null;
  let monaco: typeof Monaco;

  // Debounce timer for auto-save
  let saveTimeout: ReturnType<typeof setTimeout>;

  onMount(async () => {
    // Dynamic import for Monaco to avoid SSR issues
    monaco = await import('monaco-editor');

    // Configure Monaco
    monaco.editor.defineTheme('python-dark', {
      base: 'vs-dark',
      inherit: true,
      rules: [
        { token: 'comment', foreground: '6a9955' },
        { token: 'string', foreground: 'ce9178' },
        { token: 'keyword', foreground: '569cd6' },
        { token: 'number', foreground: 'b5cea8' },
        { token: 'type', foreground: '4ec9b0' },
      ],
      colors: {
        'editor.background': '#1e1e1e',
        'editor.foreground': '#d4d4d4',
        'editorLineNumber.foreground': '#858585',
        'editorLineNumber.activeForeground': '#c6c6c6',
        'editor.selectionBackground': '#264f78',
        'editor.lineHighlightBackground': '#2a2a2a',
      }
    });

    editor = monaco.editor.create(container, {
      value,
      language,
      theme: 'python-dark',
      readOnly,
      minimap: { enabled: false },
      fontSize: 14,
      lineNumbers: 'on',
      scrollBeyondLastLine: false,
      automaticLayout: true,
      tabSize: 4,
      insertSpaces: true,
      wordWrap: 'on',
      padding: { top: 16, bottom: 16 },
      renderLineHighlight: 'line',
      cursorBlinking: 'smooth',
      smoothScrolling: true,
    });

    // Handle content changes
    editor.onDidChangeModelContent(() => {
      const newValue = editor?.getValue() || '';
      dispatch('change', { value: newValue });

      // Debounced save
      clearTimeout(saveTimeout);
      saveTimeout = setTimeout(() => {
        dispatch('save', { value: newValue });
      }, 1000);
    });

    // Add keyboard shortcut for running tests (Cmd/Ctrl + Enter)
    editor.addCommand(monaco.KeyMod.CtrlCmd | monaco.KeyCode.Enter, () => {
      dispatch('run');
    });
  });

  onDestroy(() => {
    clearTimeout(saveTimeout);
    editor?.dispose();
  });

  // Update editor value when prop changes
  $: if (editor && value !== editor.getValue()) {
    editor.setValue(value);
  }

  // Update read-only state
  $: if (editor) {
    editor.updateOptions({ readOnly });
  }

  /**
   * Reset editor to provided value
   */
  export function reset(newValue: string) {
    if (editor) {
      editor.setValue(newValue);
    }
  }

  /**
   * Get current editor value
   */
  export function getValue(): string {
    return editor?.getValue() || '';
  }

  /**
   * Focus the editor
   */
  export function focus() {
    editor?.focus();
  }
</script>

<div class="editor-container" bind:this={container}></div>

<style>
  .editor-container {
    width: 100%;
    height: 100%;
    min-height: 300px;
  }
</style>
