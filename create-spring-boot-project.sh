#!/bin/bash

# ============================================================================
# CREATE SPRING BOOT PROJECT USING SPRING INITIALIZR
# ============================================================================
# This script downloads a pre-configured Spring Boot project from Spring Initializr
# Run with: bash create-spring-boot-project.sh
# ============================================================================

set -e  # Exit on any error

echo "============================================================================"
echo "🏴‍☠️ CREATING SPRING BOOT PROJECT - CHARACTER SERVICE"
echo "============================================================================"
echo ""

# ============================================================================
# Configuration
# ============================================================================
PROJECT_NAME="character-service"
GROUP_ID="com.onepiece"
ARTIFACT_ID="character-service"
PACKAGE_NAME="com.onepiece.character"
JAVA_VERSION="17"
SPRING_BOOT_VERSION="3.2.0"

# Dependencies
DEPENDENCIES="web,data-jpa,postgresql,lombok,devtools"

# Spring Initializr URL
INITIALIZR_URL="https://start.spring.io/starter.zip"

echo "Project Configuration:"
echo "  📦 Project: Maven"
echo "  ☕ Language: Java $JAVA_VERSION"
echo "  🍃 Spring Boot: $SPRING_BOOT_VERSION"
echo "  📂 Group: $GROUP_ID"
echo "  📂 Artifact: $ARTIFACT_ID"
echo "  📦 Package: $PACKAGE_NAME"
echo "  📚 Dependencies: Spring Web, Spring Data JPA, PostgreSQL, Lombok, DevTools"
echo ""

# ============================================================================
# Check if project already exists
# ============================================================================
if [ -d "$PROJECT_NAME" ]; then
    echo "⚠️  WARNING: Directory '$PROJECT_NAME' already exists!"
    echo ""
    echo "Options:"
    echo "  1. Delete existing directory and create new project"
    echo "  2. Cancel and keep existing project"
    echo ""
    read -p "Enter choice (1 or 2): " choice
    
    if [ "$choice" = "1" ]; then
        echo "Deleting existing directory..."
        rm -rf "$PROJECT_NAME"
    else
        echo "Cancelled. Keeping existing project."
        exit 0
    fi
fi

# ============================================================================
# Download Spring Boot Project from Spring Initializr
# ============================================================================
echo ""
echo "📥 Downloading Spring Boot project from Spring Initializr..."
echo ""

curl -G "$INITIALIZR_URL" \
    -d type=maven-project \
    -d language=java \
    -d bootVersion="$SPRING_BOOT_VERSION" \
    -d baseDir="$PROJECT_NAME" \
    -d groupId="$GROUP_ID" \
    -d artifactId="$ARTIFACT_ID" \
    -d name="$PROJECT_NAME" \
    -d description="One Piece Character Trading Service" \
    -d packageName="$PACKAGE_NAME" \
    -d packaging=jar \
    -d javaVersion="$JAVA_VERSION" \
    -d dependencies="$DEPENDENCIES" \
    -o "$PROJECT_NAME.zip"

# ============================================================================
# Extract Project
# ============================================================================
echo ""
echo "📦 Extracting project..."
unzip -q "$PROJECT_NAME.zip"
rm "$PROJECT_NAME.zip"

echo ""
echo "✅ Project extracted to: $PROJECT_NAME/"

# ============================================================================
# Create Package Structure
# ============================================================================
echo ""
echo "📁 Creating package structure..."

cd "$PROJECT_NAME"

# Create additional packages
mkdir -p "src/main/java/com/onepiece/character/model"
mkdir -p "src/main/java/com/onepiece/character/repository"
mkdir -p "src/main/java/com/onepiece/character/service"
mkdir -p "src/main/java/com/onepiece/character/controller"
mkdir -p "src/main/java/com/onepiece/character/exception"
mkdir -p "src/main/java/com/onepiece/character/dto"

echo "✅ Package structure created:"
echo "   ├── model       (for entities like Character.java)"
echo "   ├── repository  (for database access)"
echo "   ├── service     (for business logic)"
echo "   ├── controller  (for REST APIs)"
echo "   ├── exception   (for custom exceptions)"
echo "   └── dto         (for data transfer objects)"

# ============================================================================
# Configure application.properties
# ============================================================================
echo ""
echo "⚙️  Configuring application.properties..."

cat > "src/main/resources/application.properties" << 'EOF'
# ============================================================================
# ONE PIECE CHARACTER SERVICE - APPLICATION CONFIGURATION
# ============================================================================

# ----------------------------------------------------------------------------
# Server Configuration
# ----------------------------------------------------------------------------
server.port=8081
spring.application.name=character-service

# ----------------------------------------------------------------------------
# Database Configuration
# ----------------------------------------------------------------------------
spring.datasource.url=jdbc:postgresql://localhost:5432/onepiece_characters
spring.datasource.username=postgres
spring.datasource.password=postgres
spring.datasource.driver-class-name=org.postgresql.Driver

# ----------------------------------------------------------------------------
# JPA/Hibernate Configuration
# ----------------------------------------------------------------------------
# ddl-auto options:
#   - create: Drop and recreate tables on startup (LOSES DATA!)
#   - create-drop: Create tables on startup, drop on shutdown (LOSES DATA!)
#   - update: Update schema without losing data (RECOMMENDED for development)
#   - validate: Only validate schema, don't modify (RECOMMENDED for production)
#   - none: Do nothing
spring.jpa.hibernate.ddl-auto=update

# Show SQL queries in console (great for learning!)
spring.jpa.show-sql=true

# Format SQL queries for readability
spring.jpa.properties.hibernate.format_sql=true

# PostgreSQL dialect
spring.jpa.properties.hibernate.dialect=org.hibernate.dialect.PostgreSQLDialect

# ----------------------------------------------------------------------------
# Logging Configuration
# ----------------------------------------------------------------------------
# Log SQL queries
logging.level.org.hibernate.SQL=DEBUG

# Log SQL parameter values
logging.level.org.hibernate.type.descriptor.sql.BasicBinder=TRACE

# Log Spring Boot info
logging.level.org.springframework.web=INFO

# ----------------------------------------------------------------------------
# Development Tools
# ----------------------------------------------------------------------------
# Enable hot reload (DevTools)
spring.devtools.restart.enabled=true
EOF

echo "✅ application.properties configured"

# ============================================================================
# Download Maven Dependencies
# ============================================================================
echo ""
echo "📦 Downloading Maven dependencies..."
echo "   (This may take a few minutes on first run)"
echo ""

./mvnw clean install -DskipTests

# ============================================================================
# Create README for the project
# ============================================================================
echo ""
echo "📝 Creating project README..."

cat > "README.md" << 'EOF'
# 🏴‍☠️ One Piece Character Service

Spring Boot microservice for managing One Piece characters in the trading platform.

## 🚀 Quick Start

### Prerequisites
- Java JDK 17+
- Maven 3.6+
- PostgreSQL 12+

### Run the Application

```bash
# Using Maven wrapper
./mvnw spring-boot:run

# Or using installed Maven
mvn spring-boot:run
```

The service will start on: http://localhost:8081

### Database Setup

Database is automatically created by the setup script.
If you need to create it manually:

```bash
sudo -u postgres psql -c "CREATE DATABASE onepiece_characters;"
```

## 📁 Project Structure

```
src/main/java/com/onepiece/character/
├── CharacterServiceApplication.java  (Main application)
├── model/                            (JPA entities)
├── repository/                       (Database access)
├── service/                          (Business logic)
├── controller/                       (REST APIs)
├── exception/                        (Custom exceptions)
└── dto/                              (Data transfer objects)
```

## 🔧 Configuration

Configuration is in `src/main/resources/application.properties`

Key settings:
- Server port: 8081
- Database: PostgreSQL (localhost:5432/onepiece_characters)
- JPA: Auto-update schema, show SQL queries

## 📚 Next Steps

1. Create Character entity in `model/Character.java`
2. Create CharacterRepository in `repository/CharacterRepository.java`
3. Create CharacterService in `service/CharacterService.java`
4. Create CharacterController in `controller/CharacterController.java`

Follow the TODO.md file in the repository root for detailed instructions.

## 🧪 Testing

```bash
# Run tests
./mvnw test

# Run with coverage
./mvnw test jacoco:report
```

## 📖 API Documentation

Once the service is running, API endpoints will be available at:
- GET    /api/characters       - Get all characters
- GET    /api/characters/{id}  - Get character by ID
- POST   /api/characters       - Create new character
- PUT    /api/characters/{id}  - Update character
- DELETE /api/characters/{id}  - Delete character

## 🏴‍☠️ One Piece Trading Platform

This service is part of the One Piece Trading Platform project.
See the main repository for complete documentation.
EOF

echo "✅ README.md created"

# ============================================================================
# Verify Project Structure
# ============================================================================
echo ""
echo "============================================================================"
echo "✅ PROJECT CREATED SUCCESSFULLY!"
echo "============================================================================"
echo ""
echo "📂 Project Location: $(pwd)"
echo ""
echo "📁 Project Structure:"
tree -L 3 -I 'target|.mvn' . 2>/dev/null || find . -maxdepth 3 -type d | grep -v target | grep -v .mvn | head -20

# ============================================================================
# Display Next Steps
# ============================================================================
echo ""
echo "============================================================================"
echo "📋 NEXT STEPS:"
echo "============================================================================"
echo ""
echo "1. Open the project in your IDE:"
echo "   → IntelliJ IDEA: File → Open → Select 'character-service' folder"
echo "   → VS Code: code character-service"
echo ""
echo "2. Verify the project builds:"
echo "   → cd character-service"
echo "   → ./mvnw clean install"
echo ""
echo "3. Run the application:"
echo "   → ./mvnw spring-boot:run"
echo "   → Should start on http://localhost:8081"
echo ""
echo "4. Create Character.java entity:"
echo "   → Location: src/main/java/com/onepiece/character/model/Character.java"
echo "   → Use the Character.java template in the repository root as guidance"
echo ""
echo "5. Follow TODO.md Phase 1.5 onwards"
echo ""
echo "============================================================================"
echo "🏴‍☠️ Ready to implement Character.java!"
echo "============================================================================"

