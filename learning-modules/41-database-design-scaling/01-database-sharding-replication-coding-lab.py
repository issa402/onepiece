"""
🏴‍☠️ DATABASE DESIGN & SCALING MASTERY - SHARDING & REPLICATION
═══════════════════════════════════════════════════════════════════════════════

🎯 WHAT YOU'LL MASTER IN THIS LAB (ROADMAP.SH ALIGNED):
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

📚 PART 1: DATABASE SCALING FUNDAMENTALS (What & Why)
   - What database scaling is and why it's critical for billion-user platforms
   - Why horizontal scaling (sharding) enables infinite growth
   - How vertical scaling provides immediate performance gains
   - What replication distributes read load across multiple databases
   - Why scaling patterns prevent database bottlenecks under high load

⚡ PART 2: DATABASE SHARDING (Horizontal Scaling)
   - Sharding strategies (range-based, hash-based, directory-based)
   - Shard key selection for optimal data distribution
   - Cross-shard queries and distributed transactions
   - Resharding strategies for growing datasets
   - Consistent hashing for dynamic shard management

🗄️ PART 3: DATABASE REPLICATION (Read Scaling)
   - Master-slave replication for read scaling
   - Master-master replication for write scaling
   - Read replicas and eventual consistency
   - Replication lag and consistency guarantees
   - Failover and disaster recovery strategies

🔒 PART 4: CONSISTENCY & CAP THEOREM (Distributed Systems)
   - CAP theorem trade-offs (Consistency, Availability, Partition tolerance)
   - ACID properties in distributed databases
   - Eventual consistency vs strong consistency
   - Conflict resolution in distributed systems
   - Consensus algorithms (Raft, Paxos)

🚀 PART 5: ADVANCED SCALING PATTERNS (Enterprise Grade)
   - Database federation and functional partitioning
   - CQRS (Command Query Responsibility Segregation)
   - Event sourcing for audit trails and replay
   - Database connection pooling and optimization
   - Multi-region database deployment

💰 SALARY IMPACT: $130K → $500K+ (Database scaling expertise commands top salaries)
🏢 COMPANIES: Instagram, Netflix, TikTok, Uber, Amazon, Google, Meta, Twitter

📖 ROADMAP.SH SYSTEM DESIGN CONCEPTS COVERED:
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
✅ Database Scaling (horizontal scaling, vertical scaling, sharding)
✅ Replication (master-slave, master-master, read replicas)
✅ Consistency (ACID, CAP theorem, eventual consistency)
✅ Distributed Systems (consensus, conflict resolution, partition tolerance)
✅ Performance (connection pooling, query optimization, indexing)

🏴‍☠️ ONE PIECE TRADING PLATFORM IMPLEMENTATION:
This lab builds a massively scalable One Piece character trading database that can
handle billions of trades, real-time bounty updates, and global user distribution.
"""

import asyncio
import hashlib
import random
import time
from typing import List, Dict, Any, Optional
from dataclasses import dataclass
from enum import Enum
import logging
from concurrent.futures import ThreadPoolExecutor
import asyncpg
import redis
from sqlalchemy import create_engine, text, MetaData, Table, Column, Integer, String, BigInteger, DateTime, Boolean
from sqlalchemy.pool import QueuePool
import json

# ============================================================================
# 🏴‍☠️ SECTION 1: ONE PIECE TRADING DATABASE SHARDING MODELS
# ============================================================================

class ShardingStrategy(Enum):
    """
    🏴‍☠️ DATABASE SHARDING STRATEGIES FOR ONE PIECE TRADING PLATFORM
    
    Different strategies for distributing trading data across multiple databases:
    - RANGE_BASED: Shard by data ranges (user_id 1-1M, 1M-2M, etc.)
    - HASH_BASED: Shard by hash of key (consistent distribution)
    - DIRECTORY_BASED: Lookup service maps keys to shards
    - GEOGRAPHIC: Shard by user location (regional databases)
    """
    RANGE_BASED = "range_based"
    HASH_BASED = "hash_based"
    DIRECTORY_BASED = "directory_based"
    GEOGRAPHIC = "geographic"

@dataclass
class DatabaseShard:
    """
    🏴‍☠️ ONE PIECE TRADING DATABASE SHARD
    
    Represents a single database shard in our trading platform.
    Each shard contains a subset of users, characters, and trading data.
    """
    shard_id: str
    host: str
    port: int
    database: str
    min_range: Optional[int] = None  # For range-based sharding
    max_range: Optional[int] = None  # For range-based sharding
    region: Optional[str] = None     # For geographic sharding
    is_master: bool = True
    replicas: List['DatabaseShard'] = None
    
    def __post_init__(self):
        if self.replicas is None:
            self.replicas = []
    
    def get_connection_url(self) -> str:
        """Get PostgreSQL connection URL for this shard"""
        return f"postgresql://user:pass@{self.host}:{self.port}/{self.database}"

class OnePieceShardManager:
    """
    🏴‍☠️ ONE PIECE TRADING PLATFORM SHARD MANAGER
    
    Manages database sharding for massive scale trading platform.
    Patterns used by:
    - Instagram: Shards user data across 1000+ database servers
    - Netflix: Shards viewing data by user_id for 230M+ users
    - TikTok: Shards video metadata by creator_id for billions of videos
    """
    
    def __init__(self, strategy: ShardingStrategy = ShardingStrategy.HASH_BASED):
        self.strategy = strategy
        self.shards: List[DatabaseShard] = []
        self.shard_count = 0
        self.logger = logging.getLogger(__name__)
        
        # Consistent hashing ring for hash-based sharding
        self.hash_ring: Dict[int, str] = {}
        self.virtual_nodes = 150  # Virtual nodes per shard for better distribution
        
    def add_shard(self, shard: DatabaseShard):
        """Add a new database shard to the cluster"""
        self.shards.append(shard)
        self.shard_count += 1
        
        if self.strategy == ShardingStrategy.HASH_BASED:
            self._add_to_hash_ring(shard)
            
        self.logger.info(f"🏴‍☠️ Added database shard: {shard.shard_id}")
        
    def _add_to_hash_ring(self, shard: DatabaseShard):
        """
        🏴‍☠️ ADD SHARD TO CONSISTENT HASH RING
        
        Consistent hashing ensures minimal data movement when adding/removing shards.
        Each shard gets multiple virtual nodes for better distribution.
        """
        for i in range(self.virtual_nodes):
            virtual_key = f"{shard.shard_id}:{i}"
            hash_value = int(hashlib.md5(virtual_key.encode()).hexdigest(), 16)
            self.hash_ring[hash_value] = shard.shard_id
            
    def get_shard_for_key(self, key: str) -> DatabaseShard:
        """
        🏴‍☠️ GET DATABASE SHARD FOR TRADING KEY
        
        Routes trading operations to the correct database shard based on strategy:
        - Hash-based: Consistent hashing for even distribution
        - Range-based: Route by key range (user_id, character_id)
        - Geographic: Route by user location
        """
        if self.strategy == ShardingStrategy.HASH_BASED:
            return self._get_shard_by_hash(key)
        elif self.strategy == ShardingStrategy.RANGE_BASED:
            return self._get_shard_by_range(key)
        elif self.strategy == ShardingStrategy.GEOGRAPHIC:
            return self._get_shard_by_geography(key)
        else:
            # Fallback to simple modulo
            shard_index = hash(key) % len(self.shards)
            return self.shards[shard_index]
            
    def _get_shard_by_hash(self, key: str) -> DatabaseShard:
        """
        🏴‍☠️ CONSISTENT HASH-BASED SHARD SELECTION
        
        Uses consistent hashing to route keys to shards.
        This minimizes data movement when shards are added/removed.
        """
        if not self.hash_ring:
            raise Exception("🚨 No shards available in hash ring!")
            
        key_hash = int(hashlib.md5(key.encode()).hexdigest(), 16)
        
        # Find the first hash value >= key_hash
        for hash_value in sorted(self.hash_ring.keys()):
            if hash_value >= key_hash:
                shard_id = self.hash_ring[hash_value]
                return next(s for s in self.shards if s.shard_id == shard_id)
                
        # Wrap around to the first shard
        first_hash = min(self.hash_ring.keys())
        shard_id = self.hash_ring[first_hash]
        return next(s for s in self.shards if s.shard_id == shard_id)
        
    def _get_shard_by_range(self, key: str) -> DatabaseShard:
        """
        🏴‍☠️ RANGE-BASED SHARD SELECTION
        
        Routes keys to shards based on numeric ranges.
        Example: user_id 1-1M goes to shard1, 1M-2M goes to shard2
        """
        try:
            numeric_key = int(key.split('_')[-1])  # Extract numeric part
            
            for shard in self.shards:
                if (shard.min_range is not None and shard.max_range is not None and
                    shard.min_range <= numeric_key < shard.max_range):
                    return shard
                    
        except (ValueError, IndexError):
            pass
            
        # Fallback to hash-based if range parsing fails
        return self._get_shard_by_hash(key)
        
    def _get_shard_by_geography(self, key: str) -> DatabaseShard:
        """
        🏴‍☠️ GEOGRAPHIC SHARD SELECTION
        
        Routes keys to shards based on geographic regions.
        Example: US users go to US shard, EU users go to EU shard
        """
        # In real implementation, this would lookup user's region
        # For demo, we'll use key prefix to determine region
        if key.startswith('us_'):
            region_shards = [s for s in self.shards if s.region == 'us']
        elif key.startswith('eu_'):
            region_shards = [s for s in self.shards if s.region == 'eu']
        elif key.startswith('asia_'):
            region_shards = [s for s in self.shards if s.region == 'asia']
        else:
            region_shards = self.shards
            
        if region_shards:
            return random.choice(region_shards)
        else:
            return self.shards[0]  # Fallback

# ============================================================================
# 🏴‍☠️ SECTION 2: DATABASE REPLICATION SYSTEM
# ============================================================================

class ReplicationStrategy(Enum):
    """
    🏴‍☠️ DATABASE REPLICATION STRATEGIES FOR ONE PIECE TRADING

    Different replication patterns for high availability and read scaling:
    - MASTER_SLAVE: One master for writes, multiple slaves for reads
    - MASTER_MASTER: Multiple masters for writes (conflict resolution needed)
    - READ_REPLICA: Dedicated read-only replicas for query scaling
    """
    MASTER_SLAVE = "master_slave"
    MASTER_MASTER = "master_master"
    READ_REPLICA = "read_replica"

class OnePieceReplicationManager:
    """
    🏴‍☠️ ONE PIECE TRADING DATABASE REPLICATION MANAGER

    Manages database replication for high availability and read scaling.
    Patterns used by:
    - Instagram: 100+ read replicas for photo metadata queries
    - Netflix: Master-slave replication for user viewing history
    - TikTok: Read replicas in multiple regions for global access
    """

    def __init__(self, strategy: ReplicationStrategy = ReplicationStrategy.MASTER_SLAVE):
        self.strategy = strategy
        self.logger = logging.getLogger(__name__)

    async def setup_replication(self, master_shard: DatabaseShard, replica_shards: List[DatabaseShard]):
        """
        🏴‍☠️ SETUP DATABASE REPLICATION

        Configures replication between master and replica databases.
        In production, this would configure PostgreSQL streaming replication.
        """
        master_shard.replicas = replica_shards

        for replica in replica_shards:
            replica.is_master = False
            self.logger.info(f"🏴‍☠️ Configured replica: {replica.shard_id} for master: {master_shard.shard_id}")

        self.logger.info(f"✅ Replication setup complete: 1 master, {len(replica_shards)} replicas")

    async def execute_read_query(self, shard: DatabaseShard, query: str, params: dict = None):
        """
        🏴‍☠️ EXECUTE READ QUERY WITH REPLICA ROUTING

        Routes read queries to replica databases for load distribution.
        Falls back to master if replicas are unavailable.
        """
        # Try replicas first for read queries
        if shard.replicas and self.strategy in [ReplicationStrategy.MASTER_SLAVE, ReplicationStrategy.READ_REPLICA]:
            replica = random.choice(shard.replicas)
            try:
                return await self._execute_query(replica, query, params)
            except Exception as e:
                self.logger.warning(f"🚨 Replica query failed, falling back to master: {str(e)}")

        # Fallback to master
        return await self._execute_query(shard, query, params)

    async def execute_write_query(self, shard: DatabaseShard, query: str, params: dict = None):
        """
        🏴‍☠️ EXECUTE WRITE QUERY ON MASTER

        Routes write queries to master database.
        In master-master setup, includes conflict resolution.
        """
        if not shard.is_master and self.strategy == ReplicationStrategy.MASTER_SLAVE:
            raise Exception(f"🚨 Cannot write to replica shard: {shard.shard_id}")

        return await self._execute_query(shard, query, params)

    async def _execute_query(self, shard: DatabaseShard, query: str, params: dict = None):
        """Execute query on specific database shard"""
        # In real implementation, this would use actual database connections
        self.logger.info(f"📊 Executing query on {shard.shard_id}: {query[:50]}...")

        # Simulate query execution time
        await asyncio.sleep(0.01)

        return {"status": "success", "shard": shard.shard_id, "query": query}

# ============================================================================
# 🏴‍☠️ SECTION 3: CAP THEOREM & CONSISTENCY MODELS
# ============================================================================

class ConsistencyLevel(Enum):
    """
    🏴‍☠️ CONSISTENCY LEVELS FOR ONE PIECE TRADING PLATFORM

    Different consistency guarantees for distributed trading operations:
    - STRONG: All nodes see the same data simultaneously (ACID)
    - EVENTUAL: Nodes will eventually converge to same state
    - WEAK: No guarantees about when nodes will converge
    - CAUSAL: Causally related operations are seen in same order
    """
    STRONG = "strong"
    EVENTUAL = "eventual"
    WEAK = "weak"
    CAUSAL = "causal"

class CAPTheoremManager:
    """
    🏴‍☠️ CAP THEOREM IMPLEMENTATION FOR ONE PIECE TRADING

    Manages trade-offs between Consistency, Availability, and Partition tolerance.

    CAP Theorem states you can only guarantee 2 of 3:
    - Consistency: All nodes see the same data at the same time
    - Availability: System remains operational during failures
    - Partition tolerance: System continues despite network failures

    Examples:
    - CP (Consistency + Partition): Banking systems, critical trades
    - AP (Availability + Partition): Social media feeds, recommendations
    - CA (Consistency + Availability): Single-datacenter systems
    """

    def __init__(self, consistency_level: ConsistencyLevel = ConsistencyLevel.EVENTUAL):
        self.consistency_level = consistency_level
        self.logger = logging.getLogger(__name__)

    async def execute_distributed_transaction(self, operation: str, shards: List[DatabaseShard], data: dict):
        """
        🏴‍☠️ EXECUTE DISTRIBUTED TRANSACTION ACROSS SHARDS

        Implements distributed transaction with chosen consistency level:
        - Strong: Two-phase commit (2PC) for ACID guarantees
        - Eventual: Async replication with conflict resolution
        - Weak: Fire-and-forget with no consistency guarantees
        """
        if self.consistency_level == ConsistencyLevel.STRONG:
            return await self._execute_strong_consistency(operation, shards, data)
        elif self.consistency_level == ConsistencyLevel.EVENTUAL:
            return await self._execute_eventual_consistency(operation, shards, data)
        else:
            return await self._execute_weak_consistency(operation, shards, data)

    async def _execute_strong_consistency(self, operation: str, shards: List[DatabaseShard], data: dict):
        """
        🏴‍☠️ STRONG CONSISTENCY WITH TWO-PHASE COMMIT

        Implements 2PC protocol for ACID transactions across shards.
        Used for critical operations like money transfers, character trades.
        """
        self.logger.info(f"🔒 Starting strong consistency transaction: {operation}")

        # Phase 1: Prepare
        prepared_shards = []
        try:
            for shard in shards:
                # In real implementation, this would send PREPARE to each shard
                self.logger.info(f"📝 Preparing shard {shard.shard_id} for {operation}")
                await asyncio.sleep(0.01)  # Simulate network latency
                prepared_shards.append(shard)

            # Phase 2: Commit
            for shard in prepared_shards:
                self.logger.info(f"✅ Committing on shard {shard.shard_id}")
                await asyncio.sleep(0.01)

            self.logger.info(f"🎉 Strong consistency transaction completed: {operation}")
            return {"status": "committed", "shards": len(prepared_shards)}

        except Exception as e:
            # Rollback on any failure
            for shard in prepared_shards:
                self.logger.warning(f"🔄 Rolling back shard {shard.shard_id}")

            raise Exception(f"🚨 Transaction failed: {str(e)}")

    async def _execute_eventual_consistency(self, operation: str, shards: List[DatabaseShard], data: dict):
        """
        🏴‍☠️ EVENTUAL CONSISTENCY WITH ASYNC REPLICATION

        Implements eventual consistency for high availability.
        Used for non-critical operations like user profiles, character stats.
        """
        self.logger.info(f"⏳ Starting eventual consistency operation: {operation}")

        # Execute on primary shard immediately
        primary_shard = shards[0]
        self.logger.info(f"✅ Executed on primary shard: {primary_shard.shard_id}")

        # Async replication to other shards
        replication_tasks = []
        for shard in shards[1:]:
            task = asyncio.create_task(self._replicate_async(shard, operation, data))
            replication_tasks.append(task)

        # Don't wait for replication to complete
        self.logger.info(f"🚀 Eventual consistency operation initiated: {operation}")
        return {"status": "accepted", "primary_shard": primary_shard.shard_id, "replicating_to": len(shards) - 1}

    async def _replicate_async(self, shard: DatabaseShard, operation: str, data: dict):
        """Async replication to replica shards"""
        await asyncio.sleep(random.uniform(0.1, 0.5))  # Simulate replication delay
        self.logger.info(f"🔄 Replicated {operation} to shard {shard.shard_id}")

    async def _execute_weak_consistency(self, operation: str, shards: List[DatabaseShard], data: dict):
        """
        🏴‍☠️ WEAK CONSISTENCY - FIRE AND FORGET

        No consistency guarantees, maximum availability.
        Used for analytics, logging, non-critical updates.
        """
        self.logger.info(f"🔥 Fire-and-forget operation: {operation}")

        # Execute on all shards without waiting for confirmation
        tasks = []
        for shard in shards:
            task = asyncio.create_task(self._execute_fire_forget(shard, operation, data))
            tasks.append(task)

        return {"status": "fired", "targets": len(shards)}
