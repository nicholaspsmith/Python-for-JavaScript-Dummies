// Test specifications for useImperativeHandle exercise

/*
Expected FancyInput implementation:

const FancyInput = forwardRef(function FancyInput(props, ref) {
  const inputRef = useRef(null);
  const [value, setValue] = useState('');

  useImperativeHandle(ref, () => ({
    focus: () => {
      inputRef.current?.focus();
    },
    clear: () => {
      setValue('');
    },
    getValue: () => {
      return value;
    },
  }));

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

Key points:
1. forwardRef allows component to receive a ref from parent
2. useImperativeHandle customizes what that ref points to
3. Instead of ref.current = <input DOM node>
   We get ref.current = { focus, clear, getValue }
4. Parent can't do inputRef.current.value (encapsulation!)
5. Great for creating component libraries with controlled APIs
*/
