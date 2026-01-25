declare module 'monaco-jsx-syntax-highlight' {
  import type * as Monaco from 'monaco-editor';

  export function getWorker(): Worker;

  export class MonacoJsxSyntaxHighlight {
    constructor(worker: Worker | string, monaco: typeof Monaco, options?: {
      customTypescriptUrl?: string;
    });

    highlighterBuilder(context: {
      editor: Monaco.editor.IStandaloneCodeEditor;
      filePath?: string;
    }, config?: {
      jsxTagCycle?: number;
      enableConsole?: boolean;
    }): {
      highlighter: (code?: string) => void;
      dispose: () => void;
    };
  }
}
