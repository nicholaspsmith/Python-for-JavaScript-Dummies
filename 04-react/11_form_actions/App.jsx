import { useActionState } from 'react';
import './styles.css';

// Simulated server action
async function submitForm(prevState, formData) {
  // Simulate network delay
  await new Promise(resolve => setTimeout(resolve, 1000));

  const name = formData.get('name');
  const email = formData.get('email');

  // Validate
  if (!name || name.length < 2) {
    return { error: 'Name must be at least 2 characters' };
  }
  if (!email || !email.includes('@')) {
    return { error: 'Please enter a valid email' };
  }

  // Success
  return { success: true, message: `Thanks, ${name}! We'll contact you at ${email}` };
}

export default function App() {
  // TODO: Use useActionState to manage form state
  // const [state, formAction, isPending] = useActionState(submitForm, null);

  return (
    <div className="form-container">
      <h1>Contact Form</h1>
      <p className="subtitle">React 19 Form Actions Demo</p>

      {/* TODO: Add action={formAction} to the form */}
      <form>
        <div className="form-group">
          <label htmlFor="name">Name</label>
          <input
            type="text"
            id="name"
            name="name"
            placeholder="Your name"
            required
            // TODO: Disable when pending
          />
        </div>

        <div className="form-group">
          <label htmlFor="email">Email</label>
          <input
            type="email"
            id="email"
            name="email"
            placeholder="your@email.com"
            required
            // TODO: Disable when pending
          />
        </div>

        {/* TODO: Show error message if state.error */}

        {/* TODO: Show success message if state.success */}

        <button type="submit">
          {/* Show "Submitting..." when pending, "Submit" otherwise */}
          Submit
        </button>
      </form>
    </div>
  );
}
