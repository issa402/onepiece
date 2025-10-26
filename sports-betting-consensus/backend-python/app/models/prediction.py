"""
📊 Database models for sports betting predictions

This module defines SQLAlchemy models for storing:
- Games and match information
- Betting predictions from various sources
- Consensus calculations and recommendations
- Historical accuracy tracking
"""

from sqlalchemy import Column, Integer, String, Float, DateTime, Boolean, Text, ForeignKey, JSON, Enum
from sqlalchemy.orm import relationship
from sqlalchemy.sql import func
from datetime import datetime
import enum
from typing import Optional, Dict, Any

from app.core.database import Base

class SportType(str, enum.Enum):
    """Supported sports types"""
    NBA = "nba"
    NFL = "nfl"
    MLB = "mlb"
    NHL = "nhl"
    SOCCER = "soccer"
    TENNIS = "tennis"
    COLLEGE_BASKETBALL = "college_basketball"
    COLLEGE_FOOTBALL = "college_football"

class PredictionType(str, enum.Enum):
    """Types of predictions"""
    WINNER = "winner"
    SPREAD = "spread"
    OVER_UNDER = "over_under"
    MONEYLINE = "moneyline"

class SourceReliability(str, enum.Enum):
    """Source reliability ratings"""
    HIGH = "high"
    MEDIUM = "medium"
    LOW = "low"
    UNKNOWN = "unknown"

class Game(Base):
    """Game/match information"""
    __tablename__ = "games"
    
    id = Column(Integer, primary_key=True, index=True)
    
    # Game details
    team1 = Column(String(100), nullable=False, index=True)
    team2 = Column(String(100), nullable=False, index=True)
    sport = Column(Enum(SportType), nullable=False, index=True)
    league = Column(String(50), nullable=True)
    season = Column(String(20), nullable=True)
    
    # Scheduling
    game_date = Column(DateTime, nullable=False, index=True)
    venue = Column(String(200), nullable=True)
    home_team = Column(String(100), nullable=True)
    
    # Game status
    is_completed = Column(Boolean, default=False, index=True)
    actual_winner = Column(String(100), nullable=True)
    final_score_team1 = Column(Integer, nullable=True)
    final_score_team2 = Column(Integer, nullable=True)
    
    # Metadata
    external_id = Column(String(100), nullable=True, unique=True)  # ID from sports API
    created_at = Column(DateTime, default=func.now())
    updated_at = Column(DateTime, default=func.now(), onupdate=func.now())
    
    # Relationships
    predictions = relationship("Prediction", back_populates="game", cascade="all, delete-orphan")
    consensus = relationship("Consensus", back_populates="game", uselist=False)
    
    def __repr__(self):
        return f"<Game(id={self.id}, {self.team1} vs {self.team2}, {self.game_date})>"
    
    @property
    def display_name(self) -> str:
        """Human-readable game name"""
        return f"{self.team1} vs {self.team2}"
    
    @property
    def is_upcoming(self) -> bool:
        """Check if game is in the future"""
        return self.game_date > datetime.utcnow()

class Source(Base):
    """Betting prediction sources/websites"""
    __tablename__ = "sources"
    
    id = Column(Integer, primary_key=True, index=True)
    
    # Source details
    name = Column(String(100), nullable=False, unique=True, index=True)
    website_url = Column(String(500), nullable=False)
    display_name = Column(String(100), nullable=False)
    
    # Reliability and weighting
    reliability = Column(Enum(SourceReliability), default=SourceReliability.UNKNOWN)
    weight = Column(Float, default=1.0)  # Weight in consensus calculation
    
    # Performance tracking
    total_predictions = Column(Integer, default=0)
    correct_predictions = Column(Integer, default=0)
    accuracy_rate = Column(Float, default=0.0)
    
    # Scraping configuration
    is_active = Column(Boolean, default=True, index=True)
    scraping_enabled = Column(Boolean, default=True)
    last_scraped_at = Column(DateTime, nullable=True)
    scraping_frequency_minutes = Column(Integer, default=60)
    
    # Technical details
    selector_config = Column(JSON, nullable=True)  # CSS selectors for scraping
    headers_config = Column(JSON, nullable=True)  # HTTP headers for requests
    
    # Metadata
    created_at = Column(DateTime, default=func.now())
    updated_at = Column(DateTime, default=func.now(), onupdate=func.now())
    
    # Relationships
    predictions = relationship("Prediction", back_populates="source")
    
    def __repr__(self):
        return f"<Source(id={self.id}, name={self.name}, accuracy={self.accuracy_rate:.2f})>"
    
    def update_accuracy(self):
        """Update accuracy rate based on correct/total predictions"""
        if self.total_predictions > 0:
            self.accuracy_rate = self.correct_predictions / self.total_predictions
        else:
            self.accuracy_rate = 0.0

class Prediction(Base):
    """Individual predictions from sources"""
    __tablename__ = "predictions"
    
    id = Column(Integer, primary_key=True, index=True)
    
    # Foreign keys
    game_id = Column(Integer, ForeignKey("games.id"), nullable=False, index=True)
    source_id = Column(Integer, ForeignKey("sources.id"), nullable=False, index=True)
    
    # Prediction details
    prediction_type = Column(Enum(PredictionType), nullable=False)
    predicted_winner = Column(String(100), nullable=True)
    predicted_spread = Column(Float, nullable=True)
    predicted_total = Column(Float, nullable=True)  # Over/under
    confidence_score = Column(Float, nullable=True)  # 0.0 to 1.0
    
    # Analysis
    reasoning = Column(Text, nullable=True)
    key_factors = Column(JSON, nullable=True)  # List of factors mentioned
    sentiment_score = Column(Float, nullable=True)  # -1.0 to 1.0
    
    # Scraping metadata
    scraped_at = Column(DateTime, default=func.now(), index=True)
    raw_text = Column(Text, nullable=True)  # Original scraped text
    source_url = Column(String(1000), nullable=True)  # Specific article URL
    
    # Accuracy tracking
    is_correct = Column(Boolean, nullable=True)  # Set after game completion
    accuracy_checked_at = Column(DateTime, nullable=True)
    
    # Metadata
    created_at = Column(DateTime, default=func.now())
    updated_at = Column(DateTime, default=func.now(), onupdate=func.now())
    
    # Relationships
    game = relationship("Game", back_populates="predictions")
    source = relationship("Source", back_populates="predictions")
    
    def __repr__(self):
        return f"<Prediction(id={self.id}, game_id={self.game_id}, source={self.source.name if self.source else 'Unknown'}, winner={self.predicted_winner})>"
    
    def check_accuracy(self):
        """Check if prediction was correct after game completion"""
        if self.game and self.game.is_completed and self.game.actual_winner:
            if self.prediction_type == PredictionType.WINNER:
                self.is_correct = (self.predicted_winner == self.game.actual_winner)
            # Add logic for other prediction types (spread, over/under)
            self.accuracy_checked_at = datetime.utcnow()

class Consensus(Base):
    """Consensus calculations for games"""
    __tablename__ = "consensus"
    
    id = Column(Integer, primary_key=True, index=True)
    
    # Foreign key
    game_id = Column(Integer, ForeignKey("games.id"), nullable=False, unique=True, index=True)
    
    # Consensus results
    predicted_winner = Column(String(100), nullable=False)
    confidence_score = Column(Float, nullable=False)  # 0.0 to 1.0
    consensus_percentage = Column(Float, nullable=False)  # Percentage of sources agreeing
    
    # Source breakdown
    total_sources = Column(Integer, nullable=False)
    sources_agreeing = Column(Integer, nullable=False)
    weighted_score = Column(Float, nullable=False)  # Weighted by source reliability
    
    # Recommendation
    recommendation = Column(String(20), nullable=False)  # "bet", "avoid", "monitor"
    risk_level = Column(String(20), nullable=False)  # "low", "medium", "high"
    
    # Analysis details
    reasoning = Column(Text, nullable=True)
    key_factors = Column(JSON, nullable=True)
    conflicting_opinions = Column(JSON, nullable=True)
    
    # Performance tracking
    is_correct = Column(Boolean, nullable=True)
    actual_confidence = Column(Float, nullable=True)  # How confident we should have been
    
    # Metadata
    calculated_at = Column(DateTime, default=func.now(), index=True)
    ai_analysis_used = Column(Boolean, default=False)
    processing_time_ms = Column(Integer, nullable=True)
    
    # Relationships
    game = relationship("Game", back_populates="consensus")
    
    def __repr__(self):
        return f"<Consensus(id={self.id}, game_id={self.game_id}, winner={self.predicted_winner}, confidence={self.confidence_score:.2f})>"
    
    @property
    def recommendation_strength(self) -> str:
        """Get recommendation strength based on confidence"""
        if self.confidence_score >= 0.8:
            return "strong"
        elif self.confidence_score >= 0.6:
            return "moderate"
        else:
            return "weak"

class UserPrediction(Base):
    """User's own predictions and betting history"""
    __tablename__ = "user_predictions"
    
    id = Column(Integer, primary_key=True, index=True)
    
    # User and game
    user_id = Column(String(100), nullable=False, index=True)  # Will integrate with auth later
    game_id = Column(Integer, ForeignKey("games.id"), nullable=False, index=True)
    
    # User's prediction
    predicted_winner = Column(String(100), nullable=False)
    confidence = Column(Float, nullable=True)
    bet_amount = Column(Float, nullable=True)
    odds = Column(Float, nullable=True)
    
    # Outcome
    is_correct = Column(Boolean, nullable=True)
    profit_loss = Column(Float, nullable=True)
    
    # Metadata
    created_at = Column(DateTime, default=func.now())
    
    def __repr__(self):
        return f"<UserPrediction(id={self.id}, user={self.user_id}, game_id={self.game_id}, winner={self.predicted_winner})>"
