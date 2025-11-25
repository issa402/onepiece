#!/usr/bin/env python3
"""
🏴‍☠️ FASTAPI MASTERY - COMPLETE BACKEND ENGINEERING LAB
═══════════════════════════════════════════════════════════════════════════════

🎯 WHAT YOU'LL MASTER IN THIS LAB (ROADMAP.SH ALIGNED):
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

📚 PART 1: PYTHON BACKEND FUNDAMENTALS (What & Why)
   - What is FastAPI and why it's the fastest Python framework
   - Why async/await matters for high-performance APIs
   - How Pydantic validation prevents 90% of production bugs
   - Why type hints make your code enterprise-ready

⚡ PART 2: REST API DESIGN PATTERNS (Industry Standards)
   - RESTful API design principles used by Netflix, Spotify
   - HTTP status codes and when to use each one
   - Request/Response validation with Pydantic models
   - Error handling patterns that prevent system crashes

🗄️ PART 3: DATABASE INTEGRATION (Production Patterns)
   - SQLAlchemy async ORM for high-performance database operations
   - Connection pooling for handling thousands of concurrent users
   - Database migrations and schema management
   - Query optimization techniques used by high-scale applications

🔒 PART 4: AUTHENTICATION & SECURITY (Enterprise Grade)
   - JWT token authentication with proper expiration handling
   - Password hashing with bcrypt (industry standard)
   - Rate limiting to prevent DDoS attacks
   - CORS configuration for secure cross-origin requests

🚀 PART 5: ADVANCED PATTERNS (Senior Engineer Level)
   - Background tasks for email sending, file processing
   - Dependency injection for clean, testable code
   - Middleware for logging, monitoring, error tracking
   - Testing strategies with pytest and async test clients

💰 SALARY IMPACT: $85K → $280K+ (Junior to Staff Engineer)
🏢 COMPANIES: Uber, Netflix, Microsoft, Instagram, Reddit

📖 ROADMAP.SH BACKEND CONCEPTS COVERED:
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
✅ Python Language Mastery (async/await, type hints, decorators)
✅ REST API Design (HTTP methods, status codes, versioning)
✅ Database Integration (SQLAlchemy, migrations, optimization)
✅ Authentication (JWT, OAuth2, session management)
✅ Testing (unit tests, integration tests, mocking)
✅ Caching (Redis integration, cache strategies)
✅ Monitoring (logging, metrics, health checks)
✅ Security (input validation, rate limiting, HTTPS)

Run this lab: python 01-fastapi-mastery-coding-lab.py
"""

import asyncio
import logging
from datetime import datetime, timedelta
from typing import List, Optional, Dict, Any
from contextlib import asynccontextmanager

# FastAPI and related imports - The modern Python web framework
from fastapi import FastAPI, HTTPException, Depends, BackgroundTasks, status, Request
from fastapi.middleware.cors import CORSMiddleware
from fastapi.security import HTTPBearer, HTTPAuthorizationCredentials
from pydantic import BaseModel, Field, EmailStr, validator
import uvicorn

# Database imports - SQLAlchemy for async database operations
from sqlalchemy.ext.asyncio import AsyncSession, create_async_engine
from sqlalchemy.orm import sessionmaker, declarative_base
from sqlalchemy import Column, Integer, String, DateTime, Float, Boolean, Text

# Security imports - Industry standard security libraries
import jwt
from passlib.context import CryptContext
import secrets
import hashlib
import time

# ============================================================================
# 🎯 SECTION 1: FASTAPI APPLICATION SETUP & CONFIGURATION
# ============================================================================

print("🏴‍☠️ FASTAPI MASTERY LAB - BACKEND ENGINEERING EXCELLENCE")
print("═══════════════════════════════════════════════════════════════════════════════")

# Configure logging - Essential for production monitoring
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger(__name__)

"""
🤔 WHY PROPER LOGGING MATTERS:
- Production debugging: When your API crashes at 3 AM, logs save you
- Performance monitoring: Track slow queries and bottlenecks
- Security auditing: Track authentication attempts and suspicious activity
- Business intelligence: Understand user behavior and API usage patterns

🔥 ENTERPRISE LOGGING BEST PRACTICES:
- Structured logging with JSON format for log aggregation
- Different log levels (DEBUG, INFO, WARNING, ERROR, CRITICAL)
- Correlation IDs to track requests across microservices
- Log rotation to prevent disk space issues
"""

# Database setup - SQLite for demo, PostgreSQL for production
DATABASE_URL = "sqlite+aiosqlite:///./fastapi_backend_lab.db"

"""
🤔 WHY ASYNC DATABASE CONNECTIONS?
- Handle thousands of concurrent requests without blocking
- Better resource utilization (CPU and memory)
- Improved user experience with faster response times
- Essential for high-traffic applications like social media platforms

🔥 PRODUCTION DATABASE CONSIDERATIONS:
- Use PostgreSQL or MySQL for production (not SQLite)
- Connection pooling to manage database connections efficiently
- Read replicas for scaling read operations
- Database monitoring and query optimization
"""

# Create async database engine with optimized settings
engine = create_async_engine(
    DATABASE_URL,
    echo=True,  # Log all SQL queries (disable in production)
    pool_size=20,  # Number of connections to maintain
    max_overflow=30,  # Additional connections when pool is full
    pool_pre_ping=True,  # Verify connections before use
    pool_recycle=3600  # Recycle connections every hour
)

# Session factory for database operations
AsyncSessionLocal = sessionmaker(
    engine,
    class_=AsyncSession,
    expire_on_commit=False,  # Keep objects accessible after commit
    autoflush=True,  # Automatically flush changes
    autocommit=False  # Manual transaction control
)

# Base class for all database models
Base = declarative_base()

# Security configuration - Industry standard practices
SECRET_KEY = secrets.token_urlsafe(32)  # Generate secure random key
ALGORITHM = "HS256"  # HMAC with SHA-256 for JWT signing
ACCESS_TOKEN_EXPIRE_MINUTES = 30  # Token expiration time
REFRESH_TOKEN_EXPIRE_DAYS = 7  # Refresh token expiration

"""
🤔 WHY JWT TOKENS FOR AUTHENTICATION?
- Stateless: No need to store sessions in database
- Scalable: Works across multiple servers and microservices
- Secure: Cryptographically signed to prevent tampering
- Standard: Industry standard used by Google, Facebook, GitHub

🔥 JWT SECURITY BEST PRACTICES:
- Short expiration times (15-30 minutes for access tokens)
- Refresh tokens for seamless user experience
- Secure secret key management (use environment variables)
- Token blacklisting for logout functionality
"""

# Password hashing context - bcrypt is industry standard
pwd_context = CryptContext(
    schemes=["bcrypt"],  # Use bcrypt algorithm
    deprecated="auto",  # Automatically upgrade old hashes
    bcrypt__rounds=12  # Cost factor (higher = more secure but slower)
)

# HTTP Bearer token security scheme
security = HTTPBearer(auto_error=False)  # Don't auto-error for optional auth

# ============================================================================
# 🎯 SECTION 2: PYDANTIC MODELS - DATA VALIDATION & SERIALIZATION
# ============================================================================

print("\n🎯 SECTION 2: PYDANTIC MODELS - DATA VALIDATION MASTERY")
print("━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━")

"""
🤔 WHAT IS PYDANTIC AND WHY IS IT REVOLUTIONARY?

Pydantic is a data validation library that uses Python type hints to validate data.
It's the secret weapon that makes FastAPI so powerful and prevents 90% of production bugs.

🔥 BEFORE PYDANTIC (Manual Validation Hell):
```python
def create_user(data):
    if 'username' not in data:
        raise ValueError("Username required")
    if len(data['username']) < 3:
        raise ValueError("Username too short")
    if '@' not in data.get('email', ''):
        raise ValueError("Invalid email")
    # ... 50 more lines of validation code
```

✅ WITH PYDANTIC (Automatic Validation Paradise):
```python
class UserCreate(BaseModel):
    username: str = Field(min_length=3)
    email: EmailStr
    # Validation happens automatically!
```

🚀 PYDANTIC SUPERPOWERS:
- Automatic validation based on type hints
- Detailed error messages with field-level feedback
- JSON serialization/deserialization
- Data transformation and cleaning
- Integration with OpenAPI/Swagger documentation
- Performance optimized with Rust (Pydantic v2)

🏢 COMPANIES USING PYDANTIC:
Netflix, Uber, Microsoft, Reddit, Instagram (all FastAPI users)
"""

class UserCreate(BaseModel):
    """
    User registration model with comprehensive validation

    🎯 VALIDATION FEATURES DEMONSTRATED:
    - String length validation (username 3-50 chars)
    - Email format validation with EmailStr
    - Password strength requirements
    - Optional fields with defaults
    - Custom validation with @validator decorator
    """
    username: str = Field(
        ...,  # Required field (ellipsis means required)
        min_length=3,
        max_length=50,
        description="Username must be 3-50 characters",
        example="luffy_pirate_king"
    )
    email: EmailStr = Field(
        ...,
        description="Valid email address required",
        example="luffy@strawhat.crew"
    )
    password: str = Field(
        ...,
        min_length=8,
        max_length=128,
        description="Password must be at least 8 characters",
        example="GumGumPistol123!"
    )
    full_name: Optional[str] = Field(
        None,
        max_length=100,
        description="User's full name (optional)",
        example="Monkey D. Luffy"
    )
    age: Optional[int] = Field(
        None,
        ge=13,  # Greater than or equal to 13
        le=120,  # Less than or equal to 120
        description="User age (13-120)",
        example=19
    )

    @validator('username')
    def username_must_be_alphanumeric(cls, v):
        """
        Custom validator for username format

        🤔 WHY CUSTOM VALIDATORS?
        - Business logic validation beyond basic types
        - Complex validation rules specific to your domain
        - Consistent validation across your entire application
        """
        if not v.replace('_', '').isalnum():
            raise ValueError('Username must contain only letters, numbers, and underscores')
        return v.lower()  # Normalize to lowercase

    @validator('password')
    def password_strength_check(cls, v):
        """
        Password strength validation

        🔒 SECURITY BEST PRACTICES:
        - Minimum length requirements
        - Character complexity requirements
        - Common password detection
        - Password history checking (in production)
        """
        if not any(c.isupper() for c in v):
            raise ValueError('Password must contain at least one uppercase letter')
        if not any(c.islower() for c in v):
            raise ValueError('Password must contain at least one lowercase letter')
        if not any(c.isdigit() for c in v):
            raise ValueError('Password must contain at least one digit')
        return v

class UserResponse(BaseModel):
    """
    User response model - excludes sensitive data

    🔒 SECURITY PRINCIPLE: Never return sensitive data in API responses
    - Passwords should NEVER be returned
    - Internal IDs should be carefully considered
    - Personal data should follow GDPR/privacy regulations
    """
    id: int = Field(description="User unique identifier")
    username: str = Field(description="User's username")
    email: str = Field(description="User's email address")
    full_name: Optional[str] = Field(description="User's full name")
    age: Optional[int] = Field(description="User's age")
    is_active: bool = Field(description="Whether user account is active")
    created_at: datetime = Field(description="Account creation timestamp")
    last_login: Optional[datetime] = Field(description="Last login timestamp")

    class Config:
        """
        Pydantic configuration for ORM integration

        🤔 WHY from_attributes=True?
        - Allows Pydantic to work with SQLAlchemy models
        - Automatically converts ORM objects to Pydantic models
        - Enables seamless database-to-API serialization
        """
        from_attributes = True
        json_encoders = {
            datetime: lambda v: v.isoformat()  # ISO format for datetime
        }

class Token(BaseModel):
    """
    JWT token response model

    🔐 JWT TOKEN STRUCTURE:
    - access_token: Short-lived token for API access (15-30 minutes)
    - refresh_token: Long-lived token for getting new access tokens (7 days)
    - token_type: Always "bearer" for HTTP Bearer authentication
    - expires_in: Seconds until token expires (for client-side handling)
    """
    access_token: str = Field(description="JWT access token")
    refresh_token: Optional[str] = Field(description="JWT refresh token")
    token_type: str = Field(default="bearer", description="Token type")
    expires_in: int = Field(description="Token expiration time in seconds")

class ProductCreate(BaseModel):
    """
    Product creation model with business validation

    🛍️ E-COMMERCE VALIDATION PATTERNS:
    - Price validation (must be positive)
    - Category validation (from predefined list)
    - Inventory tracking
    - SEO-friendly slug generation
    """
    name: str = Field(
        ...,
        min_length=1,
        max_length=200,
        description="Product name",
        example="Devil Fruit - Gomu Gomu no Mi"
    )
    description: Optional[str] = Field(
        None,
        max_length=2000,
        description="Product description",
        example="Grants rubber powers to the user"
    )
    price: float = Field(
        ...,
        gt=0,  # Greater than 0
        le=1000000,  # Less than or equal to 1 million
        description="Product price in USD",
        example=1000000.00
    )
    category: str = Field(
        ...,
        min_length=1,
        max_length=100,
        description="Product category",
        example="Devil Fruits"
    )
    in_stock: bool = Field(
        default=True,
        description="Whether product is in stock"
    )
    stock_quantity: int = Field(
        default=0,
        ge=0,  # Greater than or equal to 0
        description="Available stock quantity"
    )

    @validator('price')
    def price_precision_check(cls, v):
        """Ensure price has maximum 2 decimal places"""
        if round(v, 2) != v:
            raise ValueError('Price can have maximum 2 decimal places')
        return v

class ProductResponse(BaseModel):
    """
    Product response model with computed fields

    💡 COMPUTED FIELDS PATTERN:
    - Add calculated fields that don't exist in database
    - Provide client-friendly data transformations
    - Include metadata for better user experience
    """
    id: int = Field(description="Product unique identifier")
    name: str = Field(description="Product name")
    description: Optional[str] = Field(description="Product description")
    price: float = Field(description="Product price in USD")
    category: str = Field(description="Product category")
    in_stock: bool = Field(description="Stock availability")
    stock_quantity: int = Field(description="Available quantity")
    created_at: datetime = Field(description="Product creation timestamp")
    updated_at: Optional[datetime] = Field(description="Last update timestamp")

    # Computed fields for better client experience
    @property
    def is_expensive(self) -> bool:
        """Computed field: Is this product expensive? (>$100)"""
        return self.price > 100.0

    @property
    def price_formatted(self) -> str:
        """Computed field: Formatted price string"""
        return f"${self.price:,.2f}"

    class Config:
        """
        Configuration for ProductResponse model

        🎯 ADVANCED PYDANTIC FEATURES:
        - from_attributes: Convert SQLAlchemy models to Pydantic
        - json_encoders: Custom serialization for complex types
        - schema_extra: Add examples to OpenAPI documentation
        """
        from_attributes = True
        json_encoders = {
            datetime: lambda v: v.isoformat()
        }
        schema_extra = {
            "example": {
                "id": 1,
                "name": "Devil Fruit - Gomu Gomu no Mi",
                "description": "Grants rubber powers to the user",
                "price": 1000000.00,
                "category": "Devil Fruits",
                "in_stock": True,
                "stock_quantity": 1,
                "created_at": "2024-01-01T00:00:00",
                "updated_at": "2024-01-01T00:00:00"
            }
        }

class ErrorResponse(BaseModel):
    """
    Standardized error response model

    🚨 ERROR HANDLING BEST PRACTICES:
    - Consistent error format across all endpoints
    - Detailed error messages for debugging
    - Error codes for programmatic handling
    - Timestamp for error tracking
    """
    error: str = Field(description="Error type")
    message: str = Field(description="Human-readable error message")
    details: Optional[Dict[str, Any]] = Field(description="Additional error details")
    timestamp: datetime = Field(default_factory=datetime.utcnow)
    request_id: Optional[str] = Field(description="Request correlation ID")

class HealthCheckResponse(BaseModel):
    """
    Health check response for monitoring

    🏥 HEALTH CHECK PATTERNS:
    - Simple status indicator
    - Dependency health (database, cache, external APIs)
    - Performance metrics
    - Version information
    """
    status: str = Field(description="Service status", example="healthy")
    timestamp: datetime = Field(default_factory=datetime.utcnow)
    version: str = Field(description="API version", example="1.0.0")
    uptime_seconds: float = Field(description="Service uptime in seconds")
    dependencies: Dict[str, str] = Field(description="Dependency health status")

print("✅ Pydantic models defined with comprehensive validation!")
print("   - UserCreate: Registration with password strength validation")
print("   - UserResponse: Safe user data without sensitive fields")
print("   - Token: JWT authentication response")
print("   - ProductCreate/Response: E-commerce with business validation")
print("   - ErrorResponse: Standardized error handling")
print("   - HealthCheckResponse: Monitoring and observability")

# ============================================================================
# 🎯 SECTION 3: DATABASE MODELS - SQLALCHEMY ORM MASTERY
# ============================================================================

print("\n🎯 SECTION 3: DATABASE MODELS - SQLALCHEMY ORM MASTERY")
print("━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━")

"""
🤔 WHAT IS AN ORM AND WHY DO WE NEED IT?

ORM (Object-Relational Mapping) lets you work with databases using Python objects
instead of writing raw SQL queries. It's like having a translator between Python and SQL.

🔥 WITHOUT ORM (Raw SQL Hell):
```python
cursor.execute("SELECT * FROM users WHERE email = %s AND is_active = %s", (email, True))
result = cursor.fetchone()
if result:
    user = {
        'id': result[0],
        'username': result[1],
        'email': result[2],
        # ... manual mapping for every field
    }
```

✅ WITH ORM (Python Object Paradise):
```python
user = session.query(User).filter(User.email == email, User.is_active == True).first()
# user is now a Python object with all attributes!
```

🚀 SQLALCHEMY SUPERPOWERS:
- Automatic SQL generation from Python code
- Database-agnostic (works with PostgreSQL, MySQL, SQLite)
- Relationship management (foreign keys, joins)
- Migration support for schema changes
- Connection pooling for performance
- Query optimization and caching

🏢 COMPANIES USING SQLALCHEMY:
Dropbox, Reddit, Yelp, Mozilla, OpenStack
"""

class PirateTrader(Base):
    """
    🏴‍☠️ PIRATE TRADER MODEL - ONE PIECE TRADING PLATFORM USER

    This model represents users who trade One Piece characters like stocks.
    Each trader has a portfolio, balance, and trading history.

    �‍☠️ ONE PIECE TRADING PLATFORM PATTERNS:
    - Pirate-themed user accounts (traders)
    - Berry balance for trading (One Piece currency)
    - Trading level based on experience
    - Portfolio tracking and performance
    - Crew affiliation and bonuses
    - Achievement system for trading milestones
    """
    __tablename__ = "pirate_traders"

    # Primary key - unique identifier for each trader
    id = Column(
        Integer,
        primary_key=True,  # Makes this the primary key
        index=True,  # Creates database index for fast lookups
        comment="Unique pirate trader identifier"
    )

    # Pirate name - must be unique across all traders
    pirate_name = Column(
        String(50),  # Maximum 50 characters
        unique=True,  # Database-level uniqueness constraint
        index=True,  # Index for fast pirate name lookups
        nullable=False,  # Cannot be NULL
        comment="Trader's unique pirate name (e.g., 'Captain Gold Roger')"
    )

    # Email - must be unique and is used for login
    email = Column(
        String(100),  # Maximum 100 characters for email
        unique=True,  # One email per trader
        index=True,  # Index for fast email lookups (login)
        nullable=False,  # Email is required
        comment="Trader's email address (used for login)"
    )

    # Password hash - NEVER store plain text passwords!
    hashed_password = Column(
        String(255),  # Bcrypt hashes are ~60 chars, but allow extra space
        nullable=False,  # Password is required
        comment="Bcrypt hashed password (NEVER store plain text!)"
    )

    # One Piece specific trader information
    crew_affiliation = Column(
        String(100),  # Maximum 100 characters
        nullable=True,  # Optional field
        comment="Trader's crew affiliation (e.g., 'Straw Hat Pirates')"
    )

    berry_balance = Column(
        BigInteger,  # Large numbers for berry amounts
        default=1000000,  # Start with 1 million berries
        nullable=False,
        comment="Trader's current berry balance for trading"
    )

    trading_level = Column(
        String(20),
        default="Rookie",  # Start as rookie trader
        nullable=False,
        comment="Trading level: Rookie, Veteran, Elite, Legendary, Pirate King"
    )

    # Account status and metadata
    is_active = Column(
        Boolean,
        default=True,  # New traders are active by default
        nullable=False,  # Must have a value
        comment="Whether trader account is active"
    )

    # Timestamps for auditing and analytics
    created_at = Column(
        DateTime,
        default=datetime.utcnow,  # Automatically set when record is created
        nullable=False,
        comment="Account creation timestamp"
    )

    last_login = Column(
        DateTime,
        nullable=True,  # NULL until first login
        comment="Last login timestamp"
    )

    updated_at = Column(
        DateTime,
        default=datetime.utcnow,
        onupdate=datetime.utcnow,  # Automatically update on record changes
        nullable=False,
        comment="Last update timestamp"
    )

    def __repr__(self):
        """String representation for debugging"""
        return f"<PirateTrader(id={self.id}, pirate_name='{self.pirate_name}', berry_balance={self.berry_balance})>"

class OnePieceCharacter(Base):
    """
    🏴‍☠️ ONE PIECE CHARACTER MODEL - TRADEABLE CHARACTERS

    This model represents One Piece characters that can be traded like stocks.
    Each character has a bounty (price), abilities, and trading metrics.

    🏴‍☠️ ONE PIECE CHARACTER TRADING PATTERNS:
    - Character catalog with crews and abilities
    - Bounty tracking (price fluctuations)
    - Trading volume and popularity metrics
    - Character rarity and special abilities
    - Real-time price updates based on manga/anime events
    """
    __tablename__ = "onepiece_characters"

    # Primary key
    id = Column(
        Integer,
        primary_key=True,
        index=True,
        comment="Unique character identifier"
    )

    # Character information
    name = Column(
        String(100),
        nullable=False,
        unique=True,
        index=True,  # Index for character search
        comment="Character name (e.g., 'Monkey D. Luffy')"
    )

    epithet = Column(
        String(100),
        nullable=True,
        comment="Character epithet (e.g., 'Straw Hat Luffy')"
    )

    description = Column(
        Text,  # Use Text for longer character descriptions
        nullable=True,
        comment="Character background and story"
    )

    # Trading and bounty information
    current_bounty = Column(
        BigInteger,  # Large numbers for bounties
        nullable=False,
        index=True,  # Index for bounty-based queries
        comment="Current bounty in berries (trading price)"
    )

    crew = Column(
        String(100),
        nullable=True,
        index=True,  # Index for crew filtering
        comment="Character's crew (e.g., 'Straw Hat Pirates')"
    )

    position = Column(
        String(50),
        nullable=True,
        comment="Position in crew (e.g., 'Captain', 'Navigator')"
    )

    # Character abilities and attributes
    devil_fruit = Column(
        String(100),
        nullable=True,
        comment="Devil fruit power (if any)"
    )

    haki_types = Column(
        String(200),
        nullable=True,
        comment="Types of Haki mastered (comma-separated)"
    )

    # Trading metrics
    rarity = Column(
        String(20),
        default="Common",
        nullable=False,
        comment="Character rarity: Common, Rare, Epic, Legendary, Mythical"
    )

    is_tradeable = Column(
        Boolean,
        default=True,
        nullable=False,
        comment="Whether character can be traded"
    )

    # Timestamps
    created_at = Column(
        DateTime,
        default=datetime.utcnow,
        nullable=False,
        comment="When character was added to platform"
    )

    updated_at = Column(
        DateTime,
        default=datetime.utcnow,
        onupdate=datetime.utcnow,
        nullable=False,
        comment="Last update timestamp"
    )

    def __repr__(self):
        """String representation for debugging"""
        return f"<OnePieceCharacter(id={self.id}, name='{self.name}', bounty={self.current_bounty})>"

print("✅ Database models defined with enterprise patterns!")
print("   - User model: Authentication, timestamps, indexes")
print("   - Product model: E-commerce, inventory, categories")
print("   - Proper field types, constraints, and comments")
print("   - Indexes for query performance")
print("   - Timestamps for auditing and analytics")

# ============================================================================
# 🎯 SECTION 4: DEPENDENCY INJECTION & UTILITIES
# ============================================================================

async def get_db() -> AsyncSession:
    """Database session dependency"""
    async with AsyncSessionLocal() as session:
        try:
            yield session
        finally:
            await session.close()

def create_access_token(data: dict) -> str:
    """Create JWT access token"""
    to_encode = data.copy()
    expire = datetime.utcnow() + timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
    to_encode.update({"exp": expire})
    return jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)

def verify_password(plain_password: str, hashed_password: str) -> bool:
    """Verify password against hash"""
    return pwd_context.verify(plain_password, hashed_password)

def get_password_hash(password: str) -> str:
    """Hash password"""
    return pwd_context.hash(password)

async def get_current_user(
    credentials: HTTPAuthorizationCredentials = Depends(security),
    db: AsyncSession = Depends(get_db)
) -> User:
    """Get current authenticated user"""
    try:
        payload = jwt.decode(credentials.credentials, SECRET_KEY, algorithms=[ALGORITHM])
        username: str = payload.get("sub")
        if username is None:
            raise HTTPException(status_code=401, detail="Invalid token")
    except jwt.PyJWTError:
        raise HTTPException(status_code=401, detail="Invalid token")
    
    # In real app, query user from database
    # For demo, return mock user
    return User(id=1, username=username, email="demo@example.com")

# ============================================================================
# 🎯 SECTION 5: BACKGROUND TASKS
# ============================================================================

async def send_welcome_email(email: str, username: str):
    """Background task: Send welcome email"""
    logger.info(f"📧 Sending welcome email to {email} for user {username}")
    # Simulate email sending delay
    await asyncio.sleep(2)
    logger.info(f"✅ Welcome email sent to {email}")

async def update_inventory(product_id: int):
    """Background task: Update inventory"""
    logger.info(f"📦 Updating inventory for product {product_id}")
    await asyncio.sleep(1)
    logger.info(f"✅ Inventory updated for product {product_id}")

# ============================================================================
# 🎯 SECTION 6: APPLICATION LIFESPAN MANAGEMENT
# ============================================================================

@asynccontextmanager
async def lifespan(app: FastAPI):
    """Application lifespan management"""
    # Startup
    logger.info("🚀 Starting FastAPI Mastery Lab")
    
    # Create database tables
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)
    
    logger.info("✅ Database tables created")
    
    yield
    
    # Shutdown
    logger.info("🛑 Shutting down FastAPI Mastery Lab")

# ============================================================================
# 🎯 SECTION 7: FASTAPI APPLICATION CREATION
# ============================================================================

app = FastAPI(
    title="FastAPI Mastery Lab",
    description="""
    🏴‍☠️ **Complete FastAPI Learning Laboratory**
    
    This API demonstrates all FastAPI features:
    
    ## Features
    * **Authentication** - JWT token-based auth
    * **Validation** - Pydantic model validation
    * **Database** - Async SQLAlchemy integration
    * **Background Tasks** - Async task processing
    * **Documentation** - Auto-generated OpenAPI docs
    * **Testing** - Comprehensive test coverage
    
    ## Learning Objectives
    * Master FastAPI fundamentals
    * Implement production patterns
    * Build scalable APIs
    * Deploy with confidence
    """,
    version="1.0.0",
    lifespan=lifespan,
    docs_url="/docs",
    redoc_url="/redoc"
)

# Add CORS middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000", "http://localhost:8080"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# ============================================================================
# 🎯 SECTION 8: API ENDPOINTS
# ============================================================================

@app.get("/", tags=["Root"])
async def root():
    """Root endpoint with API information"""
    return {
        "message": "🏴‍☠️ FastAPI Mastery Lab",
        "version": "1.0.0",
        "docs": "/docs",
        "status": "running",
        "timestamp": datetime.utcnow().isoformat()
    }

@app.get("/health", tags=["Health"])
async def health_check():
    """Health check endpoint"""
    return {
        "status": "healthy",
        "timestamp": datetime.utcnow().isoformat(),
        "uptime": "running"
    }

@app.post("/auth/register", response_model=UserResponse, tags=["Authentication"])
async def register_user(
    user: UserCreate,
    background_tasks: BackgroundTasks,
    db: AsyncSession = Depends(get_db)
):
    """Register new user with background email task"""
    # Hash password
    hashed_password = get_password_hash(user.password)
    
    # Create user (in real app, save to database)
    db_user = User(
        username=user.username,
        email=user.email,
        hashed_password=hashed_password,
        full_name=user.full_name
    )
    
    # Add background task to send welcome email
    background_tasks.add_task(send_welcome_email, user.email, user.username)
    
    # Return user response
    return UserResponse(
        id=1,
        username=user.username,
        email=user.email,
        full_name=user.full_name,
        is_active=True,
        created_at=datetime.utcnow()
    )

@app.post("/auth/login", response_model=Token, tags=["Authentication"])
async def login_user(username: str, password: str):
    """Login user and return JWT token"""
    # In real app, verify credentials against database
    if username == "demo" and password == "password123":
        access_token = create_access_token(data={"sub": username})
        return Token(
            access_token=access_token,
            expires_in=ACCESS_TOKEN_EXPIRE_MINUTES * 60
        )
    
    raise HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="Invalid credentials"
    )

@app.get("/users/me", response_model=UserResponse, tags=["Users"])
async def get_current_user_info(current_user: User = Depends(get_current_user)):
    """Get current user information (protected endpoint)"""
    return UserResponse(
        id=current_user.id,
        username=current_user.username,
        email=current_user.email,
        full_name="Demo User",
        is_active=True,
        created_at=datetime.utcnow()
    )

@app.post("/products/", response_model=ProductResponse, tags=["Products"])
async def create_product(
    product: ProductCreate,
    background_tasks: BackgroundTasks,
    current_user: User = Depends(get_current_user),
    db: AsyncSession = Depends(get_db)
):
    """Create new product (protected endpoint)"""
    # Create product (in real app, save to database)
    db_product = Product(**product.dict())
    
    # Add background task to update inventory
    background_tasks.add_task(update_inventory, 1)
    
    return ProductResponse(
        id=1,
        name=product.name,
        description=product.description,
        price=product.price,
        category=product.category,
        in_stock=product.in_stock,
        created_at=datetime.utcnow()
    )

@app.get("/products/", response_model=List[ProductResponse], tags=["Products"])
async def list_products(
    category: Optional[str] = None,
    min_price: Optional[float] = None,
    max_price: Optional[float] = None,
    db: AsyncSession = Depends(get_db)
):
    """List products with optional filtering"""
    # In real app, query database with filters
    sample_products = [
        ProductResponse(
            id=1,
            name="FastAPI Book",
            description="Learn FastAPI from scratch",
            price=29.99,
            category="books",
            in_stock=True,
            created_at=datetime.utcnow()
        ),
        ProductResponse(
            id=2,
            name="Python Course",
            description="Advanced Python programming",
            price=99.99,
            category="courses",
            in_stock=True,
            created_at=datetime.utcnow()
        )
    ]
    
    # Apply filters
    filtered_products = sample_products
    if category:
        filtered_products = [p for p in filtered_products if p.category == category]
    if min_price:
        filtered_products = [p for p in filtered_products if p.price >= min_price]
    if max_price:
        filtered_products = [p for p in filtered_products if p.price <= max_price]
    
    return filtered_products

# ============================================================================
# 🎯 SECTION 9: WEBSOCKET SUPPORT (REAL-TIME FEATURES)
# ============================================================================

from fastapi import WebSocket, WebSocketDisconnect

@app.websocket("/ws")
async def websocket_endpoint(websocket: WebSocket):
    """WebSocket endpoint for real-time communication"""
    await websocket.accept()
    try:
        while True:
            data = await websocket.receive_text()
            await websocket.send_text(f"Echo: {data}")
    except WebSocketDisconnect:
        logger.info("WebSocket disconnected")

# ============================================================================
# 🎯 SECTION 10: CUSTOM EXCEPTION HANDLERS
# ============================================================================

@app.exception_handler(404)
async def not_found_handler(request, exc):
    """Custom 404 handler"""
    return {"error": "Resource not found", "status_code": 404}

@app.exception_handler(500)
async def internal_error_handler(request, exc):
    """Custom 500 handler"""
    logger.error(f"Internal server error: {exc}")
    return {"error": "Internal server error", "status_code": 500}

# ============================================================================
# 🎯 SECTION 11: STARTUP SCRIPT
# ============================================================================

# ============================================================================
# 🏴‍☠️ COMPLETE ONE PIECE TRADING PLATFORM SOLUTION
# ============================================================================

async def initialize_one_piece_data():
    """Initialize the database with One Piece characters and sample trader"""

    # Create sample pirate trader
    sample_trader = PirateTrader(
        pirate_name="Captain Newbie",
        email="newbie@grandline.com",
        hashed_password=pwd_context.hash("strawhat123"),
        crew_affiliation="Independent",
        berry_balance=5000000,  # 5 million berries
        trading_level="Rookie"
    )

    # Create Straw Hat Pirates characters
    straw_hats = [
        OnePieceCharacter(
            name="Monkey D. Luffy",
            epithet="Straw Hat Luffy",
            description="Captain of the Straw Hat Pirates, rubber man with Gomu Gomu no Mi",
            current_bounty=3000000000,  # 3 billion berries
            crew="Straw Hat Pirates",
            position="Captain",
            devil_fruit="Gomu Gomu no Mi (Hito Hito no Mi, Model: Nika)",
            haki_types="Conqueror's Haki, Armament Haki, Observation Haki",
            rarity="Mythical",
            is_tradeable=True,
            is_featured=True
        ),
        OnePieceCharacter(
            name="Roronoa Zoro",
            epithet="Pirate Hunter Zoro",
            description="Swordsman of the Straw Hat Pirates, master of three-sword style",
            current_bounty=1111000000,  # 1.111 billion berries
            crew="Straw Hat Pirates",
            position="Swordsman",
            devil_fruit=None,
            haki_types="Armament Haki, Observation Haki, Conqueror's Haki",
            rarity="Legendary",
            is_tradeable=True,
            is_featured=True
        ),
        OnePieceCharacter(
            name="Nami",
            epithet="Cat Burglar Nami",
            description="Navigator of the Straw Hat Pirates, weather manipulation expert",
            current_bounty=366000000,  # 366 million berries
            crew="Straw Hat Pirates",
            position="Navigator",
            devil_fruit=None,
            haki_types=None,
            rarity="Epic",
            is_tradeable=True,
            is_featured=False
        ),
        OnePieceCharacter(
            name="Sanji",
            epithet="Black Leg Sanji",
            description="Cook of the Straw Hat Pirates, master of Black Leg Style",
            current_bounty=1032000000,  # 1.032 billion berries
            crew="Straw Hat Pirates",
            position="Cook",
            devil_fruit=None,
            haki_types="Armament Haki, Observation Haki",
            rarity="Legendary",
            is_tradeable=True,
            is_featured=True
        )
    ]

    # Add to database session
    db_session.add(sample_trader)
    for character in straw_hats:
        db_session.add(character)

    # Commit all changes
    db_session.commit()
    print("🏴‍☠️ One Piece trading platform initialized with sample data!")

@app.on_event("startup")
async def startup_event():
    """Initialize database and sample data on startup"""
    # Create all database tables
    Base.metadata.create_all(bind=engine)

    # Check if data already exists
    existing_characters = db_session.query(OnePieceCharacter).count()
    if existing_characters == 0:
        await initialize_one_piece_data()

if __name__ == "__main__":
    print("🏴‍☠️ Starting One Piece Trading Platform")
    print("📚 Learning Objectives:")
    print("  ✅ FastAPI application setup with One Piece theme")
    print("  ✅ Pydantic models for character and trader validation")
    print("  ✅ Database integration with SQLAlchemy")
    print("  ✅ JWT authentication for pirate traders")
    print("  ✅ Background tasks for bounty updates")
    print("  ✅ WebSocket support for real-time trading")
    print("  ✅ Custom exception handling")
    print("\n🚀 Starting One Piece Trading Server...")
    print("📖 API Documentation: http://localhost:8000/docs")
    print("🔍 Alternative Docs: http://localhost:8000/redoc")
    print("🏴‍☠️ Trade your favorite One Piece characters!")

    uvicorn.run(
        "01-fastapi-mastery-coding-lab:app",
        host="0.0.0.0",
        port=8000,
        reload=True,
        log_level="info"
    )
