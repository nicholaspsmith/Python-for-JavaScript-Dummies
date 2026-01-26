// Test specifications for useCallback exercise

/*
Expected behavior:

1. Without useCallback + memo:
   - Clicking "Update Other State" causes child to re-render
   - handleClick is a new function reference each render

2. With useCallback + memo:
   - const handleClick = useCallback(() => {
       setCount(c => c + 1);
     }, []);
   - Wrap ExpensiveChild with memo()
   - Child only re-renders when its props actually change
   - Clicking "Update Other State" no longer re-renders child

3. Dependencies:
   - Empty [] means function never changes
   - If callback needs external values, add them to deps
   - useCallback(() => {...}, [dependency1, dependency2])
*/
