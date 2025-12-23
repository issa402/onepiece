from sqlalchemy.orm import Session
from backend.db.user_model import UserModel     
from backend.schemas.user import UserCreate 
from abc import ABC, abstractmethod


T = TypeVar("T")
class Repository(Generic[T], ABC):
    """Generic repository pattern for data access - clean architecture"""
    
    @abstractmethod
    async def create(self, entity: T) -> T:
        # TODO: Database insert operation
        pass
    
    @abstractmethod
    async def get_by_id(self, entity_id: UUID) -> Optional[T]:
        # TODO: Database query by ID
        pass
    
    @abstractmethod
    async def update(self, entity: T) -> T:
        # TODO: Database update with optimistic locking
        pass
    
    @abstractmethod
    async def delete(self, entity_id: UUID) -> bool:
        # TODO: Database delete operation
        pass
    
    @abstractmethod
    async def list_all(self, limit: int = 100, offset: int = 0) -> List[T]:
        # TODO: Paginated query for all entities
        pass

