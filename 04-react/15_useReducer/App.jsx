import { useReducer } from 'react';
import './styles.css';

const products = [
  { id: 1, name: 'React T-Shirt', price: 25 },
  { id: 2, name: 'JavaScript Mug', price: 15 },
  { id: 3, name: 'Node.js Sticker Pack', price: 5 },
];

const initialState = {
  items: [], // { id, name, price, quantity }
};

// TODO: Implement the reducer function
// Handle these action types:
// - ADD_ITEM: Add item to cart (or increment quantity if exists)
// - REMOVE_ITEM: Remove item from cart
// - UPDATE_QUANTITY: Update item quantity
// - CLEAR_CART: Empty the cart
function cartReducer(state, action) {
  switch (action.type) {
    case 'ADD_ITEM':
      // TODO: Check if item exists, if so increment quantity
      // Otherwise add new item with quantity 1
      return state;

    case 'REMOVE_ITEM':
      // TODO: Filter out the item with matching id
      return state;

    case 'UPDATE_QUANTITY':
      // TODO: Update quantity for item with matching id
      // Remove item if quantity becomes 0
      return state;

    case 'CLEAR_CART':
      // TODO: Return initial state
      return state;

    default:
      return state;
  }
}

export default function App() {
  const [state, dispatch] = useReducer(cartReducer, initialState);

  const total = state.items.reduce(
    (sum, item) => sum + item.price * item.quantity,
    0
  );

  return (
    <div className="container">
      <h1>Shopping Cart</h1>

      <div className="products">
        <h2>Products</h2>
        {products.map((product) => (
          <div key={product.id} className="product">
            <span>{product.name} - ${product.price}</span>
            <button
              onClick={() =>
                dispatch({ type: 'ADD_ITEM', payload: product })
              }
            >
              Add to Cart
            </button>
          </div>
        ))}
      </div>

      <div className="cart">
        <h2>Cart ({state.items.length} items)</h2>
        {state.items.length === 0 ? (
          <p className="empty">Your cart is empty</p>
        ) : (
          <>
            {state.items.map((item) => (
              <div key={item.id} className="cart-item">
                <span className="item-name">{item.name}</span>
                <div className="item-controls">
                  <button
                    onClick={() =>
                      dispatch({
                        type: 'UPDATE_QUANTITY',
                        payload: { id: item.id, quantity: item.quantity - 1 },
                      })
                    }
                  >
                    -
                  </button>
                  <span className="quantity">{item.quantity}</span>
                  <button
                    onClick={() =>
                      dispatch({
                        type: 'UPDATE_QUANTITY',
                        payload: { id: item.id, quantity: item.quantity + 1 },
                      })
                    }
                  >
                    +
                  </button>
                  <button
                    className="remove"
                    onClick={() =>
                      dispatch({ type: 'REMOVE_ITEM', payload: { id: item.id } })
                    }
                  >
                    Remove
                  </button>
                </div>
                <span className="item-total">${item.price * item.quantity}</span>
              </div>
            ))}
            <div className="total">
              <strong>Total: ${total}</strong>
            </div>
            <button
              className="clear-btn"
              onClick={() => dispatch({ type: 'CLEAR_CART' })}
            >
              Clear Cart
            </button>
          </>
        )}
      </div>
    </div>
  );
}
