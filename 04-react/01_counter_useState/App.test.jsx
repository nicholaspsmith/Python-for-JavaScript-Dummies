import { render, screen, fireEvent } from '@testing-library/react';
import App from './App';

describe('Counter', () => {
  test('displays initial count of 0', () => {
    render(<App />);
    expect(screen.getByText(/count: 0/i)).toBeInTheDocument();
  });

  test('increments count when Increment button is clicked', () => {
    render(<App />);
    fireEvent.click(screen.getByText(/increment/i));
    expect(screen.getByText(/count: 1/i)).toBeInTheDocument();
  });

  test('decrements count when Decrement button is clicked', () => {
    render(<App />);
    fireEvent.click(screen.getByText(/decrement/i));
    expect(screen.getByText(/count: -1/i)).toBeInTheDocument();
  });

  test('resets count to 0 when Reset button is clicked', () => {
    render(<App />);
    fireEvent.click(screen.getByText(/increment/i));
    fireEvent.click(screen.getByText(/increment/i));
    fireEvent.click(screen.getByText(/reset/i));
    expect(screen.getByText(/count: 0/i)).toBeInTheDocument();
  });
});
