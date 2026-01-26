// Test specifications for Polymorphism exercise

/*
Expected behavior:

1. PaymentProcessor interface compliance:
   - Both CreditCardProcessor and PayPalProcessor can be used as PaymentProcessor

2. CreditCardProcessor:
   - processPayment(100) logs 'Processing $100 via Credit Card'
   - getPaymentMethod() === 'Credit Card'

3. PayPalProcessor:
   - processPayment(100) logs 'Processing $100 via PayPal'
   - getPaymentMethod() === 'PayPal'

4. Container<T>:
   - new Container<number>(42).getValue() === 42
   - new Container<string>('hello').getValue() === 'hello'
   - setValue changes the value

5. Pair<T, U>:
   - new Pair<string, number>('a', 1).first === 'a'
   - new Pair<string, number>('a', 1).second === 1
   - swap() returns Pair<U, T> with values swapped
*/
