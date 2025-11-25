"""
🏆 FANZONE CONNECT - DISTRIBUTED SYSTEM ARCHITECTURE
Learning Modules: 40 (System Design Fundamentals), 45 (Complete System Design)
World Cup 2026 Fan Platform - Scalable Distributed Architecture for 5M+ Users
"""

import asyncio
import logging
from datetime import datetime, timezone
from typing import Dict, List, Optional, Any, Union
from dataclasses import dataclass, field
from enum import Enum
import json
import hashlib
import random
import time

import aiohttp
import asyncpg
import redis.asyncio as redis
from pydantic import BaseModel

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# =====================================================
# MODULE 40: SYSTEM DESIGN FUNDAMENTALS - CORE PATTERNS
# =====================================================

class ServiceStatus(str, Enum):
    HEALTHY = "healthy"
    DEGRADED = "degraded"
    UNHEALTHY = "unhealthy"
    MAINTENANCE = "maintenance"

class LoadBalancingStrategy(str, Enum):
    ROUND_ROBIN = "round_robin"
    WEIGHTED_ROUND_ROBIN = "weighted_round_robin"
    LEAST_CONNECTIONS = "least_connections"
    CONSISTENT_HASH = "consistent_hash"
    GEOGRAPHIC = "geographic"

@dataclass
class ServiceInstance:
    """Service instance in the distributed system"""
    id: str
    name: str
    host: str
    port: int
    status: ServiceStatus = ServiceStatus.HEALTHY
    weight: int = 1
    current_connections: int = 0
    last_health_check: Optional[datetime] = None
    metadata: Dict[str, Any] = field(default_factory=dict)
    
    @property
    def endpoint(self) -> str:
        return f"http://{self.host}:{self.port}"

class ServiceRegistry:
    """
    Service discovery and registry for World Cup 2026 microservices
    Handles service registration, health checking, and load balancing
    """
    
    def __init__(self, redis_client: redis.Redis):
        self.redis = redis_client
        self.services: Dict[str, List[ServiceInstance]] = {}
        self.health_check_interval = 30  # seconds
        self.health_check_timeout = 5    # seconds
        
    async def register_service(self, service: ServiceInstance):
        """Register a service instance"""
        service_key = f"service:{service.name}"
        
        # Store in Redis for persistence
        await self.redis.hset(
            service_key,
            service.id,
            json.dumps({
                "id": service.id,
                "name": service.name,
                "host": service.host,
                "port": service.port,
                "status": service.status.value,
                "weight": service.weight,
                "metadata": service.metadata,
                "registered_at": datetime.now(timezone.utc).isoformat()
            })
        )
        
        # Add to local registry
        if service.name not in self.services:
            self.services[service.name] = []
        
        # Remove existing instance with same ID
        self.services[service.name] = [
            s for s in self.services[service.name] if s.id != service.id
        ]
        
        self.services[service.name].append(service)
        
        logger.info(f"✅ Registered service: {service.name}#{service.id} at {service.endpoint}")
    
    async def deregister_service(self, service_name: str, service_id: str):
        """Deregister a service instance"""
        service_key = f"service:{service_name}"
        
        # Remove from Redis
        await self.redis.hdel(service_key, service_id)
        
        # Remove from local registry
        if service_name in self.services:
            self.services[service_name] = [
                s for s in self.services[service_name] if s.id != service_id
            ]
        
        logger.info(f"❌ Deregistered service: {service_name}#{service_id}")
    
    async def discover_services(self, service_name: str) -> List[ServiceInstance]:
        """Discover healthy instances of a service"""
        if service_name not in self.services:
            # Load from Redis
            await self._load_services_from_redis(service_name)
        
        # Return only healthy instances
        healthy_instances = [
            s for s in self.services.get(service_name, [])
            if s.status == ServiceStatus.HEALTHY
        ]
        
        return healthy_instances
    
    async def _load_services_from_redis(self, service_name: str):
        """Load service instances from Redis"""
        service_key = f"service:{service_name}"
        instances_data = await self.redis.hgetall(service_key)
        
        instances = []
        for instance_id, instance_json in instances_data.items():
            try:
                data = json.loads(instance_json)
                instance = ServiceInstance(
                    id=data["id"],
                    name=data["name"],
                    host=data["host"],
                    port=data["port"],
                    status=ServiceStatus(data["status"]),
                    weight=data.get("weight", 1),
                    metadata=data.get("metadata", {})
                )
                instances.append(instance)
            except Exception as e:
                logger.error(f"❌ Error loading service instance {instance_id}: {e}")
        
        self.services[service_name] = instances
    
    async def health_check_services(self):
        """Perform health checks on all registered services"""
        for service_name, instances in self.services.items():
            for instance in instances:
                try:
                    # Perform health check
                    health_url = f"{instance.endpoint}/health"
                    
                    async with aiohttp.ClientSession() as session:
                        async with session.get(
                            health_url,
                            timeout=aiohttp.ClientTimeout(total=self.health_check_timeout)
                        ) as response:
                            if response.status == 200:
                                instance.status = ServiceStatus.HEALTHY
                            else:
                                instance.status = ServiceStatus.DEGRADED
                
                except Exception as e:
                    logger.warning(f"⚠️ Health check failed for {service_name}#{instance.id}: {e}")
                    instance.status = ServiceStatus.UNHEALTHY
                
                instance.last_health_check = datetime.now(timezone.utc)
                
                # Update status in Redis
                await self._update_instance_status(instance)
    
    async def _update_instance_status(self, instance: ServiceInstance):
        """Update instance status in Redis"""
        service_key = f"service:{instance.name}"
        
        try:
            instance_data = await self.redis.hget(service_key, instance.id)
            if instance_data:
                data = json.loads(instance_data)
                data["status"] = instance.status.value
                data["last_health_check"] = instance.last_health_check.isoformat()
                
                await self.redis.hset(service_key, instance.id, json.dumps(data))
        except Exception as e:
            logger.error(f"❌ Error updating instance status: {e}")

class LoadBalancer:
    """
    Advanced load balancer for World Cup 2026 platform
    Supports multiple load balancing strategies
    """
    
    def __init__(self, service_registry: ServiceRegistry):
        self.service_registry = service_registry
        self.round_robin_counters: Dict[str, int] = {}
        self.consistent_hash_ring: Dict[str, List[str]] = {}
    
    async def get_service_instance(
        self,
        service_name: str,
        strategy: LoadBalancingStrategy = LoadBalancingStrategy.ROUND_ROBIN,
        context: Optional[Dict[str, Any]] = None
    ) -> Optional[ServiceInstance]:
        """Get a service instance using the specified load balancing strategy"""
        
        instances = await self.service_registry.discover_services(service_name)
        
        if not instances:
            logger.warning(f"⚠️ No healthy instances found for service: {service_name}")
            return None
        
        if strategy == LoadBalancingStrategy.ROUND_ROBIN:
            return self._round_robin_select(service_name, instances)
        
        elif strategy == LoadBalancingStrategy.WEIGHTED_ROUND_ROBIN:
            return self._weighted_round_robin_select(service_name, instances)
        
        elif strategy == LoadBalancingStrategy.LEAST_CONNECTIONS:
            return self._least_connections_select(instances)
        
        elif strategy == LoadBalancingStrategy.CONSISTENT_HASH:
            return self._consistent_hash_select(service_name, instances, context)
        
        elif strategy == LoadBalancingStrategy.GEOGRAPHIC:
            return self._geographic_select(instances, context)
        
        else:
            # Default to round robin
            return self._round_robin_select(service_name, instances)
    
    def _round_robin_select(self, service_name: str, instances: List[ServiceInstance]) -> ServiceInstance:
        """Round robin load balancing"""
        if service_name not in self.round_robin_counters:
            self.round_robin_counters[service_name] = 0
        
        index = self.round_robin_counters[service_name] % len(instances)
        self.round_robin_counters[service_name] += 1
        
        return instances[index]
    
    def _weighted_round_robin_select(self, service_name: str, instances: List[ServiceInstance]) -> ServiceInstance:
        """Weighted round robin load balancing"""
        # Create weighted list
        weighted_instances = []
        for instance in instances:
            weighted_instances.extend([instance] * instance.weight)
        
        if not weighted_instances:
            return instances[0]
        
        if service_name not in self.round_robin_counters:
            self.round_robin_counters[service_name] = 0
        
        index = self.round_robin_counters[service_name] % len(weighted_instances)
        self.round_robin_counters[service_name] += 1
        
        return weighted_instances[index]
    
    def _least_connections_select(self, instances: List[ServiceInstance]) -> ServiceInstance:
        """Least connections load balancing"""
        return min(instances, key=lambda x: x.current_connections)
    
    def _consistent_hash_select(
        self,
        service_name: str,
        instances: List[ServiceInstance],
        context: Optional[Dict[str, Any]]
    ) -> ServiceInstance:
        """Consistent hash load balancing"""
        if not context or 'hash_key' not in context:
            # Fallback to round robin
            return self._round_robin_select(service_name, instances)
        
        hash_key = context['hash_key']
        hash_value = int(hashlib.md5(hash_key.encode()).hexdigest(), 16)
        
        # Simple consistent hashing
        index = hash_value % len(instances)
        return instances[index]
    
    def _geographic_select(
        self,
        instances: List[ServiceInstance],
        context: Optional[Dict[str, Any]]
    ) -> ServiceInstance:
        """Geographic load balancing"""
        if not context or 'user_region' not in context:
            return random.choice(instances)
        
        user_region = context['user_region']
        
        # Prefer instances in the same region
        regional_instances = [
            instance for instance in instances
            if instance.metadata.get('region') == user_region
        ]
        
        if regional_instances:
            return random.choice(regional_instances)
        else:
            return random.choice(instances)

# =====================================================
# MODULE 45: COMPLETE SYSTEM DESIGN - CIRCUIT BREAKER
# =====================================================

class CircuitBreakerState(str, Enum):
    CLOSED = "closed"      # Normal operation
    OPEN = "open"          # Failing, reject requests
    HALF_OPEN = "half_open"  # Testing if service recovered

@dataclass
class CircuitBreakerConfig:
    failure_threshold: int = 5      # Failures before opening
    recovery_timeout: int = 60      # Seconds before trying half-open
    success_threshold: int = 3      # Successes to close from half-open
    timeout: int = 30               # Request timeout in seconds

class CircuitBreaker:
    """
    Circuit breaker pattern for World Cup 2026 resilient architecture
    Prevents cascading failures in distributed systems
    """
    
    def __init__(self, name: str, config: CircuitBreakerConfig):
        self.name = name
        self.config = config
        self.state = CircuitBreakerState.CLOSED
        self.failure_count = 0
        self.success_count = 0
        self.last_failure_time: Optional[datetime] = None
        self.next_attempt_time: Optional[datetime] = None
    
    async def call(self, func, *args, **kwargs):
        """Execute function with circuit breaker protection"""
        
        # Check if circuit is open
        if self.state == CircuitBreakerState.OPEN:
            if self._should_attempt_reset():
                self.state = CircuitBreakerState.HALF_OPEN
                self.success_count = 0
                logger.info(f"🔄 Circuit breaker {self.name} transitioning to HALF_OPEN")
            else:
                raise Exception(f"Circuit breaker {self.name} is OPEN")
        
        try:
            # Execute the function with timeout
            result = await asyncio.wait_for(
                func(*args, **kwargs),
                timeout=self.config.timeout
            )
            
            # Success - handle state transitions
            self._on_success()
            return result
            
        except Exception as e:
            # Failure - handle state transitions
            self._on_failure()
            raise e
    
    def _should_attempt_reset(self) -> bool:
        """Check if we should attempt to reset the circuit breaker"""
        if not self.next_attempt_time:
            return True
        
        return datetime.now(timezone.utc) >= self.next_attempt_time
    
    def _on_success(self):
        """Handle successful request"""
        if self.state == CircuitBreakerState.HALF_OPEN:
            self.success_count += 1
            
            if self.success_count >= self.config.success_threshold:
                self.state = CircuitBreakerState.CLOSED
                self.failure_count = 0
                self.success_count = 0
                logger.info(f"✅ Circuit breaker {self.name} CLOSED - service recovered")
        
        elif self.state == CircuitBreakerState.CLOSED:
            # Reset failure count on success
            self.failure_count = 0
    
    def _on_failure(self):
        """Handle failed request"""
        self.failure_count += 1
        self.last_failure_time = datetime.now(timezone.utc)
        
        if self.state == CircuitBreakerState.CLOSED:
            if self.failure_count >= self.config.failure_threshold:
                self.state = CircuitBreakerState.OPEN
                self.next_attempt_time = datetime.now(timezone.utc) + \
                    timedelta(seconds=self.config.recovery_timeout)
                logger.warning(f"🚨 Circuit breaker {self.name} OPENED - too many failures")
        
        elif self.state == CircuitBreakerState.HALF_OPEN:
            # Failed during half-open, go back to open
            self.state = CircuitBreakerState.OPEN
            self.next_attempt_time = datetime.now(timezone.utc) + \
                timedelta(seconds=self.config.recovery_timeout)
            logger.warning(f"🚨 Circuit breaker {self.name} back to OPEN - recovery failed")

class DistributedSystemManager:
    """
    Main manager for World Cup 2026 distributed system
    Coordinates service discovery, load balancing, and resilience patterns
    """
    
    def __init__(self, redis_url: str):
        self.redis_url = redis_url
        self.redis_client = None
        self.service_registry = None
        self.load_balancer = None
        self.circuit_breakers: Dict[str, CircuitBreaker] = {}
    
    async def initialize(self):
        """Initialize distributed system components"""
        logger.info("🏗️ Initializing World Cup 2026 Distributed System...")
        
        # Initialize Redis
        self.redis_client = redis.from_url(self.redis_url, decode_responses=True)
        await self.redis_client.ping()
        
        # Initialize service registry
        self.service_registry = ServiceRegistry(self.redis_client)
        
        # Initialize load balancer
        self.load_balancer = LoadBalancer(self.service_registry)
        
        # Start health check background task
        asyncio.create_task(self._health_check_loop())
        
        logger.info("✅ Distributed system initialized")
    
    async def register_service(
        self,
        name: str,
        host: str,
        port: int,
        weight: int = 1,
        metadata: Optional[Dict[str, Any]] = None
    ) -> str:
        """Register a new service instance"""
        service_id = f"{name}-{host}-{port}-{int(time.time())}"
        
        service = ServiceInstance(
            id=service_id,
            name=name,
            host=host,
            port=port,
            weight=weight,
            metadata=metadata or {}
        )
        
        await self.service_registry.register_service(service)
        return service_id
    
    async def call_service(
        self,
        service_name: str,
        method: str,
        endpoint: str,
        data: Optional[Dict[str, Any]] = None,
        strategy: LoadBalancingStrategy = LoadBalancingStrategy.ROUND_ROBIN,
        context: Optional[Dict[str, Any]] = None
    ) -> Any:
        """Make a resilient service call with load balancing and circuit breaker"""
        
        # Get circuit breaker for this service
        circuit_breaker = self._get_circuit_breaker(service_name)
        
        async def make_request():
            # Get service instance using load balancer
            instance = await self.load_balancer.get_service_instance(
                service_name, strategy, context
            )
            
            if not instance:
                raise Exception(f"No healthy instances available for {service_name}")
            
            # Make HTTP request
            url = f"{instance.endpoint}{endpoint}"
            
            async with aiohttp.ClientSession() as session:
                if method.upper() == "GET":
                    async with session.get(url, params=data) as response:
                        response.raise_for_status()
                        return await response.json()
                
                elif method.upper() == "POST":
                    async with session.post(url, json=data) as response:
                        response.raise_for_status()
                        return await response.json()
                
                else:
                    raise ValueError(f"Unsupported HTTP method: {method}")
        
        # Execute with circuit breaker protection
        return await circuit_breaker.call(make_request)
    
    def _get_circuit_breaker(self, service_name: str) -> CircuitBreaker:
        """Get or create circuit breaker for service"""
        if service_name not in self.circuit_breakers:
            config = CircuitBreakerConfig(
                failure_threshold=5,
                recovery_timeout=60,
                success_threshold=3,
                timeout=30
            )
            
            self.circuit_breakers[service_name] = CircuitBreaker(
                f"cb-{service_name}",
                config
            )
        
        return self.circuit_breakers[service_name]
    
    async def _health_check_loop(self):
        """Background task for health checking services"""
        while True:
            try:
                await self.service_registry.health_check_services()
                await asyncio.sleep(30)  # Health check every 30 seconds
            except Exception as e:
                logger.error(f"❌ Health check loop error: {e}")
                await asyncio.sleep(10)  # Retry after 10 seconds on error

# Example usage
async def main():
    """Example usage of World Cup 2026 distributed system"""
    
    # Initialize distributed system
    system = DistributedSystemManager("redis://redis:6379")
    await system.initialize()
    
    # Register some services
    await system.register_service("user-service", "localhost", 8001, weight=2)
    await system.register_service("user-service", "localhost", 8002, weight=1)
    await system.register_service("match-service", "localhost", 8003)
    
    # Make service calls
    try:
        user_data = await system.call_service(
            "user-service",
            "GET",
            "/api/v1/users/123",
            strategy=LoadBalancingStrategy.WEIGHTED_ROUND_ROBIN
        )
        
        print(f"🏆 User data: {user_data}")
        
    except Exception as e:
        print(f"❌ Service call failed: {e}")

if __name__ == "__main__":
    asyncio.run(main())
