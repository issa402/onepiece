#!/usr/bin/env npx tsx
/**
 * 🏴‍☠️ REACT + TYPESCRIPT TODO APPLICATION PROJECT
 * Production-ready todo application with advanced features
 * 
 * This project demonstrates:
 * - Complex state management with useReducer
 * - Local storage persistence
 * - Drag and drop functionality
 * - Advanced filtering and sorting
 * - Form validation with custom hooks
 * - Performance optimization
 * - Accessibility best practices
 * - TypeScript best practices
 * 
 * Features:
 * - Create, edit, delete todos
 * - Mark todos as complete/incomplete
 * - Drag and drop reordering
 * - Priority levels (low, medium, high)
 * - Due dates and reminders
 * - Categories and tags
 * - Search and filtering
 * - Bulk operations
 * - Offline support with local storage
 * - Keyboard shortcuts
 * 
 * Run this project: npx tsx 03-todo-app-project.tsx
 */

import React, { 
  useState, 
  useEffect, 
  useCallback, 
  useMemo, 
  useReducer,
  useRef,
  createContext,
  useContext,
  KeyboardEvent,
  FormEvent,
  ChangeEvent
} from 'react';
import { createRoot } from 'react-dom/client';

// ============================================================================
// 🎯 SECTION 1: TYPE DEFINITIONS
// ============================================================================

/**
 * 🔹 COMPREHENSIVE TYPE SYSTEM
 * 
 * WHAT THIS TEACHES:
 * - Complex interface design for real applications
 * - Discriminated unions for different states
 * - Generic types for reusable components
 * - Utility types for derived interfaces
 */

// Core todo interface
interface Todo {
  id: string;
  title: string;
  description?: string;
  completed: boolean;
  priority: 'low' | 'medium' | 'high';
  category: string;
  tags: string[];
  dueDate?: Date;
  createdAt: Date;
  updatedAt: Date;
  order: number;
}

// Filter and sort options
interface TodoFilters {
  status: 'all' | 'active' | 'completed';
  priority?: 'low' | 'medium' | 'high';
  category?: string;
  tags: string[];
  search: string;
  dueDateRange?: {
    start: Date;
    end: Date;
  };
}

interface TodoSortOptions {
  field: keyof Pick<Todo, 'title' | 'createdAt' | 'dueDate' | 'priority' | 'order'>;
  direction: 'asc' | 'desc';
}

// Application state
interface TodoState {
  todos: Todo[];
  filters: TodoFilters;
  sortOptions: TodoSortOptions;
  selectedTodos: string[];
  categories: string[];
  isLoading: boolean;
  error: string | null;
}

// Action types for reducer
type TodoAction =
  | { type: 'ADD_TODO'; payload: Omit<Todo, 'id' | 'createdAt' | 'updatedAt' | 'order'> }
  | { type: 'UPDATE_TODO'; payload: { id: string; updates: Partial<Todo> } }
  | { type: 'DELETE_TODO'; payload: string }
  | { type: 'DELETE_TODOS'; payload: string[] }
  | { type: 'TOGGLE_TODO'; payload: string }
  | { type: 'REORDER_TODOS'; payload: { sourceIndex: number; destinationIndex: number } }
  | { type: 'SET_FILTERS'; payload: Partial<TodoFilters> }
  | { type: 'SET_SORT'; payload: TodoSortOptions }
  | { type: 'SELECT_TODO'; payload: string }
  | { type: 'SELECT_ALL_TODOS' }
  | { type: 'CLEAR_SELECTION' }
  | { type: 'LOAD_TODOS'; payload: Todo[] }
  | { type: 'SET_LOADING'; payload: boolean }
  | { type: 'SET_ERROR'; payload: string | null };

// Form data interfaces
interface TodoFormData {
  title: string;
  description: string;
  priority: Todo['priority'];
  category: string;
  tags: string;
  dueDate: string;
}

interface TodoFormErrors {
  title?: string;
  description?: string;
  category?: string;
  dueDate?: string;
}

// ============================================================================
// 🎯 SECTION 2: STATE MANAGEMENT WITH REDUCER
// ============================================================================

/**
 * 🔹 COMPLEX STATE MANAGEMENT
 * 
 * WHAT THIS TEACHES:
 * - useReducer for complex state logic
 * - Immutable state updates
 * - Action-based state management
 * - Type-safe reducers
 * 
 * REAL-WORLD USAGE:
 * - Redux-style state management without Redux
 * - Complex form state management
 * - Undo/redo functionality
 * - Multi-step wizards
 */

// Initial state
const initialTodoState: TodoState = {
  todos: [],
  filters: {
    status: 'all',
    tags: [],
    search: ''
  },
  sortOptions: {
    field: 'createdAt',
    direction: 'desc'
  },
  selectedTodos: [],
  categories: ['Personal', 'Work', 'Shopping', 'Health'],
  isLoading: false,
  error: null
};

// Utility function to generate unique IDs
const generateId = (): string => {
  return Date.now().toString(36) + Math.random().toString(36).substr(2);
};

// Todo reducer with comprehensive action handling
const todoReducer = (state: TodoState, action: TodoAction): TodoState => {
  switch (action.type) {
    case 'ADD_TODO': {
      const newTodo: Todo = {
        ...action.payload,
        id: generateId(),
        createdAt: new Date(),
        updatedAt: new Date(),
        order: state.todos.length
      };
      
      return {
        ...state,
        todos: [...state.todos, newTodo],
        error: null
      };
    }
    
    case 'UPDATE_TODO': {
      return {
        ...state,
        todos: state.todos.map(todo =>
          todo.id === action.payload.id
            ? { ...todo, ...action.payload.updates, updatedAt: new Date() }
            : todo
        ),
        error: null
      };
    }
    
    case 'DELETE_TODO': {
      return {
        ...state,
        todos: state.todos.filter(todo => todo.id !== action.payload),
        selectedTodos: state.selectedTodos.filter(id => id !== action.payload),
        error: null
      };
    }
    
    case 'DELETE_TODOS': {
      return {
        ...state,
        todos: state.todos.filter(todo => !action.payload.includes(todo.id)),
        selectedTodos: [],
        error: null
      };
    }
    
    case 'TOGGLE_TODO': {
      return {
        ...state,
        todos: state.todos.map(todo =>
          todo.id === action.payload
            ? { ...todo, completed: !todo.completed, updatedAt: new Date() }
            : todo
        ),
        error: null
      };
    }
    
    case 'REORDER_TODOS': {
      const { sourceIndex, destinationIndex } = action.payload;
      const newTodos = [...state.todos];
      const [removed] = newTodos.splice(sourceIndex, 1);
      newTodos.splice(destinationIndex, 0, removed);
      
      // Update order property
      const reorderedTodos = newTodos.map((todo, index) => ({
        ...todo,
        order: index,
        updatedAt: new Date()
      }));
      
      return {
        ...state,
        todos: reorderedTodos,
        error: null
      };
    }
    
    case 'SET_FILTERS': {
      return {
        ...state,
        filters: { ...state.filters, ...action.payload }
      };
    }
    
    case 'SET_SORT': {
      return {
        ...state,
        sortOptions: action.payload
      };
    }
    
    case 'SELECT_TODO': {
      const isSelected = state.selectedTodos.includes(action.payload);
      return {
        ...state,
        selectedTodos: isSelected
          ? state.selectedTodos.filter(id => id !== action.payload)
          : [...state.selectedTodos, action.payload]
      };
    }
    
    case 'SELECT_ALL_TODOS': {
      const visibleTodos = getFilteredAndSortedTodos(state.todos, state.filters, state.sortOptions);
      const allSelected = visibleTodos.every(todo => state.selectedTodos.includes(todo.id));
      
      return {
        ...state,
        selectedTodos: allSelected
          ? state.selectedTodos.filter(id => !visibleTodos.some(todo => todo.id === id))
          : [...new Set([...state.selectedTodos, ...visibleTodos.map(todo => todo.id)])]
      };
    }
    
    case 'CLEAR_SELECTION': {
      return {
        ...state,
        selectedTodos: []
      };
    }
    
    case 'LOAD_TODOS': {
      return {
        ...state,
        todos: action.payload,
        isLoading: false,
        error: null
      };
    }
    
    case 'SET_LOADING': {
      return {
        ...state,
        isLoading: action.payload
      };
    }
    
    case 'SET_ERROR': {
      return {
        ...state,
        error: action.payload,
        isLoading: false
      };
    }
    
    default:
      return state;
  }
};

// ============================================================================
// 🎯 SECTION 3: UTILITY FUNCTIONS
// ============================================================================

/**
 * 🔹 FILTERING AND SORTING LOGIC
 * 
 * WHAT THIS TEACHES:
 * - Complex array filtering with multiple criteria
 * - Dynamic sorting with type safety
 * - Performance optimization with memoization
 * - Functional programming patterns
 */

// Filter and sort todos based on current state
const getFilteredAndSortedTodos = (
  todos: Todo[],
  filters: TodoFilters,
  sortOptions: TodoSortOptions
): Todo[] => {
  let filtered = todos;
  
  // Filter by status
  if (filters.status !== 'all') {
    filtered = filtered.filter(todo => 
      filters.status === 'completed' ? todo.completed : !todo.completed
    );
  }
  
  // Filter by priority
  if (filters.priority) {
    filtered = filtered.filter(todo => todo.priority === filters.priority);
  }
  
  // Filter by category
  if (filters.category) {
    filtered = filtered.filter(todo => todo.category === filters.category);
  }
  
  // Filter by tags
  if (filters.tags.length > 0) {
    filtered = filtered.filter(todo =>
      filters.tags.some(tag => todo.tags.includes(tag))
    );
  }
  
  // Filter by search term
  if (filters.search) {
    const searchLower = filters.search.toLowerCase();
    filtered = filtered.filter(todo =>
      todo.title.toLowerCase().includes(searchLower) ||
      todo.description?.toLowerCase().includes(searchLower) ||
      todo.tags.some(tag => tag.toLowerCase().includes(searchLower))
    );
  }
  
  // Filter by due date range
  if (filters.dueDateRange) {
    filtered = filtered.filter(todo => {
      if (!todo.dueDate) return false;
      return todo.dueDate >= filters.dueDateRange!.start &&
             todo.dueDate <= filters.dueDateRange!.end;
    });
  }
  
  // Sort todos
  return filtered.sort((a, b) => {
    const { field, direction } = sortOptions;
    let aValue: any = a[field];
    let bValue: any = b[field];
    
    // Handle different data types
    if (field === 'priority') {
      const priorityOrder = { low: 1, medium: 2, high: 3 };
      aValue = priorityOrder[a.priority];
      bValue = priorityOrder[b.priority];
    } else if (aValue instanceof Date && bValue instanceof Date) {
      aValue = aValue.getTime();
      bValue = bValue.getTime();
    } else if (typeof aValue === 'string' && typeof bValue === 'string') {
      aValue = aValue.toLowerCase();
      bValue = bValue.toLowerCase();
    }
    
    if (aValue < bValue) return direction === 'asc' ? -1 : 1;
    if (aValue > bValue) return direction === 'asc' ? 1 : -1;
    return 0;
  });
};
