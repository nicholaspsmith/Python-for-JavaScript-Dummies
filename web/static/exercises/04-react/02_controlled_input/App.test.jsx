import { render, screen, fireEvent } from '@testing-library/react';
import App from './App';

describe('Controlled Input', () => {
  test('displays empty input initially', () => {
    render(<App />);
    const input = screen.getByPlaceholderText(/type something/i);
    expect(input.value).toBe('');
  });

  test('updates display when typing', () => {
    render(<App />);
    const input = screen.getByPlaceholderText(/type something/i);
    fireEvent.change(input, { target: { value: 'Hello' } });
    expect(screen.getByText(/you typed:/i).textContent).toContain('Hello');
  });

  test('shows correct character count', () => {
    render(<App />);
    const input = screen.getByPlaceholderText(/type something/i);
    fireEvent.change(input, { target: { value: 'Hello' } });
    expect(screen.getByText(/character count:/i).textContent).toContain('5');
  });

  test('clears input when Clear button is clicked', () => {
    render(<App />);
    const input = screen.getByPlaceholderText(/type something/i);
    fireEvent.change(input, { target: { value: 'Hello' } });
    fireEvent.click(screen.getByText(/clear/i));
    expect(input.value).toBe('');
  });
});
