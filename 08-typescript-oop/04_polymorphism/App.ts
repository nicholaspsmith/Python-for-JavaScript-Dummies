// Polymorphism in TypeScript
// Subtype polymorphism and parametric polymorphism (generics)

// === PART 1: SUBTYPE POLYMORPHISM ===

// TODO: Create PaymentProcessor interface
// - processPayment(amount: number): boolean
// - getPaymentMethod(): string

// TODO: Create CreditCardProcessor class
// - private cardNumber: string
// - implements PaymentProcessor

// TODO: Create PayPalProcessor class
// - private email: string
// - implements PaymentProcessor

// === PART 2: PARAMETRIC POLYMORPHISM ===

// TODO: Create generic Container<T> class
// - private value: T
// - getValue(): T
// - setValue(value: T): void

// TODO: Create generic Pair<T, U> class
// - constructor(public first: T, public second: U)
// - swap(): Pair<U, T>

// ============ TEST YOUR CODE ============
// Uncomment the lines below to test your implementation

// Part 1: Subtype Polymorphism
// const processors: PaymentProcessor[] = [
//   new CreditCardProcessor('4111-1111-1111-1111'),
//   new PayPalProcessor('user@example.com')
// ];

// processors.forEach(processor => {
//   console.log(`Using ${processor.getPaymentMethod()}`);
//   processor.processPayment(99.99);
// });

// Part 2: Generics
// const numberContainer = new Container<number>(42);
// console.log('Number value:', numberContainer.getValue());
// numberContainer.setValue(100);
// console.log('Updated value:', numberContainer.getValue());

// const stringContainer = new Container<string>('Hello');
// console.log('String value:', stringContainer.getValue());

// const pair = new Pair<string, number>('age', 25);
// console.log('Original pair:', pair.first, pair.second);
// const swapped = pair.swap();
// console.log('Swapped pair:', swapped.first, swapped.second);
