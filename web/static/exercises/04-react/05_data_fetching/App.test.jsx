import { render, screen, waitFor, fireEvent } from '@testing-library/react';
import App from './App';

describe('Data Fetching', () => {
  test('shows loading state initially', () => {
    render(<App />);
    expect(screen.getByText(/loading/i)).toBeInTheDocument();
  });

  test('displays user data after loading', async () => {
    render(<App />);
    await waitFor(() => {
      expect(screen.getByText(/john doe/i)).toBeInTheDocument();
    }, { timeout: 2000 });
    expect(screen.getByText(/john@example.com/i)).toBeInTheDocument();
  });

  test('has a refresh button', async () => {
    render(<App />);
    await waitFor(() => {
      expect(screen.getByText(/refresh/i)).toBeInTheDocument();
    }, { timeout: 2000 });
  });

  test('shows loading when refresh is clicked', async () => {
    render(<App />);
    await waitFor(() => {
      expect(screen.getByText(/john doe/i)).toBeInTheDocument();
    }, { timeout: 2000 });

    fireEvent.click(screen.getByText(/refresh/i));
    expect(screen.getByText(/loading/i)).toBeInTheDocument();
  });
});
