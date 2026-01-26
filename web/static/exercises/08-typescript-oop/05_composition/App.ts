// Composition Over Inheritance
// Build flexible systems by composing behaviors

// TODO: Create EmailChannel interface
// - send(message: string, email: string): void

// TODO: Create SMSChannel interface
// - send(message: string, phone: string): void

// TODO: Create PushChannel interface
// - send(message: string, deviceId: string): void

// TODO: Create EmailNotifier class implementing EmailChannel
// - send() logs 'Sending via Email: {message} to {email}'

// TODO: Create SMSNotifier class implementing SMSChannel
// - send() logs 'Sending via SMS: {message} to {phone}'

// TODO: Create PushNotifier class implementing PushChannel
// - send() logs 'Sending via Push: {message} to {deviceId}'

// TODO: Create User class with composition
// - private name: string
// - private email?: string
// - private phone?: string
// - private deviceId?: string
// - private emailChannel?: EmailChannel
// - private smsChannel?: SMSChannel
// - private pushChannel?: PushChannel
// - constructor(name: string)
// - setEmailChannel(channel: EmailChannel, email: string): void
// - setSMSChannel(channel: SMSChannel, phone: string): void
// - setPushChannel(channel: PushChannel, deviceId: string): void
// - notify(message: string): void - sends to all configured channels

// ============ TEST YOUR CODE ============
// Uncomment the lines below to test your implementation

// const user1 = new User('Alice');
// user1.setEmailChannel(new EmailNotifier(), 'alice@example.com');
// user1.setSMSChannel(new SMSNotifier(), '+1-555-0123');
// console.log('Notifying Alice (Email + SMS):');
// user1.notify('Your order has shipped!');

// const user2 = new User('Bob');
// user2.setPushChannel(new PushNotifier(), 'device-xyz-789');
// console.log('\nNotifying Bob (Push only):');
// user2.notify('New message received!');

// const user3 = new User('Charlie');
// user3.setEmailChannel(new EmailNotifier(), 'charlie@example.com');
// user3.setSMSChannel(new SMSNotifier(), '+1-555-0456');
// user3.setPushChannel(new PushNotifier(), 'device-abc-123');
// console.log('\nNotifying Charlie (All channels):');
// user3.notify('Important update!');
