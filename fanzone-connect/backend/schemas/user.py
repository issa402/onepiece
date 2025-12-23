from pydantic import BaseModel
from uuid import UUID
from typing import List, Optional  
from datetime import datetime


class UserCreate(BaseModel):
    username: str   
    email : str     
    country_of_origin: Optional[str] = None      
    cultures: Optional[List[str]] = None

class UserRead(BaseModel):
    id : UUID   
    username:str    
    email:str
    country_of_origin: Optional[str] = None                         
    cultures: Optional[List[str]] = None
    status: str        
    created_at: datetime

class UserUpdate(BaseModel): 
    username: Optional[str] = None  
    email: Optional[str] =None
    country_of_origin: Optional[str] = None   
    cultures: Optional[List[str]] = None

class UserResponse(BaseModel):
    id : UUID     
    username : str      
    email : str     
    country_of_origin : Optional[str] = None    
    cultures : Optional[List[str]]= None   

    class Config:  
        from_attributes = True
        orm_mode = True