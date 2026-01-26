// Test specifications for useId exercise

/*
Expected FormField implementation:

function FormField({ label, type = 'text', hint, value, onChange }) {
  const id = useId();
  const inputId = `${id}-input`;
  const hintId = `${id}-hint`;

  return (
    <div className="form-field">
      <label htmlFor={inputId}>
        {label}
      </label>
      <input
        id={inputId}
        aria-describedby={hint ? hintId : undefined}
        type={type}
        value={value}
        onChange={onChange}
      />
      {hint && (
        <p id={hintId} className="hint">
          {hint}
        </p>
      )}
    </div>
  );
}

Key points:
1. useId() generates a unique base ID like ":r1:"
2. Append suffixes for related elements: `${id}-input`, `${id}-hint`
3. htmlFor on label matches id on input
4. aria-describedby links input to hint for screen readers
5. Each FormField instance gets different IDs automatically
*/
