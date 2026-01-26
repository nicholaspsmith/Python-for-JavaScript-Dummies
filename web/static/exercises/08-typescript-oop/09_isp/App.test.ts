// Test specifications for Interface Segregation Principle exercise

/*
Expected behavior:

1. Segregated interfaces:
   - Workable has only work()
   - Eatable has only eat()
   - Sleepable has only sleep()

2. Human class:
   - Implements all three interfaces
   - work(), eat(), sleep() all log appropriate messages
   - Can be used anywhere any of the interfaces is expected

3. Robot class:
   - Implements only Workable
   - Has no eat() or sleep() methods
   - Can only be passed to functions expecting Workable

4. Manager functions:
   - assignWork() accepts any Workable (Human or Robot)
   - scheduleLunch() accepts only Eatable (Human, not Robot)
   - endDay() accepts only Sleepable (Human, not Robot)

5. ISP Benefits:
   - Robot doesn't have useless empty methods
   - Type safety prevents passing Robot to scheduleLunch/endDay
   - Each interface is focused and cohesive
*/
