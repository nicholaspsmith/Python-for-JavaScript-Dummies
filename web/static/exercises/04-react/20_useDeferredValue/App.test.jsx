// Test specifications for useDeferredValue exercise

/*
Expected implementation:

export default function App() {
  const [query, setQuery] = useState('');
  const deferredQuery = useDeferredValue(query);

  // Check if we're showing stale results
  const isStale = query !== deferredQuery;

  return (
    // ... input uses `query` for controlled value
    // ... SearchResults uses `deferredQuery` for rendering
    // ... show stale indicator when isStale is true
  );
}

Key points:
1. useDeferredValue(value) returns a deferred version of that value
2. During urgent updates, React shows old deferred value
3. Then updates deferred value in background (lower priority)
4. query !== deferredQuery means we're showing stale data
5. Use this to indicate loading/staleness to user
6. Works great with memo() to avoid re-renders with old value

When to use which:
- useTransition: When you control the state update
- useDeferredValue: When value comes from props or external source
*/
