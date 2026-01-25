declare module 'monaco-jsx-highlighter' {
  import type * as Monaco from 'monaco-editor';

  export default class MonacoJSXHighlighter {
    constructor(
      monaco: typeof Monaco,
      babelParse: (code: string) => any,
      traverse: any,
      editor: Monaco.editor.IStandaloneCodeEditor
    );

    highlightOnDidChangeModelContent(debounceTime?: number): () => void;
    addJSXCommentCommand(): () => void;
    highlightCode(): void;
  }
}
