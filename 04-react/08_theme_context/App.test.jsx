import { render, screen, fireEvent } from '@testing-library/react';
import App from './App';

describe('Theme Context', () => {
  test('displays initial theme', () => {
    render(<App />);
    expect(screen.getByText(/current theme:/i)).toBeInTheDocument();
  });

  test('starts with light theme by default', () => {
    render(<App />);
    expect(screen.getByText(/light/i)).toBeInTheDocument();
  });

  test('toggles to dark theme when button is clicked', () => {
    render(<App />);
    fireEvent.click(screen.getByText(/toggle theme/i));
    expect(screen.getByText(/dark/i)).toBeInTheDocument();
  });

  test('toggles back to light theme', () => {
    render(<App />);
    fireEvent.click(screen.getByText(/toggle theme/i));
    fireEvent.click(screen.getByText(/toggle theme/i));
    expect(screen.getByText(/light/i)).toBeInTheDocument();
  });

  test('applies theme class to card', () => {
    const { container } = render(<App />);
    const card = container.querySelector('.card');
    expect(card).toHaveClass('light');

    fireEvent.click(screen.getByText(/toggle theme/i));
    expect(card).toHaveClass('dark');
  });
});
