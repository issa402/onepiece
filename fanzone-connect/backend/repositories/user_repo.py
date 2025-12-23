from sqlalchemy.orm import Session  
from backend.db.user_model import UserModel              
from backend.schemas.user import UserCreate, UserUpdate
from uuid import  UUID
from typing import List, Optional

class UserRepository:
    def __init__(self, db:Session):
        self.db = db 

    def create(self, payload: UserCreate) -> UserModel:
        user = UserModel(**payload.dict())     
        self.db.add(user)     
        self.db.commit()
        self.db.refresh(user)  
        return user

    def get_id(self, user_id:UUID) -> Optional[UserModel]: 
        return self.db.query(UserModel).filter(UserModel.id == user_id).first()
    
    def get_all(self) -> List[UserModel]:   
        return self.db.query(UserModel).all()



    def update(self, user_id: UUID, payload: UserUpdate) -> Optional[UserModel]:
        user = self.get_id(user_id)  
        if not user:
            return None   
        for key, value in payload.dict(exclude_unset = True).items():  
            if value is not None:   
                setattr(user, key, value)
        self.db.commit()  
        self.db.refresh(user)  
        return user
        