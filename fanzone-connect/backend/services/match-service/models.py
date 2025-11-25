"""
🏆 FANZONE CONNECT - MATCH SERVICE MODELS
Learning Modules: 14 (Django vs SQLAlchemy), 03 (Database Design), 41 (Database Scaling)
World Cup 2026 Fan Platform - Match Data Models with Advanced ORM
"""

from datetime import datetime, timezone
from typing import Optional, List, Dict, Any
from enum import Enum
import uuid

from sqlalchemy import Column, String, Integer, DateTime, Boolean, Text, JSON, ForeignKey, Index, CheckConstraint
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship, validates
from sqlalchemy.dialects.postgresql import UUID, ARRAY
from pydantic import BaseModel, validator
import redis

Base = declarative_base()

# =====================================================
# ENUMS FOR WORLD CUP 2026
# =====================================================

class MatchStatus(str, Enum):
    SCHEDULED = "scheduled"
    LIVE = "live"
    HALF_TIME = "half_time"
    FINISHED = "finished"
    POSTPONED = "postponed"
    CANCELLED = "cancelled"

class MatchPhase(str, Enum):
    GROUP_STAGE = "group_stage"
    ROUND_OF_32 = "round_of_32"
    ROUND_OF_16 = "round_of_16"
    QUARTER_FINAL = "quarter_final"
    SEMI_FINAL = "semi_final"
    THIRD_PLACE = "third_place"
    FINAL = "final"

class EventType(str, Enum):
    GOAL = "goal"
    YELLOW_CARD = "yellow_card"
    RED_CARD = "red_card"
    SUBSTITUTION = "substitution"
    PENALTY = "penalty"
    OWN_GOAL = "own_goal"
    VAR_DECISION = "var_decision"

# =====================================================
# SQLALCHEMY MODELS - MODULE 14 & 03
# =====================================================

class Team(Base):
    """World Cup 2026 Team Model with Advanced Features"""
    __tablename__ = "teams"
    
    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    name = Column(String(100), nullable=False, index=True)
    code = Column(String(3), nullable=False, unique=True, index=True)  # FIFA country code
    flag_url = Column(String(255), nullable=False)
    fifa_ranking = Column(Integer, nullable=False, index=True)
    confederation = Column(String(50), nullable=False)  # CONCACAF, UEFA, etc.
    
    # Team statistics
    goals_scored = Column(Integer, default=0)
    goals_conceded = Column(Integer, default=0)
    matches_played = Column(Integer, default=0)
    wins = Column(Integer, default=0)
    draws = Column(Integer, default=0)
    losses = Column(Integer, default=0)
    
    # Social media and fan engagement
    social_media_handles = Column(JSON, default=dict)  # Twitter, Instagram, etc.
    fan_count = Column(Integer, default=0)
    
    # Metadata
    created_at = Column(DateTime(timezone=True), default=datetime.utcnow)
    updated_at = Column(DateTime(timezone=True), default=datetime.utcnow, onupdate=datetime.utcnow)
    
    # Relationships
    home_matches = relationship("Match", foreign_keys="Match.home_team_id", back_populates="home_team")
    away_matches = relationship("Match", foreign_keys="Match.away_team_id", back_populates="away_team")
    
    # Indexes for performance
    __table_args__ = (
        Index('idx_team_ranking', 'fifa_ranking'),
        Index('idx_team_confederation', 'confederation'),
        CheckConstraint('fifa_ranking > 0', name='check_positive_ranking'),
    )
    
    @property
    def goal_difference(self):
        return self.goals_scored - self.goals_conceded
    
    @property
    def points(self):
        return (self.wins * 3) + self.draws

class Venue(Base):
    """World Cup 2026 Venue Model"""
    __tablename__ = "venues"
    
    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    name = Column(String(200), nullable=False, index=True)
    city = Column(String(100), nullable=False, index=True)
    country = Column(String(3), nullable=False)  # USA, CAN, MEX
    capacity = Column(Integer, nullable=False)
    
    # Location data for geospatial queries
    latitude = Column(String(20))
    longitude = Column(String(20))
    timezone = Column(String(50), nullable=False)
    
    # Venue features
    has_roof = Column(Boolean, default=False)
    surface_type = Column(String(50), default="natural_grass")
    
    # Metadata
    created_at = Column(DateTime(timezone=True), default=datetime.utcnow)
    
    # Relationships
    matches = relationship("Match", back_populates="venue")
    
    __table_args__ = (
        Index('idx_venue_city_country', 'city', 'country'),
        CheckConstraint('capacity > 0', name='check_positive_capacity'),
    )

class Match(Base):
    """World Cup 2026 Match Model with Real-time Features"""
    __tablename__ = "matches"
    
    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    
    # Match details
    match_number = Column(Integer, nullable=False, unique=True, index=True)
    phase = Column(String(20), nullable=False, index=True)
    group_name = Column(String(10))  # Group A, B, C, etc. (null for knockout)
    
    # Teams
    home_team_id = Column(UUID(as_uuid=True), ForeignKey('teams.id'), nullable=False, index=True)
    away_team_id = Column(UUID(as_uuid=True), ForeignKey('teams.id'), nullable=False, index=True)
    
    # Venue and timing
    venue_id = Column(UUID(as_uuid=True), ForeignKey('venues.id'), nullable=False, index=True)
    scheduled_datetime = Column(DateTime(timezone=True), nullable=False, index=True)
    actual_start_time = Column(DateTime(timezone=True))
    actual_end_time = Column(DateTime(timezone=True))
    
    # Match status and score
    status = Column(String(20), nullable=False, default=MatchStatus.SCHEDULED, index=True)
    home_score = Column(Integer, default=0)
    away_score = Column(Integer, default=0)
    home_penalty_score = Column(Integer)  # For penalty shootouts
    away_penalty_score = Column(Integer)
    
    # Match statistics
    attendance = Column(Integer)
    referee = Column(String(100))
    weather_conditions = Column(JSON)  # Temperature, humidity, wind, etc.
    
    # Fan engagement metrics
    fan_zone_events_count = Column(Integer, default=0)
    tickets_sold = Column(Integer, default=0)
    social_media_mentions = Column(Integer, default=0)
    
    # Real-time data
    current_minute = Column(Integer, default=0)
    added_time = Column(Integer, default=0)
    is_half_time = Column(Boolean, default=False)
    
    # Metadata
    created_at = Column(DateTime(timezone=True), default=datetime.utcnow)
    updated_at = Column(DateTime(timezone=True), default=datetime.utcnow, onupdate=datetime.utcnow)
    
    # Relationships
    home_team = relationship("Team", foreign_keys=[home_team_id], back_populates="home_matches")
    away_team = relationship("Team", foreign_keys=[away_team_id], back_populates="away_matches")
    venue = relationship("Venue", back_populates="matches")
    events = relationship("MatchEvent", back_populates="match", cascade="all, delete-orphan")
    
    # Advanced indexes for World Cup queries
    __table_args__ = (
        Index('idx_match_datetime_status', 'scheduled_datetime', 'status'),
        Index('idx_match_phase_group', 'phase', 'group_name'),
        Index('idx_match_teams', 'home_team_id', 'away_team_id'),
        Index('idx_match_venue_date', 'venue_id', 'scheduled_datetime'),
        CheckConstraint('home_team_id != away_team_id', name='check_different_teams'),
        CheckConstraint('home_score >= 0', name='check_positive_home_score'),
        CheckConstraint('away_score >= 0', name='check_positive_away_score'),
    )
    
    @property
    def is_live(self):
        return self.status == MatchStatus.LIVE
    
    @property
    def total_goals(self):
        return self.home_score + self.away_score
    
    @property
    def winner_team_id(self):
        if self.status != MatchStatus.FINISHED:
            return None
        if self.home_penalty_score is not None and self.away_penalty_score is not None:
            return self.home_team_id if self.home_penalty_score > self.away_penalty_score else self.away_team_id
        if self.home_score > self.away_score:
            return self.home_team_id
        elif self.away_score > self.home_score:
            return self.away_team_id
        return None  # Draw

class MatchEvent(Base):
    """Real-time Match Events for World Cup 2026"""
    __tablename__ = "match_events"
    
    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    match_id = Column(UUID(as_uuid=True), ForeignKey('matches.id'), nullable=False, index=True)
    
    # Event details
    event_type = Column(String(20), nullable=False, index=True)
    minute = Column(Integer, nullable=False)
    added_time_minute = Column(Integer, default=0)
    
    # Player and team info
    team_id = Column(UUID(as_uuid=True), ForeignKey('teams.id'), nullable=False, index=True)
    player_name = Column(String(100))
    player_number = Column(Integer)
    
    # Additional event data
    description = Column(Text)
    event_data = Column(JSON)  # Flexible data for different event types
    
    # Metadata
    created_at = Column(DateTime(timezone=True), default=datetime.utcnow, index=True)
    
    # Relationships
    match = relationship("Match", back_populates="events")
    team = relationship("Team")
    
    __table_args__ = (
        Index('idx_event_match_minute', 'match_id', 'minute'),
        Index('idx_event_type_team', 'event_type', 'team_id'),
        CheckConstraint('minute >= 0', name='check_positive_minute'),
        CheckConstraint('added_time_minute >= 0', name='check_positive_added_time'),
    )

# =====================================================
# PYDANTIC MODELS FOR API VALIDATION
# =====================================================

class TeamResponse(BaseModel):
    """Team API response model"""
    id: str
    name: str
    code: str
    flag_url: str
    fifa_ranking: int
    confederation: str
    goals_scored: int
    goals_conceded: int
    matches_played: int
    wins: int
    draws: int
    losses: int
    points: int
    goal_difference: int
    fan_count: int
    
    class Config:
        from_attributes = True

class VenueResponse(BaseModel):
    """Venue API response model"""
    id: str
    name: str
    city: str
    country: str
    capacity: int
    latitude: Optional[str]
    longitude: Optional[str]
    timezone: str
    has_roof: bool
    surface_type: str
    
    class Config:
        from_attributes = True

class MatchEventResponse(BaseModel):
    """Match event API response model"""
    id: str
    event_type: str
    minute: int
    added_time_minute: int
    team_id: str
    player_name: Optional[str]
    player_number: Optional[int]
    description: Optional[str]
    created_at: datetime
    
    class Config:
        from_attributes = True

class MatchResponse(BaseModel):
    """Match API response model"""
    id: str
    match_number: int
    phase: str
    group_name: Optional[str]
    home_team: TeamResponse
    away_team: TeamResponse
    venue: VenueResponse
    scheduled_datetime: datetime
    actual_start_time: Optional[datetime]
    status: str
    home_score: int
    away_score: int
    home_penalty_score: Optional[int]
    away_penalty_score: Optional[int]
    attendance: Optional[int]
    referee: Optional[str]
    current_minute: int
    added_time: int
    is_half_time: bool
    fan_zone_events_count: int
    tickets_sold: int
    events: List[MatchEventResponse] = []
    
    class Config:
        from_attributes = True
    
    @validator('scheduled_datetime', pre=True)
    def parse_datetime(cls, v):
        if isinstance(v, str):
            return datetime.fromisoformat(v.replace('Z', '+00:00'))
        return v

class MatchCreate(BaseModel):
    """Match creation model"""
    match_number: int
    phase: MatchPhase
    group_name: Optional[str]
    home_team_id: str
    away_team_id: str
    venue_id: str
    scheduled_datetime: datetime
    referee: Optional[str]
    
    @validator('home_team_id', 'away_team_id', 'venue_id')
    def validate_uuid(cls, v):
        try:
            uuid.UUID(v)
            return v
        except ValueError:
            raise ValueError('Invalid UUID format')

class MatchUpdate(BaseModel):
    """Match update model"""
    status: Optional[MatchStatus]
    home_score: Optional[int]
    away_score: Optional[int]
    current_minute: Optional[int]
    added_time: Optional[int]
    is_half_time: Optional[bool]
    attendance: Optional[int]
    actual_start_time: Optional[datetime]
    actual_end_time: Optional[datetime]

# =====================================================
# REDIS CACHE MODELS - MODULE 41 (DATABASE SCALING)
# =====================================================

class MatchCache:
    """Redis caching for World Cup match data"""
    
    def __init__(self, redis_client: redis.Redis):
        self.redis = redis_client
        self.cache_ttl = 300  # 5 minutes for live matches
        self.static_ttl = 3600  # 1 hour for finished matches
    
    def get_cache_key(self, match_id: str, data_type: str = "match") -> str:
        return f"worldcup2026:{data_type}:{match_id}"
    
    async def cache_match(self, match: MatchResponse):
        """Cache match data with appropriate TTL"""
        cache_key = self.get_cache_key(match.id)
        ttl = self.cache_ttl if match.status == MatchStatus.LIVE else self.static_ttl
        
        await self.redis.setex(
            cache_key,
            ttl,
            match.json()
        )
    
    async def get_cached_match(self, match_id: str) -> Optional[MatchResponse]:
        """Retrieve cached match data"""
        cache_key = self.get_cache_key(match_id)
        cached_data = await self.redis.get(cache_key)
        
        if cached_data:
            return MatchResponse.parse_raw(cached_data)
        return None
    
    async def invalidate_match_cache(self, match_id: str):
        """Invalidate match cache when data changes"""
        cache_key = self.get_cache_key(match_id)
        await self.redis.delete(cache_key)
