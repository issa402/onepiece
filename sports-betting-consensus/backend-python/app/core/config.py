# ============================================================================
# 📚 LEARNING GUIDE: Application Configuration Management (app/core/config.py)
# ============================================================================
#
# 🎯 PURPOSE:
# This configuration module is the central nervous system of your application.
# It handles all environment-specific settings, secrets, and configuration
# parameters using Pydantic Settings for type safety and validation. This
# approach ensures your application can run consistently across development,
# testing, and production environments while maintaining security best practices.
#
# Key responsibilities:
# - Environment variable management with type validation
# - Database connection configuration
# - API keys and secrets management
# - Service URLs and endpoints configuration
# - Feature flags and application behavior settings
# - Logging and monitoring configuration
#
# 🔧 TECHNOLOGIES USED:
# - Pydantic Settings: Type-safe configuration with automatic validation
# - Environment Variables: 12-factor app configuration methodology
# - Type Hints: Python type system for configuration validation
# - Validators: Custom validation logic for complex configuration
# - Field Definitions: Default values, descriptions, and constraints
#
# 📖 IN-DEPTH EXPLANATION:
#
# **Why Pydantic Settings over os.environ?**
# Traditional approach:
# ```python
# DATABASE_URL = os.environ.get('DATABASE_URL', 'sqlite:///default.db')
# DEBUG = os.environ.get('DEBUG', 'False').lower() == 'true'
# ```
# Problems: No type safety, manual type conversion, no validation
#
# Pydantic Settings approach:
# ```python
# class Settings(BaseSettings):
#     DATABASE_URL: str = Field(env="DATABASE_URL")
#     DEBUG: bool = Field(default=False, env="DEBUG")
# ```
# Benefits: Automatic type conversion, validation, IDE support, documentation
#
# **Configuration Hierarchy (Priority Order):**
# 1. Environment variables (highest priority)
# 2. .env file values
# 3. Default values in Field definitions (lowest priority)
#
# **Environment Variable Naming Convention:**
# - Use UPPERCASE with underscores: DATABASE_URL, OPENAI_API_KEY
# - Group related settings: REDIS_HOST, REDIS_PORT, REDIS_PASSWORD
# - Use descriptive names: SCRAPING_DELAY_SECONDS vs DELAY
#
# **Security Best Practices:**
# - Never commit secrets to version control
# - Use different .env files for different environments
# - Validate required secrets at startup
# - Use secure defaults (e.g., DEBUG=False in production)
#
# **Configuration Validation Patterns:**
# - URL validation for database and service endpoints
# - Range validation for numeric settings (ports, timeouts)
# - Enum validation for categorical settings (log levels, environments)
# - Custom validators for complex business rules
#
# **Real-world Configuration Examples:**
# Netflix: Uses similar patterns for microservice configuration
# Spotify: Environment-based configuration for different deployment stages
# Uber: Type-safe configuration management across thousands of services
#
# 📚 LEARNING MODULE REFERENCES:
# - Module 34 (TypeScript/Node.js): Lines 800-1000 - Environment configuration patterns
# - Module 33 (Java Spring Boot): Lines 300-500 - Application properties management
# - Module 36 (AI/LLM Integration): Lines 200-400 - API key management and security
#
# ✅ IMPLEMENTATION CHECKLIST:
# [ ] Define Settings class inheriting from BaseSettings
# [ ] Add all required configuration fields with proper types
# [ ] Set appropriate default values for development
# [ ] Add Field descriptions and validation constraints
# [ ] Implement custom validators for complex settings
# [ ] Create .env.example file with all required variables
# [ ] Add configuration validation at application startup
# [ ] Document environment-specific configuration differences
# [ ] Implement configuration testing with different environments
# [ ] Add configuration change detection and hot-reloading
#
# 🎓 WHAT YOU NEED TO LEARN/UNDERSTAND:
# - Pydantic BaseSettings class and its capabilities
# - Python type hints and their role in configuration
# - Environment variable best practices and security
# - Configuration validation and error handling
# - The 12-factor app methodology for configuration
# - Secrets management in different environments
# - Configuration testing strategies
# - Environment-specific deployment patterns
#
# 🚀 REAL-WORLD EXAMPLES:
# - FastAPI applications: Pydantic Settings is the standard approach
# - Django: Similar patterns with django-environ
# - Flask: Flask-Config provides similar functionality
# - Microservices: Each service has its own configuration management
#
# 💡 CONFIGURATION CATEGORIES:
# 1. **Application Settings**: Name, version, debug mode
# 2. **Database Settings**: Connection strings, pool sizes, timeouts
# 3. **External Services**: API keys, service URLs, authentication
# 4. **Performance Settings**: Cache sizes, worker counts, timeouts
# 5. **Security Settings**: JWT secrets, encryption keys, CORS settings
# 6. **Feature Flags**: Enable/disable features, A/B testing
#
# 🔐 SECURITY CONSIDERATIONS:
# - Use environment variables for all secrets
# - Validate configuration at startup to fail fast
# - Log configuration (without secrets) for debugging
# - Use different configurations for different environments
# - Implement configuration change auditing
#
# 🔍 DEBUGGING CONFIGURATION:
# - Print non-sensitive configuration at startup
# - Use configuration validation errors for troubleshooting
# - Test configuration loading in isolation
# - Use type hints for IDE support and error detection
#
# ============================================================================

"""
🔧 Configuration settings for the Sports Betting Consensus Aggregator

This module handles all configuration settings using Pydantic Settings
for type safety and validation.
"""

from pydantic_settings import BaseSettings
from pydantic import Field, validator
from typing import List, Optional
import os
from pathlib import Path

class Settings(BaseSettings):
    """Application settings with environment variable support"""
    
    # Application settings
    APP_NAME: str = "Sports Betting Consensus Aggregator"
    APP_VERSION: str = "1.0.0"
    DEBUG: bool = Field(default=False, env="DEBUG")
    
    # API settings
    API_V1_STR: str = "/api/v1"
    ALLOWED_HOSTS: List[str] = Field(
        default=["localhost", "127.0.0.1", "0.0.0.0"],
        env="ALLOWED_HOSTS"
    )
    
    # Database settings
    DATABASE_URL: str = Field(
        default="postgresql://postgres:password@localhost:5432/sports_betting",
        env="DATABASE_URL"
    )
    
    # Redis settings
    REDIS_URL: str = Field(
        default="redis://localhost:6379/0",
        env="REDIS_URL"
    )
    
    # Celery settings
    CELERY_BROKER_URL: str = Field(
        default="redis://localhost:6379/1",
        env="CELERY_BROKER_URL"
    )
    CELERY_RESULT_BACKEND: str = Field(
        default="redis://localhost:6379/2",
        env="CELERY_RESULT_BACKEND"
    )
    
    # AI/LLM API keys
    OPENAI_API_KEY: Optional[str] = Field(default=None, env="OPENAI_API_KEY")
    ANTHROPIC_API_KEY: Optional[str] = Field(default=None, env="ANTHROPIC_API_KEY")
    
    # Web scraping settings
    SCRAPING_DELAY: float = Field(default=2.0, env="SCRAPING_DELAY")
    MAX_CONCURRENT_SCRAPES: int = Field(default=5, env="MAX_CONCURRENT_SCRAPES")
    REQUEST_TIMEOUT: int = Field(default=30, env="REQUEST_TIMEOUT")
    USER_AGENT: str = Field(
        default="Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36",
        env="USER_AGENT"
    )
    
    # Rate limiting
    RATE_LIMIT_PER_MINUTE: int = Field(default=60, env="RATE_LIMIT_PER_MINUTE")
    
    # Security settings
    SECRET_KEY: str = Field(
        default="your-secret-key-change-in-production",
        env="SECRET_KEY"
    )
    ACCESS_TOKEN_EXPIRE_MINUTES: int = Field(default=30, env="ACCESS_TOKEN_EXPIRE_MINUTES")
    
    # Logging settings
    LOG_LEVEL: str = Field(default="INFO", env="LOG_LEVEL")
    LOG_FORMAT: str = Field(
        default="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
        env="LOG_FORMAT"
    )
    
    # Sports betting sites to scrape
    BETTING_SITES: List[str] = Field(
        default=[
            "espn.com",
            "cbssports.com",
            "bleacherreport.com",
            "si.com",
            "theathletic.com"
        ],
        env="BETTING_SITES"
    )
    
    # Background job settings
    SCRAPING_SCHEDULE_MINUTES: int = Field(default=60, env="SCRAPING_SCHEDULE_MINUTES")
    CLEANUP_SCHEDULE_HOURS: int = Field(default=24, env="CLEANUP_SCHEDULE_HOURS")
    
    # Cache settings
    CACHE_TTL_SECONDS: int = Field(default=3600, env="CACHE_TTL_SECONDS")  # 1 hour
    PREDICTION_CACHE_TTL: int = Field(default=1800, env="PREDICTION_CACHE_TTL")  # 30 minutes
    
    # AI analysis settings
    AI_MODEL_TEMPERATURE: float = Field(default=0.3, env="AI_MODEL_TEMPERATURE")
    AI_MAX_TOKENS: int = Field(default=1000, env="AI_MAX_TOKENS")
    AI_TIMEOUT_SECONDS: int = Field(default=30, env="AI_TIMEOUT_SECONDS")
    
    # Monitoring and metrics
    ENABLE_METRICS: bool = Field(default=True, env="ENABLE_METRICS")
    METRICS_PORT: int = Field(default=8001, env="METRICS_PORT")
    
    @validator("ALLOWED_HOSTS", pre=True)
    def parse_allowed_hosts(cls, v):
        """Parse comma-separated allowed hosts"""
        if isinstance(v, str):
            return [host.strip() for host in v.split(",")]
        return v
    
    @validator("BETTING_SITES", pre=True)
    def parse_betting_sites(cls, v):
        """Parse comma-separated betting sites"""
        if isinstance(v, str):
            return [site.strip() for site in v.split(",")]
        return v
    
    @validator("DATABASE_URL")
    def validate_database_url(cls, v):
        """Validate database URL format"""
        if not v.startswith(("postgresql://", "sqlite:///")):
            raise ValueError("DATABASE_URL must start with postgresql:// or sqlite:///")
        return v
    
    @validator("REDIS_URL")
    def validate_redis_url(cls, v):
        """Validate Redis URL format"""
        if not v.startswith("redis://"):
            raise ValueError("REDIS_URL must start with redis://")
        return v
    
    class Config:
        """Pydantic configuration"""
        env_file = ".env"
        env_file_encoding = "utf-8"
        case_sensitive = True

# Create settings instance
settings = Settings()

# Development settings override
if settings.DEBUG:
    settings.LOG_LEVEL = "DEBUG"
    settings.SCRAPING_DELAY = 1.0  # Faster scraping in development
    settings.CACHE_TTL_SECONDS = 300  # Shorter cache in development

# Validate required settings
def validate_settings():
    """Validate critical settings on startup"""
    errors = []
    
    # Check AI API keys
    if not settings.OPENAI_API_KEY and not settings.ANTHROPIC_API_KEY:
        errors.append("At least one AI API key (OPENAI_API_KEY or ANTHROPIC_API_KEY) must be provided")
    
    # Check database URL
    if "localhost" in settings.DATABASE_URL and not settings.DEBUG:
        errors.append("Production DATABASE_URL should not use localhost")
    
    # Check secret key
    if settings.SECRET_KEY == "your-secret-key-change-in-production" and not settings.DEBUG:
        errors.append("SECRET_KEY must be changed in production")
    
    if errors:
        raise ValueError(f"Configuration errors: {'; '.join(errors)}")

# Export commonly used settings
DATABASE_URL = settings.DATABASE_URL
REDIS_URL = settings.REDIS_URL
DEBUG = settings.DEBUG

# ============================================================================
# 📝 REFERENCE IMPLEMENTATION (Check your code against this)
# ============================================================================
#
# """
# Complete Configuration Management Implementation
#
# This reference shows how to implement a production-ready configuration
# system with proper validation, security, and environment management.
# """
#
# from pydantic_settings import BaseSettings
# from pydantic import Field, validator, AnyHttpUrl
# from typing import List, Optional, Union
# import os
# from pathlib import Path
# from enum import Enum
#
# class Environment(str, Enum):
#     """Application environment types"""
#     DEVELOPMENT = "development"
#     TESTING = "testing"
#     STAGING = "staging"
#     PRODUCTION = "production"
#
# class LogLevel(str, Enum):
#     """Logging levels"""
#     DEBUG = "DEBUG"
#     INFO = "INFO"
#     WARNING = "WARNING"
#     ERROR = "ERROR"
#     CRITICAL = "CRITICAL"
#
# class Settings(BaseSettings):
#     """
#     Application settings with comprehensive validation and documentation.
#
#     This class demonstrates best practices for configuration management:
#     - Type safety with Pydantic
#     - Environment variable integration
#     - Validation and error handling
#     - Security considerations
#     - Documentation and examples
#     """
#
#     # ========================================================================
#     # APPLICATION SETTINGS
#     # ========================================================================
#
#     APP_NAME: str = Field(
#         default="Sports Betting Consensus Aggregator",
#         description="Application name for logging and monitoring"
#     )
#
#     APP_VERSION: str = Field(
#         default="1.0.0",
#         description="Application version for API responses and logging"
#     )
#
#     ENVIRONMENT: Environment = Field(
#         default=Environment.DEVELOPMENT,
#         description="Application environment (development, testing, staging, production)"
#     )
#
#     DEBUG: bool = Field(
#         default=False,
#         description="Enable debug mode (should be False in production)"
#     )
#
#     # ========================================================================
#     # API SETTINGS
#     # ========================================================================
#
#     API_V1_STR: str = Field(
#         default="/api/v1",
#         description="API version prefix for all endpoints"
#     )
#
#     ALLOWED_HOSTS: List[str] = Field(
#         default=["localhost", "127.0.0.1", "0.0.0.0"],
#         description="List of allowed hosts for CORS and security"
#     )
#
#     CORS_ORIGINS: List[str] = Field(
#         default=["http://localhost:3000", "http://localhost:8080"],
#         description="Allowed CORS origins for frontend applications"
#     )
#
#     # ========================================================================
#     # DATABASE SETTINGS
#     # ========================================================================
#
#     DATABASE_URL: str = Field(
#         default="postgresql://postgres:password@localhost:5432/sports_betting",
#         description="Database connection URL (PostgreSQL recommended for production)"
#     )
#
#     DATABASE_POOL_SIZE: int = Field(
#         default=10,
#         ge=1,
#         le=50,
#         description="Database connection pool size"
#     )
#
#     DATABASE_MAX_OVERFLOW: int = Field(
#         default=20,
#         ge=0,
#         le=100,
#         description="Maximum database connection overflow"
#     )
#
#     # ========================================================================
#     # REDIS SETTINGS
#     # ========================================================================
#
#     REDIS_URL: str = Field(
#         default="redis://localhost:6379/0",
#         description="Redis connection URL for caching"
#     )
#
#     REDIS_CACHE_TTL: int = Field(
#         default=3600,
#         ge=60,
#         le=86400,
#         description="Default cache TTL in seconds (1 hour default)"
#     )
#
#     # ========================================================================
#     # CELERY SETTINGS
#     # ========================================================================
#
#     CELERY_BROKER_URL: str = Field(
#         default="redis://localhost:6379/1",
#         description="Celery message broker URL"
#     )
#
#     CELERY_RESULT_BACKEND: str = Field(
#         default="redis://localhost:6379/2",
#         description="Celery result backend URL"
#     )
#
#     # ========================================================================
#     # AI/LLM API SETTINGS
#     # ========================================================================
#
#     OPENAI_API_KEY: Optional[str] = Field(
#         default=None,
#         description="OpenAI API key for GPT models (required for AI features)"
#     )
#
#     ANTHROPIC_API_KEY: Optional[str] = Field(
#         default=None,
#         description="Anthropic API key for Claude models (fallback AI provider)"
#     )
#
#     AI_MODEL_TEMPERATURE: float = Field(
#         default=0.1,
#         ge=0.0,
#         le=2.0,
#         description="AI model temperature for prediction analysis"
#     )
#
#     AI_MAX_TOKENS: int = Field(
#         default=1000,
#         ge=100,
#         le=4000,
#         description="Maximum tokens for AI model responses"
#     )
#
#     # ========================================================================
#     # SCRAPING SETTINGS
#     # ========================================================================
#
#     SCRAPING_DELAY_MIN: float = Field(
#         default=1.0,
#         ge=0.1,
#         le=10.0,
#         description="Minimum delay between scraping requests (seconds)"
#     )
#
#     SCRAPING_DELAY_MAX: float = Field(
#         default=3.0,
#         ge=1.0,
#         le=30.0,
#         description="Maximum delay between scraping requests (seconds)"
#     )
#
#     SCRAPING_TIMEOUT: int = Field(
#         default=30,
#         ge=5,
#         le=120,
#         description="HTTP request timeout for scraping (seconds)"
#     )
#
#     SCRAPING_MAX_RETRIES: int = Field(
#         default=3,
#         ge=1,
#         le=10,
#         description="Maximum retry attempts for failed scraping requests"
#     )
#
#     # ========================================================================
#     # LOGGING SETTINGS
#     # ========================================================================
#
#     LOG_LEVEL: LogLevel = Field(
#         default=LogLevel.INFO,
#         description="Application logging level"
#     )
#
#     LOG_FILE: Optional[str] = Field(
#         default="logs/app.log",
#         description="Log file path (None for console only)"
#     )
#
#     # ========================================================================
#     # SECURITY SETTINGS
#     # ========================================================================
#
#     JWT_SECRET_KEY: str = Field(
#         default="your-secret-key-change-in-production",
#         min_length=32,
#         description="JWT secret key for token signing (MUST change in production)"
#     )
#
#     JWT_ALGORITHM: str = Field(
#         default="HS256",
#         description="JWT signing algorithm"
#     )
#
#     JWT_EXPIRE_MINUTES: int = Field(
#         default=60,
#         ge=5,
#         le=1440,
#         description="JWT token expiration time in minutes"
#     )
#
#     # ========================================================================
#     # EXTERNAL SERVICE SETTINGS
#     # ========================================================================
#
#     JAVA_API_URL: str = Field(
#         default="http://localhost:8080",
#         description="Java Spring Boot API Gateway URL"
#     )
#
#     MCP_SERVER_URL: str = Field(
#         default="http://localhost:3001",
#         description="MCP Server URL for AI agent integration"
#     )
#
#     # ========================================================================
#     # VALIDATORS
#     # ========================================================================
#
#     @validator('DATABASE_URL')
#     def validate_database_url(cls, v):
#         """Validate database URL format"""
#         if not v.startswith(('postgresql://', 'sqlite:///')):
#             raise ValueError('DATABASE_URL must start with postgresql:// or sqlite:///')
#         return v
#
#     @validator('REDIS_URL')
#     def validate_redis_url(cls, v):
#         """Validate Redis URL format"""
#         if not v.startswith('redis://'):
#             raise ValueError('REDIS_URL must start with redis://')
#         return v
#
#     @validator('OPENAI_API_KEY', 'ANTHROPIC_API_KEY')
#     def validate_api_keys(cls, v):
#         """Validate API key format"""
#         if v and len(v) < 10:
#             raise ValueError('API keys must be at least 10 characters long')
#         return v
#
#     @validator('SCRAPING_DELAY_MAX')
#     def validate_scraping_delays(cls, v, values):
#         """Ensure max delay is greater than min delay"""
#         if 'SCRAPING_DELAY_MIN' in values and v <= values['SCRAPING_DELAY_MIN']:
#             raise ValueError('SCRAPING_DELAY_MAX must be greater than SCRAPING_DELAY_MIN')
#         return v
#
#     @validator('JWT_SECRET_KEY')
#     def validate_jwt_secret(cls, v, values):
#         """Validate JWT secret in production"""
#         if values.get('ENVIRONMENT') == Environment.PRODUCTION:
#             if v == "your-secret-key-change-in-production":
#                 raise ValueError('JWT_SECRET_KEY must be changed in production')
#         return v
#
#     class Config:
#         """Pydantic configuration"""
#         env_file = ".env"
#         env_file_encoding = "utf-8"
#         case_sensitive = True
#         validate_assignment = True
#
# # Create global settings instance
# settings = Settings()
#
# # Export commonly used settings
# __all__ = ["settings", "Settings"]
#
# ============================================================================
