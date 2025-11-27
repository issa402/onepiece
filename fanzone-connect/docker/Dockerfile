# ═══════════════════════════════════════════════════════════════════════════════
# 🏆 FANZONE CONNECT - MAIN APPLICATION DOCKERFILE
# ═══════════════════════════════════════════════════════════════════════════════
#
# PURPOSE:
# Containerizes the FANZONE CONNECT Python/FastAPI application.
# Creates a portable, reproducible environment that runs anywhere Docker runs.
#
# USAGE:
#   docker build -t fanzone-connect:latest .
#   docker run -p 8000:8000 fanzone-connect:latest
#
# DOCKERFILE CONCEPTS:
# - Multi-stage builds (smaller final image)
# - Layer caching (faster rebuilds)
# - Non-root user (security)
# - Health checks
# - Environment variables
#
# LINUX COMMANDS USED IN DOCKERFILE:
# - apt-get update/install (package management)
# - useradd (create non-root user)
# - pip install (Python packages)
# - chmod/chown (permissions)
# ═══════════════════════════════════════════════════════════════════════════════

# ─────────────────────────────────────────────────────────────────────────────
# STAGE 1: Builder stage (install dependencies)
# ─────────────────────────────────────────────────────────────────────────────
# TODO: FROM python:3.11-slim as builder
# TODO: Set WORKDIR to /app
# TODO: Install build dependencies (gcc, libpq-dev for psycopg2)
# TODO: Copy requirements.txt
# TODO: Create virtual environment
# TODO: pip install dependencies into virtual environment

# ─────────────────────────────────────────────────────────────────────────────
# STAGE 2: Runtime stage (final image)
# ─────────────────────────────────────────────────────────────────────────────
# TODO: FROM python:3.11-slim
# TODO: Set environment variables:
#       PYTHONDONTWRITEBYTECODE=1
#       PYTHONUNBUFFERED=1
# TODO: Install runtime dependencies only (libpq5)
# TODO: Create non-root user (appuser)
# TODO: Copy virtual environment from builder stage
# TODO: Copy application code
# TODO: Set ownership to appuser
# TODO: Switch to appuser (USER appuser)
# TODO: EXPOSE 8000
# TODO: Add HEALTHCHECK instruction
# TODO: CMD to start the application (uvicorn)

# ─────────────────────────────────────────────────────────────────────────────
# ALTERNATIVE: Development Dockerfile
# ─────────────────────────────────────────────────────────────────────────────
# TODO: For development, create Dockerfile.dev with:
#       - Volume mounts for live reload
#       - Debug mode enabled
#       - Development dependencies installed

# ─────────────────────────────────────────────────────────────────────────────
# BEST PRACTICES IMPLEMENTED:
# ─────────────────────────────────────────────────────────────────────────────
# TODO: Use specific version tags (not :latest in FROM)
# TODO: Minimize layers by combining RUN commands
# TODO: Order commands from least to most frequently changing
# TODO: Use .dockerignore to exclude unnecessary files
# TODO: Don't store secrets in the image
# TODO: Run as non-root user
# TODO: Use multi-stage builds to reduce image size

