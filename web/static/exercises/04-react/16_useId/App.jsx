import { useId, useState } from 'react';
import './styles.css';

// TODO: Create a reusable FormField component
// It should:
// - Use useId() to generate a unique ID
// - Associate the label with the input using htmlFor and id
// - Support different input types
// - Include aria-describedby for the hint text
function FormField({ label, type = 'text', hint, value, onChange }) {
  // TODO: Generate unique IDs for input and hint
  // const id = useId();
  // Use `${id}-input` for the input
  // Use `${id}-hint` for the hint paragraph

  return (
    <div className="form-field">
      <label
        // TODO: Add htmlFor attribute
      >
        {label}
      </label>
      <input
        // TODO: Add id attribute
        // TODO: Add aria-describedby pointing to hint
        type={type}
        value={value}
        onChange={onChange}
      />
      {hint && (
        <p
          // TODO: Add id for aria-describedby reference
          className="hint"
        >
          {hint}
        </p>
      )}
    </div>
  );
}

export default function App() {
  const [formData, setFormData] = useState({
    firstName: '',
    lastName: '',
    email: '',
    password: '',
  });

  const handleChange = (field) => (e) => {
    setFormData((prev) => ({ ...prev, [field]: e.target.value }));
  };

  return (
    <div className="container">
      <h1>useId for Accessibility</h1>

      <form className="form" onSubmit={(e) => e.preventDefault()}>
        <FormField
          label="First Name"
          value={formData.firstName}
          onChange={handleChange('firstName')}
          hint="Enter your given name"
        />

        <FormField
          label="Last Name"
          value={formData.lastName}
          onChange={handleChange('lastName')}
          hint="Enter your family name"
        />

        <FormField
          label="Email"
          type="email"
          value={formData.email}
          onChange={handleChange('email')}
          hint="We'll never share your email"
        />

        <FormField
          label="Password"
          type="password"
          value={formData.password}
          onChange={handleChange('password')}
          hint="Must be at least 8 characters"
        />

        <button type="submit" className="submit-btn">
          Submit
        </button>
      </form>

      <div className="explanation">
        <p><strong>Why useId?</strong></p>
        <ul>
          <li>Generates unique IDs that are stable between server and client</li>
          <li>Avoids ID collisions when component is used multiple times</li>
          <li>Essential for accessibility (labels, aria attributes)</li>
        </ul>
        <p><strong>Test it:</strong> Click on any label - it should focus the correct input!</p>
      </div>
    </div>
  );
}
