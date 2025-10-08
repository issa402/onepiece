/*
🏴‍☠️ API GATEWAY - CHARACTER ROUTES
═══════════════════════════════════════════════════════════════════════════════

🎯 WHAT YOU'RE BUILDING:
This file contains all character-related API routes for your API Gateway.
These routes will proxy requests to the Character Service microservice.

📚 LEARNING OBJECTIVES:
- Express.js routing patterns
- HTTP proxy middleware
- Request/response transformation
- Error handling for microservices
- API endpoint design
- Service-to-service communication

🔗 CONNECTS TO:
- services/api-gateway/server.js (imports this file)
- services/character-service/app.py (proxies requests to this service)
- frontend/src/services/api.ts (frontend calls these endpoints)
*/

const express = require('express');
const { createProxyMiddleware } = require('http-proxy-middleware');
const router = express.Router();

// Character Service URL (from environment or default)
const CHARACTER_SERVICE_URL = process.env.CHARACTER_SERVICE_URL || 'http://localhost:5001';

// TODO 1: CHARACTER LIST ENDPOINT
// ═══════════════════════════════════════════════════════════
/*
🎯 YOUR TASK: Create GET /api/characters endpoint

This endpoint should:
1. Proxy requests to Character Service
2. Handle pagination parameters
3. Add request logging
4. Handle service errors gracefully
*/

// GET /api/characters - List all characters with pagination
router.get('/', createProxyMiddleware({
    target: CHARACTER_SERVICE_URL,
    changeOrigin: true,
    pathRewrite: {
        '^/api/characters': '/api/characters'
    },
    onProxyReq: (proxyReq, req, res) => {
        console.log(`📡 Proxying GET /api/characters to Character Service`);
        
        // Add request headers
        proxyReq.setHeader('X-Forwarded-For', req.ip);
        proxyReq.setHeader('X-Request-ID', req.headers['x-request-id'] || 'unknown');
    },
    onProxyRes: (proxyRes, req, res) => {
        console.log(`📡 Character Service responded with status: ${proxyRes.statusCode}`);
    },
    onError: (err, req, res) => {
        console.error('❌ Character Service proxy error:', err.message);
        res.status(503).json({
            error: 'Character Service unavailable',
            message: 'Please try again later',
            timestamp: new Date().toISOString()
        });
    }
}));

// TODO 2: SINGLE CHARACTER ENDPOINT
// ═══════════════════════════════════════════════════════════
/*
🎯 YOUR TASK: Create GET /api/characters/:id endpoint

This endpoint should:
1. Validate character ID parameter
2. Proxy to Character Service
3. Handle 404 errors gracefully
4. Add caching headers
*/

// GET /api/characters/:id - Get specific character
router.get('/:id', (req, res, next) => {
    const characterId = req.params.id;
    
    // Validate character ID
    if (!characterId || isNaN(characterId)) {
        return res.status(400).json({
            error: 'Invalid character ID',
            message: 'Character ID must be a valid number',
            timestamp: new Date().toISOString()
        });
    }
    
    next();
}, createProxyMiddleware({
    target: CHARACTER_SERVICE_URL,
    changeOrigin: true,
    pathRewrite: {
        '^/api/characters': '/api/characters'
    },
    onProxyReq: (proxyReq, req, res) => {
        console.log(`📡 Proxying GET /api/characters/${req.params.id} to Character Service`);
    },
    onProxyRes: (proxyRes, req, res) => {
        // Add caching headers for character data
        if (proxyRes.statusCode === 200) {
            res.setHeader('Cache-Control', 'public, max-age=300'); // 5 minutes
        }
    },
    onError: (err, req, res) => {
        console.error('❌ Character Service proxy error:', err.message);
        res.status(503).json({
            error: 'Character Service unavailable',
            message: 'Unable to fetch character details',
            timestamp: new Date().toISOString()
        });
    }
}));

// TODO 3: CHARACTER SEARCH ENDPOINT
// ═══════════════════════════════════════════════════════════
/*
🎯 YOUR TASK: Create GET /api/characters/search endpoint

This endpoint should:
1. Handle search query parameters
2. Validate search terms
3. Proxy to Character Service search
4. Add search analytics logging
*/

// GET /api/characters/search - Search characters
router.get('/search', (req, res, next) => {
    const { q, crew, bounty_min, bounty_max, limit = 20 } = req.query;
    
    // Validate search parameters
    if (!q && !crew && !bounty_min && !bounty_max) {
        return res.status(400).json({
            error: 'Missing search parameters',
            message: 'At least one search parameter is required (q, crew, bounty_min, bounty_max)',
            timestamp: new Date().toISOString()
        });
    }
    
    // Log search analytics
    console.log(`🔍 Character search: query="${q}", crew="${crew}", bounty_range="${bounty_min}-${bounty_max}"`);
    
    next();
}, createProxyMiddleware({
    target: CHARACTER_SERVICE_URL,
    changeOrigin: true,
    pathRewrite: {
        '^/api/characters/search': '/api/characters/search'
    },
    onProxyReq: (proxyReq, req, res) => {
        console.log(`📡 Proxying character search to Character Service`);
    }
}));

// TODO 4: CHARACTER STATS ENDPOINT
// ═══════════════════════════════════════════════════════════
/*
🎯 YOUR TASK: Create GET /api/characters/stats endpoint

This endpoint should:
1. Proxy to Character Service stats
2. Add response caching
3. Handle aggregation errors
4. Format response for frontend
*/

// GET /api/characters/stats - Get character statistics
router.get('/stats', createProxyMiddleware({
    target: CHARACTER_SERVICE_URL,
    changeOrigin: true,
    pathRewrite: {
        '^/api/characters/stats': '/api/characters/stats'
    },
    onProxyReq: (proxyReq, req, res) => {
        console.log(`📊 Proxying character stats request to Character Service`);
    },
    onProxyRes: (proxyRes, req, res) => {
        // Cache stats for 10 minutes
        if (proxyRes.statusCode === 200) {
            res.setHeader('Cache-Control', 'public, max-age=600');
        }
    }
}));

// TODO 5: CHARACTER FAVORITES ENDPOINT (AUTHENTICATED)
// ═══════════════════════════════════════════════════════════
/*
🎯 YOUR TASK: Create authenticated endpoints for user favorites

These endpoints should:
1. Require authentication
2. Handle user-specific data
3. Proxy to Character Service
4. Add user context to requests
*/

// GET /api/characters/favorites - Get user's favorite characters (requires auth)
router.get('/favorites', (req, res, next) => {
    // Check if user is authenticated
    if (!req.user) {
        return res.status(401).json({
            error: 'Authentication required',
            message: 'Please log in to view favorites',
            timestamp: new Date().toISOString()
        });
    }
    
    next();
}, createProxyMiddleware({
    target: CHARACTER_SERVICE_URL,
    changeOrigin: true,
    pathRewrite: {
        '^/api/characters/favorites': '/api/characters/favorites'
    },
    onProxyReq: (proxyReq, req, res) => {
        // Add user ID to request headers
        proxyReq.setHeader('X-User-ID', req.user.id);
        console.log(`❤️ Proxying favorites request for user ${req.user.id}`);
    }
}));

// POST /api/characters/:id/favorite - Add character to favorites
router.post('/:id/favorite', (req, res, next) => {
    if (!req.user) {
        return res.status(401).json({
            error: 'Authentication required',
            message: 'Please log in to add favorites',
            timestamp: new Date().toISOString()
        });
    }
    
    next();
}, createProxyMiddleware({
    target: CHARACTER_SERVICE_URL,
    changeOrigin: true,
    pathRewrite: {
        '^/api/characters': '/api/characters'
    },
    onProxyReq: (proxyReq, req, res) => {
        proxyReq.setHeader('X-User-ID', req.user.id);
        console.log(`❤️ Adding character ${req.params.id} to favorites for user ${req.user.id}`);
    }
}));

// TODO 6: ERROR HANDLING MIDDLEWARE
// ═══════════════════════════════════════════════════════════
/*
🎯 YOUR TASK: Add comprehensive error handling

This middleware should:
1. Handle all character route errors
2. Log errors appropriately
3. Return consistent error responses
4. Add error tracking
*/

// Error handling middleware for character routes
router.use((err, req, res, next) => {
    console.error('❌ Character routes error:', err);
    
    // Determine error type and response
    let statusCode = 500;
    let errorMessage = 'Internal server error';
    
    if (err.code === 'ECONNREFUSED') {
        statusCode = 503;
        errorMessage = 'Character Service unavailable';
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
🎯 WHAT'S NEXT? YOUR NEXT IMPLEMENTATION STEP AFTER CHARACTERS.JS
═══════════════════════════════════════════════════════════════════════════════

🏴‍☠️ CONGRATULATIONS! You've completed the Character Routes file!

📚 WHAT YOU JUST BUILT:
✅ Character listing endpoint with pagination
✅ Single character retrieval with validation
✅ Character search with multiple filters
✅ Character statistics endpoint with caching
✅ User favorites (authenticated endpoints)
✅ Comprehensive error handling
✅ Request/response logging
✅ Service proxy configuration

🎯 YOUR NEXT IMPLEMENTATION STEP (FOLLOW THIS EXACT ORDER):

═══════════════════════════════════════════════════════════════════════════════
📍 NEXT FILE: services/api-gateway/routes/trading.js
═══════════════════════════════════════════════════════════════════════════════

🔥 CREATE THIS FILE NEXT: services/api-gateway/routes/trading.js
⏱️ TIME: 45-60 minutes
🎯 PURPOSE: Create trading-specific routes for buy/sell operations

WHAT YOU'LL CREATE IN trading.js:
• POST /api/trades - Execute buy/sell trades
• GET /api/trades/:userId - Get user's trade history
• GET /api/portfolio/:userId - Get user's portfolio
• POST /api/trades/cancel - Cancel pending trades
• GET /api/market/prices - Get current market prices

AFTER COMPLETING trading.js, THAT FILE WILL TELL YOU:
→ Next file: services/api-gateway/middleware/auth.js

═══════════════════════════════════════════════════════════════════════════════
🧪 TEST THIS FILE FIRST:
═══════════════════════════════════════════════════════════════════════════════

□ Import this file in server.js: app.use('/api/characters', require('./routes/characters'));
□ Start API Gateway: node server.js
□ Test endpoints:
  - curl http://localhost:3000/api/characters
  - curl http://localhost:3000/api/characters/1
  - curl http://localhost:3000/api/characters/search?q=luffy

If these work, proceed to create trading.js!

🚀 Keep building your legendary One Piece trading platform! ⚔️
*/
