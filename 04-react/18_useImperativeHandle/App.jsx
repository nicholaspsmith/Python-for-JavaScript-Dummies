import { useRef, useImperativeHandle, forwardRef, useState } from 'react';
import './styles.css';

// TODO: Use forwardRef and useImperativeHandle to create a controlled API
// The parent should NOT have direct access to the input DOM node
// Instead, expose only: focus(), clear(), getValue()
const FancyInput = forwardRef(function FancyInput(props, ref) {
  const inputRef = useRef(null);
  const [value, setValue] = useState('');

  // TODO: Use useImperativeHandle to define the ref API
  // useImperativeHandle(ref, () => ({
  //   focus: () => { ... },
  //   clear: () => { ... },
  //   getValue: () => { ... },
  // }));

  return (
    <div className="fancy-input">
      <input
        ref={inputRef}
        type="text"
        value={value}
        onChange={(e) => setValue(e.target.value)}
        placeholder={props.placeholder}
      />
      <span className="input-icon">✏️</span>
    </div>
  );
});

export default function App() {
  const inputRef = useRef(null);
  const [message, setMessage] = useState('');

  function handleFocus() {
    inputRef.current?.focus();
    setMessage('Input focused!');
  }

  function handleClear() {
    inputRef.current?.clear();
    setMessage('Input cleared!');
  }

  function handleGetValue() {
    const value = inputRef.current?.getValue();
    setMessage(`Current value: "${value || '(empty)'}"`);
  }

  return (
    <div className="container">
      <h1>useImperativeHandle Demo</h1>

      <div className="explanation">
        <p>
          <strong>Why useImperativeHandle?</strong>
        </p>
        <p>
          Instead of exposing the full DOM node, we expose only specific methods.
          This provides better encapsulation and a cleaner API.
        </p>
      </div>

      <div className="demo">
        <FancyInput ref={inputRef} placeholder="Type something..." />

        <div className="buttons">
          <button onClick={handleFocus}>Focus</button>
          <button onClick={handleClear}>Clear</button>
          <button onClick={handleGetValue}>Get Value</button>
        </div>

        {message && <p className="message">{message}</p>}
      </div>

      <div className="api-info">
        <h3>Exposed API:</h3>
        <ul>
          <li><code>focus()</code> - Focuses the input</li>
          <li><code>clear()</code> - Clears the input value</li>
          <li><code>getValue()</code> - Returns current value</li>
        </ul>
        <p className="note">
          The parent cannot access inputRef.current.value directly!
        </p>
      </div>
    </div>
  );
}
