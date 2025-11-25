"""
🏆 FANZONE CONNECT - CQRS EVENT SOURCING
Learning Modules: 24 (Event Sourcing CQRS), 42 (Microservices Architecture)
World Cup 2026 Fan Platform - Advanced Event Sourcing with CQRS Pattern
"""

import asyncio
import logging
from datetime import datetime, timezone
from typing import Dict, List, Optional, Any, Union
from abc import ABC, abstractmethod
from dataclasses import dataclass, field
from enum import Enum
import json
import uuid
from collections import defaultdict

import redis.asyncio as redis
from pydantic import BaseModel, Field
import asyncpg

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# =====================================================
# MODULE 24: EVENT SOURCING CQRS - CORE PATTERNS
# =====================================================

class EventType(str, Enum):
    """World Cup 2026 event types"""
    # Fan events
    FAN_REGISTERED = "fan_registered"
    FAN_JOINED_EVENT = "fan_joined_event"
    FAN_LEFT_EVENT = "fan_left_event"
    FAN_LIKED_MATCH = "fan_liked_match"
    FAN_SHARED_CONTENT = "fan_shared_content"
    
    # Match events
    MATCH_SCHEDULED = "match_scheduled"
    MATCH_STARTED = "match_started"
    MATCH_GOAL_SCORED = "match_goal_scored"
    MATCH_CARD_ISSUED = "match_card_issued"
    MATCH_ENDED = "match_ended"
    
    # Fan Zone events
    FANZONE_EVENT_CREATED = "fanzone_event_created"
    FANZONE_EVENT_UPDATED = "fanzone_event_updated"
    FANZONE_CAPACITY_REACHED = "fanzone_capacity_reached"

@dataclass
class DomainEvent:
    """Base domain event for World Cup 2026 platform"""
    
    event_id: str = field(default_factory=lambda: str(uuid.uuid4()))
    event_type: EventType = field()
    aggregate_id: str = field()
    aggregate_type: str = field()
    event_data: Dict[str, Any] = field()
    event_version: int = field()
    occurred_at: datetime = field(default_factory=lambda: datetime.now(timezone.utc))
    user_id: Optional[str] = field(default=None)
    correlation_id: Optional[str] = field(default=None)
    causation_id: Optional[str] = field(default=None)
    
    def to_dict(self) -> Dict[str, Any]:
        """Convert event to dictionary for storage"""
        return {
            "event_id": self.event_id,
            "event_type": self.event_type.value,
            "aggregate_id": self.aggregate_id,
            "aggregate_type": self.aggregate_type,
            "event_data": self.event_data,
            "event_version": self.event_version,
            "occurred_at": self.occurred_at.isoformat(),
            "user_id": self.user_id,
            "correlation_id": self.correlation_id,
            "causation_id": self.causation_id
        }
    
    @classmethod
    def from_dict(cls, data: Dict[str, Any]) -> 'DomainEvent':
        """Create event from dictionary"""
        return cls(
            event_id=data["event_id"],
            event_type=EventType(data["event_type"]),
            aggregate_id=data["aggregate_id"],
            aggregate_type=data["aggregate_type"],
            event_data=data["event_data"],
            event_version=data["event_version"],
            occurred_at=datetime.fromisoformat(data["occurred_at"]),
            user_id=data.get("user_id"),
            correlation_id=data.get("correlation_id"),
            causation_id=data.get("causation_id")
        )

class EventStore:
    """
    Event Store for World Cup 2026 platform
    Stores all domain events with optimistic concurrency control
    """
    
    def __init__(self, connection_string: str):
        self.connection_string = connection_string
        self.pool = None
        
    async def initialize(self):
        """Initialize PostgreSQL connection pool"""
        self.pool = await asyncpg.create_pool(
            self.connection_string,
            min_size=5,
            max_size=20
        )
        
        # Create events table if not exists
        async with self.pool.acquire() as conn:
            await conn.execute("""
                CREATE TABLE IF NOT EXISTS events (
                    event_id UUID PRIMARY KEY,
                    event_type VARCHAR(100) NOT NULL,
                    aggregate_id UUID NOT NULL,
                    aggregate_type VARCHAR(100) NOT NULL,
                    event_data JSONB NOT NULL,
                    event_version INTEGER NOT NULL,
                    occurred_at TIMESTAMP WITH TIME ZONE NOT NULL,
                    user_id UUID,
                    correlation_id UUID,
                    causation_id UUID,
                    created_at TIMESTAMP WITH TIME ZONE DEFAULT NOW()
                );
                
                CREATE INDEX IF NOT EXISTS idx_events_aggregate 
                ON events (aggregate_id, event_version);
                
                CREATE INDEX IF NOT EXISTS idx_events_type_time 
                ON events (event_type, occurred_at);
                
                CREATE INDEX IF NOT EXISTS idx_events_correlation 
                ON events (correlation_id) WHERE correlation_id IS NOT NULL;
            """)
        
        logger.info("📦 Event Store initialized for World Cup 2026")
    
    async def append_events(
        self, 
        aggregate_id: str, 
        events: List[DomainEvent], 
        expected_version: int
    ) -> bool:
        """
        Append events to the event store with optimistic concurrency control
        """
        async with self.pool.acquire() as conn:
            async with conn.transaction():
                # Check current version
                current_version = await conn.fetchval(
                    "SELECT COALESCE(MAX(event_version), 0) FROM events WHERE aggregate_id = $1",
                    uuid.UUID(aggregate_id)
                )
                
                if current_version != expected_version:
                    logger.error(f"❌ Concurrency conflict: expected {expected_version}, got {current_version}")
                    return False
                
                # Insert events
                for event in events:
                    await conn.execute("""
                        INSERT INTO events (
                            event_id, event_type, aggregate_id, aggregate_type,
                            event_data, event_version, occurred_at, user_id,
                            correlation_id, causation_id
                        ) VALUES ($1, $2, $3, $4, $5, $6, $7, $8, $9, $10)
                    """,
                        uuid.UUID(event.event_id),
                        event.event_type.value,
                        uuid.UUID(event.aggregate_id),
                        event.aggregate_type,
                        json.dumps(event.event_data),
                        event.event_version,
                        event.occurred_at,
                        uuid.UUID(event.user_id) if event.user_id else None,
                        uuid.UUID(event.correlation_id) if event.correlation_id else None,
                        uuid.UUID(event.causation_id) if event.causation_id else None
                    )
                
                logger.info(f"📝 Appended {len(events)} events for aggregate {aggregate_id}")
                return True
    
    async def get_events(
        self, 
        aggregate_id: str, 
        from_version: int = 0
    ) -> List[DomainEvent]:
        """Get events for an aggregate from a specific version"""
        async with self.pool.acquire() as conn:
            rows = await conn.fetch("""
                SELECT event_id, event_type, aggregate_id, aggregate_type,
                       event_data, event_version, occurred_at, user_id,
                       correlation_id, causation_id
                FROM events 
                WHERE aggregate_id = $1 AND event_version > $2
                ORDER BY event_version
            """, uuid.UUID(aggregate_id), from_version)
            
            events = []
            for row in rows:
                events.append(DomainEvent(
                    event_id=str(row['event_id']),
                    event_type=EventType(row['event_type']),
                    aggregate_id=str(row['aggregate_id']),
                    aggregate_type=row['aggregate_type'],
                    event_data=json.loads(row['event_data']),
                    event_version=row['event_version'],
                    occurred_at=row['occurred_at'],
                    user_id=str(row['user_id']) if row['user_id'] else None,
                    correlation_id=str(row['correlation_id']) if row['correlation_id'] else None,
                    causation_id=str(row['causation_id']) if row['causation_id'] else None
                ))
            
            return events
    
    async def get_events_by_type(
        self, 
        event_type: EventType, 
        limit: int = 100
    ) -> List[DomainEvent]:
        """Get events by type for projections"""
        async with self.pool.acquire() as conn:
            rows = await conn.fetch("""
                SELECT event_id, event_type, aggregate_id, aggregate_type,
                       event_data, event_version, occurred_at, user_id,
                       correlation_id, causation_id
                FROM events 
                WHERE event_type = $1
                ORDER BY occurred_at DESC
                LIMIT $2
            """, event_type.value, limit)
            
            events = []
            for row in rows:
                events.append(DomainEvent.from_dict({
                    "event_id": str(row['event_id']),
                    "event_type": row['event_type'],
                    "aggregate_id": str(row['aggregate_id']),
                    "aggregate_type": row['aggregate_type'],
                    "event_data": json.loads(row['event_data']),
                    "event_version": row['event_version'],
                    "occurred_at": row['occurred_at'].isoformat(),
                    "user_id": str(row['user_id']) if row['user_id'] else None,
                    "correlation_id": str(row['correlation_id']) if row['correlation_id'] else None,
                    "causation_id": str(row['causation_id']) if row['causation_id'] else None
                }))
            
            return events

# =====================================================
# AGGREGATE ROOT BASE CLASS
# =====================================================

class AggregateRoot(ABC):
    """Base class for World Cup 2026 aggregates"""
    
    def __init__(self, aggregate_id: str):
        self.aggregate_id = aggregate_id
        self.version = 0
        self.uncommitted_events: List[DomainEvent] = []
    
    def apply_event(self, event: DomainEvent):
        """Apply event to aggregate state"""
        self.version = event.event_version
        self._handle_event(event)
    
    def raise_event(self, event_type: EventType, event_data: Dict[str, Any], user_id: str = None):
        """Raise a new domain event"""
        event = DomainEvent(
            event_type=event_type,
            aggregate_id=self.aggregate_id,
            aggregate_type=self.__class__.__name__,
            event_data=event_data,
            event_version=self.version + 1,
            user_id=user_id
        )
        
        self.uncommitted_events.append(event)
        self.apply_event(event)
    
    def mark_events_as_committed(self):
        """Mark events as committed after successful persistence"""
        self.uncommitted_events.clear()
    
    @abstractmethod
    def _handle_event(self, event: DomainEvent):
        """Handle specific event types - implemented by concrete aggregates"""
        pass

# =====================================================
# WORLD CUP 2026 AGGREGATES
# =====================================================

class FanAggregate(AggregateRoot):
    """Fan aggregate for World Cup 2026 platform"""
    
    def __init__(self, fan_id: str):
        super().__init__(fan_id)
        self.email = None
        self.username = None
        self.country_code = None
        self.favorite_teams = []
        self.joined_events = []
        self.liked_matches = []
        self.is_active = True
    
    def register_fan(self, email: str, username: str, country_code: str, user_id: str):
        """Register a new World Cup fan"""
        if self.email is not None:
            raise ValueError("Fan already registered")
        
        self.raise_event(
            EventType.FAN_REGISTERED,
            {
                "email": email,
                "username": username,
                "country_code": country_code,
                "registered_at": datetime.now(timezone.utc).isoformat()
            },
            user_id
        )
    
    def join_event(self, event_id: str, event_name: str, user_id: str):
        """Fan joins a World Cup event"""
        if event_id in self.joined_events:
            raise ValueError("Fan already joined this event")
        
        self.raise_event(
            EventType.FAN_JOINED_EVENT,
            {
                "event_id": event_id,
                "event_name": event_name,
                "joined_at": datetime.now(timezone.utc).isoformat()
            },
            user_id
        )
    
    def like_match(self, match_id: str, home_team: str, away_team: str, user_id: str):
        """Fan likes a World Cup match"""
        if match_id in self.liked_matches:
            return  # Already liked
        
        self.raise_event(
            EventType.FAN_LIKED_MATCH,
            {
                "match_id": match_id,
                "home_team": home_team,
                "away_team": away_team,
                "liked_at": datetime.now(timezone.utc).isoformat()
            },
            user_id
        )
    
    def _handle_event(self, event: DomainEvent):
        """Handle fan-specific events"""
        if event.event_type == EventType.FAN_REGISTERED:
            self.email = event.event_data["email"]
            self.username = event.event_data["username"]
            self.country_code = event.event_data["country_code"]
        
        elif event.event_type == EventType.FAN_JOINED_EVENT:
            self.joined_events.append(event.event_data["event_id"])
        
        elif event.event_type == EventType.FAN_LIKED_MATCH:
            self.liked_matches.append(event.event_data["match_id"])

class MatchAggregate(AggregateRoot):
    """Match aggregate for World Cup 2026"""
    
    def __init__(self, match_id: str):
        super().__init__(match_id)
        self.home_team = None
        self.away_team = None
        self.venue = None
        self.scheduled_time = None
        self.status = "scheduled"
        self.home_score = 0
        self.away_score = 0
        self.events = []
    
    def schedule_match(
        self, 
        home_team: str, 
        away_team: str, 
        venue: str, 
        scheduled_time: datetime,
        user_id: str
    ):
        """Schedule a World Cup match"""
        self.raise_event(
            EventType.MATCH_SCHEDULED,
            {
                "home_team": home_team,
                "away_team": away_team,
                "venue": venue,
                "scheduled_time": scheduled_time.isoformat()
            },
            user_id
        )
    
    def start_match(self, user_id: str):
        """Start the match"""
        if self.status != "scheduled":
            raise ValueError("Match cannot be started")
        
        self.raise_event(
            EventType.MATCH_STARTED,
            {
                "started_at": datetime.now(timezone.utc).isoformat()
            },
            user_id
        )
    
    def score_goal(self, team: str, player: str, minute: int, user_id: str):
        """Record a goal in the match"""
        if self.status != "live":
            raise ValueError("Cannot score goal in non-live match")
        
        self.raise_event(
            EventType.MATCH_GOAL_SCORED,
            {
                "team": team,
                "player": player,
                "minute": minute,
                "scored_at": datetime.now(timezone.utc).isoformat()
            },
            user_id
        )
    
    def _handle_event(self, event: DomainEvent):
        """Handle match-specific events"""
        if event.event_type == EventType.MATCH_SCHEDULED:
            self.home_team = event.event_data["home_team"]
            self.away_team = event.event_data["away_team"]
            self.venue = event.event_data["venue"]
            self.scheduled_time = datetime.fromisoformat(event.event_data["scheduled_time"])
        
        elif event.event_type == EventType.MATCH_STARTED:
            self.status = "live"
        
        elif event.event_type == EventType.MATCH_GOAL_SCORED:
            team = event.event_data["team"]
            if team == self.home_team:
                self.home_score += 1
            elif team == self.away_team:
                self.away_score += 1
            
            self.events.append(event.event_data)

# =====================================================
# MODULE 42: MICROSERVICES ARCHITECTURE - REPOSITORY
# =====================================================

class EventSourcedRepository:
    """Repository for event-sourced aggregates"""
    
    def __init__(self, event_store: EventStore):
        self.event_store = event_store
    
    async def get_by_id(self, aggregate_class, aggregate_id: str):
        """Load aggregate from event store"""
        events = await self.event_store.get_events(aggregate_id)
        
        if not events:
            return None
        
        aggregate = aggregate_class(aggregate_id)
        
        for event in events:
            aggregate.apply_event(event)
        
        return aggregate
    
    async def save(self, aggregate: AggregateRoot):
        """Save aggregate changes to event store"""
        if not aggregate.uncommitted_events:
            return True
        
        expected_version = aggregate.version - len(aggregate.uncommitted_events)
        
        success = await self.event_store.append_events(
            aggregate.aggregate_id,
            aggregate.uncommitted_events,
            expected_version
        )
        
        if success:
            aggregate.mark_events_as_committed()
        
        return success

# Example usage
async def main():
    """Example usage of CQRS Event Sourcing for World Cup 2026"""
    
    # Initialize event store
    event_store = EventStore("postgresql://user:pass@localhost/worldcup_events")
    await event_store.initialize()
    
    # Initialize repository
    repository = EventSourcedRepository(event_store)
    
    # Create and register a fan
    fan_id = str(uuid.uuid4())
    fan = FanAggregate(fan_id)
    fan.register_fan("fan@worldcup.com", "worldcupfan", "USA", "admin")
    fan.join_event("event123", "NYC Fan Festival", "admin")
    fan.like_match("match456", "Brazil", "Argentina", "admin")
    
    # Save fan aggregate
    await repository.save(fan)
    
    # Load fan aggregate
    loaded_fan = await repository.get_by_id(FanAggregate, fan_id)
    print(f"🏆 Loaded fan: {loaded_fan.username} from {loaded_fan.country_code}")
    print(f"📊 Joined events: {len(loaded_fan.joined_events)}")
    print(f"❤️ Liked matches: {len(loaded_fan.liked_matches)}")

if __name__ == "__main__":
    asyncio.run(main())
