<script lang="ts">
	import { onMount } from 'svelte';
	import { browser } from '$app/environment';
	import favicon from '$lib/assets/favicon.svg';
	import { theme } from '$lib/stores/theme';
	import { registerPyodideCleanup } from '$lib/stores/pyodide';
	import { cancelPendingSync } from '$lib/stores/progress';
	import { initHints } from '$lib/stores/hints';

	let { children } = $props();

	onMount(() => {
		theme.init();
		initHints();

		// Register cleanup handlers for page unload
		if (browser) {
			registerPyodideCleanup();

			// Clean up progress sync on page unload
			window.addEventListener('beforeunload', () => {
				cancelPendingSync();
			});
		}
	});
</script>

<svelte:head>
	<link rel="icon" href={favicon} />
</svelte:head>

{@render children()}
