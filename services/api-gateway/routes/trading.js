/*
🏴‍☠️ API GATEWAY - TRADING ROUTES
═══════════════════════════════════════════════════════════════════════════════

🎯 WHAT YOU'RE BUILDING:
This file contains all trading-related API routes for your API Gateway.
These routes handle buy/sell operations, portfolio management, and market data.

📚 LEARNING OBJECTIVES:
- Trading system API design
- Transaction handling and validation
- Real-time market data endpoints
- Portfolio management APIs
- Trade execution and cancellation
- Financial data security

🔗 CONNECTS TO:
- services/api-gateway/routes/characters.js (previous file you completed)
- services/trading-service/ (C# trading service - proxies requests here)
- services/price-engine/ (price calculation service)
- frontend/src/components/TradingInterface.tsx (frontend trading UI)
*/

const express = require('express');
const { createProxyMiddleware } = require('http-proxy-middleware');
const router = express.Router();

// Trading Service URL (C# service)
const TRADING_SERVICE_URL = process.env.TRADING_SERVICE_URL || 'http://localhost:5002';
// Price Engine URL
const PRICE_ENGINE_URL = process.env.PRICE_ENGINE_URL || 'http://localhost:5003';

// TODO 1: TRADE EXECUTION ENDPOINT
// ═══════════════════════════════════════════════════════════
/*
🎯 YOUR TASK: Create POST /api/trades endpoint for executing trades

This endpoint should:
1. Require authentication
2. Validate trade parameters
3. Check user balance/holdings
4. Execute trade via Trading Service
5. Log all trade attempts
*/

// POST /api/trades - Execute a buy or sell trade
router.post('/', (req, res, next) => {
    // Authentication check
    if (!req.user) {
        return res.status(401).json({
            error: 'Authentication required',
            message: 'Please log in to execute trades',
            timestamp: new Date().toISOString()
        });
    }
    
    // Validate trade parameters
    const { characterId, action, quantity, price } = req.body;
    
    if (!characterId || !action || !quantity || !price) {
        return res.status(400).json({
            error: 'Missing trade parameters',
            message: 'characterId, action, quantity, and price are required',
            timestamp: new Date().toISOString()
        });
    }
    
    if (!['buy', 'sell'].includes(action)) {
        return res.status(400).json({
            error: 'Invalid trade action',
            message: 'Action must be either "buy" or "sell"',
            timestamp: new Date().toISOString()
        });
    }
    
    if (quantity <= 0 || price <= 0) {
        return res.status(400).json({
            error: 'Invalid trade values',
            message: 'Quantity and price must be positive numbers',
            timestamp: new Date().toISOString()
        });
    }
    
    // Log trade attempt
    console.log(`💰 Trade attempt: User ${req.user.id} wants to ${action} ${quantity} of character ${characterId} at ${price}`);
    
    next();
}, createProxyMiddleware({
    target: TRADING_SERVICE_URL,
    changeOrigin: true,
    pathRewrite: {
        '^/api/trades': '/api/trades'
    },
    onProxyReq: (proxyReq, req, res) => {
        // Add user context to trading service request
        proxyReq.setHeader('X-User-ID', req.user.id);
        proxyReq.setHeader('X-User-Email', req.user.email);
        proxyReq.setHeader('X-Request-ID', req.headers['x-request-id'] || 'unknown');
        
        console.log(`📡 Proxying trade execution to Trading Service for user ${req.user.id}`);
    },
    onProxyRes: (proxyRes, req, res) => {
        console.log(`💰 Trading Service responded with status: ${proxyRes.statusCode}`);
        
        // Log successful trades
        if (proxyRes.statusCode === 200 || proxyRes.statusCode === 201) {
            console.log(`✅ Trade executed successfully for user ${req.user.id}`);
        }
    },
    onError: (err, req, res) => {
        console.error('❌ Trading Service proxy error:', err.message);
        res.status(503).json({
            error: 'Trading Service unavailable',
            message: 'Unable to execute trade at this time',
            timestamp: new Date().toISOString()
        });
    }
}));

// TODO 2: USER TRADE HISTORY ENDPOINT
// ═══════════════════════════════════════════════════════════
/*
🎯 YOUR TASK: Create GET /api/trades/:userId endpoint

This endpoint should:
1. Require authentication
2. Verify user can access requested data
3. Support pagination and filtering
4. Return formatted trade history
*/

// GET /api/trades/:userId - Get user's trade history
router.get('/:userId', (req, res, next) => {
    const requestedUserId = req.params.userId;
    
    // Authentication check
    if (!req.user) {
        return res.status(401).json({
            error: 'Authentication required',
            message: 'Please log in to view trade history',
            timestamp: new Date().toISOString()
        });
    }
    
    // Authorization check - users can only view their own trades
    if (req.user.id !== parseInt(requestedUserId) && req.user.role !== 'admin') {
        return res.status(403).json({
            error: 'Access denied',
            message: 'You can only view your own trade history',
            timestamp: new Date().toISOString()
        });
    }
    
    console.log(`📊 Fetching trade history for user ${requestedUserId}`);
    
    next();
}, createProxyMiddleware({
    target: TRADING_SERVICE_URL,
    changeOrigin: true,
    pathRewrite: {
        '^/api/trades': '/api/trades'
    },
    onProxyReq: (proxyReq, req, res) => {
        proxyReq.setHeader('X-User-ID', req.user.id);
        proxyReq.setHeader('X-User-Role', req.user.role || 'user');
    }
}));

// TODO 3: USER PORTFOLIO ENDPOINT
// ═══════════════════════════════════════════════════════════
/*
🎯 YOUR TASK: Create GET /api/portfolio/:userId endpoint

This endpoint should:
1. Require authentication
2. Verify user access rights
3. Get current portfolio holdings
4. Include current market values
*/

// GET /api/portfolio/:userId - Get user's current portfolio
router.get('/portfolio/:userId', (req, res, next) => {
    const requestedUserId = req.params.userId;
    
    // Authentication and authorization checks
    if (!req.user) {
        return res.status(401).json({
            error: 'Authentication required',
            message: 'Please log in to view portfolio',
            timestamp: new Date().toISOString()
        });
    }
    
    if (req.user.id !== parseInt(requestedUserId) && req.user.role !== 'admin') {
        return res.status(403).json({
            error: 'Access denied',
            message: 'You can only view your own portfolio',
            timestamp: new Date().toISOString()
        });
    }
    
    console.log(`💼 Fetching portfolio for user ${requestedUserId}`);
    
    next();
}, createProxyMiddleware({
    target: TRADING_SERVICE_URL,
    changeOrigin: true,
    pathRewrite: {
        '^/api/trades/portfolio': '/api/portfolio'
    },
    onProxyReq: (proxyReq, req, res) => {
        proxyReq.setHeader('X-User-ID', req.user.id);
    },
    onProxyRes: (proxyRes, req, res) => {
        // Add caching for portfolio data (short cache due to price changes)
        if (proxyRes.statusCode === 200) {
            res.setHeader('Cache-Control', 'private, max-age=30'); // 30 seconds
        }
    }
}));

// TODO 4: TRADE CANCELLATION ENDPOINT
// ═══════════════════════════════════════════════════════════
/*
🎯 YOUR TASK: Create POST /api/trades/cancel endpoint

This endpoint should:
1. Require authentication
2. Validate trade ID and ownership
3. Check if trade can be cancelled
4. Execute cancellation via Trading Service
*/

// POST /api/trades/cancel - Cancel a pending trade
router.post('/cancel', (req, res, next) => {
    if (!req.user) {
        return res.status(401).json({
            error: 'Authentication required',
            message: 'Please log in to cancel trades',
            timestamp: new Date().toISOString()
        });
    }
    
    const { tradeId } = req.body;
    
    if (!tradeId) {
        return res.status(400).json({
            error: 'Missing trade ID',
            message: 'Trade ID is required for cancellation',
            timestamp: new Date().toISOString()
        });
    }
    
    console.log(`❌ Trade cancellation request: User ${req.user.id} wants to cancel trade ${tradeId}`);
    
    next();
}, createProxyMiddleware({
    target: TRADING_SERVICE_URL,
    changeOrigin: true,
    pathRewrite: {
        '^/api/trades/cancel': '/api/trades/cancel'
    },
    onProxyReq: (proxyReq, req, res) => {
        proxyReq.setHeader('X-User-ID', req.user.id);
    }
}));

// TODO 5: MARKET PRICES ENDPOINT
// ═══════════════════════════════════════════════════════════
/*
🎯 YOUR TASK: Create GET /api/market/prices endpoint

This endpoint should:
1. Get current market prices from Price Engine
2. Support filtering by character IDs
3. Include price change data
4. Add appropriate caching
*/

// GET /api/market/prices - Get current market prices
router.get('/market/prices', createProxyMiddleware({
    target: PRICE_ENGINE_URL,
    changeOrigin: true,
    pathRewrite: {
        '^/api/trades/market/prices': '/api/prices'
    },
    onProxyReq: (proxyReq, req, res) => {
        console.log(`📈 Fetching current market prices from Price Engine`);
    },
    onProxyRes: (proxyRes, req, res) => {
        // Short cache for price data (prices change frequently)
        if (proxyRes.statusCode === 200) {
            res.setHeader('Cache-Control', 'public, max-age=10'); // 10 seconds
        }
    },
    onError: (err, req, res) => {
        console.error('❌ Price Engine proxy error:', err.message);
        res.status(503).json({
            error: 'Price Engine unavailable',
            message: 'Unable to fetch current prices',
            timestamp: new Date().toISOString()
        });
    }
}));

// TODO 6: MARKET STATISTICS ENDPOINT
// ═══════════════════════════════════════════════════════════
/*
🎯 YOUR TASK: Create GET /api/market/stats endpoint

This endpoint should:
1. Get market statistics and trends
2. Include volume and price change data
3. Support time range filtering
4. Cache appropriately
*/

// GET /api/market/stats - Get market statistics
router.get('/market/stats', createProxyMiddleware({
    target: PRICE_ENGINE_URL,
    changeOrigin: true,
    pathRewrite: {
        '^/api/trades/market/stats': '/api/stats'
    },
    onProxyReq: (proxyReq, req, res) => {
        console.log(`📊 Fetching market statistics from Price Engine`);
    },
    onProxyRes: (proxyRes, req, res) => {
        // Longer cache for statistics
        if (proxyRes.statusCode === 200) {
            res.setHeader('Cache-Control', 'public, max-age=60'); // 1 minute
        }
    }
}));

// Error handling middleware for trading routes
router.use((err, req, res, next) => {
    console.error('❌ Trading routes error:', err);
    
    let statusCode = 500;
    let errorMessage = 'Internal server error';
    
    if (err.code === 'ECONNREFUSED') {
        statusCode = 503;
        errorMessage = 'Trading Service unavailable';
    } else if (err.status) {
        statusCode = err.status;
        errorMessage = err.message;
    }
    
    res.status(statusCode).json({
        error: errorMessage,
        path: req.path,
        method: req.method,
        timestamp: new Date().toISOString(),
        requestId: req.headers['x-request-id'] || 'unknown'
    });
});

module.exports = router;

/*
═══════════════════════════════════════════════════════════════════════════════
🎯 WHAT'S NEXT? YOUR NEXT IMPLEMENTATION STEP AFTER TRADING.JS
═══════════════════════════════════════════════════════════════════════════════

🏴‍☠️ CONGRATULATIONS! You've completed the Trading Routes file!

📚 WHAT YOU JUST BUILT:
✅ Trade execution endpoint with validation
✅ User trade history with authorization
✅ Portfolio management endpoints
✅ Trade cancellation functionality
✅ Market prices from Price Engine
✅ Market statistics and trends
✅ Comprehensive error handling
✅ Authentication and authorization checks

🎯 YOUR NEXT IMPLEMENTATION STEP (FOLLOW THIS EXACT ORDER):

═══════════════════════════════════════════════════════════════════════════════
📍 NEXT FILE: services/api-gateway/middleware/auth.js
═══════════════════════════════════════════════════════════════════════════════

🔥 CREATE THIS FILE NEXT: services/api-gateway/middleware/auth.js
⏱️ TIME: 30-45 minutes
🎯 PURPOSE: Create JWT authentication middleware for your API Gateway

WHAT YOU'LL CREATE IN auth.js:
• JWT token verification middleware
• User authentication and authorization
• Token refresh functionality
• Role-based access control
• Security headers and validation

AFTER COMPLETING auth.js, THAT FILE WILL TELL YOU:
→ Next step: Test your complete API Gateway OR start Character Service

═══════════════════════════════════════════════════════════════════════════════
🧪 TEST THIS FILE FIRST:
═══════════════════════════════════════════════════════════════════════════════

□ Import this file in server.js: app.use('/api/trades', require('./routes/trading'));
□ Start API Gateway: node server.js
□ Test endpoints (you'll need authentication for most):
  - curl http://localhost:3000/api/trades/market/prices
  - curl http://localhost:3000/api/trades/market/stats

If these work, proceed to create auth.js!

🚀 Keep building your legendary One Piece trading platform! ⚔️
*/
