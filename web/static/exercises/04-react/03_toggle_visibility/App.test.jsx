import { render, screen, fireEvent } from '@testing-library/react';
import App from './App';

describe('Toggle Visibility', () => {
  test('content is hidden initially', () => {
    render(<App />);
    expect(screen.queryByText(/this content can be toggled/i)).not.toBeInTheDocument();
  });

  test('shows "Show Content" button initially', () => {
    render(<App />);
    expect(screen.getByText(/show content/i)).toBeInTheDocument();
  });

  test('shows content when button is clicked', () => {
    render(<App />);
    fireEvent.click(screen.getByText(/show content/i));
    expect(screen.getByText(/this content can be toggled/i)).toBeInTheDocument();
  });

  test('button changes to "Hide Content" when content is visible', () => {
    render(<App />);
    fireEvent.click(screen.getByText(/show content/i));
    expect(screen.getByText(/hide content/i)).toBeInTheDocument();
  });

  test('hides content when button is clicked again', () => {
    render(<App />);
    fireEvent.click(screen.getByText(/show content/i));
    fireEvent.click(screen.getByText(/hide content/i));
    expect(screen.queryByText(/this content can be toggled/i)).not.toBeInTheDocument();
  });
});
