// Dependency Inversion Principle (DIP)
// High-level modules should not depend on low-level modules.
// Both should depend on abstractions.

// BAD EXAMPLE - Direct dependency on concretions (DO NOT USE):
// class NotificationService {
//   private emailSender = new EmailSender();  // Tightly coupled!
//   private htmlFormatter = new HTMLFormatter(); // Can't swap!
//   notify(msg: string) {
//     this.emailSender.send(this.htmlFormatter.format(msg));
//   }
// }

// GOOD DESIGN - Depend on abstractions:

// TODO: Create MessageFormatter interface
// - format(message: string): string

// TODO: Create NotificationSender interface
// - send(formattedMessage: string): void

// TODO: Create Logger interface
// - log(message: string): void

// TODO: Create HTMLFormatter implementing MessageFormatter
// - format returns '<div>{message}</div>'

// TODO: Create PlainTextFormatter implementing MessageFormatter
// - format returns message unchanged

// TODO: Create EmailSender implementing NotificationSender
// - send logs 'Sending email: {formattedMessage}'

// TODO: Create SMSSender implementing NotificationSender
// - send logs 'Sending SMS: {formattedMessage}'

// TODO: Create ConsoleLogger implementing Logger
// - log outputs '[LOG] {message}' using console.log

// TODO: Create NotificationService class (high-level module)
// - constructor(
//     private formatter: MessageFormatter,
//     private sender: NotificationSender,
//     private logger: Logger
//   )
// - notify(message: string): void
//   - Formats the message
//   - Sends the formatted message
//   - Logs 'Notification sent: {original message}'

// ============ TEST YOUR CODE ============
// Uncomment the lines below to test your implementation

// const logger = new ConsoleLogger();

// // Configuration 1: HTML email notifications
// const emailService = new NotificationService(
//   new HTMLFormatter(),
//   new EmailSender(),
//   logger
// );
// console.log('=== HTML Email ===');
// emailService.notify('Welcome to our platform!');

// // Configuration 2: Plain text SMS notifications
// const smsService = new NotificationService(
//   new PlainTextFormatter(),
//   new SMSSender(),
//   logger
// );
// console.log('\n=== Plain Text SMS ===');
// smsService.notify('Your code is 123456');

// // Configuration 3: HTML SMS (why not?)
// const htmlSmsService = new NotificationService(
//   new HTMLFormatter(),
//   new SMSSender(),
//   logger
// );
// console.log('\n=== HTML SMS ===');
// htmlSmsService.notify('Special offer!');

// Notice: NotificationService never changed!
// We just injected different implementations.
