/*
🏴‍☠️ CHARACTER DETAIL COMPONENT - LEARN BY CODING
═══════════════════════════════════════════════════════════

🎯 WHAT YOU'LL LEARN BY CODING THIS:
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
✅ React Router parameters and dynamic routing
✅ useParams hook for URL parameter extraction
✅ Conditional rendering and loading states
✅ Form handling and user input validation
✅ API calls with dynamic parameters
✅ Error handling for missing data

📚 REACT ROUTER SYNTAX YOU'LL USE:
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

1. URL PARAMETERS:
   // Route: /character/:id
   const { id } = useParams<{ id: string }>();

2. NAVIGATION:
   const navigate = useNavigate();
   navigate('/characters');

3. DYNAMIC API CALLS:
   const fetchCharacter = async (id: string) => {
     const response = await axios.get(`/api/characters/${id}`);
     return response.data;
   };

4. CONDITIONAL RENDERING:
   {character ? (
     <div>{character.name}</div>
   ) : (
     <div>Character not found</div>
   )}

5. FORM HANDLING:
   const handleSubmit = (e: React.FormEvent) => {
     e.preventDefault();
     // Handle form submission
   };

🔧 TYPESCRIPT INTERFACES YOU'LL NEED:
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

interface Character {
  id: number;
  name: string;
  crew: string;
  bounty: number;
  current_price: number;
  description: string;
  image_url?: string;
}

interface TradeForm {
  quantity: number;
  action: 'buy' | 'sell';
}
*/

/*
🧪 HANDS-ON LAB 1: REACT ROUTER IMPORTS
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

📚 WHAT EACH IMPORT DOES:
• useParams: Extract parameters from URL (like character ID)
• useNavigate: Programmatically navigate between pages
• useState/useEffect: Manage component state and side effects
• axios: Make HTTP requests to your Flask API

🎯 YOUR TASK: Import the required dependencies
*/

// TODO 1: IMPORT STATEMENTS
// EXAMPLE: import { useParams } from 'react-router-dom';
// YOUR CODE HERE - Import React hooks:


// YOUR CODE HERE - Import React Router hooks:


// YOUR CODE HERE - Import axios:


// YOUR CODE HERE - Import CSS:


/*
🧪 HANDS-ON LAB 2: TYPESCRIPT INTERFACES
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

📚 WHY INTERFACES FOR DETAIL VIEW:
• Character: Full character data from API
• TradeForm: User input for buying/selling
• RouteParams: URL parameters type safety

🎯 YOUR TASK: Define interfaces for character detail
*/

// TODO 2: TYPESCRIPT INTERFACES
// YOUR CODE HERE - Define Character interface:


// YOUR CODE HERE - Define TradeForm interface:


// YOUR CODE HERE - Define RouteParams interface:


/*
🧪 HANDS-ON LAB 3: COMPONENT STATE SETUP
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

📚 STATE FOR DETAIL VIEW:
• character: Store the character data
• loading: Show loading spinner
• error: Handle API errors
• tradeForm: Handle buy/sell form data

🎯 YOUR TASK: Set up component state
*/

// TODO 3: COMPONENT DECLARATION AND STATE
// EXAMPLE: const CharacterDetail: React.FC = () => {
// YOUR CODE HERE - Create component and state:


/*
🧪 HANDS-ON LAB 4: URL PARAMETER EXTRACTION
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

📚 EXTRACTING URL PARAMETERS:
• useParams extracts parameters from URL
• URL like /character/1 gives us { id: '1' }
• Convert string to number for API calls

🎯 YOUR TASK: Extract character ID from URL
*/

// TODO 4: URL PARAMETER EXTRACTION
// YOUR CODE HERE - Extract character ID from URL:


/*
🧪 HANDS-ON LAB 5: API DATA FETCHING
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

📚 FETCHING CHARACTER DATA:
• useEffect runs when component mounts
• Fetch character data based on ID from URL
• Handle loading states and errors

🎯 YOUR TASK: Fetch character data from API
*/

// TODO 5: DATA FETCHING FUNCTION
// YOUR CODE HERE - Create fetchCharacter function:


// TODO 6: USE EFFECT FOR DATA LOADING
// YOUR CODE HERE - Use useEffect to load data:


/*
🧪 HANDS-ON LAB 6: FORM HANDLING
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

📚 HANDLING TRADE FORMS:
• Controlled components with value and onChange
• Form validation before submission
• API calls for buy/sell actions

🎯 YOUR TASK: Handle buy/sell form
*/

// TODO 7: FORM HANDLERS
// YOUR CODE HERE - Create form change handler:


// YOUR CODE HERE - Create form submit handler:


/*
🧪 HANDS-ON LAB 7: COMPONENT RENDER
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

📚 CONDITIONAL RENDERING:
• Show loading spinner while fetching
• Show error message if API fails
• Show character details when loaded
• Show 404 if character not found

🎯 YOUR TASK: Render the component UI
*/

// TODO 8: COMPONENT RETURN/RENDER
// YOUR CODE HERE - Return JSX with conditional rendering:


// TODO 9: EXPORT COMPONENT
// YOUR CODE HERE - Export the component:


/*
═══════════════════════════════════════════════════════════
🏆 COMPLETE CODE SOLUTION (SCROLL DOWN TO CHECK YOUR WORK)
═══════════════════════════════════════════════════════════

import React, { useState, useEffect } from 'react';
import { useParams, useNavigate } from 'react-router-dom';
import axios from 'axios';
import './CharacterDetail.css';

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
}

interface TradeForm {
  quantity: number;
  action: 'buy' | 'sell';
}

interface RouteParams {
  id: string;
}

const CharacterDetail: React.FC = () => {
  const [character, setCharacter] = useState<Character | null>(null);
  const [loading, setLoading] = useState<boolean>(true);
  const [error, setError] = useState<string | null>(null);
  const [tradeForm, setTradeForm] = useState<TradeForm>({
    quantity: 1,
    action: 'buy'
  });

  const { id } = useParams<RouteParams>();
  const navigate = useNavigate();

  const fetchCharacter = async (characterId: string) => {
    try {
      setLoading(true);
      const response = await axios.get(`http://localhost:5000/api/characters/${characterId}`);
      setCharacter(response.data);
      setError(null);
    } catch (err) {
      setError('Character not found');
      setCharacter(null);
    } finally {
      setLoading(false);
    }
  };

  useEffect(() => {
    if (id) {
      fetchCharacter(id);
    }
  }, [id]);

  const handleFormChange = (e: React.ChangeEvent<HTMLInputElement | HTMLSelectElement>) => {
    const { name, value } = e.target;
    setTradeForm(prev => ({
      ...prev,
      [name]: name === 'quantity' ? parseInt(value) : value
    }));
  };

  const handleTradeSubmit = async (e: React.FormEvent) => {
    e.preventDefault();
    try {
      // TODO: Implement actual trading API call
      console.log('Trade submitted:', tradeForm, 'for character:', character?.name);
      alert(`${tradeForm.action} ${tradeForm.quantity} shares of ${character?.name}`);
    } catch (err) {
      console.error('Trade failed:', err);
    }
  };

  if (loading) {
    return (
      <div className="character-detail loading">
        <div className="loading-spinner">Loading character...</div>
      </div>
    );
  }

  if (error || !character) {
    return (
      <div className="character-detail error">
        <h2>Character Not Found</h2>
        <p>{error}</p>
        <button onClick={() => navigate('/characters')}>
          Back to Characters
        </button>
      </div>
    );
  }

  return (
    <div className="character-detail">
      <button className="back-button" onClick={() => navigate('/characters')}>
        ← Back to Characters
      </button>

      <div className="character-header">
        <div className="character-image">
          {character.image_url ? (
            <img src={character.image_url} alt={character.name} />
          ) : (
            <div className="placeholder-image">🏴‍☠️</div>
          )}
        </div>

        <div className="character-info">
          <h1>{character.name}</h1>
          <p className="crew">{character.crew}</p>
          <div className="stats">
            <div className="stat">
              <label>Current Price:</label>
              <span className="price">${character.current_price.toFixed(2)}</span>
            </div>
            <div className="stat">
              <label>Bounty:</label>
              <span className="bounty">₿{character.bounty.toLocaleString()}</span>
            </div>
            <div className="stat">
              <label>Market Cap:</label>
              <span className="market-cap">${character.market_cap.toLocaleString()}</span>
            </div>
            <div className="stat">
              <label>Weekly Change:</label>
              <span className={`change ${character.weekly_change >= 0 ? 'positive' : 'negative'}`}>
                {character.weekly_change >= 0 ? '+' : ''}{character.weekly_change.toFixed(2)}%
              </span>
            </div>
          </div>
        </div>
      </div>

      <div className="character-description">
        <h3>About {character.name}</h3>
        <p>{character.description}</p>
      </div>

      <div className="trading-section">
        <h3>Trade {character.name}</h3>
        <form onSubmit={handleTradeSubmit} className="trade-form">
          <div className="form-group">
            <label htmlFor="action">Action:</label>
            <select
              id="action"
              name="action"
              value={tradeForm.action}
              onChange={handleFormChange}
            >
              <option value="buy">Buy</option>
              <option value="sell">Sell</option>
            </select>
          </div>

          <div className="form-group">
            <label htmlFor="quantity">Quantity:</label>
            <input
              type="number"
              id="quantity"
              name="quantity"
              min="1"
              value={tradeForm.quantity}
              onChange={handleFormChange}
            />
          </div>

          <div className="trade-summary">
            <p>
              Total: ${(character.current_price * tradeForm.quantity).toFixed(2)}
            </p>
          </div>

          <button type="submit" className={`trade-button ${tradeForm.action}`}>
            {tradeForm.action.toUpperCase()} {tradeForm.quantity} shares
          </button>
        </form>
      </div>
    </div>
  );
};

export default CharacterDetail;

*/