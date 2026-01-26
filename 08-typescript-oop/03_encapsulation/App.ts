// Encapsulation in TypeScript
// Protect internal state with access modifiers and controlled access

interface Transaction {
  type: 'deposit' | 'withdraw';
  amount: number;
  date: Date;
}

// TODO: Create BankAccount class
// - private _balance: number (initialize to 0)
// - private readonly _accountNumber: string
// - private _transactions: Transaction[]
// - constructor(accountNumber: string)
// - get balance(): number
// - get accountNumber(): string
// - deposit(amount: number): boolean
// - withdraw(amount: number): boolean
// - getTransactionHistory(): Transaction[]

// ============ TEST YOUR CODE ============
// Uncomment the lines below to test your implementation

// const account = new BankAccount('ACC-12345');
// console.log('Account number:', account.accountNumber);
// console.log('Initial balance:', account.balance);

// console.log('Deposit $100:', account.deposit(100));
// console.log('Balance after deposit:', account.balance);

// console.log('Withdraw $30:', account.withdraw(30));
// console.log('Balance after withdraw:', account.balance);

// console.log('Withdraw $100 (should fail):', account.withdraw(100));
// console.log('Balance unchanged:', account.balance);

// console.log('Deposit -50 (should fail):', account.deposit(-50));

// console.log('Transaction history:', account.getTransactionHistory());

// This should not compile:
// account._balance = 1000000; // Error: _balance is private
// account._accountNumber = 'HACKED'; // Error: readonly
