// Test specifications for Encapsulation exercise

/*
Expected behavior:

1. BankAccount initialization:
   - new BankAccount('ACC-123').balance === 0
   - new BankAccount('ACC-123').accountNumber === 'ACC-123'

2. Deposit:
   - deposit(100) returns true, balance becomes 100
   - deposit(-50) returns false, balance unchanged
   - deposit(0) returns false

3. Withdraw:
   - After deposit(100), withdraw(30) returns true, balance is 70
   - withdraw(100) when balance is 70 returns false
   - withdraw(-10) returns false

4. Transaction history:
   - Returns array of Transaction objects
   - Each has type, amount, and date
   - Returned array is a copy (modifying it doesn't affect internal state)

5. Encapsulation:
   - _balance, _accountNumber, _transactions are not directly accessible
   - accountNumber cannot be modified after creation
*/
