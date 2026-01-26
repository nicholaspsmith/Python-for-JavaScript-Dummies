// Test specifications for Classes and Inheritance exercise

/*
Expected behavior:

1. Animal class:
   - new Animal('Generic').getName() === 'Generic'
   - new Animal('Generic').makeSound() === 'Some sound'
   - 'name' property should be protected (accessible in subclasses)

2. Dog class:
   - new Dog('Buddy', 'Labrador').getName() === 'Buddy'
   - new Dog('Buddy', 'Labrador').getBreed() === 'Labrador'
   - new Dog('Buddy', 'Labrador').makeSound() === 'Woof!'
   - Dog should be instanceof Animal

3. Cat class:
   - new Cat('Whiskers').getName() === 'Whiskers'
   - new Cat('Whiskers').makeSound() === 'Meow!'
   - Cat should be instanceof Animal
*/
