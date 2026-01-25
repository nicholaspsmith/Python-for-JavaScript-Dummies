import { useState } from 'react';
import './styles.css';

export default function App() {
  // TODO: Use useState to create a count state variable

  return (
    <div className="counter">
      <h1>Counter</h1>
      <p className="count">Count: {/* Display count here */}</p>
      <div className="buttons">
        {/* Add Increment, Decrement, and Reset buttons */}
      </div>
    </div>
  );
}
