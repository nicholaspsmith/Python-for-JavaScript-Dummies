// Test specifications for useTransition exercise

/*
Expected implementation:

export default function App() {
  const [query, setQuery] = useState('');
  const [filterQuery, setFilterQuery] = useState('');
  const [isPending, startTransition] = useTransition();

  const filteredItems = useMemo(
    () => filterItems(allItems, filterQuery),
    [filterQuery]
  );

  function handleSearch(e) {
    const value = e.target.value;
    setQuery(value); // Urgent: update input immediately

    // Non-urgent: can be interrupted
    startTransition(() => {
      setFilterQuery(value);
    });
  }

  // ... rest of component uses isPending to show loading state
}

Key points:
1. useTransition returns [isPending, startTransition]
2. Wrap non-urgent updates in startTransition()
3. Urgent updates (like typing) happen immediately
4. Non-urgent updates can be interrupted
5. isPending is true while transition is in progress
6. Use isPending to show loading indicators
7. Great for expensive renders, filters, tabs, navigation
*/
