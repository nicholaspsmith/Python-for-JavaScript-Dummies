<script lang="ts">
  import { theme } from '$lib/stores/theme';
  import { onMount } from 'svelte';

  let scrollContainer: HTMLElement;
  let showBackToTop = false;

  onMount(() => {
    const handleScroll = () => {
      showBackToTop = scrollContainer.scrollTop > 300;
    };

    scrollContainer.addEventListener('scroll', handleScroll);
    return () => scrollContainer.removeEventListener('scroll', handleScroll);
  });

  function scrollToTop() {
    scrollContainer.scrollTo({ top: 0, behavior: 'smooth' });
  }

  const sections = [
    {
      title: "Variables",
      items: [
        { js: "const x = 5;", py: "x = 5", note: "No const/let/var needed" },
        { js: "let y = 10;", py: "y = 10", note: "Variables are mutable by default" },
        { js: "const arr = [1, 2, 3];", py: "arr = [1, 2, 3]", note: "Lists are always mutable" },
      ]
    },
    {
      title: "Data Types",
      items: [
        { js: "true / false", py: "True / False", note: "Capital first letter" },
        { js: "null", py: "None", note: "" },
        { js: "undefined", py: "None", note: "Python has only None" },
        { js: "'string' or \"string\"", py: "'string' or \"string\"", note: "Same! Also '''multiline'''" },
        { js: "[1, 2, 3]", py: "[1, 2, 3]", note: "Arrays → Lists" },
        { js: "{ key: 'value' }", py: "{ 'key': 'value' }", note: "Objects → Dicts (keys need quotes)" },
        { js: "new Set([1, 2, 3])", py: "{1, 2, 3} or set([1, 2, 3])", note: "" },
        { js: "new Map()", py: "dict() or {}", note: "" },
      ]
    },
    {
      title: "Operators",
      items: [
        { js: "===", py: "==", note: "No triple equals in Python" },
        { js: "!==", py: "!=", note: "" },
        { js: "&&", py: "and", note: "" },
        { js: "||", py: "or", note: "" },
        { js: "!value", py: "not value", note: "" },
        { js: "a ?? b", py: "a if a is not None else b", note: "Nullish coalescing" },
        { js: "cond ? a : b", py: "a if cond else b", note: "Ternary operator" },
        { js: "x++", py: "x += 1", note: "No ++ or -- operators" },
        { js: "x--", py: "x -= 1", note: "" },
        { js: "**", py: "**", note: "Same! Exponentiation" },
        { js: "//", py: "# (comment) or // (floor div)", note: "// is floor division in Python" },
      ]
    },
    {
      title: "Loops",
      items: [
        { js: "for (let i = 0; i < 5; i++)", py: "for i in range(5):", note: "" },
        { js: "for (let i = 1; i < 10; i++)", py: "for i in range(1, 10):", note: "Start at 1" },
        { js: "for (let i = 0; i < 10; i += 2)", py: "for i in range(0, 10, 2):", note: "Step by 2" },
        { js: "for (let i = 10; i > 0; i--)", py: "for i in range(10, 0, -1):", note: "Count down" },
        { js: "for (const item of arr)", py: "for item in arr:", note: "" },
        { js: "for (const [i, item] of arr.entries())", py: "for i, item in enumerate(arr):", note: "" },
        { js: "for (const key in obj)", py: "for key in obj:", note: "" },
        { js: "for (const [k, v] of Object.entries(obj))", py: "for k, v in obj.items():", note: "" },
        { js: "while (condition)", py: "while condition:", note: "No parentheses needed" },
        { js: "arr.forEach(x => console.log(x))", py: `for x in arr:\n    print(x)`, note: "" },
      ]
    },
    {
      title: "Functions",
      items: [
        { js: "function add(a, b) { return a + b; }", py: `def add(a, b):\n    return a + b`, note: "" },
        { js: "const add = (a, b) => a + b;", py: "add = lambda a, b: a + b", note: "Arrow → Lambda" },
        { js: "function greet(name = 'World')", py: "def greet(name='World'):", note: "Default params" },
        { js: "function sum(...nums)", py: "def sum(*nums):", note: "Rest params → *args" },
        { js: "function config({a, b})", py: "def config(**kwargs):", note: "Destructuring → **kwargs" },
        { js: "async function fetch()", py: "async def fetch():", note: "" },
        { js: "await promise", py: "await coroutine", note: "" },
      ]
    },
    {
      title: "Conditionals",
      items: [
        { js: "if (x > 5) { ... }", py: `if x > 5:\n    ...`, note: "No parentheses, use colon" },
        { js: "} else if (x > 3) {", py: "elif x > 3:", note: "elif, not else if" },
        { js: "} else {", py: "else:", note: "" },
        { js: "switch (x) { case 1: ... }", py: `match x:\n    case 1: ...`, note: "Python 3.10+ match" },
      ]
    },
    {
      title: "Arrays → Lists",
      items: [
        { js: "arr.length", py: "len(arr)", note: "" },
        { js: "arr.push(x)", py: "arr.append(x)", note: "" },
        { js: "arr.pop()", py: "arr.pop()", note: "Same!" },
        { js: "arr.shift()", py: "arr.pop(0)", note: "Pop from front" },
        { js: "arr.unshift(x)", py: "arr.insert(0, x)", note: "Insert at front" },
        { js: "arr.slice(1, 3)", py: "arr[1:3]", note: "Slicing syntax" },
        { js: "arr.slice(1)", py: "arr[1:]", note: "From index to end" },
        { js: "arr.slice(-2)", py: "arr[-2:]", note: "Last 2 elements" },
        { js: "arr.splice(i, 1)", py: "del arr[i] or arr.pop(i)", note: "Remove at index" },
        { js: "arr.concat(other)", py: "arr + other", note: "Or arr.extend(other)" },
        { js: "arr.indexOf(x)", py: "arr.index(x)", note: "Raises ValueError if not found" },
        { js: "arr.includes(x)", py: "x in arr", note: "" },
        { js: "arr.find(x => x > 5)", py: "next((x for x in arr if x > 5), None)", note: "" },
        { js: "arr.findIndex(x => x > 5)", py: "next((i for i, x in enumerate(arr) if x > 5), -1)", note: "" },
        { js: "arr.filter(x => x > 5)", py: "[x for x in arr if x > 5]", note: "List comprehension" },
        { js: "arr.map(x => x * 2)", py: "[x * 2 for x in arr]", note: "List comprehension" },
        { js: "arr.reduce((a, b) => a + b, 0)", py: "sum(arr)", note: "Or functools.reduce()" },
        { js: "arr.some(x => x > 5)", py: "any(x > 5 for x in arr)", note: "" },
        { js: "arr.every(x => x > 5)", py: "all(x > 5 for x in arr)", note: "" },
        { js: "arr.sort()", py: "arr.sort() or sorted(arr)", note: "sort() mutates, sorted() returns new" },
        { js: "arr.sort((a, b) => a - b)", py: "arr.sort() or sorted(arr)", note: "Numbers sort correctly by default" },
        { js: "arr.sort((a, b) => a.localeCompare(b))", py: "arr.sort() or sorted(arr)", note: "Strings sort correctly by default" },
        { js: "arr.reverse()", py: "arr.reverse() or arr[::-1]", note: "reverse() mutates" },
        { js: "arr.join(', ')", py: "', '.join(arr)", note: "Separator comes first" },
        { js: "[...arr]", py: "arr.copy() or arr[:]", note: "Shallow copy" },
        { js: "[...arr1, ...arr2]", py: "[*arr1, *arr2]", note: "Spread → Unpack" },
      ]
    },
    {
      title: "Strings",
      items: [
        { js: "str.length", py: "len(str)", note: "" },
        { js: "str.charAt(i)", py: "str[i]", note: "" },
        { js: "str.substring(1, 3)", py: "str[1:3]", note: "" },
        { js: "str.slice(1)", py: "str[1:]", note: "" },
        { js: "str.split(',')", py: "str.split(',')", note: "Same!" },
        { js: "str.trim()", py: "str.strip()", note: "" },
        { js: "str.trimStart()", py: "str.lstrip()", note: "" },
        { js: "str.trimEnd()", py: "str.rstrip()", note: "" },
        { js: "str.toLowerCase()", py: "str.lower()", note: "" },
        { js: "str.toUpperCase()", py: "str.upper()", note: "" },
        { js: "str.startsWith('a')", py: "str.startswith('a')", note: "Lowercase 'w'" },
        { js: "str.endsWith('z')", py: "str.endswith('z')", note: "Lowercase 'w'" },
        { js: "str.includes('x')", py: "'x' in str", note: "" },
        { js: "str.indexOf('x')", py: "str.find('x')", note: "Returns -1 if not found" },
        { js: "str.replace('a', 'b')", py: "str.replace('a', 'b')", note: "Same!" },
        { js: "str.replaceAll('a', 'b')", py: "str.replace('a', 'b')", note: "Python replaces all by default" },
        { js: "`Hello ${name}`", py: "f'Hello {name}'", note: "Template literals → f-strings" },
        { js: "str.repeat(3)", py: "str * 3", note: "" },
        { js: "str.padStart(5, '0')", py: "str.zfill(5) or str.rjust(5, '0')", note: "" },
      ]
    },
    {
      title: "Objects → Dicts",
      items: [
        { js: "{ key: 'value' }", py: "{ 'key': 'value' }", note: "Keys need quotes" },
        { js: "obj.key", py: "obj['key'] or obj.get('key')", note: "get() returns None if missing" },
        { js: "obj.key = 'new'", py: "obj['key'] = 'new'", note: "" },
        { js: "delete obj.key", py: "del obj['key']", note: "" },
        { js: "'key' in obj", py: "'key' in obj", note: "Same!" },
        { js: "Object.keys(obj)", py: "obj.keys() or list(obj.keys())", note: "" },
        { js: "Object.values(obj)", py: "obj.values() or list(obj.values())", note: "" },
        { js: "Object.entries(obj)", py: "obj.items()", note: "" },
        { js: "{ ...obj1, ...obj2 }", py: "{ **obj1, **obj2 }", note: "Spread → Unpack" },
        { js: "const { a, b } = obj", py: "a, b = obj['a'], obj['b']", note: "No destructuring shorthand" },
      ]
    },
    {
      title: "Math",
      items: [
        { js: "Math.floor(x)", py: "int(x) or x // 1", note: "// is floor division" },
        { js: "Math.ceil(x)", py: "math.ceil(x)", note: "import math" },
        { js: "Math.round(x)", py: "round(x)", note: "" },
        { js: "Math.abs(x)", py: "abs(x)", note: "" },
        { js: "Math.max(a, b, c)", py: "max(a, b, c)", note: "" },
        { js: "Math.min(a, b, c)", py: "min(a, b, c)", note: "" },
        { js: "Math.pow(x, y)", py: "x ** y", note: "" },
        { js: "Math.sqrt(x)", py: "x ** 0.5 or math.sqrt(x)", note: "" },
        { js: "Math.random()", py: "random.random()", note: "import random" },
        { js: "Math.floor(Math.random() * 10)", py: "random.randint(0, 9)", note: "" },
        { js: "parseInt('42')", py: "int('42')", note: "" },
        { js: "parseFloat('3.14')", py: "float('3.14')", note: "" },
        { js: "Number.isInteger(x)", py: "isinstance(x, int)", note: "" },
        { js: "Number.isNaN(x)", py: "math.isnan(x)", note: "" },
        { js: "Infinity", py: "float('inf')", note: "" },
      ]
    },
    {
      title: "Type Checking",
      items: [
        { js: "typeof x === 'string'", py: "isinstance(x, str)", note: "" },
        { js: "typeof x === 'number'", py: "isinstance(x, (int, float))", note: "" },
        { js: "typeof x === 'boolean'", py: "isinstance(x, bool)", note: "" },
        { js: "typeof x === 'object'", py: "isinstance(x, dict)", note: "Or list, etc." },
        { js: "typeof x === 'function'", py: "callable(x)", note: "" },
        { js: "Array.isArray(x)", py: "isinstance(x, list)", note: "" },
        { js: "x instanceof Date", py: "isinstance(x, datetime)", note: "from datetime import datetime" },
      ]
    },
    {
      title: "Error Handling",
      items: [
        { js: "try { ... } catch (e) { ... }", py: `try:\n    ...\nexcept Exception as e:\n    ...`, note: "" },
        { js: "throw new Error('msg')", py: "raise Exception('msg')", note: "" },
        { js: "finally { ... }", py: `finally:\n    ...`, note: "Same concept" },
      ]
    },
    {
      title: "Classes",
      items: [
        { js: "class Dog { }", py: "class Dog:", note: "" },
        { js: "constructor(name) { this.name = name; }", py: `def __init__(self, name):\n    self.name = name`, note: "" },
        { js: "this.name", py: "self.name", note: "Explicit self" },
        { js: "class Dog extends Animal", py: "class Dog(Animal):", note: "" },
        { js: "super()", py: "super().__init__()", note: "" },
        { js: "static method() { }", py: `@staticmethod\ndef method():`, note: "" },
        { js: "get name() { return this._name; }", py: `@property\ndef name(self):`, note: "" },
      ]
    },
    {
      title: "Common Patterns",
      items: [
        { js: "arr.length === 0", py: "len(arr) == 0 or not arr", note: "Empty check" },
        { js: "str === ''", py: "str == '' or not str", note: "Empty string check" },
        { js: "x === null || x === undefined", py: "x is None", note: "" },
        { js: "x !== null && x !== undefined", py: "x is not None", note: "" },
        { js: "Math.max(...arr)", py: "max(arr)", note: "No spread needed" },
        { js: "Math.min(...arr)", py: "min(arr)", note: "" },
        { js: "arr.flat()", py: "[x for sub in arr for x in sub]", note: "Flatten one level" },
        { js: "[...new Set(arr)]", py: "list(set(arr))", note: "Remove duplicates" },
        { js: "Object.assign({}, obj)", py: "obj.copy() or dict(obj)", note: "Shallow copy" },
        { js: "JSON.stringify(obj)", py: "json.dumps(obj)", note: "import json" },
        { js: "JSON.parse(str)", py: "json.loads(str)", note: "import json" },
      ]
    },
  ];
</script>

<svelte:head>
  <title>JS to Python Cheatsheet</title>
</svelte:head>

<div class="cheatsheet" bind:this={scrollContainer}>
  <div class="back-bar">
    <a href="/" class="back-link">← Back to Exercises</a>
    <button class="theme-toggle" on:click={() => theme.toggle()} aria-label="Toggle theme">
      {#if $theme === 'dark'}
        <svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2">
          <circle cx="12" cy="12" r="5"/>
          <line x1="12" y1="1" x2="12" y2="3"/>
          <line x1="12" y1="21" x2="12" y2="23"/>
          <line x1="4.22" y1="4.22" x2="5.64" y2="5.64"/>
          <line x1="18.36" y1="18.36" x2="19.78" y2="19.78"/>
          <line x1="1" y1="12" x2="3" y2="12"/>
          <line x1="21" y1="12" x2="23" y2="12"/>
          <line x1="4.22" y1="19.78" x2="5.64" y2="18.36"/>
          <line x1="18.36" y1="5.64" x2="19.78" y2="4.22"/>
        </svg>
      {:else}
        <svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2">
          <path d="M21 12.79A9 9 0 1 1 11.21 3 7 7 0 0 0 21 12.79z"/>
        </svg>
      {/if}
    </button>
  </div>

  <header>
    <h1>JavaScript → Python Cheatsheet</h1>
    <p class="subtitle">Quick reference for JS developers learning Python</p>
  </header>

  <nav class="toc">
    <h2>Contents</h2>
    <ul>
      {#each sections as section}
        <li><a href="#{section.title.toLowerCase().replace(/[→\s]/g, '-')}">{section.title}</a></li>
      {/each}
    </ul>
  </nav>

  <main>
    {#each sections as section}
      <section id={section.title.toLowerCase().replace(/[→\s]/g, '-')}>
        <h2>{section.title}</h2>
        <div class="table-wrapper">
          <table>
            <thead>
              <tr>
                <th>JavaScript</th>
                <th>Python</th>
                <th>Notes</th>
              </tr>
            </thead>
            <tbody>
              {#each section.items as item}
                <tr>
                  <td><code>{item.js}</code></td>
                  <td><code>{item.py}</code></td>
                  <td>{item.note}</td>
                </tr>
              {/each}
            </tbody>
          </table>
        </div>
      </section>
    {/each}
  </main>

  {#if showBackToTop}
    <button class="back-to-top" on:click={scrollToTop} aria-label="Back to top">
      <svg width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2">
        <path d="M18 15l-6-6-6 6"/>
      </svg>
    </button>
  {/if}
</div>

<style>
  :global(body) {
    overflow: hidden;
  }

  .cheatsheet {
    max-width: 1200px;
    margin: 0 auto;
    padding: 2rem;
    color: var(--text-primary);
    height: 100vh;
    overflow-y: auto;
    scroll-behavior: smooth;
  }

  .back-bar {
    position: sticky;
    top: -2rem;
    background: var(--bg-primary);
    z-index: 10;
    padding: 0.75rem 2rem;
    margin: -2rem -2rem 1rem -2rem;
    border-bottom: 1px solid var(--border-color);
    display: flex;
    align-items: center;
    justify-content: space-between;
  }

  .back-link {
    display: inline-flex;
    align-items: center;
    gap: 0.5rem;
    padding: 0.5rem 1rem;
    background: var(--bg-secondary);
    border: 1px solid var(--border-color);
    border-radius: 6px;
    color: var(--text-secondary);
    text-decoration: none;
    font-weight: 500;
    transition: all 0.15s;
  }

  .back-link:hover {
    background: var(--bg-tertiary);
    color: var(--text-primary);
    border-color: var(--text-tertiary);
  }

  .theme-toggle {
    display: flex;
    align-items: center;
    justify-content: center;
    width: 36px;
    height: 36px;
    background: var(--bg-secondary);
    border: 1px solid var(--border-color);
    border-radius: 6px;
    color: var(--text-secondary);
    cursor: pointer;
    transition: all 0.15s;
  }

  .theme-toggle:hover {
    background: var(--bg-tertiary);
    color: var(--text-primary);
    border-color: var(--text-tertiary);
  }

  header {
    text-align: center;
    margin-top: 50px;
    margin-bottom: 2rem;
    padding-bottom: 2rem;
    border-bottom: 1px solid var(--border-color);
  }

  h1 {
    font-size: 2.5rem;
    margin: 0 0 0.5rem 0;
    background: linear-gradient(135deg, #f7df1e 0%, #3776ab 100%);
    -webkit-background-clip: text;
    -webkit-text-fill-color: transparent;
    background-clip: text;
  }

  .subtitle {
    color: var(--text-secondary);
    font-size: 1.125rem;
    margin: 0;
  }

  .toc {
    position: sticky;
    top: 1.8rem;
    background: var(--bg-secondary);
    border-radius: 8px;
    padding: 1rem 1.5rem;
    margin: -2rem -2rem 1rem -2rem;
    padding-left: 2rem;
  }

  .toc h2 {
    margin: 0 0 1rem 0;
    font-size: 1rem;
    color: var(--text-secondary);
  }

  .toc ul {
    display: flex;
    flex-wrap: wrap;
    gap: 0.5rem 1rem;
    margin: 0;
    padding: 0;
    list-style: none;
  }

  .toc a {
    color: #60a5fa;
    text-decoration: none;
    font-size: 0.875rem;
  }

  .toc a:hover {
    text-decoration: underline;
  }

  section {
    margin-bottom: 3rem;
    scroll-margin-top: 11.25rem;
  }

  section h2 {
    font-size: 1.5rem;
    margin: 0 0 1rem 0;
    padding-bottom: 0.5rem;
    border-bottom: 2px solid var(--border-color);
  }

  .table-wrapper {
    overflow-x: auto;
  }

  table {
    width: 100%;
    border-collapse: collapse;
    font-size: 0.875rem;
  }

  th, td {
    padding: 0.75rem;
    text-align: left;
    border-bottom: 1px solid var(--border-color);
  }

  th {
    background: var(--bg-tertiary);
    font-weight: 600;
    color: var(--text-secondary);
  }

  th:first-child {
    color: #f7df1e;
  }

  th:nth-child(2) {
    color: #3776ab;
  }

  td:first-child code {
    color: #fbbf24;
  }

  td:nth-child(2) code {
    color: #60a5fa;
  }

  /* Light mode overrides for JavaScript colors */
  :global([data-theme="light"]) th:first-child {
    color: #459900;
  }

  :global([data-theme="light"]) td:first-child code {
    color: #62a63c;
  }

  td:last-child {
    color: var(--text-tertiary);
    font-size: 0.8125rem;
  }

  code {
    font-family: 'JetBrains Mono', monospace;
    font-size: 0.8125rem;
    white-space: pre-wrap;
  }

  tr:hover {
    background: var(--bg-secondary);
  }

  .back-to-top {
    position: fixed;
    bottom: 2rem;
    right: 2rem;
    width: 44px;
    height: 44px;
    display: flex;
    align-items: center;
    justify-content: center;
    background: var(--bg-secondary);
    border: 1px solid var(--border-color);
    border-radius: 50%;
    color: var(--text-secondary);
    cursor: pointer;
    transition: all 0.15s;
    box-shadow: 0 2px 8px rgba(0, 0, 0, 0.3);
    z-index: 20;
  }

  .back-to-top:hover {
    background: var(--bg-tertiary);
    color: var(--text-primary);
    border-color: var(--text-tertiary);
    transform: translateY(-2px);
  }

  @media (max-width: 768px) {
    .cheatsheet {
      padding: 1rem;
    }

    h1 {
      font-size: 1.75rem;
    }

    .toc ul {
      flex-direction: column;
    }

    th, td {
      padding: 0.5rem;
    }

    td:last-child {
      display: none;
    }
  }
</style>
