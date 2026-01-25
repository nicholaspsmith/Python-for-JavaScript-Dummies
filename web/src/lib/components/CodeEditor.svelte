<script lang="ts">
  import { onMount, onDestroy, createEventDispatcher, tick } from 'svelte';
  import type * as Monaco from 'monaco-editor';
  import { browser } from '$app/environment';
  import { theme } from '../stores/theme';

  export let value: string = '';
  export let language: string = 'python';
  export let readOnly: boolean = false;
  export let isJsx: boolean = false;

  const dispatch = createEventDispatcher();

  let container: HTMLDivElement;
  let editor: Monaco.editor.IStandaloneCodeEditor | null = null;
  let monaco: typeof Monaco;
  let jsxHighlighter: any = null;
  let isMounted = true;

  // Debounce timer for auto-save
  let saveTimeout: ReturnType<typeof setTimeout>;

  // Subscribe to theme changes
  let unsubscribeTheme: (() => void) | null = null;

  function getMonacoTheme(currentTheme: string): string {
    return currentTheme === 'light' ? 'vs' : 'vs-dark';
  }

  onMount(async () => {
    if (!browser) return;

    // Wait for container to be available with retry
    const waitForContainer = async (retries = 10): Promise<boolean> => {
      for (let i = 0; i < retries; i++) {
        if (!isMounted) return false;
        if (container && container.isConnected) return true;
        await new Promise(r => setTimeout(r, 50));
      }
      return false;
    };

    const containerReady = await waitForContainer();
    if (!containerReady || !isMounted) {
      console.warn('CodeEditor: component unmounted or container not ready');
      return;
    }

    // Configure Monaco environment BEFORE importing to prevent worker errors
    // We only need syntax highlighting, not IntelliSense or diagnostics
    (window as any).MonacoEnvironment = {
      getWorker: function () {
        // Return a minimal no-op worker to prevent errors
        const blob = new Blob([
          'self.onmessage = function() {}'
        ], { type: 'application/javascript' });
        return new Worker(URL.createObjectURL(blob));
      }
    };

    // Dynamic import for Monaco to avoid SSR issues
    monaco = await import('monaco-editor');

    // Check again if we're still mounted after async import
    if (!isMounted || !container?.isConnected) {
      console.warn('CodeEditor: component unmounted during Monaco load');
      return;
    }

    // Disable TypeScript/JavaScript diagnostics (we only need syntax highlighting)
    const ts = (monaco.languages as any).typescript;
    if (ts?.javascriptDefaults) {
      ts.javascriptDefaults.setDiagnosticsOptions({
        noSemanticValidation: true,
        noSyntaxValidation: true
      });
    }
    if (ts?.typescriptDefaults) {
      ts.typescriptDefaults.setDiagnosticsOptions({
        noSemanticValidation: true,
        noSyntaxValidation: true
      });
    }

    // Get initial theme
    let currentTheme = 'dark';
    const unsubInit = theme.subscribe(t => { currentTheme = t; });
    unsubInit();

    // Determine file extension based on language (required for JSX highlighting)
    const getFileExtension = (lang: string, jsx: boolean): string => {
      switch (lang) {
        case 'javascriptreact': return 'jsx';
        case 'typescriptreact': return 'tsx';
        case 'javascript': return jsx ? 'jsx' : 'js';
        case 'typescript': return jsx ? 'tsx' : 'ts';
        case 'python': return 'py';
        case 'sql': return 'sql';
        default: return 'txt';
      }
    };

    // Create model with proper file URI (required for JSX syntax highlight)
    const fileExt = getFileExtension(language, isJsx);
    const modelUri = monaco.Uri.parse(`file:///main.${fileExt}`);
    const model = monaco.editor.createModel(value, language, modelUri);

    editor = monaco.editor.create(container, {
      model,
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

    // Set up JSX highlighting if needed
    if (isJsx || language === 'javascriptreact' || language === 'typescriptreact') {
      setupJSXHighlighter();
    }
  });

  async function setupJSXHighlighter() {
    if (!editor || !monaco) return;

    try {
      const { MonacoJsxSyntaxHighlight, getWorker } = await import('monaco-jsx-syntax-highlight');

      const monacoJsxSyntaxHighlight = new MonacoJsxSyntaxHighlight(getWorker(), monaco);

      const { highlighter, dispose } = monacoJsxSyntaxHighlight.highlighterBuilder({
        editor: editor
      });

      // Store dispose function for cleanup
      jsxHighlighter = { dispose };

      // Initial highlight
      highlighter();

      // Highlight on content change
      editor.onDidChangeModelContent(() => {
        highlighter();
      });

      console.log('JSX highlighter initialized successfully');
    } catch (error) {
      console.error('Failed to setup JSX highlighter:', error);
    }
  }

  onDestroy(() => {
    isMounted = false;
    clearTimeout(saveTimeout);
    unsubscribeTheme?.();
    jsxHighlighter?.dispose?.();
    const model = editor?.getModel();
    editor?.dispose();
    model?.dispose();
  });

  // Update editor value when prop changes
  $: if (editor && value !== editor.getValue()) {
    editor.setValue(value);
  }

  // Update language when prop changes (create new model with correct URI for JSX)
  $: if (editor && monaco && language) {
    const oldModel = editor.getModel();
    const currentValue = oldModel?.getValue() || value;

    // Determine file extension based on language
    const getFileExt = (lang: string, jsx: boolean): string => {
      switch (lang) {
        case 'javascriptreact': return 'jsx';
        case 'typescriptreact': return 'tsx';
        case 'javascript': return jsx ? 'jsx' : 'js';
        case 'typescript': return jsx ? 'tsx' : 'ts';
        case 'python': return 'py';
        case 'sql': return 'sql';
        default: return 'txt';
      }
    };

    const ext = getFileExt(language, isJsx);

    // Create new model with correct URI
    const newUri = monaco.Uri.parse(`file:///main.${ext}`);

    // Only recreate if URI extension changed
    if (!oldModel || !oldModel.uri.path.endsWith(`.${ext}`)) {
      const newModel = monaco.editor.createModel(currentValue, language, newUri);
      editor.setModel(newModel);
      oldModel?.dispose();

      // Setup JSX highlighter when switching to JSX
      if ((isJsx || language === 'javascriptreact' || language === 'typescriptreact') && !jsxHighlighter) {
        setupJSXHighlighter();
      }
    }
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

  /* JSX Syntax Highlighting Styles (monaco-jsx-syntax-highlight) - Dark Mode */
  :global([data-theme="dark"] .jsx-tag-angle-bracket) {
    color: #808080 !important;
  }
  :global([data-theme="dark"] .jsx-tag-name) {
    color: #4ec9b0 !important;
  }
  :global([data-theme="dark"] .jsx-tag-attribute-key) {
    color: #9cdcfe !important;
  }
  :global([data-theme="dark"] .jsx-expression-braces) {
    color: #ffd700 !important;
  }
  :global([data-theme="dark"] .jsx-text) {
    color: #d4d4d4 !important;
  }

  /* JSX Syntax Highlighting Styles (monaco-jsx-syntax-highlight) - Light Mode */
  :global([data-theme="light"] .jsx-tag-angle-bracket) {
    color: #808080 !important;
  }
  :global([data-theme="light"] .jsx-tag-name) {
    color: #267f99 !important;
  }
  :global([data-theme="light"] .jsx-tag-attribute-key) {
    color: #e50000 !important;
  }
  :global([data-theme="light"] .jsx-expression-braces) {
    color: #0431fa !important;
  }
  :global([data-theme="light"] .jsx-text) {
    color: #333333 !important;
  }
</style>
