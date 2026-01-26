// Test specifications for Single Responsibility Principle exercise

/*
Expected behavior:

1. EmailValidator (single responsibility: validation):
   - isValid('test@example.com') === true
   - isValid('invalid') === false
   - isValid('no-at.com') === false
   - isValid('no-dot@com') === false

2. EmailService (single responsibility: sending):
   - send() logs the email details
   - Does not validate or store anything

3. UserRepository (single responsibility: data storage):
   - add() stores users
   - findByEmail() retrieves by email
   - getAll() returns all users
   - Does not validate or send emails

4. UserReportGenerator (single responsibility: reporting):
   - generate() creates formatted string
   - Does not store or modify data

Benefits of SRP:
- Each class is focused and easy to understand
- Changes to email validation don't affect storage
- Changes to reporting don't affect email sending
- Easy to test each class in isolation
*/
