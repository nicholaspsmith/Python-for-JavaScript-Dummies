// Test specifications for useReducer exercise

/*
Expected reducer implementation:

case 'ADD_ITEM': {
  const existingItem = state.items.find(item => item.id === action.payload.id);
  if (existingItem) {
    return {
      ...state,
      items: state.items.map(item =>
        item.id === action.payload.id
          ? { ...item, quantity: item.quantity + 1 }
          : item
      ),
    };
  }
  return {
    ...state,
    items: [...state.items, { ...action.payload, quantity: 1 }],
  };
}

case 'REMOVE_ITEM':
  return {
    ...state,
    items: state.items.filter(item => item.id !== action.payload.id),
  };

case 'UPDATE_QUANTITY': {
  const { id, quantity } = action.payload;
  if (quantity <= 0) {
    return {
      ...state,
      items: state.items.filter(item => item.id !== id),
    };
  }
  return {
    ...state,
    items: state.items.map(item =>
      item.id === id ? { ...item, quantity } : item
    ),
  };
}

case 'CLEAR_CART':
  return initialState;
*/
