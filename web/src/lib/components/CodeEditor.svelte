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

  // Track workers and blob URLs for cleanup
  let monacoWorker: Worker | null = null;
  let monacoWorkerBlobUrl: string | null = null;
  let jsxWorker: Worker | null = null;

  function getMonacoTheme(currentTheme: string): string {
    return currentTheme === 'light' ? 'vs' : 'vs-dark';
  }

  // Track if we've already registered completion providers
  let pythonCompletionsRegistered = false;
  let tsCompletionsRegistered = false;
  let sqlCompletionsRegistered = false;

  function registerPythonCompletions(monacoInstance: typeof Monaco) {
    if (pythonCompletionsRegistered) return;
    pythonCompletionsRegistered = true;

    const pythonKeywords = [
      'False', 'None', 'True', 'and', 'as', 'assert', 'async', 'await',
      'break', 'class', 'continue', 'def', 'del', 'elif', 'else', 'except',
      'finally', 'for', 'from', 'global', 'if', 'import', 'in', 'is',
      'lambda', 'nonlocal', 'not', 'or', 'pass', 'raise', 'return', 'try',
      'while', 'with', 'yield'
    ];

    const pythonBuiltins = [
      'abs', 'all', 'any', 'bin', 'bool', 'bytes', 'callable', 'chr',
      'dict', 'dir', 'divmod', 'enumerate', 'eval', 'filter', 'float',
      'format', 'frozenset', 'getattr', 'globals', 'hasattr', 'hash',
      'help', 'hex', 'id', 'input', 'int', 'isinstance', 'issubclass',
      'iter', 'len', 'list', 'locals', 'map', 'max', 'min', 'next',
      'object', 'oct', 'open', 'ord', 'pow', 'print', 'range', 'repr',
      'reversed', 'round', 'set', 'setattr', 'slice', 'sorted', 'str',
      'sum', 'super', 'tuple', 'type', 'vars', 'zip'
    ];

    const pythonSnippets = [
      { label: 'def', insertText: 'def ${1:function_name}(${2:params}):\n    ${3:pass}', documentation: 'Define a function' },
      { label: 'class', insertText: 'class ${1:ClassName}:\n    def __init__(self${2:, params}):\n        ${3:pass}', documentation: 'Define a class' },
      { label: 'if', insertText: 'if ${1:condition}:\n    ${2:pass}', documentation: 'If statement' },
      { label: 'for', insertText: 'for ${1:item} in ${2:iterable}:\n    ${3:pass}', documentation: 'For loop' },
      { label: 'while', insertText: 'while ${1:condition}:\n    ${2:pass}', documentation: 'While loop' },
      { label: 'try', insertText: 'try:\n    ${1:pass}\nexcept ${2:Exception} as ${3:e}:\n    ${4:pass}', documentation: 'Try/except block' },
      { label: 'with', insertText: 'with ${1:expression} as ${2:variable}:\n    ${3:pass}', documentation: 'With statement' },
      { label: 'lambda', insertText: 'lambda ${1:x}: ${2:x}', documentation: 'Lambda function' },
      { label: 'list comprehension', insertText: '[${1:x} for ${2:x} in ${3:iterable}]', documentation: 'List comprehension' },
      { label: 'dict comprehension', insertText: '{${1:k}: ${2:v} for ${3:k}, ${4:v} in ${5:iterable}}', documentation: 'Dictionary comprehension' },
    ];

    monacoInstance.languages.registerCompletionItemProvider('python', {
      provideCompletionItems: (model, position) => {
        const word = model.getWordUntilPosition(position);
        const range = {
          startLineNumber: position.lineNumber,
          endLineNumber: position.lineNumber,
          startColumn: word.startColumn,
          endColumn: word.endColumn
        };

        const suggestions: Monaco.languages.CompletionItem[] = [];

        // Add keywords
        for (const keyword of pythonKeywords) {
          suggestions.push({
            label: keyword,
            kind: monacoInstance.languages.CompletionItemKind.Keyword,
            insertText: keyword,
            range
          });
        }

        // Add builtins
        for (const builtin of pythonBuiltins) {
          suggestions.push({
            label: builtin,
            kind: monacoInstance.languages.CompletionItemKind.Function,
            insertText: builtin,
            detail: 'Built-in function',
            range
          });
        }

        // Add snippets
        for (const snippet of pythonSnippets) {
          suggestions.push({
            label: snippet.label,
            kind: monacoInstance.languages.CompletionItemKind.Snippet,
            insertText: snippet.insertText,
            insertTextRules: monacoInstance.languages.CompletionItemInsertTextRule.InsertAsSnippet,
            documentation: snippet.documentation,
            range
          });
        }

        return { suggestions };
      }
    });
  }

  function registerTypeScriptCompletions(monacoInstance: typeof Monaco) {
    if (tsCompletionsRegistered) return;
    tsCompletionsRegistered = true;

    const tsKeywords = [
      'abstract', 'any', 'as', 'async', 'await', 'boolean', 'break', 'case',
      'catch', 'class', 'const', 'continue', 'debugger', 'declare', 'default',
      'delete', 'do', 'else', 'enum', 'export', 'extends', 'false', 'finally',
      'for', 'from', 'function', 'get', 'if', 'implements', 'import', 'in',
      'instanceof', 'interface', 'let', 'module', 'namespace', 'new', 'null',
      'number', 'object', 'of', 'package', 'private', 'protected', 'public',
      'readonly', 'return', 'set', 'static', 'string', 'super', 'switch',
      'this', 'throw', 'true', 'try', 'type', 'typeof', 'undefined', 'var',
      'void', 'while', 'with', 'yield'
    ];

    const tsBuiltins = [
      'Array', 'Boolean', 'console', 'Date', 'Error', 'Function', 'JSON',
      'Math', 'Number', 'Object', 'Promise', 'RegExp', 'String', 'Symbol',
      'Map', 'Set', 'WeakMap', 'WeakSet', 'parseInt', 'parseFloat', 'isNaN',
      'isFinite', 'encodeURI', 'decodeURI', 'setTimeout', 'setInterval',
      'clearTimeout', 'clearInterval', 'fetch', 'Response', 'Request'
    ];

    const tsSnippets = [
      { label: 'function', insertText: 'function ${1:name}(${2:params}) {\n  ${3}\n}', documentation: 'Function declaration' },
      { label: 'arrow function', insertText: 'const ${1:name} = (${2:params}) => {\n  ${3}\n};', documentation: 'Arrow function' },
      { label: 'async function', insertText: 'async function ${1:name}(${2:params}) {\n  ${3}\n}', documentation: 'Async function' },
      { label: 'class', insertText: 'class ${1:Name} {\n  constructor(${2:params}) {\n    ${3}\n  }\n}', documentation: 'Class declaration' },
      { label: 'interface', insertText: 'interface ${1:Name} {\n  ${2:property}: ${3:type};\n}', documentation: 'Interface declaration' },
      { label: 'type', insertText: 'type ${1:Name} = ${2:type};', documentation: 'Type alias' },
      { label: 'if', insertText: 'if (${1:condition}) {\n  ${2}\n}', documentation: 'If statement' },
      { label: 'for', insertText: 'for (let ${1:i} = 0; ${1:i} < ${2:length}; ${1:i}++) {\n  ${3}\n}', documentation: 'For loop' },
      { label: 'for...of', insertText: 'for (const ${1:item} of ${2:iterable}) {\n  ${3}\n}', documentation: 'For...of loop' },
      { label: 'forEach', insertText: '${1:array}.forEach((${2:item}) => {\n  ${3}\n});', documentation: 'forEach loop' },
      { label: 'map', insertText: '${1:array}.map((${2:item}) => ${3});', documentation: 'Array map' },
      { label: 'filter', insertText: '${1:array}.filter((${2:item}) => ${3});', documentation: 'Array filter' },
      { label: 'reduce', insertText: '${1:array}.reduce((${2:acc}, ${3:item}) => {\n  ${4}\n}, ${5:initial});', documentation: 'Array reduce' },
      { label: 'try/catch', insertText: 'try {\n  ${1}\n} catch (${2:error}) {\n  ${3}\n}', documentation: 'Try/catch block' },
      { label: 'promise', insertText: 'new Promise((resolve, reject) => {\n  ${1}\n});', documentation: 'New Promise' },
      { label: 'console.log', insertText: 'console.log(${1});', documentation: 'Console log' },
      { label: 'useState', insertText: 'const [${1:state}, set${1/(.*)/${1:/capitalize}/}] = useState(${2:initial});', documentation: 'React useState hook' },
      { label: 'useEffect', insertText: 'useEffect(() => {\n  ${1}\n}, [${2}]);', documentation: 'React useEffect hook' },
    ];

    // Register for both JavaScript and TypeScript
    const languages = ['javascript', 'typescript', 'javascriptreact', 'typescriptreact'];

    for (const lang of languages) {
      monacoInstance.languages.registerCompletionItemProvider(lang, {
        triggerCharacters: ['.', '"', "'", '`', '/', '@', '<', ' '],
        provideCompletionItems: (model, position) => {
          const word = model.getWordUntilPosition(position);
          const range = {
            startLineNumber: position.lineNumber,
            endLineNumber: position.lineNumber,
            startColumn: word.startColumn,
            endColumn: word.endColumn
          };

          const suggestions: Monaco.languages.CompletionItem[] = [];

          for (const keyword of tsKeywords) {
            suggestions.push({
              label: keyword,
              kind: monacoInstance.languages.CompletionItemKind.Keyword,
              insertText: keyword,
              range
            });
          }

          for (const builtin of tsBuiltins) {
            suggestions.push({
              label: builtin,
              kind: monacoInstance.languages.CompletionItemKind.Class,
              insertText: builtin,
              detail: 'Built-in',
              range
            });
          }

          for (const snippet of tsSnippets) {
            suggestions.push({
              label: snippet.label,
              kind: monacoInstance.languages.CompletionItemKind.Snippet,
              insertText: snippet.insertText,
              insertTextRules: monacoInstance.languages.CompletionItemInsertTextRule.InsertAsSnippet,
              documentation: snippet.documentation,
              range
            });
          }

          return { suggestions, incomplete: true };
        }
      });
    }
  }

  function registerSqlCompletions(monacoInstance: typeof Monaco) {
    if (sqlCompletionsRegistered) return;
    sqlCompletionsRegistered = true;

    const sqlKeywords = [
      'SELECT', 'FROM', 'WHERE', 'AND', 'OR', 'NOT', 'IN', 'LIKE', 'BETWEEN',
      'IS', 'NULL', 'AS', 'JOIN', 'INNER', 'LEFT', 'RIGHT', 'OUTER', 'FULL',
      'ON', 'GROUP', 'BY', 'HAVING', 'ORDER', 'ASC', 'DESC', 'LIMIT', 'OFFSET',
      'INSERT', 'INTO', 'VALUES', 'UPDATE', 'SET', 'DELETE', 'CREATE', 'TABLE',
      'DROP', 'ALTER', 'ADD', 'COLUMN', 'INDEX', 'PRIMARY', 'KEY', 'FOREIGN',
      'REFERENCES', 'UNIQUE', 'DEFAULT', 'CHECK', 'CONSTRAINT', 'CASCADE',
      'UNION', 'ALL', 'DISTINCT', 'EXISTS', 'CASE', 'WHEN', 'THEN', 'ELSE',
      'END', 'CAST', 'CONVERT', 'COALESCE', 'NULLIF', 'WITH', 'RECURSIVE',
      'OVER', 'PARTITION', 'ROW_NUMBER', 'RANK', 'DENSE_RANK', 'NTILE',
      'LEAD', 'LAG', 'FIRST_VALUE', 'LAST_VALUE'
    ];

    const sqlFunctions = [
      'COUNT', 'SUM', 'AVG', 'MIN', 'MAX', 'ABS', 'ROUND', 'CEIL', 'FLOOR',
      'UPPER', 'LOWER', 'TRIM', 'LTRIM', 'RTRIM', 'LENGTH', 'SUBSTRING',
      'CONCAT', 'REPLACE', 'INSTR', 'LEFT', 'RIGHT', 'REVERSE', 'REPEAT',
      'NOW', 'DATE', 'TIME', 'DATETIME', 'YEAR', 'MONTH', 'DAY', 'HOUR',
      'MINUTE', 'SECOND', 'DATEDIFF', 'DATEADD', 'STRFTIME', 'JULIANDAY',
      'IFNULL', 'IIF', 'TYPEOF', 'PRINTF', 'RANDOM', 'GROUP_CONCAT'
    ];

    const sqlSnippets = [
      { label: 'SELECT', insertText: 'SELECT ${1:columns}\nFROM ${2:table}\nWHERE ${3:condition};', documentation: 'Basic SELECT query' },
      { label: 'SELECT JOIN', insertText: 'SELECT ${1:columns}\nFROM ${2:table1}\nJOIN ${3:table2} ON ${4:condition}\nWHERE ${5:condition};', documentation: 'SELECT with JOIN' },
      { label: 'INSERT', insertText: 'INSERT INTO ${1:table} (${2:columns})\nVALUES (${3:values});', documentation: 'INSERT statement' },
      { label: 'UPDATE', insertText: 'UPDATE ${1:table}\nSET ${2:column} = ${3:value}\nWHERE ${4:condition};', documentation: 'UPDATE statement' },
      { label: 'DELETE', insertText: 'DELETE FROM ${1:table}\nWHERE ${2:condition};', documentation: 'DELETE statement' },
      { label: 'CREATE TABLE', insertText: 'CREATE TABLE ${1:table_name} (\n  ${2:id} INTEGER PRIMARY KEY,\n  ${3:column} ${4:TEXT}\n);', documentation: 'CREATE TABLE statement' },
      { label: 'GROUP BY', insertText: 'SELECT ${1:column}, COUNT(*)\nFROM ${2:table}\nGROUP BY ${1:column};', documentation: 'GROUP BY query' },
      { label: 'ORDER BY', insertText: 'SELECT ${1:columns}\nFROM ${2:table}\nORDER BY ${3:column} ${4|ASC,DESC|};', documentation: 'ORDER BY clause' },
      { label: 'CASE', insertText: 'CASE\n  WHEN ${1:condition} THEN ${2:result}\n  ELSE ${3:default}\nEND', documentation: 'CASE expression' },
      { label: 'CTE', insertText: 'WITH ${1:cte_name} AS (\n  ${2:query}\n)\nSELECT * FROM ${1:cte_name};', documentation: 'Common Table Expression' },
      { label: 'subquery', insertText: 'SELECT ${1:columns}\nFROM ${2:table}\nWHERE ${3:column} IN (\n  SELECT ${4:column}\n  FROM ${5:table2}\n);', documentation: 'Subquery in WHERE' },
    ];

    monacoInstance.languages.registerCompletionItemProvider('sql', {
      provideCompletionItems: (model, position) => {
        const word = model.getWordUntilPosition(position);
        const range = {
          startLineNumber: position.lineNumber,
          endLineNumber: position.lineNumber,
          startColumn: word.startColumn,
          endColumn: word.endColumn
        };

        const suggestions: Monaco.languages.CompletionItem[] = [];

        for (const keyword of sqlKeywords) {
          suggestions.push({
            label: keyword,
            kind: monacoInstance.languages.CompletionItemKind.Keyword,
            insertText: keyword,
            range
          });
          // Also add lowercase version
          suggestions.push({
            label: keyword.toLowerCase(),
            kind: monacoInstance.languages.CompletionItemKind.Keyword,
            insertText: keyword.toLowerCase(),
            range
          });
        }

        for (const func of sqlFunctions) {
          suggestions.push({
            label: func,
            kind: monacoInstance.languages.CompletionItemKind.Function,
            insertText: func + '(${1})',
            insertTextRules: monacoInstance.languages.CompletionItemInsertTextRule.InsertAsSnippet,
            detail: 'SQL function',
            range
          });
        }

        for (const snippet of sqlSnippets) {
          suggestions.push({
            label: snippet.label,
            kind: monacoInstance.languages.CompletionItemKind.Snippet,
            insertText: snippet.insertText,
            insertTextRules: monacoInstance.languages.CompletionItemInsertTextRule.InsertAsSnippet,
            documentation: snippet.documentation,
            range
          });
        }

        return { suggestions };
      }
    });
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
        // Clean up previous worker if exists
        if (monacoWorker) {
          monacoWorker.terminate();
        }
        if (monacoWorkerBlobUrl) {
          URL.revokeObjectURL(monacoWorkerBlobUrl);
        }

        // Return a minimal no-op worker to prevent errors
        const blob = new Blob([
          'self.onmessage = function() {}'
        ], { type: 'application/javascript' });
        monacoWorkerBlobUrl = URL.createObjectURL(blob);
        monacoWorker = new Worker(monacoWorkerBlobUrl);
        return monacoWorker;
      }
    };

    // Dynamic import for Monaco to avoid SSR issues
    monaco = await import('monaco-editor');

    // Check again if we're still mounted after async import
    if (!isMounted || !container?.isConnected) {
      console.warn('CodeEditor: component unmounted during Monaco load');
      return;
    }

    // Disable TypeScript/JavaScript diagnostics and suggestions (we use our own)
    const ts = (monaco.languages as any).typescript;
    if (ts?.javascriptDefaults) {
      ts.javascriptDefaults.setDiagnosticsOptions({
        noSemanticValidation: true,
        noSyntaxValidation: true
      });
      // Disable built-in completions by setting empty extra libs
      ts.javascriptDefaults.setCompilerOptions({
        noLib: true,
        allowNonTsExtensions: true
      });
    }
    if (ts?.typescriptDefaults) {
      ts.typescriptDefaults.setDiagnosticsOptions({
        noSemanticValidation: true,
        noSyntaxValidation: true
      });
      ts.typescriptDefaults.setCompilerOptions({
        noLib: true,
        allowNonTsExtensions: true
      });
    }

    // Register completion providers BEFORE creating editor
    if (language === 'python') {
      registerPythonCompletions(monaco);
    } else if (language === 'javascript' || language === 'typescript' || language === 'javascriptreact' || language === 'typescriptreact') {
      registerTypeScriptCompletions(monaco);
    } else if (language === 'sql') {
      registerSqlCompletions(monaco);
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
      // Enable autocomplete
      quickSuggestions: true,
      suggestOnTriggerCharacters: true,
      wordBasedSuggestions: 'currentDocument',
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

      // Get the worker and store reference for cleanup
      jsxWorker = getWorker();
      const monacoJsxSyntaxHighlight = new MonacoJsxSyntaxHighlight(jsxWorker, monaco);

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

    // Clean up JSX highlighter and worker
    jsxHighlighter?.dispose?.();
    if (jsxWorker) {
      jsxWorker.terminate();
      jsxWorker = null;
    }

    // Clean up Monaco editor
    const model = editor?.getModel();
    editor?.dispose();
    model?.dispose();

    // Clean up Monaco worker and blob URL
    if (monacoWorker) {
      monacoWorker.terminate();
      monacoWorker = null;
    }
    if (monacoWorkerBlobUrl) {
      URL.revokeObjectURL(monacoWorkerBlobUrl);
      monacoWorkerBlobUrl = null;
    }
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
