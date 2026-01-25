import { useState, useEffect } from 'react';
import './styles.css';

// Mock search function
const mockSearch = (query) => {
  const items = ['Apple', 'Banana', 'Cherry', 'Date', 'Elderberry', 'Fig', 'Grape'];
  return items.filter(item =>
    item.toLowerCase().includes(query.toLowerCase())
  );
};

export default function App() {
  // TODO: Create state for query, debouncedQuery, and results

  // TODO: Implement debounce using useEffect
  // When query changes, start a timer
  // If query changes again before 500ms, cancel the timer
  // After 500ms, update debouncedQuery

  // TODO: When debouncedQuery changes, perform the search

  return (
    <div className="search-container">
      <h1>Debounced Search</h1>

      <input
        type="text"
        placeholder="Search fruits..."
        // TODO: Make this a controlled input
      />

      {/* TODO: Show 'Searching...' when query !== debouncedQuery */}

      {/* TODO: Show results count and list */}
      <div className="results">
        <p>Found X results</p>
        <ul>
          {/* Map through results */}
        </ul>
      </div>
    </div>
  );
}
