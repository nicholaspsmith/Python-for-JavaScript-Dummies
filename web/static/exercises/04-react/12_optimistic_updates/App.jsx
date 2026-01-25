import { useState, useOptimistic, useTransition } from 'react';
import './styles.css';

// Simulated server request - randomly fails 30% of the time
async function likePost(currentLikes) {
  await new Promise(resolve => setTimeout(resolve, 1000));

  // Randomly fail to demonstrate rollback
  if (Math.random() < 0.3) {
    throw new Error('Failed to like post');
  }

  return currentLikes + 1;
}

export default function App() {
  const [likes, setLikes] = useState(42);
  const [error, setError] = useState(null);

  // TODO: Use useOptimistic to create optimistic state
  // const [optimisticLikes, addOptimisticLike] = useOptimistic(
  //   likes,
  //   (currentLikes, newLike) => currentLikes + newLike
  // );

  // TODO: Use useTransition to track pending state
  // const [isPending, startTransition] = useTransition();

  async function handleLike() {
    setError(null);

    // TODO: Start transition and add optimistic update
    // startTransition(async () => {
    //   addOptimisticLike(1);
    //   try {
    //     const newLikes = await likePost(likes);
    //     setLikes(newLikes);
    //   } catch (e) {
    //     setError(e.message);
    //   }
    // });
  }

  return (
    <div className="post">
      <h1>Optimistic Updates Demo</h1>

      <div className="card">
        <div className="content">
          <h2>Check out this cool React 19 feature!</h2>
          <p>useOptimistic provides instant feedback while waiting for server confirmation.</p>
        </div>

        <div className="actions">
          <button
            className={`like-button`}
            onClick={handleLike}
            // TODO: Disable when pending
          >
            <span className="heart">❤️</span>
            <span className="count">{/* Show optimisticLikes */}42</span>
            {/* TODO: Show spinner when pending */}
          </button>
        </div>

        {/* TODO: Show error message if error exists */}
      </div>

      <p className="hint">
        Try clicking multiple times! ~30% of requests will fail to demonstrate rollback.
      </p>
    </div>
  );
}
