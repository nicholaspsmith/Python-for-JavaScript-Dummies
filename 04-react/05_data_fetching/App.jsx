import { useState, useEffect } from 'react';
import './styles.css';

// Mock API function - simulates network request
const fetchUser = () => {
  return new Promise((resolve) => {
    setTimeout(() => {
      resolve({
        name: 'John Doe',
        email: 'john@example.com',
        role: 'Developer'
      });
    }, 1000);
  });
};

export default function App() {
  // TODO: Create state for user, loading, and error

  // TODO: Use useEffect to fetch user data on mount

  // TODO: Create a refresh function to refetch data

  return (
    <div className="user-card">
      <h1>User Profile</h1>

      {/* TODO: Show loading state */}

      {/* TODO: Show error state */}

      {/* TODO: Show user data when loaded */}
      <div className="user-info">
        <p><strong>Name:</strong> {/* user name */}</p>
        <p><strong>Email:</strong> {/* user email */}</p>
        <p><strong>Role:</strong> {/* user role */}</p>
      </div>

      {/* TODO: Add refresh button */}
    </div>
  );
}
