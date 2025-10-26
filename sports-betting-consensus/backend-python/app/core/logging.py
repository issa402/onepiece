# ============================================================================
# 📚 LEARNING GUIDE: Logging Configuration (app/core/logging.py)
# ============================================================================
#
# 🎯 PURPOSE:
# This module sets up comprehensive logging for the application.
# It configures structured logging with proper formatting, levels,
# and output destinations for debugging and monitoring.
#
# 🔧 TECHNOLOGIES USED:
# - Python logging: Built-in logging framework
# - Structured logging: JSON format for production
# - Log rotation: Prevent log files from growing too large
# - Multiple handlers: Console and file output
#
# 📖 IN-DEPTH EXPLANATION:
#
# **Logging Best Practices:**
# - Use appropriate log levels (DEBUG, INFO, WARNING, ERROR, CRITICAL)
# - Include contextual information (request IDs, user IDs, timestamps)
# - Structure logs for easy parsing and analysis
# - Separate application logs from access logs
# - Configure log rotation to manage disk space
#
# 💡 HINTS:
# - Use logger.info() for normal operations
# - Use logger.warning() for recoverable issues
# - Use logger.error() for serious problems
# - Use logger.debug() for detailed debugging info
# - Include relevant context in log messages
#
# 🧪 TEST YOUR CODE:
# from app.core.logging import setup_logging
# setup_logging()
# import logging
# logger = logging.getLogger(__name__)
# logger.info("Test message")

# YOUR IMPLEMENTATION HERE:
# (Write your logging setup function below)

# ============================================================================
# 📝 REFERENCE IMPLEMENTATION (Check your code against this)
# ============================================================================

import logging
import logging.config
import sys
from pathlib import Path
from typing import Dict, Any

def setup_logging(log_level: str = "INFO", log_file: str = None) -> None:
    """
    Set up comprehensive logging configuration
    
    Args:
        log_level: Logging level (DEBUG, INFO, WARNING, ERROR, CRITICAL)
        log_file: Optional log file path
    """
    
    # Create logs directory if it doesn't exist
    if log_file:
        log_path = Path(log_file)
        log_path.parent.mkdir(parents=True, exist_ok=True)
    
    # Logging configuration
    config: Dict[str, Any] = {
        "version": 1,
        "disable_existing_loggers": False,
        "formatters": {
            "detailed": {
                "format": "%(asctime)s - %(name)s - %(levelname)s - %(message)s",
                "datefmt": "%Y-%m-%d %H:%M:%S"
            },
            "simple": {
                "format": "%(levelname)s - %(message)s"
            }
        },
        "handlers": {
            "console": {
                "class": "logging.StreamHandler",
                "level": log_level,
                "formatter": "detailed",
                "stream": sys.stdout
            }
        },
        "root": {
            "level": log_level,
            "handlers": ["console"]
        },
        "loggers": {
            "uvicorn": {
                "level": "INFO",
                "handlers": ["console"],
                "propagate": False
            },
            "uvicorn.error": {
                "level": "INFO",
                "handlers": ["console"],
                "propagate": False
            },
            "uvicorn.access": {
                "level": "INFO",
                "handlers": ["console"],
                "propagate": False
            }
        }
    }
    
    # Add file handler if log_file is specified
    if log_file:
        config["handlers"]["file"] = {
            "class": "logging.handlers.RotatingFileHandler",
            "level": log_level,
            "formatter": "detailed",
            "filename": log_file,
            "maxBytes": 10485760,  # 10MB
            "backupCount": 5
        }
        config["root"]["handlers"].append("file")
        config["loggers"]["uvicorn"]["handlers"].append("file")
        config["loggers"]["uvicorn.error"]["handlers"].append("file")
        config["loggers"]["uvicorn.access"]["handlers"].append("file")
    
    # Apply configuration
    logging.config.dictConfig(config)
    
    # Log startup message
    logger = logging.getLogger(__name__)
    logger.info("🚀 Logging system initialized")
    logger.info(f"📊 Log level: {log_level}")
    if log_file:
        logger.info(f"📁 Log file: {log_file}")

# ============================================================================
