// Open/Closed Principle (OCP)
// Software entities should be open for extension, closed for modification

// TODO: Create DiscountStrategy interface
// - calculate(price: number): number
// - getDescription(): string

// TODO: Create NoDiscount class implementing DiscountStrategy
// - calculate returns original price
// - getDescription returns 'No discount'

// TODO: Create PercentageDiscount class implementing DiscountStrategy
// - constructor(private percentage: number)
// - calculate returns price * (1 - percentage / 100)
// - getDescription returns '{percentage}% off'

// TODO: Create FixedDiscount class implementing DiscountStrategy
// - constructor(private amount: number)
// - calculate returns Math.max(0, price - amount)
// - getDescription returns '${amount} off'

// TODO: Create BuyOneGetOneFree class implementing DiscountStrategy
// - calculate returns price / 2
// - getDescription returns 'Buy one get one free'

// TODO: Create PriceCalculator class
// - calculateFinalPrice(price: number, discount: DiscountStrategy): number

// EXTENSION: Add SeasonalDiscount without modifying existing code
// TODO: Create SeasonalDiscount class implementing DiscountStrategy
// - constructor(private percentage: number, private season: string)
// - getDescription returns '{season} sale: {percentage}% off'

// ============ TEST YOUR CODE ============
// Uncomment the lines below to test your implementation

// const calculator = new PriceCalculator();
// const originalPrice = 100;

// const noDiscount = new NoDiscount();
// console.log(`${noDiscount.getDescription()}: $${calculator.calculateFinalPrice(originalPrice, noDiscount)}`);

// const tenPercent = new PercentageDiscount(10);
// console.log(`${tenPercent.getDescription()}: $${calculator.calculateFinalPrice(originalPrice, tenPercent)}`);

// const fixed25 = new FixedDiscount(25);
// console.log(`${fixed25.getDescription()}: $${calculator.calculateFinalPrice(originalPrice, fixed25)}`);

// const bogo = new BuyOneGetOneFree();
// console.log(`${bogo.getDescription()}: $${calculator.calculateFinalPrice(originalPrice, bogo)}`);

// Extension - new discount type added without modifying existing code!
// const winterSale = new SeasonalDiscount(30, 'Winter');
// console.log(`${winterSale.getDescription()}: $${calculator.calculateFinalPrice(originalPrice, winterSale)}`);
