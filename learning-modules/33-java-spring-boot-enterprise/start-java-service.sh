#!/bin/bash

# 🏴‍☠️ JAVA SPRING BOOT SERVICE STARTUP SCRIPT
# Start your Java Character Service for the One Piece Trading Platform

set -euo pipefail

# Script configuration
SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
PROJECT_ROOT="$(cd "${SCRIPT_DIR}/../.." && pwd)"
LOG_DIR="${PROJECT_ROOT}/logs"
TIMESTAMP=$(date +"%Y%m%d_%H%M%S")
LOG_FILE="${LOG_DIR}/java-service_${TIMESTAMP}.log"

# Colors for output
RED='\033[0;31m'
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
BLUE='\033[0;34m'
NC='\033[0m' # No Color

# Logging function
log() {
    local level="$1"
    local message="$2"
    local timestamp=$(date '+%Y-%m-%d %H:%M:%S')
    local log_entry="[${timestamp}] [${level}] ${message}"

    case "${level}" in
        "INFO")  echo -e "${GREEN}${log_entry}${NC}" ;;
        "WARN")  echo -e "${YELLOW}${log_entry}${NC}" ;;
        "ERROR") echo -e "${RED}${log_entry}${NC}" ;;
        "DEBUG") echo -e "${BLUE}${log_entry}${NC}" ;;
        *)       echo "${log_entry}" ;;
    esac

    # Create log directory if it doesn't exist
    mkdir -p "${LOG_DIR}"
    echo "${log_entry}" >> "${LOG_FILE}"
}

# Check prerequisites
check_prerequisites() {
    log "INFO" "🔍 Checking prerequisites..."

    # Check Java
    if ! command -v java &> /dev/null; then
        log "ERROR" "Java is not installed. Please install Java 17 or higher."
        log "INFO" "Install with: sudo apt install openjdk-17-jdk"
        exit 1
    fi

    local java_version=$(java -version 2>&1 | head -n1 | cut -d'"' -f2 | cut -d'.' -f1)
    if [[ ${java_version} -lt 17 ]]; then
        log "ERROR" "Java 17 or higher is required. Current version: ${java_version}"
        exit 1
    fi
    log "INFO" "✅ Java ${java_version} detected"

    # Check Maven
    if ! command -v mvn &> /dev/null; then
        log "ERROR" "Maven is not installed. Please install Maven 3.6 or higher."
        log "INFO" "Install with: sudo apt install maven"
        exit 1
    fi

    local maven_version=$(mvn -version 2>/dev/null | head -n1 | grep -oE '[0-9]+\.[0-9]+\.[0-9]+' | head -n1)
    log "INFO" "✅ Maven ${maven_version} detected"

    # Check if port 8080 is available
    if netstat -tuln 2>/dev/null | grep -q ":8080 "; then
        log "WARN" "Port 8080 is already in use. The Java service may fail to start."
        log "INFO" "Stop existing service with: pkill -f 'java.*spring-boot' or use different port"
    else
        log "INFO" "✅ Port 8080 is available"
    fi
}

# Build the Java application
build_application() {
    log "INFO" "🔨 Building Java Spring Boot application..."

    cd "${SCRIPT_DIR}"

    # Clean and build
    if mvn clean package -DskipTests -q; then
        log "INFO" "✅ Build successful"
    else
        log "ERROR" "❌ Build failed. Check Maven configuration and dependencies."
        exit 1
    fi
}

# Start the Java service
start_service() {
    log "INFO" "🚀 Starting Java Character Service..."

    cd "${SCRIPT_DIR}"

    # Default configuration
    local profile="${1:-development}"
    local port="${2:-8080}"

    # Database configuration
    local db_url="jdbc:postgresql://localhost:5432/onepiece_trading"
    local db_username="onepiece_user"
    local db_password="${DB_PASSWORD:-onepiece_password}"

    # Redis configuration
    local redis_host="localhost"
    local redis_port="6379"

    log "INFO" "Profile: ${profile}"
    log "INFO" "Port: ${port}"
    log "INFO" "Database: ${db_url}"
    log "INFO" "Redis: ${redis_host}:${redis_port}"

    # Start the application
    java -jar target/*.jar \
        --spring.profiles.active="${profile}" \
        --server.port="${port}" \
        --spring.datasource.url="${db_url}" \
        --spring.datasource.username="${db_username}" \
        --spring.datasource.password="${db_password}" \
        --spring.redis.host="${redis_host}" \
        --spring.redis.port="${redis_port}" \
        --management.endpoints.web.exposure.include=health,info,metrics,prometheus \
        --logging.level.com.onepiece=INFO \
        --logging.level.org.springframework.web=DEBUG \
        2>&1 | tee -a "${LOG_FILE}"
}

# Health check
health_check() {
    local port="${1:-8080}"
    local max_attempts=30
    local attempt=1

    log "INFO" "🏥 Performing health check..."

    while [[ ${attempt} -le ${max_attempts} ]]; do
        if curl -f -s --max-time 5 "http://localhost:${port}/actuator/health" > /dev/null; then
            log "INFO" "✅ Java service is healthy!"
            log "INFO" "🌐 Service URLs:"
            log "INFO" "  - Health: http://localhost:${port}/actuator/health"
            log "INFO" "  - Info: http://localhost:${port}/actuator/info"
            log "INFO" "  - Metrics: http://localhost:${port}/actuator/metrics"
            log "INFO" "  - Characters API: http://localhost:${port}/api/v1/characters"
            log "INFO" "  - Swagger UI: http://localhost:${port}/swagger-ui.html"
            return 0
        fi

        log "INFO" "Waiting for service to start (${attempt}/${max_attempts})..."
        sleep 2
        ((attempt++))
    done

    log "ERROR" "❌ Service failed to start within timeout"
    log "ERROR" "Check logs: ${LOG_FILE}"
    return 1
}

# Show usage
show_usage() {
    echo "🏴‍☠️ One Piece Java Character Service Startup Script"
    echo ""
    echo "Usage: $0 [COMMAND] [OPTIONS]"
    echo ""
    echo "Commands:"
    echo "  start [profile] [port]  - Start the Java service (default: development 8080)"
    echo "  build                   - Build the application only"
    echo "  check                   - Check prerequisites only"
    echo "  health [port]           - Check service health (default: 8080)"
    echo "  help                    - Show this help message"
    echo ""
    echo "Examples:"
    echo "  $0 start                    # Start with development profile on port 8080"
    echo "  $0 start production 8081    # Start with production profile on port 8081"
    echo "  $0 build                    # Build the application"
    echo "  $0 health 8080              # Check health of service on port 8080"
    echo ""
    echo "Environment Variables:"
    echo "  DB_PASSWORD                 # Database password (default: onepiece_password)"
    echo ""
    echo "Prerequisites:"
    echo "  - Java 17 or higher"
    echo "  - Maven 3.6 or higher"
    echo "  - PostgreSQL running on localhost:5432"
    echo "  - Redis running on localhost:6379"
}

# Main function
main() {
    local command="${1:-start}"

    case "${command}" in
        "start")
            check_prerequisites
            build_application
            start_service "${2:-development}" "${3:-8080}"
            ;;
        "build")
            check_prerequisites
            build_application
            ;;
        "check")
            check_prerequisites
            ;;
        "health")
            health_check "${2:-8080}"
            ;;
        "help"|"-h"|"--help")
            show_usage
            ;;
        *)
            log "ERROR" "Unknown command: ${command}"
            show_usage
            exit 1
            ;;
    esac
}

# Trap for cleanup
cleanup() {
    log "INFO" "🧹 Cleaning up..."
    # Add any cleanup logic here
}

trap cleanup EXIT

# Run main function
main "$@"
