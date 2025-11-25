"""
🏴‍☠️ CACHING STRATEGIES MASTERY - MULTI-LEVEL PERFORMANCE OPTIMIZATION
═══════════════════════════════════════════════════════════════════════════════

🎯 WHAT YOU'LL MASTER IN THIS LAB (ROADMAP.SH ALIGNED):
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

📚 PART 1: CACHING FUNDAMENTALS (What & Why)
   - What caching is and why it's critical for sub-millisecond response times
   - Why multi-level caching enables 99.9% cache hit rates
   - How cache hierarchies reduce database load by 95%+
   - What cache invalidation strategies prevent stale data
   - Why caching patterns enable billion-user platforms

⚡ PART 2: CLIENT-SIDE CACHING (Browser & Mobile)
   - Browser caching with HTTP headers (Cache-Control, ETag)
   - Local storage and session storage for user data
   - Service workers for offline-first applications
   - Mobile app caching for reduced network usage
   - CDN edge caching for global content delivery

🗄️ PART 3: APPLICATION-LEVEL CACHING (In-Memory)
   - In-memory caches (Redis, Memcached) for hot data
   - Application-level caching with LRU eviction
   - Query result caching for expensive database operations
   - Session caching for user authentication state
   - Distributed caching across multiple servers

🔒 PART 4: DATABASE CACHING (Query Optimization)
   - Database query result caching
   - Connection pooling for reduced overhead
   - Prepared statement caching
   - Index caching for faster lookups
   - Buffer pool optimization

🚀 PART 5: ADVANCED CACHING PATTERNS (Enterprise Grade)
   - Write-through vs write-back caching strategies
   - Cache-aside pattern for flexible caching
   - Read-through and write-through patterns
   - Cache warming and preloading strategies
   - Cache invalidation and consistency patterns

💰 SALARY IMPACT: $125K → $480K+ (Caching expertise drives performance optimization roles)
🏢 COMPANIES: Netflix, Instagram, TikTok, Uber, Amazon, Google, Meta, Twitter

📖 ROADMAP.SH SYSTEM DESIGN CONCEPTS COVERED:
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
✅ Caching Strategies (multi-level, hierarchical, distributed)
✅ Cache Patterns (write-through, write-back, cache-aside)
✅ Performance Optimization (hit rates, latency reduction, throughput)
✅ Invalidation Strategies (TTL, event-based, manual)
✅ Consistency Models (eventual consistency, strong consistency)

🏴‍☠️ ONE PIECE TRADING PLATFORM IMPLEMENTATION:
This lab builds a multi-level caching system for the One Piece character trading
platform with browser, application, and database caching for ultra-fast trading.
"""

import asyncio
import time
import json
import hashlib
from typing import Dict, Any, Optional, List, Tuple
from dataclasses import dataclass, field
from enum import Enum
import logging
from abc import ABC, abstractmethod
import redis
from datetime import datetime, timedelta
import weakref

# ============================================================================
# 🏴‍☠️ SECTION 1: CACHE STRATEGY MODELS
# ============================================================================

class CacheStrategy(Enum):
    """
    🏴‍☠️ CACHING STRATEGIES FOR ONE PIECE TRADING PLATFORM
    
    Different caching patterns for optimal performance:
    - CACHE_ASIDE: Application manages cache explicitly
    - WRITE_THROUGH: Write to cache and database simultaneously
    - WRITE_BACK: Write to cache first, database later
    - READ_THROUGH: Cache loads data on cache miss
    """
    CACHE_ASIDE = "cache_aside"
    WRITE_THROUGH = "write_through"
    WRITE_BACK = "write_back"
    READ_THROUGH = "read_through"

class EvictionPolicy(Enum):
    """
    🏴‍☠️ CACHE EVICTION POLICIES
    
    Different strategies for removing data when cache is full:
    - LRU: Least Recently Used (most common)
    - LFU: Least Frequently Used
    - FIFO: First In, First Out
    - TTL: Time To Live based expiration
    """
    LRU = "lru"
    LFU = "lfu"
    FIFO = "fifo"
    TTL = "ttl"

@dataclass
class CacheEntry:
    """
    🏴‍☠️ CACHE ENTRY FOR ONE PIECE TRADING DATA
    
    Represents a single cached item with metadata for eviction and consistency.
    """
    key: str
    value: Any
    created_at: datetime
    last_accessed: datetime
    access_count: int = 0
    ttl_seconds: Optional[int] = None
    
    def is_expired(self) -> bool:
        """Check if cache entry has expired based on TTL"""
        if self.ttl_seconds is None:
            return False
        return (datetime.now() - self.created_at).total_seconds() > self.ttl_seconds
        
    def touch(self):
        """Update access metadata for LRU/LFU policies"""
        self.last_accessed = datetime.now()
        self.access_count += 1

class OnePieceCacheInterface(ABC):
    """
    🏴‍☠️ ABSTRACT CACHE INTERFACE
    
    Common interface for all cache implementations in the trading platform.
    """
    
    @abstractmethod
    async def get(self, key: str) -> Optional[Any]:
        """Get value from cache"""
        pass
        
    @abstractmethod
    async def set(self, key: str, value: Any, ttl_seconds: Optional[int] = None) -> bool:
        """Set value in cache"""
        pass
        
    @abstractmethod
    async def delete(self, key: str) -> bool:
        """Delete value from cache"""
        pass
        
    @abstractmethod
    async def clear(self) -> bool:
        """Clear all cache entries"""
        pass
        
    @abstractmethod
    async def get_stats(self) -> Dict[str, Any]:
        """Get cache statistics"""
        pass

# ============================================================================
# 🏴‍☠️ SECTION 2: IN-MEMORY CACHE IMPLEMENTATION
# ============================================================================

class OnePieceInMemoryCache(OnePieceCacheInterface):
    """
    🏴‍☠️ IN-MEMORY CACHE FOR ONE PIECE TRADING PLATFORM
    
    High-performance in-memory cache with configurable eviction policies.
    Used for hot trading data like character bounties and user sessions.
    
    Patterns used by:
    - Netflix: In-memory caching for video metadata (99.9% hit rate)
    - Instagram: Photo metadata caching for instant loading
    - TikTok: Video recommendation caching for personalized feeds
    """
    
    def __init__(self, max_size: int = 10000, eviction_policy: EvictionPolicy = EvictionPolicy.LRU):
        self.max_size = max_size
        self.eviction_policy = eviction_policy
        self.cache: Dict[str, CacheEntry] = {}
        self.access_order: List[str] = []  # For LRU tracking
        self.logger = logging.getLogger(__name__)
        
        # Statistics
        self.hits = 0
        self.misses = 0
        self.evictions = 0
        
    async def get(self, key: str) -> Optional[Any]:
        """
        🏴‍☠️ GET VALUE FROM IN-MEMORY CACHE
        
        Retrieves cached trading data with LRU/LFU tracking.
        Returns None for cache misses or expired entries.
        """
        entry = self.cache.get(key)
        
        if entry is None:
            self.misses += 1
            return None
            
        if entry.is_expired():
            await self.delete(key)
            self.misses += 1
            return None
            
        # Update access metadata
        entry.touch()
        self._update_access_order(key)
        
        self.hits += 1
        self.logger.debug(f"✅ Cache hit for key: {key}")
        
        return entry.value
        
    async def set(self, key: str, value: Any, ttl_seconds: Optional[int] = None) -> bool:
        """
        🏴‍☠️ SET VALUE IN IN-MEMORY CACHE
        
        Stores trading data in cache with optional TTL.
        Triggers eviction if cache is full.
        """
        # Check if we need to evict entries
        if len(self.cache) >= self.max_size and key not in self.cache:
            await self._evict_entry()
            
        # Create or update cache entry
        entry = CacheEntry(
            key=key,
            value=value,
            created_at=datetime.now(),
            last_accessed=datetime.now(),
            ttl_seconds=ttl_seconds
        )
        
        self.cache[key] = entry
        self._update_access_order(key)
        
        self.logger.debug(f"💾 Cached key: {key} (TTL: {ttl_seconds}s)")
        return True
        
    async def delete(self, key: str) -> bool:
        """Delete entry from cache"""
        if key in self.cache:
            del self.cache[key]
            if key in self.access_order:
                self.access_order.remove(key)
            return True
        return False
        
    async def clear(self) -> bool:
        """Clear all cache entries"""
        self.cache.clear()
        self.access_order.clear()
        return True
        
    def _update_access_order(self, key: str):
        """Update access order for LRU tracking"""
        if key in self.access_order:
            self.access_order.remove(key)
        self.access_order.append(key)
        
    async def _evict_entry(self):
        """
        🏴‍☠️ EVICT CACHE ENTRY BASED ON POLICY
        
        Removes least valuable entry based on configured eviction policy:
        - LRU: Remove least recently used
        - LFU: Remove least frequently used
        - FIFO: Remove oldest entry
        """
        if not self.cache:
            return
            
        if self.eviction_policy == EvictionPolicy.LRU:
            # Remove least recently used (first in access_order)
            if self.access_order:
                key_to_evict = self.access_order[0]
                await self.delete(key_to_evict)
                self.evictions += 1
                self.logger.debug(f"🗑️ LRU evicted key: {key_to_evict}")
                
        elif self.eviction_policy == EvictionPolicy.LFU:
            # Remove least frequently used
            min_access_count = min(entry.access_count for entry in self.cache.values())
            key_to_evict = next(
                key for key, entry in self.cache.items() 
                if entry.access_count == min_access_count
            )
            await self.delete(key_to_evict)
            self.evictions += 1
            self.logger.debug(f"🗑️ LFU evicted key: {key_to_evict}")
            
        elif self.eviction_policy == EvictionPolicy.FIFO:
            # Remove oldest entry
            oldest_key = min(self.cache.keys(), key=lambda k: self.cache[k].created_at)
            await self.delete(oldest_key)
            self.evictions += 1
            self.logger.debug(f"🗑️ FIFO evicted key: {oldest_key}")
            
    async def get_stats(self) -> Dict[str, Any]:
        """
        🏴‍☠️ GET CACHE PERFORMANCE STATISTICS
        
        Returns detailed cache metrics for monitoring and optimization.
        """
        total_requests = self.hits + self.misses
        hit_rate = (self.hits / total_requests * 100) if total_requests > 0 else 0
        
        return {
            "cache_type": "in_memory",
            "max_size": self.max_size,
            "current_size": len(self.cache),
            "eviction_policy": self.eviction_policy.value,
            "hits": self.hits,
            "misses": self.misses,
            "hit_rate_percent": round(hit_rate, 2),
            "evictions": self.evictions,
            "memory_usage_percent": round(len(self.cache) / self.max_size * 100, 2)
        }

# ============================================================================
# 🏴‍☠️ SECTION 3: DISTRIBUTED CACHE IMPLEMENTATION
# ============================================================================

class OnePieceDistributedCache(OnePieceCacheInterface):
    """
    🏴‍☠️ DISTRIBUTED CACHE FOR ONE PIECE TRADING PLATFORM

    Distributed caching system that spans multiple nodes for high availability.
    Implements consistent hashing for optimal data distribution.

    Patterns used by:
    - Netflix: Distributed caching across 15,000+ servers
    - Instagram: Photo metadata caching across global regions
    - TikTok: Video recommendation caching for billions of users
    """

    def __init__(self, nodes: List[str], replication_factor: int = 2):
        self.nodes = nodes
        self.replication_factor = replication_factor
        self.node_caches = {node: OnePieceInMemoryCache() for node in nodes}
        self.hash_ring = self._build_hash_ring()
        self.logger = logging.getLogger(__name__)

        # Statistics
        self.total_requests = 0
        self.cache_hits = 0
        self.cache_misses = 0
        self.replication_writes = 0

    def _build_hash_ring(self) -> Dict[int, str]:
        """Build consistent hash ring for node selection"""
        hash_ring = {}

        # Add multiple virtual nodes per physical node for better distribution
        virtual_nodes_per_node = 150

        for node in self.nodes:
            for i in range(virtual_nodes_per_node):
                virtual_node_key = f"{node}:{i}"
                hash_value = hash(virtual_node_key) % (2**32)
                hash_ring[hash_value] = node

        return dict(sorted(hash_ring.items()))

    def _get_nodes_for_key(self, key: str) -> List[str]:
        """Get nodes responsible for storing a key"""
        key_hash = hash(key) % (2**32)

        # Find the first node in the ring >= key_hash
        selected_nodes = []
        ring_keys = list(self.hash_ring.keys())

        start_index = 0
        for i, ring_key in enumerate(ring_keys):
            if ring_key >= key_hash:
                start_index = i
                break

        # Select nodes for replication
        for i in range(self.replication_factor):
            node_index = (start_index + i) % len(ring_keys)
            ring_key = ring_keys[node_index]
            node = self.hash_ring[ring_key]

            if node not in selected_nodes:
                selected_nodes.append(node)

        return selected_nodes[:self.replication_factor]

    async def get(self, key: str) -> Optional[Any]:
        """Get value from distributed cache"""
        self.total_requests += 1

        nodes = self._get_nodes_for_key(key)

        # Try to get from each replica node
        for node in nodes:
            cache = self.node_caches[node]
            value = await cache.get(key)

            if value is not None:
                self.cache_hits += 1
                self.logger.debug(f"🎯 Cache hit for {key} on node {node}")
                return value

        self.cache_misses += 1
        self.logger.debug(f"❌ Cache miss for {key}")
        return None

    async def set(self, key: str, value: Any, ttl_seconds: Optional[int] = None):
        """Set value in distributed cache with replication"""
        nodes = self._get_nodes_for_key(key)

        # Write to all replica nodes
        for node in nodes:
            cache = self.node_caches[node]
            await cache.set(key, value, ttl_seconds)
            self.replication_writes += 1

        self.logger.debug(f"💾 Stored {key} on nodes: {nodes}")

    async def delete(self, key: str):
        """Delete value from distributed cache"""
        nodes = self._get_nodes_for_key(key)

        # Delete from all replica nodes
        for node in nodes:
            cache = self.node_caches[node]
            await cache.delete(key)

        self.logger.debug(f"🗑️ Deleted {key} from nodes: {nodes}")

    async def get_stats(self) -> Dict[str, Any]:
        """Get distributed cache statistics"""
        total_requests = self.total_requests
        hit_rate = (self.cache_hits / total_requests * 100) if total_requests > 0 else 0

        # Aggregate node statistics
        node_stats = {}
        total_size = 0
        total_capacity = 0

        for node, cache in self.node_caches.items():
            stats = await cache.get_stats()
            node_stats[node] = stats
            total_size += stats["current_size"]
            total_capacity += stats["max_size"]

        return {
            "cache_type": "distributed",
            "total_nodes": len(self.nodes),
            "replication_factor": self.replication_factor,
            "total_requests": total_requests,
            "cache_hits": self.cache_hits,
            "cache_misses": self.cache_misses,
            "hit_rate_percent": round(hit_rate, 2),
            "replication_writes": self.replication_writes,
            "total_size": total_size,
            "total_capacity": total_capacity,
            "utilization_percent": round(total_size / total_capacity * 100, 2) if total_capacity > 0 else 0,
            "node_stats": node_stats
        }

# ============================================================================
# 🏴‍☠️ SECTION 4: MULTI-LEVEL CACHE MANAGER
# ============================================================================

class OnePieceMultiLevelCache:
    """
    🏴‍☠️ MULTI-LEVEL CACHE MANAGER FOR ONE PIECE TRADING

    Implements a complete multi-level caching hierarchy:
    1. L1: In-memory cache (fastest, smallest)
    2. L2: Distributed cache (fast, medium size)
    3. L3: Database cache (slower, largest)

    Cache hierarchy used by:
    - Netflix: 99.9% cache hit rate across multiple levels
    - Instagram: Photo serving with sub-10ms response times
    - TikTok: Video recommendation caching for instant loading
    """

    def __init__(self):
        # L1 Cache: In-memory (fastest)
        self.l1_cache = OnePieceInMemoryCache(
            max_size=1000,
            eviction_policy=EvictionPolicy.LRU,
            default_ttl=300  # 5 minutes
        )

        # L2 Cache: Distributed (fast, larger)
        self.l2_cache = OnePieceDistributedCache(
            nodes=["node1", "node2", "node3"],
            replication_factor=2
        )

        # L3 Cache: Database simulation (slower, largest)
        self.l3_cache = OnePieceInMemoryCache(
            max_size=10000,
            eviction_policy=EvictionPolicy.LFU,
            default_ttl=3600  # 1 hour
        )

        self.logger = logging.getLogger(__name__)

        # Performance tracking
        self.l1_hits = 0
        self.l2_hits = 0
        self.l3_hits = 0
        self.cache_misses = 0

    async def get(self, key: str) -> Optional[Any]:
        """
        🏴‍☠️ GET VALUE FROM MULTI-LEVEL CACHE

        Implements cache hierarchy with automatic promotion:
        1. Check L1 cache first (fastest)
        2. If miss, check L2 cache and promote to L1
        3. If miss, check L3 cache and promote to L2 and L1
        4. If miss, return None (would fetch from database in production)
        """
        # Try L1 cache first
        value = await self.l1_cache.get(key)
        if value is not None:
            self.l1_hits += 1
            self.logger.debug(f"🎯 L1 cache hit for {key}")
            return value

        # Try L2 cache
        value = await self.l2_cache.get(key)
        if value is not None:
            self.l2_hits += 1
            self.logger.debug(f"🎯 L2 cache hit for {key}")

            # Promote to L1 cache
            await self.l1_cache.set(key, value)
            return value

        # Try L3 cache
        value = await self.l3_cache.get(key)
        if value is not None:
            self.l3_hits += 1
            self.logger.debug(f"🎯 L3 cache hit for {key}")

            # Promote to L2 and L1 caches
            await self.l2_cache.set(key, value)
            await self.l1_cache.set(key, value)
            return value

        # Complete cache miss
        self.cache_misses += 1
        self.logger.debug(f"❌ Complete cache miss for {key}")
        return None

    async def set(self, key: str, value: Any, ttl_seconds: Optional[int] = None):
        """Set value in all cache levels"""
        # Write to all cache levels
        await self.l1_cache.set(key, value, ttl_seconds)
        await self.l2_cache.set(key, value, ttl_seconds)
        await self.l3_cache.set(key, value, ttl_seconds)

        self.logger.debug(f"💾 Stored {key} in all cache levels")

    async def delete(self, key: str):
        """Delete value from all cache levels"""
        await self.l1_cache.delete(key)
        await self.l2_cache.delete(key)
        await self.l3_cache.delete(key)

        self.logger.debug(f"🗑️ Deleted {key} from all cache levels")

    async def get_performance_stats(self) -> Dict[str, Any]:
        """Get comprehensive cache performance statistics"""
        total_requests = self.l1_hits + self.l2_hits + self.l3_hits + self.cache_misses

        if total_requests == 0:
            return {"error": "No cache requests recorded"}

        return {
            "total_requests": total_requests,
            "l1_hits": self.l1_hits,
            "l2_hits": self.l2_hits,
            "l3_hits": self.l3_hits,
            "cache_misses": self.cache_misses,
            "l1_hit_rate": round(self.l1_hits / total_requests * 100, 2),
            "l2_hit_rate": round(self.l2_hits / total_requests * 100, 2),
            "l3_hit_rate": round(self.l3_hits / total_requests * 100, 2),
            "overall_hit_rate": round((total_requests - self.cache_misses) / total_requests * 100, 2),
            "cache_efficiency": {
                "l1_efficiency": "Fastest - sub-millisecond response",
                "l2_efficiency": "Fast - single-digit millisecond response",
                "l3_efficiency": "Medium - tens of milliseconds response",
                "database_fallback": "Slow - hundreds of milliseconds response"
            }
        }

# ============================================================================
# 🏴‍☠️ SECTION 5: COMPLETE CACHING DEMO
# ============================================================================

async def run_multi_level_caching_demo():
    """
    🏴‍☠️ COMPLETE ONE PIECE MULTI-LEVEL CACHING DEMO

    This demo showcases a production-ready caching system with:
    1. Multi-level cache hierarchy (L1, L2, L3)
    2. Automatic cache promotion for hot data
    3. Different eviction policies per level
    4. Comprehensive performance monitoring
    5. Real-time character and trading data caching
    """
    print("🏴‍☠️ Starting One Piece Multi-Level Caching System...")
    print("=" * 80)

    # 1. Initialize Multi-Level Cache
    cache_manager = OnePieceMultiLevelCache()

    print("✅ Initialized multi-level cache hierarchy:")
    print("  🚀 L1 Cache: In-memory (1,000 items, LRU, 5min TTL)")
    print("  ⚡ L2 Cache: Distributed (3 nodes, 2x replication)")
    print("  💾 L3 Cache: Database cache (10,000 items, LFU, 1hr TTL)")

    # 2. Populate Cache with One Piece Data
    print("\n💾 Populating cache with One Piece trading data...")

    # Character bounty data
    character_data = {
        "luffy_bounty": 3000000000,
        "zoro_bounty": 1111000000,
        "nami_bounty": 366000000,
        "sanji_bounty": 1032000000,
        "chopper_bounty": 1000,
        "robin_bounty": 930000000,
        "franky_bounty": 394000000,
        "brook_bounty": 383000000,
        "jinbe_bounty": 1100000000,
        "usopp_bounty": 500000000
    }

    # Trading data
    trading_data = {
        "luffy_last_price": 2900000000,
        "zoro_last_price": 1050000000,
        "nami_last_price": 350000000,
        "market_volume_24h": 15000000000,
        "active_traders": 50000,
        "total_trades_today": 12500
    }

    # User portfolio data
    portfolio_data = {
        "user_001_portfolio": {"luffy": 1, "zoro": 2, "nami": 5, "berries": 1000000000},
        "user_002_portfolio": {"sanji": 3, "chopper": 10, "robin": 1, "berries": 500000000},
        "user_003_portfolio": {"franky": 2, "brook": 4, "jinbe": 1, "berries": 750000000}
    }

    # Store all data in cache
    all_data = {**character_data, **trading_data, **portfolio_data}

    for key, value in all_data.items():
        await cache_manager.set(key, value)

    print(f"  📊 Stored {len(all_data)} items in cache")

    # 3. Simulate Cache Access Patterns
    print("\n🔍 Simulating realistic cache access patterns...")

    # Hot data (frequently accessed)
    hot_keys = ["luffy_bounty", "zoro_bounty", "market_volume_24h", "active_traders"]

    # Warm data (occasionally accessed)
    warm_keys = ["nami_bounty", "sanji_bounty", "luffy_last_price", "total_trades_today"]

    # Cold data (rarely accessed)
    cold_keys = ["chopper_bounty", "brook_bounty", "user_003_portfolio"]

    # Simulate access patterns
    access_patterns = [
        (hot_keys, 50, "🔥 Hot data access"),
        (warm_keys, 20, "🌡️ Warm data access"),
        (cold_keys, 5, "❄️ Cold data access"),
        (hot_keys, 30, "🔥 Hot data re-access")  # Re-access hot data
    ]

    for keys, access_count, description in access_patterns:
        print(f"\n  {description} ({access_count} requests)...")

        for _ in range(access_count):
            key = random.choice(keys)
            value = await cache_manager.get(key)

            if value is not None:
                # Simulate some processing time
                await asyncio.sleep(0.001)

    # 4. Test Cache Miss Scenario
    print("\n❌ Testing cache miss scenarios...")

    missing_keys = ["unknown_character", "invalid_user", "non_existent_data"]

    for key in missing_keys:
        value = await cache_manager.get(key)
        if value is None:
            print(f"  ❌ Cache miss for {key} (expected)")

    # 5. Display Performance Statistics
    print("\n📈 Cache Performance Analysis:")
    print("-" * 50)

    perf_stats = await cache_manager.get_performance_stats()

    print(f"  📊 Total Requests: {perf_stats['total_requests']}")
    print(f"  🚀 L1 Hits: {perf_stats['l1_hits']} ({perf_stats['l1_hit_rate']}%)")
    print(f"  ⚡ L2 Hits: {perf_stats['l2_hits']} ({perf_stats['l2_hit_rate']}%)")
    print(f"  💾 L3 Hits: {perf_stats['l3_hits']} ({perf_stats['l3_hit_rate']}%)")
    print(f"  ❌ Cache Misses: {perf_stats['cache_misses']}")
    print(f"  🎯 Overall Hit Rate: {perf_stats['overall_hit_rate']}%")

    # 6. Display Individual Cache Statistics
    print(f"\n📊 Individual Cache Level Statistics:")
    print("-" * 50)

    l1_stats = await cache_manager.l1_cache.get_stats()
    l2_stats = await cache_manager.l2_cache.get_stats()
    l3_stats = await cache_manager.l3_cache.get_stats()

    print(f"  🚀 L1 Cache (In-Memory):")
    print(f"    📊 Size: {l1_stats['current_size']}/{l1_stats['max_size']}")
    print(f"    🎯 Hit Rate: {l1_stats['hit_rate_percent']}%")
    print(f"    🗑️ Evictions: {l1_stats['evictions']}")

    print(f"  ⚡ L2 Cache (Distributed):")
    print(f"    📊 Nodes: {l2_stats['total_nodes']}")
    print(f"    🎯 Hit Rate: {l2_stats['hit_rate_percent']}%")
    print(f"    🔄 Replication: {l2_stats['replication_factor']}x")

    print(f"  💾 L3 Cache (Database):")
    print(f"    📊 Size: {l3_stats['current_size']}/{l3_stats['max_size']}")
    print(f"    🎯 Hit Rate: {l3_stats['hit_rate_percent']}%")
    print(f"    📈 Utilization: {l3_stats['memory_usage_percent']}%")

    print("\n🎉 Multi-level caching demo completed successfully!")
    print("🏴‍☠️ Your One Piece platform now has Netflix-level caching performance! ⚔️")

if __name__ == "__main__":
    # Configure logging
    logging.basicConfig(
        level=logging.INFO,
        format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
    )

    print("🏴‍☠️ ONE PIECE TRADING PLATFORM - MULTI-LEVEL CACHING MASTERY")
    print("=" * 80)
    print("📚 Learning Objectives:")
    print("  ✅ Multi-level cache hierarchy design")
    print("  ✅ Cache promotion and demotion strategies")
    print("  ✅ Different eviction policies per cache level")
    print("  ✅ Distributed caching with consistent hashing")
    print("  ✅ Cache performance monitoring and optimization")
    print("  ✅ Production-ready caching patterns")
    print("\n🚀 Starting multi-level caching demonstration...")

    # Run the complete demo
    asyncio.run(run_multi_level_caching_demo())
