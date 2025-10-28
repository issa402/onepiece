# ============================================================================
# 📚 LEARNING GUIDE: FastAPI Main Application (app/main.py)
# ============================================================================
#
# 🎯 PURPOSE:
# This is the entry point for your Python FastAPI backend service. It handles:
# - Application initialization and configuration
# - Middleware setup (CORS, security, rate limiting)
# - API route registration and organization
# - Background task coordination with Celery
# - Health checks and monitoring endpoints
# - Integration with other microservices (Java API Gateway)
#
# 🔧 TECHNOLOGIES USED:
# - FastAPI: Modern Python web framework with automatic API docs
# - Uvicorn: ASGI server for running FastAPI applications
# - Pydantic: Data validation and serialization
# - SQLAlchemy: Database ORM for PostgreSQL integration
# - Celery: Distributed task queue for background jobs
# - Redis: Message broker and caching layer
# - Middleware: CORS, security headers, rate limiting
#
# 📖 IN-DEPTH EXPLANATION:
#
# **What is FastAPI and why use it?**
# FastAPI is a modern Python web framework that provides:
# - Automatic API documentation (Swagger/OpenAPI)
# - Type hints for request/response validation
# - Async/await support for high performance
# - Dependency injection system
# - Built-in security features
#
# **Application Lifecycle:**
# 1. Startup: Initialize database, Redis, background services
# 2. Request Processing: Handle HTTP requests with middleware chain
# 3. Response: Return JSON responses with proper status codes
# 4. Shutdown: Clean up resources and connections
#
# **Middleware Chain (Order Matters!):**
# 1. TrustedHostMiddleware - Validate allowed hosts
# 2. CORSMiddleware - Handle cross-origin requests
# 3. RateLimitMiddleware - Prevent abuse
# 4. Your custom middleware
# 5. FastAPI routing and endpoint handlers
#
# **Background Tasks vs Celery:**
# - FastAPI BackgroundTasks: Simple, in-process tasks
# - Celery: Distributed, scalable, persistent task queue
# - Use Celery for: Web scraping, AI analysis, data processing
# - Use BackgroundTasks for: Logging, cleanup, notifications
#
# 📚 LEARNING MODULE REFERENCES:
# - Module 34 (TypeScript/Node.js): Lines 200-300 - Express.js middleware patterns
# - Module 35 (React/Next.js): Lines 400-500 - API route handling in Next.js
# - Module 36 (AI/LLM Integration): Lines 100-200 - Async service integration
#
# ✅ IMPLEMENTATION CHECKLIST:
# [ ] Set up FastAPI app with proper configuration
# [ ] Configure middleware in correct order
# [ ] Implement lifespan events for startup/shutdown
# [ ] Create health check endpoints
# [ ] Set up API route organization
# [ ] Configure CORS for frontend integration
# [ ] Add rate limiting and security headers
# [ ] Integrate with database and Redis
# [ ] Set up background task coordination
# [ ] Add comprehensive error handling
# [ ] Configure logging and monitoring
#
# 🎓 WHAT YOU NEED TO LEARN/UNDERSTAND:
# - FastAPI dependency injection system
# - Async/await patterns in Python
# - Middleware execution order and purpose
# - CORS and security best practices
# - Database connection pooling
# - Background task patterns
# - API versioning strategies
# - Health check implementation
# - Error handling and status codes
# - Logging and monitoring setup
#
# 🚀 REAL-WORLD EXAMPLES:
# - Netflix: Uses FastAPI for microservices
# - Uber: FastAPI for real-time data processing
# - Microsoft: FastAPI for AI/ML model serving
#
# ============================================================================

# ============================================================================
# 💻 YOUR CODE GOES HERE - TRY TO IMPLEMENT FIRST!
# ============================================================================
#
# 🎯 YOUR TASK: Create a FastAPI application for sports betting consensus
#
# 📋 STEP-BY-STEP IMPLEMENTATION:
#
# 1. Import required libraries:
#    - FastAPI (main framework)
#    - HTTPException (error handling)
#    - CORSMiddleware (cross-origin requests)
#    - Pydantic BaseModel (data validation)
#    - uvicorn (ASGI server)
#
# 2. Create FastAPI app with:
#    - Title and description
#    - Version information
#    - API documentation settings
#    - Middleware configuration
#
# 3. Add middleware in correct order:
#    - TrustedHostMiddleware (security)
#    - CORSMiddleware (frontend access)
#    - Custom middleware (optional)
#
# 4. Create API endpoints:
#    - GET /health (health check)
#    - POST /api/v1/predictions/consensus (main prediction endpoint)
#    - GET /docs (automatic API documentation)
#
# ============================================================================
# 🎯 DETAILED EXPLANATION OF YOUR CODE:
# ============================================================================

# ============================================================================
# STEP 1: IMPORTS - WHAT EACH ONE DOES
# ============================================================================
#
# **WHAT YOU WROTE:**
from fastapi import FastAPI, HTTPException, Depends, BackgroundTasks
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel

# **DETAILED BREAKDOWN:**
#
# 🔹 **FastAPI**: The main web framework class
#    - WHAT IT DOES: Creates your web server (like Apache or Nginx but for Python)
#    - WHY YOU NEED IT: This IS your API - without it, no web server exists
#    - REAL EXAMPLE: Netflix uses FastAPI for their recommendation microservices
#    - HOW IT WORKS: Handles HTTP requests (GET, POST) and returns JSON responses
#
# 🔹 **HTTPException**: For returning HTTP error codes
#    - WHAT IT DOES: Sends proper error responses (404 Not Found, 500 Server Error)
#    - WHY YOU NEED IT: When something goes wrong, users need meaningful error messages
#    - REAL EXAMPLE: When Spotify can't find a song, it returns HTTPException(404, "Song not found")
#    - HOW IT WORKS: raise HTTPException(status_code=404, detail="Game not found")
#
# 🔹 **Depends**: Dependency injection system
#    - WHAT IT DOES: Automatically provides things like database connections to your functions
#    - WHY YOU NEED IT: Avoids repeating code and manages resources efficiently
#    - REAL EXAMPLE: Instagram uses this to inject user authentication into every endpoint
#    - HOW IT WORKS: def get_prediction(db: Session = Depends(get_db)): # db is automatically provided
#
# 🔹 **BackgroundTasks**: Run tasks after returning response
#    - WHAT IT DOES: Lets you do slow work (like sending emails) without making users wait
#    - WHY YOU NEED IT: Web scraping takes time - users shouldn't wait 30 seconds for a response
#    - REAL EXAMPLE: When you upload to YouTube, the response is instant but video processing happens in background
#    - HOW IT WORKS: background_tasks.add_task(scrape_betting_sites, game_query)
#
# 🔹 **CORSMiddleware**: Allows browsers to call your API
#    - WHAT IT DOES: Tells browsers "yes, this React app can call this API"
#    - WHY YOU NEED IT: Without this, your frontend gets "CORS error" and can't load data
#    - REAL EXAMPLE: Facebook's API allows facebook.com to make calls but blocks other sites
#    - HOW IT WORKS: Adds HTTP headers like "Access-Control-Allow-Origin: http://localhost:3000"
#
# 🔹 **BaseModel**: Creates data validation classes
#    - WHAT IT DOES: Defines the structure of data your API accepts/returns
#    - WHY YOU NEED IT: Prevents bad data from crashing your app + automatic API docs
#    - REAL EXAMPLE: Twitter's API has a Tweet model with id, text, author fields
#    - HOW IT WORKS: class GameQuery(BaseModel): team1: str; team2: str

# ============================================================================
# STEP 2: FASTAPI APP CREATION - WHAT YOUR CODE DOES
# ============================================================================
#
# **WHAT YOU WROTE:**
app = FastAPI(
    title = "Sports Betting Consensus Aggregator",
    description = "AI-powered betting predictions",
    version = "1.0.0"
)

# **DETAILED BREAKDOWN:**
#
# 🔹 **app = FastAPI()**: Creates your web server instance
#    - WHAT IT DOES: This single line creates an entire web server capable of handling thousands of requests
#    - WHY YOU NEED IT: This IS your application - everything else attaches to this object
#    - REAL EXAMPLE: Like opening a restaurant - this creates the building, you add tables/menu later
#    - HOW IT WORKS: FastAPI() returns an ASGI application that can serve HTTP requests
#
# 🔹 **title**: Shows up in API documentation
#    - WHAT IT DOES: When developers visit /docs, they see this as the main heading
#    - WHY YOU NEED IT: Professional APIs always have clear titles for documentation
#    - REAL EXAMPLE: "Stripe Payment API", "GitHub REST API", "OpenAI API"
#    - HOW IT WORKS: FastAPI generates interactive docs at /docs using this title
#
# 🔹 **description**: Explains what your API does
#    - WHAT IT DOES: Appears under the title in API docs, explains the purpose
#    - WHY YOU NEED IT: Other developers need to understand what your API does
#    - REAL EXAMPLE: "Process payments securely", "Manage code repositories", "Generate AI text"
#    - HOW IT WORKS: Shows up in the OpenAPI/Swagger documentation interface
#
# 🔹 **version**: Tracks API changes
#    - WHAT IT DOES: Helps developers know which version they're using
#    - WHY YOU NEED IT: When you update your API, clients need to know what changed
#    - REAL EXAMPLE: "v1.0.0" (first release), "v1.1.0" (new features), "v2.0.0" (breaking changes)
#    - HOW IT WORKS: Follows semantic versioning (major.minor.patch)

# ============================================================================
# STEP 3: CORS MIDDLEWARE - WHAT YOUR CODE DOES
# ============================================================================
#
# **WHAT YOU WROTE:**
app.add_middleware(
    CORSMiddleware(
        allow_origins = ["http://localhost:3000"],
        allow_methods = ["*"],  # ⚠️ NOTE: You wrote "allow_method" but it should be "allow_methods"
        allow_headers = ["*"]
    )
)

# **DETAILED BREAKDOWN:**
#
# 🔹 **app.add_middleware()**: Adds functionality that runs on every request
#    - WHAT IT DOES: Middleware is like a security guard that checks every request before it reaches your endpoints
#    - WHY YOU NEED IT: Handles cross-cutting concerns (CORS, authentication, logging) automatically
#    - REAL EXAMPLE: Airport security checks every passenger - middleware checks every HTTP request
#    - HOW IT WORKS: Request → Middleware → Your endpoint → Middleware → Response
#
# 🔹 **CORSMiddleware**: Handles Cross-Origin Resource Sharing
#    - WHAT IT DOES: Tells browsers which websites are allowed to call your API
#    - WHY YOU NEED IT: By default, browsers block requests from localhost:3000 to localhost:8000
#    - REAL EXAMPLE: Without this, your React app gets "CORS policy" error when calling your API
#    - HOW IT WORKS: Adds special headers to responses that browsers understand
#
# 🔹 **allow_origins**: Which websites can call your API
#    - WHAT IT DOES: ["http://localhost:3000"] means only your React dev server can call this API
#    - WHY YOU NEED IT: Security - prevents random websites from using your API
#    - REAL EXAMPLE: Production might be ["https://yourdomain.com", "https://www.yourdomain.com"]
#    - HOW IT WORKS: Browser checks this list before allowing the request
#
# 🔹 **allow_methods**: Which HTTP methods are allowed
#    - WHAT IT DOES: ["*"] means all methods (GET, POST, PUT, DELETE, etc.) are allowed
#    - WHY YOU NEED IT: Some APIs only allow GET requests, others need POST for data submission
#    - REAL EXAMPLE: Read-only APIs might only allow ["GET"], full APIs allow ["GET", "POST", "PUT", "DELETE"]
#    - HOW IT WORKS: Browser checks if the request method (POST) is in the allowed list
#
# 🔹 **allow_headers**: Which headers browsers can send
#    - WHAT IT DOES: ["*"] means all headers (Authorization, Content-Type, etc.) are allowed
#    - WHY YOU NEED IT: Modern apps send authentication tokens and content type information
#    - REAL EXAMPLE: ["Authorization", "Content-Type"] for APIs that need login tokens
#    - HOW IT WORKS: Browser checks if headers like "Authorization: Bearer token123" are allowed

# ⚠️ **BUG FIX NEEDED:** You wrote "allow_method" but it should be "allow_methods" (plural)

# ============================================================================
# STEP 4: CREATE PYDANTIC MODELS - DATA VALIDATION
# ============================================================================
#
# **WHAT TO DO:** Create classes that define the structure of your API data
# **WHY YOU NEED IT:** Type safety, automatic validation, and API documentation
# **WHEN TO USE:** For every API endpoint that accepts or returns data
# **HOW IT WORKS:** Pydantic validates data and converts types automatically
#
# **DETAILED BREAKDOWN:**
#
# 🔹 **class GameQuery(BaseModel)**: Defines what data users send to request predictions
#    - WHAT IT DOES: Validates that users provide team1, team2, and optional date
#    - WHY YOU NEED IT: Prevents crashes from bad data like {"team1": 123} (number instead of string)
#    - REAL EXAMPLE: Uber's API has RideRequest(pickup_location, destination, ride_type)
#    - HOW IT WORKS: FastAPI automatically validates request body matches this model
#
# 🔹 **class PredictionResponse(BaseModel)**: Defines what your API returns
#    - WHAT IT DOES: Guarantees your API always returns consistent data structure
#    - WHY YOU NEED IT: Frontend developers know exactly what fields to expect
#    - REAL EXAMPLE: Twitter's API always returns Tweet(id, text, author, created_at)
#    - HOW IT WORKS: FastAPI automatically converts your return dict to this model
#
# **YOUR CODE HERE:**
# from datetime import datetime
# from typing import Optional, List
#
# class GameQuery(BaseModel):
#     team1: str  # Required field - must be a string
#     team2: str  # Required field - must be a string
#     date: Optional[str] = None  # Optional field - can be None
#
# class PredictionResponse(BaseModel):
#     predicted_winner: str
#     confidence: float  # 0.0 to 1.0
#     consensus_percentage: float
#     sources_analyzed: int
#     recommendation: str  # "bet", "avoid", "monitor"
#     explanation: str
from datetime import datetime
from typing import Optional, List

class GameQuery(BaseModel):
    team1: str
    team2: str
    date: Optional[str] = None
    sport: Optional[str] = None

class PredictionResponse(BaseModel):
    predicted_winner:str
    confidence: float
    consensus_percentage: float
    sources_analyzed: int
    recommendation: str
    explanation: str
# ============================================================================
# STEP 5: CREATE HEALTH CHECK ENDPOINT
# ============================================================================
#
# **WHAT TO DO:** Create a simple endpoint to check if your API is working
# **WHY YOU NEED IT:** Load balancers and monitoring systems need to check API health
# **WHEN TO USE:** Always in production APIs - it's industry standard
# **HOW IT WORKS:** Returns simple JSON response with status information
#
# **DETAILED BREAKDOWN:**
#
# 🔹 **@app.get("/health")**: HTTP GET request to /health URL
#    - WHAT IT DOES: When someone visits http://localhost:8000/health, this function runs
#    - WHY YOU NEED IT: Kubernetes, Docker, AWS load balancers all check /health endpoints
#    - REAL EXAMPLE: Netflix has thousands of microservices, each with a /health endpoint
#    - HOW IT WORKS: @app.get() is a decorator that registers this function as a route handler
#
# 🔹 **async def health_check()**: Asynchronous function definition
#    - WHAT IT DOES: Can handle multiple requests simultaneously without blocking
#    - WHY YOU NEED IT: If 1000 users check health at once, they don't have to wait in line
#    - REAL EXAMPLE: Instagram handles millions of requests per second using async functions
#    - HOW IT WORKS: Python's asyncio allows one thread to handle many requests
#
# 🔹 **return {"status": "healthy"}**: JSON response
#    - WHAT IT DOES: FastAPI automatically converts Python dict to JSON response
#    - WHY YOU NEED IT: Monitoring systems expect specific response format
#    - REAL EXAMPLE: AWS Application Load Balancer expects {"status": "healthy"} response
#    - HOW IT WORKS: FastAPI adds Content-Type: application/json header automatically
#
# **YOUR CODE HERE:**
# from datetime import datetime
#
# @app.get("/health")
# async def health_check():
#     """Health check endpoint for load balancers and monitoring"""
#     return {
#         "status": "healthy",
#         "service": "sports-betting-api",
#         "timestamp": datetime.utcnow().isoformat(),
#         "version": "1.0.0"
#     }

@app.get("/health")
async def health_check():
    return{
        "status": "healthy",
        "service": "sports-betting-api",
        "timestamp": datetime.utcnow().isoformat(),
        "version": "1.0.0"    }
# ============================================================================
# STEP 6: CREATE MAIN PREDICTION ENDPOINT
# ============================================================================
#
# **WHAT TO DO:** Create the main endpoint that provides betting predictions
# **WHY YOU NEED IT:** This is your core business logic - the whole point of your API
# **WHEN TO USE:** This is what users will call to get predictions
# **HOW IT WORKS:** Orchestrates scraping, AI analysis, and returns consensus
#
# **DETAILED BREAKDOWN:**
#
# 🔹 **@app.post("/api/v1/predictions/consensus")**: HTTP POST endpoint
#    - WHAT IT DOES: Accepts POST requests with game data, returns predictions
#    - WHY POST: POST requests can include request body data (team1, team2, date)
#    - REAL EXAMPLE: OpenAI's API uses POST /v1/chat/completions for AI requests
#    - HOW IT WORKS: Users send JSON data in request body, get JSON response back
#
# 🔹 **query: GameQuery**: Pydantic model parameter
#    - WHAT IT DOES: FastAPI automatically validates request body matches GameQuery model
#    - WHY YOU NEED IT: Prevents crashes from malformed requests
#    - REAL EXAMPLE: If user sends {"team1": 123}, FastAPI returns 422 validation error
#    - HOW IT WORKS: Pydantic deserializes JSON to Python object with type checking
#
# 🔹 **background_tasks: BackgroundTasks**: Dependency injection
#    - WHAT IT DOES: Allows you to run slow tasks after returning response to user
#    - WHY YOU NEED IT: Web scraping takes 10-30 seconds, users shouldn't wait
#    - REAL EXAMPLE: When you upload to Instagram, response is instant but image processing happens later
#    - HOW IT WORKS: background_tasks.add_task(function_name, param1, param2)
#
# **YOUR CODE HERE:**
from app.services.prediction_service import PredictionService
# from app.services.prediction_service import PredictionService

@app.post("/api/v1/predictions/consensus", response model = PredictionResponse)
async def get_consensus_prediction(
    query: GameQuery,
    background_tasks: BackgroundTasks
):

    try:
        prediction_service = PredictionService()
        result = await prediction_service.get_consensus(
            f"{query.team1} vs {query.team2}",
            query.date
        )
        return result
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Prediction failed: {str(e)}")
# @app.post("/api/v1/predictions/consensus", response_model=PredictionResponse)
# async def get_consensus_prediction(
#     query: GameQuery,
#     background_tasks: BackgroundTasks
# ):
#     """
#     Get AI-powered consensus prediction for a sports game
#
#     This endpoint:
#     1. Scrapes multiple betting sites for predictions
#     2. Uses AI to analyze and extract structured data
#     3. Calculates consensus recommendation
#     4. Returns actionable betting advice
#     """
#     try:
#         prediction_service = PredictionService()
#         result = await prediction_service.get_consensus(
#             f"{query.team1} vs {query.team2}",
#             query.date
#         )
#         return result
#     except Exception as e:
#         raise HTTPException(status_code=500, detail=f"Prediction failed: {str(e)}")

# ============================================================================
# 🎯 WHAT TO DO NEXT - COMPLETE IMPLEMENTATION GUIDE
# ============================================================================
#
# **CONGRATULATIONS!** You've learned the fundamentals. Now complete the implementation:
#
# 🔹 **STEP 1: Finish this file (main.py)**
#    - Implement the remaining Pydantic models (GameQuery, PredictionResponse)
#    - Add the health check endpoint (@app.get("/health"))
#    - Add the main prediction endpoint (@app.post("/api/v1/predictions/consensus"))
#    - Test with: uvicorn app.main:app --reload --port 8000
#    - Visit: http://localhost:8000/docs for API documentation
#
# 🔹 **STEP 2: Move to scraper_service.py**
#    - Location: sports-betting-consensus/backend-python/app/services/scraper_service.py
#    - What you'll build: Web scraping service that gets betting predictions from multiple sites
#    - Key concepts: asyncio, aiohttp, BeautifulSoup, rate limiting, anti-bot measures
#    - Real-world example: How Google scrapes millions of websites concurrently
#
# 🔹 **STEP 3: Move to ai_analysis_service.py**
#    - Location: sports-betting-consensus/backend-python/app/services/ai_analysis_service.py
#    - What you'll build: AI service that analyzes scraped text and extracts structured predictions
#    - Key concepts: OpenAI API, Anthropic Claude, prompt engineering, data validation
#    - Real-world example: How ChatGPT processes and structures unstructured text
#
# 🔹 **STEP 4: Move to React frontend**
#    - Location: sports-betting-consensus/frontend/src/components/PredictionDashboard.tsx
#    - What you'll build: React dashboard that displays betting predictions and analytics
#    - Key concepts: React hooks, state management, API integration, real-time updates
#    - Real-world example: How Netflix builds their streaming interface
#
# 🔹 **STEP 5: Move to Java Spring Boot**
#    - Location: sports-betting-consensus/backend-java/pom.xml
#    - What you'll build: Enterprise API gateway that orchestrates microservices
#    - Key concepts: Spring Boot, Maven, REST APIs, microservice communication
#    - Real-world example: How Uber coordinates their ride-sharing microservices
#
# 🔹 **STEP 6: Move to MCP Server**
#    - Location: sports-betting-consensus/mcp-server/src/index.ts
#    - What you'll build: AI agent integration server using Model Context Protocol
#    - Key concepts: TypeScript, Express.js, AI tool integration, protocol implementation
#    - Real-world example: How AI assistants access external tools and services

# ============================================================================
# 📚 WANT TO MASTER FASTAPI FIRST?
# ============================================================================
#
# **🎯 COMPREHENSIVE FASTAPI LEARNING MODULE AVAILABLE!**
#
# **Location:** `/home/iscjmz/onepiece/learning-modules/37-fastapi-mastery/`
#
# **What you'll get:**
# - ✅ **Complete FastAPI mastery guide** (README.md)
# - ✅ **Hands-on coding lab** (01-fastapi-mastery-coding-lab.py)
# - ✅ **Real-world examples** from Netflix, Uber, Microsoft
# - ✅ **Production patterns** and best practices
# - ✅ **Career guidance** and salary expectations
#
# **To start the FastAPI mastery module:**
# ```bash
# cd /home/iscjmz/onepiece/learning-modules/37-fastapi-mastery
# python 01-fastapi-mastery-coding-lab.py
# # Visit http://localhost:8000/docs
# ```
#
# **This module covers:**
# - FastAPI vs Flask vs Django comparison
# - Async/await and high-performance APIs
# - Pydantic models and validation
# - Database integration with SQLAlchemy
# - Authentication and security (JWT, OAuth2)
# - Background tasks and WebSocket support
# - Testing, documentation, and deployment
# - Microservices and production patterns

# ============================================================================
# 🧪 TEST YOUR CURRENT CODE:
# ============================================================================
#
# **Run your FastAPI app:**
# ```bash
# cd /home/iscjmz/onepiece/sports-betting-consensus/backend-python
# uvicorn app.main:app --reload --host 0.0.0.0 --port 8000
# ```
#
# **Visit these URLs:**
# - http://localhost:8000/ (root endpoint)
# - http://localhost:8000/docs (interactive API documentation)
# - http://localhost:8000/redoc (alternative documentation)
# - http://localhost:8000/health (health check - implement this!)
#
# **Fix the bug in your CORS middleware:**
# Change `allow_method` to `allow_methods` (plural) in your middleware configuration

# YOUR IMPLEMENTATION HERE:
# (Write your FastAPI application below)

# ============================================================================
# 📝 REFERENCE IMPLEMENTATION (Check your code against this)
# ============================================================================

# from contextlib import asynccontextmanager
# from fastapi import FastAPI, HTTPException, Depends, BackgroundTasks
# from fastapi.middleware.cors import CORSMiddleware
# from fastapi.middleware.trustedhost import TrustedHostMiddleware
# from fastapi.responses import JSONResponse
# import uvicorn
# import logging
# from typing import List, Optional
# import asyncio
# from datetime import datetime, timedelta
#
# # Internal imports
# from app.core.config import settings
# from app.core.logging import setup_logging
# from app.api.v1.api import api_router
# from app.core.database import engine, Base
# from app.services.scraper_service import ScraperService
# from app.services.prediction_service import PredictionService
# from app.models.prediction import Prediction, Game, Source
setup_logging()
logger = logging.getLogger(__name__)

@asynccontextmanager
async def lifespan( app: FastAPI):
    logger.info("Application Starting")
    Base.metadata.create_all(bind = engine)
    logger.info("Database tables created")

    app.state.scraper_service = ScraperService()
    app.state.prediction_service = PredictionService()
    logger.info("Service initialized")
    yield
    logger.info("Application Shutting Down")
# # Setup logging
# setup_logging()
# logger = logging.getLogger(__name__)
#
# # Create database tables
# @asynccontextmanager
# async def lifespan(app: FastAPI):
#     """Application lifespan events"""
#     # Startup
#     logger.info("🚀 Starting Sports Betting Consensus Aggregator")
#
#     # Create database tables
#     Base.metadata.create_all(bind=engine)
#     logger.info("📊 Database tables created")
#
#     # Initialize services
#     app.state.scraper_service = ScraperService()
#     app.state.prediction_service = PredictionService()
#     logger.info("🔧 Services initialized")
#
#     yield
#
#     # Shutdown
#     logger.info("🛑 Shutting down Sports Betting Consensus Aggregator")


# # Create FastAPI application
# app = FastAPI(
#     title="Sports Betting Consensus Aggregator",
#     description="""
#     🎯 **AI-Powered Sports Betting Consensus Aggregator**
#
#     This API aggregates sports betting predictions from multiple websites,
#     uses AI to analyze consensus, and provides data-driven betting recommendations.
#
#     ## Features
#
#     * **Real-time Web Scraping** - Automated scraping of 5+ sports betting sites
#     * **AI-Powered Analysis** - LLM extraction of predictions from unstructured text
#     * **Consensus Algorithm** - Weighted scoring based on source reliability
#     * **Background Processing** - Celery-based scheduled scraping jobs
#     * **Performance Tracking** - Historical accuracy metrics and analytics
#
#     ## Endpoints
#
#     * **Predictions** - Get consensus predictions for games
#     * **Scraping** - Trigger manual scraping of betting sites
#     * **Analytics** - Historical performance and accuracy metrics
#     * **Health** - Service health checks and monitoring
#     """,
#     version="1.0.0",
#     docs_url="/docs",
#     redoc_url="/redoc",
#     lifespan=lifespan
# )
#
# # Add middleware
# app.add_middleware(
#     CORSMiddleware,
#     allow_origins=settings.ALLOWED_HOSTS,
#     allow_credentials=True,
#     allow_methods=["*"],
#     allow_headers=["*"],
# )
#
# app.add_middleware(
#     TrustedHostMiddleware,
#     allowed_hosts=settings.ALLOWED_HOSTS
# )

# # Include API routes
# app.include_router(api_router, prefix="/api/v1")
#
# # Root endpoint
# @app.get("/", tags=["Root"])
# async def root():
#     """Root endpoint with API information"""
#     return {
#         "message": "🎯 Sports Betting Consensus Aggregator API",
#         "version": "1.0.0",
#         "docs": "/docs",
#         "health": "/health",
#         "status": "operational",
#         "timestamp": datetime.utcnow().isoformat()
#     }
#
# # Health check endpoint
# @app.get("/health", tags=["Health"])
# async def health_check():
#     """Health check endpoint for monitoring"""
#     try:
#         # Check database connection
#         from app.core.database import SessionLocal
#         db = SessionLocal()
#         db.execute("SELECT 1")
#         db.close()
#         db_status = "healthy"
#     except Exception as e:
#         logger.error(f"Database health check failed: {e}")
#         db_status = "unhealthy"
#
#     # Check Redis connection
#     try:
#         from app.core.redis import redis_client
#         await redis_client.ping()
#         redis_status = "healthy"
#     except Exception as e:
#         logger.error(f"Redis health check failed: {e}")
#         redis_status = "unhealthy"
#
#     # Overall health status
#     overall_status = "healthy" if db_status == "healthy" and redis_status == "healthy" else "unhealthy"
#
#     health_data = {
#         "status": overall_status,
#         "timestamp": datetime.utcnow().isoformat(),
#         "services": {
#             "database": db_status,
#             "redis": redis_status,
#             "api": "healthy"
#         },
#         "version": "1.0.0"
#     }
#
#     if overall_status == "unhealthy":
#         return JSONResponse(status_code=503, content=health_data)
#
#     return health_data

# # Quick prediction endpoint for testing
# @app.get("/quick-prediction", tags=["Quick Test"])
# async def quick_prediction(
#     team1: str = "Lakers",
#     team2: str = "Warriors",
#     date: Optional[str] = None,
#     background_tasks: BackgroundTasks = BackgroundTasks()
# ):
#     """
#     Quick prediction endpoint for testing the scraping and AI analysis.
#
#     This endpoint demonstrates the core functionality:
#     1. Scrapes betting sites for the specified game
#     2. Uses AI to analyze predictions
#     3. Returns consensus recommendation
#     """
#     try:
#         # Parse date or use tomorrow
#         if date:
#             game_date = datetime.fromisoformat(date)
#         else:
#             game_date = datetime.now() + timedelta(days=1)
#
#         # Get services from app state
#         scraper_service = app.state.scraper_service
#         prediction_service = app.state.prediction_service
#
#         logger.info(f"🎯 Quick prediction requested: {team1} vs {team2} on {game_date.date()}")
#
#         # Create game object
#         game_query = f"{team1} vs {team2}"
#
#         # Trigger background scraping
#         background_tasks.add_task(
#             scraper_service.scrape_all_sources,
#             game_query,
#             game_date
#         )
#
#         # For demo purposes, return a mock consensus
#         # In production, this would wait for scraping to complete
#         mock_consensus = {
#             "game": {
#                 "team1": team1,
#                 "team2": team2,
#                 "date": game_date.isoformat(),
#                 "sport": "NBA"
#             },
#             "consensus": {
#                 "predicted_winner": team1,
#                 "confidence": 0.75,
#                 "consensus_percentage": 75.0,
#                 "total_sources": 5,
#                 "sources_agreeing": 4
#             },
#             "predictions": [
#                 {
#                     "source": "ESPN",
#                     "prediction": team1,
#                     "confidence": 0.8,
#                     "reasoning": "Strong home court advantage and recent winning streak"
#                 },
#                 {
#                     "source": "CBS Sports",
#                     "prediction": team1,
#                     "confidence": 0.7,
#                     "reasoning": "Better offensive rating and key player matchups"
#                 },
#                 {
#                     "source": "The Athletic",
#                     "prediction": team2,
#                     "confidence": 0.6,
#                     "reasoning": "Road team has been playing well recently"
#                 },
#                 {
#                     "source": "Bleacher Report",
#                     "prediction": team1,
#                     "confidence": 0.75,
#                     "reasoning": "Statistical analysis favors home team"
#                 },
#                 {
#                     "source": "Sports Illustrated",
#                     "prediction": team1,
#                     "confidence": 0.8,
#                     "reasoning": "Expert analysis and injury reports favor home team"
#                 }
#             ],
#             "recommendation": {
#                 "action": "bet",
#                 "team": team1,
#                 "confidence": "high",
#                 "risk_level": "moderate",
#                 "explanation": f"Strong consensus (75%) favors {team1}. 4 out of 5 sources predict {team1} to win with solid reasoning based on recent performance and matchup analysis."
#             },
#             "metadata": {
#                 "scraped_at": datetime.utcnow().isoformat(),
#                 "processing_time_ms": 1250,
#                 "ai_analysis_used": True,
#                 "background_scraping": True
#             }
#         }
#
#         logger.info(f"✅ Quick prediction generated for {team1} vs {team2}")
#         return mock_consensus
#
#     except Exception as e:
#         logger.error(f"❌ Quick prediction failed: {e}")
#         raise HTTPException(
#             status_code=500,
#             detail=f"Failed to generate prediction: {str(e)}"
#         )
#
# # Global exception handler
# @app.exception_handler(Exception)
# async def global_exception_handler(request, exc):
#     """Global exception handler for unhandled errors"""
#     logger.error(f"Unhandled exception: {exc}", exc_info=True)
#     return JSONResponse(
#         status_code=500,
#         content={
#             "error": "Internal server error",
#             "message": "An unexpected error occurred",
#             "timestamp": datetime.utcnow().isoformat()
#         }
#     )
#
# # Run the application
# if __name__ == "__main__":
#     uvicorn.run(
#         "app.main:app",
#         host="0.0.0.0",
#         port=8000,
#         reload=True,
#         log_level="info"
#     )
