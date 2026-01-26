// Test specifications for useLayoutEffect exercise

/*
Expected Tooltip implementation:

function Tooltip({ text, targetRef, visible }) {
  const tooltipRef = useRef(null);
  const [position, setPosition] = useState({ top: 0, left: 0 });

  useLayoutEffect(() => {
    if (visible && targetRef.current && tooltipRef.current) {
      const targetRect = targetRef.current.getBoundingClientRect();
      const tooltipRect = tooltipRef.current.getBoundingClientRect();

      // Position centered above the target
      const top = targetRect.top - tooltipRect.height - 8;
      const left = targetRect.left + (targetRect.width - tooltipRect.width) / 2;

      setPosition({ top, left });
    }
  }, [visible, targetRef]);

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

Key points:
1. useLayoutEffect runs synchronously after DOM mutations
2. Runs BEFORE browser paint - user never sees wrong position
3. useEffect would cause flicker (paint -> measure -> paint again)
4. Use for: measurements, scroll position, animations
*/
