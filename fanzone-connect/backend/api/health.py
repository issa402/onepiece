from fastapi import APIRouter, Depends, HTTPException    
from sqlalchemy.orm import Session  
from sqlalchemy.orm import text   

from backend.db.base import get__db  
from backend.cache.redis_client import redis_client     

router = APIRouter()

@router.get("/health")
async def health(db:Session = Depends(get_db)):
    try:   
        db.execute(text("SELECT1"))   
        redis_client.ping() 
        return {"status": "healthy"} 
    except Exception as e:   
        raise HTTPException(status_code = 500, detail = str(e))