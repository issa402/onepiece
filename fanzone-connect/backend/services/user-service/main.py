"""
🏆 FANZONE CONNECT - USER SERVICE
Combines Multiple Learning Modules:
- Module 05: CI/CD Testing (pytest, test automation)
- Module 07: Security Authentication (OAuth2, JWT, encryption)
- Module 37: FastAPI Mastery (async APIs, dependency injection)
- Module 38: Advanced Backend Engineering (API design, validation)

World Cup 2026 Fan Platform - User Management Microservice
"""

import asyncio
import logging
from contextlib import asynccontextmanager
from datetime import datetime, timedelta
from typing import List, Optional
import uuid

import bcrypt
import jwt
from fastapi import FastAPI, HTTPException, Depends, status, Security
from fastapi.security import HTTPBearer, HTTPAuthorizationCredentials
from fastapi.middleware.cors import CORSMiddleware
from fastapi.middleware.trustedhost import TrustedHostMiddleware
from pydantic import BaseModel, EmailStr, validator
from sqlalchemy.ext.asyncio import AsyncSession, create_async_engine, async_sessionmaker
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column
from sqlalchemy import String, DateTime, Boolean, select
import redis.asyncio as redis

# Configure logging for production monitoring
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger(__name__)

# =====================================================
# MODULE 07: SECURITY & AUTHENTICATION
# =====================================================

class SecurityConfig:
    """Advanced security configuration for World Cup platform"""
    SECRET_KEY = "worldcup2026-fanzone-connect-ultra-secure-key"
    ALGORITHM = "HS256"
    ACCESS_TOKEN_EXPIRE_MINUTES = 30
    REFRESH_TOKEN_EXPIRE_DAYS = 7
    PASSWORD_MIN_LENGTH = 8
    MAX_LOGIN_ATTEMPTS = 5
    LOCKOUT_DURATION_MINUTES = 15

security = HTTPBearer()

class PasswordValidator:
    """Advanced password validation with security best practices"""
    
    @staticmethod
    def validate_password(password: str) -> bool:
        """Validate password strength for World Cup security"""
        if len(password) < SecurityConfig.PASSWORD_MIN_LENGTH:
            return False
        
        has_upper = any(c.isupper() for c in password)
        has_lower = any(c.islower() for c in password)
        has_digit = any(c.isdigit() for c in password)
        has_special = any(c in "!@#$%^&*()_+-=[]{}|;:,.<>?" for c in password)
        
        return all([has_upper, has_lower, has_digit, has_special])
    
    @staticmethod
    def hash_password(password: str) -> str:
        """Hash password using bcrypt with salt"""
        salt = bcrypt.gensalt()
        return bcrypt.hashpw(password.encode('utf-8'), salt).decode('utf-8')
    
    @staticmethod
    def verify_password(password: str, hashed: str) -> bool:
        """Verify password against hash"""
        return bcrypt.checkpw(password.encode('utf-8'), hashed.encode('utf-8'))

class JWTManager:
    """JWT token management for secure authentication"""
    
    @staticmethod
    def create_access_token(data: dict) -> str:
        """Create JWT access token for World Cup fans"""
        to_encode = data.copy()
        expire = datetime.utcnow() + timedelta(minutes=SecurityConfig.ACCESS_TOKEN_EXPIRE_MINUTES)
        to_encode.update({"exp": expire, "type": "access"})
        
        return jwt.encode(to_encode, SecurityConfig.SECRET_KEY, algorithm=SecurityConfig.ALGORITHM)
    
    @staticmethod
    def create_refresh_token(data: dict) -> str:
        """Create JWT refresh token"""
        to_encode = data.copy()
        expire = datetime.utcnow() + timedelta(days=SecurityConfig.REFRESH_TOKEN_EXPIRE_DAYS)
        to_encode.update({"exp": expire, "type": "refresh"})
        
        return jwt.encode(to_encode, SecurityConfig.SECRET_KEY, algorithm=SecurityConfig.ALGORITHM)
    
    @staticmethod
    def verify_token(token: str) -> dict:
        """Verify and decode JWT token"""
        try:
            payload = jwt.decode(token, SecurityConfig.SECRET_KEY, algorithms=[SecurityConfig.ALGORITHM])
            return payload
        except jwt.ExpiredSignatureError:
            raise HTTPException(
                status_code=status.HTTP_401_UNAUTHORIZED,
                detail="Token has expired"
            )
        except jwt.JWTError:
            raise HTTPException(
                status_code=status.HTTP_401_UNAUTHORIZED,
                detail="Invalid token"
            )

# =====================================================
# MODULE 37: FASTAPI MASTERY & MODULE 38: ADVANCED BACKEND
# =====================================================

class Base(DeclarativeBase):
    """SQLAlchemy base class with advanced ORM features"""
    pass

class User(Base):
    """User model for World Cup 2026 fans"""
    __tablename__ = "users"
    
    id: Mapped[str] = mapped_column(String, primary_key=True, default=lambda: str(uuid.uuid4()))
    email: Mapped[str] = mapped_column(String, unique=True, index=True)
    username: Mapped[str] = mapped_column(String, unique=True, index=True)
    password_hash: Mapped[str] = mapped_column(String)
    first_name: Mapped[Optional[str]] = mapped_column(String)
    last_name: Mapped[Optional[str]] = mapped_column(String)
    country_code: Mapped[Optional[str]] = mapped_column(String(2))
    preferred_language: Mapped[str] = mapped_column(String(2), default="en")
    is_active: Mapped[bool] = mapped_column(Boolean, default=True)
    is_verified: Mapped[bool] = mapped_column(Boolean, default=False)
    fan_level: Mapped[str] = mapped_column(String, default="standard")  # standard, premium, vip
    created_at: Mapped[datetime] = mapped_column(DateTime, default=datetime.utcnow)
    updated_at: Mapped[datetime] = mapped_column(DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)

# Pydantic models for API validation
class UserCreate(BaseModel):
    """User creation schema with advanced validation"""
    email: EmailStr
    username: str
    password: str
    first_name: Optional[str] = None
    last_name: Optional[str] = None
    country_code: Optional[str] = None
    preferred_language: str = "en"
    
    @validator('username')
    def validate_username(cls, v):
        if len(v) < 3 or len(v) > 30:
            raise ValueError('Username must be between 3 and 30 characters')
        if not v.isalnum():
            raise ValueError('Username must contain only alphanumeric characters')
        return v
    
    @validator('password')
    def validate_password(cls, v):
        if not PasswordValidator.validate_password(v):
            raise ValueError('Password must be at least 8 characters with uppercase, lowercase, digit, and special character')
        return v

class UserResponse(BaseModel):
    """User response schema"""
    id: str
    email: str
    username: str
    first_name: Optional[str]
    last_name: Optional[str]
    country_code: Optional[str]
    preferred_language: str
    is_active: bool
    is_verified: bool
    fan_level: str
    created_at: datetime
    
    class Config:
        from_attributes = True

class LoginRequest(BaseModel):
    """Login request schema"""
    email: str
    password: str

class TokenResponse(BaseModel):
    """Token response schema"""
    access_token: str
    refresh_token: str
    token_type: str = "bearer"
    expires_in: int = SecurityConfig.ACCESS_TOKEN_EXPIRE_MINUTES * 60

# =====================================================
# DATABASE & REDIS SETUP
# =====================================================

# Database setup
DATABASE_URL = "postgresql+asyncpg://fanzone_user:worldcup2026@postgres:5432/fanzone_connect"
engine = create_async_engine(DATABASE_URL, echo=True)
AsyncSessionLocal = async_sessionmaker(engine, expire_on_commit=False)

# Redis setup for caching and rate limiting
redis_client = None

async def get_redis():
    """Get Redis client for caching"""
    global redis_client
    if redis_client is None:
        redis_client = redis.from_url("redis://redis:6379", decode_responses=True)
    return redis_client

async def get_db():
    """Database dependency injection"""
    async with AsyncSessionLocal() as session:
        try:
            yield session
        finally:
            await session.close()

# =====================================================
# AUTHENTICATION DEPENDENCIES
# =====================================================

async def get_current_user(
    credentials: HTTPAuthorizationCredentials = Security(security),
    db: AsyncSession = Depends(get_db)
) -> User:
    """Get current authenticated user"""
    token = credentials.credentials
    payload = JWTManager.verify_token(token)
    
    user_id = payload.get("sub")
    if user_id is None:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Invalid token payload"
        )
    
    result = await db.execute(select(User).where(User.id == user_id))
    user = result.scalar_one_or_none()
    
    if user is None:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="User not found"
        )
    
    return user

# =====================================================
# FASTAPI APPLICATION WITH LIFESPAN MANAGEMENT
# =====================================================

@asynccontextmanager
async def lifespan(app: FastAPI):
    """Application lifespan management"""
    logger.info("🏆 FANZONE CONNECT User Service Starting...")
    logger.info("🌍 World Cup 2026 Fan Platform - User Management")

    # Initialize database tables
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)

    # Initialize Redis connection
    await get_redis()

    logger.info("✅ User Service Ready for World Cup 2026!")
    yield

    # Cleanup
    if redis_client:
        await redis_client.close()
    await engine.dispose()
    logger.info("🏁 User Service Shutdown Complete")

# FastAPI application with advanced configuration
app = FastAPI(
    title="🏆 FANZONE CONNECT - User Service",
    description="World Cup 2026 Fan Platform - User Management Microservice",
    version="1.0.0",
    lifespan=lifespan,
    docs_url="/docs",
    redoc_url="/redoc"
)

# Security middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000", "https://fanzoneconnect.com"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.add_middleware(
    TrustedHostMiddleware,
    allowed_hosts=["localhost", "*.fanzoneconnect.com"]
)

# =====================================================
# API ENDPOINTS WITH ADVANCED FEATURES
# =====================================================

@app.get("/health")
async def health_check():
    """Health check endpoint for load balancer"""
    return {
        "status": "healthy",
        "service": "user-service",
        "timestamp": datetime.utcnow().isoformat(),
        "version": "1.0.0"
    }

@app.post("/register", response_model=UserResponse, status_code=status.HTTP_201_CREATED)
async def register_user(
    user_data: UserCreate,
    db: AsyncSession = Depends(get_db),
    redis_conn = Depends(get_redis)
):
    """Register new World Cup fan with advanced validation"""

    # Check if user already exists
    result = await db.execute(
        select(User).where(
            (User.email == user_data.email) | (User.username == user_data.username)
        )
    )
    existing_user = result.scalar_one_or_none()

    if existing_user:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="User with this email or username already exists"
        )

    # Create new user
    hashed_password = PasswordValidator.hash_password(user_data.password)

    new_user = User(
        email=user_data.email,
        username=user_data.username,
        password_hash=hashed_password,
        first_name=user_data.first_name,
        last_name=user_data.last_name,
        country_code=user_data.country_code,
        preferred_language=user_data.preferred_language
    )

    db.add(new_user)
    await db.commit()
    await db.refresh(new_user)

    # Cache user data in Redis
    await redis_conn.setex(
        f"user:{new_user.id}",
        3600,  # 1 hour cache
        f"{new_user.email}:{new_user.username}"
    )

    logger.info(f"🎉 New World Cup fan registered: {new_user.email}")
    return new_user

@app.post("/login", response_model=TokenResponse)
async def login_user(
    login_data: LoginRequest,
    db: AsyncSession = Depends(get_db),
    redis_conn = Depends(get_redis)
):
    """Authenticate World Cup fan with JWT tokens"""

    # Rate limiting check
    login_key = f"login_attempts:{login_data.email}"
    attempts = await redis_conn.get(login_key)

    if attempts and int(attempts) >= SecurityConfig.MAX_LOGIN_ATTEMPTS:
        raise HTTPException(
            status_code=status.HTTP_429_TOO_MANY_REQUESTS,
            detail=f"Too many login attempts. Try again in {SecurityConfig.LOCKOUT_DURATION_MINUTES} minutes."
        )

    # Find user
    result = await db.execute(select(User).where(User.email == login_data.email))
    user = result.scalar_one_or_none()

    if not user or not PasswordValidator.verify_password(login_data.password, user.password_hash):
        # Increment failed attempts
        current_attempts = int(attempts) + 1 if attempts else 1
        await redis_conn.setex(login_key, SecurityConfig.LOCKOUT_DURATION_MINUTES * 60, current_attempts)

        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Invalid email or password"
        )

    if not user.is_active:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Account is deactivated"
        )

    # Clear failed attempts on successful login
    await redis_conn.delete(login_key)

    # Create tokens
    token_data = {"sub": user.id, "email": user.email, "username": user.username}
    access_token = JWTManager.create_access_token(token_data)
    refresh_token = JWTManager.create_refresh_token(token_data)

    logger.info(f"🔐 World Cup fan logged in: {user.email}")

    return TokenResponse(
        access_token=access_token,
        refresh_token=refresh_token
    )

@app.get("/profile", response_model=UserResponse)
async def get_user_profile(current_user: User = Depends(get_current_user)):
    """Get current user profile"""
    return current_user

@app.get("/users", response_model=List[UserResponse])
async def list_users(
    skip: int = 0,
    limit: int = 100,
    db: AsyncSession = Depends(get_db),
    current_user: User = Depends(get_current_user)
):
    """List World Cup fans (admin only)"""
    # In production, add admin role check
    result = await db.execute(select(User).offset(skip).limit(limit))
    users = result.scalars().all()
    return users

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(
        "main:app",
        host="0.0.0.0",
        port=8001,
        reload=True,
        log_level="info"
    )
