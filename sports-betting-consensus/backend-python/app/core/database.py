# ============================================================================
# 📚 LEARNING GUIDE: Database Configuration & Session Management (app/core/database.py)
# ============================================================================
#
# 🎯 PURPOSE:
# This database module is the foundation of your application's data persistence layer.
# It establishes and manages connections to PostgreSQL, handles session lifecycle,
# provides connection pooling for performance, and offers utilities for database
# operations. This module implements the Repository pattern and ensures proper
# resource management for database connections.
#
# Key responsibilities:
# - Database engine configuration with connection pooling
# - SQLAlchemy session factory and dependency injection
# - Database health checks and connection monitoring
# - Transaction management and rollback handling
# - Database migration support and schema management
# - Connection lifecycle management for optimal performance
#
# 🔧 TECHNOLOGIES USED:
# - SQLAlchemy: Python SQL toolkit and Object-Relational Mapping (ORM)
# - PostgreSQL: Production-grade relational database
# - Connection Pooling: Efficient database connection management
# - Dependency Injection: FastAPI's dependency system for session management
# - Context Managers: Proper resource cleanup and transaction handling
# - Async Support: Non-blocking database operations (optional)
#
# 📖 IN-DEPTH EXPLANATION:
#
# **Why SQLAlchemy over raw SQL?**
# Raw SQL approach:
# ```python
# import psycopg2
# conn = psycopg2.connect("postgresql://...")
# cursor = conn.cursor()
# cursor.execute("SELECT * FROM predictions WHERE game_id = %s", (game_id,))
# ```
# Problems: SQL injection risks, no type safety, manual connection management
#
# SQLAlchemy ORM approach:
# ```python
# from sqlalchemy.orm import Session
# predictions = session.query(Prediction).filter(Prediction.game_id == game_id).all()
# ```
# Benefits: Type safety, automatic SQL generation, relationship handling, security
#
# **Database Connection Patterns:**
# 1. **Connection per Request**: Create new connection for each HTTP request
# 2. **Connection Pooling**: Reuse connections from a pool (recommended)
# 3. **Persistent Connections**: Long-lived connections (for specific use cases)
#
# **Session Management Strategies:**
# - **Session per Request**: Most common pattern for web applications
# - **Session per Thread**: For multi-threaded applications
# - **Session per Transaction**: For complex business operations
#
# **Connection Pool Configuration:**
# - **pool_size**: Number of persistent connections to maintain
# - **max_overflow**: Additional connections beyond pool_size
# - **pool_timeout**: Time to wait for available connection
# - **pool_recycle**: Time before recreating connections
#
# **Transaction Management:**
# ```python
# try:
#     session.add(new_prediction)
#     session.commit()
# except Exception:
#     session.rollback()
#     raise
# finally:
#     session.close()
# ```
#
# **Database Health Monitoring:**
# - Connection pool status monitoring
# - Query performance tracking
# - Connection leak detection
# - Database availability checks
#
# 📚 LEARNING MODULE REFERENCES:
# - Module 33 (Java Spring Boot): Lines 700-900 - Database integration patterns
# - Module 34 (TypeScript/Node.js): Lines 1000-1200 - Database connection management
# - Module 35 (React/Next.js): Lines 300-500 - API integration with databases
#
# ✅ IMPLEMENTATION CHECKLIST:
# [ ] Configure SQLAlchemy engine with proper connection settings
# [ ] Set up connection pooling for optimal performance
# [ ] Create session factory with proper configuration
# [ ] Implement dependency injection for FastAPI integration
# [ ] Add database health check functionality
# [ ] Create database initialization and migration support
# [ ] Implement proper error handling and logging
# [ ] Add connection monitoring and metrics
# [ ] Create database utilities for common operations
# [ ] Add support for read/write database splitting (if needed)
#
# 🎓 WHAT YOU NEED TO LEARN/UNDERSTAND:
# - SQLAlchemy Core vs ORM differences and use cases
# - Database connection pooling concepts and configuration
# - Transaction management and ACID properties
# - Database session lifecycle and best practices
# - SQL injection prevention and security considerations
# - Database performance optimization techniques
# - Connection leak detection and prevention
# - Database migration strategies and tools
#
# 🚀 REAL-WORLD EXAMPLES:
# - Instagram: SQLAlchemy for handling billions of database operations
# - Reddit: Connection pooling for managing high-traffic loads
# - Dropbox: Database session management for file metadata
# - Netflix: Database connection optimization for streaming metadata
#
# ============================================================================

"""
📊 Database configuration and session management

This module sets up SQLAlchemy database connections, session management,
and provides utilities for database operations.
"""

from sqlalchemy import create_engine, MetaData
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, Session
from sqlalchemy.pool import StaticPool
import logging
from typing import Generator

from app.core.config import settings

logger = logging.getLogger(__name__)

# Database engine configuration
if settings.DATABASE_URL.startswith("sqlite"):
    # SQLite configuration for development/testing
    engine = create_engine(
        settings.DATABASE_URL,
        connect_args={"check_same_thread": False},
        poolclass=StaticPool,
        echo=settings.DEBUG
    )
else:
    # PostgreSQL configuration for production
    engine = create_engine(
        settings.DATABASE_URL,
        pool_pre_ping=True,
        pool_recycle=300,
        pool_size=10,
        max_overflow=20,
        echo=settings.DEBUG
    )

# Session factory
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Base class for models
Base = declarative_base()

# Metadata for migrations
metadata = MetaData()

def get_db() -> Generator[Session, None, None]:
    """
    Database dependency for FastAPI endpoints.
    
    Yields:
        Session: SQLAlchemy database session
    """
    db = SessionLocal()
    try:
        yield db
    except Exception as e:
        logger.error(f"Database session error: {e}")
        db.rollback()
        raise
    finally:
        db.close()

def create_tables():
    """Create all database tables"""
    try:
        Base.metadata.create_all(bind=engine)
        logger.info("✅ Database tables created successfully")
    except Exception as e:
        logger.error(f"❌ Failed to create database tables: {e}")
        raise

def drop_tables():
    """Drop all database tables (use with caution!)"""
    try:
        Base.metadata.drop_all(bind=engine)
        logger.info("🗑️ Database tables dropped successfully")
    except Exception as e:
        logger.error(f"❌ Failed to drop database tables: {e}")
        raise

def check_database_connection() -> bool:
    """
    Check if database connection is working.
    
    Returns:
        bool: True if connection is successful, False otherwise
    """
    try:
        with engine.connect() as connection:
            connection.execute("SELECT 1")
        logger.info("✅ Database connection successful")
        return True
    except Exception as e:
        logger.error(f"❌ Database connection failed: {e}")
        return False

class DatabaseManager:
    """Database management utilities"""
    
    @staticmethod
    def get_session() -> Session:
        """Get a new database session"""
        return SessionLocal()
    
    @staticmethod
    def execute_raw_sql(sql: str, params: dict = None) -> list:
        """
        Execute raw SQL query.
        
        Args:
            sql: SQL query string
            params: Query parameters
            
        Returns:
            list: Query results
        """
        try:
            with engine.connect() as connection:
                result = connection.execute(sql, params or {})
                return result.fetchall()
        except Exception as e:
            logger.error(f"Raw SQL execution failed: {e}")
            raise
    
    @staticmethod
    def get_table_info(table_name: str) -> dict:
        """
        Get information about a database table.
        
        Args:
            table_name: Name of the table
            
        Returns:
            dict: Table information
        """
        try:
            with engine.connect() as connection:
                # Get column information
                if settings.DATABASE_URL.startswith("postgresql"):
                    sql = """
                    SELECT column_name, data_type, is_nullable, column_default
                    FROM information_schema.columns
                    WHERE table_name = :table_name
                    ORDER BY ordinal_position
                    """
                else:
                    # SQLite
                    sql = f"PRAGMA table_info({table_name})"
                
                result = connection.execute(sql, {"table_name": table_name})
                columns = result.fetchall()
                
                # Get row count
                count_sql = f"SELECT COUNT(*) FROM {table_name}"
                count_result = connection.execute(count_sql)
                row_count = count_result.scalar()
                
                return {
                    "table_name": table_name,
                    "columns": [dict(row) for row in columns],
                    "row_count": row_count
                }
        except Exception as e:
            logger.error(f"Failed to get table info for {table_name}: {e}")
            raise

# Database health check
async def database_health_check() -> dict:
    """
    Perform database health check.
    
    Returns:
        dict: Health check results
    """
    try:
        # Test connection
        connection_ok = check_database_connection()
        
        # Get basic stats
        with engine.connect() as connection:
            # Check if we can query system tables
            if settings.DATABASE_URL.startswith("postgresql"):
                result = connection.execute(
                    "SELECT COUNT(*) FROM information_schema.tables WHERE table_schema = 'public'"
                )
            else:
                result = connection.execute(
                    "SELECT COUNT(*) FROM sqlite_master WHERE type='table'"
                )
            
            table_count = result.scalar()
        
        return {
            "status": "healthy" if connection_ok else "unhealthy",
            "connection": "ok" if connection_ok else "failed",
            "tables": table_count,
            "engine": str(engine.url).split("@")[0] + "@***"  # Hide credentials
        }
    except Exception as e:
        logger.error(f"Database health check failed: {e}")
        return {
            "status": "unhealthy",
            "error": str(e),
            "connection": "failed"
        }

# Initialize database on import
if __name__ != "__main__":
    try:
        # Test connection on startup
        check_database_connection()
    except Exception as e:
        logger.warning(f"Database connection test failed on startup: {e}")
        logger.info("Database will be initialized when first accessed")
