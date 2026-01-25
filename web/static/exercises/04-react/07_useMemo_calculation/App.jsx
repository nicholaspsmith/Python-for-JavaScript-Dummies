import { useState, useMemo } from 'react';
import './styles.css';

// Expensive calculation - factorial with artificial delay
const calculateFactorial = (n) => {
  console.log('Calculating factorial...');
  if (n < 0) return 'Invalid';
  if (n > 12) return 'Too large';

  let result = 1;
  for (let i = 2; i <= n; i++) {
    result *= i;
  }
  return result;
};

export default function App() {
  // TODO: Create state for number input and counter

  // TODO: Use useMemo to memoize factorial calculation
  // It should only recalculate when the number changes

  return (
    <div className="memo-demo">
      <h1>useMemo Demo</h1>

      <div className="input-group">
        <label>Number (0-12):</label>
        <input
          type="number"
          min="0"
          max="12"
          // TODO: Make this controlled
        />
      </div>

      <div className="result">
        <p>Factorial: <strong>{/* Show factorial result */}</strong></p>
        <p className="hint">
          (Check console to see when calculation runs)
        </p>
      </div>

      <hr />

      <div className="counter-section">
        <p>Counter: <strong>{/* Show counter */}</strong></p>
        <button>
          Increment Counter
        </button>
        <p className="hint">
          Clicking this shouldn't recalculate the factorial!
        </p>
      </div>
    </div>
  );
}
