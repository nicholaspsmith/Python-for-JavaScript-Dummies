// Repository Pattern
// Abstract data access behind a consistent interface

// TODO: Create Product interface
// - id: string
// - name: string
// - price: number
// - category: string

// TODO: Create generic Repository<T> interface
// - findById(id: string): T | undefined
// - findAll(): T[]
// - save(item: T): void
// - delete(id: string): boolean
// - findBy(predicate: (item: T) => boolean): T[]

// TODO: Create InMemoryProductRepository implementing Repository<Product>
// - private products: Map<string, Product> = new Map()
// - findById: returns product from map
// - findAll: returns array of all products
// - save: adds/updates product in map (use product.id as key)
// - delete: removes product, returns true if existed
// - findBy: filters products by predicate

// TODO: Create ProductService class
// - constructor(private repository: Repository<Product>)
// - getProduct(id: string): Product | undefined
// - getAllProducts(): Product[]
// - createProduct(product: Product): void
// - deleteProduct(id: string): boolean
// - getProductsByCategory(category: string): Product[]
// - getExpensiveProducts(minPrice: number): Product[]

// ============ TEST YOUR CODE ============
// Uncomment the lines below to test your implementation

// const repository = new InMemoryProductRepository();
// const productService = new ProductService(repository);

// // Add some products
// productService.createProduct({ id: '1', name: 'Laptop', price: 999, category: 'Electronics' });
// productService.createProduct({ id: '2', name: 'Mouse', price: 29, category: 'Electronics' });
// productService.createProduct({ id: '3', name: 'Desk', price: 299, category: 'Furniture' });
// productService.createProduct({ id: '4', name: 'Chair', price: 199, category: 'Furniture' });
// productService.createProduct({ id: '5', name: 'Monitor', price: 399, category: 'Electronics' });

// console.log('=== All Products ===');
// productService.getAllProducts().forEach(p =>
//   console.log(`${p.name}: $${p.price} (${p.category})`)
// );

// console.log('\n=== Electronics ===');
// productService.getProductsByCategory('Electronics').forEach(p =>
//   console.log(`${p.name}: $${p.price}`)
// );

// console.log('\n=== Expensive Products (>$200) ===');
// productService.getExpensiveProducts(200).forEach(p =>
//   console.log(`${p.name}: $${p.price}`)
// );

// console.log('\n=== Get Single Product ===');
// const laptop = productService.getProduct('1');
// console.log('Found:', laptop?.name);

// console.log('\n=== Delete Product ===');
// console.log('Deleted Mouse:', productService.deleteProduct('2'));
// console.log('Products after delete:', productService.getAllProducts().length);

// The beauty: ProductService doesn't know if data is in memory,
// database, or cloud. It just uses the Repository interface!
