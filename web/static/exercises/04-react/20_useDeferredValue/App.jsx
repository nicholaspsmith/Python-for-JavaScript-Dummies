import { useState, useDeferredValue, useMemo, memo } from 'react';
import './styles.css';

// Expensive list component that we want to defer
const SearchResults = memo(function SearchResults({ query }) {
  // Simulate expensive rendering
  const items = useMemo(() => {
    if (!query) return [];

    // Generate items that match query (simulating a search)
    const results = [];
    for (let i = 0; i < 500; i++) {
      // Artificial slowdown
      const start = performance.now();
      while (performance.now() - start < 0.1) {}

      if (i % 3 === 0 || query.length > 2) {
        results.push({
          id: i,
          title: `Result ${i + 1}: "${query}" match`,
          snippet: `This item contains the search term "${query}" and was found at index ${i}.`,
        });
      }
    }
    return results;
  }, [query]);

  if (!query) {
    return <div className="empty">Type to search...</div>;
  }

  return (
    <div className="results">
      <div className="result-count">{items.length} results found</div>
      {items.slice(0, 50).map((item) => (
        <div key={item.id} className="result-item">
          <h3>{item.title}</h3>
          <p>{item.snippet}</p>
        </div>
      ))}
    </div>
  );
});

export default function App() {
  const [query, setQuery] = useState('');

  // TODO: Create a deferred version of the query
  // const deferredQuery = useDeferredValue(query);

  // Without useDeferredValue (blocking)
  const deferredQuery = query;

  // Check if we're showing stale results
  const isStale = query !== deferredQuery;

  return (
    <div className="container">
      <h1>useDeferredValue Demo</h1>

      <div className="explanation">
        <p>
          <strong>useDeferredValue</strong> defers updating expensive UI.
        </p>
        <p>
          Type quickly in the search box. Without deferring, the input lags.
          With <code>useDeferredValue</code>, the input stays responsive while
          results update in the background.
        </p>
      </div>

      <div className="search-container">
        <input
          type="text"
          value={query}
          onChange={(e) => setQuery(e.target.value)}
          placeholder="Search..."
          className="search-input"
        />

        <div className={`results-container ${isStale ? 'stale' : ''}`}>
          {isStale && <div className="stale-indicator">Updating...</div>}
          <SearchResults query={deferredQuery} />
        </div>
      </div>

      <div className="comparison">
        <h3>useTransition vs useDeferredValue</h3>
        <table>
          <thead>
            <tr>
              <th>useTransition</th>
              <th>useDeferredValue</th>
            </tr>
          </thead>
          <tbody>
            <tr>
              <td>Wraps state updates</td>
              <td>Wraps values</td>
            </tr>
            <tr>
              <td>You control when to defer</td>
              <td>Value defers automatically</td>
            </tr>
            <tr>
              <td>Good for your own state</td>
              <td>Good for props from parent</td>
            </tr>
          </tbody>
        </table>
      </div>
    </div>
  );
}
