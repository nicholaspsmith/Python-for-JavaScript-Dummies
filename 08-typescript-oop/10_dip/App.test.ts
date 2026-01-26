// Test specifications for Dependency Inversion Principle exercise

/*
Expected behavior:

1. Abstractions (interfaces):
   - MessageFormatter: format(message: string): string
   - NotificationSender: send(formattedMessage: string): void
   - Logger: log(message: string): void

2. Low-level implementations:
   - HTMLFormatter.format('Hello') === '<div>Hello</div>'
   - PlainTextFormatter.format('Hello') === 'Hello'
   - EmailSender.send('msg') logs 'Sending email: msg'
   - SMSSender.send('msg') logs 'Sending SMS: msg'
   - ConsoleLogger.log('msg') logs '[LOG] msg'

3. NotificationService (high-level module):
   - Accepts any implementations of the interfaces
   - notify() calls formatter, sender, and logger
   - Works with any combination of implementations

4. DIP Benefits:
   - NotificationService is not coupled to specific implementations
   - Easy to add new formatters/senders without changing NotificationService
   - Easy to test with mock implementations
   - Configuration happens at composition time
*/
