#!/usr/bin/env npx tsx
/**
 * 🏴‍☠️ REACT + TYPESCRIPT ADVANCED PATTERNS - HANDS-ON CODING LAB
 * Advanced React patterns with TypeScript for production applications
 * 
 * This lab covers:
 * - Advanced TypeScript patterns (generics, conditional types, mapped types)
 * - Higher-Order Components (HOCs) with TypeScript
 * - Render Props pattern with proper typing
 * - Compound Components pattern
 * - Custom hooks with complex logic
 * - Performance optimization patterns
 * - Error boundaries and error handling
 * - Advanced state management patterns
 * 
 * Run this lab: npx tsx 02-advanced-patterns-lab.tsx
 */

import React, { 
  useState, 
  useEffect, 
  useCallback, 
  useMemo, 
  useRef,
  useReducer,
  createContext,
  useContext,
  forwardRef,
  useImperativeHandle,
  ComponentType,
  ReactNode,
  RefObject
} from 'react';
import { createRoot } from 'react-dom/client';

// ============================================================================
// 🎯 SECTION 1: ADVANCED TYPESCRIPT PATTERNS
// ============================================================================

/**
 * 🔹 ADVANCED TYPESCRIPT TYPES
 * 
 * WHAT THIS TEACHES:
 * - Generic constraints and conditional types
 * - Mapped types and utility types
 * - Template literal types
 * - Discriminated unions
 * 
 * REAL-WORLD USAGE:
 * - Type-safe API clients (like tRPC)
 * - Form libraries with dynamic validation
 * - Component libraries with flexible props
 */

// Generic constraint example - only allow objects with id property
type WithId<T> = T & { id: string };

// Conditional type - extract array element type
type ArrayElement<T> = T extends (infer U)[] ? U : never;

// Mapped type - make all properties optional except specified ones
type PartialExcept<T, K extends keyof T> = Partial<T> & Pick<T, K>;

// Template literal type for CSS properties
type CSSProperty = `--${string}`;
type ThemeVariables = Record<CSSProperty, string>;

// Discriminated union for different message types
type Message = 
  | { type: 'text'; content: string; }
  | { type: 'image'; url: string; alt: string; }
  | { type: 'file'; filename: string; size: number; }
  | { type: 'system'; message: string; timestamp: Date; };

// Generic API response with status discrimination
type ApiResponse<T> = 
  | { status: 'loading'; data?: undefined; error?: undefined; }
  | { status: 'success'; data: T; error?: undefined; }
  | { status: 'error'; data?: undefined; error: string; };

// Advanced utility type for component props
type PropsWithOptionalChildren<P = {}> = P & {
  children?: ReactNode;
};

// Extract component props type
type ComponentProps<T> = T extends ComponentType<infer P> ? P : never;

// ============================================================================
// 🎯 SECTION 2: HIGHER-ORDER COMPONENTS (HOCs)
// ============================================================================

/**
 * 🔹 TYPED HIGHER-ORDER COMPONENTS
 * 
 * WHAT THIS TEACHES:
 * - Creating reusable component logic with HOCs
 * - Proper TypeScript typing for HOCs
 * - Props forwarding and ref handling
 * - HOC composition patterns
 * 
 * REAL-WORLD USAGE:
 * - Authentication wrappers
 * - Loading state management
 * - Error boundary wrappers
 * - Analytics tracking
 */

// HOC for adding loading state
interface WithLoadingProps {
  isLoading: boolean;
}

const withLoading = <P extends object>(
  Component: ComponentType<P>
) => {
  const WithLoadingComponent = (props: P & WithLoadingProps) => {
    const { isLoading, ...restProps } = props;
    
    if (isLoading) {
      return (
        <div className="loading-spinner">
          <div className="spinner"></div>
          <p>Loading...</p>
        </div>
      );
    }
    
    return <Component {...(restProps as P)} />;
  };
  
  WithLoadingComponent.displayName = `withLoading(${Component.displayName || Component.name})`;
  
  return WithLoadingComponent;
};

// HOC for error boundary functionality
interface WithErrorBoundaryProps {
  fallback?: ComponentType<{ error: Error; resetError: () => void }>;
}

const withErrorBoundary = <P extends object>(
  Component: ComponentType<P>
) => {
  return class extends React.Component<
    P & WithErrorBoundaryProps,
    { hasError: boolean; error?: Error }
  > {
    constructor(props: P & WithErrorBoundaryProps) {
      super(props);
      this.state = { hasError: false };
    }

    static getDerivedStateFromError(error: Error) {
      return { hasError: true, error };
    }

    componentDidCatch(error: Error, errorInfo: React.ErrorInfo) {
      console.error('Error caught by HOC:', error, errorInfo);
    }

    resetError = () => {
      this.setState({ hasError: false, error: undefined });
    };

    render() {
      if (this.state.hasError) {
        const { fallback: Fallback } = this.props;
        
        if (Fallback && this.state.error) {
          return <Fallback error={this.state.error} resetError={this.resetError} />;
        }
        
        return (
          <div className="error-fallback">
            <h2>Something went wrong</h2>
            <button onClick={this.resetError}>Try again</button>
          </div>
        );
      }

      const { fallback, ...restProps } = this.props;
      return <Component {...(restProps as P)} />;
    }
  };
};

// HOC for analytics tracking
interface WithAnalyticsProps {
  trackingId?: string;
  eventName?: string;
}

const withAnalytics = <P extends object>(
  Component: ComponentType<P>
) => {
  const WithAnalyticsComponent = (props: P & WithAnalyticsProps) => {
    const { trackingId, eventName, ...restProps } = props;
    
    useEffect(() => {
      if (trackingId && eventName) {
        // Simulate analytics tracking
        console.log(`Analytics: ${eventName} tracked for ${trackingId}`);
      }
    }, [trackingId, eventName]);
    
    return <Component {...(restProps as P)} />;
  };
  
  WithAnalyticsComponent.displayName = `withAnalytics(${Component.displayName || Component.name})`;
  
  return WithAnalyticsComponent;
};

// ============================================================================
// 🎯 SECTION 3: RENDER PROPS PATTERN
// ============================================================================

/**
 * 🔹 RENDER PROPS WITH TYPESCRIPT
 * 
 * WHAT THIS TEACHES:
 * - Render props pattern for sharing logic
 * - Function as children pattern
 * - Proper typing for render functions
 * - Flexible component composition
 * 
 * REAL-WORLD USAGE:
 * - Data fetching components
 * - Form state management
 * - Mouse/touch tracking
 * - Virtualization libraries
 */

// Mouse tracker with render props
interface MousePosition {
  x: number;
  y: number;
}

interface MouseTrackerProps {
  children: (position: MousePosition) => ReactNode;
}

const MouseTracker: React.FC<MouseTrackerProps> = ({ children }) => {
  const [position, setPosition] = useState<MousePosition>({ x: 0, y: 0 });
  
  useEffect(() => {
    const handleMouseMove = (event: MouseEvent) => {
      setPosition({ x: event.clientX, y: event.clientY });
    };
    
    document.addEventListener('mousemove', handleMouseMove);
    
    return () => {
      document.removeEventListener('mousemove', handleMouseMove);
    };
  }, []);
  
  return <>{children(position)}</>;
};

// Data fetcher with render props
interface DataFetcherProps<T> {
  url: string;
  children: (state: ApiResponse<T>) => ReactNode;
}

const DataFetcher = <T,>({ url, children }: DataFetcherProps<T>) => {
  const [state, setState] = useState<ApiResponse<T>>({ status: 'loading' });
  
  useEffect(() => {
    const fetchData = async () => {
      try {
        setState({ status: 'loading' });
        
        // Simulate API call
        await new Promise(resolve => setTimeout(resolve, 1000));
        
        // Mock successful response
        const mockData = { message: 'Data loaded successfully' } as T;
        setState({ status: 'success', data: mockData });
      } catch (error) {
        setState({ 
          status: 'error', 
          error: error instanceof Error ? error.message : 'Unknown error' 
        });
      }
    };
    
    fetchData();
  }, [url]);
  
  return <>{children(state)}</>;
};
