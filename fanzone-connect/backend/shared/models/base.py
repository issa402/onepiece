"""
🏆 FANZONE CONNECT - BASE MODEL CLASSES
Module 00: OOP Fundamentals - Advanced Object-Oriented Programming

This module demonstrates SOLID principles and advanced OOP patterns
for the World Cup 2026 fan platform architecture.
"""

from abc import ABC, abstractmethod
from datetime import datetime, timezone
from typing import Any, Dict, List, Optional, Type, TypeVar, Generic
from uuid import uuid4, UUID
from dataclasses import dataclass, field
from enum import Enum
import json
import logging

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

T = TypeVar('T')

class EntityStatus(Enum):
    """Entity status enumeration following OOP best practices"""
    ACTIVE = "active"
    INACTIVE = "inactive"
    PENDING = "pending"
    DELETED = "deleted"
    SUSPENDED = "suspended"

class BaseEntity(ABC):
    """
    Abstract base entity implementing SOLID principles
    - Single Responsibility: Handles basic entity operations
    - Open/Closed: Extensible through inheritance
    - Liskov Substitution: All subclasses can replace base
    - Interface Segregation: Minimal interface
    - Dependency Inversion: Depends on abstractions
    """
    
    def __init__(self, entity_id: Optional[UUID] = None):
        self._id: UUID = entity_id or uuid4()
        self._created_at: datetime = datetime.now(timezone.utc)
        self._updated_at: datetime = datetime.now(timezone.utc)
        self._status: EntityStatus = EntityStatus.ACTIVE
        self._version: int = 1
        
    @property
    def id(self) -> UUID:
        """Entity unique identifier"""
        return self._id
    
    @property
    def created_at(self) -> datetime:
        """Entity creation timestamp"""
        return self._created_at
    
    @property
    def updated_at(self) -> datetime:
        """Entity last update timestamp"""
        return self._updated_at
    
    @property
    def status(self) -> EntityStatus:
        """Entity current status"""
        return self._status
    
    @property
    def version(self) -> int:
        """Entity version for optimistic locking"""
        return self._version
    
    def update_timestamp(self) -> None:
        """Update the entity timestamp"""
        self._updated_at = datetime.now(timezone.utc)
        self._version += 1
    
    def activate(self) -> None:
        """Activate the entity"""
        self._status = EntityStatus.ACTIVE
        self.update_timestamp()
    
    def deactivate(self) -> None:
        """Deactivate the entity"""
        self._status = EntityStatus.INACTIVE
        self.update_timestamp()
    
    def soft_delete(self) -> None:
        """Soft delete the entity"""
        self._status = EntityStatus.DELETED
        self.update_timestamp()
    
    @abstractmethod
    def validate(self) -> bool:
        """Validate entity state - must be implemented by subclasses"""
        pass
    
    @abstractmethod
    def to_dict(self) -> Dict[str, Any]:
        """Convert entity to dictionary - must be implemented by subclasses"""
        pass
    
    def __str__(self) -> str:
        return f"{self.__class__.__name__}(id={self.id}, status={self.status.value})"
    
    def __repr__(self) -> str:
        return self.__str__()

class Repository(Generic[T], ABC):
    """
    Generic repository pattern implementation
    Demonstrates Dependency Inversion Principle
    """
    
    @abstractmethod
    async def create(self, entity: T) -> T:
        """Create a new entity"""
        pass
    
    @abstractmethod
    async def get_by_id(self, entity_id: UUID) -> Optional[T]:
        """Get entity by ID"""
        pass
    
    @abstractmethod
    async def update(self, entity: T) -> T:
        """Update existing entity"""
        pass
    
    @abstractmethod
    async def delete(self, entity_id: UUID) -> bool:
        """Delete entity by ID"""
        pass
    
    @abstractmethod
    async def list_all(self, limit: int = 100, offset: int = 0) -> List[T]:
        """List all entities with pagination"""
        pass

class DomainEvent:
    """
    Domain event for event-driven architecture
    Implements Observer pattern for loose coupling
    """
    
    def __init__(self, event_type: str, entity_id: UUID, data: Dict[str, Any]):
        self.event_id: UUID = uuid4()
        self.event_type: str = event_type
        self.entity_id: UUID = entity_id
        self.data: Dict[str, Any] = data
        self.timestamp: datetime = datetime.now(timezone.utc)
    
    def to_dict(self) -> Dict[str, Any]:
        return {
            "event_id": str(self.event_id),
            "event_type": self.event_type,
            "entity_id": str(self.entity_id),
            "data": self.data,
            "timestamp": self.timestamp.isoformat()
        }
    
    def to_json(self) -> str:
        return json.dumps(self.to_dict())

@dataclass
class ValueObject:
    """
    Base value object for immutable data structures
    Demonstrates value object pattern from DDD
    """
    
    def __post_init__(self):
        # Make the object immutable after initialization
        object.__setattr__(self, '_frozen', True)
    
    def __setattr__(self, name: str, value: Any) -> None:
        if hasattr(self, '_frozen') and self._frozen:
            raise AttributeError(f"Cannot modify immutable value object: {name}")
        super().__setattr__(name, value)

# Example usage demonstrating OOP principles
if __name__ == "__main__":
    logger.info("🏆 FANZONE CONNECT - OOP Fundamentals Demo")
    logger.info("Demonstrating SOLID principles and design patterns")
    logger.info("Ready for World Cup 2026 fan platform development!")
