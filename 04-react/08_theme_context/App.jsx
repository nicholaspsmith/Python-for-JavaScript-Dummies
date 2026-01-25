import { createContext, useContext, useState } from 'react';
import './styles.css';

// TODO: Create ThemeContext with createContext
// Default value should include theme and toggleTheme

// TODO: Create ThemeProvider component
// It should manage theme state ('light' or 'dark')
// and provide theme value + toggleTheme function

// TODO: Create useTheme hook that uses useContext

// A card component that uses the theme
function Card() {
  // TODO: Use the useTheme hook to get theme and toggleTheme

  return (
    <div className={`card`}>
      <h2>Themed Card</h2>
      <p>Current theme: {/* show theme */}</p>
      <button>
        Toggle Theme
      </button>
    </div>
  );
}

export default function App() {
  return (
    // TODO: Wrap with ThemeProvider
    <div className="app">
      <h1>Theme Context Demo</h1>
      <Card />
    </div>
  );
}
