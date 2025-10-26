# ============================================================================
# 📚 LEARNING GUIDE: API Router Configuration (app/api/v1/api.py)
# ============================================================================
#
# 🎯 PURPOSE:
# This module sets up the main API router that organizes all endpoints.
# It groups related endpoints together and provides a clean structure
# for the FastAPI application.
#
# 🔧 TECHNOLOGIES USED:
# - FastAPI APIRouter: Modular route organization
# - Route prefixes: Clean URL structure
# - Tags: API documentation grouping
# - Dependencies: Shared functionality across routes
#
# 📖 IN-DEPTH EXPLANATION:
#
# **API Router Benefits:**
# - Modular organization of endpoints
# - Shared dependencies and middleware
# - Clean URL structure with prefixes
# - Better API documentation organization
# - Easier testing and maintenance
#
# 💡 HINTS:
# - Use descriptive tags for API documentation
# - Group related endpoints in separate routers
# - Use dependencies for common functionality
# - Include proper response models
# - Add comprehensive docstrings
#
# 🧪 TEST YOUR CODE:
# from app.api.v1.api import api_router
# print(api_router.routes)

# YOUR IMPLEMENTATION HERE:
# (Write your API router configuration below)

# ============================================================================
# 📝 REFERENCE IMPLEMENTATION (Check your code against this)
# ============================================================================

from fastapi import APIRouter
from app.api.v1 import predictions

# Create main API router
api_router = APIRouter()

# Include prediction endpoints
api_router.include_router(
    predictions.router,
    prefix="/predictions",
    tags=["predictions"]
)

# Health check endpoint
@api_router.get("/health", tags=["health"])
async def api_health():
    """API health check endpoint"""
    return {
        "status": "healthy",
        "service": "sports-betting-api",
        "version": "1.0.0"
    }

# ============================================================================
