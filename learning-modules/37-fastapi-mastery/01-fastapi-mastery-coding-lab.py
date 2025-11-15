#!/usr/bin/env python3
"""
🏴‍☠️ FASTAPI MASTERY - HANDS-ON CODING LAB
Complete FastAPI implementation with real-world examples

This lab covers:
- FastAPI application setup
- Pydantic models and validation
- Database integration with SQLAlchemy
- Authentication and security
- Background tasks and async operations
- Testing and documentation
- Production deployment patterns

Run this lab: python 01-fastapi-mastery-coding-lab.py
"""

import asyncio
import logging
from datetime import datetime, timedelta
from typing import List, Optional
from contextlib import asynccontextmanager

# FastAPI and related imports
from fastapi import FastAPI, HTTPException, Depends, BackgroundTasks, status
from fastapi.middleware.cors import CORSMiddleware
from fastapi.security import HTTPBearer, HTTPAuthorizationCredentials
from pydantic import BaseModel, Field, EmailStr
import uvicorn

# Database imports
from sqlalchemy.ext.asyncio import AsyncSession, create_async_engine
from sqlalchemy.orm import sessionmaker, declarative_base
from sqlalchemy import Column, Integer, String, DateTime, Float, Boolean

# Security imports
import jwt
from passlib.context import CryptContext
import secrets

# ============================================================================
# 🎯 SECTION 1: FASTAPI APPLICATION SETUP
# ============================================================================

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# Database setup (SQLite for demo - use PostgreSQL in production)
DATABASE_URL = "sqlite+aiosqlite:///./fastapi_lab.db"
engine = create_async_engine(DATABASE_URL, echo=True)
AsyncSessionLocal = sessionmaker(engine, class_=AsyncSession, expire_on_commit=False)
Base = declarative_base()

# Security configuration
SECRET_KEY = secrets.token_urlsafe(32)
ALGORITHM = "HS256"
ACCESS_TOKEN_EXPIRE_MINUTES = 30
pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")
security = HTTPBearer()

# ============================================================================
# 🎯 SECTION 2: PYDANTIC MODELS (REQUEST/RESPONSE VALIDATION)
# ============================================================================

class UserCreate(BaseModel):
    """User registration model with validation"""
    username: str = Field(..., min_length=3, max_length=50, description="Username (3-50 chars)")
    email: EmailStr = Field(..., description="Valid email address")
    password: str = Field(..., min_length=8, description="Password (min 8 chars)")
    full_name: Optional[str] = Field(None, max_length=100, description="Full name")

class UserResponse(BaseModel):
    """User response model (excludes sensitive data)"""
    id: int
    username: str
    email: str
    full_name: Optional[str]
    is_active: bool
    created_at: datetime

    class Config:
        from_attributes = True

class Token(BaseModel):
    """JWT token response"""
    access_token: str
    token_type: str = "bearer"
    expires_in: int

class ProductCreate(BaseModel):
    """Product creation model"""
    name: str = Field(..., min_length=1, max_length=200)
    description: Optional[str] = Field(None, max_length=1000)
    price: float = Field(..., gt=0, description="Price must be positive")
    category: str = Field(..., min_length=1, max_length=100)
    in_stock: bool = True

class ProductResponse(BaseModel):
    """Product response model"""
    id: int
    name: str
    description: Optional[str]
    price: float
    category: str
    in_stock: bool
    created_at: datetime

    class Config:
        from_attributes = True

# ============================================================================
# 🎯 SECTION 3: DATABASE MODELS (SQLAlchemy)
# ============================================================================

class User(Base):
    """User database model"""
    __tablename__ = "users"
    
    id = Column(Integer, primary_key=True, index=True)
    username = Column(String(50), unique=True, index=True, nullable=False)
    email = Column(String(100), unique=True, index=True, nullable=False)
    hashed_password = Column(String(100), nullable=False)
    full_name = Column(String(100), nullable=True)
    is_active = Column(Boolean, default=True)
    created_at = Column(DateTime, default=datetime.utcnow)


class Product(Base):
    """Product database model"""
    __tablename__ = "products"
    
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(200), nullable=False, index=True)
    description = Column(String(1000), nullable=True)
    price = Column(Float, nullable=False)
    category = Column(String(100), nullable=False, index=True)
    in_stock = Column(Boolean, default=True)
    created_at = Column(DateTime, default=datetime.utcnow)

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

if __name__ == "__main__":
    print("🏴‍☠️ Starting FastAPI Mastery Lab")
    print("📚 Learning Objectives:")
    print("  ✅ FastAPI application setup")
    print("  ✅ Pydantic models and validation")
    print("  ✅ Database integration")
    print("  ✅ Authentication and security")
    print("  ✅ Background tasks")
    print("  ✅ WebSocket support")
    print("  ✅ Custom exception handling")
    print("\n🚀 Starting server...")
    print("📖 API Documentation: http://localhost:8000/docs")
    print("🔍 Alternative Docs: http://localhost:8000/redoc")
    
    uvicorn.run(
        "01-fastapi-mastery-coding-lab:app",
        host="0.0.0.0",
        port=8000,
        reload=True,
        log_level="info"
    )
