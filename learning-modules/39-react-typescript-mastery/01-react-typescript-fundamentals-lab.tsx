#!/usr/bin/env npx tsx
/**
 * 🏴‍☠️ REACT + TYPESCRIPT FUNDAMENTALS - HANDS-ON CODING LAB
 * Complete React + TypeScript implementation with real-world examples
 * 
 * This lab covers:
 * - TypeScript fundamentals with React
 * - Component typing and props validation
 * - State management with hooks
 * - Event handling with proper types
 * - Custom hooks creation
 * - Context API with TypeScript
 * - Form handling and validation
 * - API integration with proper typing
 * 
 * Run this lab: npx tsx 01-react-typescript-fundamentals-lab.tsx
 */

import React, { 
  useState, 
  useEffect, 
  useCallback, 
  useMemo, 
  useContext, 
  createContext,
  useRef,
  FormEvent,
  ChangeEvent
} from 'react';
import { createRoot } from 'react-dom/client';

// ============================================================================
// 🎯 SECTION 1: TYPESCRIPT FUNDAMENTALS FOR REACT
// ============================================================================

/**
 * 🔹 BASIC TYPES AND INTERFACES
 * 
 * WHAT THIS TEACHES:
 * - How to define proper TypeScript interfaces for React components
 * - Type safety for props and state
 * - Union types and optional properties
 * 
 * REAL-WORLD USAGE:
 * - Netflix uses similar interfaces for movie/show data
 * - Airbnb uses this pattern for property listings
 * - GitHub uses this for repository and user data
 */

// User interface - represents a user in our application
interface User {
  id: string;
  name: string;
  email: string;
  avatar?: string; // Optional property
  role: 'admin' | 'user' | 'moderator'; // Union type
  preferences: {
    theme: 'light' | 'dark';
    notifications: boolean;
    language: string;
  };
  createdAt: Date;
}

// Post interface - represents a social media post
interface Post {
  id: string;
  title: string;
  content: string;
  author: User;
  tags: string[];
  likes: number;
  comments: Comment[];
  publishedAt: Date;
  isPublished: boolean;
}

// Comment interface - represents a comment on a post
interface Comment {
  id: string;
  content: string;
  author: User;
  postId: string;
  createdAt: Date;
  replies?: Comment[]; // Optional nested comments
}

// API Response wrapper - generic type for API responses
interface ApiResponse<T> {
  data: T;
  status: 'success' | 'error' | 'loading';
  message?: string;
  timestamp: Date;
}

// ============================================================================
// 🎯 SECTION 2: COMPONENT PROPS TYPING
// ============================================================================

/**
 * 🔹 TYPED COMPONENT PROPS
 * 
 * WHAT THIS TEACHES:
 * - How to properly type React component props
 * - Optional vs required props
 * - Function props with proper signatures
 * - Children prop typing
 * 
 * REAL-WORLD USAGE:
 * - Every major React application uses this pattern
 * - Essential for component libraries and design systems
 * - Prevents runtime errors and improves developer experience
 */

// Props for UserCard component
interface UserCardProps {
  user: User;
  showEmail?: boolean; // Optional prop with default
  onUserClick: (userId: string) => void; // Function prop
  onUserEdit?: (user: User) => void; // Optional function prop
  className?: string;
  children?: React.ReactNode; // For nested content
}

// UserCard component with full TypeScript typing
const UserCard: React.FC<UserCardProps> = ({ 
  user, 
  showEmail = false, 
  onUserClick, 
  onUserEdit,
  className = '',
  children 
}) => {
  // Event handler with proper typing
  const handleClick = useCallback(() => {
    onUserClick(user.id);
  }, [user.id, onUserClick]);

  const handleEdit = useCallback(() => {
    if (onUserEdit) {
      onUserEdit(user);
    }
  }, [user, onUserEdit]);

  return (
    <div className={`user-card ${className}`} onClick={handleClick}>
      <div className="user-avatar">
        {user.avatar ? (
          <img src={user.avatar} alt={`${user.name} avatar`} />
        ) : (
          <div className="avatar-placeholder">
            {user.name.charAt(0).toUpperCase()}
          </div>
        )}
      </div>
      
      <div className="user-info">
        <h3>{user.name}</h3>
        <span className="user-role">{user.role}</span>
        {showEmail && <p className="user-email">{user.email}</p>}
        
        {onUserEdit && (
          <button onClick={handleEdit} className="edit-button">
            Edit User
          </button>
        )}
      </div>
      
      {children && <div className="user-card-footer">{children}</div>}
    </div>
  );
};

// ============================================================================
// 🎯 SECTION 3: STATE MANAGEMENT WITH HOOKS
// ============================================================================

/**
 * 🔹 TYPED STATE MANAGEMENT
 * 
 * WHAT THIS TEACHES:
 * - useState with proper TypeScript typing
 * - Complex state objects with interfaces
 * - State update patterns that maintain type safety
 * - useEffect with cleanup and dependencies
 * 
 * REAL-WORLD USAGE:
 * - Discord uses similar patterns for chat state
 * - Spotify uses this for player state management
 * - Slack uses this for workspace and channel state
 */

// Application state interface
interface AppState {
  users: User[];
  posts: Post[];
  currentUser: User | null;
  loading: boolean;
  error: string | null;
  filters: {
    searchTerm: string;
    selectedTags: string[];
    sortBy: 'date' | 'likes' | 'title';
    sortOrder: 'asc' | 'desc';
  };
}

// Initial state
const initialState: AppState = {
  users: [],
  posts: [],
  currentUser: null,
  loading: false,
  error: null,
  filters: {
    searchTerm: '',
    selectedTags: [],
    sortBy: 'date',
    sortOrder: 'desc'
  }
};

// Main application component with complex state management
const SocialMediaApp: React.FC = () => {
  // Typed state with complex object
  const [state, setState] = useState<AppState>(initialState);
  
  // Individual state pieces for better performance
  const [selectedPost, setSelectedPost] = useState<Post | null>(null);
  const [isModalOpen, setIsModalOpen] = useState<boolean>(false);
  
  // Refs with proper typing
  const searchInputRef = useRef<HTMLInputElement>(null);
  const modalRef = useRef<HTMLDivElement>(null);

  // ============================================================================
  // 🎯 SECTION 4: CUSTOM HOOKS WITH TYPESCRIPT
  // ============================================================================

  /**
   * 🔹 CUSTOM HOOKS
   * 
   * WHAT THIS TEACHES:
   * - Creating reusable logic with custom hooks
   * - Proper return type annotations
   * - Generic hooks for flexibility
   * - Hook composition patterns
   */

  // Custom hook for API calls with proper typing
  const useApi = <T,>(url: string, dependencies: any[] = []) => {
    const [data, setData] = useState<T | null>(null);
    const [loading, setLoading] = useState<boolean>(true);
    const [error, setError] = useState<string | null>(null);

    useEffect(() => {
      const fetchData = async () => {
        try {
          setLoading(true);
          setError(null);
          
          // Simulate API call
          await new Promise(resolve => setTimeout(resolve, 1000));
          
          // Mock data based on URL
          let mockData: any;
          if (url.includes('users')) {
            mockData = generateMockUsers(5);
          } else if (url.includes('posts')) {
            mockData = generateMockPosts(10);
          }
          
          setData(mockData);
        } catch (err) {
          setError(err instanceof Error ? err.message : 'An error occurred');
        } finally {
          setLoading(false);
        }
      };

      fetchData();
    }, [url, ...dependencies]);

    return { data, loading, error, refetch: () => fetchData() };
  };

  // Custom hook for local storage with TypeScript
  const useLocalStorage = <T,>(key: string, initialValue: T) => {
    const [storedValue, setStoredValue] = useState<T>(() => {
      try {
        const item = window.localStorage.getItem(key);
        return item ? JSON.parse(item) : initialValue;
      } catch (error) {
        console.error(`Error reading localStorage key "${key}":`, error);
        return initialValue;
      }
    });

    const setValue = useCallback((value: T | ((val: T) => T)) => {
      try {
        const valueToStore = value instanceof Function ? value(storedValue) : value;
        setStoredValue(valueToStore);
        window.localStorage.setItem(key, JSON.stringify(valueToStore));
      } catch (error) {
        console.error(`Error setting localStorage key "${key}":`, error);
      }
    }, [key, storedValue]);

    return [storedValue, setValue] as const;
  };

  // Using custom hooks
  const { data: users, loading: usersLoading } = useApi<User[]>('/api/users');
  const { data: posts, loading: postsLoading } = useApi<Post[]>('/api/posts');
  const [userPreferences, setUserPreferences] = useLocalStorage('userPrefs', {
    theme: 'light' as const,
    autoSave: true
  });

  // ============================================================================
  // 🎯 SECTION 5: EVENT HANDLING WITH PROPER TYPES
  // ============================================================================

  /**
   * 🔹 TYPED EVENT HANDLERS
   * 
   * WHAT THIS TEACHES:
   * - Proper event type annotations
   * - Form handling with TypeScript
   * - Preventing default behavior safely
   * - Event delegation patterns
   */

  // Search handler with proper event typing
  const handleSearch = useCallback((event: ChangeEvent<HTMLInputElement>) => {
    const searchTerm = event.target.value;
    
    setState(prevState => ({
      ...prevState,
      filters: {
        ...prevState.filters,
        searchTerm
      }
    }));
  }, []);

  // Form submission with proper typing
  const handleFormSubmit = useCallback((event: FormEvent<HTMLFormElement>) => {
    event.preventDefault();
    
    const formData = new FormData(event.currentTarget);
    const title = formData.get('title') as string;
    const content = formData.get('content') as string;
    
    if (!title || !content) {
      setState(prev => ({ ...prev, error: 'Title and content are required' }));
      return;
    }

    // Create new post logic here
    console.log('Creating post:', { title, content });
  }, []);

  // User selection handler
  const handleUserSelect = useCallback((userId: string) => {
    const user = users?.find(u => u.id === userId);
    if (user) {
      setState(prev => ({ ...prev, currentUser: user }));
    }
  }, [users]);

  return (
    <div className="social-media-app">
      <header className="app-header">
        <h1>🏴‍☠️ Social Media Dashboard</h1>
        <div className="search-container">
          <input
            ref={searchInputRef}
            type="text"
            placeholder="Search posts..."
            value={state.filters.searchTerm}
            onChange={handleSearch}
            className="search-input"
          />
        </div>
      </header>

      <main className="app-main">
        {usersLoading || postsLoading ? (
          <div className="loading">Loading...</div>
        ) : (
          <div className="content-grid">
            <aside className="sidebar">
              <h2>Users</h2>
              {users?.map(user => (
                <UserCard
                  key={user.id}
                  user={user}
                  onUserClick={handleUserSelect}
                  showEmail={state.currentUser?.role === 'admin'}
                />
              ))}
            </aside>

            <section className="main-content">
              <h2>Posts</h2>
              <form onSubmit={handleFormSubmit} className="post-form">
                <input
                  name="title"
                  type="text"
                  placeholder="Post title..."
                  required
                />
                <textarea
                  name="content"
                  placeholder="What's on your mind?"
                  required
                />
                <button type="submit">Create Post</button>
              </form>

              {state.error && (
                <div className="error-message">{state.error}</div>
              )}

              <div className="posts-list">
                {posts?.map(post => (
                  <article key={post.id} className="post-card">
                    <h3>{post.title}</h3>
                    <p>{post.content}</p>
                    <div className="post-meta">
                      <span>By: {post.author.name}</span>
                      <span>Likes: {post.likes}</span>
                      <span>Comments: {post.comments.length}</span>
                    </div>
                  </article>
                ))}
              </div>
            </section>
          </div>
        )}
      </main>
    </div>
  );
};

// ============================================================================
// 🎯 SECTION 6: CONTEXT API WITH TYPESCRIPT
// ============================================================================

/**
 * 🔹 TYPED CONTEXT API
 *
 * WHAT THIS TEACHES:
 * - Creating type-safe context providers
 * - Context value interfaces
 * - Custom context hooks
 * - Provider composition patterns
 *
 * REAL-WORLD USAGE:
 * - Theme providers in design systems
 * - Authentication context in apps
 * - Shopping cart context in e-commerce
 */

// Theme context interface
interface ThemeContextType {
  theme: 'light' | 'dark';
  toggleTheme: () => void;
  colors: {
    primary: string;
    secondary: string;
    background: string;
    text: string;
  };
}

// Create context with proper typing
const ThemeContext = createContext<ThemeContextType | undefined>(undefined);

// Custom hook to use theme context
const useTheme = (): ThemeContextType => {
  const context = useContext(ThemeContext);
  if (!context) {
    throw new Error('useTheme must be used within a ThemeProvider');
  }
  return context;
};

// Theme provider component
const ThemeProvider: React.FC<{ children: React.ReactNode }> = ({ children }) => {
  const [theme, setTheme] = useState<'light' | 'dark'>('light');

  const toggleTheme = useCallback(() => {
    setTheme(prev => prev === 'light' ? 'dark' : 'light');
  }, []);

  const colors = useMemo(() => ({
    primary: theme === 'light' ? '#007bff' : '#0d6efd',
    secondary: theme === 'light' ? '#6c757d' : '#6c757d',
    background: theme === 'light' ? '#ffffff' : '#1a1a1a',
    text: theme === 'light' ? '#333333' : '#ffffff'
  }), [theme]);

  const value: ThemeContextType = {
    theme,
    toggleTheme,
    colors
  };

  return (
    <ThemeContext.Provider value={value}>
      {children}
    </ThemeContext.Provider>
  );
};

// ============================================================================
// 🎯 SECTION 7: UTILITY FUNCTIONS AND HELPERS
// ============================================================================

/**
 * 🔹 UTILITY FUNCTIONS WITH TYPESCRIPT
 *
 * WHAT THIS TEACHES:
 * - Generic utility functions
 * - Type guards and type predicates
 * - Array manipulation with proper typing
 * - Date formatting and validation
 */

// Generic utility function for array filtering
const filterByProperty = <T, K extends keyof T>(
  array: T[],
  property: K,
  value: T[K]
): T[] => {
  return array.filter(item => item[property] === value);
};

// Type guard function
const isUser = (obj: any): obj is User => {
  return obj &&
         typeof obj.id === 'string' &&
         typeof obj.name === 'string' &&
         typeof obj.email === 'string' &&
         typeof obj.role === 'string';
};

// Mock data generators with proper typing
const generateMockUsers = (count: number): User[] => {
  const users: User[] = [];
  const roles: User['role'][] = ['admin', 'user', 'moderator'];
  const themes: User['preferences']['theme'][] = ['light', 'dark'];

  for (let i = 0; i < count; i++) {
    users.push({
      id: `user-${i + 1}`,
      name: `User ${i + 1}`,
      email: `user${i + 1}@example.com`,
      avatar: `https://api.dicebear.com/7.x/avataaars/svg?seed=${i}`,
      role: roles[Math.floor(Math.random() * roles.length)],
      preferences: {
        theme: themes[Math.floor(Math.random() * themes.length)],
        notifications: Math.random() > 0.5,
        language: 'en'
      },
      createdAt: new Date(Date.now() - Math.random() * 365 * 24 * 60 * 60 * 1000)
    });
  }

  return users;
};

const generateMockPosts = (count: number): Post[] => {
  const posts: Post[] = [];
  const users = generateMockUsers(3);
  const tags = ['react', 'typescript', 'javascript', 'web-dev', 'frontend'];

  for (let i = 0; i < count; i++) {
    posts.push({
      id: `post-${i + 1}`,
      title: `Post Title ${i + 1}`,
      content: `This is the content for post ${i + 1}. It contains some interesting information about web development.`,
      author: users[Math.floor(Math.random() * users.length)],
      tags: tags.slice(0, Math.floor(Math.random() * 3) + 1),
      likes: Math.floor(Math.random() * 100),
      comments: [],
      publishedAt: new Date(Date.now() - Math.random() * 30 * 24 * 60 * 60 * 1000),
      isPublished: true
    });
  }

  return posts;
};
