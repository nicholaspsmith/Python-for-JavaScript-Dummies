// Test specifications for Open/Closed Principle exercise

/*
Expected behavior:

1. DiscountStrategy implementations:
   - NoDiscount.calculate(100) === 100
   - PercentageDiscount(10).calculate(100) === 90
   - PercentageDiscount(25).calculate(100) === 75
   - FixedDiscount(25).calculate(100) === 75
   - FixedDiscount(150).calculate(100) === 0 (not negative)
   - BuyOneGetOneFree.calculate(100) === 50

2. PriceCalculator:
   - Works with any DiscountStrategy
   - calculateFinalPrice(100, new PercentageDiscount(10)) === 90

3. SeasonalDiscount (extension):
   - SeasonalDiscount(20, 'Summer').calculate(100) === 80
   - getDescription() includes season name

4. OCP Benefits demonstrated:
   - PriceCalculator never needed to change
   - New discount types added by creating new classes
   - Existing strategies remain untouched
*/
