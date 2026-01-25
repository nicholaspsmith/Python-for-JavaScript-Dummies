import { render, screen, fireEvent } from '@testing-library/react';
import App from './App';

describe('useMemo Calculation', () => {
  beforeEach(() => {
    jest.spyOn(console, 'log').mockImplementation(() => {});
  });

  afterEach(() => {
    console.log.mockRestore();
  });

  test('calculates factorial of initial value', () => {
    render(<App />);
    // Factorial of 5 is 120
    expect(screen.getByText('120')).toBeInTheDocument();
  });

  test('recalculates when number changes', () => {
    render(<App />);
    const input = screen.getByRole('spinbutton');

    console.log.mockClear();
    fireEvent.change(input, { target: { value: '6' } });

    expect(console.log).toHaveBeenCalledWith('Calculating factorial...');
    expect(screen.getByText('720')).toBeInTheDocument();
  });

  test('does NOT recalculate when only counter changes', () => {
    render(<App />);

    console.log.mockClear();
    fireEvent.click(screen.getByText(/increment/i));

    expect(console.log).not.toHaveBeenCalledWith('Calculating factorial...');
  });

  test('counter increments independently', () => {
    render(<App />);
    fireEvent.click(screen.getByText(/increment/i));
    fireEvent.click(screen.getByText(/increment/i));
    expect(screen.getByText('2')).toBeInTheDocument();
  });
});
