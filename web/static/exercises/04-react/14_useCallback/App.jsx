import { useState, useCallback, memo, useRef } from 'react';
import './styles.css';

// TODO: Wrap this component with memo() to prevent unnecessary re-renders
function ExpensiveChild({ onClick, label }) {
  const renderCount = useRef(0);
  renderCount.current++;

  return (
    <div className="child">
      <h3>{label}</h3>
      <p>Child render count: {renderCount.current}</p>
      <button onClick={onClick}>Click me</button>
    </div>
  );
}

export default function App() {
  const [count, setCount] = useState(0);
  const [otherState, setOtherState] = useState(0);
  const parentRenderCount = useRef(0);
  parentRenderCount.current++;

  // This function is recreated on every render!
  // TODO: Wrap with useCallback to memoize it
  const handleClick = () => {
    setCount(c => c + 1);
  };

  return (
    <div className="container">
      <h1>useCallback Demo</h1>

      <div className="parent-info">
        <p>Parent render count: {parentRenderCount.current}</p>
        <p>Count: {count}</p>
      </div>

      <div className="controls">
        <button onClick={() => setOtherState(s => s + 1)}>
          Update Other State ({otherState})
        </button>
      </div>

      <div className="children">
        <ExpensiveChild
          onClick={handleClick}
          label="Child Component"
        />
      </div>

      <div className="explanation">
        <p><strong>Problem:</strong> Click "Update Other State" - the child re-renders even though its props didn't meaningfully change!</p>
        <p><strong>Solution:</strong> Use useCallback + memo to prevent this.</p>
      </div>
    </div>
  );
}
