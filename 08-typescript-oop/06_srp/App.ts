// Single Responsibility Principle (SRP)
// A class should have only one reason to change

// BAD EXAMPLE - Violates SRP (DO NOT USE):
// class UserManager {
//   private users: User[] = [];
//   addUser(user: User) { /* manages users */ }
//   validateEmail(email: string) { /* validates */ }
//   sendEmail(to: string, subject: string) { /* sends email */ }
//   generateReport() { /* creates report */ }
// }
// This class has 4 reasons to change!

// TODO: Create User interface
// - id: number
// - name: string
// - email: string

// TODO: Create EmailValidator class
// - isValid(email: string): boolean
// - Returns true if email contains '@' and '.'

// TODO: Create EmailService class
// - send(to: string, subject: string, body: string): void
// - Logs 'Sending email to {to}: {subject}'

// TODO: Create UserRepository class
// - private users: User[] = []
// - add(user: User): void
// - findByEmail(email: string): User | undefined
// - getAll(): User[]

// TODO: Create UserReportGenerator class
// - generate(users: User[]): string
// - Returns 'User Report:\n- {name} ({email})\n...' for each user

// ============ TEST YOUR CODE ============
// Uncomment the lines below to test your implementation

// const validator = new EmailValidator();
// console.log('Valid email:', validator.isValid('test@example.com'));
// console.log('Invalid email:', validator.isValid('invalid-email'));

// const emailService = new EmailService();
// emailService.send('user@example.com', 'Welcome!', 'Thanks for joining.');

// const userRepo = new UserRepository();
// userRepo.add({ id: 1, name: 'Alice', email: 'alice@example.com' });
// userRepo.add({ id: 2, name: 'Bob', email: 'bob@example.com' });
// console.log('All users:', userRepo.getAll());
// console.log('Find Alice:', userRepo.findByEmail('alice@example.com'));

// const reportGenerator = new UserReportGenerator();
// console.log(reportGenerator.generate(userRepo.getAll()));
