<script lang="ts">
  import { onMount, onDestroy, createEventDispatcher } from 'svelte';
  import type * as Monaco from 'monaco-editor';
  import { theme } from '../stores/theme';

  export let value: string = '';
  export let language: string = 'python';
  export let readOnly: boolean = false;

  const dispatch = createEventDispatcher();

  let container: HTMLDivElement;
  let editor: Monaco.editor.IStandaloneCodeEditor | null = null;
  let monaco: typeof Monaco;

  // Debounce timer for auto-save
  let saveTimeout: ReturnType<typeof setTimeout>;

  // Subscribe to theme changes
  let unsubscribeTheme: (() => void) | null = null;

  function getMonacoTheme(currentTheme: string): string {
    return currentTheme === 'light' ? 'python-light' : 'python-dark';
  }

  onMount(async () => {
    // Dynamic import for Monaco to avoid SSR issues
    monaco = await import('monaco-editor');

    // Configure dark theme
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

    // Configure light theme
    monaco.editor.defineTheme('python-light', {
      base: 'vs',
      inherit: true,
      rules: [
        { token: 'comment', foreground: '008000' },
        { token: 'string', foreground: 'a31515' },
        { token: 'keyword', foreground: '0000ff' },
        { token: 'number', foreground: '098658' },
        { token: 'type', foreground: '267f99' },
      ],
      colors: {
        'editor.background': '#ffffff',
        'editor.foreground': '#333333',
        'editorLineNumber.foreground': '#999999',
        'editorLineNumber.activeForeground': '#333333',
        'editor.selectionBackground': '#add6ff',
        'editor.lineHighlightBackground': '#f5f5f5',
      }
    });

    // Get initial theme
    let currentTheme = 'dark';
    const unsubInit = theme.subscribe(t => { currentTheme = t; });
    unsubInit();

    editor = monaco.editor.create(container, {
      value,
      language,
      theme: getMonacoTheme(currentTheme),
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

    // Subscribe to theme changes and update editor theme
    unsubscribeTheme = theme.subscribe(t => {
      if (monaco && editor) {
        monaco.editor.setTheme(getMonacoTheme(t));
      }
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
    unsubscribeTheme?.();
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
