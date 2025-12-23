from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base  

# If your password contains @, encode it as %40
SQLALCHEMY_DATABASE_URL = "postgresql://isaac:AbrilM23%40@localhost:5432/fanzone"

engine = create_engine(SQLALCHEMY_DATABASE_URL)
SessionLocal = sessionmaker(bind=engine, autocommit=False, autoflush=False)
Base = declarative_base()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

# Optional: test connection separately
try:
    conn = engine.connect()
    print("Connected OK")
    conn.close()
except Exception as e:
    print("Connection failed:", e)
