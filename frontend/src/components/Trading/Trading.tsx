/*
🏴‍☠️ TRADING COMPONENT - LEARN BY CODING
═══════════════════════════════════════════════════════════

🎯 WHAT YOU'LL LEARN BY CODING THIS:
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
✅ Advanced form handling with validation
✅ Real-time calculations and updates
✅ API integration for trading operations
✅ User feedback and confirmation dialogs
✅ Error handling and retry logic
✅ State management for complex forms

📚 TRADING FORM PATTERNS YOU'LL USE:
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

1. FORM VALIDATION:
   const validateTrade = (form: TradeForm) => {
     if (form.quantity <= 0) return 'Quantity must be positive';
     if (form.action === 'sell' && form.quantity > userHoldings) {
       return 'Insufficient shares to sell';
     }
     return null;
   };

2. REAL-TIME CALCULATIONS:
   const totalCost = quantity * currentPrice;
   const estimatedFees = totalCost * 0.001; // 0.1% fee

3. CONFIRMATION DIALOG:
   const confirmTrade = () => {
     return window.confirm(`Confirm ${action} ${quantity} shares?`);
   };

🔧 TYPESCRIPT INTERFACES YOU'LL NEED:
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

interface TradeForm {
  character_id: number;
  action: 'buy' | 'sell';
  quantity: number;
  price_type: 'market' | 'limit';
  limit_price?: number;
}

interface TradeResult {
  success: boolean;
  message: string;
  transaction_id?: number;
}
*/

/*
🧪 HANDS-ON LAB 1: TRADING IMPORTS
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

📚 WHAT EACH IMPORT DOES:
• React hooks: useState, useEffect for form state
• useParams: Get character ID from URL
• axios: API calls for trading operations

🎯 YOUR TASK: Import trading dependencies
*/

// TODO 1: IMPORT STATEMENTS
// YOUR CODE HERE - Import React hooks:


// YOUR CODE HERE - Import React Router hooks:


// YOUR CODE HERE - Import axios:


// YOUR CODE HERE - Import CSS:


/*
🧪 HANDS-ON LAB 2: TRADING INTERFACES
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

📚 TRADING DATA STRUCTURE:
• TradeForm: User's trading input
• TradeResult: API response from trade execution
• Character: Character data for trading

🎯 YOUR TASK: Define trading interfaces
*/

// TODO 2: TYPESCRIPT INTERFACES
// YOUR CODE HERE - Define TradeForm interface:


// YOUR CODE HERE - Define TradeResult interface:


// YOUR CODE HERE - Define Character interface:


/*
🧪 HANDS-ON LAB 3: TRADING STATE MANAGEMENT
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

📚 TRADING STATE:
• tradeForm: User's trading inputs
• character: Character being traded
• userBalance: Available funds
• isSubmitting: Prevent double submissions

🎯 YOUR TASK: Set up trading state
*/

// TODO 3: COMPONENT DECLARATION AND STATE
// YOUR CODE HERE - Create Trading component and state:


/*
🧪 HANDS-ON LAB 4: FORM VALIDATION
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

📚 TRADING VALIDATION:
• Check positive quantities
• Verify sufficient funds for buying
• Verify sufficient shares for selling
• Validate limit prices

🎯 YOUR TASK: Create validation functions
*/

// TODO 4: VALIDATION FUNCTIONS
// YOUR CODE HERE - Create validateTrade function:


// YOUR CODE HERE - Create calculateTradeCost function:


/*
🧪 HANDS-ON LAB 5: TRADING EXECUTION
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

📚 TRADE EXECUTION:
• Submit trade to API
• Handle success/error responses
• Update UI with results
• Reset form after successful trade

🎯 YOUR TASK: Handle trade execution
*/

// TODO 5: TRADING FUNCTIONS
// YOUR CODE HERE - Create executeTrade function:


// TODO 6: FORM HANDLERS
// YOUR CODE HERE - Create form change and submit handlers:


/*
🧪 HANDS-ON LAB 6: TRADING UI
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

📚 TRADING INTERFACE:
• Character information display
• Buy/sell toggle buttons
• Quantity and price inputs
• Real-time cost calculations
• Submit and cancel buttons

🎯 YOUR TASK: Render trading interface
*/

// TODO 7: COMPONENT RETURN/RENDER
// YOUR CODE HERE - Return JSX with trading UI:


// TODO 8: EXPORT COMPONENT
// YOUR CODE HERE - Export the Trading component:


/*
═══════════════════════════════════════════════════════════
🏆 COMPLETE CODE SOLUTION (SCROLL DOWN TO CHECK YOUR WORK)
═══════════════════════════════════════════════════════════

import React, { useState, useEffect } from 'react';
import { useParams, useNavigate } from 'react-router-dom';
import axios from 'axios';
import './Trading.css';

interface TradeForm {
  character_id: number;
  action: 'buy' | 'sell';
  quantity: number;
  price_type: 'market' | 'limit';
  limit_price?: number;
}

interface TradeResult {
  success: boolean;
  message: string;
  transaction_id?: number;
  new_balance?: number;
}

interface Character {
  id: number;
  name: string;
  crew: string;
  current_price: number;
  bounty: number;
  description: string;
  image_url?: string;
}

interface UserHolding {
  character_id: number;
  quantity: number;
  average_price: number;
}

const Trading: React.FC = () => {
  const [tradeForm, setTradeForm] = useState<TradeForm>({
    character_id: 0,
    action: 'buy',
    quantity: 1,
    price_type: 'market'
  });

  const [character, setCharacter] = useState<Character | null>(null);
  const [userBalance, setUserBalance] = useState<number>(0);
  const [userHolding, setUserHolding] = useState<UserHolding | null>(null);
  const [isSubmitting, setIsSubmitting] = useState<boolean>(false);
  const [tradeResult, setTradeResult] = useState<TradeResult | null>(null);
  const [loading, setLoading] = useState<boolean>(true);
  const [error, setError] = useState<string | null>(null);

  const { id } = useParams<{ id: string }>();
  const navigate = useNavigate();

  const validateTrade = (form: TradeForm): string | null => {
    if (form.quantity <= 0) {
      return 'Quantity must be greater than 0';
    }

    if (form.action === 'buy') {
      const totalCost = calculateTradeCost(form);
      if (totalCost > userBalance) {
        return 'Insufficient funds for this purchase';
      }
    }

    if (form.action === 'sell') {
      const availableShares = userHolding?.quantity || 0;
      if (form.quantity > availableShares) {
        return `You only own ${availableShares} shares`;
      }
    }

    if (form.price_type === 'limit' && (!form.limit_price || form.limit_price <= 0)) {
      return 'Limit price must be greater than 0';
    }

    return null;
  };

  const calculateTradeCost = (form: TradeForm): number => {
    const price = form.price_type === 'market'
      ? character?.current_price || 0
      : form.limit_price || 0;

    const subtotal = form.quantity * price;
    const fee = subtotal * 0.001; // 0.1% trading fee

    return subtotal + fee;
  };

  const executeTrade = async (form: TradeForm): Promise<TradeResult> => {
    try {
      const response = await axios.post('http://localhost:5000/api/trades', {
        user_id: 1, // TODO: Get from authentication
        character_id: form.character_id,
        action: form.action,
        quantity: form.quantity,
        price_type: form.price_type,
        limit_price: form.limit_price
      });

      return {
        success: true,
        message: `Successfully ${form.action === 'buy' ? 'bought' : 'sold'} ${form.quantity} shares`,
        transaction_id: response.data.transaction_id,
        new_balance: response.data.new_balance
      };
    } catch (err: any) {
      return {
        success: false,
        message: err.response?.data?.message || 'Trade execution failed'
      };
    }
  };

  const handleFormChange = (e: React.ChangeEvent<HTMLInputElement | HTMLSelectElement>) => {
    const { name, value } = e.target;
    setTradeForm(prev => ({
      ...prev,
      [name]: name === 'quantity' || name === 'limit_price'
        ? parseFloat(value) || 0
        : value
    }));

    // Clear previous results when form changes
    setTradeResult(null);
  };

  const handleActionChange = (action: 'buy' | 'sell') => {
    setTradeForm(prev => ({ ...prev, action }));
    setTradeResult(null);
  };

  const handleSubmit = async (e: React.FormEvent) => {
    e.preventDefault();

    const validationError = validateTrade(tradeForm);
    if (validationError) {
      setTradeResult({
        success: false,
        message: validationError
      });
      return;
    }

    const confirmed = window.confirm(
      `Confirm ${tradeForm.action} ${tradeForm.quantity} shares of ${character?.name} ` +
      `for ${formatCurrency(calculateTradeCost(tradeForm))}?`
    );

    if (!confirmed) return;

    setIsSubmitting(true);
    const result = await executeTrade(tradeForm);
    setTradeResult(result);

    if (result.success) {
      // Update user balance
      if (result.new_balance !== undefined) {
        setUserBalance(result.new_balance);
      }

      // Reset form
      setTradeForm(prev => ({
        ...prev,
        quantity: 1,
        limit_price: undefined
      }));

      // Refresh user holdings
      fetchUserData();
    }

    setIsSubmitting(false);
  };

  const formatCurrency = (amount: number): string => {
    return new Intl.NumberFormat('en-US', {
      style: 'currency',
      currency: 'USD'
    }).format(amount);
  };

  const fetchCharacterData = async (characterId: string) => {
    try {
      const response = await axios.get(`http://localhost:5000/api/characters/${characterId}`);
      setCharacter(response.data);
      setTradeForm(prev => ({ ...prev, character_id: parseInt(characterId) }));
    } catch (err) {
      setError('Character not found');
    }
  };

  const fetchUserData = async () => {
    try {
      const userId = 1; // TODO: Get from authentication

      const [balanceResponse, holdingResponse] = await Promise.all([
        axios.get(`http://localhost:5000/api/users/${userId}/balance`),
        axios.get(`http://localhost:5000/api/portfolio/${userId}/holdings/${tradeForm.character_id}`)
      ]);

      setUserBalance(balanceResponse.data.balance);
      setUserHolding(holdingResponse.data || null);
    } catch (err) {
      console.error('Failed to fetch user data:', err);
    }
  };

  useEffect(() => {
    if (id) {
      Promise.all([
        fetchCharacterData(id),
        fetchUserData()
      ]).finally(() => setLoading(false));
    }
  }, [id]);

  if (loading) {
    return (
      <div className="trading loading">
        <div className="loading-spinner">Loading trading interface...</div>
      </div>
    );
  }

  if (error || !character) {
    return (
      <div className="trading error">
        <h2>Character Not Found</h2>
        <p>{error}</p>
        <button onClick={() => navigate('/characters')}>
          Back to Characters
        </button>
      </div>
    );
  }

  const tradeCost = calculateTradeCost(tradeForm);
  const availableShares = userHolding?.quantity || 0;

  return (
    <div className="trading">
      <div className="trading-header">
        <button className="back-button" onClick={() => navigate(`/character/${character.id}`)}>
          ← Back to {character.name}
        </button>
        <h1>Trade {character.name}</h1>
      </div>

      <div className="trading-content">
        <div className="character-info">
          <div className="character-image">
            {character.image_url ? (
              <img src={character.image_url} alt={character.name} />
            ) : (
              <div className="placeholder-image">🏴‍☠️</div>
            )}
          </div>

          <div className="character-details">
            <h2>{character.name}</h2>
            <p className="crew">{character.crew}</p>
            <div className="price">
              <label>Current Price:</label>
              <span>{formatCurrency(character.current_price)}</span>
            </div>
            <div className="bounty">
              <label>Bounty:</label>
              <span>₿{character.bounty.toLocaleString()}</span>
            </div>
          </div>
        </div>

        <div className="user-info">
          <div className="balance">
            <label>Available Balance:</label>
            <span>{formatCurrency(userBalance)}</span>
          </div>

          <div className="holdings">
            <label>Your Holdings:</label>
            <span>{availableShares} shares</span>
            {userHolding && (
              <small>Avg. Price: {formatCurrency(userHolding.average_price)}</small>
            )}
          </div>
        </div>

        <form onSubmit={handleSubmit} className="trading-form">
          <div className="action-selector">
            <button
              type="button"
              className={`action-button ${tradeForm.action === 'buy' ? 'active' : ''}`}
              onClick={() => handleActionChange('buy')}
            >
              BUY
            </button>
            <button
              type="button"
              className={`action-button ${tradeForm.action === 'sell' ? 'active' : ''}`}
              onClick={() => handleActionChange('sell')}
              disabled={availableShares === 0}
            >
              SELL
            </button>
          </div>

          <div className="form-group">
            <label htmlFor="quantity">Quantity:</label>
            <input
              type="number"
              id="quantity"
              name="quantity"
              min="1"
              max={tradeForm.action === 'sell' ? availableShares : undefined}
              value={tradeForm.quantity}
              onChange={handleFormChange}
              required
            />
          </div>

          <div className="form-group">
            <label htmlFor="price_type">Order Type:</label>
            <select
              id="price_type"
              name="price_type"
              value={tradeForm.price_type}
              onChange={handleFormChange}
            >
              <option value="market">Market Order</option>
              <option value="limit">Limit Order</option>
            </select>
          </div>

          {tradeForm.price_type === 'limit' && (
            <div className="form-group">
              <label htmlFor="limit_price">Limit Price:</label>
              <input
                type="number"
                id="limit_price"
                name="limit_price"
                step="0.01"
                min="0.01"
                value={tradeForm.limit_price || ''}
                onChange={handleFormChange}
                placeholder="Enter limit price"
                required
              />
            </div>
          )}

          <div className="trade-summary">
            <div className="summary-row">
              <span>Shares:</span>
              <span>{tradeForm.quantity}</span>
            </div>
            <div className="summary-row">
              <span>Price per share:</span>
              <span>
                {tradeForm.price_type === 'market'
                  ? formatCurrency(character.current_price)
                  : formatCurrency(tradeForm.limit_price || 0)
                }
              </span>
            </div>
            <div className="summary-row">
              <span>Trading fee (0.1%):</span>
              <span>{formatCurrency(tradeCost * 0.001)}</span>
            </div>
            <div className="summary-row total">
              <span>Total {tradeForm.action === 'buy' ? 'Cost' : 'Proceeds'}:</span>
              <span>{formatCurrency(tradeCost)}</span>
            </div>
          </div>

          {tradeResult && (
            <div className={`trade-result ${tradeResult.success ? 'success' : 'error'}`}>
              {tradeResult.message}
            </div>
          )}

          <button
            type="submit"
            className={`submit-button ${tradeForm.action}`}
            disabled={isSubmitting}
          >
            {isSubmitting
              ? 'Processing...'
              : `${tradeForm.action.toUpperCase()} ${tradeForm.quantity} Shares`
            }
          </button>
        </form>
      </div>
    </div>
  );
};

export default Trading;

*/