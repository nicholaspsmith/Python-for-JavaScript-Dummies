// Liskov Substitution Principle (LSP)
// Subtypes must be substitutable for their base types

// BAD EXAMPLE - Violates LSP (DO NOT USE):
// class Rectangle {
//   constructor(protected width: number, protected height: number) {}
//   setWidth(w: number) { this.width = w; }
//   setHeight(h: number) { this.height = h; }
//   getArea() { return this.width * this.height; }
// }
// class Square extends Rectangle {
//   setWidth(w: number) { this.width = w; this.height = w; }  // BREAKS LSP!
//   setHeight(h: number) { this.width = h; this.height = h; } // BREAKS LSP!
// }
// Using Square where Rectangle is expected causes unexpected behavior!

// GOOD DESIGN - Follows LSP:

// TODO: Create Shape interface
// - getArea(): number
// - getPerimeter(): number

// TODO: Create Rectangle class implementing Shape
// - constructor(protected width: number, protected height: number)
// - getArea() returns width * height
// - getPerimeter() returns 2 * (width + height)
// - getWidth(): number
// - getHeight(): number

// TODO: Create Square class implementing Shape (NOT extending Rectangle!)
// - constructor(private side: number)
// - getArea() returns side * side
// - getPerimeter() returns 4 * side
// - getSide(): number

// TODO: Create printShapeInfo function
// - Takes a Shape parameter
// - Logs 'Area: {area}, Perimeter: {perimeter}'

// ============ TEST YOUR CODE ============
// Uncomment the lines below to test your implementation

// const shapes: Shape[] = [
//   new Rectangle(10, 5),
//   new Square(7),
//   new Rectangle(3, 8),
//   new Square(4)
// ];

// console.log('All shapes (LSP in action - any Shape works):');
// shapes.forEach((shape, i) => {
//   console.log(`Shape ${i + 1}:`);
//   printShapeInfo(shape);
// });

// Specific methods still work
// const rect = new Rectangle(10, 5);
// console.log(`\nRectangle: ${rect.getWidth()} x ${rect.getHeight()}`);

// const square = new Square(7);
// console.log(`Square: ${square.getSide()} x ${square.getSide()}`);
