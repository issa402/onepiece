#!/bin/bash

# ============================================================================
# ONE PIECE TRADING PLATFORM - DEVELOPMENT ENVIRONMENT SETUP
# ============================================================================
# This script installs all required tools for Spring Boot development
# Run with: bash setup-environment.sh
# ============================================================================

set -e  # Exit on any error

echo "============================================================================"
echo "🏴‍☠️ ONE PIECE TRADING PLATFORM - ENVIRONMENT SETUP"
echo "============================================================================"
echo ""
echo "This script will install:"
echo "  ✅ Java JDK 17"
echo "  ✅ Maven"
echo "  ✅ PostgreSQL"
echo "  ✅ Additional utilities (curl, wget, unzip, git)"
echo ""
echo "Press ENTER to continue or Ctrl+C to cancel..."
read

# ============================================================================
# STEP 1: Update Package Lists
# ============================================================================
echo ""
echo "📦 Step 1: Updating package lists..."
sudo apt update

# ============================================================================
# STEP 2: Install Java JDK 17
# ============================================================================
echo ""
echo "☕ Step 2: Installing Java JDK 17..."
sudo apt install -y openjdk-17-jdk

echo ""
echo "Verifying Java installation..."
java -version
javac -version

# ============================================================================
# STEP 3: Install Maven
# ============================================================================
echo ""
echo "📦 Step 3: Installing Maven..."
sudo apt install -y maven

echo ""
echo "Verifying Maven installation..."
mvn -version

# ============================================================================
# STEP 4: Install PostgreSQL
# ============================================================================
echo ""
echo "🐘 Step 4: Installing PostgreSQL..."
sudo apt install -y postgresql postgresql-contrib

echo ""
echo "Starting PostgreSQL service..."
sudo systemctl start postgresql
sudo systemctl enable postgresql

echo ""
echo "Verifying PostgreSQL is running..."
sudo systemctl status postgresql --no-pager

# ============================================================================
# STEP 5: Create PostgreSQL Database
# ============================================================================
echo ""
echo "🗄️ Step 5: Creating PostgreSQL database..."

# Create database
sudo -u postgres psql -c "CREATE DATABASE onepiece_characters;" 2>/dev/null || echo "Database already exists"

# Set postgres user password
sudo -u postgres psql -c "ALTER USER postgres PASSWORD 'postgres';"

# Verify database
echo ""
echo "Verifying database creation..."
sudo -u postgres psql -c "\l" | grep onepiece || echo "Warning: Database not found"

# ============================================================================
# STEP 6: Install Additional Utilities
# ============================================================================
echo ""
echo "🔧 Step 6: Installing additional utilities..."
sudo apt install -y curl wget unzip git

# ============================================================================
# STEP 7: Verify All Installations
# ============================================================================
echo ""
echo "============================================================================"
echo "✅ INSTALLATION COMPLETE - VERIFICATION"
echo "============================================================================"
echo ""

echo "Java Version:"
java -version 2>&1 | head -n 1
echo ""

echo "Maven Version:"
mvn -version | head -n 1
echo ""

echo "PostgreSQL Version:"
psql --version
echo ""

echo "Git Version:"
git --version
echo ""

echo "PostgreSQL Service Status:"
sudo systemctl is-active postgresql
echo ""

echo "PostgreSQL Database:"
sudo -u postgres psql -c "\l" | grep onepiece_characters || echo "❌ Database not found"
echo ""

# ============================================================================
# STEP 8: Display Next Steps
# ============================================================================
echo "============================================================================"
echo "🎉 ENVIRONMENT SETUP COMPLETE!"
echo "============================================================================"
echo ""
echo "✅ Java JDK 17 installed"
echo "✅ Maven installed"
echo "✅ PostgreSQL installed and running"
echo "✅ Database 'onepiece_characters' created"
echo "✅ Additional utilities installed"
echo ""
echo "============================================================================"
echo "📋 NEXT STEPS:"
echo "============================================================================"
echo ""
echo "1. Create Spring Boot project using Spring Initializr"
echo "   → Run: bash create-spring-boot-project.sh"
echo ""
echo "2. Or manually visit: https://start.spring.io/"
echo "   Configuration:"
echo "   - Project: Maven"
echo "   - Language: Java"
echo "   - Spring Boot: 3.2.0 (or latest)"
echo "   - Group: com.onepiece"
echo "   - Artifact: character-service"
echo "   - Package name: com.onepiece.character"
echo "   - Java: 17"
echo "   Dependencies: Spring Web, Spring Data JPA, PostgreSQL Driver, Lombok"
echo ""
echo "3. Follow the TODO.md file for complete instructions"
echo ""
echo "============================================================================"
echo "🏴‍☠️ Ready to build the One Piece Trading Platform!"
echo "============================================================================"

