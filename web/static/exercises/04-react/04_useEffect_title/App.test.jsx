import { render, screen, fireEvent } from '@testing-library/react';
import App from './App';

describe('useEffect Document Title', () => {
  beforeEach(() => {
    document.title = 'Test';
  });

  test('sets initial document title to Count: 0', () => {
    render(<App />);
    expect(document.title).toBe('Count: 0');
  });

  test('updates title when count increments', () => {
    render(<App />);
    fireEvent.click(screen.getByText(/\+/));
    expect(document.title).toBe('Count: 1');
  });

  test('updates title when count decrements', () => {
    render(<App />);
    fireEvent.click(screen.getByText(/-/));
    expect(document.title).toBe('Count: -1');
  });

  test('updates title after multiple changes', () => {
    render(<App />);
    fireEvent.click(screen.getByText(/\+/));
    fireEvent.click(screen.getByText(/\+/));
    fireEvent.click(screen.getByText(/\+/));
    expect(document.title).toBe('Count: 3');
  });
});
