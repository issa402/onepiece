#!/bin/bash

# 🏴‍☠️ ONE PIECE TRADING PLATFORM - JAVA SPRING BOOT STARTUP SCRIPT
# Enterprise startup script like Netflix/Amazon production systems

echo "🏴‍☠️ Starting One Piece Trading Platform - Java Spring Boot Edition"
echo "=================================================================="

# Colors for output
RED='\033[0;31m'
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
BLUE='\033[0;34m'
NC='\033[0m' # No Color

# Function to print colored output
print_status() {
    echo -e "${GREEN}[INFO]${NC} $1"
}

print_warning() {
    echo -e "${YELLOW}[WARN]${NC} $1"
}

print_error() {
    echo -e "${RED}[ERROR]${NC} $1"
}

print_header() {
    echo -e "${BLUE}$1${NC}"
}

# Check prerequisites
print_header "🔍 Checking Prerequisites..."

# Check Java
if command -v java &> /dev/null; then
    JAVA_VERSION=$(java -version 2>&1 | head -n 1 | cut -d'"' -f2)
    print_status "Java found: $JAVA_VERSION"
else
    print_error "Java not found! Please install Java 17+"
    exit 1
fi

# Check Maven
if command -v mvn &> /dev/null; then
    MVN_VERSION=$(mvn -version | head -n 1)
    print_status "Maven found: $MVN_VERSION"
else
    print_error "Maven not found! Please install Maven 3.6+"
    exit 1
fi

# Check MySQL connection
print_header "🗄️ Checking Database Connection..."
if command -v mysql &> /dev/null; then
    if mysql -u root -e "USE onepiece_market;" 2>/dev/null; then
        print_status "Database connection successful"
    else
        print_warning "Cannot connect to onepiece_market database"
        print_warning "Make sure MySQL is running and database exists"
    fi
else
    print_warning "MySQL client not found - cannot test database connection"
fi

# Set environment variables
print_header "⚙️ Setting Environment Variables..."
export SPRING_PROFILES_ACTIVE=${SPRING_PROFILES_ACTIVE:-dev}
export DB_USER=${DB_USER:-root}
export DB_PASSWORD=${DB_PASSWORD:-}
export SERVER_PORT=${SERVER_PORT:-8080}

print_status "Profile: $SPRING_PROFILES_ACTIVE"
print_status "Database User: $DB_USER"
print_status "Server Port: $SERVER_PORT"

# Build the application
print_header "🔨 Building Application..."
if mvn clean compile; then
    print_status "Build successful"
else
    print_error "Build failed!"
    exit 1
fi

# Run tests (optional)
if [ "$1" = "--with-tests" ]; then
    print_header "🧪 Running Tests..."
    if mvn test; then
        print_status "All tests passed"
    else
        print_error "Tests failed!"
        exit 1
    fi
fi

# Start the application
print_header "🚀 Starting Spring Boot Application..."
print_status "Application will be available at: http://localhost:$SERVER_PORT/api"
print_status "Health check: http://localhost:$SERVER_PORT/api/actuator/health"
print_status "API documentation: http://localhost:$SERVER_PORT/api/swagger-ui.html"
print_status "Metrics: http://localhost:$SERVER_PORT/api/actuator/metrics"

echo ""
print_header "🏴‍☠️ One Piece Trading Platform - Java Spring Boot"
print_status "Press Ctrl+C to stop the application"
echo ""

# Run the Spring Boot application
mvn spring-boot:run \
    -Dspring-boot.run.profiles=$SPRING_PROFILES_ACTIVE \
    -Dspring-boot.run.jvmArguments="-Xmx512m -Xms256m" \
    -Dserver.port=$SERVER_PORT
