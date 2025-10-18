/**
 * 🏴‍☠️ ONE PIECE TRADING PLATFORM - REACT & NEXT.JS CODING LAB
 * 
 * This file contains comprehensive React and Next.js examples
 * demonstrating all concepts from basic components to advanced patterns.
 * 
 * To run this lab:
 * 1. Create a new Next.js project: npx create-next-app@latest onepiece-frontend --typescript --tailwind --app
 * 2. Replace the default files with these examples
 * 3. Run: npm run dev
 */

'use client';

import React, { useState, useEffect, useReducer, useCallback, useMemo, createContext, useContext } from 'react';
import Image from 'next/image';
import Link from 'next/link';

// ============================================================================
// 🎯 SECTION 1: TYPE DEFINITIONS
// ============================================================================

interface Character {
  id: string;
  name: string;
  bounty: number;
  crew: string;
  devilFruit?: string;
  haki: string[];
  image: string;
  description: string;
  isActive: boolean;
  createdAt: Date;
}

interface User {
  id: string;
  name: string;
  email: string;
  favorites: string[];
  cart: string[];
}

interface Trade {
  id: string;
  buyerId: string;
  sellerId: string;
  characterId: string;
  amount: number;
  status: 'pending' | 'accepted' | 'rejected' | 'completed';
  createdAt: Date;
}

// ============================================================================
// 🎯 SECTION 2: CONTEXT AND STATE MANAGEMENT
// ============================================================================

// Global App Context
interface AppContextType {
  user: User | null;
  characters: Character[];
  trades: Trade[];
  setUser: (user: User | null) => void;
  setCharacters: (characters: Character[]) => void;
  addToFavorites: (characterId: string) => void;
  removeFromFavorites: (characterId: string) => void;
  addToCart: (characterId: string) => void;
  removeFromCart: (characterId: string) => void;
}

const AppContext = createContext<AppContextType | undefined>(undefined);

// Custom hook to use app context
export function useAppContext() {
  const context = useContext(AppContext);
  if (!context) {
    throw new Error('useAppContext must be used within AppProvider');
  }
  return context;
}

// App Provider Component
export function AppProvider({ children }: { children: React.ReactNode }) {
  const [user, setUser] = useState<User | null>(null);
  const [characters, setCharacters] = useState<Character[]>([]);
  const [trades, setTrades] = useState<Trade[]>([]);

  // Load initial data
  useEffect(() => {
    loadInitialData();
  }, []);

  const loadInitialData = async () => {
    // Simulate API calls
    const mockCharacters: Character[] = [
      {
        id: '1',
        name: 'Monkey D. Luffy',
        bounty: 3000000000,
        crew: 'Straw Hat Pirates',
        devilFruit: 'Gomu Gomu no Mi',
        haki: ['Observation', 'Armament', 'Conqueror\'s'],
        image: '/images/luffy.jpg',
        description: 'Captain of the Straw Hat Pirates and aspiring Pirate King.',
        isActive: true,
        createdAt: new Date('2023-01-01')
      },
      {
        id: '2',
        name: 'Roronoa Zoro',
        bounty: 1111000000,
        crew: 'Straw Hat Pirates',
        haki: ['Observation', 'Armament'],
        image: '/images/zoro.jpg',
        description: 'Swordsman of the Straw Hat Pirates, aiming to be the world\'s greatest swordsman.',
        isActive: true,
        createdAt: new Date('2023-01-01')
      },
      {
        id: '3',
        name: 'Nami',
        bounty: 366000000,
        crew: 'Straw Hat Pirates',
        haki: [],
        image: '/images/nami.jpg',
        description: 'Navigator of the Straw Hat Pirates with exceptional weather prediction skills.',
        isActive: true,
        createdAt: new Date('2023-01-01')
      }
    ];

    setCharacters(mockCharacters);

    // Mock user
    const mockUser: User = {
      id: 'user1',
      name: 'Pirate Trader',
      email: 'trader@onepiece.com',
      favorites: [],
      cart: []
    };

    setUser(mockUser);
  };

  const addToFavorites = useCallback((characterId: string) => {
    setUser(prev => {
      if (!prev) return prev;
      if (prev.favorites.includes(characterId)) return prev;
      
      return {
        ...prev,
        favorites: [...prev.favorites, characterId]
      };
    });
  }, []);

  const removeFromFavorites = useCallback((characterId: string) => {
    setUser(prev => {
      if (!prev) return prev;
      
      return {
        ...prev,
        favorites: prev.favorites.filter(id => id !== characterId)
      };
    });
  }, []);

  const addToCart = useCallback((characterId: string) => {
    setUser(prev => {
      if (!prev) return prev;
      if (prev.cart.includes(characterId)) return prev;
      
      return {
        ...prev,
        cart: [...prev.cart, characterId]
      };
    });
  }, []);

  const removeFromCart = useCallback((characterId: string) => {
    setUser(prev => {
      if (!prev) return prev;
      
      return {
        ...prev,
        cart: prev.cart.filter(id => id !== characterId)
      };
    });
  }, []);

  const contextValue: AppContextType = {
    user,
    characters,
    trades,
    setUser,
    setCharacters,
    addToFavorites,
    removeFromFavorites,
    addToCart,
    removeFromCart
  };

  return (
    <AppContext.Provider value={contextValue}>
      {children}
    </AppContext.Provider>
  );
}

// ============================================================================
// 🎯 SECTION 3: REUSABLE UI COMPONENTS
// ============================================================================

// Button Component with variants
interface ButtonProps {
  variant?: 'primary' | 'secondary' | 'danger' | 'success';
  size?: 'sm' | 'md' | 'lg';
  disabled?: boolean;
  loading?: boolean;
  children: React.ReactNode;
  onClick?: () => void;
  className?: string;
}

export function Button({ 
  variant = 'primary', 
  size = 'md', 
  disabled = false,
  loading = false,
  children, 
  onClick,
  className = ''
}: ButtonProps) {
  const baseClasses = 'font-semibold rounded-lg transition-all duration-200 focus:outline-none focus:ring-2 disabled:opacity-50 disabled:cursor-not-allowed';
  
  const variantClasses = {
    primary: 'bg-blue-600 hover:bg-blue-700 text-white focus:ring-blue-500',
    secondary: 'bg-gray-200 hover:bg-gray-300 text-gray-800 focus:ring-gray-500',
    danger: 'bg-red-600 hover:bg-red-700 text-white focus:ring-red-500',
    success: 'bg-green-600 hover:bg-green-700 text-white focus:ring-green-500'
  };
  
  const sizeClasses = {
    sm: 'px-3 py-1.5 text-sm',
    md: 'px-4 py-2 text-base',
    lg: 'px-6 py-3 text-lg'
  };
  
  const classes = `${baseClasses} ${variantClasses[variant]} ${sizeClasses[size]} ${className}`;

  return (
    <button 
      className={classes}
      disabled={disabled || loading}
      onClick={onClick}
    >
      {loading ? (
        <div className="flex items-center justify-center">
          <div className="animate-spin rounded-full h-4 w-4 border-b-2 border-white mr-2"></div>
          Loading...
        </div>
      ) : (
        children
      )}
    </button>
  );
}

// Modal Component
interface ModalProps {
  isOpen: boolean;
  onClose: () => void;
  title: string;
  children: React.ReactNode;
  size?: 'sm' | 'md' | 'lg' | 'xl';
}

export function Modal({ isOpen, onClose, title, children, size = 'md' }: ModalProps) {
  if (!isOpen) return null;

  const sizeClasses = {
    sm: 'max-w-sm',
    md: 'max-w-md',
    lg: 'max-w-lg',
    xl: 'max-w-xl'
  };

  return (
    <div className="fixed inset-0 z-50 overflow-y-auto">
      {/* Backdrop */}
      <div 
        className="fixed inset-0 bg-black bg-opacity-50 transition-opacity"
        onClick={onClose}
      ></div>
      
      {/* Modal */}
      <div className="flex min-h-full items-center justify-center p-4">
        <div className={`relative bg-white rounded-lg shadow-xl ${sizeClasses[size]} w-full`}>
          {/* Header */}

// ============================================================================
// 🎯 SECTION 5: SHOPPING CART WITH ADVANCED STATE MANAGEMENT
// ============================================================================

// Cart state management with useReducer
interface CartState {
  items: { characterId: string; quantity: number }[];
  total: number;
  isOpen: boolean;
}

type CartAction =
  | { type: 'ADD_ITEM'; payload: string }
  | { type: 'REMOVE_ITEM'; payload: string }
  | { type: 'UPDATE_QUANTITY'; payload: { characterId: string; quantity: number } }
  | { type: 'CLEAR_CART' }
  | { type: 'TOGGLE_CART' }
  | { type: 'CALCULATE_TOTAL'; payload: Character[] };

function cartReducer(state: CartState, action: CartAction): CartState {
  switch (action.type) {
    case 'ADD_ITEM':
      const existingItem = state.items.find(item => item.characterId === action.payload);
      if (existingItem) {
        return {
          ...state,
          items: state.items.map(item =>
            item.characterId === action.payload
              ? { ...item, quantity: item.quantity + 1 }
              : item
          )
        };
      } else {
        return {
          ...state,
          items: [...state.items, { characterId: action.payload, quantity: 1 }]
        };
      }

    case 'REMOVE_ITEM':
      return {
        ...state,
        items: state.items.filter(item => item.characterId !== action.payload)
      };

    case 'UPDATE_QUANTITY':
      return {
        ...state,
        items: state.items.map(item =>
          item.characterId === action.payload.characterId
            ? { ...item, quantity: action.payload.quantity }
            : item
        )
      };

    case 'CLEAR_CART':
      return {
        ...state,
        items: [],
        total: 0
      };

    case 'TOGGLE_CART':
      return {
        ...state,
        isOpen: !state.isOpen
      };

    case 'CALCULATE_TOTAL':
      const total = state.items.reduce((sum, item) => {
        const character = action.payload.find(char => char.id === item.characterId);
        return sum + (character ? character.bounty * item.quantity : 0);
      }, 0);

      return {
        ...state,
        total
      };

    default:
      return state;
  }
}

export function ShoppingCart() {
  const { characters } = useAppContext();
  const [cartState, dispatch] = useReducer(cartReducer, {
    items: [],
    total: 0,
    isOpen: false
  });

  // Calculate total whenever items or characters change
  useEffect(() => {
    dispatch({ type: 'CALCULATE_TOTAL', payload: characters });
  }, [cartState.items, characters]);

  const addToCart = (characterId: string) => {
    dispatch({ type: 'ADD_ITEM', payload: characterId });
  };

  const removeFromCart = (characterId: string) => {
    dispatch({ type: 'REMOVE_ITEM', payload: characterId });
  };

  const updateQuantity = (characterId: string, quantity: number) => {
    if (quantity <= 0) {
      removeFromCart(characterId);
    } else {
      dispatch({ type: 'UPDATE_QUANTITY', payload: { characterId, quantity } });
    }
  };

  const clearCart = () => {
    dispatch({ type: 'CLEAR_CART' });
  };

  const toggleCart = () => {
    dispatch({ type: 'TOGGLE_CART' });
  };

  const cartCharacters = cartState.items.map(item => {
    const character = characters.find(char => char.id === item.characterId);
    return character ? { character, quantity: item.quantity } : null;
  }).filter(Boolean);

  return (
    <>
      {/* Cart Toggle Button */}
      <button
        onClick={toggleCart}
        className="fixed top-4 right-4 bg-blue-600 text-white p-3 rounded-full shadow-lg hover:bg-blue-700 transition-colors z-40"
      >
        🛒 {cartState.items.length > 0 && (
          <span className="absolute -top-2 -right-2 bg-red-500 text-white text-xs rounded-full h-6 w-6 flex items-center justify-center">
            {cartState.items.reduce((sum, item) => sum + item.quantity, 0)}
          </span>
        )}
      </button>

      {/* Cart Sidebar */}
      <div className={`fixed inset-y-0 right-0 w-96 bg-white shadow-xl transform transition-transform duration-300 z-50 ${
        cartState.isOpen ? 'translate-x-0' : 'translate-x-full'
      }`}>
        <div className="flex flex-col h-full">
          {/* Header */}
          <div className="flex items-center justify-between p-6 border-b">
            <h2 className="text-xl font-bold">Shopping Cart</h2>
            <button
              onClick={toggleCart}
              className="text-gray-500 hover:text-gray-700"
            >
              ✕
            </button>
          </div>

          {/* Cart Items */}
          <div className="flex-1 overflow-y-auto p-6">
            {cartCharacters.length === 0 ? (
              <div className="text-center text-gray-500 mt-12">
                <p className="text-4xl mb-4">🏴‍☠️</p>
                <p>Your cart is empty</p>
                <p className="text-sm mt-2">Add some pirates to start trading!</p>
              </div>
            ) : (
              <div className="space-y-4">
                {cartCharacters.map(({ character, quantity }) => (
                  <div key={character!.id} className="flex items-center space-x-3 bg-gray-50 p-3 rounded-lg">
                    <div className="w-16 h-16 bg-gray-200 rounded-lg flex items-center justify-center">
                      <span className="text-2xl">🏴‍☠️</span>
                    </div>

                    <div className="flex-1">
                      <h4 className="font-semibold text-sm">{character!.name}</h4>
                      <p className="text-xs text-gray-600">{character!.crew}</p>
                      <p className="text-sm font-medium text-blue-600">
                        {character!.bounty.toLocaleString()} berries
                      </p>
                    </div>

                    <div className="flex items-center space-x-2">
                      <button
                        onClick={() => updateQuantity(character!.id, quantity - 1)}
                        className="w-6 h-6 bg-gray-200 rounded text-sm hover:bg-gray-300"
                      >
                        -
                      </button>
                      <span className="w-8 text-center text-sm">{quantity}</span>
                      <button
                        onClick={() => updateQuantity(character!.id, quantity + 1)}
                        className="w-6 h-6 bg-gray-200 rounded text-sm hover:bg-gray-300"
                      >
                        +
                      </button>
                    </div>

                    <button
                      onClick={() => removeFromCart(character!.id)}
                      className="text-red-500 hover:text-red-700 text-sm"
                    >
                      🗑️
                    </button>
                  </div>
                ))}
              </div>
            )}
          </div>

          {/* Footer */}
          {cartCharacters.length > 0 && (
            <div className="border-t p-6">
              <div className="flex justify-between items-center mb-4">
                <span className="text-lg font-semibold">Total:</span>
                <span className="text-xl font-bold text-green-600">
                  {cartState.total.toLocaleString()} berries
                </span>
              </div>

              <div className="space-y-2">
                <Button
                  variant="success"
                  className="w-full"
                  onClick={() => alert('Checkout functionality would be implemented here!')}
                >
                  Proceed to Checkout
                </Button>

                <Button
                  variant="secondary"
                  className="w-full"
                  onClick={clearCart}
                >
                  Clear Cart
                </Button>
              </div>
            </div>
          )}
        </div>
      </div>

      {/* Backdrop */}
      {cartState.isOpen && (
        <div
          className="fixed inset-0 bg-black bg-opacity-50 z-40"
          onClick={toggleCart}
        ></div>
      )}
    </>
  );
}

// ============================================================================
// 🎯 SECTION 6: PERFORMANCE OPTIMIZED COMPONENTS
// ============================================================================

// Memoized Character Card for performance
const MemoizedCharacterCard = React.memo(CharacterCard, (prevProps, nextProps) => {
  return (
    prevProps.character.id === nextProps.character.id &&
    prevProps.character.name === nextProps.character.name &&
    prevProps.character.bounty === nextProps.character.bounty &&
    prevProps.showActions === nextProps.showActions
  );
});

// Virtual List Component for large datasets
interface VirtualListProps {
  items: any[];
  itemHeight: number;
  containerHeight: number;
  renderItem: (item: any, index: number) => React.ReactNode;
}

export function VirtualList({ items, itemHeight, containerHeight, renderItem }: VirtualListProps) {
  const [scrollTop, setScrollTop] = useState(0);

  const visibleStart = Math.floor(scrollTop / itemHeight);
  const visibleEnd = Math.min(
    visibleStart + Math.ceil(containerHeight / itemHeight) + 1,
    items.length
  );

  const visibleItems = items.slice(visibleStart, visibleEnd);

  const totalHeight = items.length * itemHeight;
  const offsetY = visibleStart * itemHeight;

  return (
    <div
      style={{ height: containerHeight }}
      className="overflow-auto"
      onScroll={(e) => setScrollTop(e.currentTarget.scrollTop)}
    >
      <div style={{ height: totalHeight, position: 'relative' }}>
        <div style={{ transform: `translateY(${offsetY}px)` }}>
          {visibleItems.map((item, index) => (
            <div key={visibleStart + index} style={{ height: itemHeight }}>
              {renderItem(item, visibleStart + index)}
            </div>
          ))}
        </div>
      </div>
    </div>
  );
}

// ============================================================================
// 🎯 SECTION 7: MAIN DEMO COMPONENT
// ============================================================================

export default function OnePieceTradingPlatformDemo() {
  const [activeTab, setActiveTab] = useState<'browse' | 'search' | 'favorites'>('browse');
  const { characters, user } = useAppContext();

  const favoriteCharacters = useMemo(() => {
    if (!user) return [];
    return characters.filter(char => user.favorites.includes(char.id));
  }, [characters, user]);

  const tabs = [
    { id: 'browse', label: 'Browse Characters', count: characters.length },
    { id: 'search', label: 'Search & Filter', count: null },
    { id: 'favorites', label: 'Favorites', count: favoriteCharacters.length }
  ];

  return (
    <div className="min-h-screen bg-gray-100">
      {/* Header */}
      <header className="bg-white shadow-sm border-b">
        <div className="max-w-7xl mx-auto px-4 py-6">
          <div className="flex items-center justify-between">
            <div>
              <h1 className="text-3xl font-bold text-gray-900">
                🏴‍☠️ One Piece Trading Platform
              </h1>
              <p className="text-gray-600 mt-1">
                Discover, collect, and trade your favorite pirates!
              </p>
            </div>

            {user && (
              <div className="text-right">
                <p className="font-semibold">Welcome, {user.name}!</p>
                <p className="text-sm text-gray-600">
                  {user.favorites.length} favorites • {user.cart.length} in cart
                </p>
              </div>
            )}
          </div>
        </div>
      </header>

      {/* Navigation Tabs */}
      <nav className="bg-white border-b">
        <div className="max-w-7xl mx-auto px-4">
          <div className="flex space-x-8">
            {tabs.map(tab => (
              <button
                key={tab.id}
                onClick={() => setActiveTab(tab.id as any)}
                className={`py-4 px-1 border-b-2 font-medium text-sm transition-colors ${
                  activeTab === tab.id
                    ? 'border-blue-500 text-blue-600'
                    : 'border-transparent text-gray-500 hover:text-gray-700 hover:border-gray-300'
                }`}
              >
                {tab.label}
                {tab.count !== null && (
                  <span className="ml-2 bg-gray-100 text-gray-600 py-0.5 px-2 rounded-full text-xs">
                    {tab.count}
                  </span>
                )}
              </button>
            ))}
          </div>
        </div>
      </nav>

      {/* Main Content */}
      <main className="max-w-7xl mx-auto px-4 py-8">
        {activeTab === 'browse' && (
          <div>
            <div className="mb-6">
              <h2 className="text-2xl font-bold mb-2">All Characters</h2>
              <p className="text-gray-600">Browse through our collection of One Piece characters.</p>
            </div>

            <div className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 xl:grid-cols-4 gap-6">
              {characters.map(character => (
                <MemoizedCharacterCard key={character.id} character={character} />
              ))}
            </div>
          </div>
        )}

        {activeTab === 'search' && <CharacterSearch />}

        {activeTab === 'favorites' && (
          <div>
            <div className="mb-6">
              <h2 className="text-2xl font-bold mb-2">Your Favorites</h2>
              <p className="text-gray-600">Characters you've marked as favorites.</p>
            </div>

            {favoriteCharacters.length === 0 ? (
              <div className="text-center py-12 text-gray-500">
                <p className="text-4xl mb-4">💔</p>
                <p className="text-xl mb-2">No favorites yet!</p>
                <p>Start browsing and add some characters to your favorites.</p>
              </div>
            ) : (
              <div className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 xl:grid-cols-4 gap-6">
                {favoriteCharacters.map(character => (
                  <MemoizedCharacterCard key={character.id} character={character} />
                ))}
              </div>
            )}
          </div>
        )}
      </main>

      {/* Shopping Cart */}
      <ShoppingCart />
    </div>
  );
}

// ============================================================================
// 🎯 SECTION 8: DEMO RUNNER
// ============================================================================

/**
 * 🚀 DEMO RUNNER FUNCTION
 *
 * This function demonstrates how to use all the components together.
 * In a real Next.js app, you would use this in your page components.
 */
export function runOnePieceTradingPlatformDemo() {
  console.log('🏴‍☠️ ONE PIECE TRADING PLATFORM DEMO');
  console.log('=====================================');
  console.log('');
  console.log('✅ React Components Created:');
  console.log('   - AppProvider (Context & State Management)');
  console.log('   - Button (Reusable UI Component)');
  console.log('   - Modal (Overlay Component)');
  console.log('   - LoadingSpinner (Loading States)');
  console.log('   - CharacterCard (Complex Component with Hooks)');
  console.log('   - CharacterSearch (Advanced Filtering)');
  console.log('   - ShoppingCart (useReducer State Management)');
  console.log('   - VirtualList (Performance Optimization)');
  console.log('   - OnePieceTradingPlatformDemo (Main App)');
  console.log('');
  console.log('✅ React Concepts Demonstrated:');
  console.log('   - Functional Components with TypeScript');
  console.log('   - useState, useEffect, useReducer, useContext');
  console.log('   - useMemo, useCallback for performance');
  console.log('   - Custom hooks and context patterns');
  console.log('   - Component composition and reusability');
  console.log('   - Event handling and form management');
  console.log('   - Conditional rendering and lists');
  console.log('   - Performance optimization with React.memo');
  console.log('');
  console.log('✅ Next.js Features Ready:');
  console.log('   - TypeScript integration');
  console.log('   - Image optimization with next/image');
  console.log('   - Link navigation with next/link');
  console.log('   - Client-side routing preparation');
  console.log('   - API route integration ready');
  console.log('');
  console.log('🎯 To use in Next.js:');
  console.log('   1. Wrap your app with <AppProvider>');
  console.log('   2. Use <OnePieceTradingPlatformDemo /> in your page');
  console.log('   3. Add Tailwind CSS for styling');
  console.log('   4. Connect to your API routes');
  console.log('');
  console.log('🏴‍☠️ Ready to sail the Grand Line of React development!');
}

// Run the demo
if (typeof window !== 'undefined') {
  runOnePieceTradingPlatformDemo();
}
          <div className="flex items-center justify-between p-6 border-b">
            <h3 className="text-lg font-semibold">{title}</h3>
            <button 
              onClick={onClose}
              className="text-gray-400 hover:text-gray-600 text-xl"
            >
              ✕
            </button>
          </div>
          
          {/* Content */}
          <div className="p-6">
            {children}
          </div>
        </div>
      </div>
    </div>
  );
}

// Loading Spinner Component
export function LoadingSpinner({ size = 'md' }: { size?: 'sm' | 'md' | 'lg' }) {
  const sizeClasses = {
    sm: 'h-4 w-4',
    md: 'h-8 w-8',
    lg: 'h-12 w-12'
  };

  return (
    <div className="flex justify-center items-center">
      <div className={`animate-spin rounded-full border-b-2 border-blue-600 ${sizeClasses[size]}`}></div>
    </div>
  );
}

// Character Card Component
interface CharacterCardProps {
  character: Character;
  showActions?: boolean;
}

export function CharacterCard({ character, showActions = true }: CharacterCardProps) {
  const { user, addToFavorites, removeFromFavorites, addToCart } = useAppContext();
  const [imageLoading, setImageLoading] = useState(true);
  const [imageError, setImageError] = useState(false);

  const isFavorite = user?.favorites.includes(character.id) || false;
  const isInCart = user?.cart.includes(character.id) || false;

  const handleFavoriteToggle = () => {
    if (isFavorite) {
      removeFromFavorites(character.id);
    } else {
      addToFavorites(character.id);
    }
  };

  const handleAddToCart = () => {
    addToCart(character.id);
  };

  return (
    <div className="bg-white rounded-lg shadow-md hover:shadow-lg transition-shadow duration-300 overflow-hidden">
      {/* Character Image */}
      <div className="relative h-48 bg-gray-200">
        {!imageError ? (
          <Image
            src={character.image}
            alt={character.name}
            fill
            className={`object-cover transition-opacity duration-300 ${
              imageLoading ? 'opacity-0' : 'opacity-100'
            }`}
            onLoad={() => setImageLoading(false)}
            onError={() => {
              setImageError(true);
              setImageLoading(false);
            }}
          />
        ) : (
          <div className="flex items-center justify-center h-full text-gray-500">
            <span className="text-4xl">🏴‍☠️</span>
          </div>
        )}
        
        {imageLoading && (
          <div className="absolute inset-0 flex items-center justify-center">
            <LoadingSpinner size="md" />
          </div>
        )}
      </div>

      {/* Character Info */}
      <div className="p-4">
        <h3 className="text-xl font-bold mb-2 text-gray-800">{character.name}</h3>
        
        <div className="space-y-2 text-sm text-gray-600 mb-4">
          <p><span className="font-semibold">Crew:</span> {character.crew}</p>
          <p><span className="font-semibold">Bounty:</span> {character.bounty.toLocaleString()} berries</p>
          
          {character.devilFruit && (
            <p><span className="font-semibold">Devil Fruit:</span> {character.devilFruit}</p>
          )}
          
          {character.haki.length > 0 && (
            <p><span className="font-semibold">Haki:</span> {character.haki.join(', ')}</p>
          )}
        </div>

        <p className="text-sm text-gray-700 mb-4 line-clamp-2">{character.description}</p>

        {/* Actions */}
        {showActions && (
          <div className="flex space-x-2">
            <Button
              variant={isFavorite ? 'danger' : 'secondary'}
              size="sm"
              onClick={handleFavoriteToggle}
              className="flex-1"
            >
              {isFavorite ? '❤️ Favorited' : '🤍 Favorite'}
            </Button>
            
            <Button
              variant={isInCart ? 'secondary' : 'primary'}
              size="sm"
              onClick={handleAddToCart}
              disabled={isInCart}
              className="flex-1"
            >
              {isInCart ? 'In Cart' : 'Add to Cart'}
            </Button>
          </div>
        )}
      </div>
    </div>
  );
}

// ============================================================================
// 🎯 SECTION 4: ADVANCED COMPONENTS WITH HOOKS
// ============================================================================

// Search and Filter Component
interface SearchFilters {
  search: string;
  crew: string;
  minBounty: number;
  maxBounty: number;
  sortBy: 'name' | 'bounty' | 'crew';
  sortOrder: 'asc' | 'desc';
}

export function CharacterSearch() {
  const { characters } = useAppContext();
  const [filters, setFilters] = useState<SearchFilters>({
    search: '',
    crew: '',
    minBounty: 0,
    maxBounty: 10000000000,
    sortBy: 'name',
    sortOrder: 'asc'
  });

  // Get unique crews for filter dropdown
  const crews = useMemo(() => {
    const uniqueCrews = [...new Set(characters.map(char => char.crew))];
    return uniqueCrews.sort();
  }, [characters]);

  // Filter and sort characters
  const filteredCharacters = useMemo(() => {
    let filtered = characters.filter(character => {
      const matchesSearch = character.name.toLowerCase().includes(filters.search.toLowerCase());
      const matchesCrew = !filters.crew || character.crew === filters.crew;
      const matchesBounty = character.bounty >= filters.minBounty && character.bounty <= filters.maxBounty;
      
      return matchesSearch && matchesCrew && matchesBounty;
    });

    // Sort results
    filtered.sort((a, b) => {
      let aValue: string | number;
      let bValue: string | number;

      switch (filters.sortBy) {
        case 'name':
          aValue = a.name;
          bValue = b.name;
          break;
        case 'bounty':
          aValue = a.bounty;
          bValue = b.bounty;
          break;
        case 'crew':
          aValue = a.crew;
          bValue = b.crew;
          break;
        default:
          aValue = a.name;
          bValue = b.name;
      }

      if (typeof aValue === 'string' && typeof bValue === 'string') {
        return filters.sortOrder === 'asc' 
          ? aValue.localeCompare(bValue)
          : bValue.localeCompare(aValue);
      } else {
        return filters.sortOrder === 'asc' 
          ? (aValue as number) - (bValue as number)
          : (bValue as number) - (aValue as number);
      }
    });

    return filtered;
  }, [characters, filters]);

  const updateFilter = (key: keyof SearchFilters, value: string | number) => {
    setFilters(prev => ({ ...prev, [key]: value }));
  };

  return (
    <div className="space-y-6">
      {/* Search and Filter Controls */}
      <div className="bg-white p-6 rounded-lg shadow-md">
        <h2 className="text-xl font-bold mb-4">Search & Filter Characters</h2>
        
        <div className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-4">
          {/* Search Input */}
          <div>
            <label className="block text-sm font-medium text-gray-700 mb-2">
              Search by Name
            </label>
            <input
              type="text"
              value={filters.search}
              onChange={(e) => updateFilter('search', e.target.value)}
              placeholder="Enter character name..."
              className="w-full px-3 py-2 border border-gray-300 rounded-lg focus:outline-none focus:ring-2 focus:ring-blue-500"
            />
          </div>

          {/* Crew Filter */}
          <div>
            <label className="block text-sm font-medium text-gray-700 mb-2">
              Filter by Crew
            </label>
            <select
              value={filters.crew}
              onChange={(e) => updateFilter('crew', e.target.value)}
              className="w-full px-3 py-2 border border-gray-300 rounded-lg focus:outline-none focus:ring-2 focus:ring-blue-500"
            >
              <option value="">All Crews</option>
              {crews.map(crew => (
                <option key={crew} value={crew}>{crew}</option>
              ))}
            </select>
          </div>

          {/* Sort Options */}
          <div>
            <label className="block text-sm font-medium text-gray-700 mb-2">
              Sort By
            </label>
            <div className="flex space-x-2">
              <select
                value={filters.sortBy}
                onChange={(e) => updateFilter('sortBy', e.target.value)}
                className="flex-1 px-3 py-2 border border-gray-300 rounded-lg focus:outline-none focus:ring-2 focus:ring-blue-500"
              >
                <option value="name">Name</option>
                <option value="bounty">Bounty</option>
                <option value="crew">Crew</option>
              </select>
              
              <select
                value={filters.sortOrder}
                onChange={(e) => updateFilter('sortOrder', e.target.value)}
                className="px-3 py-2 border border-gray-300 rounded-lg focus:outline-none focus:ring-2 focus:ring-blue-500"
              >
                <option value="asc">↑</option>
                <option value="desc">↓</option>
              </select>
            </div>
          </div>
        </div>

        {/* Bounty Range */}
        <div className="mt-4">
          <label className="block text-sm font-medium text-gray-700 mb-2">
            Bounty Range: {filters.minBounty.toLocaleString()} - {filters.maxBounty.toLocaleString()} berries
          </label>
          <div className="flex space-x-4">
            <input
              type="range"
              min="0"
              max="10000000000"
              step="100000000"
              value={filters.minBounty}
              onChange={(e) => updateFilter('minBounty', parseInt(e.target.value))}
              className="flex-1"
            />
            <input
              type="range"
              min="0"
              max="10000000000"
              step="100000000"
              value={filters.maxBounty}
              onChange={(e) => updateFilter('maxBounty', parseInt(e.target.value))}
              className="flex-1"
            />
          </div>
        </div>
      </div>

      {/* Results */}
      <div>
        <div className="flex justify-between items-center mb-4">
          <h3 className="text-lg font-semibold">
            Results ({filteredCharacters.length} characters)
          </h3>
        </div>

        {filteredCharacters.length === 0 ? (
          <div className="text-center py-12 text-gray-500">
            <p className="text-xl mb-2">🏴‍☠️</p>
            <p>No characters found matching your criteria.</p>
          </div>
        ) : (
          <div className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 xl:grid-cols-4 gap-6">
            {filteredCharacters.map(character => (
              <CharacterCard key={character.id} character={character} />
            ))}
          </div>
        )}
      </div>
    </div>
  );
}
