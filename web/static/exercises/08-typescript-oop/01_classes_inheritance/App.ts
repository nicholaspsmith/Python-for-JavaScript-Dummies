// Classes and Inheritance in TypeScript
// Learn how to create classes and use inheritance

// TODO: Create an Animal class
// - protected name property
// - constructor that accepts name
// - makeSound() method returns 'Some sound'
// - getName() method returns the name

// TODO: Create a Dog class that extends Animal
// - private breed property
// - constructor accepts name and breed, calls super(name)
// - override makeSound() to return 'Woof!'
// - getBreed() method returns the breed

// TODO: Create a Cat class that extends Animal
// - override makeSound() to return 'Meow!'

// ============ TEST YOUR CODE ============
// Uncomment the lines below to test your implementation

// const animal = new Animal('Generic');
// console.log('Animal name:', animal.getName());
// console.log('Animal sound:', animal.makeSound());

// const dog = new Dog('Buddy', 'Labrador');
// console.log('Dog name:', dog.getName());
// console.log('Dog breed:', dog.getBreed());
// console.log('Dog sound:', dog.makeSound());

// const cat = new Cat('Whiskers');
// console.log('Cat name:', cat.getName());
// console.log('Cat sound:', cat.makeSound());

// Test inheritance
// console.log('Is dog an Animal?', dog instanceof Animal);
// console.log('Is cat an Animal?', cat instanceof Animal);
