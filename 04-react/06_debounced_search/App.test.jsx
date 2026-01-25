import { render, screen, fireEvent, waitFor } from '@testing-library/react';
import { act } from 'react-dom/test-utils';
import App from './App';

describe('Debounced Search', () => {
  beforeEach(() => {
    jest.useFakeTimers();
  });

  afterEach(() => {
    jest.useRealTimers();
  });

  test('shows empty state initially', () => {
    render(<App />);
    expect(screen.getByPlaceholderText(/search/i)).toHaveValue('');
  });

  test('shows searching indicator while debouncing', () => {
    render(<App />);
    fireEvent.change(screen.getByPlaceholderText(/search/i), {
      target: { value: 'app' }
    });
    expect(screen.getByText(/searching/i)).toBeInTheDocument();
  });

  test('shows results after debounce delay', async () => {
    render(<App />);
    fireEvent.change(screen.getByPlaceholderText(/search/i), {
      target: { value: 'app' }
    });

    act(() => {
      jest.advanceTimersByTime(500);
    });

    await waitFor(() => {
      expect(screen.getByText(/apple/i)).toBeInTheDocument();
    });
  });

  test('debounces multiple rapid inputs', () => {
    render(<App />);
    const input = screen.getByPlaceholderText(/search/i);

    fireEvent.change(input, { target: { value: 'a' } });
    act(() => { jest.advanceTimersByTime(200); });

    fireEvent.change(input, { target: { value: 'ap' } });
    act(() => { jest.advanceTimersByTime(200); });

    fireEvent.change(input, { target: { value: 'app' } });

    // Still showing searching because timer reset
    expect(screen.getByText(/searching/i)).toBeInTheDocument();
  });
});
