import { writable, get } from 'svelte/store';

// Sandpack loading state
export const sandpackReady = writable<boolean>(false);
export const sandpackLoading = writable<boolean>(false);
export const sandpackError = writable<string | null>(null);

// Store the Sandpack module
let SandpackModule: any = null;

/**
 * Initialize Sandpack client
 */
export async function initSandpack(): Promise<void> {
  if (SandpackModule || get(sandpackLoading)) {
    return;
  }

  sandpackLoading.set(true);
  sandpackError.set(null);

  try {
    // Dynamically import Sandpack client
    SandpackModule = await import('@codesandbox/sandpack-client');

    sandpackReady.set(true);
    console.log('Sandpack client loaded successfully');
  } catch (error) {
    const message = error instanceof Error ? error.message : 'Failed to load Sandpack';
    sandpackError.set(message);
    console.error('Failed to load Sandpack:', error);
    throw error;
  } finally {
    sandpackLoading.set(false);
  }
}

/**
 * Load a Sandpack client for an iframe
 */
export async function loadSandpackClient(
  iframe: HTMLIFrameElement,
  sandboxSetup: { files: Record<string, { code: string }>; entry?: string; dependencies?: Record<string, string> },
  options?: { showOpenInCodeSandbox?: boolean }
): Promise<any> {
  if (!SandpackModule) {
    throw new Error('Sandpack not initialized');
  }
  return SandpackModule.loadSandpackClient(iframe, sandboxSetup, options);
}
