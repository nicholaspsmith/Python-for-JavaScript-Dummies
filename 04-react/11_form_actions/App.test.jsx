import { render, screen, fireEvent, waitFor } from '@testing-library/react';
import App from './App';

describe('Form Actions', () => {
  test('renders form fields', () => {
    render(<App />);
    expect(screen.getByLabelText(/name/i)).toBeInTheDocument();
    expect(screen.getByLabelText(/email/i)).toBeInTheDocument();
    expect(screen.getByRole('button', { name: /submit/i })).toBeInTheDocument();
  });

  test('shows submitting state when form is submitted', async () => {
    render(<App />);

    fireEvent.change(screen.getByLabelText(/name/i), { target: { value: 'John' } });
    fireEvent.change(screen.getByLabelText(/email/i), { target: { value: 'john@example.com' } });
    fireEvent.click(screen.getByRole('button', { name: /submit/i }));

    expect(screen.getByText(/submitting/i)).toBeInTheDocument();
  });

  test('shows success message on valid submission', async () => {
    render(<App />);

    fireEvent.change(screen.getByLabelText(/name/i), { target: { value: 'John' } });
    fireEvent.change(screen.getByLabelText(/email/i), { target: { value: 'john@example.com' } });
    fireEvent.click(screen.getByRole('button', { name: /submit/i }));

    await waitFor(() => {
      expect(screen.getByText(/thanks, john/i)).toBeInTheDocument();
    }, { timeout: 2000 });
  });

  test('shows error message on invalid email', async () => {
    render(<App />);

    fireEvent.change(screen.getByLabelText(/name/i), { target: { value: 'John' } });
    fireEvent.change(screen.getByLabelText(/email/i), { target: { value: 'invalid' } });
    fireEvent.click(screen.getByRole('button', { name: /submit/i }));

    await waitFor(() => {
      expect(screen.getByText(/valid email/i)).toBeInTheDocument();
    }, { timeout: 2000 });
  });
});
