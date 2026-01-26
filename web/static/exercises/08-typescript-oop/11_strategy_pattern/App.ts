// Strategy Pattern
// Define a family of algorithms, encapsulate each one, and make them interchangeable

// TODO: Create TextStrategy interface
// - process(text: string): string

// TODO: Create UpperCaseStrategy implementing TextStrategy
// - process returns text.toUpperCase()

// TODO: Create LowerCaseStrategy implementing TextStrategy
// - process returns text.toLowerCase()

// TODO: Create TitleCaseStrategy implementing TextStrategy
// - process capitalizes first letter of each word
// - Example: 'hello world' -> 'Hello World'

// TODO: Create SlugStrategy implementing TextStrategy
// - process converts to lowercase and replaces spaces with hyphens
// - Example: 'Hello World' -> 'hello-world'

// TODO: Create ReverseStrategy implementing TextStrategy
// - process reverses the string
// - Example: 'Hello' -> 'olleH'

// TODO: Create TextProcessor class (Context)
// - private strategy: TextStrategy
// - constructor(strategy: TextStrategy)
// - setStrategy(strategy: TextStrategy): void
// - execute(text: string): string - calls strategy.process()

// ============ TEST YOUR CODE ============
// Uncomment the lines below to test your implementation

// const processor = new TextProcessor(new UpperCaseStrategy());
// const text = 'Hello World from TypeScript';

// console.log('Original:', text);
// console.log('');

// console.log('UpperCase:', processor.execute(text));

// processor.setStrategy(new LowerCaseStrategy());
// console.log('LowerCase:', processor.execute(text));

// processor.setStrategy(new TitleCaseStrategy());
// console.log('TitleCase:', processor.execute('hello world from typescript'));

// processor.setStrategy(new SlugStrategy());
// console.log('Slug:', processor.execute(text));

// processor.setStrategy(new ReverseStrategy());
// console.log('Reverse:', processor.execute(text));

// // Strategy can be selected dynamically
// const strategies: Record<string, TextStrategy> = {
//   upper: new UpperCaseStrategy(),
//   lower: new LowerCaseStrategy(),
//   title: new TitleCaseStrategy(),
//   slug: new SlugStrategy(),
//   reverse: new ReverseStrategy()
// };

// console.log('\n=== Dynamic Strategy Selection ===');
// ['upper', 'slug', 'reverse'].forEach(name => {
//   processor.setStrategy(strategies[name]);
//   console.log(`${name}: ${processor.execute('Dynamic Strategy')}`);
// });
