import { Suspense, use } from 'react';
import './styles.css';

// Create a promise for user data
const userPromise = new Promise((resolve) => {
  setTimeout(() => {
    resolve({
      name: 'Jane Doe',
      email: 'jane@example.com',
      avatar: '👩‍💻'
    });
  }, 1500);
});

// TODO: Create UserProfile component that uses the use() hook
// The use() hook reads the promise and suspends until it resolves
function UserProfile() {
  // TODO: Use the use() hook to read userPromise
  // const user = use(userPromise);

  return (
    <div className="profile">
      <div className="avatar">{/* user.avatar */}</div>
      <h2>{/* user.name */}</h2>
      <p>{/* user.email */}</p>
    </div>
  );
}

// Loading fallback component
function LoadingSkeleton() {
  return (
    <div className="profile skeleton">
      <div className="avatar">⏳</div>
      <div className="skeleton-text"></div>
      <div className="skeleton-text short"></div>
    </div>
  );
}

export default function App() {
  return (
    <div className="container">
      <h1>React 19: use() Hook</h1>

      {/* TODO: Wrap UserProfile with Suspense */}
      {/* Use LoadingSkeleton as the fallback */}
      <UserProfile />
    </div>
  );
}
