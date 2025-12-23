from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session   
from backend.schemas.user import UserCreate, UserRead , UserResponse
from backend.repositories.user_repo import UserRepository   
from backend.db.base import get_db
from backend.db.user_model import UserModel
from uuid import UUID  


router = APIRouter(prefix = "/users")

@router.post("", response_model = UserRead)
async def create_user(payload: UserCreate, db: Session = Depends(get_db)):
    repo = UserRepository(db)
    user = repo.create(payload) 
    cultures = user.cultures.split(",") if user.cultures else None
    return UserRead(
        id = user.id, 
        username = user.username,   
        email = user.email, 
        country_of_origin = user.country_of_origin,  
        cultures = cultures,
        status = "active",   
        created_at = user.created_at
    )




@router.get("",  response_model =list[UserResponse])
async def list_user(db: Session = Depends(get_db)):     
    repo = UserRepository(db)
    users = repo.get_all()  
    return users

@router.get("/{user_id}", response_model = UserResponse)
async def get_user(user_id:UUID, db: Session = Depends(get_db)):
    repo = UserRepository(db)  
    user = repo.get_id(user_id)
    if not user:  
        raise HTTPException (status_code = 404, detail = "User not found")
    return user 
    