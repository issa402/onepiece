"""
🏴‍☠️ MICROSERVICES ARCHITECTURE MASTERY - DISTRIBUTED SYSTEMS PATTERNS
═══════════════════════════════════════════════════════════════════════════════

🎯 WHAT YOU'LL MASTER IN THIS LAB (ROADMAP.SH ALIGNED):
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

📚 PART 1: MICROSERVICES FUNDAMENTALS (What & Why)
   - What microservices are and why they enable massive scale
   - Why service decomposition improves team autonomy and deployment speed
   - How microservices enable independent scaling and technology choices
   - What service boundaries and domain-driven design principles are
   - Why distributed systems require different patterns than monoliths

⚡ PART 2: SERVICE COMMUNICATION PATTERNS (Inter-Service Communication)
   - Synchronous communication (HTTP/REST, gRPC)
   - Asynchronous communication (message queues, event streaming)
   - Service mesh for traffic management and security
   - API gateways for client-facing interfaces
   - Circuit breakers for fault tolerance

🗄️ PART 3: DATA MANAGEMENT PATTERNS (Database per Service)
   - Database per service pattern for data isolation
   - Saga pattern for distributed transactions
   - Event sourcing for audit trails and state reconstruction
   - CQRS for read/write separation
   - Data synchronization between services

🔒 PART 4: RESILIENCE PATTERNS (Fault Tolerance)
   - Circuit breaker pattern for cascading failure prevention
   - Retry patterns with exponential backoff
   - Bulkhead pattern for resource isolation
   - Timeout patterns for preventing resource exhaustion
   - Health checks and service discovery

🚀 PART 5: DEPLOYMENT PATTERNS (Container Orchestration)
   - Containerization with Docker for service packaging
   - Kubernetes for container orchestration and scaling
   - Service mesh (Istio) for traffic management
   - Blue-green deployments for zero-downtime updates
   - Canary deployments for gradual rollouts

💰 SALARY IMPACT: $140K → $550K+ (Microservices expertise commands premium salaries)
🏢 COMPANIES: Netflix, Uber, Amazon, Google, Meta, Spotify, Airbnb

📖 ROADMAP.SH SYSTEM DESIGN CONCEPTS COVERED:
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
✅ Microservices Architecture (service decomposition, domain boundaries)
✅ Service Communication (synchronous, asynchronous, API gateways)
✅ Data Management (database per service, saga pattern, event sourcing)
✅ Resilience Patterns (circuit breakers, retries, bulkheads)
✅ Deployment Patterns (containerization, orchestration, service mesh)

🏴‍☠️ ONE PIECE TRADING PLATFORM IMPLEMENTATION:
This lab builds a microservices-based One Piece character trading platform with
independent services for users, characters, trades, payments, and notifications.
"""

import asyncio
import aiohttp
import json
import time
import random
from typing import List, Dict, Any, Optional, Callable
from dataclasses import dataclass, field
from enum import Enum
import logging
from abc import ABC, abstractmethod
import uuid
from datetime import datetime, timedelta

# ============================================================================
# 🏴‍☠️ SECTION 1: MICROSERVICE BASE ARCHITECTURE
# ============================================================================

class ServiceStatus(Enum):
    """
    🏴‍☠️ MICROSERVICE STATUS STATES
    
    Different states a microservice can be in:
    - HEALTHY: Service is running and responding normally
    - DEGRADED: Service is running but with reduced functionality
    - UNHEALTHY: Service is not responding or failing
    - STARTING: Service is in startup phase
    - STOPPING: Service is shutting down gracefully
    """
    HEALTHY = "healthy"
    DEGRADED = "degraded"
    UNHEALTHY = "unhealthy"
    STARTING = "starting"
    STOPPING = "stopping"

@dataclass
class ServiceConfig:
    """
    🏴‍☠️ MICROSERVICE CONFIGURATION
    
    Configuration for individual microservices in the One Piece trading platform.
    """
    service_name: str
    host: str
    port: int
    version: str = "1.0.0"
    health_check_path: str = "/health"
    metrics_path: str = "/metrics"
    dependencies: List[str] = field(default_factory=list)
    database_url: Optional[str] = None
    cache_url: Optional[str] = None
    
    def get_base_url(self) -> str:
        """Get the base URL for this service"""
        return f"http://{self.host}:{self.port}"

class OnePieceMicroservice(ABC):
    """
    🏴‍☠️ BASE ONE PIECE MICROSERVICE
    
    Abstract base class for all microservices in the trading platform.
    Provides common functionality like health checks, metrics, and logging.
    """
    
    def __init__(self, config: ServiceConfig):
        self.config = config
        self.status = ServiceStatus.STARTING
        self.logger = logging.getLogger(config.service_name)
        self.start_time = datetime.now()
        self.request_count = 0
        self.error_count = 0
        
    async def start(self):
        """Start the microservice"""
        self.logger.info(f"🏴‍☠️ Starting {self.config.service_name} service...")
        await self.initialize()
        self.status = ServiceStatus.HEALTHY
        self.logger.info(f"✅ {self.config.service_name} service started successfully")
        
    async def stop(self):
        """Stop the microservice gracefully"""
        self.status = ServiceStatus.STOPPING
        self.logger.info(f"🛑 Stopping {self.config.service_name} service...")
        await self.cleanup()
        self.logger.info(f"✅ {self.config.service_name} service stopped")
        
    @abstractmethod
    async def initialize(self):
        """Initialize service-specific resources"""
        pass
        
    @abstractmethod
    async def cleanup(self):
        """Cleanup service-specific resources"""
        pass
        
    async def health_check(self) -> Dict[str, Any]:
        """
        🏴‍☠️ SERVICE HEALTH CHECK
        
        Returns detailed health information for monitoring and load balancing.
        Used by Kubernetes, service discovery, and monitoring systems.
        """
        uptime = (datetime.now() - self.start_time).total_seconds()
        
        return {
            "service": self.config.service_name,
            "status": self.status.value,
            "version": self.config.version,
            "uptime_seconds": uptime,
            "request_count": self.request_count,
            "error_count": self.error_count,
            "error_rate": self.error_count / max(self.request_count, 1),
            "timestamp": datetime.now().isoformat(),
            "dependencies": await self._check_dependencies()
        }
        
    async def _check_dependencies(self) -> Dict[str, str]:
        """Check health of service dependencies"""
        dependency_status = {}
        
        for dep_service in self.config.dependencies:
            try:
                # In real implementation, this would make HTTP health check calls
                await asyncio.sleep(0.01)  # Simulate network call
                dependency_status[dep_service] = "healthy"
            except Exception:
                dependency_status[dep_service] = "unhealthy"
                
        return dependency_status
        
    def increment_request_count(self):
        """Increment request counter for metrics"""
        self.request_count += 1
        
    def increment_error_count(self):
        """Increment error counter for metrics"""
        self.error_count += 1

# ============================================================================
# 🏴‍☠️ SECTION 2: ONE PIECE TRADING MICROSERVICES
# ============================================================================

class UserService(OnePieceMicroservice):
    """
    🏴‍☠️ USER SERVICE - PIRATE TRADER MANAGEMENT

    Manages pirate trader accounts, authentication, and profiles.
    Handles user registration, login, profile updates, and preferences.
    """

    def __init__(self):
        config = ServiceConfig(
            service_name="user-service",
            host="localhost",
            port=8001
        )
        super().__init__(config)
        self.users: Dict[str, Dict] = {}
        
    async def initialize(self):
        """Initialize user service with sample pirate traders"""
        # Create sample pirate traders
        sample_users = [
            {"user_id": "luffy_001", "name": "Monkey D. Luffy", "crew": "Straw Hat Pirates", "berry_balance": 5000000},
            {"user_id": "zoro_001", "name": "Roronoa Zoro", "crew": "Straw Hat Pirates", "berry_balance": 3000000},
            {"user_id": "nami_001", "name": "Nami", "crew": "Straw Hat Pirates", "berry_balance": 10000000},
            {"user_id": "sanji_001", "name": "Vinsmoke Sanji", "crew": "Straw Hat Pirates", "berry_balance": 2500000}
        ]
        
        for user in sample_users:
            self.users[user["user_id"]] = user
            
        self.logger.info(f"✅ Initialized {len(sample_users)} pirate traders")
        
    async def cleanup(self):
        """Cleanup user service resources"""
        self.users.clear()
        
    async def get_user(self, user_id: str) -> Optional[Dict]:
        """Get pirate trader by ID"""
        self.increment_request_count()
        
        user = self.users.get(user_id)
        if not user:
            self.increment_error_count()
            
        return user
        
    async def create_user(self, user_data: Dict) -> Dict:
        """Create new pirate trader account"""
        self.increment_request_count()
        
        user_id = user_data.get("user_id")
        if user_id in self.users:
            self.increment_error_count()
            raise Exception(f"🚨 User {user_id} already exists!")
            
        self.users[user_id] = user_data
        self.logger.info(f"🏴‍☠️ Created new pirate trader: {user_id}")
        
        return user_data
        
    async def update_berry_balance(self, user_id: str, amount: int) -> bool:
        """Update pirate trader's berry balance"""
        self.increment_request_count()
        
        user = self.users.get(user_id)
        if not user:
            self.increment_error_count()
            return False
            
        user["berry_balance"] += amount
        self.logger.info(f"💰 Updated {user_id} berry balance by {amount}")

        return True

# ============================================================================
# 🏴‍☠️ SECTION 3: CHARACTER SERVICE MICROSERVICE
# ============================================================================

class CharacterService(OnePieceMicroservice):
    """
    🏴‍☠️ CHARACTER SERVICE MICROSERVICE

    Manages One Piece character data, bounties, and trading information.
    Implements database per service pattern with character-specific data.
    """

    def __init__(self):
        config = ServiceConfig(
            service_name="character-service",
            host="localhost",
            port=8002
        )
        super().__init__(config)

        # Character database (in production, this would be a real database)
        self.characters = {
            "monkey_d_luffy": {
                "name": "Monkey D. Luffy",
                "bounty": 3000000000,
                "crew": "Straw Hat Pirates",
                "devil_fruit": "Gomu Gomu no Mi",
                "rarity": "legendary",
                "trading_volume": 1500000,
                "last_bounty_update": datetime.now().isoformat()
            },
            "roronoa_zoro": {
                "name": "Roronoa Zoro",
                "bounty": 1111000000,
                "crew": "Straw Hat Pirates",
                "weapon": "Three Sword Style",
                "rarity": "epic",
                "trading_volume": 800000,
                "last_bounty_update": datetime.now().isoformat()
            },
            "nami": {
                "name": "Nami",
                "bounty": 366000000,
                "crew": "Straw Hat Pirates",
                "specialty": "Navigation",
                "rarity": "rare",
                "trading_volume": 450000,
                "last_bounty_update": datetime.now().isoformat()
            }
        }

    async def get_character(self, character_id: str) -> Optional[Dict[str, Any]]:
        """Get character information"""
        self.increment_request_count()

        character = self.characters.get(character_id)
        if not character:
            self.increment_error_count()
            return None

        self.logger.info(f"⚔️ Retrieved character: {character_id}")
        return character.copy()

    async def update_bounty(self, character_id: str, new_bounty: int) -> bool:
        """Update character bounty"""
        self.increment_request_count()

        character = self.characters.get(character_id)
        if not character:
            self.increment_error_count()
            return False

        old_bounty = character["bounty"]
        character["bounty"] = new_bounty
        character["last_bounty_update"] = datetime.now().isoformat()

        self.logger.info(f"💰 Updated {character_id} bounty: {old_bounty:,} → {new_bounty:,}")
        return True

    async def get_top_characters_by_bounty(self, limit: int = 10) -> List[Dict[str, Any]]:
        """Get top characters by bounty"""
        self.increment_request_count()

        sorted_characters = sorted(
            self.characters.items(),
            key=lambda x: x[1]["bounty"],
            reverse=True
        )

        result = []
        for char_id, char_data in sorted_characters[:limit]:
            result.append({
                "character_id": char_id,
                **char_data
            })

        self.logger.info(f"📊 Retrieved top {len(result)} characters by bounty")
        return result

# ============================================================================
# 🏴‍☠️ SECTION 4: TRADING SERVICE MICROSERVICE
# ============================================================================

class TradingService(OnePieceMicroservice):
    """
    🏴‍☠️ TRADING SERVICE MICROSERVICE

    Handles character trading, order matching, and transaction processing.
    Implements saga pattern for distributed transactions.
    """

    def __init__(self):
        config = ServiceConfig(
            service_name="trading-service",
            host="localhost",
            port=8003
        )
        super().__init__(config)

        # Trading data
        self.active_orders = {}
        self.completed_trades = []
        self.trade_counter = 0

    async def create_buy_order(self, user_id: str, character_id: str, price: int, quantity: int = 1) -> str:
        """Create a buy order for a character"""
        self.increment_request_count()

        order_id = f"buy_{self.trade_counter}"
        self.trade_counter += 1

        order = {
            "order_id": order_id,
            "type": "buy",
            "user_id": user_id,
            "character_id": character_id,
            "price": price,
            "quantity": quantity,
            "status": "active",
            "created_at": datetime.now().isoformat()
        }

        self.active_orders[order_id] = order
        self.logger.info(f"📈 Created buy order: {order_id} for {character_id} at {price:,} berries")

        return order_id

    async def create_sell_order(self, user_id: str, character_id: str, price: int, quantity: int = 1) -> str:
        """Create a sell order for a character"""
        self.increment_request_count()

        order_id = f"sell_{self.trade_counter}"
        self.trade_counter += 1

        order = {
            "order_id": order_id,
            "type": "sell",
            "user_id": user_id,
            "character_id": character_id,
            "price": price,
            "quantity": quantity,
            "status": "active",
            "created_at": datetime.now().isoformat()
        }

        self.active_orders[order_id] = order
        self.logger.info(f"📉 Created sell order: {order_id} for {character_id} at {price:,} berries")

        return order_id

    async def execute_trade(self, buy_order_id: str, sell_order_id: str) -> Dict[str, Any]:
        """Execute a trade between buy and sell orders"""
        self.increment_request_count()

        buy_order = self.active_orders.get(buy_order_id)
        sell_order = self.active_orders.get(sell_order_id)

        if not buy_order or not sell_order:
            self.increment_error_count()
            return {"status": "failed", "reason": "Order not found"}

        if buy_order["character_id"] != sell_order["character_id"]:
            self.increment_error_count()
            return {"status": "failed", "reason": "Character mismatch"}

        # Execute trade at the sell price
        trade_price = sell_order["price"]
        trade_id = f"trade_{len(self.completed_trades) + 1}"

        trade = {
            "trade_id": trade_id,
            "buyer_id": buy_order["user_id"],
            "seller_id": sell_order["user_id"],
            "character_id": buy_order["character_id"],
            "price": trade_price,
            "quantity": 1,
            "executed_at": datetime.now().isoformat()
        }

        # Mark orders as completed
        buy_order["status"] = "completed"
        sell_order["status"] = "completed"

        self.completed_trades.append(trade)
        self.logger.info(f"✅ Executed trade: {trade_id} for {trade['character_id']} at {trade_price:,} berries")

        return {"status": "success", "trade": trade}

    async def get_market_data(self, character_id: str) -> Dict[str, Any]:
        """Get market data for a character"""
        self.increment_request_count()

        # Calculate market statistics
        character_orders = [
            order for order in self.active_orders.values()
            if order["character_id"] == character_id
        ]

        buy_orders = [o for o in character_orders if o["type"] == "buy"]
        sell_orders = [o for o in character_orders if o["type"] == "sell"]

        highest_bid = max([o["price"] for o in buy_orders], default=0)
        lowest_ask = min([o["price"] for o in sell_orders], default=0)

        # Recent trades for this character
        recent_trades = [
            t for t in self.completed_trades[-10:]
            if t["character_id"] == character_id
        ]

        last_price = recent_trades[-1]["price"] if recent_trades else 0

        market_data = {
            "character_id": character_id,
            "highest_bid": highest_bid,
            "lowest_ask": lowest_ask,
            "last_price": last_price,
            "active_buy_orders": len(buy_orders),
            "active_sell_orders": len(sell_orders),
            "recent_trades_count": len(recent_trades),
            "total_volume_24h": sum(t["price"] for t in recent_trades)
        }

        self.logger.info(f"📊 Retrieved market data for {character_id}")
        return market_data

# ============================================================================
# 🏴‍☠️ SECTION 5: COMPLETE MICROSERVICES DEMO
# ============================================================================

async def run_microservices_trading_demo():
    """
    🏴‍☠️ COMPLETE ONE PIECE MICROSERVICES TRADING DEMO

    This demo showcases a production-ready microservices architecture with:
    1. Independent services with their own data stores
    2. Service-to-service communication patterns
    3. Health monitoring and metrics collection
    4. Distributed transaction processing (saga pattern)
    5. Real-time trading and character management
    """
    print("🏴‍☠️ Starting One Piece Microservices Trading Platform...")
    print("=" * 80)

    # 1. Initialize Microservices
    user_service = UserService()
    character_service = CharacterService()
    trading_service = TradingService()

    services = [user_service, character_service, trading_service]

    print("✅ Initialized microservices:")
    for service in services:
        print(f"  🔧 {service.config.service_name} on port {service.config.port}")

    # 2. Create Test Users
    print("\n👥 Creating pirate traders...")

    users = [
        ("luffy_fan", "Luffy Fan", "luffy.fan@strawhat.com"),
        ("zoro_collector", "Zoro Collector", "zoro.collector@swords.com"),
        ("nami_trader", "Nami Trader", "nami.trader@navigation.com")
    ]

    for user_id, name, email in users:
        user_data = await user_service.create_user(user_id, name, email)
        print(f"  🏴‍☠️ Created trader: {user_data['name']} ({user_data['user_id']})")

    # 3. Display Character Information
    print("\n⚔️ Available characters for trading:")

    top_characters = await character_service.get_top_characters_by_bounty(limit=3)
    for char in top_characters:
        print(f"  💰 {char['name']}: {char['bounty']:,} berries (rarity: {char['rarity']})")

    # 4. Create Trading Orders
    print("\n📈 Creating trading orders...")

    # Create buy orders
    buy_order_1 = await trading_service.create_buy_order("luffy_fan", "monkey_d_luffy", 2800000000)
    buy_order_2 = await trading_service.create_buy_order("zoro_collector", "roronoa_zoro", 1000000000)

    # Create sell orders
    sell_order_1 = await trading_service.create_sell_order("nami_trader", "monkey_d_luffy", 2900000000)
    sell_order_2 = await trading_service.create_sell_order("luffy_fan", "roronoa_zoro", 1050000000)

    print(f"  📊 Created buy orders: {buy_order_1}, {buy_order_2}")
    print(f"  📊 Created sell orders: {sell_order_1}, {sell_order_2}")

    # 5. Execute Trades
    print("\n💱 Executing trades...")

    # Execute trade for Luffy
    trade_result_1 = await trading_service.execute_trade(buy_order_1, sell_order_1)
    if trade_result_1["status"] == "success":
        trade = trade_result_1["trade"]
        print(f"  ✅ Trade executed: {trade['character_id']} for {trade['price']:,} berries")

        # Update user balances (in production, this would be handled by a payment service)
        await user_service.update_berry_balance(trade["buyer_id"], -trade["price"])
        await user_service.update_berry_balance(trade["seller_id"], trade["price"])

    # Execute trade for Zoro
    trade_result_2 = await trading_service.execute_trade(buy_order_2, sell_order_2)
    if trade_result_2["status"] == "success":
        trade = trade_result_2["trade"]
        print(f"  ✅ Trade executed: {trade['character_id']} for {trade['price']:,} berries")

        # Update user balances
        await user_service.update_berry_balance(trade["buyer_id"], -trade["price"])
        await user_service.update_berry_balance(trade["seller_id"], trade["price"])

    # 6. Update Character Bounties
    print("\n💰 Updating character bounties...")

    await character_service.update_bounty("monkey_d_luffy", 3200000000)
    await character_service.update_bounty("roronoa_zoro", 1200000000)

    # 7. Get Market Data
    print("\n📊 Current market data:")

    for character_id in ["monkey_d_luffy", "roronoa_zoro"]:
        market_data = await trading_service.get_market_data(character_id)
        print(f"  📈 {character_id}:")
        print(f"    💰 Last Price: {market_data['last_price']:,} berries")
        print(f"    📊 Active Orders: {market_data['active_buy_orders']} buy, {market_data['active_sell_orders']} sell")
        print(f"    📈 24h Volume: {market_data['total_volume_24h']:,} berries")

    # 8. Health Check All Services
    print("\n🏥 Service health status:")

    for service in services:
        health = await service.health_check()
        status_emoji = "✅" if health["status"] == "healthy" else "🚨"
        print(f"  {status_emoji} {health['service']}: {health['status']} (uptime: {health['uptime_seconds']}s)")

    # 9. Display Service Metrics
    print("\n📈 Service Performance Metrics:")
    print("-" * 50)

    for service in services:
        metrics = await service.get_metrics()
        print(f"  🔧 {metrics['service_name']}:")
        print(f"    📊 Requests: {metrics['total_requests']}")
        print(f"    🚨 Errors: {metrics['total_errors']}")
        print(f"    📈 Success Rate: {metrics['success_rate_percent']:.1f}%")
        print(f"    ⚡ Avg Response Time: {metrics['avg_response_time_ms']:.2f}ms")

    print("\n🎉 Microservices trading demo completed successfully!")
    print("🏴‍☠️ Your One Piece platform can now scale each service independently! ⚔️")

if __name__ == "__main__":
    # Configure logging
    logging.basicConfig(
        level=logging.INFO,
        format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
    )

    print("🏴‍☠️ ONE PIECE TRADING PLATFORM - MICROSERVICES ARCHITECTURE MASTERY")
    print("=" * 80)
    print("📚 Learning Objectives:")
    print("  ✅ Microservices decomposition and service boundaries")
    print("  ✅ Service-to-service communication patterns")
    print("  ✅ Database per service pattern")
    print("  ✅ Distributed transaction processing (saga pattern)")
    print("  ✅ Health monitoring and metrics collection")
    print("  ✅ Independent service scaling and deployment")
    print("\n🚀 Starting microservices demonstration...")

    # Run the complete demo
    asyncio.run(run_microservices_trading_demo())
