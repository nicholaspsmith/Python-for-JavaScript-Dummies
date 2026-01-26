// Interfaces vs Abstract Classes
// Learn when to use each and how they work together

// TODO: Create a Drawable interface
// - draw(): void

// TODO: Create a Resizable interface
// - resize(factor: number): void

// TODO: Create an abstract Shape class that implements Drawable
// - protected color: string
// - constructor that sets color
// - abstract getArea(): number
// - draw() logs 'Drawing a {color} shape'

// TODO: Create Rectangle class extending Shape, implementing Resizable
// - private width and height
// - constructor(color, width, height)
// - getArea() returns width * height
// - resize(factor) multiplies both dimensions by factor

// TODO: Create Circle class extending Shape
// - private radius
// - constructor(color, radius)
// - getArea() returns Math.PI * radius * radius

// ============ TEST YOUR CODE ============
// Uncomment the lines below to test your implementation

// const rect = new Rectangle('blue', 10, 5);
// console.log('Rectangle area:', rect.getArea());
// rect.draw();
// rect.resize(2);
// console.log('Rectangle area after resize:', rect.getArea());

// const circle = new Circle('red', 7);
// console.log('Circle area:', circle.getArea().toFixed(2));
// circle.draw();

// Type checking with interfaces
// const drawables: Drawable[] = [rect, circle];
// drawables.forEach(d => d.draw());
