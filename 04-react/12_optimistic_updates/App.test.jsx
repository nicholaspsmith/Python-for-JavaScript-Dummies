import { render, screen, fireEvent, waitFor } from '@testing-library/react';
import App from './App';

describe('Optimistic Updates', () => {
  test('displays initial like count', () => {
    render(<App />);
    expect(screen.getByText('42')).toBeInTheDocument();
  });

  test('shows optimistic update immediately on click', () => {
    render(<App />);
    fireEvent.click(screen.getByRole('button'));

    // Should immediately show 43 (optimistic update)
    expect(screen.getByText('43')).toBeInTheDocument();
  });

  test('shows pending state while processing', () => {
    render(<App />);
    fireEvent.click(screen.getByRole('button'));

    // Button should be disabled during pending
    expect(screen.getByRole('button')).toBeDisabled();
  });

  test('handles successful update', async () => {
    // Mock Math.random to always succeed
    jest.spyOn(Math, 'random').mockReturnValue(0.5);

    render(<App />);
    fireEvent.click(screen.getByRole('button'));

    await waitFor(() => {
      expect(screen.getByRole('button')).not.toBeDisabled();
    }, { timeout: 2000 });

    expect(screen.getByText('43')).toBeInTheDocument();

    Math.random.mockRestore();
  });

  test('reverts on failure and shows error', async () => {
    // Mock Math.random to always fail
    jest.spyOn(Math, 'random').mockReturnValue(0.1);

    render(<App />);
    fireEvent.click(screen.getByRole('button'));

    await waitFor(() => {
      expect(screen.getByText(/failed/i)).toBeInTheDocument();
    }, { timeout: 2000 });

    // Should revert to original count
    expect(screen.getByText('42')).toBeInTheDocument();

    Math.random.mockRestore();
  });
});
