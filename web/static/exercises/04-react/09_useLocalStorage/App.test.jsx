import { render, screen, fireEvent } from '@testing-library/react';
import App from './App';

describe('useLocalStorage', () => {
  beforeEach(() => {
    localStorage.clear();
  });

  test('uses initial values when localStorage is empty', () => {
    render(<App />);
    expect(screen.getByPlaceholderText(/enter your name/i).value).toBe('');
  });

  test('saves name to localStorage', () => {
    render(<App />);
    const input = screen.getByPlaceholderText(/enter your name/i);
    fireEvent.change(input, { target: { value: 'Alice' } });

    expect(localStorage.getItem('name')).toBe('"Alice"');
  });

  test('loads name from localStorage', () => {
    localStorage.setItem('name', '"Bob"');
    render(<App />);

    expect(screen.getByPlaceholderText(/enter your name/i).value).toBe('Bob');
  });

  test('displays name in preview', () => {
    render(<App />);
    fireEvent.change(screen.getByPlaceholderText(/enter your name/i), {
      target: { value: 'Charlie' }
    });

    expect(screen.getByText(/hello, charlie/i)).toBeInTheDocument();
  });

  test('saves color to localStorage', () => {
    render(<App />);
    const colorInput = screen.getByDisplayValue(/#/i);
    fireEvent.change(colorInput, { target: { value: '#ff0000' } });

    expect(localStorage.getItem('favoriteColor')).toBe('"#ff0000"');
  });
});
