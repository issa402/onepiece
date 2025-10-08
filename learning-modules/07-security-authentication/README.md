# 🏴‍☠️ MODULE 7: SECURITY & AUTHENTICATION MASTERY
## From Zero to Hero - Complete Application Security & Identity Management

### 🎯 **WHAT YOU'LL LEARN FROM ABSOLUTE SCRATCH:**

#### **🔥 PART 1: SECURITY FUNDAMENTALS (What & Why)**
- **What is Application Security?** - Protecting your app from attacks
- **Why Learn Security?** - Prevent data breaches that destroy companies
- **What are Common Vulnerabilities?** - SQL injection, XSS, CSRF attacks
- **What is Authentication?** - Verifying user identity
- **What is Authorization?** - Controlling user permissions

#### **⚡ PART 2: AUTHENTICATION SYSTEMS (Professional Security)**
- **What is JWT?** - JSON Web Tokens for stateless authentication
- **What is OAuth2?** - Industry-standard authorization framework
- **What is Multi-Factor Authentication?** - Additional security layers
- **What is Session Management?** - Secure user session handling
- **What is Password Security?** - Hashing, salting, and best practices

#### **🗄️ PART 3: ENTERPRISE SECURITY (Production Systems)**
- **API Security** - Rate limiting, API keys, secure endpoints
- **Data Encryption** - At-rest and in-transit encryption
- **Security Headers** - HTTPS, CORS, CSP implementation
- **Input Validation** - Preventing injection attacks
- **Audit Logging** - Security event tracking and compliance

#### **🚀 PART 4: ADVANCED SECURITY (Enterprise Ready)**
- **Zero-Trust Architecture** - Never trust, always verify
- **Penetration Testing** - Finding vulnerabilities before attackers
- **Compliance Standards** - GDPR, SOC2, PCI-DSS requirements
- **Incident Response** - Handling security breaches

### 💰 **SALARY PROGRESSION:**
```
📚 Basic Security (auth, validation)           →  $90K-$130K  (Junior Full-Stack)
⚡ Authentication Systems (JWT, OAuth2)        →  $130K-$180K (Mid-Level Security)
🗄️ Enterprise Security (encryption, audit)    →  $180K-$280K (Senior Security)
🚀 Security Architecture (zero-trust, SOC2)   →  $280K-$450K (Staff Security)
🌐 Security Leadership (compliance, teams)    →  $450K-$700K+ (Principal Security)
```

### 🏢 **COMPANIES THAT HIRE FOR THESE SKILLS:**

#### **🔥 BASIC SECURITY:**
- **Entry Level**: Startups, smaller tech companies, agencies
- **Why They Need It**: Basic protection, user authentication

#### **⚡ AUTHENTICATION SYSTEMS:**
- **Mid Level**: Stripe, PayPal, fintech companies, SaaS platforms
- **Why They Need It**: User management, secure transactions

#### **🗄️ ENTERPRISE SECURITY:**
- **Senior Level**: Banks, trading firms, healthcare, government contractors
- **Why They Need It**: Regulatory compliance, data protection

#### **🚀 SECURITY ARCHITECTURE:**
- **Staff Level**: FAANG companies, defense contractors, critical infrastructure
- **Why They Need It**: Nation-state threats, advanced persistent threats

### 🔥 **WHY EACH CONCEPT MATTERS FOR YOUR CAREER:**

#### **📚 INSECURE VS SECURE AUTHENTICATION:**
```javascript
// ❌ INSECURE AUTHENTICATION (what gets companies hacked):
// Your current approach (dangerous and vulnerable):

// Insecure login endpoint
app.post('/login', (req, res) => {
    const { username, password } = req.body;
    
    // SQL Injection vulnerability!
    const query = `SELECT * FROM users WHERE username = '${username}' AND password = '${password}'`;
    db.query(query, (err, results) => {
        if (results.length > 0) {
            // No password hashing!
            // No session management!
            // No rate limiting!
            res.json({ success: true, user: results[0] });
        } else {
            res.json({ success: false });
        }
    });
});

// Problems:
// - SQL injection vulnerability
// - Passwords stored in plain text
// - No rate limiting (brute force attacks)
// - No session management
// - No input validation
// - No HTTPS enforcement
// - No audit logging

// ✅ SECURE AUTHENTICATION (professional approach):
// Enterprise-grade security for your One Piece platform

const bcrypt = require('bcrypt');
const jwt = require('jsonwebtoken');
const rateLimit = require('express-rate-limit');
const helmet = require('helmet');
const validator = require('validator');

// Security middleware
app.use(helmet()); // Security headers
app.use(express.json({ limit: '10mb' })); // Prevent payload attacks

// Rate limiting for login attempts
const loginLimiter = rateLimit({
    windowMs: 15 * 60 * 1000, // 15 minutes
    max: 5, // limit each IP to 5 requests per windowMs
    message: {
        error: 'Too many login attempts, please try again later.',
        retryAfter: '15 minutes'
    },
    standardHeaders: true,
    legacyHeaders: false,
});

// Input validation middleware
const validateLoginInput = (req, res, next) => {
    const { email, password } = req.body;
    
    // Validate email format
    if (!email || !validator.isEmail(email)) {
        return res.status(400).json({
            success: false,
            error: 'Valid email is required'
        });
    }
    
    // Validate password strength
    if (!password || password.length < 8) {
        return res.status(400).json({
            success: false,
            error: 'Password must be at least 8 characters'
        });
    }
    
    // Sanitize inputs
    req.body.email = validator.normalizeEmail(email);
    req.body.password = validator.escape(password);
    
    next();
};

// Secure user registration
app.post('/api/auth/register', validateLoginInput, async (req, res) => {
    try {
        const { email, password, username } = req.body;
        
        // Check if user already exists
        const existingUser = await pool.query(
            'SELECT id FROM users WHERE email = $1 OR username = $2',
            [email, username]
        );
        
        if (existingUser.rows.length > 0) {
            return res.status(409).json({
                success: false,
                error: 'User already exists'
            });
        }
        
        // Hash password with salt
        const saltRounds = 12;
        const hashedPassword = await bcrypt.hash(password, saltRounds);
        
        // Create user with secure defaults
        const result = await pool.query(`
            INSERT INTO users (email, username, password_hash, balance, created_at, is_active, failed_login_attempts)
            VALUES ($1, $2, $3, $4, NOW(), true, 0)
            RETURNING id, email, username, balance, created_at
        `, [email, username, hashedPassword, 10000.00]);
        
        const user = result.rows[0];
        
        // Generate JWT token
        const token = jwt.sign(
            { 
                userId: user.id, 
                email: user.email,
                role: 'user'
            },
            process.env.JWT_SECRET,
            { 
                expiresIn: '24h',
                issuer: 'onepiece-trading',
                audience: 'onepiece-users'
            }
        );
        
        // Log successful registration
        await pool.query(`
            INSERT INTO audit_logs (user_id, action, ip_address, user_agent, timestamp)
            VALUES ($1, 'USER_REGISTERED', $2, $3, NOW())
        `, [user.id, req.ip, req.get('User-Agent')]);
        
        res.status(201).json({
            success: true,
            message: 'User registered successfully',
            token,
            user: {
                id: user.id,
                email: user.email,
                username: user.username,
                balance: user.balance
            }
        });
        
    } catch (error) {
        console.error('Registration error:', error);
        res.status(500).json({
            success: false,
            error: 'Internal server error'
        });
    }
});

// Secure user login
app.post('/api/auth/login', loginLimiter, validateLoginInput, async (req, res) => {
    try {
        const { email, password } = req.body;
        
        // Get user with security info
        const result = await pool.query(`
            SELECT id, email, username, password_hash, balance, is_active, 
                   failed_login_attempts, locked_until
            FROM users 
            WHERE email = $1
        `, [email]);
        
        if (result.rows.length === 0) {
            // Don't reveal if user exists
            return res.status(401).json({
                success: false,
                error: 'Invalid credentials'
            });
        }
        
        const user = result.rows[0];
        
        // Check if account is locked
        if (user.locked_until && new Date() < user.locked_until) {
            return res.status(423).json({
                success: false,
                error: 'Account temporarily locked due to failed login attempts'
            });
        }
        
        // Check if account is active
        if (!user.is_active) {
            return res.status(401).json({
                success: false,
                error: 'Account is deactivated'
            });
        }
        
        // Verify password
        const isValidPassword = await bcrypt.compare(password, user.password_hash);
        
        if (!isValidPassword) {
            // Increment failed login attempts
            const failedAttempts = user.failed_login_attempts + 1;
            const lockUntil = failedAttempts >= 5 ? 
                new Date(Date.now() + 30 * 60 * 1000) : // Lock for 30 minutes
                null;
            
            await pool.query(`
                UPDATE users 
                SET failed_login_attempts = $1, locked_until = $2
                WHERE id = $3
            `, [failedAttempts, lockUntil, user.id]);
            
            // Log failed login attempt
            await pool.query(`
                INSERT INTO audit_logs (user_id, action, ip_address, user_agent, timestamp)
                VALUES ($1, 'LOGIN_FAILED', $2, $3, NOW())
            `, [user.id, req.ip, req.get('User-Agent')]);
            
            return res.status(401).json({
                success: false,
                error: 'Invalid credentials'
            });
        }
        
        // Reset failed login attempts on successful login
        await pool.query(`
            UPDATE users 
            SET failed_login_attempts = 0, locked_until = NULL, last_login = NOW()
            WHERE id = $1
        `, [user.id]);
        
        // Generate JWT token
        const token = jwt.sign(
            { 
                userId: user.id, 
                email: user.email,
                role: 'user'
            },
            process.env.JWT_SECRET,
            { 
                expiresIn: '24h',
                issuer: 'onepiece-trading',
                audience: 'onepiece-users'
            }
        );
        
        // Log successful login
        await pool.query(`
            INSERT INTO audit_logs (user_id, action, ip_address, user_agent, timestamp)
            VALUES ($1, 'LOGIN_SUCCESS', $2, $3, NOW())
        `, [user.id, req.ip, req.get('User-Agent')]);
        
        res.json({
            success: true,
            message: 'Login successful',
            token,
            user: {
                id: user.id,
                email: user.email,
                username: user.username,
                balance: user.balance
            }
        });
        
    } catch (error) {
        console.error('Login error:', error);
        res.status(500).json({
            success: false,
            error: 'Internal server error'
        });
    }
});

// JWT Authentication middleware
const authenticateToken = (req, res, next) => {
    const authHeader = req.headers['authorization'];
    const token = authHeader && authHeader.split(' ')[1];
    
    if (!token) {
        return res.status(401).json({
            success: false,
            error: 'Access token required'
        });
    }
    
    jwt.verify(token, process.env.JWT_SECRET, {
        issuer: 'onepiece-trading',
        audience: 'onepiece-users'
    }, (err, decoded) => {
        if (err) {
            return res.status(403).json({
                success: false,
                error: 'Invalid or expired token'
            });
        }
        
        req.user = decoded;
        next();
    });
};

// Secure trading endpoint with authorization
app.post('/api/trade', authenticateToken, async (req, res) => {
    const client = await pool.connect();
    
    try {
        await client.query('BEGIN');
        
        const { characterId, quantity, action } = req.body;
        const userId = req.user.userId;
        
        // Input validation
        if (!characterId || !quantity || !action) {
            return res.status(400).json({
                success: false,
                error: 'Missing required fields'
            });
        }
        
        if (!['buy', 'sell'].includes(action)) {
            return res.status(400).json({
                success: false,
                error: 'Invalid action. Must be buy or sell'
            });
        }
        
        if (quantity <= 0 || quantity > 1000) {
            return res.status(400).json({
                success: false,
                error: 'Invalid quantity. Must be between 1 and 1000'
            });
        }
        
        // Get character price with row locking
        const charResult = await client.query(
            'SELECT current_price FROM characters WHERE id = $1 FOR UPDATE',
            [characterId]
        );
        
        if (charResult.rows.length === 0) {
            throw new Error('Character not found');
        }
        
        const price = charResult.rows[0].current_price;
        const totalCost = price * quantity;
        
        if (action === 'buy') {
            // Check user balance with row locking
            const balanceResult = await client.query(
                'SELECT balance FROM users WHERE id = $1 FOR UPDATE',
                [userId]
            );
            
            if (balanceResult.rows[0].balance < totalCost) {
                throw new Error('Insufficient funds');
            }
            
            // Update user balance
            await client.query(
                'UPDATE users SET balance = balance - $1 WHERE id = $2',
                [totalCost, userId]
            );
        }
        
        // Record transaction
        await client.query(`
            INSERT INTO transactions (user_id, character_id, action, quantity, price, total_cost)
            VALUES ($1, $2, $3, $4, $5, $6)
        `, [userId, characterId, action, quantity, price, totalCost]);
        
        // Log trading activity
        await client.query(`
            INSERT INTO audit_logs (user_id, action, details, ip_address, timestamp)
            VALUES ($1, 'TRADE_EXECUTED', $2, $3, NOW())
        `, [userId, JSON.stringify({ characterId, action, quantity, totalCost }), req.ip]);
        
        await client.query('COMMIT');
        
        res.json({
            success: true,
            message: `Successfully ${action === 'buy' ? 'bought' : 'sold'} ${quantity} shares`,
            transaction: {
                character_id: characterId,
                action,
                quantity,
                price,
                total_cost: totalCost
            }
        });
        
    } catch (error) {
        await client.query('ROLLBACK');
        console.error('Transaction error:', error);
        
        res.status(400).json({
            success: false,
            error: error.message
        });
    } finally {
        client.release();
    }
});

// Benefits of secure authentication:
// - Prevents SQL injection attacks
// - Secure password hashing with bcrypt
// - Rate limiting prevents brute force
// - JWT tokens for stateless auth
// - Account lockout after failed attempts
// - Complete audit logging
// - Input validation and sanitization
// - Security headers with Helmet
// - Database transactions for consistency
```
**Why This Matters**: Security breaches cost companies millions. Equifax lost $4 billion due to poor security. Companies pay premium salaries for engineers who can build secure systems.

**🏴‍☠️ READY TO SECURE YOUR WAY TO $300K+? ⚔️**
