import { useState } from 'react';
import './styles.css';

export default function App() {
  // TODO: Create state for the input value

  return (
    <div className="controlled-input">
      <h1>Controlled Input</h1>

      {/* TODO: Add controlled input with value and onChange */}
      <input
        type="text"
        placeholder="Type something..."
      />

      <div className="output">
        <p>You typed: <strong>{/* Show value */}</strong></p>
        <p>Character count: <strong>{/* Show length */}</strong></p>
      </div>

      {/* TODO: Add Clear button */}
    </div>
  );
}
