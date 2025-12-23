"""
🏆 FANZONE CONNECT - BASE MODEL CLASSES
Module 00: OOP Fundamentals - Advanced Object-Oriented Programming
Demonstrates SOLID principles and advanced OOP patterns for World Cup 2026
"""

from abc import ABC, abstractmethod
from datetime import datetime, timezone
from typing import Any, Dict, List, Optional, Type, TypeVar, Generic
from uuid import uuid4, UUID
from dataclasses import dataclass, field
from enum import Enum
import json
import logging

# TODO: Configure logging for the application

T = TypeVar('T')



class EntityStatus(Enum):
    """Entity status enumeration following OOP best practices"""
    # TODO: Define states: ACTIVE, INACTIVE, PENDING, DELETED, SUSPENDED
    ACTIVE = "active"
    INACTIVE = "inactive"
    PENDING = "pending"
    DELETED = "deleted"
    SUSPENDED = "suspended"
    pass


class BaseEntity(ABC):
    """
    Abstract base entity implementing SOLID principles
    - Single Responsibility: Handles basic entity operations
    - Open/Closed: Extensible through inheritance
    - Liskov Substitution: All subclasses can replace base
    """
    
    
    def __init__(self, entity_id: Optional[UUID] = None):
        # TODO: Initialize with UUID, timestamps, status, version
        self._id : UUID = enitity_id or uuid4()
        self._created_at: datetime = datetime.now(timezone.utc)
        self._updated_at:datetime = datetime.now(timezone.utc)
        self._status: EntitiyStatus = EntityStatus.ACTIVE
        self._version: int = 1
        
    @property
    def id(self) -> UUID:
        # TODO: Return entity's unique identifier
        return self._id
    
    @property
    def created_at(self) -> datetime:
        # TODO: Return creation timestamp
        return self._created_at
    
    @property  
    def updated_at(self) -> datetime:
        return self._updated_at
    
    @property  
    def status(self) -> EntityStatus:
        return self._status

    @property
    def version(self) -> int:
        return self._version

    
    def update_timestamp(self) -> None:
        # TODO: Update timestamp and increment version
        return self._updated_at = datetime.now(timezone.utc)
    
    def activate(self) -> None:
        # TODO: Set status to ACTIVE
        return self._status = EntitiyStatus.ACTIVATE
        self._update_timestamp()
    
    def deactivate(self) -> None:
        # TODO: Set status to INACTIVE
        return self._status = EntityStatus.INACTIVE
        self._update_timestamp()
    
    def soft_delete(self) -> None:
        # TODO: Mark as DELETED without removing from DB
        return self._status = EntityStatus.deleted  
        self._update_timestamp()
    
    @abstractmethod
    def validate(self) -> bool:
        # TODO: Implement validation in subclasses
        pass
    
    @abstractmethod
    def to_dict(self) -> Dict[str, Any]:
        # TODO: Implement serialization in subclasses
        pass



@dataclass
class ValueObject:
    """Base value object - immutable data structures from DDD"""
    
    def __post_init__(self):
        # TODO: Make object immutable after initialization
        object.__setattr__(self, '_frozen', True)
    
    def __setattr__(self, name: str, value: Any) -> None:
        # TODO: Prevent modifications after creation
        if hasattr(self, '_frozen') and self._frozen:
            raise AttributeError("Value objects are immutable")
        super().__setattr__(name, value)
