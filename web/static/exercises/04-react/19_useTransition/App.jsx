import { useState, useTransition, useMemo } from 'react';
import './styles.css';

// Generate a large list of items
const allItems = Array.from({ length: 5000 }, (_, i) => ({
  id: i,
  name: `Item ${i + 1}`,
  category: ['Electronics', 'Clothing', 'Books', 'Home', 'Sports'][i % 5],
}));

// Simulate expensive filtering with artificial delay
function filterItems(items, query) {
  if (!query) return items;

  // Simulate expensive computation
  const start = performance.now();
  while (performance.now() - start < 1) {
    // Artificial delay to make filtering "expensive"
  }

  return items.filter(
    (item) =>
      item.name.toLowerCase().includes(query.toLowerCase()) ||
      item.category.toLowerCase().includes(query.toLowerCase())
  );
}

export default function App() {
  const [query, setQuery] = useState('');
  const [filterQuery, setFilterQuery] = useState('');

  // TODO: Use useTransition to make filtering non-blocking
  // const [isPending, startTransition] = useTransition();

  // For now, isPending is always false (no transition)
  const isPending = false;

  const filteredItems = useMemo(
    () => filterItems(allItems, filterQuery),
    [filterQuery]
  );

  function handleSearch(e) {
    const value = e.target.value;
    setQuery(value); // Urgent: update input immediately

    // TODO: Wrap the filter update in startTransition
    // This makes it non-urgent, keeping the input responsive
    // startTransition(() => {
    //   setFilterQuery(value);
    // });

    // Without transition (blocking):
    setFilterQuery(value);
  }

  return (
    <div className="container">
      <h1>useTransition Demo</h1>

      <div className="explanation">
        <p>
          <strong>Problem:</strong> Filtering 5000 items blocks the UI.
          Try typing quickly - the input feels sluggish!
        </p>
        <p>
          <strong>Solution:</strong> Use <code>useTransition</code> to mark
          filtering as non-urgent. The input stays responsive!
        </p>
      </div>

      <div className="search-box">
        <input
          type="text"
          value={query}
          onChange={handleSearch}
          placeholder="Search items..."
          className={isPending ? 'pending' : ''}
        />
        {isPending && <span className="loading">Updating...</span>}
      </div>

      <div className="stats">
        Showing {filteredItems.length} of {allItems.length} items
      </div>

      <div className={`list ${isPending ? 'stale' : ''}`}>
        {filteredItems.slice(0, 100).map((item) => (
          <div key={item.id} className="list-item">
            <span className="item-name">{item.name}</span>
            <span className="item-category">{item.category}</span>
          </div>
        ))}
        {filteredItems.length > 100 && (
          <div className="more">
            ... and {filteredItems.length - 100} more items
          </div>
        )}
      </div>
    </div>
  );
}
