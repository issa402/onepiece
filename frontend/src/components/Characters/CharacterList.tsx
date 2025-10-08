/*
🏴‍☠️ CHARACTER LIST COMPONENT - LEARN BY CODING
═══════════════════════════════════════════════════════════

🎯 WHAT YOU'LL LEARN BY CODING THIS:
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
✅ React functional components and hooks
✅ TypeScript interfaces and props
✅ API calls with axios and error handling
✅ State management with useState and useEffect
✅ Event handling and user interactions
✅ Conditional rendering and loading states

� REACT SYNTAX YOU'LL USE:
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

1. COMPONENT DECLARATION:
   const ComponentName: React.FC<Props> = ({ prop1, prop2 }) => {
     return <div>Content</div>;
   };

2. STATE HOOKS:
   const [state, setState] = useState<Type>(initialValue);
   const [loading, setLoading] = useState<boolean>(false);

3. EFFECT HOOKS:
   useEffect(() => {
     // Side effect code
   }, [dependencies]);

4. API CALLS:
   const fetchData = async () => {
     try {
       const response = await axios.get('/api/endpoint');
       setData(response.data);
     } catch (error) {
       setError(error.message);
     }
   };

5. CONDITIONAL RENDERING:
   {loading ? <div>Loading...</div> : <div>Content</div>}
   {error && <div>Error: {error}</div>}

6. MAP OVER ARRAYS:
   {items.map(item => (
     <div key={item.id}>{item.name}</div>
   ))}

� TYPESCRIPT INTERFACES YOU'LL NEED:
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

interface Character {
  id: number;
  name: string;
  crew: string;
  bounty: number;
  current_price: number;
}

interface Props {
  // Component props go here
}
*/

/*
🧪 HANDS-ON LAB 1: REACT IMPORTS & DEPENDENCIES
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

📚 IMPORT SYNTAX EXPLAINED:
• import React from 'react' - Default import
• import { useState } from 'react' - Named import (destructuring)
• import axios from 'axios' - Third-party library import
• import './file.css' - CSS file import

📚 CODING EXAMPLE:
import React, { useState, useEffect } from 'react';
import axios from 'axios';

🎯 YOUR TASK: Write the import statements
Import React hooks, axios, and CSS file
*/

// TODO 1: IMPORT STATEMENTS - Write your imports here:

// YOUR CODE HERE - Import React, hooks, axios, and CSS


/*
🧪 HANDS-ON LAB 2: TYPESCRIPT INTERFACES
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

📚 INTERFACE SYNTAX EXPLAINED:
• interface Name { } - Defines a new type
• property: type - Required property
• property?: type - Optional property (can be undefined)
• number, string, boolean - Basic TypeScript types

📚 CODING EXAMPLE:
interface User {
  id: number;
  name: string;
  email?: string;  // Optional
}

🎯 YOUR TASK: Define the Character interface
Match the data structure from your Flask API
*/

// TODO 2: TYPESCRIPT INTERFACES - Define your Character interface:

// YOUR CODE HERE - Define Character interface with all properties
// 
// interface PaginationInfo {
//   page: number;
//   per_page: number;
//   total: number;
//   pages: number;
//   has_next: boolean;
//   has_prev: boolean;
// }
// 
// interface FilterOptions {
//   crew: string;
//   minPrice: number;
//   maxPrice: number;
//   sortBy: 'name' | 'bounty' | 'current_price' | 'weekly_change';
//   sortOrder: 'asc' | 'desc';
// }

/*
🧪 HANDS-ON LAB 3: REACT STATE MANAGEMENT
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

📚 USESTATE SYNTAX EXPLAINED:
• const [value, setValue] = useState(initialValue)
• value: Current state value
• setValue: Function to update the state
• <Type[]>: TypeScript array type

📚 CODING EXAMPLE:
const [count, setCount] = useState<number>(0);
const [users, setUsers] = useState<User[]>([]);
const [loading, setLoading] = useState<boolean>(true);

🎯 YOUR TASK: Set up component state
Create state for characters, loading, error, and search
*/

// TODO 3: COMPONENT STATE SETUP - Create your component and state:

// YOUR CODE HERE - Create component function and useState hooks
//   //   sortBy: 'name',
//   //   sortOrder: 'asc'
//   // });
//   
//   // Pagination state
//   // const [pagination, setPagination] = useState<PaginationInfo>({
//   //   page: 1,
//   //   per_page: 12,
//   //   total: 0,
//   //   pages: 0,
//   //   has_next: false,
//   //   has_prev: false
//   // });

/*
🧪 HANDS-ON LAB 4: API CALLS WITH AXIOS
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

📚 ASYNC/AWAIT SYNTAX EXPLAINED:
• async function: Function that returns a Promise
• await: Wait for Promise to resolve before continuing
• try/catch: Handle errors that might occur
• axios.get(url): Make HTTP GET request

📚 CODING EXAMPLE:
const fetchData = async () => {
  try {
    const response = await axios.get('/api/data');
    setData(response.data);
  } catch (error) {
    setError('Failed to load');
  }
};

🎯 YOUR TASK: Create API call function
Make request to your Flask backend and handle response
*/

// TODO 4: FETCH CHARACTERS FUNCTION - Create your API call function:

// YOUR CODE HERE - Create fetchCharacters function with async/await
/*
🧪 HANDS-ON LAB 5: USEEFFECT HOOK
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

📚 USEEFFECT SYNTAX EXPLAINED:
• useEffect(() => { code }, [dependencies])
• Empty array []: Run once when component mounts
• [variable]: Run when variable changes
• No array: Run on every render

📚 CODING EXAMPLE:
useEffect(() => {
  fetchData();
}, []); // Run once on mount

useEffect(() => {
  searchUsers();
}, [searchTerm]); // Run when searchTerm changes

🎯 YOUR TASK: Set up useEffect to load data when component mounts
Call your fetchCharacters function when component first loads
*/

// TODO 5: USE EFFECT FOR DATA LOADING - Set up useEffect:

// YOUR CODE HERE - Create useEffect to call fetchCharacters on mount

/*
🧪 HANDS-ON LAB 6: JSX RENDERING
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

📚 JSX SYNTAX EXPLAINED:
• JSX: JavaScript XML - write HTML-like code in JavaScript
• {variable}: Embed JavaScript expressions in JSX
• className: Use instead of class (class is reserved in JS)
• Conditional rendering: {condition ? <div>Yes</div> : <div>No</div>}
• Map arrays: {items.map(item => <div key={item.id}>{item.name}</div>)}

📚 CODING EXAMPLE:
return (
  <div className="container">
    <h1>Title</h1>
    {loading ? <p>Loading...</p> : <p>Data loaded!</p>}
    {items.map(item => (
      <div key={item.id}>{item.name}</div>
    ))}
  </div>
);

🎯 YOUR TASK: Create the JSX return statement
Show loading, error, or character list based on state
*/

// TODO 6: JSX RENDERING - Create your return statement:

// YOUR CODE HERE - Create JSX with conditional rendering for loading/error/characters

// TODO 7: EXPORT COMPONENT - Export your component:

// YOUR CODE HERE - Export default CharacterList

// TODO 7: RENDER LOADING STATE
//   if (loading) {
//     return (
//       <div className="character-list-container">
//         <LoadingSpinner message="Loading One Piece characters..." />
//       </div>
//     );
//   }

// TODO 8: RENDER ERROR STATE
//   if (error) {
//     return (
//       <div className="character-list-container">
//         <ErrorMessage 
//           message={error} 
//           onRetry={handleRefresh}
//         />
//       </div>
//     );
//   }

// TODO 9: MAIN RENDER METHOD
//   return (
//     <div className="character-list-container">
//       {/* Page Header */}
//       <div className="character-list-header">
//         <h1>🏴‍☠️ One Piece Character Market</h1>
//         <p>Trade your favorite pirates and marines!</p>
//       </div>
//       
//       {/* Search and Filter Controls */}
//       <div className="character-list-controls">
//         <SearchBar 
//           value={searchTerm}
//           onChange={handleSearchChange}
//           placeholder="Search characters..."
//         />
//         
//         <FilterPanel 
//           filters={filters}
//           onChange={handleFilterChange}
//         />
//         
//         <button 
//           className="refresh-button"
//           onClick={handleRefresh}
//           title="Refresh data"
//         >
//           🔄 Refresh
//         </button>
//       </div>
//       
//       {/* Character Grid */}
//       <div className="character-grid">
//         {characters.length > 0 ? (
//           characters.map(character => (
//             <CharacterCard 
//               key={character.id}
//               character={character}
//             />
//           ))
//         ) : (
//           <div className="no-characters">
//             <p>No characters found matching your criteria.</p>
//           </div>
//         )}
//       </div>
//       
//       {/* Pagination */}
//       {pagination.pages > 1 && (
//         <Pagination 
//           currentPage={pagination.page}
//           totalPages={pagination.pages}
//           onPageChange={handlePageChange}
//           hasNext={pagination.has_next}
//           hasPrev={pagination.has_prev}
//         />
//       )}
//     </div>
//   );
// };

// TODO 10: EXPORT COMPONENT
// export default CharacterList;

/*
🎯 WHAT EACH PART DOES:

State Management: Manages characters, loading, error, search, and pagination
fetchCharacters: Makes API calls to get character data
Event Handlers: Handle user interactions (search, filter, pagination)
Conditional Rendering: Shows loading, error, or character data
Character Grid: Displays characters in a responsive grid layout
Pagination: Handles large datasets with page navigation

🚀 REACT HOOKS YOU'LL LEARN:

1. useState - Manage component state
2. useEffect - Handle side effects (API calls)
3. useCallback - Optimize function references
4. Custom hooks - Reusable stateful logic
5. useContext - Access global state
6. useMemo - Optimize expensive calculations

📚 COMPONENT PATTERNS:

1. Container vs Presentational - Logic vs UI separation
2. Controlled Components - Form inputs controlled by React
3. Conditional Rendering - Show different UI based on state
4. Event Handling - User interaction responses
5. Props Drilling - Passing data down component tree
6. Component Composition - Building complex UI from simple parts

🔧 API INTEGRATION CONCEPTS:

1. Axios HTTP client - Making API requests
2. Query parameters - URL-based filtering and pagination
3. Error handling - Graceful failure management
4. Loading states - User feedback during async operations
5. Data transformation - Converting API data for UI
6. Caching strategies - Optimizing API calls

CSS STYLING APPROACH:
- CSS Modules or styled-components
- Responsive grid layout
- Mobile-first design
- Loading and error state styling
- Hover effects and animations
- Accessibility considerations

NEXT FILE AFTER THIS: Create Character Card Component! 🚀
*/

/*
═══════════════════════════════════════════════════════════
🏴‍☠️ COMPLETE WORKING CODE - REFERENCE IMPLEMENTATION
═══════════════════════════════════════════════════════════

📚 USE THIS AS REFERENCE WHEN CODING ABOVE SECTIONS
Copy sections from here when you complete each TODO above
This is the complete, working CharacterList component
*/

// COMPLETE WORKING IMPORTS
import React, { useState, useEffect, useCallback } from 'react';
import { Link } from 'react-router-dom';
import axios from 'axios';
import './CharacterList.css';

// COMPLETE WORKING INTERFACES
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

// COMPLETE WORKING COMPONENT
const CharacterListComplete: React.FC = () => {
  // State management
  const [characters, setCharacters] = useState<Character[]>([]);
  const [loading, setLoading] = useState<boolean>(true);
  const [error, setError] = useState<string | null>(null);
  const [searchTerm, setSearchTerm] = useState<string>('');

  // API call function
  const fetchCharacters = useCallback(async () => {
    try {
      setLoading(true);
      setError(null);

      const response = await axios.get('http://localhost:5000/api/characters');
      setCharacters(response.data.characters || []);
    } catch (err) {
      setError('Failed to load characters. Please try again.');
      console.error('Error fetching characters:', err);
    } finally {
      setLoading(false);
    }
  }, []);

  // Load data when component mounts
  useEffect(() => {
    fetchCharacters();
  }, [fetchCharacters]);

  // Filter characters based on search term
  const filteredCharacters = characters.filter(character =>
    character.name.toLowerCase().includes(searchTerm.toLowerCase()) ||
    character.crew.toLowerCase().includes(searchTerm.toLowerCase())
  );

  // Event handlers
  const handleSearchChange = (event: React.ChangeEvent<HTMLInputElement>) => {
    setSearchTerm(event.target.value);
  };

  const handleRefresh = () => {
    fetchCharacters();
  };

  // Render loading state
  if (loading) {
    return (
      <div className="character-list-container">
        <div className="loading-spinner">
          <div className="spinner"></div>
          <p>Loading One Piece characters...</p>
        </div>
      </div>
    );
  }

  // Render error state
  if (error) {
    return (
      <div className="character-list-container">
        <div className="error-message">
          <h3>⚠️ Error Loading Characters</h3>
          <p>{error}</p>
          <button onClick={handleRefresh} className="retry-button">
            Try Again
          </button>
        </div>
      </div>
    );
  }

  // Main render
  return (
    <div className="character-list-container">
      <header className="character-list-header">
        <h1>🏴‍☠️ One Piece Stock Market</h1>
        <p>Trade your favorite One Piece characters!</p>
      </header>

      {/* Search Bar */}
      <div className="search-section">
        <input
          type="text"
          placeholder="Search characters or crews..."
          value={searchTerm}
          onChange={handleSearchChange}
          className="search-input"
        />
        <button onClick={handleRefresh} className="refresh-button">
          🔄 Refresh
        </button>
      </div>

      {/* Characters Grid */}
      <div className="characters-grid">
        {filteredCharacters.length > 0 ? (
          filteredCharacters.map((character) => (
            <div key={character.id} className="character-card">
              <div className="character-header">
                <h3>{character.name}</h3>
                <span className="crew-badge">{character.crew}</span>
              </div>

              <div className="character-stats">
                <div className="stat">
                  <label>Bounty:</label>
                  <span>₿{character.bounty.toLocaleString()}</span>
                </div>
                <div className="stat">
                  <label>Current Price:</label>
                  <span>${character.current_price}</span>
                </div>
                <div className="stat">
                  <label>Market Cap:</label>
                  <span>${character.market_cap.toLocaleString()}</span>
                </div>
                <div className="stat">
                  <label>Weekly Change:</label>
                  <span className={character.weekly_change >= 0 ? 'positive' : 'negative'}>
                    {character.weekly_change >= 0 ? '+' : ''}{character.weekly_change}%
                  </span>
                </div>
              </div>

              <div className="character-actions">
                <Link to={`/character/${character.id}`} className="view-button">
                  View Details
                </Link>
                <button className="trade-button">
                  Trade
                </button>
              </div>
            </div>
          ))
        ) : (
          <div className="no-characters">
            <p>No characters found matching "{searchTerm}"</p>
          </div>
        )}
      </div>

      {/* Stats Footer */}
      <footer className="character-list-footer">
        <p>Showing {filteredCharacters.length} of {characters.length} characters</p>
      </footer>
    </div>
  );
};

export default CharacterListComplete;
