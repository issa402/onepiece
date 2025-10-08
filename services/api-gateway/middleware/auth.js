/*
🏴‍☠️ API GATEWAY - AUTHENTICATION MIDDLEWARE
═══════════════════════════════════════════════════════════════════════════════

🎯 WHAT YOU'RE BUILDING:
This file contains JWT authentication and authorization middleware for your API Gateway.
It handles user authentication, token validation, and role-based access control.

📚 LEARNING OBJECTIVES:
- JWT token verification and validation
- Authentication middleware patterns
- Role-based authorization
- Security best practices
- Token refresh mechanisms
- Error handling for auth failures

🔗 CONNECTS TO:
- services/api-gateway/routes/trading.js (previous file you completed)
- services/api-gateway/routes/characters.js (uses this middleware)
- services/user-service/ (user authentication service)
- All protected API endpoints
*/

const jwt = require('jsonwebtoken');
const axios = require('axios');

// JWT Secret (in production, use environment variable)
const JWT_SECRET = process.env.JWT_SECRET || 'your-super-secret-jwt-key-change-this-in-production';
const USER_SERVICE_URL = process.env.USER_SERVICE_URL || 'http://localhost:5004';

// TODO 1: JWT TOKEN VERIFICATION MIDDLEWARE
// ═══════════════════════════════════════════════════════════
/*
🎯 YOUR TASK: Create JWT token verification middleware

This middleware should:
1. Extract JWT token from Authorization header
2. Verify token signature and expiration
3. Decode user information from token
4. Add user data to request object
5. Handle token errors gracefully
*/

const verifyToken = (req, res, next) => {
    try {
        // Extract token from Authorization header
        const authHeader = req.headers.authorization;
        
        if (!authHeader) {
            return res.status(401).json({
                error: 'No authorization header',
                message: 'Authorization header is required',
                timestamp: new Date().toISOString()
            });
        }
        
        // Check if header starts with 'Bearer '
        if (!authHeader.startsWith('Bearer ')) {
            return res.status(401).json({
                error: 'Invalid authorization format',
                message: 'Authorization header must start with "Bearer "',
                timestamp: new Date().toISOString()
            });
        }
        
        // Extract token
        const token = authHeader.substring(7); // Remove 'Bearer ' prefix
        
        if (!token) {
            return res.status(401).json({
                error: 'No token provided',
                message: 'JWT token is required',
                timestamp: new Date().toISOString()
            });
        }
        
        // Verify token
        const decoded = jwt.verify(token, JWT_SECRET);
        
        // Add user information to request
        req.user = {
            id: decoded.userId,
            email: decoded.email,
            username: decoded.username,
            role: decoded.role || 'user',
            tokenExp: decoded.exp
        };
        
        console.log(`🔐 User authenticated: ${req.user.email} (ID: ${req.user.id})`);
        
        next();
        
    } catch (error) {
        console.error('❌ JWT verification error:', error.message);
        
        // Handle specific JWT errors
        if (error.name === 'TokenExpiredError') {
            return res.status(401).json({
                error: 'Token expired',
                message: 'Your session has expired. Please log in again.',
                timestamp: new Date().toISOString()
            });
        }
        
        if (error.name === 'JsonWebTokenError') {
            return res.status(401).json({
                error: 'Invalid token',
                message: 'The provided token is invalid',
                timestamp: new Date().toISOString()
            });
        }
        
        return res.status(401).json({
            error: 'Authentication failed',
            message: 'Unable to verify token',
            timestamp: new Date().toISOString()
        });
    }
};

// TODO 2: OPTIONAL AUTHENTICATION MIDDLEWARE
// ═══════════════════════════════════════════════════════════
/*
🎯 YOUR TASK: Create optional authentication middleware

This middleware should:
1. Try to authenticate user if token is provided
2. Continue without authentication if no token
3. Add user data to request if authenticated
4. Used for endpoints that work with or without auth
*/

const optionalAuth = (req, res, next) => {
    const authHeader = req.headers.authorization;
    
    // If no auth header, continue without authentication
    if (!authHeader || !authHeader.startsWith('Bearer ')) {
        console.log('📡 Request without authentication');
        return next();
    }
    
    // If auth header exists, try to authenticate
    verifyToken(req, res, next);
};

// TODO 3: ROLE-BASED AUTHORIZATION MIDDLEWARE
// ═══════════════════════════════════════════════════════════
/*
🎯 YOUR TASK: Create role-based authorization middleware

This middleware should:
1. Check if user has required role
2. Support multiple roles
3. Handle admin access
4. Return appropriate error messages
*/

const requireRole = (roles) => {
    return (req, res, next) => {
        // Ensure user is authenticated first
        if (!req.user) {
            return res.status(401).json({
                error: 'Authentication required',
                message: 'Please log in to access this resource',
                timestamp: new Date().toISOString()
            });
        }
        
        // Convert single role to array
        const requiredRoles = Array.isArray(roles) ? roles : [roles];
        
        // Check if user has any of the required roles
        const userRole = req.user.role;
        
        // Admin always has access
        if (userRole === 'admin') {
            console.log(`🔐 Admin access granted for ${req.user.email}`);
            return next();
        }
        
        // Check if user has required role
        if (requiredRoles.includes(userRole)) {
            console.log(`🔐 Role-based access granted: ${userRole} for ${req.user.email}`);
            return next();
        }
        
        console.log(`❌ Access denied: User ${req.user.email} has role "${userRole}", required: ${requiredRoles.join(' or ')}`);
        
        return res.status(403).json({
            error: 'Insufficient permissions',
            message: `This resource requires one of the following roles: ${requiredRoles.join(', ')}`,
            userRole: userRole,
            requiredRoles: requiredRoles,
            timestamp: new Date().toISOString()
        });
    };
};

// TODO 4: USER OWNERSHIP VERIFICATION
// ═══════════════════════════════════════════════════════════
/*
🎯 YOUR TASK: Create user ownership verification middleware

This middleware should:
1. Check if user can access specific user data
2. Allow users to access their own data
3. Allow admins to access any data
4. Handle user ID parameter validation
*/

const requireOwnership = (userIdParam = 'userId') => {
    return (req, res, next) => {
        if (!req.user) {
            return res.status(401).json({
                error: 'Authentication required',
                message: 'Please log in to access this resource',
                timestamp: new Date().toISOString()
            });
        }
        
        const requestedUserId = req.params[userIdParam];
        
        if (!requestedUserId) {
            return res.status(400).json({
                error: 'Missing user ID',
                message: `User ID parameter "${userIdParam}" is required`,
                timestamp: new Date().toISOString()
            });
        }
        
        // Admin can access any user's data
        if (req.user.role === 'admin') {
            console.log(`🔐 Admin access to user ${requestedUserId} data by ${req.user.email}`);
            return next();
        }
        
        // Users can only access their own data
        if (req.user.id === parseInt(requestedUserId)) {
            console.log(`🔐 User accessing own data: ${req.user.email}`);
            return next();
        }
        
        console.log(`❌ Ownership denied: User ${req.user.email} (ID: ${req.user.id}) tried to access user ${requestedUserId} data`);
        
        return res.status(403).json({
            error: 'Access denied',
            message: 'You can only access your own data',
            timestamp: new Date().toISOString()
        });
    };
};

// TODO 5: TOKEN REFRESH MIDDLEWARE
// ═══════════════════════════════════════════════════════════
/*
🎯 YOUR TASK: Create token refresh functionality

This middleware should:
1. Check if token is close to expiration
2. Generate new token if needed
3. Add new token to response headers
4. Handle refresh errors
*/

const refreshTokenIfNeeded = async (req, res, next) => {
    if (!req.user) {
        return next();
    }
    
    try {
        const currentTime = Math.floor(Date.now() / 1000);
        const tokenExp = req.user.tokenExp;
        const timeUntilExpiry = tokenExp - currentTime;
        
        // If token expires in less than 5 minutes, refresh it
        if (timeUntilExpiry < 300) {
            console.log(`🔄 Token refresh needed for user ${req.user.email}`);
            
            // Generate new token
            const newToken = jwt.sign(
                {
                    userId: req.user.id,
                    email: req.user.email,
                    username: req.user.username,
                    role: req.user.role
                },
                JWT_SECRET,
                { expiresIn: '24h' }
            );
            
            // Add new token to response headers
            res.setHeader('X-New-Token', newToken);
            
            console.log(`✅ Token refreshed for user ${req.user.email}`);
        }
        
        next();
        
    } catch (error) {
        console.error('❌ Token refresh error:', error.message);
        // Don't fail the request, just continue without refresh
        next();
    }
};

// TODO 6: RATE LIMITING BY USER
// ═══════════════════════════════════════════════════════════
/*
🎯 YOUR TASK: Create user-specific rate limiting

This middleware should:
1. Track requests per user
2. Apply different limits based on user role
3. Reset counters periodically
4. Handle rate limit exceeded
*/

const userRateLimit = (() => {
    const userRequests = new Map();
    
    // Rate limits by role (requests per minute)
    const rateLimits = {
        admin: 1000,
        premium: 200,
        user: 60,
        guest: 20
    };
    
    // Clean up old entries every minute
    setInterval(() => {
        const oneMinuteAgo = Date.now() - 60000;
        for (const [userId, data] of userRequests.entries()) {
            if (data.resetTime < oneMinuteAgo) {
                userRequests.delete(userId);
            }
        }
    }, 60000);
    
    return (req, res, next) => {
        const userId = req.user ? req.user.id : req.ip;
        const userRole = req.user ? req.user.role : 'guest';
        const limit = rateLimits[userRole] || rateLimits.guest;
        
        const now = Date.now();
        const userData = userRequests.get(userId);
        
        if (!userData || now - userData.resetTime > 60000) {
            // First request or reset time passed
            userRequests.set(userId, {
                count: 1,
                resetTime: now
            });
            return next();
        }
        
        if (userData.count >= limit) {
            console.log(`⚠️ Rate limit exceeded for ${req.user ? req.user.email : req.ip} (${userRole})`);
            
            return res.status(429).json({
                error: 'Rate limit exceeded',
                message: `Too many requests. Limit: ${limit} requests per minute`,
                limit: limit,
                resetTime: new Date(userData.resetTime + 60000).toISOString(),
                timestamp: new Date().toISOString()
            });
        }
        
        userData.count++;
        next();
    };
})();

// Export all middleware functions
module.exports = {
    verifyToken,
    optionalAuth,
    requireRole,
    requireOwnership,
    refreshTokenIfNeeded,
    userRateLimit
};

/*
═══════════════════════════════════════════════════════════════════════════════
🎯 WHAT'S NEXT? YOUR NEXT IMPLEMENTATION STEP AFTER AUTH.JS
═══════════════════════════════════════════════════════════════════════════════

🏴‍☠️ CONGRATULATIONS! You've completed the Authentication Middleware!

📚 WHAT YOU JUST BUILT:
✅ JWT token verification middleware
✅ Optional authentication for public endpoints
✅ Role-based authorization system
✅ User ownership verification
✅ Automatic token refresh functionality
✅ User-specific rate limiting
✅ Comprehensive error handling
✅ Security best practices implementation

🎯 YOUR NEXT IMPLEMENTATION STEPS (CHOOSE YOUR PATH):

═══════════════════════════════════════════════════════════════════════════════
📍 OPTION A: TEST YOUR COMPLETE API GATEWAY (RECOMMENDED)
═══════════════════════════════════════════════════════════════════════════════

🔥 NEXT STEP: Test all your API Gateway components together
⏱️ TIME: 30-45 minutes
🎯 PURPOSE: Verify your API Gateway works end-to-end

WHAT TO TEST:
1. Update server.js to use your new middleware and routes
2. Start API Gateway: node server.js
3. Test all endpoints with and without authentication
4. Verify error handling and security features

TESTING COMMANDS:
□ curl http://localhost:3000/health (Health check)
□ curl http://localhost:3000/api/characters (Public endpoint)
□ curl -H "Authorization: Bearer <token>" http://localhost:3000/api/trades (Protected endpoint)

═══════════════════════════════════════════════════════════════════════════════
📍 OPTION B: BUILD CHARACTER SERVICE (BACKEND FOCUS)
═══════════════════════════════════════════════════════════════════════════════

🔥 NEXT FILE: services/character-service/app.py
⏱️ TIME: 2-3 hours
🎯 PURPOSE: Create the Python Character Service that your API Gateway connects to

WHAT YOU'LL BUILD:
• Flask application with character endpoints
• Database models and ORM setup
• Character CRUD operations
• Search and filtering functionality
• Integration with API Gateway

AFTER COMPLETING app.py, THAT FILE WILL TELL YOU:
→ Next file: services/character-service/models/character.py

═══════════════════════════════════════════════════════════════════════════════
📍 OPTION C: BUILD REACT FRONTEND (FRONTEND FOCUS)
═══════════════════════════════════════════════════════════════════════════════

🔥 NEXT FILE: frontend/src/App.tsx
⏱️ TIME: 3-4 hours
🎯 PURPOSE: Create React frontend that consumes your API Gateway

WHAT YOU'LL BUILD:
• React application setup
• Authentication components
• Character browsing interface
• Trading interface
• API integration with your Gateway

AFTER COMPLETING App.tsx, THAT FILE WILL TELL YOU:
→ Next file: frontend/src/components/CharacterCard.tsx

═══════════════════════════════════════════════════════════════════════════════
📍 OPTION D: LEARN DATABASE OPTIMIZATION
═══════════════════════════════════════════════════════════════════════════════

🔥 NEXT LEARNING MODULE: Module 3 - Database Optimization
📁 NEXT FILE: learning-modules/03-database-optimization/01-postgresql-redis-coding-lab.py
⏱️ TIME: 2-3 hours
🎯 PURPOSE: Optimize database performance and add caching

WHAT YOU'LL LEARN:
• Database indexing and query optimization
• Redis caching strategies
• Connection pooling
• Performance monitoring

═══════════════════════════════════════════════════════════════════════════════
🎯 RECOMMENDED PATH FOR BEGINNERS:
═══════════════════════════════════════════════════════════════════════════════

1. ✅ API Gateway Complete (server.js + routes + middleware) - COMPLETED!
2. 🔥 Test API Gateway (NEXT - verify everything works)
3. 🐍 Build Character Service (services/character-service/app.py)
4. 📱 Build React Frontend (frontend/src/App.tsx)
5. 🗄️ Database Optimization (Module 3)

═══════════════════════════════════════════════════════════════════════════════
🧪 INTEGRATION TEST FOR YOUR API GATEWAY:
═══════════════════════════════════════════════════════════════════════════════

Update your server.js to include all the files you created:

```javascript
// Add these imports to server.js
const { verifyToken, optionalAuth, requireRole } = require('./middleware/auth');
app.use('/api/characters', require('./routes/characters'));
app.use('/api/trades', require('./routes/trading'));
```

🚀 Your API Gateway is now complete and ready to handle enterprise-grade traffic! ⚔️
*/
