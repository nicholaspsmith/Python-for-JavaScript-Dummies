import { useState, useEffect } from 'react';
import './styles.css';

// TODO: Create useLocalStorage custom hook
// function useLocalStorage(key, initialValue) {
//   1. Initialize state from localStorage (if exists) or initialValue
//   2. Use useEffect to sync state changes to localStorage
//   3. Return [value, setValue]
// }

export default function App() {
  // TODO: Use useLocalStorage for name and color preferences
  // Example: const [name, setName] = useLocalStorage('name', '');
  // Example: const [color, setColor] = useLocalStorage('favoriteColor', '#3b82f6');

  return (
    <div className="preferences">
      <h1>User Preferences</h1>
      <p className="subtitle">Your preferences are saved to localStorage!</p>

      <div className="form-group">
        <label>Your Name:</label>
        <input
          type="text"
          placeholder="Enter your name"
          // TODO: Make controlled with useLocalStorage value
        />
      </div>

      <div className="form-group">
        <label>Favorite Color:</label>
        <input
          type="color"
          // TODO: Make controlled with useLocalStorage value
        />
      </div>

      <div className="preview" style={{ /* Apply selected color */ }}>
        <p>Hello, {/* Show name or 'Guest' */}!</p>
        <p>Your favorite color is displayed above.</p>
      </div>

      <p className="hint">
        Try refreshing the page - your preferences will persist!
      </p>
    </div>
  );
}
