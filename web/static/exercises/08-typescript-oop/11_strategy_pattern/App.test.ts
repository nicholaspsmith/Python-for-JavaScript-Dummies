// Test specifications for Strategy Pattern exercise

/*
Expected behavior:

1. TextStrategy interface:
   - Single method: process(text: string): string

2. Strategy implementations:
   - UpperCaseStrategy.process('Hello') === 'HELLO'
   - LowerCaseStrategy.process('Hello') === 'hello'
   - TitleCaseStrategy.process('hello world') === 'Hello World'
   - SlugStrategy.process('Hello World') === 'hello-world'
   - ReverseStrategy.process('Hello') === 'olleH'

3. TextProcessor (Context):
   - Delegates to the current strategy
   - setStrategy() changes the algorithm at runtime
   - Same interface regardless of strategy

4. Strategy Pattern Benefits:
   - Easy to add new strategies
   - Strategies are interchangeable at runtime
   - Context (TextProcessor) doesn't know strategy details
   - Each strategy is independently testable
*/
