// Test specifications for Liskov Substitution Principle exercise

/*
Expected behavior:

1. Shape interface:
   - Both Rectangle and Square implement Shape
   - printShapeInfo works with any Shape

2. Rectangle:
   - new Rectangle(10, 5).getArea() === 50
   - new Rectangle(10, 5).getPerimeter() === 30
   - Has getWidth() and getHeight()

3. Square:
   - new Square(7).getArea() === 49
   - new Square(7).getPerimeter() === 28
   - Has getSide()

4. LSP Compliance:
   - Any code expecting Shape works with both Rectangle and Square
   - No unexpected side effects
   - Each class fulfills the Shape contract completely

5. Why this follows LSP:
   - Square doesn't inherit misleading setWidth/setHeight from Rectangle
   - Each shape correctly implements its own behavior
   - Substitutability is guaranteed through the Shape interface
*/
