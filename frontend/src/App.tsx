/*
🏴‍☠️ SRE MASTERY: REACT FRONTEND RESILIENCE BLUEPRINT
═══════════════════════════════════════════════════════════

🎯 LEARNING OBJECTIVES - BECOME A FRONTEND SRE EXPERT:
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
✅ Master React error boundaries for fault tolerance
✅ Implement client-side circuit breaker patterns
✅ Learn performance monitoring and Core Web Vitals
✅ Practice progressive loading and graceful degradation
✅ Understand client-side caching and offline strategies
✅ Implement comprehensive error handling and user feedback

📖 FRONTEND SRE THEORY: CLIENT-SIDE RELIABILITY
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
Frontend reliability challenges and solutions:

1. 🚨 ERROR BOUNDARIES - Catch and handle component crashes
2. 🔄 RETRY LOGIC - Automatic retry for failed API calls
3. 📊 PERFORMANCE MONITORING - Track Core Web Vitals
4. 💾 OFFLINE SUPPORT - Service workers and caching
5. 🎯 PROGRESSIVE LOADING - Skeleton screens and lazy loading
6. 🔒 SECURITY - XSS protection and input validation

🔧 REAL-WORLD FRONTEND SRE CONNECTION:
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
This frontend architecture implements patterns used by:
• Netflix: Error boundaries and progressive loading
• Facebook: React error boundaries and performance monitoring
• Google: Core Web Vitals optimization and offline-first design
• Airbnb: Client-side circuit breakers and retry logic
• Spotify: Real-time updates with graceful degradation

📊 INDUSTRY SALARY IMPACT:
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
Frontend SRE expertise increases salary potential:
• Frontend Engineer: $85K-$160K (performance optimization)
• Full-Stack Engineer: $95K-$180K (end-to-end reliability)
• SRE Engineer: $122K-$204K (frontend monitoring and observability)
*/

/*
🧪 HANDS-ON LAB 1: FRONTEND SRE IMPORTS & DEPENDENCIES
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

📚 THEORY: React SRE Import Strategy

Core React Imports:
• React: Base library for component creation
• useState: Local state management for UI state
• useEffect: Side effects and lifecycle management
• useCallback: Performance optimization (memoization)
• useMemo: Expensive computation caching
• ErrorBoundary: Catch and handle component errors

Routing & Navigation:
• BrowserRouter: Client-side routing foundation
• Routes/Route: Declarative route configuration
• Navigate: Programmatic navigation
• useNavigate: Hook for navigation in components

HTTP Client & Error Handling:
• axios: HTTP client with interceptors and retry logic
• axios-retry: Automatic retry for failed requests

Performance & Monitoring:
• web-vitals: Core Web Vitals measurement
• react-error-boundary: Enhanced error boundaries

🔧 SRE PATTERN: Defensive Imports
Import only what you need to minimize bundle size and attack surface
*/




import React, {
  useState,
  useEffect,
  useCallback,
  useMemo,
  createContext,
  useContext
} from 'react';
import {
  BrowserRouter as Router,
  Routes,
  Route,
  Navigate,
  useNavigate
} from 'react-router-dom';
import axios, { AxiosError, AxiosResponse } from 'axios';
import { ErrorBoundary } from 'react-error-boundary';
import { getCLS, getFID, getFCP, getLCP, getTTFB } from 'web-vitals';
import './App.css';
// 
// // Import your components (you'll create these)
// import Header from './components/Header/Header';
// import Dashboard from './components/Dashboard/Dashboard';
// import CharacterList from './components/Characters/CharacterList';
// import CharacterDetail from './components/Characters/CharacterDetail';
// import Portfolio from './components/Portfolio/Portfolio';
// import Trading from './components/Trading/Trading';
// import Login from './components/Auth/Login';
// import Register from './components/Auth/Register';
// import { AuthProvider, useAuth } from './contexts/AuthContext';
// import { ApiProvider } from './contexts/ApiContext';

// WRITE YOUR IMPORTS HERE:
import Header from './components/Header/Header';
import Dashboard from './components/Dashboard/Dashboard';
import CharacterList from './components/Characters/CharacterList';
import CharacterDetail from './components/CharacterDetail/CharacterDetail';
import Portfolio from './components/Portfolio/Portfolio';
import Trading from './components/Trading/Trading';
import Login from './components/Auth/Login';
import {AuthProvider, useAuth} from './contexts/AuthContext';
import {ApiProvider} from './contexts/ApiContext';

/*
🧪 HANDS-ON LAB 2: TYPESCRIPT INTERFACES FOR TYPE SAFETY
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

📚 THEORY: TypeScript in SRE Context

Type Safety Benefits:
✅ Catch errors at compile time (not runtime)
✅ Better IDE support and autocomplete
✅ Self-documenting code with interfaces
✅ Refactoring safety across large codebases
✅ API contract enforcement

🔧 SRE BEST PRACTICE: Strict Type Checking
• Use strict mode in tsconfig.json
• Define interfaces for all API responses
• Use union types for error states
• Implement discriminated unions for state management

🏢 INDUSTRY USAGE:
• Microsoft: TypeScript creator, uses extensively
• Slack: Migrated entire codebase to TypeScript
• Airbnb: Uses TypeScript for type safety at scale
*/

// Core domain interfaces with comprehensive type safety
interface Character {
  id: number;
  name: string;
  crew: string;
  bounty: number;
  current_price: number;
  market_cap: number;
  sentiment_score: number;
  weekly_change: number;
  description: string;
  image_url?: string;
  is_active: boolean;
  created_at: string;
  updated_at: string;
}




// 
// interface User {
//   id: number;
//   username: string;
//   email: string;
//   balance: number;
//   first_name?: string;
//   last_name?: string;
// }
// 
// interface PortfolioHolding {
//   character_id: number;
//   character_name: string;
//   crew: string;
//   quantity: number;
//   average_price: number;
//   current_price: number;
//   total_invested: number;
//   current_value: number;
//   gain_loss: number;
//   gain_loss_percentage: number;
// }

// TODO 3: PROTECTED ROUTE COMPONENT
// Create a component to protect authenticated routes:
// 
// const ProtectedRoute: React.FC<{ children: React.ReactNode }> = ({ children }) => {
//   // Get authentication status from context
//   // const { isAuthenticated, loading } = useAuth();
//   
//   // Show loading spinner while checking auth
//   // if (loading) return <div>Loading...</div>;
//   
//   // Redirect to login if not authenticated
//   // return isAuthenticated ? <>{children}</> : <Navigate to="/login" />;
// };
const ProtectedRoute: React.FC<{ children: React.ReactNode }> = ({ children }) => {
  const{ isAuthenticated, loading} = useAuth();

  if (loading) return <div> Loading...</div>;

  return isAuthenticated ? <> {children}</> : <Navigate to = "/login" />;
}
// TODO 4: MAIN APP COMPONENT
// function App(): JSX.Element {
//   // State for global app data
//   // const [characters, setCharacters] = useState<Character[]>([]);
//   // const [loading, setLoading] = useState<boolean>(true);
//   // const [error, setError] = useState<string | null>(null);

function App(): JSX.Element {
  const [characters, setCharacters] = useState<Character[]>([]);
  const[loading, setloading] = useState<boolean>(true);
  const[error, setError] = useState<string | null>(null);
}

//   // Load initial data when app starts
//   // useEffect(() => {
//   //   loadInitialData();
//   // }, []);
useEffect(() => {
  loadInitialData();
}, []);
//   // Function to load characters and market data
//   // const loadInitialData = async () => {
//   //   try {
//   //     setLoading(true);
//   //     // Fetch characters from API
//   //     // const response = await axios.get('/api/characters');
//   //     // setCharacters(response.data.characters);
//   //   } catch (err) {
//   //     // Handle errors
//   //     // setError('Failed to load market data');
//   //   } finally {
//   //     // setLoading(false);
//   //   }
//   // };
const loadInitialData = async() => {
  try {
    setLoading(true);
    cosnt response = await axios.get('/api/characters');
    setCharacters(response.data.characters);
  } catch (err) {
    setError('Failed to load market data');
  } finally {
    setloading(false);
  }
};

return(
  <AuthProvider>
    <ApiProvider>
      <Router>
        <div className = "App">
          <Header/>
          <main className = "main-content">
            <Routes>
              <Route path = "/login" element = {<Login />} />
              <Route path = "/register" element = {<Register />} />

              <Route path = "/" element = {
                <ProtectedRoute>
                  <Dashboard/>
                </ProtectedRoute>
              }/>
              <Route path = "/characters" element = {
                <ProtectedRoute>
                  <Dashboard/>
                </ProtectedRoute>
              }/>
              <Route path = "/characters/:id" element = {
                <ProtectedRoute>
                  <CharacterDetail/>
                </ProtectedRoute>
              }/>
              <Route path = "portfolio" element = {
                <ProtectedRoute>
                  <Portfolio/>
                </ProtectedRoute>
              }/>
              <Route path = "trading" element = {
                <ProtectedRoute>
                  <Trading/>
                </ProtectedRoute>
              }/>
              <Route path = "*" element = {<Navigate to = "/" />} />
            </Routes>
          </main>
        </div>
      </Router>
    </ApiProvider>
  </AuthProvider>
);


// TODO 5: RENDER METHOD WITH ROUTING
//   return (
//     <AuthProvider>
//       <ApiProvider>
//         <Router>
//           <div className="App">
//             {/* Header component with navigation */}
//             <Header />
//             
//             {/* Main content area */}
//             <main className="main-content">
//               <Routes>
//                 {/* Public routes */}
//                 <Route path="/login" element={<Login />} />
//                 <Route path="/register" element={<Register />} />
//                 
//                 {/* Protected routes */}
//                 <Route path="/" element={
//                   <ProtectedRoute>
//                     <Dashboard />
//                   </ProtectedRoute>
//                 } />
//                 
//                 <Route path="/characters" element={
//                   <ProtectedRoute>
//                     <CharacterList />
//                   </ProtectedRoute>
//                 } />
//                 
//                 <Route path="/characters/:id" element={
//                   <ProtectedRoute>
//                     <CharacterDetail />
//                   </ProtectedRoute>
//                 } />
//                 
//                 <Route path="/portfolio" element={
//                   <ProtectedRoute>
//                     <Portfolio />
//                   </ProtectedRoute>
//                 } />
//                 
//                 <Route path="/trading" element={
//                   <ProtectedRoute>
//                     <Trading />
//                   </ProtectedRoute>
//                 } />
//                 
//                 {/* Redirect unknown routes to dashboard */}
//                 <Route path="*" element={<Navigate to="/" />} />
//               </Routes>
//             </main>
//           </div>
//         </Router>
//       </ApiProvider>
//     </AuthProvider>
//   );
// }

// TODO 6: EXPORT DEFAULT
// export default App;
export default App;
/*
🎯 WHAT EACH PART DOES:

Interfaces: Define TypeScript types for data structures
ProtectedRoute: Ensures only authenticated users access certain pages
App Component: Main application component with routing
Routes: Define URL paths and corresponding components
Context Providers: Provide global state to all components

🚀 REACT CONCEPTS YOU'LL LEARN:

1. Functional Components - Modern React component style
2. JSX - JavaScript XML for UI templates
3. Props - Data passed between components
4. State - Component data that can change
5. Hooks - useState, useEffect, useContext, etc.
6. Event Handling - onClick, onChange, etc.
7. Conditional Rendering - Show/hide based on state

📚 TYPESCRIPT CONCEPTS:

1. Interfaces - Define object shapes
2. Types - Define data types
3. Generic Types - Reusable type definitions
4. Optional Properties - Properties that may not exist
5. Type Guards - Runtime type checking
6. Strict Type Checking - Catch errors at compile time

🔧 REACT ROUTER CONCEPTS:

1. BrowserRouter - Enables routing in your app
2. Routes - Container for route definitions
3. Route - Individual route configuration
4. Navigate - Programmatic navigation
5. useNavigate - Hook for navigation
6. Protected Routes - Authentication-based routing

COMPONENT HIERARCHY:
App (Main)
├── Header (Navigation)
├── Dashboard (Overview)
├── CharacterList (Browse characters)
├── CharacterDetail (Individual character)
├── Portfolio (User holdings)
├── Trading (Buy/sell interface)
├── Login (Authentication)
└── Register (User signup)

NEXT FILE AFTER THIS: Create Character List Component! 🚀
*/
