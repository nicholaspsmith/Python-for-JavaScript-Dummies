// Test specifications for Repository Pattern exercise

/*
Expected behavior:

1. Product interface:
   - Has id, name, price, category fields

2. Repository<T> interface:
   - Generic interface for any entity type
   - CRUD operations + flexible querying

3. InMemoryProductRepository:
   - findById('1') returns product with id '1' or undefined
   - findAll() returns array of all products
   - save(product) adds/updates product
   - delete('1') removes product, returns true/false
   - findBy(p => p.price > 100) filters products

4. ProductService:
   - Uses Repository through dependency injection
   - getProduct delegates to repository.findById
   - getAllProducts delegates to repository.findAll
   - createProduct delegates to repository.save
   - deleteProduct delegates to repository.delete
   - getProductsByCategory uses findBy with category filter
   - getExpensiveProducts uses findBy with price filter

5. Repository Pattern Benefits:
   - Data access logic is isolated in repository
   - ProductService is testable with mock repository
   - Easy to swap implementations (InMemory -> Database -> Cloud)
   - Single source of truth for data operations
*/
