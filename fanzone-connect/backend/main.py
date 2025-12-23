from fastapi import FastAPI
from fastapi import Depends, HTTPException, FastAPI
from sqlalchemy.orm import Session 
from fastapi.middleware.cors import CORSMiddleware    

from backend.metrics.prometheus import setup_metrics
from backend.cache.redis_client import redis_client
from backend.db.base import get_db
from sqlalchemy import text

from backend.api import health
from backend.api import users
from backend.db.base import Base, engine
from backend.db import user_model  # import your models so they're registered

app = FastAPI()

setup_metrics(app)

# Create tables at startup
Base.metadata.create_all(bind=engine)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True, 
    allow_methods=["*"], 
    allow_headers=["*"]
)



app.include_router(health.router)
app.include_router(users.router)

