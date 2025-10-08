"""
🏴‍☠️ SECURITY & AUTHENTICATION MASTERY - HANDS-ON CODING LAB
═══════════════════════════════════════════════════════════

🎯 WHAT YOU'LL CODE TODAY:
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
✅ OAuth2 + JWT authentication for One Piece trading platform
✅ API security with rate limiting and input validation
✅ OWASP Top 10 security practices implementation
✅ Role-based access control (RBAC) for trading permissions
✅ Security headers and HTTPS enforcement
✅ API key management and rotation

💰 SALARY IMPACT: +?0K-?00K (Security expertise is PREMIUM)
🏢 COMPANIES: All fintech, banks, FAANG (security is non-negotiable)

📚 WHY SECURITY EXPERTISE = BIG MONEY:
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

🔥 SECURITY BREACHES COST MILLIONS:

1. EQUIFAX (2017):
   - 147 million users compromised
   - ? billion in costs
   - Stock dropped 35%
   - Could have been prevented with proper security

2. CAPITAL ONE (2019):
   - 100 million customers affected
   - ?50 million fine
   - Misconfigured AWS security

3. TWITTER (2020):
   - High-profile accounts hacked
   - Bitcoin scam via compromised admin tools
   - Internal security failure

🔥 WHY COMPANIES PAY PREMIUM FOR SECURITY ENGINEERS:

1. REGULATORY COMPLIANCE:
   - GDPR: €20M or 4% revenue fines
   - SOX: Criminal penalties for executives
   - PCI DSS: Required for payment processing

2. BUSINESS IMPACT:
   - Customer trust = revenue
   - Data breaches = lawsuits
   - Downtime = lost money

3. SKILL SCARCITY:
   - Few developers understand security deeply
   - High demand, low supply = high salaries
   - Security + Backend = ?00K-?00K+

📖 ESSENTIAL RESOURCES:
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
🔗 OWASP Top 10: https://owasp.org/www-project-top-ten/
🔗 OAuth2 RFC: https://tools.ietf.org/html/rfc6749
🔗 JWT Best Practices: https://tools.ietf.org/html/rfc8725
🔗 Django Security: https://docs.djangoproject.com/en/4.2/topics/security/
🔗 API Security: https://github.com/shieldfy/API-Security-Checklist
"""

# ═══════════════════════════════════════════════════════════
# 🧪 HANDS-ON LAB 1: JWT AUTHENTICATION FOR ONE PIECE TRADING
# ═══════════════════════════════════════════════════════════

"""
📚 JWT (JSON WEB TOKENS) FOR TRADING PLATFORM:

🔥 WHY JWT FOR ONE PIECE TRADING PLATFORM:

1. STATELESS AUTHENTICATION:
   - No server-side session storage needed
   - Perfect for microservices architecture
   - Scales horizontally without session sharing

2. SECURE TOKEN STRUCTURE:
   Header.Payload.Signature
   - Header: Algorithm and token type
   - Payload: User claims (id, permissions, expiry)
   - Signature: Cryptographic verification

3. TRADING-SPECIFIC CLAIMS:
   {
     "user_id": 123,
     "email": "luffy@strawhat.com",
     "trading_level": "legendary",
     "permissions": ["trade", "view_portfolio", "admin"],
     "balance": 50000.00,
     "exp": 1640995200,
     "iat": 1640908800
   }

🎯 YOUR CODING MISSION:
Implement secure JWT authentication for One Piece trading!
"""

# TODO 1: CREATE JWT AUTHENTICATION SERVICE
# ═══════════════════════════════════════════════════════════
"""
🎯 YOUR TASK: Create JWT service for One Piece trading platform

Create file: apps/authentication/jwt_service.py
"""

# FILE: apps/authentication/jwt_service.py
# YOUR CODE HERE - Import required modules:
import jwt
import datetime
from django.conf import settings
from django.contrib.auth import get_user_model
# Add more imports...

# YOUR CODE HERE - Create JWTService class:
class JWTService:
    """Enterprise JWT service for One Piece trading platform"""
    
    def __init__(self):
        # Add JWT configuration
        self.secret_key = # Add secret key
        self.algorithm = # Add algorithm
        self.access_token_lifetime = # Add lifetime
        self.refresh_token_lifetime = # Add refresh lifetime
    
    # YOUR CODE HERE - Add token generation:
    def generate_tokens(self, user):
        """Generate access and refresh tokens for One Piece trader"""
        # Add token generation logic with trading-specific claims
        pass
    
    # YOUR CODE HERE - Add token validation:
    def validate_token(self, token):
        """Validate JWT token and return user data"""
        # Add token validation logic
        pass
    
    # YOUR CODE HERE - Add token refresh:
    def refresh_access_token(self, refresh_token):
        """Refresh access token for continued trading"""
        # Add token refresh logic
        pass
    
    # YOUR CODE HERE - Add trading permissions check:
    def check_trading_permissions(self, token, required_permission):
        """Check if user has required trading permissions"""
        # Add permission checking logic
        pass

# TODO 2: CREATE OAUTH2 INTEGRATION
# ═══════════════════════════════════════════════════════════
"""
🎯 YOUR TASK: Implement OAuth2 for social login (Google, GitHub)

Create file: apps/authentication/oauth2_service.py
"""

# FILE: apps/authentication/oauth2_service.py
# YOUR CODE HERE - Import OAuth2 libraries:


# YOUR CODE HERE - Create OAuth2Service class:
class OAuth2Service:
    """OAuth2 integration for One Piece platform social login"""
    
    def __init__(self):
        # Add OAuth2 provider configurations
        self.providers = {
            'google': {
                'client_id': # Add Google client ID
                'client_secret': # Add Google client secret
                'redirect_uri': # Add redirect URI
                'scope': # Add required scopes
            },
            'github': {
                # Add GitHub OAuth2 config
            }
        }
    
    # YOUR CODE HERE - Add authorization URL generation:
    def get_authorization_url(self, provider, state):
        """Generate OAuth2 authorization URL"""
        # Add authorization URL logic
        pass
    
    # YOUR CODE HERE - Add token exchange:
    def exchange_code_for_token(self, provider, code, state):
        """Exchange authorization code for access token"""
        # Add token exchange logic
        pass
    
    # YOUR CODE HERE - Add user info retrieval:
    def get_user_info(self, provider, access_token):
        """Get user information from OAuth2 provider"""
        # Add user info retrieval logic
        pass

# TODO 3: CREATE AUTHENTICATION MIDDLEWARE
# ═══════════════════════════════════════════════════════════
"""
🎯 YOUR TASK: Create middleware for JWT authentication

Create file: apps/authentication/middleware.py
"""

# FILE: apps/authentication/middleware.py
# YOUR CODE HERE - Create authentication middleware:


class JWTAuthenticationMiddleware:
    """JWT authentication middleware for One Piece API"""
    
    def __init__(self, get_response):
        # Add middleware initialization
        pass
    
    def __call__(self, request):
        # YOUR CODE HERE - Add JWT token extraction and validation:
        
        
        # YOUR CODE HERE - Add user authentication:
        
        
        # YOUR CODE HERE - Add trading session validation:
        
        
        response = self.get_response(request)
        return response

# ═══════════════════════════════════════════════════════════
# 🧪 HANDS-ON LAB 2: API SECURITY & RATE LIMITING
# ═══════════════════════════════════════════════════════════

"""
📚 API SECURITY FOR TRADING PLATFORM:

🔥 CRITICAL SECURITY MEASURES FOR ONE PIECE TRADING:

1. RATE LIMITING:
   - Prevent API abuse and DDoS attacks
   - Different limits for different endpoints
   - Trading endpoints: 10 requests/minute
   - Portfolio endpoints: 100 requests/minute
   - Public endpoints: 1000 requests/hour

2. INPUT VALIDATION:
   - Prevent SQL injection attacks
   - Validate all trading parameters
   - Sanitize user inputs
   - Type checking and bounds validation

3. API KEY MANAGEMENT:
   - Separate keys for different access levels
   - Key rotation and expiration
   - Usage tracking and monitoring

🎯 YOUR CODING MISSION:
Secure your One Piece trading API like a fortress!
"""

# TODO 4: CREATE RATE LIMITING SERVICE
# ═══════════════════════════════════════════════════════════
"""
🎯 YOUR TASK: Implement Redis-based rate limiting

Create file: apps/security/rate_limiter.py
"""

# FILE: apps/security/rate_limiter.py
# YOUR CODE HERE - Import Redis and required modules:


# YOUR CODE HERE - Create RateLimiter class:
class RateLimiter:
    """Redis-based rate limiter for One Piece trading API"""
    
    def __init__(self, redis_client):
        # Add rate limiter initialization
        self.redis = redis_client
        
        # Define rate limits for different One Piece endpoints
        self.limits = {
            'trading': # Add trading limits
            'portfolio': # Add portfolio limits
            'characters': # Add character limits
            'public': # Add public limits
        }
    
    # YOUR CODE HERE - Add rate limit checking:
    def is_allowed(self, user_id, endpoint_type, ip_address=None):
        """Check if request is within rate limits"""
        # Add rate limiting logic using sliding window
        pass
    
    # YOUR CODE HERE - Add rate limit tracking:
    def track_request(self, user_id, endpoint_type, ip_address=None):
        """Track API request for rate limiting"""
        # Add request tracking logic
        pass
    
    # YOUR CODE HERE - Add rate limit reset:
    def reset_limits(self, user_id, endpoint_type):
        """Reset rate limits (admin function)"""
        # Add rate limit reset logic
        pass

# TODO 5: CREATE INPUT VALIDATION SERVICE
# ═══════════════════════════════════════════════════════════
"""
🎯 YOUR TASK: Create comprehensive input validation

Create file: apps/security/input_validator.py
"""

# FILE: apps/security/input_validator.py
# YOUR CODE HERE - Import validation libraries:


# YOUR CODE HERE - Create InputValidator class:
class InputValidator:
    """Comprehensive input validation for One Piece trading"""
    
    # YOUR CODE HERE - Add trading parameter validation:
    @staticmethod
    def validate_trade_request(trade_data):
        """Validate trading request parameters"""
        # Add validation for:
        # - Character ID exists and is tradeable
        # - Quantity is positive integer
        # - Price is positive decimal
        # - Action is 'buy' or 'sell'
        pass
    
    # YOUR CODE HERE - Add user input sanitization:
    @staticmethod
    def sanitize_user_input(user_input):
        """Sanitize user input to prevent XSS and injection"""
        # Add input sanitization logic
        pass
    
    # YOUR CODE HERE - Add SQL injection prevention:
    @staticmethod
    def validate_sql_parameters(params):
        """Validate parameters to prevent SQL injection"""
        # Add SQL injection prevention
        pass

# TODO 6: CREATE API KEY MANAGEMENT
# ═══════════════════════════════════════════════════════════
"""
🎯 YOUR TASK: Implement API key management system

Create file: apps/security/api_key_manager.py
"""

# FILE: apps/security/api_key_manager.py
# YOUR CODE HERE - Create APIKeyManager class:


class APIKeyManager:
    """API key management for One Piece trading platform"""
    
    def __init__(self):
        # Add API key configuration
        pass
    
    # YOUR CODE HERE - Add API key generation:
    def generate_api_key(self, user_id, permissions, expiry_days=30):
        """Generate new API key for One Piece trader"""
        # Add API key generation logic
        pass
    
    # YOUR CODE HERE - Add API key validation:
    def validate_api_key(self, api_key):
        """Validate API key and return permissions"""
        # Add API key validation logic
        pass
    
    # YOUR CODE HERE - Add API key rotation:
    def rotate_api_key(self, old_api_key):
        """Rotate API key for security"""
        # Add API key rotation logic
        pass

# ═══════════════════════════════════════════════════════════
# 🧪 HANDS-ON LAB 3: OWASP SECURITY IMPLEMENTATION
# ═══════════════════════════════════════════════════════════

"""
📚 OWASP TOP 10 FOR ONE PIECE TRADING PLATFORM:

🔥 OWASP TOP 10 SECURITY RISKS (2021):

1. BROKEN ACCESS CONTROL:
   - Users accessing other users' portfolios
   - Admin functions accessible to regular users
   - Missing authorization checks

2. CRYPTOGRAPHIC FAILURES:
   - Weak password hashing
   - Unencrypted sensitive data
   - Poor key management

3. INJECTION:
   - SQL injection in trading queries
   - NoSQL injection in MongoDB
   - Command injection in system calls

4. INSECURE DESIGN:
   - No rate limiting on trading endpoints
   - Weak authentication mechanisms
   - Missing security controls

5. SECURITY MISCONFIGURATION:
   - Default passwords
   - Unnecessary features enabled
   - Missing security headers

🎯 YOUR CODING MISSION:
Implement OWASP security controls for One Piece platform!
"""

# TODO 7: CREATE SECURITY HEADERS MIDDLEWARE
# ═══════════════════════════════════════════════════════════
"""
🎯 YOUR TASK: Implement security headers for One Piece API

Create file: apps/security/security_headers.py
"""

# FILE: apps/security/security_headers.py
# YOUR CODE HERE - Create SecurityHeadersMiddleware:


class SecurityHeadersMiddleware:
    """Security headers middleware for One Piece trading platform"""
    
    def __init__(self, get_response):
        # Add middleware initialization
        pass
    
    def __call__(self, request):
        response = self.get_response(request)
        
        # YOUR CODE HERE - Add security headers:
        # Content Security Policy
        response['Content-Security-Policy'] = # Add CSP
        
        # X-Frame-Options
        response['X-Frame-Options'] = # Add frame options
        
        # X-Content-Type-Options
        response['X-Content-Type-Options'] = # Add content type options
        
        # Strict-Transport-Security
        response['Strict-Transport-Security'] = # Add HSTS
        
        # X-XSS-Protection
        response['X-XSS-Protection'] = # Add XSS protection
        
        return response

# TODO 8: CREATE ACCESS CONTROL SERVICE
# ═══════════════════════════════════════════════════════════
"""
🎯 YOUR TASK: Implement role-based access control (RBAC)

Create file: apps/security/access_control.py
"""

# FILE: apps/security/access_control.py
# YOUR CODE HERE - Create AccessControlService:


class AccessControlService:
    """Role-based access control for One Piece trading"""
    
    def __init__(self):
        # Define One Piece trading roles and permissions
        self.roles = {
            'rookie_trader': # Add rookie permissions
            'experienced_trader': # Add experienced permissions
            'expert_trader': # Add expert permissions
            'admin': # Add admin permissions
        }
    
    # YOUR CODE HERE - Add permission checking:
    def has_permission(self, user, resource, action):
        """Check if user has permission for specific action"""
        # Add permission checking logic
        pass
    
    # YOUR CODE HERE - Add resource ownership validation:
    def owns_resource(self, user, resource_type, resource_id):
        """Check if user owns the resource (portfolio, trades, etc.)"""
        # Add resource ownership validation
        pass

# TODO 9: CREATE ENCRYPTION SERVICE
# ═══════════════════════════════════════════════════════════
"""
🎯 YOUR TASK: Implement encryption for sensitive data

Create file: apps/security/encryption_service.py
"""

# FILE: apps/security/encryption_service.py
# YOUR CODE HERE - Create EncryptionService:


class EncryptionService:
    """Encryption service for One Piece sensitive data"""
    
    def __init__(self):
        # Add encryption configuration
        pass
    
    # YOUR CODE HERE - Add data encryption:
    def encrypt_sensitive_data(self, data):
        """Encrypt sensitive trading data"""
        # Add encryption logic for:
        # - User personal information
        # - Trading history
        # - Financial data
        pass
    
    # YOUR CODE HERE - Add data decryption:
    def decrypt_sensitive_data(self, encrypted_data):
        """Decrypt sensitive trading data"""
        # Add decryption logic
        pass
    
    # YOUR CODE HERE - Add password hashing:
    def hash_password(self, password):
        """Hash user password securely"""
        # Add secure password hashing
        pass

# TODO 10: CREATE SECURITY MONITORING
# ═══════════════════════════════════════════════════════════
"""
🎯 YOUR TASK: Implement security monitoring and alerting

Create file: apps/security/security_monitor.py
"""

# FILE: apps/security/security_monitor.py
# YOUR CODE HERE - Create SecurityMonitor:


class SecurityMonitor:
    """Security monitoring for One Piece trading platform"""
    
    def __init__(self):
        # Add monitoring configuration
        pass
    
    # YOUR CODE HERE - Add suspicious activity detection:
    def detect_suspicious_activity(self, user_id, activity_data):
        """Detect suspicious trading activity"""
        # Add detection logic for:
        # - Unusual trading patterns
        # - Multiple failed login attempts
        # - API abuse
        # - Potential fraud
        pass
    
    # YOUR CODE HERE - Add security alerting:
    def send_security_alert(self, alert_type, details):
        """Send security alert to administrators"""
        # Add alerting logic
        pass

# ===============================================================================
# 🏴‍☠️ CONGRATULATIONS! YOU'VE MASTERED SECURITY & AUTHENTICATION! 🎉
# ===============================================================================

print('\n🏴‍☠️ CONGRATULATIONS! YOU\'VE MASTERED SECURITY & AUTHENTICATION! 🎉')
print('===============================================================================')

print('\n🎯 WHAT YOU\'VE ACCOMPLISHED:')
print('✅ Mastered OAuth2 and JWT authentication patterns')
print('✅ Implemented secure password hashing and encryption')
print('✅ Built role-based access control (RBAC) systems')
print('✅ Added comprehensive security headers and OWASP protection')
print('✅ Created security monitoring and threat detection')
print('✅ Applied enterprise security patterns used by banks and fintech')

print('\n💰 SALARY IMPACT: +$80K-$200K (Security expertise is highly valued)')
print('🏢 COMPANIES: All financial institutions, FAANG, cybersecurity firms')

print('\n===============================================================================')
print('🎯 NOW IMPLEMENT THIS IN YOUR ONE PIECE PROJECT!')
print('===============================================================================')

print('\n🚀 STEP 1: ADD JWT AUTHENTICATION TO YOUR API GATEWAY')
print('━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━')
print('📁 File to update: services/api-gateway/server.js')
print('')
print('🎯 WHAT TO DO:')
print('1. Add JWT middleware for authentication')
print('2. Implement secure login and registration endpoints')
print('3. Add role-based access control for trading operations')
print('4. Secure all API endpoints with proper authentication')
print('5. Add rate limiting and security headers')
print('')
print('📚 REFERENCE: Use the JWT patterns from this module')

print('\n🚀 STEP 2: SECURE YOUR API ENDPOINTS')
print('━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━')
print('📝 UPDATE: services/api-gateway/server.js')
print('')
print('const jwt = require("jsonwebtoken");')
print('const bcrypt = require("bcrypt");')
print('const rateLimit = require("express-rate-limit");')
print('')
print('// JWT Authentication Middleware')
print('const authenticateToken = (req, res, next) => {')
print('    const authHeader = req.headers["authorization"];')
print('    const token = authHeader && authHeader.split(" ")[1];')
print('    ')
print('    if (!token) {')
print('        return res.status(401).json({ error: "Access token required" });')
print('    }')
print('    ')
print('    jwt.verify(token, process.env.JWT_SECRET, (err, user) => {')
print('        if (err) {')
print('            return res.status(403).json({ error: "Invalid or expired token" });')
print('        }')
print('        req.user = user;')
print('        next();')
print('    });')
print('};')
print('')
print('// Rate limiting for authentication endpoints')
print('const authLimiter = rateLimit({')
print('    windowMs: 15 * 60 * 1000, // 15 minutes')
print('    max: 5, // 5 attempts per window')
print('    message: "Too many authentication attempts, try again later"')
print('});')
print('')
print('// Secure login endpoint')
print('app.post("/api/auth/login", authLimiter, async (req, res) => {')
print('    try {')
print('        const { email, password } = req.body;')
print('        ')
print('        // Validate user credentials')
print('        const user = await getUserByEmail(email);')
print('        if (!user || !await bcrypt.compare(password, user.password_hash)) {')
print('            return res.status(401).json({ error: "Invalid credentials" });')
print('        }')
print('        ')
print('        // Generate JWT token')
print('        const token = jwt.sign(')
print('            { userId: user.id, email: user.email, role: user.role },')
print('            process.env.JWT_SECRET,')
print('            { expiresIn: "24h" }')
print('        );')
print('        ')
print('        res.json({ token, user: { id: user.id, email: user.email, role: user.role } });')
print('    } catch (error) {')
print('        res.status(500).json({ error: "Authentication failed" });')
print('    }')
print('});')
print('')
print('// Protect trading endpoints')
print('app.post("/api/trades", authenticateToken, async (req, res) => {')
print('    // Only authenticated users can trade')
print('    const userId = req.user.userId;')
print('    // Add trading logic here')
print('});')
print('')
print('🔧 COPY FROM THIS MODULE:')
print('- JWT authentication patterns (lines 150-250)')
print('- Password hashing with bcrypt (lines 300-350)')
print('- Rate limiting configuration (lines 400-450)')

print('\n🚀 STEP 3: ADD SECURITY HEADERS TO ALL RESPONSES')
print('━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━')
print('📝 UPDATE: services/api-gateway/server.js')
print('')
print('const helmet = require("helmet");')
print('')
print('// Security headers middleware')
print('app.use(helmet({')
print('    contentSecurityPolicy: {')
print('        directives: {')
print('            defaultSrc: ["\'self\'"],')
print('            styleSrc: ["\'self\'", "\'unsafe-inline\'"],')
print('            scriptSrc: ["\'self\'"],')
print('            imgSrc: ["\'self\'", "data:", "https:"],')
print('            connectSrc: ["\'self\'", "ws://localhost:*", "wss://localhost:*"]')
print('        }')
print('    },')
print('    hsts: {')
print('        maxAge: 31536000,')
print('        includeSubDomains: true,')
print('        preload: true')
print('    }')
print('}));')
print('')
print('// Additional security headers')
print('app.use((req, res, next) => {')
print('    res.setHeader("X-Content-Type-Options", "nosniff");')
print('    res.setHeader("X-Frame-Options", "DENY");')
print('    res.setHeader("X-XSS-Protection", "1; mode=block");')
print('    res.setHeader("Referrer-Policy", "strict-origin-when-cross-origin");')
print('    next();')
print('});')
print('')
print('🔧 SECURITY HEADERS EXPLAINED:')
print('- Content-Security-Policy: Prevents XSS attacks')
print('- X-Frame-Options: Prevents clickjacking')
print('- X-Content-Type-Options: Prevents MIME type sniffing')
print('- Strict-Transport-Security: Enforces HTTPS')
print('- X-XSS-Protection: Browser XSS protection')

print('\n🚀 STEP 4: IMPLEMENT ROLE-BASED ACCESS CONTROL')
print('━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━')
print('📝 CREATE: services/api-gateway/middleware/rbac.js')
print('')
print('const checkRole = (requiredRole) => {')
print('    return (req, res, next) => {')
print('        const userRole = req.user.role;')
print('        ')
print('        const roleHierarchy = {')
print('            "rookie_trader": 1,')
print('            "experienced_trader": 2,')
print('            "expert_trader": 3,')
print('            "admin": 4')
print('        };')
print('        ')
print('        if (roleHierarchy[userRole] >= roleHierarchy[requiredRole]) {')
print('            next();')
print('        } else {')
print('            res.status(403).json({ error: "Insufficient permissions" });')
print('        }')
print('    };')
print('};')
print('')
print('// Usage in routes:')
print('app.get("/api/admin/users", authenticateToken, checkRole("admin"), (req, res) => {')
print('    // Only admins can access user management')
print('});')
print('')
print('app.post("/api/trades/large", authenticateToken, checkRole("expert_trader"), (req, res) => {')
print('    // Only expert traders can make large trades')
print('});')
print('')
print('🔧 ROLE DEFINITIONS:')
print('- rookie_trader: Basic trading, view characters')
print('- experienced_trader: Advanced trading, portfolio management')
print('- expert_trader: Large trades, advanced features')
print('- admin: User management, system administration')

print('\n🚀 STEP 5: ADD SECURITY TO YOUR REACT FRONTEND')
print('━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━')
print('📝 CREATE: frontend/src/contexts/AuthContext.tsx')
print('')
print('import React, { createContext, useContext, useState, useEffect } from "react";')
print('')
print('interface AuthContextType {')
print('    user: User | null;')
print('    token: string | null;')
print('    login: (email: string, password: string) => Promise<void>;')
print('    logout: () => void;')
print('    isAuthenticated: boolean;')
print('}')
print('')
print('const AuthContext = createContext<AuthContextType | null>(null);')
print('')
print('export const AuthProvider: React.FC<{ children: ReactNode }> = ({ children }) => {')
print('    const [user, setUser] = useState<User | null>(null);')
print('    const [token, setToken] = useState<string | null>(')
print('        localStorage.getItem("auth_token")')
print('    );')
print('    ')
print('    const login = async (email: string, password: string) => {')
print('        try {')
print('            const response = await fetch("/api/auth/login", {')
print('                method: "POST",')
print('                headers: { "Content-Type": "application/json" },')
print('                body: JSON.stringify({ email, password })')
print('            });')
print('            ')
print('            if (!response.ok) {')
print('                throw new Error("Login failed");')
print('            }')
print('            ')
print('            const data = await response.json();')
print('            setToken(data.token);')
print('            setUser(data.user);')
print('            localStorage.setItem("auth_token", data.token);')
print('        } catch (error) {')
print('            throw error;')
print('        }')
print('    };')
print('    ')
print('    const logout = () => {')
print('        setToken(null);')
print('        setUser(null);')
print('        localStorage.removeItem("auth_token");')
print('    };')
print('    ')
print('    return (')
print('        <AuthContext.Provider value={{')
print('            user,')
print('            token,')
print('            login,')
print('            logout,')
print('            isAuthenticated: !!token')
print('        }}>')
print('            {children}')
print('        </AuthContext.Provider>')
print('    );')
print('};')
print('')
print('export const useAuth = () => {')
print('    const context = useContext(AuthContext);')
print('    if (!context) throw new Error("useAuth must be used within AuthProvider");')
print('    return context;')
print('};')
print('')
print('🔧 SECURITY BEST PRACTICES:')
print('- Store JWT tokens securely (consider httpOnly cookies for production)')
print('- Implement token refresh mechanism')
print('- Add CSRF protection for state-changing operations')
print('- Validate all user inputs on both client and server')

print('\n🚀 STEP 6: TEST YOUR SECURITY IMPLEMENTATION')
print('━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━')
print('🧪 TESTING STEPS:')
print('')
print('1. Test authentication endpoints:')
print('   curl -X POST http://localhost:5000/api/auth/login \\')
print('        -H "Content-Type: application/json" \\')
print('        -d \'{"email": "test@example.com", "password": "password123"}\'')
print('')
print('2. Test protected endpoints:')
print('   curl -H "Authorization: Bearer YOUR_JWT_TOKEN" \\')
print('        http://localhost:5000/api/trades')
print('')
print('3. Test rate limiting:')
print('   # Make 6 rapid login attempts to trigger rate limiting')
print('   for i in {1..6}; do')
print('       curl -X POST http://localhost:5000/api/auth/login \\')
print('            -H "Content-Type: application/json" \\')
print('            -d \'{"email": "wrong@email.com", "password": "wrong"}\'')
print('   done')
print('')
print('4. Test security headers:')
print('   curl -I http://localhost:5000/api/health')
print('   # Should show security headers in response')
print('')
print('5. Test role-based access:')
print('   # Try accessing admin endpoints with regular user token')
print('   curl -H "Authorization: Bearer REGULAR_USER_TOKEN" \\')
print('        http://localhost:5000/api/admin/users')
print('')
print('✅ SUCCESS CRITERIA:')
print('- Authentication endpoints work correctly')
print('- JWT tokens are generated and validated properly')
print('- Rate limiting blocks excessive requests')
print('- Security headers are present in all responses')
print('- Role-based access control prevents unauthorized access')
print('- Invalid tokens are rejected with proper error messages')

print('\n===============================================================================')
print('🔗 HOW THIS CONNECTS TO OTHER LEARNING MODULES')
print('===============================================================================')

print('\n🧩 MODULE CONNECTIONS:')
print('')
print('📚 Module 16 (Node.js) → Your API Gateway implements JWT authentication middleware')
print('📚 Module 19 (React) → Frontend uses secure authentication context and JWT tokens')
print('📚 Module 3 (Database) → User credentials and sessions stored securely in database')
print('📚 Module 8 (Monitoring) → Security events logged and monitored for threats')
print('📚 Module 6 (System Design) → Security architecture across all microservices')
print('📚 Module 11 (APIs) → All API endpoints secured with proper authentication')

print('\n🎯 NEXT MODULES TO COMPLETE:')
print('1. Module 8: Add security monitoring and threat detection')
print('2. Module 6: Design secure microservices architecture')
print('3. Module 11: Implement secure API protocols (OAuth2, OpenID Connect)')

print('\n📚 RECOMMENDED RESOURCES FOR CONTINUED LEARNING:')
print('🔗 OWASP Top 10: https://owasp.org/www-project-top-ten/')
print('🔗 JWT Best Practices: https://auth0.com/blog/a-look-at-the-latest-draft-for-jwt-bcp/')
print('🔗 Node.js Security: https://nodejs.org/en/docs/guides/security/')
print('🔗 React Security: https://snyk.io/blog/10-react-security-best-practices/')

print('\n🏴‍☠️ YOU\'RE NOW READY TO BUILD SECURE, ENTERPRISE-GRADE APPLICATIONS! ⚔️')
print('📖 REFERENCE: Check MASTER-BLUEPRINT-ARCHITECTURE.md for the complete system overview!')
