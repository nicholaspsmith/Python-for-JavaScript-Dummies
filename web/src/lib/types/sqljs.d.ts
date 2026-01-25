declare module 'sql.js' {
  interface SqlJsStatic {
    Database: typeof Database;
  }

  interface Database {
    new (): Database;
    run(sql: string, params?: unknown[]): void;
    // Execute SQL and return results
    exec(sql: string): QueryExecResult[];
    close(): void;
    getRowsModified(): number;
  }

  interface QueryExecResult {
    columns: string[];
    values: unknown[][];
  }

  interface SqlJsConfig {
    locateFile?: (file: string) => string;
  }

  function initSqlJs(config?: SqlJsConfig): Promise<SqlJsStatic>;
  export default initSqlJs;
}
