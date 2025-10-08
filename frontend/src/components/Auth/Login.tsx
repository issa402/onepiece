/*
🏴‍☠️ LOGIN COMPONENT - LEARN BY CODING
═══════════════════════════════════════════════════════════

🎯 WHAT YOU'LL LEARN BY CODING THIS:
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
✅ Authentication form handling and validation
✅ JWT token management and storage
✅ Protected routes and authentication context
✅ Password security and input validation
✅ Error handling for authentication failures
✅ User session management

📚 AUTHENTICATION PATTERNS YOU'LL USE:
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

1. FORM VALIDATION:
   const validateEmail = (email: string) => {
     const emailRegex = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;
     return emailRegex.test(email);
   };

2. JWT TOKEN STORAGE:
   localStorage.setItem('token', response.data.token);
   const token = localStorage.getItem('token');

3. AUTHENTICATION CONTEXT:
   const { login, user, isAuthenticated } = useAuth();

4. PASSWORD SECURITY:
   const [showPassword, setShowPassword] = useState(false);

🔧 TYPESCRIPT INTERFACES YOU'LL NEED:
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

interface LoginForm {
  email: string;
  password: string;
  remember_me: boolean;
}

interface AuthResponse {
  success: boolean;
  token?: string;
  user?: User;
  message?: string;
}

interface User {
  id: number;
  email: string;
  username: string;
  balance: number;
}
*/

/*
🧪 HANDS-ON LAB 1: AUTHENTICATION IMPORTS
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

📚 WHAT EACH IMPORT DOES:
• React hooks: useState for form state
• useNavigate: Redirect after successful login
• axios: API calls for authentication
• Link: Navigation to registration page

🎯 YOUR TASK: Import authentication dependencies
*/

// TODO 1: IMPORT STATEMENTS
// YOUR CODE HERE - Import React hooks:


// YOUR CODE HERE - Import React Router hooks:


// YOUR CODE HERE - Import axios:


// YOUR CODE HERE - Import CSS:


/*
🧪 HANDS-ON LAB 2: AUTHENTICATION INTERFACES
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

📚 AUTHENTICATION DATA STRUCTURE:
• LoginForm: User's login credentials
• AuthResponse: API response from login
• User: User profile information

🎯 YOUR TASK: Define authentication interfaces
*/

// TODO 2: TYPESCRIPT INTERFACES
// YOUR CODE HERE - Define LoginForm interface:


// YOUR CODE HERE - Define AuthResponse interface:


// YOUR CODE HERE - Define User interface:


/*
🧪 HANDS-ON LAB 3: LOGIN STATE MANAGEMENT
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

📚 LOGIN STATE:
• loginForm: User's input credentials
• isSubmitting: Prevent double submissions
• error: Display authentication errors
• showPassword: Toggle password visibility

🎯 YOUR TASK: Set up login state
*/

// TODO 3: COMPONENT DECLARATION AND STATE
// YOUR CODE HERE - Create Login component and state:


/*
🧪 HANDS-ON LAB 4: FORM VALIDATION
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

📚 LOGIN VALIDATION:
• Email format validation
• Password strength requirements
• Required field validation
• Real-time validation feedback

🎯 YOUR TASK: Create validation functions
*/

// TODO 4: VALIDATION FUNCTIONS
// YOUR CODE HERE - Create validateForm function:


// YOUR CODE HERE - Create validateEmail function:


/*
🧪 HANDS-ON LAB 5: AUTHENTICATION LOGIC
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

📚 LOGIN PROCESS:
• Submit credentials to API
• Handle JWT token response
• Store token in localStorage
• Redirect to dashboard

🎯 YOUR TASK: Handle authentication
*/

// TODO 5: AUTHENTICATION FUNCTIONS
// YOUR CODE HERE - Create handleLogin function:


// TODO 6: FORM HANDLERS
// YOUR CODE HERE - Create form change and submit handlers:


/*
🧪 HANDS-ON LAB 6: LOGIN UI
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

📚 LOGIN INTERFACE:
• Email and password inputs
• Password visibility toggle
• Remember me checkbox
• Submit button with loading state
• Registration link

🎯 YOUR TASK: Render login interface
*/

// TODO 7: COMPONENT RETURN/RENDER
// YOUR CODE HERE - Return JSX with login UI:


// TODO 8: EXPORT COMPONENT
// YOUR CODE HERE - Export the Login component:


/*
═══════════════════════════════════════════════════════════
🏆 COMPLETE CODE SOLUTION (SCROLL DOWN TO CHECK YOUR WORK)
═══════════════════════════════════════════════════════════

import React, { useState } from 'react';
import { Link, useNavigate } from 'react-router-dom';
import axios from 'axios';
import './Login.css';

interface LoginForm {
  email: string;
  password: string;
  remember_me: boolean;
}

interface AuthResponse {
  success: boolean;
  token?: string;
  user?: User;
  message?: string;
}

interface User {
  id: number;
  email: string;
  username: string;
  balance: number;
  created_at: string;
}

const Login: React.FC = () => {
  const [loginForm, setLoginForm] = useState<LoginForm>({
    email: '',
    password: '',
    remember_me: false
  });

  const [isSubmitting, setIsSubmitting] = useState<boolean>(false);
  const [error, setError] = useState<string | null>(null);
  const [showPassword, setShowPassword] = useState<boolean>(false);

  const navigate = useNavigate();

  const validateEmail = (email: string): boolean => {
    const emailRegex = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;
    return emailRegex.test(email);
  };

  const validateForm = (form: LoginForm): string | null => {
    if (!form.email.trim()) {
      return 'Email is required';
    }

    if (!validateEmail(form.email)) {
      return 'Please enter a valid email address';
    }

    if (!form.password) {
      return 'Password is required';
    }

    if (form.password.length < 6) {
      return 'Password must be at least 6 characters long';
    }

    return null;
  };

  const handleLogin = async (credentials: LoginForm): Promise<AuthResponse> => {
    try {
      const response = await axios.post('http://localhost:5000/api/auth/login', {
        email: credentials.email,
        password: credentials.password
      });

      const { token, user } = response.data;

      // Store JWT token
      if (credentials.remember_me) {
        localStorage.setItem('token', token);
        localStorage.setItem('user', JSON.stringify(user));
      } else {
        sessionStorage.setItem('token', token);
        sessionStorage.setItem('user', JSON.stringify(user));
      }

      // Set default authorization header for future requests
      axios.defaults.headers.common['Authorization'] = `Bearer ${token}`;

      return {
        success: true,
        token,
        user,
        message: 'Login successful'
      };
    } catch (err: any) {
      return {
        success: false,
        message: err.response?.data?.message || 'Login failed. Please try again.'
      };
    }
  };

  const handleFormChange = (e: React.ChangeEvent<HTMLInputElement>) => {
    const { name, value, type, checked } = e.target;
    setLoginForm(prev => ({
      ...prev,
      [name]: type === 'checkbox' ? checked : value
    }));

    // Clear error when user starts typing
    if (error) {
      setError(null);
    }
  };

  const handleSubmit = async (e: React.FormEvent) => {
    e.preventDefault();

    const validationError = validateForm(loginForm);
    if (validationError) {
      setError(validationError);
      return;
    }

    setIsSubmitting(true);
    setError(null);

    const result = await handleLogin(loginForm);

    if (result.success) {
      // Redirect to dashboard or previous page
      const redirectTo = new URLSearchParams(window.location.search).get('redirect') || '/dashboard';
      navigate(redirectTo);
    } else {
      setError(result.message || 'Login failed');
    }

    setIsSubmitting(false);
  };

  const togglePasswordVisibility = () => {
    setShowPassword(prev => !prev);
  };

  return (
    <div className="login-page">
      <div className="login-container">
        <div className="login-header">
          <h1>🏴‍☠️ One Piece Stock Market</h1>
          <h2>Welcome Back, Pirate!</h2>
          <p>Sign in to your trading account</p>
        </div>

        <form onSubmit={handleSubmit} className="login-form">
          {error && (
            <div className="error-message">
              {error}
            </div>
          )}

          <div className="form-group">
            <label htmlFor="email">Email Address</label>
            <input
              type="email"
              id="email"
              name="email"
              value={loginForm.email}
              onChange={handleFormChange}
              placeholder="Enter your email"
              required
              autoComplete="email"
            />
          </div>

          <div className="form-group">
            <label htmlFor="password">Password</label>
            <div className="password-input-container">
              <input
                type={showPassword ? 'text' : 'password'}
                id="password"
                name="password"
                value={loginForm.password}
                onChange={handleFormChange}
                placeholder="Enter your password"
                required
                autoComplete="current-password"
              />
              <button
                type="button"
                className="password-toggle"
                onClick={togglePasswordVisibility}
                aria-label={showPassword ? 'Hide password' : 'Show password'}
              >
                {showPassword ? '👁️' : '👁️‍🗨️'}
              </button>
            </div>
          </div>

          <div className="form-options">
            <label className="checkbox-label">
              <input
                type="checkbox"
                name="remember_me"
                checked={loginForm.remember_me}
                onChange={handleFormChange}
              />
              <span className="checkmark"></span>
              Remember me
            </label>

            <Link to="/forgot-password" className="forgot-password-link">
              Forgot password?
            </Link>
          </div>

          <button
            type="submit"
            className="login-button"
            disabled={isSubmitting}
          >
            {isSubmitting ? (
              <>
                <span className="loading-spinner"></span>
                Signing in...
              </>
            ) : (
              'Sign In'
            )}
          </button>
        </form>

        <div className="login-footer">
          <p>
            Don't have an account?{' '}
            <Link to="/register" className="register-link">
              Create one here
            </Link>
          </p>

          <div className="demo-credentials">
            <h4>Demo Account:</h4>
            <p>Email: demo@onepiece.com</p>
            <p>Password: luffy123</p>
          </div>
        </div>
      </div>

      <div className="login-background">
        <div className="floating-berry">₿</div>
        <div className="floating-berry">₿</div>
        <div className="floating-berry">₿</div>
      </div>
    </div>
  );
};

export default Login;

*/