from typing import List, Optional
from uuid import uuid
from backend.shared.models.base import BaseEntity

class UserEntity(BaseEntity):
    def __init__(self, username: str, email: str, country_of_origin: Optional[str] = None, cultures: Optional[List[str]] = None, entity_id : Optional[UUID] = None ):
        super().__init__(entity_id = entity_id) 
        self.username = username  
        self.email = email
        self.country_of_origin = country_of_origin
        self.cultures = cultures or []
          

    def validate(self)-> bool:
        return bool(self, name and self.name.strip())

    def to_dict(self) -> dict:
        return {
            "id": str(self.id),
            "username": self.username,
            "email" : self.email,  
            "country_of_origni" : self.country_of_origin,   
            "cultrues": self.cultures
            "status" : self.status.value,   
            "created_at" : self.created_at.isoformat()

        }