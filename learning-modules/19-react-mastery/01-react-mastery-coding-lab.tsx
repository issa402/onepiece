/*
🏴‍☠️ ONE PIECE TRADING PLATFORM - REACT MASTERY LAB
═══════════════════════════════════════════════════════════

🎯 WHAT YOU'LL BUILD FOR YOUR ONE PIECE PROJECT:
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
✅ ADVANCED REACT COMPONENTS - Custom hooks, compound components
✅ STATE MANAGEMENT MASTERY - Context, Reducers, Zustand
✅ PERFORMANCE OPTIMIZATION - Memoization, virtualization, lazy loading
✅ REAL-TIME FEATURES - WebSocket integration, live price updates
✅ FORM HANDLING - Type-safe forms with validation
✅ ERROR BOUNDARIES - Graceful error handling and recovery
✅ TESTING STRATEGIES - Unit, integration, and E2E testing
✅ ACCESSIBILITY - WCAG compliance and screen reader support

💰 SALARY IMPACT: +$70K-?30K (React mastery is ESSENTIAL)
🏢 COMPANIES: Facebook, Netflix, Airbnb, Uber, Discord, Shopify

🔗 HOW THIS CONNECTS TO YOUR ONE PIECE PROJECT:
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
🎯 YOUR CURRENT CharacterList.tsx COMPONENT:
   - Basic functional component → You'll add advanced patterns
   - Simple useState → You'll use complex state management
   - Basic error handling → You'll add error boundaries
   - No performance optimization → You'll add memoization

🎯 YOUR CURRENT PROJECT STRUCTURE:
   - Individual components → You'll create compound components
   - No global state → You'll add Context and state management
   - Basic TypeScript → You'll add advanced React + TS patterns
   - No testing → You'll add comprehensive test coverage

🎯 WHAT YOU'LL ADD TO YOUR PROJECT:
   - Real-time price chart with WebSocket integration
   - Advanced trading interface with optimistic updates
   - Global state management for user portfolio
   - Performance-optimized character list with virtualization
   - Accessible forms with proper ARIA labels
   - Error boundaries with user-friendly error messages

📚 REACT CONCEPTS YOU'LL MASTER:
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

🎣 ADVANCED HOOKS:
• Custom hooks for business logic
• useReducer for complex state
• useContext for global state
• useMemo and useCallback for performance
• useRef for DOM manipulation and values

🏗️ COMPONENT PATTERNS:
• Compound components
• Render props pattern
• Higher-order components (HOCs)
• Controlled vs uncontrolled components
• Polymorphic components with TypeScript

⚡ PERFORMANCE OPTIMIZATION:
• React.memo for component memoization
• Virtual scrolling for large lists
• Code splitting with React.lazy
• Bundle optimization techniques
• Profiling and debugging performance

🔄 STATE MANAGEMENT:
• Context API patterns
• useReducer for complex state
• Third-party solutions (Zustand, Redux Toolkit)
• Optimistic updates
• Server state management

🔧 REACT + TYPESCRIPT SYNTAX YOU'LL USE:
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

1. ADVANCED COMPONENT TYPES:
   interface CharacterCardProps {
       character: Character;
       onTrade: (character: Character) => void;
       className?: string;
   }
   
   const CharacterCard: React.FC<CharacterCardProps> = React.memo(({
       character,
       onTrade,
       className
   }) => {
       // Memoized component implementation
   });

2. CUSTOM HOOKS:
   function useCharacterData(characterId: number) {
       const [character, setCharacter] = useState<Character | null>(null);
       const [loading, setLoading] = useState(true);
       const [error, setError] = useState<string | null>(null);
       
       // Custom hook logic
       return { character, loading, error, refetch };
   }

3. CONTEXT WITH TYPESCRIPT:
   interface TradingContextType {
       portfolio: Portfolio;
       addToPortfolio: (character: Character, quantity: number) => void;
       removeFromPortfolio: (characterId: number) => void;
   }
   
   const TradingContext = createContext<TradingContextType | null>(null);

4. PERFORMANCE OPTIMIZATION:
   const MemoizedCharacterList = React.memo(CharacterList, (prevProps, nextProps) => {
       return prevProps.characters.length === nextProps.characters.length;
   });
*/

import React, { 
    useState, 
    useEffect, 
    useContext, 
    useReducer, 
    useMemo, 
    useCallback, 
    useRef,
    createContext,
    ReactNode,
    ComponentProps,
    forwardRef,
    useImperativeHandle
} from 'react';

// Type definitions for our One Piece project
interface Character {
    id: number;
    name: string;
    crew: string;
    bounty: number;
    price: number;
    priceChange: number;
    image?: string;
    devilFruit?: string;
    hakiTypes: string[];
}

interface Portfolio {
    characters: PortfolioItem[];
    totalValue: number;
    totalChange: number;
}

interface PortfolioItem {
    character: Character;
    quantity: number;
    averagePrice: number;
    currentValue: number;
}

interface Trade {
    id: string;
    characterId: number;
    type: 'buy' | 'sell';
    quantity: number;
    price: number;
    timestamp: Date;
}

// 🧪 HANDS-ON LAB 1: ADVANCED HOOKS & CUSTOM HOOKS
// ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

/*
📚 CUSTOM HOOKS EXPLAINED:
Custom hooks let you extract component logic into reusable functions.
They're essential for sharing stateful logic between components
without prop drilling or complex patterns.

REAL-WORLD EXAMPLE:
Netflix uses custom hooks for data fetching, user preferences,
and video player controls across their entire application.

IN ONE PIECE PROJECT:
Custom hooks for character data fetching, WebSocket connections,
portfolio management, and trading operations.
*/

// TODO 1: CUSTOM HOOKS FOR DATA FETCHING
// YOUR CODE HERE - Create useCharacterData hook:


// TODO 2: CUSTOM HOOKS FOR WEBSOCKET
// YOUR CODE HERE - Create useWebSocket hook:


// TODO 3: CUSTOM HOOKS FOR LOCAL STORAGE
// YOUR CODE HERE - Create useLocalStorage hook:


// 🧪 HANDS-ON LAB 2: STATE MANAGEMENT PATTERNS
// ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

/*
📚 STATE MANAGEMENT EXPLAINED:
React provides multiple ways to manage state: local state, Context API,
and third-party solutions. Choosing the right approach is crucial
for maintainable applications.

REAL-WORLD EXAMPLE:
Discord uses a combination of Context API for user data and Redux
for complex chat state management across their desktop app.

IN ONE PIECE PROJECT:
Global trading context, user authentication state, real-time
price updates, and portfolio management.
*/

// TODO 4: CONTEXT API SETUP
// YOUR CODE HERE - Create TradingContext:


// TODO 5: REDUCER FOR COMPLEX STATE
// YOUR CODE HERE - Create portfolio reducer:


// TODO 6: GLOBAL STATE PROVIDER
// YOUR CODE HERE - Create TradingProvider:


// 🧪 HANDS-ON LAB 3: PERFORMANCE OPTIMIZATION
// ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

/*
📚 PERFORMANCE OPTIMIZATION EXPLAINED:
React applications can become slow with large datasets and frequent
updates. Memoization, virtualization, and proper component structure
are essential for maintaining 60fps performance.

REAL-WORLD EXAMPLE:
Twitter's timeline uses virtual scrolling and memoization to handle
thousands of tweets without performance degradation.

IN ONE PIECE PROJECT:
Optimized character lists, real-time price updates without
unnecessary re-renders, and efficient trading interfaces.
*/

// TODO 7: MEMOIZED COMPONENTS
// YOUR CODE HERE - Create memoized CharacterCard:


// TODO 8: VIRTUAL SCROLLING
// YOUR CODE HERE - Implement virtual character list:


// TODO 9: OPTIMIZED REAL-TIME UPDATES
// YOUR CODE HERE - Efficient price update handling:


// 🧪 HANDS-ON LAB 4: ADVANCED COMPONENT PATTERNS
// ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

/*
📚 COMPONENT PATTERNS EXPLAINED:
Advanced React patterns like compound components, render props,
and polymorphic components create flexible, reusable interfaces
that scale with your application.

REAL-WORLD EXAMPLE:
Shopify's Polaris design system uses compound components extensively
for their admin interface, allowing flexible composition.

IN ONE PIECE PROJECT:
Compound trading interface, flexible character display components,
and reusable form patterns.
*/

// TODO 10: COMPOUND COMPONENTS
// YOUR CODE HERE - Create TradingInterface compound component:


// TODO 11: RENDER PROPS PATTERN
// YOUR CODE HERE - Create DataFetcher with render props:


// TODO 12: POLYMORPHIC COMPONENTS
// YOUR CODE HERE - Create flexible Button component:


/*
═══════════════════════════════════════════════════════════
🏆 COMPLETE CODE SOLUTION (SCROLL DOWN TO CHECK YOUR WORK)
═══════════════════════════════════════════════════════════
*/

// 🔥 COMPLETE REACT MASTERY IMPLEMENTATION

console.log('🏴‍☠️ React Mastery - One Piece Trading Platform');

// 1. ADVANCED HOOKS & CUSTOM HOOKS SOLUTIONS

// Custom hook for character data fetching
function useCharacterData(characterId: number | null) {
    const [character, setCharacter] = useState<Character | null>(null);
    const [loading, setLoading] = useState(false);
    const [error, setError] = useState<string | null>(null);
    
    const fetchCharacter = useCallback(async (id: number) => {
        setLoading(true);
        setError(null);
        
        try {
            const response = await fetch(`/api/characters/${id}`);
            if (!response.ok) {
                throw new Error(`Failed to fetch character: ${response.statusText}`);
            }
            
            const characterData = await response.json();
            setCharacter(characterData);
        } catch (err) {
            setError(err instanceof Error ? err.message : 'Unknown error');
        } finally {
            setLoading(false);
        }
    }, []);
    
    useEffect(() => {
        if (characterId) {
            fetchCharacter(characterId);
        }
    }, [characterId, fetchCharacter]);
    
    const refetch = useCallback(() => {
        if (characterId) {
            fetchCharacter(characterId);
        }
    }, [characterId, fetchCharacter]);
    
    return { character, loading, error, refetch };
}

// Custom hook for WebSocket connections
function useWebSocket<T>(url: string) {
    const [data, setData] = useState<T | null>(null);
    const [connectionStatus, setConnectionStatus] = useState<'Connecting' | 'Open' | 'Closed'>('Closed');
    const ws = useRef<WebSocket | null>(null);
    
    useEffect(() => {
        ws.current = new WebSocket(url);
        
        ws.current.onopen = () => {
            setConnectionStatus('Open');
            console.log('🔗 WebSocket connected');
        };
        
        ws.current.onmessage = (event) => {
            try {
                const parsedData = JSON.parse(event.data);
                setData(parsedData);
            } catch (error) {
                console.error('❌ Failed to parse WebSocket message:', error);
            }
        };
        
        ws.current.onclose = () => {
            setConnectionStatus('Closed');
            console.log('🔌 WebSocket disconnected');
        };
        
        ws.current.onerror = (error) => {
            console.error('❌ WebSocket error:', error);
        };
        
        return () => {
            ws.current?.close();
        };
    }, [url]);
    
    const sendMessage = useCallback((message: any) => {
        if (ws.current?.readyState === WebSocket.OPEN) {
            ws.current.send(JSON.stringify(message));
        }
    }, []);
    
    return { data, connectionStatus, sendMessage };
}

// Custom hook for local storage
function useLocalStorage<T>(key: string, initialValue: T) {
    const [storedValue, setStoredValue] = useState<T>(() => {
        try {
            const item = window.localStorage.getItem(key);
            return item ? JSON.parse(item) : initialValue;
        } catch (error) {
            console.error(`❌ Error reading localStorage key "${key}":`, error);
            return initialValue;
        }
    });
    
    const setValue = useCallback((value: T | ((val: T) => T)) => {
        try {
            const valueToStore = value instanceof Function ? value(storedValue) : value;
            setStoredValue(valueToStore);
            window.localStorage.setItem(key, JSON.stringify(valueToStore));
        } catch (error) {
            console.error(`❌ Error setting localStorage key "${key}":`, error);
        }
    }, [key, storedValue]);
    
    return [storedValue, setValue] as const;
}

// 2. STATE MANAGEMENT PATTERNS SOLUTIONS

// Trading Context Type
interface TradingContextType {
    portfolio: Portfolio;
    trades: Trade[];
    addToPortfolio: (character: Character, quantity: number) => void;
    removeFromPortfolio: (characterId: number, quantity: number) => void;
    executeTrade: (trade: Omit<Trade, 'id' | 'timestamp'>) => void;
    getTotalValue: () => number;
}

// Create Trading Context
const TradingContext = createContext<TradingContextType | null>(null);

// Portfolio Reducer
type PortfolioAction = 
    | { type: 'ADD_CHARACTER'; character: Character; quantity: number; price: number }
    | { type: 'REMOVE_CHARACTER'; characterId: number; quantity: number }
    | { type: 'UPDATE_PRICES'; priceUpdates: { characterId: number; price: number }[] }
    | { type: 'CLEAR_PORTFOLIO' };

function portfolioReducer(state: Portfolio, action: PortfolioAction): Portfolio {
    switch (action.type) {
        case 'ADD_CHARACTER': {
            const existingItem = state.characters.find(item => item.character.id === action.character.id);
            
            if (existingItem) {
                // Update existing position
                const totalQuantity = existingItem.quantity + action.quantity;
                const totalCost = (existingItem.averagePrice * existingItem.quantity) + (action.price * action.quantity);
                const newAveragePrice = totalCost / totalQuantity;
                
                return {
                    ...state,
                    characters: state.characters.map(item =>
                        item.character.id === action.character.id
                            ? {
                                ...item,
                                quantity: totalQuantity,
                                averagePrice: newAveragePrice,
                                currentValue: totalQuantity * action.character.price
                            }
                            : item
                    )
                };
            } else {
                // Add new position
                const newItem: PortfolioItem = {
                    character: action.character,
                    quantity: action.quantity,
                    averagePrice: action.price,
                    currentValue: action.quantity * action.character.price
                };
                
                return {
                    ...state,
                    characters: [...state.characters, newItem]
                };
            }
        }
        
        case 'REMOVE_CHARACTER': {
            return {
                ...state,
                characters: state.characters.map(item =>
                    item.character.id === action.characterId
                        ? {
                            ...item,
                            quantity: Math.max(0, item.quantity - action.quantity),
                            currentValue: Math.max(0, item.quantity - action.quantity) * item.character.price
                        }
                        : item
                ).filter(item => item.quantity > 0)
            };
        }
        
        case 'UPDATE_PRICES': {
            return {
                ...state,
                characters: state.characters.map(item => {
                    const priceUpdate = action.priceUpdates.find(update => update.characterId === item.character.id);
                    if (priceUpdate) {
                        return {
                            ...item,
                            character: { ...item.character, price: priceUpdate.price },
                            currentValue: item.quantity * priceUpdate.price
                        };
                    }
                    return item;
                })
            };
        }
        
        case 'CLEAR_PORTFOLIO': {
            return {
                characters: [],
                totalValue: 0,
                totalChange: 0
            };
        }
        
        default:
            return state;
    }
}

// Trading Provider Component
interface TradingProviderProps {
    children: ReactNode;
}

const TradingProvider: React.FC<TradingProviderProps> = ({ children }) => {
    const [portfolio, dispatch] = useReducer(portfolioReducer, {
        characters: [],
        totalValue: 0,
        totalChange: 0
    });
    
    const [trades, setTrades] = useState<Trade[]>([]);
    
    // WebSocket for real-time price updates
    const { data: priceData } = useWebSocket<{ characterId: number; price: number }[]>('ws://localhost:8080/prices');
    
    // Update prices when WebSocket data arrives
    useEffect(() => {
        if (priceData) {
            dispatch({ type: 'UPDATE_PRICES', priceUpdates: priceData });
        }
    }, [priceData]);
    
    const addToPortfolio = useCallback((character: Character, quantity: number) => {
        dispatch({ type: 'ADD_CHARACTER', character, quantity, price: character.price });
    }, []);
    
    const removeFromPortfolio = useCallback((characterId: number, quantity: number) => {
        dispatch({ type: 'REMOVE_CHARACTER', characterId, quantity });
    }, []);
    
    const executeTrade = useCallback((tradeData: Omit<Trade, 'id' | 'timestamp'>) => {
        const trade: Trade = {
            ...tradeData,
            id: `trade_${Date.now()}_${Math.random().toString(36).substr(2, 9)}`,
            timestamp: new Date()
        };
        
        setTrades(prev => [trade, ...prev]);
        
        // Update portfolio based on trade
        if (trade.type === 'buy') {
            // This would typically fetch the character data
            const character: Character = {
                id: trade.characterId,
                name: 'Character Name', // Would be fetched
                crew: 'Character Crew',
                bounty: 0,
                price: trade.price,
                priceChange: 0,
                hakiTypes: []
            };
            addToPortfolio(character, trade.quantity);
        } else {
            removeFromPortfolio(trade.characterId, trade.quantity);
        }
    }, [addToPortfolio, removeFromPortfolio]);
    
    const getTotalValue = useCallback(() => {
        return portfolio.characters.reduce((total, item) => total + item.currentValue, 0);
    }, [portfolio.characters]);
    
    const contextValue: TradingContextType = {
        portfolio,
        trades,
        addToPortfolio,
        removeFromPortfolio,
        executeTrade,
        getTotalValue
    };
    
    return (
        <TradingContext.Provider value={contextValue}>
            {children}
        </TradingContext.Provider>
    );
};

// Custom hook to use trading context
function useTradingContext() {
    const context = useContext(TradingContext);
    if (!context) {
        throw new Error('useTradingContext must be used within a TradingProvider');
    }
    return context;
}

// 3. PERFORMANCE OPTIMIZATION SOLUTIONS

// Memoized Character Card Component
interface CharacterCardProps {
    character: Character;
    onTrade: (character: Character, type: 'buy' | 'sell') => void;
    className?: string;
}

const CharacterCard: React.FC<CharacterCardProps> = React.memo(({
    character,
    onTrade,
    className = ''
}) => {
    const handleBuy = useCallback(() => {
        onTrade(character, 'buy');
    }, [character, onTrade]);
    
    const handleSell = useCallback(() => {
        onTrade(character, 'sell');
    }, [character, onTrade]);
    
    const priceChangeColor = character.priceChange >= 0 ? 'text-green-500' : 'text-red-500';
    const priceChangeSymbol = character.priceChange >= 0 ? '+' : '';
    
    return (
        <div className={`character-card ${className}`}>
            <div className="character-header">
                <h3>{character.name}</h3>
                <p className="crew">{character.crew}</p>
            </div>
            
            <div className="character-stats">
                <div className="price">
                    <span className="current-price">₿{character.price.toLocaleString()}</span>
                    <span className={`price-change ${priceChangeColor}`}>
                        {priceChangeSymbol}{character.priceChange.toFixed(2)}%
                    </span>
                </div>
                
                <div className="bounty">
                    Bounty: ₿{character.bounty.toLocaleString()}
                </div>
                
                {character.devilFruit && (
                    <div className="devil-fruit">
                        🍎 {character.devilFruit}
                    </div>
                )}
                
                {character.hakiTypes.length > 0 && (
                    <div className="haki">
                        ⚡ {character.hakiTypes.join(', ')}
                    </div>
                )}
            </div>
            
            <div className="character-actions">
                <button 
                    onClick={handleBuy}
                    className="buy-button"
                    aria-label={`Buy ${character.name} stock`}
                >
                    Buy
                </button>
                <button 
                    onClick={handleSell}
                    className="sell-button"
                    aria-label={`Sell ${character.name} stock`}
                >
                    Sell
                </button>
            </div>
        </div>
    );
}, (prevProps, nextProps) => {
    // Custom comparison function for memoization
    return (
        prevProps.character.id === nextProps.character.id &&
        prevProps.character.price === nextProps.character.price &&
        prevProps.character.priceChange === nextProps.character.priceChange &&
        prevProps.onTrade === nextProps.onTrade
    );
});

// Virtual Scrolling Character List
interface VirtualCharacterListProps {
    characters: Character[];
    onTrade: (character: Character, type: 'buy' | 'sell') => void;
    itemHeight: number;
    containerHeight: number;
}

const VirtualCharacterList: React.FC<VirtualCharacterListProps> = ({
    characters,
    onTrade,
    itemHeight,
    containerHeight
}) => {
    const [scrollTop, setScrollTop] = useState(0);
    const containerRef = useRef<HTMLDivElement>(null);
    
    const visibleCount = Math.ceil(containerHeight / itemHeight);
    const startIndex = Math.floor(scrollTop / itemHeight);
    const endIndex = Math.min(startIndex + visibleCount + 1, characters.length);
    
    const visibleCharacters = useMemo(() => {
        return characters.slice(startIndex, endIndex);
    }, [characters, startIndex, endIndex]);
    
    const handleScroll = useCallback((e: React.UIEvent<HTMLDivElement>) => {
        setScrollTop(e.currentTarget.scrollTop);
    }, []);
    
    const totalHeight = characters.length * itemHeight;
    const offsetY = startIndex * itemHeight;
    
    return (
        <div
            ref={containerRef}
            className="virtual-list-container"
            style={{ height: containerHeight, overflow: 'auto' }}
            onScroll={handleScroll}
        >
            <div style={{ height: totalHeight, position: 'relative' }}>
                <div style={{ transform: `translateY(${offsetY}px)` }}>
                    {visibleCharacters.map((character, index) => (
                        <div
                            key={character.id}
                            style={{ height: itemHeight }}
                        >
                            <CharacterCard
                                character={character}
                                onTrade={onTrade}
                            />
                        </div>
                    ))}
                </div>
            </div>
        </div>
    );
};

// 4. ADVANCED COMPONENT PATTERNS SOLUTIONS

// Compound Components Pattern - Trading Interface
interface TradingInterfaceProps {
    children: ReactNode;
}

interface TradingHeaderProps {
    children: ReactNode;
}

interface TradingBodyProps {
    children: ReactNode;
}

interface TradingFooterProps {
    children: ReactNode;
}

const TradingInterface: React.FC<TradingInterfaceProps> & {
    Header: React.FC<TradingHeaderProps>;
    Body: React.FC<TradingBodyProps>;
    Footer: React.FC<TradingFooterProps>;
} = ({ children }) => {
    return (
        <div className="trading-interface">
            {children}
        </div>
    );
};

TradingInterface.Header = ({ children }) => (
    <header className="trading-header">
        {children}
    </header>
);

TradingInterface.Body = ({ children }) => (
    <main className="trading-body">
        {children}
    </main>
);

TradingInterface.Footer = ({ children }) => (
    <footer className="trading-footer">
        {children}
    </footer>
);

// Render Props Pattern - Data Fetcher
interface DataFetcherProps<T> {
    url: string;
    children: (data: {
        data: T | null;
        loading: boolean;
        error: string | null;
        refetch: () => void;
    }) => ReactNode;
}

function DataFetcher<T>({ url, children }: DataFetcherProps<T>) {
    const [data, setData] = useState<T | null>(null);
    const [loading, setLoading] = useState(true);
    const [error, setError] = useState<string | null>(null);
    
    const fetchData = useCallback(async () => {
        setLoading(true);
        setError(null);
        
        try {
            const response = await fetch(url);
            if (!response.ok) {
                throw new Error(`HTTP ${response.status}: ${response.statusText}`);
            }
            
            const result = await response.json();
            setData(result);
        } catch (err) {
            setError(err instanceof Error ? err.message : 'Unknown error');
        } finally {
            setLoading(false);
        }
    }, [url]);
    
    useEffect(() => {
        fetchData();
    }, [fetchData]);
    
    return <>{children({ data, loading, error, refetch: fetchData })}</>;
}

// Polymorphic Component Pattern - Flexible Button
type ButtonProps<T extends React.ElementType> = {
    as?: T;
    variant?: 'primary' | 'secondary' | 'danger';
    size?: 'small' | 'medium' | 'large';
    children: ReactNode;
} & ComponentProps<T>;

function Button<T extends React.ElementType = 'button'>({
    as,
    variant = 'primary',
    size = 'medium',
    children,
    className = '',
    ...props
}: ButtonProps<T>) {
    const Component = as || 'button';
    
    const baseClasses = 'button';
    const variantClasses = {
        primary: 'button-primary',
        secondary: 'button-secondary',
        danger: 'button-danger'
    };
    const sizeClasses = {
        small: 'button-small',
        medium: 'button-medium',
        large: 'button-large'
    };
    
    const classes = `${baseClasses} ${variantClasses[variant]} ${sizeClasses[size]} ${className}`.trim();
    
    return (
        <Component className={classes} {...props}>
            {children}
        </Component>
    );
}

// Error Boundary Component
interface ErrorBoundaryState {
    hasError: boolean;
    error: Error | null;
}

class ErrorBoundary extends React.Component<
    { children: ReactNode; fallback?: ReactNode },
    ErrorBoundaryState
> {
    constructor(props: { children: ReactNode; fallback?: ReactNode }) {
        super(props);
        this.state = { hasError: false, error: null };
    }
    
    static getDerivedStateFromError(error: Error): ErrorBoundaryState {
        return { hasError: true, error };
    }
    
    componentDidCatch(error: Error, errorInfo: React.ErrorInfo) {
        console.error('❌ Error caught by boundary:', error, errorInfo);
    }
    
    render() {
        if (this.state.hasError) {
            return this.props.fallback || (
                <div className="error-boundary">
                    <h2>🏴‍☠️ Something went wrong!</h2>
                    <p>The One Piece trading platform encountered an error.</p>
                    <details>
                        <summary>Error details</summary>
                        <pre>{this.state.error?.message}</pre>
                    </details>
                    <button onClick={() => this.setState({ hasError: false, error: null })}>
                        Try again
                    </button>
                </div>
            );
        }
        
        return this.props.children;
    }
}

// Main Application Component demonstrating all patterns
const OnePieceTradingApp: React.FC = () => {
    const { portfolio, executeTrade } = useTradingContext();
    
    const handleTrade = useCallback((character: Character, type: 'buy' | 'sell') => {
        executeTrade({
            characterId: character.id,
            type,
            quantity: 1,
            price: character.price
        });
    }, [executeTrade]);
    
    return (
        <ErrorBoundary>
            <div className="app">
                <TradingInterface>
                    <TradingInterface.Header>
                        <h1>🏴‍☠️ One Piece Trading Platform</h1>
                        <div className="portfolio-summary">
                            Total Value: ₿{portfolio.totalValue.toLocaleString()}
                        </div>
                    </TradingInterface.Header>
                    
                    <TradingInterface.Body>
                        <DataFetcher<Character[]> url="/api/characters">
                            {({ data: characters, loading, error, refetch }) => {
                                if (loading) return <div>Loading characters...</div>;
                                if (error) return <div>Error: {error}</div>;
                                if (!characters) return <div>No characters found</div>;
                                
                                return (
                                    <VirtualCharacterList
                                        characters={characters}
                                        onTrade={handleTrade}
                                        itemHeight={200}
                                        containerHeight={600}
                                    />
                                );
                            }}
                        </DataFetcher>
                    </TradingInterface.Body>
                    
                    <TradingInterface.Footer>
                        <Button variant="primary" size="large">
                            View Portfolio
                        </Button>
                        <Button as="a" href="/trades" variant="secondary">
                            Trade History
                        </Button>
                    </TradingInterface.Footer>
                </TradingInterface>
            </div>
        </ErrorBoundary>
    );
};

// Export the main app wrapped with providers
export default function App() {
    return (
        <TradingProvider>
            <OnePieceTradingApp />
        </TradingProvider>
    );
}

// ===============================================================================
// 🏴‍☠️ CONGRATULATIONS! YOU'VE MASTERED REACT DEVELOPMENT! 🎉
// ===============================================================================

console.log('\n🏴‍☠️ CONGRATULATIONS! YOU\'VE MASTERED REACT DEVELOPMENT! 🎉');
console.log('===============================================================================');

console.log('\n🎯 WHAT YOU\'VE ACCOMPLISHED:');
console.log('✅ Mastered advanced React hooks and custom hook patterns');
console.log('✅ Implemented complex state management with Context API and useReducer');
console.log('✅ Built performance-optimized components with memoization and virtualization');
console.log('✅ Created advanced component patterns (compound, render props, polymorphic)');
console.log('✅ Added real-time features with WebSocket integration');
console.log('✅ Implemented error boundaries and graceful error handling');
console.log('✅ Built accessible, type-safe React applications');

console.log('\n💰 SALARY IMPACT: +$70K-$130K (React mastery is essential for frontend roles)');
console.log('🏢 COMPANIES: Facebook, Netflix, Airbnb, Uber, Discord, Shopify, Stripe');

console.log('\n===============================================================================');
console.log('🎯 NOW IMPLEMENT THIS IN YOUR ONE PIECE PROJECT!');
console.log('===============================================================================');

console.log('\n🚀 STEP 1: UPGRADE YOUR CHARACTER LIST COMPONENT');
console.log('━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━');
console.log('📁 File to update: frontend/src/components/Characters/CharacterList.tsx');
console.log('');
console.log('🎯 WHAT TO DO:');
console.log('1. Replace basic useState with useReducer for complex state');
console.log('2. Add React.memo for performance optimization');
console.log('3. Implement virtual scrolling for large character lists');
console.log('4. Add real-time price updates with WebSocket');
console.log('5. Create custom hooks for character data fetching');
console.log('');
console.log('📚 REFERENCE: Use the VirtualCharacterList and custom hooks from this module');

console.log('\n🚀 STEP 2: ADD GLOBAL STATE MANAGEMENT');
console.log('━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━');
console.log('📝 CREATE: frontend/src/contexts/TradingContext.tsx');
console.log('');
console.log('import React, { createContext, useContext, useReducer } from "react";');
console.log('');
console.log('interface TradingContextType {');
console.log('    portfolio: Portfolio;');
console.log('    addToPortfolio: (character: Character, quantity: number) => void;');
console.log('    removeFromPortfolio: (characterId: number, quantity: number) => void;');
console.log('    getTotalValue: () => number;');
console.log('}');
console.log('');
console.log('const TradingContext = createContext<TradingContextType | null>(null);');
console.log('');
console.log('export const TradingProvider: React.FC<{ children: ReactNode }> = ({ children }) => {');
console.log('    const [portfolio, dispatch] = useReducer(portfolioReducer, initialState);');
console.log('    ');
console.log('    // Add your trading logic here');
console.log('    ');
console.log('    return (');
console.log('        <TradingContext.Provider value={contextValue}>');
console.log('            {children}');
console.log('        </TradingContext.Provider>');
console.log('    );');
console.log('};');
console.log('');
console.log('export const useTradingContext = () => {');
console.log('    const context = useContext(TradingContext);');
console.log('    if (!context) throw new Error("useTradingContext must be used within TradingProvider");');
console.log('    return context;');
console.log('};');
console.log('');
console.log('🔧 COPY FROM THIS MODULE:');
console.log('- TradingProvider implementation (lines 520-592)');
console.log('- Portfolio reducer logic (lines 430-513)');
console.log('- Custom hook patterns (lines 595-601)');

console.log('\n🚀 STEP 3: ADD REAL-TIME WEBSOCKET INTEGRATION');
console.log('━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━');
console.log('📝 CREATE: frontend/src/hooks/useWebSocket.ts');
console.log('');
console.log('import { useState, useEffect, useRef, useCallback } from "react";');
console.log('');
console.log('export function useWebSocket<T>(url: string) {');
console.log('    const [data, setData] = useState<T | null>(null);');
console.log('    const [connectionStatus, setConnectionStatus] = useState<"Connecting" | "Open" | "Closed">("Closed");');
console.log('    const ws = useRef<WebSocket | null>(null);');
console.log('    ');
console.log('    useEffect(() => {');
console.log('        ws.current = new WebSocket(url);');
console.log('        ');
console.log('        ws.current.onopen = () => setConnectionStatus("Open");');
console.log('        ws.current.onmessage = (event) => {');
console.log('            const parsedData = JSON.parse(event.data);');
console.log('            setData(parsedData);');
console.log('        };');
console.log('        ws.current.onclose = () => setConnectionStatus("Closed");');
console.log('        ');
console.log('        return () => ws.current?.close();');
console.log('    }, [url]);');
console.log('    ');
console.log('    const sendMessage = useCallback((message: any) => {');
console.log('        if (ws.current?.readyState === WebSocket.OPEN) {');
console.log('            ws.current.send(JSON.stringify(message));');
console.log('        }');
console.log('    }, []);');
console.log('    ');
console.log('    return { data, connectionStatus, sendMessage };');
console.log('}');
console.log('');
console.log('// Use in your components:');
console.log('const { data: priceUpdates } = useWebSocket<PriceUpdate[]>("ws://localhost:5000/prices");');
console.log('');
console.log('🔧 USE PATTERNS FROM THIS MODULE:');
console.log('- WebSocket hook implementation (lines 338-381)');
console.log('- Real-time price updates (lines 529-537)');
console.log('- Connection status handling (lines 340-372)');

console.log('\n🚀 STEP 4: CREATE PERFORMANCE-OPTIMIZED COMPONENTS');
console.log('━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━');
console.log('📝 UPDATE: frontend/src/components/Characters/CharacterCard.tsx');
console.log('');
console.log('import React, { useCallback } from "react";');
console.log('');
console.log('interface CharacterCardProps {');
console.log('    character: Character;');
console.log('    onTrade: (character: Character, type: "buy" | "sell") => void;');
console.log('}');
console.log('');
console.log('export const CharacterCard: React.FC<CharacterCardProps> = React.memo(({');
console.log('    character,');
console.log('    onTrade');
console.log('}) => {');
console.log('    const handleBuy = useCallback(() => {');
console.log('        onTrade(character, "buy");');
console.log('    }, [character, onTrade]);');
console.log('    ');
console.log('    const handleSell = useCallback(() => {');
console.log('        onTrade(character, "sell");');
console.log('    }, [character, onTrade]);');
console.log('    ');
console.log('    return (');
console.log('        <div className="character-card">');
console.log('            <h3>{character.name}</h3>');
console.log('            <p>Price: ₿{character.price.toLocaleString()}</p>');
console.log('            <p>Change: {character.priceChange.toFixed(2)}%</p>');
console.log('            ');
console.log('            <div className="actions">');
console.log('                <button onClick={handleBuy}>Buy</button>');
console.log('                <button onClick={handleSell}>Sell</button>');
console.log('            </div>');
console.log('        </div>');
console.log('    );');
console.log('}, (prevProps, nextProps) => {');
console.log('    // Custom comparison for memoization');
console.log('    return (');
console.log('        prevProps.character.id === nextProps.character.id &&');
console.log('        prevProps.character.price === nextProps.character.price &&');
console.log('        prevProps.character.priceChange === nextProps.character.priceChange');
console.log('    );');
console.log('});');
console.log('');
console.log('🔧 BENEFITS OF MEMOIZATION:');
console.log('- Prevents unnecessary re-renders when props haven\'t changed');
console.log('- Improves performance with large lists of components');
console.log('- Essential for real-time applications with frequent updates');
console.log('- Used by all major React applications (Facebook, Netflix, etc.)');

console.log('\n🚀 STEP 5: ADD ERROR BOUNDARIES AND TESTING');
console.log('━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━');
console.log('📝 CREATE: frontend/src/components/ErrorBoundary.tsx');
console.log('');
console.log('import React, { Component, ReactNode } from "react";');
console.log('');
console.log('interface ErrorBoundaryState {');
console.log('    hasError: boolean;');
console.log('    error: Error | null;');
console.log('}');
console.log('');
console.log('export class ErrorBoundary extends Component<');
console.log('    { children: ReactNode },');
console.log('    ErrorBoundaryState');
console.log('> {');
console.log('    constructor(props: { children: ReactNode }) {');
console.log('        super(props);');
console.log('        this.state = { hasError: false, error: null };');
console.log('    }');
console.log('    ');
console.log('    static getDerivedStateFromError(error: Error): ErrorBoundaryState {');
console.log('        return { hasError: true, error };');
console.log('    }');
console.log('    ');
console.log('    render() {');
console.log('        if (this.state.hasError) {');
console.log('            return (');
console.log('                <div className="error-boundary">');
console.log('                    <h2>🏴‍☠️ Something went wrong!</h2>');
console.log('                    <p>The trading platform encountered an error.</p>');
console.log('                    <button onClick={() => this.setState({ hasError: false, error: null })}>');
console.log('                        Try again');
console.log('                    </button>');
console.log('                </div>');
console.log('            );');
console.log('        }');
console.log('        ');
console.log('        return this.props.children;');
console.log('    }');
console.log('}');
console.log('');
console.log('// Wrap your app:');
console.log('// <ErrorBoundary><App /></ErrorBoundary>');
console.log('');
console.log('🔧 COPY FROM THIS MODULE:');
console.log('- ErrorBoundary implementation (lines 876-918)');
console.log('- Error handling patterns (lines 891-917)');
console.log('- Recovery mechanisms (lines 909-911)');

console.log('\n🚀 STEP 6: TEST YOUR REACT IMPLEMENTATION');
console.log('━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━');
console.log('🧪 TESTING STEPS:');
console.log('');
console.log('1. Start your React development server:');
console.log('   cd frontend');
console.log('   npm start');
console.log('');
console.log('2. Test component memoization:');
console.log('   - Open React DevTools');
console.log('   - Enable "Highlight updates when components render"');
console.log('   - Verify only changed components re-render');
console.log('');
console.log('3. Test WebSocket connection:');
console.log('   - Check browser console for WebSocket connection logs');
console.log('   - Verify real-time price updates work');
console.log('   - Test connection recovery after network issues');
console.log('');
console.log('4. Test error boundaries:');
console.log('   - Temporarily throw an error in a component');
console.log('   - Verify error boundary catches and displays fallback UI');
console.log('   - Test error recovery functionality');
console.log('');
console.log('5. Test performance with large datasets:');
console.log('   - Load 1000+ characters');
console.log('   - Verify smooth scrolling with virtual list');
console.log('   - Check memory usage doesn\'t grow excessively');
console.log('');
console.log('✅ SUCCESS CRITERIA:');
console.log('- React app starts without errors');
console.log('- Components only re-render when necessary (check DevTools)');
console.log('- WebSocket connection establishes and receives data');
console.log('- Error boundaries catch and handle errors gracefully');
console.log('- Large lists scroll smoothly with virtual scrolling');
console.log('- Global state management works across components');

console.log('\n===============================================================================');
console.log('🔗 HOW THIS CONNECTS TO OTHER LEARNING MODULES');
console.log('===============================================================================');

console.log('\n🧩 MODULE CONNECTIONS:');
console.log('');
console.log('📚 Module 15 (JavaScript) → React uses advanced JavaScript patterns and async/await');
console.log('📚 Module 18 (TypeScript) → React components use TypeScript for type safety');
console.log('📚 Module 16 (Node.js) → React frontend calls your Node.js API Gateway');
console.log('📚 Module 11 (APIs) → React consumes REST APIs and WebSocket connections');
console.log('📚 Module 7 (Security) → React handles JWT tokens and secure authentication');
console.log('📚 Module 8 (Monitoring) → React includes error tracking and performance monitoring');

console.log('\n🎯 NEXT MODULES TO COMPLETE:');
console.log('1. Module 18: Add comprehensive TypeScript types to your React components');
console.log('2. Module 7: Implement secure authentication in your React app');
console.log('3. Module 8: Add performance monitoring and error tracking');

console.log('\n📚 RECOMMENDED RESOURCES FOR CONTINUED LEARNING:');
console.log('🔗 React Documentation: https://react.dev/');
console.log('🔗 React Performance: https://react.dev/learn/render-and-commit');
console.log('🔗 React Testing Library: https://testing-library.com/docs/react-testing-library/intro/');
console.log('🔗 React Patterns: https://reactpatterns.com/');

console.log('\n🏴‍☠️ YOU\'RE NOW READY TO BUILD PROFESSIONAL, SCALABLE REACT APPLICATIONS! ⚔️');
console.log('📖 REFERENCE: Check MASTER-BLUEPRINT-ARCHITECTURE.md for the complete system overview!');

/*
═══════════════════════════════════════════════════════════════════════════════
🎯 WHAT'S NEXT? YOUR COMPLETE LEARNING PATH AFTER MODULE 19
═══════════════════════════════════════════════════════════════════════════════

🏴‍☠️ CONGRATULATIONS! You've completed Module 19: React Mastery!

📚 WHAT YOU JUST MASTERED:
✅ React components and JSX
✅ Hooks (useState, useEffect, useContext, custom hooks)
✅ State management and data flow
✅ Event handling and forms
✅ API integration with fetch/axios
✅ Performance optimization (React.memo, useMemo, useCallback)
✅ Real-time updates with WebSockets
✅ Component testing with React Testing Library

💰 CAREER IMPACT: +$60K-$120K (React Frontend Developer skills)

🎯 YOUR NEXT STEPS (CHOOSE YOUR PATH):

═══════════════════════════════════════════════════════════════════════════════
📍 OPTION 1: ADD TYPE SAFETY (RECOMMENDED)
═══════════════════════════════════════════════════════════════════════════════

🔥 NEXT MODULE: Module 18 - TypeScript Mastery
📁 NEXT FILE: learning-modules/18-typescript-mastery/01-typescript-mastery-coding-lab.ts
⏱️ TIME: 3-4 hours
🎯 WHY: Add type safety to your React components and catch errors at compile time

WHAT YOU'LL LEARN NEXT:
• TypeScript interfaces and types
• React component typing
• Props and state typing
• API response typing
• Generic components

═══════════════════════════════════════════════════════════════════════════════
📍 OPTION 2: CONNECT TO BACKEND (API INTEGRATION)
═══════════════════════════════════════════════════════════════════════════════

🔥 NEXT MODULE: Module 16 - Node.js Backend (if not completed)
📁 NEXT FILE: learning-modules/16-nodejs-backend/01-nodejs-mastery-coding-lab.js
⏱️ TIME: 4-5 hours
🎯 WHY: Your React frontend needs a backend API to connect to

WHAT YOU'LL LEARN NEXT:
• Express.js API server
• RESTful endpoints
• Database integration
• Authentication middleware
• API documentation

═══════════════════════════════════════════════════════════════════════════════
📍 OPTION 3: OPTIMIZE PERFORMANCE
═══════════════════════════════════════════════════════════════════════════════

🔥 NEXT MODULE: Module 20 - Memory Optimization
📁 NEXT FILE: learning-modules/20-memory-optimization/01-memory-performance-coding-lab.js
⏱️ TIME: 2-3 hours
🎯 WHY: Optimize your React app for large datasets and better performance

WHAT YOU'LL LEARN NEXT:
• Virtual scrolling for large lists
• Memory leak prevention
• React performance profiling
• Bundle optimization
• Lazy loading

═══════════════════════════════════════════════════════════════════════════════
📍 OPTION 4: ADD AUTHENTICATION & SECURITY
═══════════════════════════════════════════════════════════════════════════════

🔥 NEXT MODULE: Module 7 - Security & Authentication
📁 NEXT FILE: learning-modules/07-security-authentication/01-oauth2-jwt-security-coding-lab.py
⏱️ TIME: 3-4 hours
🎯 WHY: Secure your React app with proper authentication and authorization

WHAT YOU'LL LEARN NEXT:
• JWT token handling
• Protected routes
• OAuth2 integration
• Security best practices
• User session management

═══════════════════════════════════════════════════════════════════════════════
🎯 RECOMMENDED LEARNING PATH FOR FRONTEND DEVELOPERS:
═══════════════════════════════════════════════════════════════════════════════

1. ✅ Module 19: React Mastery (COMPLETED)
2. 🔥 Module 18: TypeScript Integration (NEXT)
3. 🔐 Module 7: Security & Authentication
4. ⚡ Module 20: Memory Optimization
5. 🌐 Module 16: Node.js Backend (if needed)

═══════════════════════════════════════════════════════════════════════════════
🎯 IMPLEMENTATION STATUS CHECK:
═══════════════════════════════════════════════════════════════════════════════

📁 FILES YOU SHOULD HAVE CREATED:
✅ frontend/src/components/CharacterCard.tsx (Character display)
✅ frontend/src/components/TradingInterface.tsx (Trading UI)
✅ frontend/src/components/Portfolio.tsx (Portfolio view)
✅ frontend/src/hooks/useCharacters.ts (Custom hook)
✅ frontend/src/hooks/useWebSocket.ts (WebSocket hook)
✅ frontend/src/services/api.ts (API service)
✅ frontend/src/utils/formatters.ts (Utility functions)

🧪 TESTS YOU SHOULD RUN:
□ npm test (Run React tests)
□ npm run build (Test production build)
□ npm start (Start development server)

🔧 NEXT IMPLEMENTATION TASKS:
□ Add TypeScript types to all components
□ Connect to real API Gateway
□ Add authentication flow
□ Optimize for performance

═══════════════════════════════════════════════════════════════════════════════
🏴‍☠️ READY TO CONTINUE YOUR LEGENDARY JOURNEY?
═══════════════════════════════════════════════════════════════════════════════

Choose your next module and keep building your enterprise-grade One Piece trading platform! ⚔️

📖 REFERENCE GUIDES:
• 🏴‍☠️-START-HERE-PROJECT-MASTER-GUIDE.md → Complete project overview
• IMPLEMENTATION-ROADMAP.md → Detailed implementation steps
• MASTER-BLUEPRINT-ARCHITECTURE.md → System architecture

🚀 You're building something legendary! Keep going! 🚀
*/
