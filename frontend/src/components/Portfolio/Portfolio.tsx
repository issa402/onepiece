/*
🏴‍☠️ PORTFOLIO COMPONENT - LEARN BY CODING
═══════════════════════════════════════════════════════════

🎯 WHAT YOU'LL LEARN BY CODING THIS:
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
✅ Complex state management with multiple data types
✅ Financial calculations and number formatting
✅ Data aggregation and portfolio analytics
✅ Real-time data updates and polling
✅ Advanced array methods (reduce, map, filter)
✅ Custom hooks for reusable logic

📚 FINANCIAL CALCULATIONS YOU'LL USE:
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

1. PORTFOLIO VALUE:
   const totalValue = holdings.reduce((sum, holding) =>
     sum + (holding.quantity * holding.current_price), 0);

2. PROFIT/LOSS:
   const profitLoss = currentValue - totalInvested;
   const profitLossPercent = (profitLoss / totalInvested) * 100;

3. ASSET ALLOCATION:
   const allocation = (holdingValue / totalValue) * 100;

4. NUMBER FORMATTING:
   const formatCurrency = (amount: number) =>
     new Intl.NumberFormat('en-US', {
       style: 'currency',
       currency: 'USD'
     }).format(amount);

🔧 TYPESCRIPT INTERFACES YOU'LL NEED:
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

interface Holding {
  character_id: number;
  character_name: string;
  quantity: number;
  average_price: number;
  current_price: number;
  total_value: number;
  profit_loss: number;
}

interface PortfolioSummary {
  total_value: number;
  total_invested: number;
  total_profit_loss: number;
  profit_loss_percent: number;
}
*/

/*
🧪 HANDS-ON LAB 1: PORTFOLIO IMPORTS
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

📚 WHAT EACH IMPORT DOES:
• React hooks: useState, useEffect for state management
• axios: API calls to get portfolio data
• Link: Navigation to character details

🎯 YOUR TASK: Import required dependencies
*/

// TODO 1: IMPORT STATEMENTS
// YOUR CODE HERE - Import React hooks:


// YOUR CODE HERE - Import Link from react-router-dom:


// YOUR CODE HERE - Import axios:


// YOUR CODE HERE - Import CSS:


/*
🧪 HANDS-ON LAB 2: PORTFOLIO INTERFACES
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

📚 PORTFOLIO DATA STRUCTURE:
• Holding: Individual character investment
• PortfolioSummary: Overall portfolio statistics
• Transaction: Buy/sell history

🎯 YOUR TASK: Define portfolio interfaces
*/

// TODO 2: TYPESCRIPT INTERFACES
// YOUR CODE HERE - Define Holding interface:


// YOUR CODE HERE - Define PortfolioSummary interface:


// YOUR CODE HERE - Define Transaction interface:


/*
🧪 HANDS-ON LAB 3: PORTFOLIO STATE MANAGEMENT
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

📚 PORTFOLIO STATE:
• holdings: Array of user's character investments
• summary: Calculated portfolio totals
• transactions: Trading history
• loading/error: UI states

🎯 YOUR TASK: Set up portfolio state
*/

// TODO 3: COMPONENT DECLARATION AND STATE
// YOUR CODE HERE - Create Portfolio component and state:


/*
🧪 HANDS-ON LAB 4: PORTFOLIO CALCULATIONS
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

📚 FINANCIAL CALCULATIONS:
• Total portfolio value
• Profit/loss calculations
• Percentage changes
• Asset allocation

🎯 YOUR TASK: Calculate portfolio metrics
*/

// TODO 4: PORTFOLIO CALCULATION FUNCTIONS
// YOUR CODE HERE - Create calculatePortfolioSummary function:


// YOUR CODE HERE - Create formatCurrency function:


/*
🧪 HANDS-ON LAB 5: DATA FETCHING
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

📚 PORTFOLIO DATA LOADING:
• Fetch user's holdings from API
• Get current character prices
• Load transaction history

🎯 YOUR TASK: Fetch portfolio data
*/

// TODO 5: DATA FETCHING FUNCTIONS
// YOUR CODE HERE - Create fetchPortfolio function:


// TODO 6: USE EFFECT FOR DATA LOADING
// YOUR CODE HERE - Use useEffect to load portfolio:


/*
🧪 HANDS-ON LAB 6: PORTFOLIO RENDERING
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

📚 PORTFOLIO UI COMPONENTS:
• Portfolio summary with totals
• Holdings table with current values
• Profit/loss indicators
• Asset allocation chart

🎯 YOUR TASK: Render portfolio interface
*/

// TODO 7: COMPONENT RETURN/RENDER
// YOUR CODE HERE - Return JSX with portfolio UI:


// TODO 8: EXPORT COMPONENT
// YOUR CODE HERE - Export the Portfolio component:


/*
═══════════════════════════════════════════════════════════
🏆 COMPLETE CODE SOLUTION (SCROLL DOWN TO CHECK YOUR WORK)
═══════════════════════════════════════════════════════════

import React, { useState, useEffect } from 'react';
import { Link } from 'react-router-dom';
import axios from 'axios';
import './Portfolio.css';

interface Holding {
  character_id: number;
  character_name: string;
  character_crew: string;
  quantity: number;
  average_price: number;
  current_price: number;
  total_value: number;
  profit_loss: number;
  profit_loss_percent: number;
}

interface PortfolioSummary {
  total_value: number;
  total_invested: number;
  total_profit_loss: number;
  profit_loss_percent: number;
  total_holdings: number;
}

interface Transaction {
  id: number;
  character_name: string;
  action: 'buy' | 'sell';
  quantity: number;
  price: number;
  total: number;
  timestamp: string;
}

const Portfolio: React.FC = () => {
  const [holdings, setHoldings] = useState<Holding[]>([]);
  const [summary, setSummary] = useState<PortfolioSummary | null>(null);
  const [transactions, setTransactions] = useState<Transaction[]>([]);
  const [loading, setLoading] = useState<boolean>(true);
  const [error, setError] = useState<string | null>(null);

  const calculatePortfolioSummary = (holdings: Holding[]): PortfolioSummary => {
    const totalValue = holdings.reduce((sum, holding) => sum + holding.total_value, 0);
    const totalInvested = holdings.reduce((sum, holding) =>
      sum + (holding.quantity * holding.average_price), 0);
    const totalProfitLoss = totalValue - totalInvested;
    const profitLossPercent = totalInvested > 0 ? (totalProfitLoss / totalInvested) * 100 : 0;

    return {
      total_value: totalValue,
      total_invested: totalInvested,
      total_profit_loss: totalProfitLoss,
      profit_loss_percent: profitLossPercent,
      total_holdings: holdings.length
    };
  };

  const formatCurrency = (amount: number): string => {
    return new Intl.NumberFormat('en-US', {
      style: 'currency',
      currency: 'USD'
    }).format(amount);
  };

  const formatPercent = (percent: number): string => {
    return `${percent >= 0 ? '+' : ''}${percent.toFixed(2)}%`;
  };

  const fetchPortfolio = async () => {
    try {
      setLoading(true);

      // TODO: Replace with actual user ID from authentication
      const userId = 1;

      const [holdingsResponse, transactionsResponse] = await Promise.all([
        axios.get(`http://localhost:5000/api/portfolio/${userId}/holdings`),
        axios.get(`http://localhost:5000/api/portfolio/${userId}/transactions`)
      ]);

      const holdingsData = holdingsResponse.data;
      setHoldings(holdingsData);
      setSummary(calculatePortfolioSummary(holdingsData));
      setTransactions(transactionsResponse.data);
      setError(null);
    } catch (err) {
      setError('Failed to load portfolio data');
      console.error('Portfolio fetch error:', err);
    } finally {
      setLoading(false);
    }
  };

  useEffect(() => {
    fetchPortfolio();

    // Set up polling for real-time updates
    const interval = setInterval(fetchPortfolio, 30000); // Update every 30 seconds

    return () => clearInterval(interval);
  }, []);

  if (loading) {
    return (
      <div className="portfolio loading">
        <div className="loading-spinner">Loading portfolio...</div>
      </div>
    );
  }

  if (error) {
    return (
      <div className="portfolio error">
        <h2>Error Loading Portfolio</h2>
        <p>{error}</p>
        <button onClick={fetchPortfolio}>Retry</button>
      </div>
    );
  }

  return (
    <div className="portfolio">
      <div className="portfolio-header">
        <h1>My Portfolio</h1>
        <button onClick={fetchPortfolio} className="refresh-button">
          🔄 Refresh
        </button>
      </div>

      {summary && (
        <div className="portfolio-summary">
          <div className="summary-card">
            <h3>Total Value</h3>
            <div className="value">{formatCurrency(summary.total_value)}</div>
          </div>

          <div className="summary-card">
            <h3>Total Invested</h3>
            <div className="value">{formatCurrency(summary.total_invested)}</div>
          </div>

          <div className="summary-card">
            <h3>Profit/Loss</h3>
            <div className={`value ${summary.total_profit_loss >= 0 ? 'positive' : 'negative'}`}>
              {formatCurrency(summary.total_profit_loss)}
            </div>
            <div className={`percent ${summary.profit_loss_percent >= 0 ? 'positive' : 'negative'}`}>
              {formatPercent(summary.profit_loss_percent)}
            </div>
          </div>

          <div className="summary-card">
            <h3>Holdings</h3>
            <div className="value">{summary.total_holdings}</div>
          </div>
        </div>
      )}

      <div className="holdings-section">
        <h2>My Holdings</h2>
        {holdings.length === 0 ? (
          <div className="empty-portfolio">
            <p>You don't have any holdings yet.</p>
            <Link to="/characters" className="browse-button">
              Browse Characters
            </Link>
          </div>
        ) : (
          <div className="holdings-table">
            <div className="table-header">
              <div>Character</div>
              <div>Quantity</div>
              <div>Avg Price</div>
              <div>Current Price</div>
              <div>Total Value</div>
              <div>P&L</div>
              <div>Actions</div>
            </div>

            {holdings.map((holding) => (
              <div key={holding.character_id} className="table-row">
                <div className="character-info">
                  <Link to={`/character/${holding.character_id}`}>
                    <strong>{holding.character_name}</strong>
                    <small>{holding.character_crew}</small>
                  </Link>
                </div>

                <div className="quantity">{holding.quantity}</div>

                <div className="avg-price">
                  {formatCurrency(holding.average_price)}
                </div>

                <div className="current-price">
                  {formatCurrency(holding.current_price)}
                </div>

                <div className="total-value">
                  {formatCurrency(holding.total_value)}
                </div>

                <div className={`profit-loss ${holding.profit_loss >= 0 ? 'positive' : 'negative'}`}>
                  <div>{formatCurrency(holding.profit_loss)}</div>
                  <small>{formatPercent(holding.profit_loss_percent)}</small>
                </div>

                <div className="actions">
                  <Link to={`/character/${holding.character_id}`} className="trade-button">
                    Trade
                  </Link>
                </div>
              </div>
            ))}
          </div>
        )}
      </div>

      <div className="transactions-section">
        <h2>Recent Transactions</h2>
        {transactions.length === 0 ? (
          <p>No transactions yet.</p>
        ) : (
          <div className="transactions-list">
            {transactions.slice(0, 10).map((transaction) => (
              <div key={transaction.id} className="transaction-item">
                <div className="transaction-info">
                  <strong>{transaction.character_name}</strong>
                  <span className={`action ${transaction.action}`}>
                    {transaction.action.toUpperCase()}
                  </span>
                </div>

                <div className="transaction-details">
                  <div>{transaction.quantity} shares @ {formatCurrency(transaction.price)}</div>
                  <div className="total">{formatCurrency(transaction.total)}</div>
                </div>

                <div className="transaction-date">
                  {new Date(transaction.timestamp).toLocaleDateString()}
                </div>
              </div>
            ))}
          </div>
        )}
      </div>
    </div>
  );
};

export default Portfolio;

*/