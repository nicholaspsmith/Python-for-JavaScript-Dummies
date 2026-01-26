import { useState, useRef } from 'react';
import './styles.css';

export default function App() {
  // TODO: Create a ref for the input element using useRef
  // TODO: Create a ref to track render count (doesn't cause re-renders)

  const [text, setText] = useState('Hello, React!');

  // TODO: Increment render count (hint: do this in the component body, not in useEffect)

  function handleFocus() {
    // TODO: Focus the input using the ref
  }

  function handleSelectAll() {
    // TODO: Focus and select all text in the input
  }

  return (
    <div className="container">
      <h1>useRef Demo</h1>

      <div className="input-group">
        <input
          // TODO: Attach the ref to this input
          type="text"
          value={text}
          onChange={(e) => setText(e.target.value)}
        />
      </div>

      <div className="buttons">
        <button onClick={handleFocus}>Focus Input</button>
        <button onClick={handleSelectAll}>Select All</button>
      </div>

      <p className="render-count">
        {/* TODO: Display the render count */}
        Render count: ???
      </p>

      <p className="hint">
        Notice: The render count persists without causing extra re-renders!
      </p>
    </div>
  );
}
