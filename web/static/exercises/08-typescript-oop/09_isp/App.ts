// Interface Segregation Principle (ISP)
// Clients should not be forced to depend on interfaces they don't use

// BAD EXAMPLE - Fat interface (DO NOT USE):
// interface Worker {
//   work(): void;
//   eat(): void;
//   sleep(): void;
// }
// class Robot implements Worker {
//   work() { /* OK */ }
//   eat() { /* Robots don't eat! Forced to implement empty method */ }
//   sleep() { /* Robots don't sleep! Forced to implement empty method */ }
// }

// GOOD DESIGN - Segregated interfaces:

// TODO: Create Workable interface
// - work(): void

// TODO: Create Eatable interface
// - eat(): void

// TODO: Create Sleepable interface
// - sleep(): void

// TODO: Create Human class implementing Workable, Eatable, Sleepable
// - constructor(private name: string)
// - work() logs '{name} is working'
// - eat() logs '{name} is eating lunch'
// - sleep() logs '{name} is sleeping'

// TODO: Create Robot class implementing Workable ONLY
// - constructor(private model: string)
// - work() logs 'Robot {model} is working'

// TODO: Create manager functions:
// - assignWork(worker: Workable): void - calls worker.work()
// - scheduleLunch(eater: Eatable): void - calls eater.eat()
// - endDay(sleeper: Sleepable): void - calls sleeper.sleep()

// ============ TEST YOUR CODE ============
// Uncomment the lines below to test your implementation

// const alice = new Human('Alice');
// const bob = new Human('Bob');
// const robo1 = new Robot('RX-78');
// const robo2 = new Robot('T-800');

// console.log('=== Assigning Work ===');
// // Both humans and robots can work
// assignWork(alice);
// assignWork(bob);
// assignWork(robo1);
// assignWork(robo2);

// console.log('\n=== Lunch Break ===');
// // Only humans eat
// scheduleLunch(alice);
// scheduleLunch(bob);
// // scheduleLunch(robo1); // TypeScript error! Robot doesn't implement Eatable

// console.log('\n=== End of Day ===');
// // Only humans sleep
// endDay(alice);
// endDay(bob);
// // endDay(robo1); // TypeScript error! Robot doesn't implement Sleepable

// console.log('\n=== Robots keep working 24/7 ===');
// assignWork(robo1);
// assignWork(robo2);
