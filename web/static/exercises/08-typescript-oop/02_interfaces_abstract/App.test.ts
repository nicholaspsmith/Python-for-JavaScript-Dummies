// Test specifications for Interfaces vs Abstract Classes exercise

/*
Expected behavior:

1. Drawable interface should have draw(): void

2. Resizable interface should have resize(factor: number): void

3. Shape abstract class:
   - Cannot be instantiated directly
   - draw() logs 'Drawing a {color} shape'
   - getArea() is abstract

4. Rectangle:
   - new Rectangle('blue', 10, 5).getArea() === 50
   - After resize(2), getArea() === 200
   - Implements both Drawable and Resizable

5. Circle:
   - new Circle('red', 7).getArea() === Math.PI * 49
   - Implements Drawable (through Shape)
*/
