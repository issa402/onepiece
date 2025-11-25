"""
🏆 FANZONE CONNECT - API GATEWAY
Learning Modules: 16 (Node.js Backend), 34 (TypeScript/Node.js), 25 (Bun/Fastify Performance)
World Cup 2026 Fan Platform - High-Performance API Gateway with Load Balancing
"""

import asyncio
import logging
import time
from datetime import datetime
from typing import Dict, List, Optional, Any
import json
import httpx
import redis.asyncio as redis

from fastapi import FastAPI, HTTPException, Request, Response, Depends, status
from fastapi.middleware.cors import CORSMiddleware
from fastapi.middleware.trustedhost import TrustedHostMiddleware
from fastapi.responses import JSONResponse
from contextlib import asynccontextmanager
import uvicorn

# Configure logging for production
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger(__name__)

# =====================================================
# MODULE 25: BUN/FASTAPI PERFORMANCE OPTIMIZATION
# =====================================================

class PerformanceConfig:
    """High-performance configuration for World Cup traffic"""
    
    # Connection pooling
    MAX_CONNECTIONS = 100
    MAX_KEEPALIVE_CONNECTIONS = 20
    KEEPALIVE_EXPIRY = 5
    
    # Timeouts
    REQUEST_TIMEOUT = 30.0
    CONNECT_TIMEOUT = 5.0
    
    # Rate limiting
    RATE_LIMIT_REQUESTS = 1000
    RATE_LIMIT_WINDOW = 60
    
    # Circuit breaker
    FAILURE_THRESHOLD = 5
    RECOVERY_TIMEOUT = 30
    
    # Cache settings
    CACHE_TTL = 300  # 5 minutes
    CACHE_MAX_SIZE = 10000

class ServiceRegistry:
    """Service discovery and load balancing for World Cup microservices"""
    
    def __init__(self):
        self.services = {
            "user-service": [
                "http://user-service-1:8001",
                "http://user-service-2:8001",
                "http://user-service-3:8001"
            ],
            "match-service": [
                "http://match-service-1:8003",
                "http://match-service-2:8003"
            ],
            "event-service": [
                "http://event-service-1:8002",
                "http://event-service-2:8002"
            ],
            "notification-service": [
                "http://notification-service-1:8004"
            ],
            "analytics-service": [
                "http://analytics-service-1:8005"
            ]
        }
        
        # Round-robin counters
        self.counters = {service: 0 for service in self.services}
        
        # Health status tracking
        self.health_status = {}
        for service, endpoints in self.services.items():
            self.health_status[service] = {endpoint: True for endpoint in endpoints}
    
    def get_service_url(self, service_name: str) -> Optional[str]:
        """Get next available service URL using round-robin load balancing"""
        if service_name not in self.services:
            return None
        
        endpoints = self.services[service_name]
        healthy_endpoints = [
            endpoint for endpoint in endpoints 
            if self.health_status[service_name].get(endpoint, True)
        ]
        
        if not healthy_endpoints:
            logger.error(f"❌ No healthy endpoints for service: {service_name}")
            return None
        
        # Round-robin selection
        counter = self.counters[service_name]
        selected_endpoint = healthy_endpoints[counter % len(healthy_endpoints)]
        self.counters[service_name] = (counter + 1) % len(healthy_endpoints)
        
        return selected_endpoint
    
    def mark_unhealthy(self, service_name: str, endpoint: str):
        """Mark service endpoint as unhealthy"""
        if service_name in self.health_status:
            self.health_status[service_name][endpoint] = False
            logger.warning(f"⚠️ Marked unhealthy: {service_name} - {endpoint}")
    
    def mark_healthy(self, service_name: str, endpoint: str):
        """Mark service endpoint as healthy"""
        if service_name in self.health_status:
            self.health_status[service_name][endpoint] = True
            logger.info(f"✅ Marked healthy: {service_name} - {endpoint}")

class CircuitBreaker:
    """Circuit breaker pattern for service resilience"""
    
    def __init__(self, failure_threshold: int = 5, recovery_timeout: int = 30):
        self.failure_threshold = failure_threshold
        self.recovery_timeout = recovery_timeout
        self.failure_count = 0
        self.last_failure_time = None
        self.state = "CLOSED"  # CLOSED, OPEN, HALF_OPEN
    
    def can_execute(self) -> bool:
        """Check if request can be executed"""
        if self.state == "CLOSED":
            return True
        
        if self.state == "OPEN":
            if time.time() - self.last_failure_time > self.recovery_timeout:
                self.state = "HALF_OPEN"
                return True
            return False
        
        # HALF_OPEN state
        return True
    
    def record_success(self):
        """Record successful request"""
        self.failure_count = 0
        self.state = "CLOSED"
    
    def record_failure(self):
        """Record failed request"""
        self.failure_count += 1
        self.last_failure_time = time.time()
        
        if self.failure_count >= self.failure_threshold:
            self.state = "OPEN"
            logger.warning(f"🔴 Circuit breaker OPEN - {self.failure_count} failures")

# =====================================================
# MODULE 16 & 34: NODE.JS BACKEND EQUIVALENT IN PYTHON
# =====================================================

class HTTPClient:
    """High-performance HTTP client for microservice communication"""
    
    def __init__(self):
        self.client = httpx.AsyncClient(
            limits=httpx.Limits(
                max_connections=PerformanceConfig.MAX_CONNECTIONS,
                max_keepalive_connections=PerformanceConfig.MAX_KEEPALIVE_CONNECTIONS,
                keepalive_expiry=PerformanceConfig.KEEPALIVE_EXPIRY
            ),
            timeout=httpx.Timeout(
                connect=PerformanceConfig.CONNECT_TIMEOUT,
                read=PerformanceConfig.REQUEST_TIMEOUT
            )
        )
        
        # Circuit breakers for each service
        self.circuit_breakers = {
            "user-service": CircuitBreaker(),
            "match-service": CircuitBreaker(),
            "event-service": CircuitBreaker(),
            "notification-service": CircuitBreaker(),
            "analytics-service": CircuitBreaker()
        }
    
    async def make_request(
        self, 
        service_name: str, 
        method: str, 
        path: str, 
        **kwargs
    ) -> Optional[httpx.Response]:
        """Make request to microservice with circuit breaker protection"""
        
        circuit_breaker = self.circuit_breakers.get(service_name)
        if circuit_breaker and not circuit_breaker.can_execute():
            logger.error(f"🔴 Circuit breaker OPEN for {service_name}")
            return None
        
        service_url = service_registry.get_service_url(service_name)
        if not service_url:
            return None
        
        url = f"{service_url}{path}"
        
        try:
            response = await self.client.request(method, url, **kwargs)
            
            # Record success
            if circuit_breaker:
                circuit_breaker.record_success()
            
            service_registry.mark_healthy(service_name, service_url)
            return response
            
        except Exception as e:
            logger.error(f"❌ Request failed to {service_name}: {e}")
            
            # Record failure
            if circuit_breaker:
                circuit_breaker.record_failure()
            
            service_registry.mark_unhealthy(service_name, service_url)
            return None
    
    async def close(self):
        """Close HTTP client"""
        await self.client.aclose()

# Global instances
service_registry = ServiceRegistry()
http_client = HTTPClient()
redis_client = None

# =====================================================
# RATE LIMITING AND CACHING
# =====================================================

async def get_redis():
    """Get Redis client for caching and rate limiting"""
    global redis_client
    if redis_client is None:
        redis_client = redis.from_url("redis://redis:6379", decode_responses=True)
    return redis_client

async def check_rate_limit(request: Request) -> bool:
    """Check rate limit for World Cup API"""
    client_ip = request.client.host
    redis_conn = await get_redis()
    
    key = f"rate_limit:{client_ip}"
    current_requests = await redis_conn.get(key)
    
    if current_requests is None:
        await redis_conn.setex(key, PerformanceConfig.RATE_LIMIT_WINDOW, 1)
        return True
    
    if int(current_requests) >= PerformanceConfig.RATE_LIMIT_REQUESTS:
        return False
    
    await redis_conn.incr(key)
    return True

async def get_cached_response(cache_key: str) -> Optional[Dict[str, Any]]:
    """Get cached response"""
    redis_conn = await get_redis()
    cached_data = await redis_conn.get(cache_key)
    
    if cached_data:
        return json.loads(cached_data)
    return None

async def cache_response(cache_key: str, data: Dict[str, Any], ttl: int = None):
    """Cache response data"""
    redis_conn = await get_redis()
    ttl = ttl or PerformanceConfig.CACHE_TTL
    
    await redis_conn.setex(cache_key, ttl, json.dumps(data, default=str))

# =====================================================
# FASTAPI APPLICATION
# =====================================================

@asynccontextmanager
async def lifespan(app: FastAPI):
    """Application lifespan management"""
    logger.info("🏆 FANZONE CONNECT API Gateway Starting...")
    logger.info("🌍 World Cup 2026 Fan Platform - High Performance Gateway")
    
    # Initialize Redis
    await get_redis()
    
    # Health check background task
    asyncio.create_task(health_check_background())
    
    logger.info("✅ API Gateway Ready for World Cup 2026!")
    yield
    
    # Cleanup
    await http_client.close()
    if redis_client:
        await redis_client.close()
    logger.info("🏁 API Gateway Shutdown Complete")

app = FastAPI(
    title="🏆 FANZONE CONNECT - API Gateway",
    description="World Cup 2026 Fan Platform - High Performance API Gateway",
    version="1.0.0",
    lifespan=lifespan
)

# Middleware
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
# MIDDLEWARE FOR PERFORMANCE MONITORING
# =====================================================

@app.middleware("http")
async def performance_middleware(request: Request, call_next):
    """Performance monitoring middleware"""
    start_time = time.time()
    
    # Rate limiting
    if not await check_rate_limit(request):
        return JSONResponse(
            status_code=status.HTTP_429_TOO_MANY_REQUESTS,
            content={"error": "Rate limit exceeded"}
        )
    
    response = await call_next(request)
    
    # Add performance headers
    process_time = time.time() - start_time
    response.headers["X-Process-Time"] = str(process_time)
    response.headers["X-Gateway-Version"] = "1.0.0"
    
    # Log slow requests
    if process_time > 1.0:
        logger.warning(f"⚠️ Slow request: {request.url} took {process_time:.2f}s")
    
    return response

# =====================================================
# HEALTH CHECK SYSTEM
# =====================================================

async def health_check_background():
    """Background task for service health checks"""
    while True:
        try:
            for service_name, endpoints in service_registry.services.items():
                for endpoint in endpoints:
                    try:
                        response = await http_client.client.get(
                            f"{endpoint}/health",
                            timeout=5.0
                        )
                        if response.status_code == 200:
                            service_registry.mark_healthy(service_name, endpoint)
                        else:
                            service_registry.mark_unhealthy(service_name, endpoint)
                    except Exception:
                        service_registry.mark_unhealthy(service_name, endpoint)
            
            await asyncio.sleep(30)  # Check every 30 seconds
            
        except Exception as e:
            logger.error(f"❌ Health check error: {e}")
            await asyncio.sleep(60)

@app.get("/health")
async def gateway_health():
    """API Gateway health check"""
    return {
        "status": "healthy",
        "service": "api-gateway",
        "timestamp": datetime.utcnow().isoformat(),
        "version": "1.0.0",
        "services": service_registry.health_status
    }

# =====================================================
# PROXY ENDPOINTS FOR WORLD CUP SERVICES
# =====================================================

@app.api_route("/api/users/{path:path}", methods=["GET", "POST", "PUT", "DELETE", "PATCH"])
async def proxy_user_service(request: Request, path: str):
    """Proxy requests to User Service"""
    cache_key = f"user_service:{request.method}:{path}:{request.url.query}"
    
    # Check cache for GET requests
    if request.method == "GET":
        cached_response = await get_cached_response(cache_key)
        if cached_response:
            return JSONResponse(content=cached_response)
    
    # Forward request
    body = await request.body() if request.method in ["POST", "PUT", "PATCH"] else None
    
    response = await http_client.make_request(
        "user-service",
        request.method,
        f"/{path}",
        params=dict(request.query_params),
        content=body,
        headers=dict(request.headers)
    )
    
    if response is None:
        raise HTTPException(status_code=503, detail="User service unavailable")
    
    response_data = response.json() if response.content else {}
    
    # Cache successful GET responses
    if request.method == "GET" and response.status_code == 200:
        await cache_response(cache_key, response_data)
    
    return JSONResponse(content=response_data, status_code=response.status_code)

@app.api_route("/api/matches/{path:path}", methods=["GET", "POST", "PUT", "DELETE", "PATCH"])
async def proxy_match_service(request: Request, path: str):
    """Proxy requests to Match Service"""
    cache_key = f"match_service:{request.method}:{path}:{request.url.query}"
    
    # Check cache for GET requests
    if request.method == "GET":
        cached_response = await get_cached_response(cache_key)
        if cached_response:
            return JSONResponse(content=cached_response)
    
    body = await request.body() if request.method in ["POST", "PUT", "PATCH"] else None
    
    response = await http_client.make_request(
        "match-service",
        request.method,
        f"/{path}",
        params=dict(request.query_params),
        content=body,
        headers=dict(request.headers)
    )
    
    if response is None:
        raise HTTPException(status_code=503, detail="Match service unavailable")
    
    response_data = response.json() if response.content else {}
    
    # Cache match data with shorter TTL for live matches
    if request.method == "GET" and response.status_code == 200:
        ttl = 60 if "live" in path else 300  # 1 min for live, 5 min for others
        await cache_response(cache_key, response_data, ttl)
    
    return JSONResponse(content=response_data, status_code=response.status_code)

@app.api_route("/api/events/{path:path}", methods=["GET", "POST", "PUT", "DELETE", "PATCH"])
async def proxy_event_service(request: Request, path: str):
    """Proxy requests to Event Service"""
    body = await request.body() if request.method in ["POST", "PUT", "PATCH"] else None
    
    response = await http_client.make_request(
        "event-service",
        request.method,
        f"/{path}",
        params=dict(request.query_params),
        content=body,
        headers=dict(request.headers)
    )
    
    if response is None:
        raise HTTPException(status_code=503, detail="Event service unavailable")
    
    response_data = response.json() if response.content else {}
    return JSONResponse(content=response_data, status_code=response.status_code)

# =====================================================
# ANALYTICS AND MONITORING ENDPOINTS
# =====================================================

@app.get("/api/gateway/stats")
async def gateway_stats():
    """Get API Gateway statistics"""
    return {
        "services": service_registry.health_status,
        "circuit_breakers": {
            service: {
                "state": cb.state,
                "failure_count": cb.failure_count
            }
            for service, cb in http_client.circuit_breakers.items()
        },
        "timestamp": datetime.utcnow().isoformat()
    }

if __name__ == "__main__":
    uvicorn.run(
        "main:app",
        host="0.0.0.0",
        port=8000,
        reload=False,  # Disable in production
        workers=4,     # Multiple workers for high performance
        log_level="info"
    )
