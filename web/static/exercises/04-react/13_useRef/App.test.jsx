// Test specifications for useRef exercise

/*
Expected behavior:

1. Input ref:
   - useRef() creates a ref for the input element
   - ref is attached via ref={inputRef}
   - inputRef.current gives access to the DOM node

2. Focus button:
   - Calls inputRef.current.focus()

3. Select All button:
   - Calls inputRef.current.focus()
   - Calls inputRef.current.select()

4. Render count:
   - Uses useRef to store count (not useState!)
   - Increments on each render: renderCount.current++
   - Displays renderCount.current
   - Changing the ref value doesn't cause re-renders
*/
