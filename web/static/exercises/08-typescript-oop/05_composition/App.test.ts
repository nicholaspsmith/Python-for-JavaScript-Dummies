// Test specifications for Composition Over Inheritance exercise

/*
Expected behavior:

1. Channel interfaces define the send() contract

2. Notifier implementations:
   - EmailNotifier.send('Hello', 'test@example.com') logs 'Sending via Email: Hello to test@example.com'
   - SMSNotifier.send('Hello', '+1-555-0123') logs 'Sending via SMS: Hello to +1-555-0123'
   - PushNotifier.send('Hello', 'device-123') logs 'Sending via Push: Hello to device-123'

3. User composition:
   - Users can have any combination of channels
   - notify() sends to all configured channels
   - Channels can be added/changed at runtime

4. Benefits demonstrated:
   - No inheritance hierarchy needed
   - Flexible configuration per user
   - Easy to add new channel types
*/
