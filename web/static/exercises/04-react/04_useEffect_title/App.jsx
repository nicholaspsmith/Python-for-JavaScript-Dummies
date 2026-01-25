import { useState, useEffect } from 'react';
import './styles.css';

export default function App() {
  // TODO: Create count state

  // TODO: Use useEffect to update document.title when count changes
  // The title should be 'Count: X' where X is the current count

  return (
    <div className="title-counter">
      <h1>Document Title Counter</h1>
      <p className="instruction">Watch the browser tab title change!</p>

      <p className="count">Count: {/* Display count */}</p>

      <div className="buttons">
        {/* Add increment and decrement buttons */}
      </div>
    </div>
  );
}
