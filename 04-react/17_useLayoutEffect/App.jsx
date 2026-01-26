import { useState, useRef, useLayoutEffect } from 'react';
import './styles.css';

function Tooltip({ text, targetRef, visible }) {
  const tooltipRef = useRef(null);
  const [position, setPosition] = useState({ top: 0, left: 0 });

  // TODO: Use useLayoutEffect to calculate tooltip position
  // This prevents flicker because it runs before browser paint
  // useLayoutEffect(() => {
  //   if (visible && targetRef.current && tooltipRef.current) {
  //     const targetRect = targetRef.current.getBoundingClientRect();
  //     const tooltipRect = tooltipRef.current.getBoundingClientRect();
  //
  //     // Calculate position: centered above the target
  //     const top = targetRect.top - tooltipRect.height - 8;
  //     const left = targetRect.left + (targetRect.width - tooltipRect.width) / 2;
  //
  //     setPosition({ top, left });
  //   }
  // }, [visible, targetRef]);

  if (!visible) return null;

  return (
    <div
      ref={tooltipRef}
      className="tooltip"
      style={{
        position: 'fixed',
        top: position.top,
        left: position.left,
      }}
    >
      {text}
      <div className="tooltip-arrow" />
    </div>
  );
}

export default function App() {
  const [showTooltip, setShowTooltip] = useState(false);
  const buttonRef = useRef(null);

  return (
    <div className="container">
      <h1>useLayoutEffect Demo</h1>

      <div className="explanation">
        <p><strong>useLayoutEffect vs useEffect:</strong></p>
        <ul>
          <li><code>useEffect</code>: Runs after paint (may cause flicker)</li>
          <li><code>useLayoutEffect</code>: Runs before paint (no flicker)</li>
        </ul>
        <p>For DOM measurements and positioning, use <code>useLayoutEffect</code>!</p>
      </div>

      <div className="demo-area">
        <button
          ref={buttonRef}
          className="tooltip-trigger"
          onMouseEnter={() => setShowTooltip(true)}
          onMouseLeave={() => setShowTooltip(false)}
        >
          Hover over me!
        </button>

        <Tooltip
          text="I'm positioned using useLayoutEffect!"
          targetRef={buttonRef}
          visible={showTooltip}
        />
      </div>

      <div className="comparison">
        <h3>When to use which?</h3>
        <table>
          <thead>
            <tr>
              <th>useEffect</th>
              <th>useLayoutEffect</th>
            </tr>
          </thead>
          <tbody>
            <tr>
              <td>Data fetching</td>
              <td>Measuring DOM elements</td>
            </tr>
            <tr>
              <td>Subscriptions</td>
              <td>Positioning tooltips/popovers</td>
            </tr>
            <tr>
              <td>Event listeners</td>
              <td>Synchronizing with DOM</td>
            </tr>
            <tr>
              <td>Most side effects</td>
              <td>Preventing visual flicker</td>
            </tr>
          </tbody>
        </table>
      </div>
    </div>
  );
}
