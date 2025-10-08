/*
🏴‍☠️ API GATEWAY - NODE.JS EXPRESS SERVER BLUEPRINT
Your mission: Create a central API gateway that routes requests to all microservices

WHAT YOU'RE BUILDING:
- Express.js server as API gateway
- Request routing to microservices
- Authentication middleware
- Rate limiting and security
- GraphQL endpoint integration
- Load balancing and health checks
- Request/response logging
- CORS and security headers

LEARNING OBJECTIVES:
- Node.js and Express.js fundamentals
- Middleware patterns and implementation
- HTTP proxy and request forwarding
- Authentication and authorization
- API security best practices
- GraphQL integration
- Microservices communication
*/

// TODO 1: IMPORT STATEMENTS
// Add these require statements:
// const express = require('express');
// const cors = require('cors');
// const helmet = require('helmet');
// const rateLimit = require('express-rate-limit');
// const { createProxyMiddleware } = require('http-proxy-middleware');
// const jwt = require('jsonwebtoken');
// const axios = require('axios');
// const { graphqlHTTP } = require('express-graphql');
// const { buildSchema } = require('graphql');
// const winston = require('winston');
// require('dotenv').config();

// WRITE YOUR REQUIRE STATEMENTS HERE:
const express = require('express');
const cors = require('cors');
const helmet = require('helmet');
const rateLimit = require('express-rate-limit');
const {createProxyMiddleware} = require('http-proxy-middleware');
const jwt = require('jsonwebtoken');
const axios = require('axios');
const {graphqlHTTP} = require('express-graphql');
const {buildSchema} = require('graphql');
const winston = require ('winston');
require('dotenv').config();
const {Pool} = require('pg');

const app = express();

app.use(helmet());
app.use(cors({
    origin: ['https://localhost:3000', 'https://localhost:3001'],
    credentials : true
}));

app.use(express.json({limit : '10mb' }));
app.use(express.urlencoded({extended : true}));

const limiter = rateLimit({
    windowMs : 15 * 60 * 1000,
    max: 100,
    message : {
        error : 'Too many requests sent'
    }
});

app.use('/api/', limiter);

app.use((req, res, next) => {
    console.log(`📥 ${new Date().toISOString()} - ${req.method} ${req.path}`);
    next();
});


const mysql = require('mysql2/promise');

// Database connection pool (connects to YOUR ACTUAL onepiece_market database)
const pool = mysql.createPool({
    host: process.env.DB_HOST || 'localhost',        // MySQL server location
    user: process.env.DB_USER || 'root',             // MySQL username
    password: process.env.DB_PASSWORD || 'your_mysql_password', // MySQL password
    database: process.env.DB_NAME || 'onepiece_market', // YOUR actual database name
    port: process.env.DB_PORT || 3306,               // MySQL default port
    waitForConnections: true,    // Wait for available connection instead of failing
    connectionLimit: 20,         // Maximum 20 concurrent connections (production-ready)
    queueLimit: 0,              // No limit on queued connection requests
    acquireTimeout: 60000,      // 60 seconds to get a connection before timeout
    timeout: 60000,             // 60 seconds for query execution timeout
    reconnect: true             // Automatically reconnect if connection is lost
});

console.log("Connected to Database");
pool.on('error', (err) => {
    console.error('Database error', err);
})
// TODO 2: EXPRESS APP SETUP
// Create Express application instance
// const app = express();
// const PORT = process.env.PORT || 3000;

// TODO 3: LOGGING CONFIGURATION
// Set up Winston logger for request/response logging
// const logger = winston.createLogger({
//   level: 'info',
//   format: winston.format.combine(
//     winston.format.timestamp(),
//     winston.format.json()
//   ),
//   transports: [
//     new winston.transports.File({ filename: 'logs/error.log', level: 'error' }),
//     new winston.transports.File({ filename: 'logs/combined.log' }),
//     new winston.transports.Console({
//       format: winston.format.simple()
//     })
//   ]
// });

// TODO 4: MIDDLEWARE SETUP
// Configure global middleware
// 
// // Security middleware
// app.use(helmet());
// 
// // CORS configuration
// app.use(cors({
//   origin: process.env.ALLOWED_ORIGINS?.split(',') || ['http://localhost:3000'],
//   credentials: true
// }));
// 
// // Body parsing middleware
// app.use(express.json({ limit: '10mb' }));
// app.use(express.urlencoded({ extended: true }));

// TODO 5: RATE LIMITING MIDDLEWARE
// Configure rate limiting to prevent abuse
// const limiter = rateLimit({
//   windowMs: 15 * 60 * 1000, // 15 minutes
//   max: 100, // limit each IP to 100 requests per windowMs
//   message: {
//     error: 'Too many requests from this IP, please try again later.'
//   },
//   standardHeaders: true,
//   legacyHeaders: false
// });
// 
// app.use('/api/', limiter);

// TODO 6: REQUEST LOGGING MIDDLEWARE
// Log all incoming requests
// app.use((req, res, next) => {
//   // Log request details
//   logger.info({
//     method: req.method,
//     url: req.url,
//     ip: req.ip,
//     userAgent: req.get('User-Agent'),
//     timestamp: new Date().toISOString()
//   });
//   
//   // Continue to next middleware
//   next();
// });

// TODO 7: AUTHENTICATION MIDDLEWARE
// JWT token validation middleware
// const authenticateToken = (req, res, next) => {
//   // Get token from Authorization header
//   const authHeader = req.headers['authorization'];
//   const token = authHeader && authHeader.split(' ')[1]; // Bearer TOKEN
//   
//   if (!token) {
//     return res.status(401).json({ error: 'Access token required' });
//   }
//   
//   // Verify JWT token
//   jwt.verify(token, process.env.JWT_SECRET, (err, user) => {
//     if (err) {
//       return res.status(403).json({ error: 'Invalid or expired token' });
//     }
//     
//     // Add user info to request object
//     req.user = user;
//     next();
//   });
// };

// TODO 8: SERVICE HEALTH CHECK MIDDLEWARE
// Check if microservices are healthy before routing
// const checkServiceHealth = async (serviceUrl) => {
//   try {
//     const response = await axios.get(`${serviceUrl}/health`, { timeout: 5000 });
//     return response.status === 200;
//   } catch (error) {
//     logger.error(`Service health check failed for ${serviceUrl}:`, error.message);
//     return false;
//   }
// };

// TODO 9: MICROSERVICE PROXY CONFIGURATIONS
// Configure proxy middleware for each microservice
// 
// // Character Service Proxy
// const characterServiceProxy = createProxyMiddleware({
//   target: process.env.CHARACTER_SERVICE_URL || 'http://localhost:5001',
//   changeOrigin: true,
//   pathRewrite: {
//     '^/api/characters': '/api/characters'
//   },
//   onError: (err, req, res) => {
//     logger.error('Character Service proxy error:', err);
//     res.status(503).json({ error: 'Character Service unavailable' });
//   }
// });
// 
// // Trading Service Proxy
// const tradingServiceProxy = createProxyMiddleware({
//   target: process.env.TRADING_SERVICE_URL || 'http://localhost:5002',
//   changeOrigin: true,
//   pathRewrite: {
//     '^/api/trading': '/api/trading'
//   },
//   onError: (err, req, res) => {
//     logger.error('Trading Service proxy error:', err);
//     res.status(503).json({ error: 'Trading Service unavailable' });
//   }
// });
// 
// // User Service Proxy
// const userServiceProxy = createProxyMiddleware({
//   target: process.env.USER_SERVICE_URL || 'http://localhost:5003',
//   changeOrigin: true,
//   pathRewrite: {
//     '^/api/users': '/api/users',
//     '^/api/auth': '/api/auth'
//   },
//   onError: (err, req, res) => {
//     logger.error('User Service proxy error:', err);
//     res.status(503).json({ error: 'User Service unavailable' });
//   }
// });

// TODO 10: ROUTE DEFINITIONS
// Define routes and apply appropriate middleware
// 
// // Public routes (no authentication required)
// app.use('/api/auth', userServiceProxy);
// app.use('/api/characters', characterServiceProxy);
// 
// // Protected routes (authentication required)
// app.use('/api/trading', authenticateToken, tradingServiceProxy);
// app.use('/api/users', authenticateToken, userServiceProxy);

// TODO 11: GRAPHQL SCHEMA DEFINITION
// Define GraphQL schema for unified API
// const schema = buildSchema(`
//   type Character {
//     id: ID!
//     name: String!
//     crew: String
//     bounty: Int
//     current_price: Float!
//     market_cap: Float!
//     sentiment_score: Float
//     weekly_change: Float
//   }
//   
//   type User {
//     id: ID!
//     username: String!
//     email: String!
//     balance: Float!
//   }
//   
//   type Portfolio {
//     user_id: ID!
//     holdings: [PortfolioHolding!]!
//     total_value: Float!
//   }
//   
//   type PortfolioHolding {
//     character: Character!
//     quantity: Int!
//     average_price: Float!
//     current_value: Float!
//   }
//   
//   type Query {
//     characters(page: Int, per_page: Int): [Character!]!
//     character(id: ID!): Character
//     user(id: ID!): User
//     portfolio(user_id: ID!): Portfolio
//   }
//   
//   type Mutation {
//     buyStock(user_id: ID!, character_id: ID!, quantity: Int!): Boolean
//     sellStock(user_id: ID!, character_id: ID!, quantity: Int!): Boolean
//   }
// `);

// TODO 12: GRAPHQL RESOLVERS
// Implement GraphQL resolvers that call microservices
// const root = {
//   // Query resolvers
//   characters: async ({ page = 1, per_page = 20 }) => {
//     // Call Character Service API
//     try {
//       const response = await axios.get(`${process.env.CHARACTER_SERVICE_URL}/api/characters?page=${page}&per_page=${per_page}`);
//       return response.data.characters;
//     } catch (error) {
//       throw new Error('Failed to fetch characters');
//     }
//   },
//   
//   character: async ({ id }) => {
//     // Call Character Service API for single character
//     try {
//       const response = await axios.get(`${process.env.CHARACTER_SERVICE_URL}/api/characters/${id}`);
//       return response.data;
//     } catch (error) {
//       throw new Error('Character not found');
//     }
//   },
//   
//   portfolio: async ({ user_id }) => {
//     // Call Trading Service API for portfolio
//     try {
//       const response = await axios.get(`${process.env.TRADING_SERVICE_URL}/api/trading/portfolio/${user_id}`);
//       return response.data;
//     } catch (error) {
//       throw new Error('Failed to fetch portfolio');
//     }
//   },
//   
//   // Mutation resolvers
//   buyStock: async ({ user_id, character_id, quantity }) => {
//     // Call Trading Service API to execute buy order
//     try {
//       const response = await axios.post(`${process.env.TRADING_SERVICE_URL}/api/trading/buy`, {
//         user_id,
//         character_id,
//         quantity
//       });
//       return response.data.success;
//     } catch (error) {
//       throw new Error('Failed to execute buy order');
//     }
//   }
// };

// TODO 13: GRAPHQL ENDPOINT
// Set up GraphQL endpoint
// app.use('/graphql', graphqlHTTP({
//   schema: schema,
//   rootValue: root,
//   graphiql: process.env.NODE_ENV === 'development', // Enable GraphiQL in development
// }));

// TODO 14: HEALTH CHECK ENDPOINT
// Gateway health check endpoint
// app.get('/health', async (req, res) => {
//   // Check health of all microservices
//   const services = {
//     'character-service': await checkServiceHealth(process.env.CHARACTER_SERVICE_URL),
//     'trading-service': await checkServiceHealth(process.env.TRADING_SERVICE_URL),
//     'user-service': await checkServiceHealth(process.env.USER_SERVICE_URL)
//   };
//   
//   const allHealthy = Object.values(services).every(healthy => healthy);
//   
//   res.status(allHealthy ? 200 : 503).json({
//     status: allHealthy ? 'healthy' : 'unhealthy',
//     services,
//     timestamp: new Date().toISOString()
//   });
// });

// TODO 15: ERROR HANDLING MIDDLEWARE
// Global error handler
// app.use((err, req, res, next) => {
//   logger.error('Unhandled error:', err);
//   res.status(500).json({
//     error: 'Internal server error',
//     message: process.env.NODE_ENV === 'development' ? err.message : 'Something went wrong'
//   });
// });

// TODO 16: 404 HANDLER
// Handle unknown routes
// app.use('*', (req, res) => {
//   res.status(404).json({
//     error: 'Route not found',
//     path: req.originalUrl
//   });
// });

// TODO 17: START SERVER
// Start the Express server
// app.listen(PORT, () => {
//   logger.info(`🏴‍☠️ One Piece API Gateway running on port ${PORT}`);
//   logger.info(`GraphQL endpoint: http://localhost:${PORT}/graphql`);
//   logger.info(`Health check: http://localhost:${PORT}/health`);
// });

/*
🎯 WHAT EACH PART DOES:

Express Setup: Creates web server with middleware
Authentication: JWT token validation
Rate Limiting: Prevents API abuse
Proxy Middleware: Routes requests to microservices
GraphQL: Unified API interface
Health Checks: Monitor service availability
Logging: Track requests and errors
Error Handling: Graceful error responses

🚀 NODE.JS CONCEPTS YOU'LL LEARN:

1. Express.js framework - Web server creation
2. Middleware patterns - Request processing pipeline
3. HTTP proxy - Request forwarding
4. Async/await - Asynchronous programming
5. Error handling - Try/catch and middleware
6. Environment variables - Configuration management
7. Logging - Application monitoring

📚 API GATEWAY PATTERNS:

1. Request routing - Direct traffic to services
2. Authentication gateway - Centralized auth
3. Rate limiting - Traffic control
4. Load balancing - Distribute requests
5. Circuit breaker - Handle service failures
6. Request/response transformation - Data formatting
7. Caching - Performance optimization

🔧 MICROSERVICES COMMUNICATION:

1. HTTP/REST - Service-to-service calls
2. Service discovery - Find available services
3. Health checks - Monitor service status
4. Timeout handling - Prevent hanging requests
5. Retry logic - Handle temporary failures
6. Circuit breaker - Fail fast when service down

NEXT FILE AFTER THIS: Create GraphQL Schema definitions! 🚀
*/

/*
═══════════════════════════════════════════════════════════════════════════════
🎯 WHAT'S NEXT? YOUR COMPLETE IMPLEMENTATION CHAIN AFTER API GATEWAY
═══════════════════════════════════════════════════════════════════════════════

🏴‍☠️ CONGRATULATIONS! You've completed the API Gateway server.js file!

📚 WHAT YOU JUST BUILT:
✅ Express.js API Gateway server
✅ Request routing to microservices
✅ Authentication middleware with JWT
✅ Rate limiting and security headers
✅ CORS configuration
✅ Health check endpoints
✅ Error handling and logging
✅ GraphQL integration setup

🎯 YOUR NEXT IMPLEMENTATION STEPS (FOLLOW THIS EXACT ORDER):

═══════════════════════════════════════════════════════════════════════════════
📍 STEP 1: CREATE API GATEWAY ROUTES (REQUIRED)
═══════════════════════════════════════════════════════════════════════════════

🔥 NEXT FILE: services/api-gateway/routes/characters.js
⏱️ TIME: 30-45 minutes
🎯 PURPOSE: Create character-specific routes for your API Gateway

WHAT YOU'LL CREATE:
• GET /api/characters - List all characters
• GET /api/characters/:id - Get specific character
• POST /api/characters - Create new character
• PUT /api/characters/:id - Update character
• DELETE /api/characters/:id - Delete character

AFTER COMPLETING characters.js, THAT FILE WILL TELL YOU:
→ Next file: services/api-gateway/routes/trading.js

═══════════════════════════════════════════════════════════════════════════════
📍 STEP 2: CREATE TRADING ROUTES (AFTER STEP 1)
═══════════════════════════════════════════════════════════════════════════════

🔥 NEXT FILE: services/api-gateway/routes/trading.js (after characters.js)
⏱️ TIME: 45-60 minutes
🎯 PURPOSE: Create trading-specific routes

WHAT YOU'LL CREATE:
• POST /api/trades - Execute trade
• GET /api/trades/:userId - Get user trades
• GET /api/portfolio/:userId - Get user portfolio
• POST /api/trades/cancel - Cancel trade

AFTER COMPLETING trading.js, THAT FILE WILL TELL YOU:
→ Next file: services/api-gateway/middleware/auth.js

═══════════════════════════════════════════════════════════════════════════════
📍 STEP 3: CREATE AUTHENTICATION MIDDLEWARE (AFTER STEP 2)
═══════════════════════════════════════════════════════════════════════════════

🔥 NEXT FILE: services/api-gateway/middleware/auth.js (after trading.js)
⏱️ TIME: 30-45 minutes
🎯 PURPOSE: Create JWT authentication middleware

WHAT YOU'LL CREATE:
• JWT token verification
• User authentication middleware
• Role-based authorization
• Token refresh logic

AFTER COMPLETING auth.js, THAT FILE WILL TELL YOU:
→ Next step: Test your API Gateway OR start Character Service

═══════════════════════════════════════════════════════════════════════════════
📍 STEP 4: CHOOSE YOUR NEXT PATH (AFTER STEP 3)
═══════════════════════════════════════════════════════════════════════════════

🎯 OPTION A: BUILD CHARACTER SERVICE (RECOMMENDED)
🔥 NEXT FILE: services/character-service/app.py
⏱️ TIME: 2-3 hours
🎯 PURPOSE: Create the Python service that your API Gateway will connect to

🎯 OPTION B: BUILD FRONTEND (ALTERNATIVE)
🔥 NEXT FILE: frontend/src/App.tsx
⏱️ TIME: 3-4 hours
🎯 PURPOSE: Create React frontend that consumes your API Gateway

🎯 OPTION C: ADD DATABASE OPTIMIZATION
🔥 NEXT LEARNING MODULE: Module 3 - Database Optimization
📁 NEXT FILE: learning-modules/03-database-optimization/01-postgresql-redis-coding-lab.py
⏱️ TIME: 2-3 hours
🎯 PURPOSE: Optimize database connections and add caching

═══════════════════════════════════════════════════════════════════════════════
🎯 RECOMMENDED IMPLEMENTATION ORDER:
═══════════════════════════════════════════════════════════════════════════════

1. ✅ services/api-gateway/server.js (COMPLETED)
2. 🔥 services/api-gateway/routes/characters.js (NEXT)
3. 📊 services/api-gateway/routes/trading.js
4. 🔐 services/api-gateway/middleware/auth.js
5. 🧪 Test API Gateway endpoints
6. 🐍 services/character-service/app.py (Character Service)
7. 🗄️ Database optimization (Module 3)

═══════════════════════════════════════════════════════════════════════════════
🧪 TESTS YOU SHOULD RUN FIRST:
═══════════════════════════════════════════════════════════════════════════════

□ node server.js (Start API Gateway)
□ curl http://localhost:3000/health (Health check)
□ curl http://localhost:3000/api/status (Status check)

If these work, proceed to create the routes files!

═══════════════════════════════════════════════════════════════════════════════
🏴‍☠️ READY FOR THE NEXT STEP?
═══════════════════════════════════════════════════════════════════════════════

🔥 CREATE THIS FILE NEXT: services/api-gateway/routes/characters.js

This file doesn't exist yet - you need to create it! The characters.js file will contain all the character-related API routes and will tell you what to do after completing it.

🚀 Keep building your legendary One Piece trading platform! ⚔️
*/
