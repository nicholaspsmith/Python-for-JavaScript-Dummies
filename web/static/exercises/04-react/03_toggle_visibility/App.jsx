import { useState } from 'react';
import './styles.css';

export default function App() {
  // TODO: Create state to track visibility (start hidden)

  return (
    <div className="toggle-container">
      <h1>Toggle Visibility</h1>

      {/* TODO: Button that toggles visibility and shows appropriate text */}
      <button>
        {/* Show "Show Content" or "Hide Content" based on state */}
      </button>

      {/* TODO: Conditionally render this message when visible */}
      <div className="content">
        <p>This content can be toggled!</p>
        <p>Now you see me...</p>
      </div>
    </div>
  );
}
