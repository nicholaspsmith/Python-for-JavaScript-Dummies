import { render, screen, waitFor } from '@testing-library/react';
import App from './App';

describe('use() Hook', () => {
  test('shows loading skeleton initially', () => {
    render(<App />);
    expect(screen.getByText('⏳')).toBeInTheDocument();
  });

  test('displays user data after loading', async () => {
    render(<App />);

    await waitFor(() => {
      expect(screen.getByText('Jane Doe')).toBeInTheDocument();
    }, { timeout: 2000 });

    expect(screen.getByText('jane@example.com')).toBeInTheDocument();
    expect(screen.getByText('👩‍💻')).toBeInTheDocument();
  });

  test('removes loading skeleton after data loads', async () => {
    render(<App />);

    await waitFor(() => {
      expect(screen.queryByText('⏳')).not.toBeInTheDocument();
    }, { timeout: 2000 });
  });
});
