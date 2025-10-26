# ============================================================================
# 📚 LEARNING GUIDE: Redis Configuration (app/core/redis.py)
# ============================================================================
#
# 🎯 PURPOSE:
# This module sets up Redis connection and caching functionality.
# Redis is used for caching predictions, session storage, and
# background job queuing with Celery.
#
# 🔧 TECHNOLOGIES USED:
# - Redis: In-memory data structure store
# - aioredis: Async Redis client for Python
# - Connection pooling: Efficient connection management
# - Serialization: JSON encoding/decoding for complex data
#
# 📖 IN-DEPTH EXPLANATION:
#
# **Why Redis for Caching:**
# - In-memory storage for fast access
# - Built-in data expiration (TTL)
# - Pub/sub capabilities for real-time features
# - Atomic operations for consistency
# - Excellent Python integration
#
# 💡 HINTS:
# - Use connection pooling for performance
# - Set appropriate TTL for cached data
# - Handle Redis connection failures gracefully
# - Use JSON serialization for complex objects
# - Monitor Redis memory usage
#
# 🧪 TEST YOUR CODE:
# from app.core.redis import redis_client
# await redis_client.set("test", "value")
# value = await redis_client.get("test")

# YOUR IMPLEMENTATION HERE:
# (Write your Redis configuration below)

# ============================================================================
# 📝 REFERENCE IMPLEMENTATION (Check your code against this)
# ============================================================================

import json
import logging
from typing import Any, Optional
import redis.asyncio as redis
from app.core.config import settings

logger = logging.getLogger(__name__)

# Create Redis connection pool
redis_client = redis.from_url(
    settings.REDIS_URL,
    encoding="utf-8",
    decode_responses=True,
    max_connections=20
)

async def cache_set(key: str, value: Any, ttl: int = None) -> bool:
    """
    Set a value in Redis cache with optional TTL
    
    Args:
        key: Cache key
        value: Value to cache (will be JSON serialized)
        ttl: Time to live in seconds (default from settings)
        
    Returns:
        bool: True if successful
    """
    try:
        if ttl is None:
            ttl = settings.REDIS_CACHE_TTL
        
        serialized_value = json.dumps(value) if not isinstance(value, str) else value
        await redis_client.setex(key, ttl, serialized_value)
        logger.debug(f"✅ Cached key: {key} (TTL: {ttl}s)")
        return True
        
    except Exception as e:
        logger.error(f"❌ Cache set failed for key {key}: {e}")
        return False

async def cache_get(key: str) -> Optional[Any]:
    """
    Get a value from Redis cache
    
    Args:
        key: Cache key
        
    Returns:
        Cached value or None if not found
    """
    try:
        value = await redis_client.get(key)
        if value is None:
            return None
        
        # Try to deserialize JSON, fallback to string
        try:
            return json.loads(value)
        except json.JSONDecodeError:
            return value
            
    except Exception as e:
        logger.error(f"❌ Cache get failed for key {key}: {e}")
        return None

async def cache_delete(key: str) -> bool:
    """Delete a key from Redis cache"""
    try:
        result = await redis_client.delete(key)
        logger.debug(f"🗑️ Deleted cache key: {key}")
        return bool(result)
        
    except Exception as e:
        logger.error(f"❌ Cache delete failed for key {key}: {e}")
        return False

async def cache_exists(key: str) -> bool:
    """Check if a key exists in Redis cache"""
    try:
        result = await redis_client.exists(key)
        return bool(result)
        
    except Exception as e:
        logger.error(f"❌ Cache exists check failed for key {key}: {e}")
        return False

# ============================================================================
