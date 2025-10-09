#!/bin/bash

# 🏴‍☠️ BASH DEPLOYMENT AUTOMATION SCRIPT BLUEPRINT
# Your mission: Create Bash scripts for Linux automation and deployment

# WHAT YOU'RE BUILDING:
# - Bash scripts for Linux system automation
# - Service deployment and orchestration
# - System monitoring and health checks
# - Log management and analysis
# - Security hardening and compliance
# - Performance monitoring and optimization
# - Backup and disaster recovery

# LEARNING OBJECTIVES:
# - Bash scripting fundamentals
# - Linux system administration
# - Process management and monitoring
# - File system operations
# - Network configuration and troubleshooting
# - Security best practices
# - Performance tuning and optimization

# TODO 1: SCRIPT CONFIGURATION AND VARIABLES
# Set script configuration
# set -euo pipefail  # Exit on error, undefined vars, pipe failures
# 
# # Script metadata
# SCRIPT_NAME="deploy-onepiece-services.sh"
# SCRIPT_VERSION="1.0.0"
# SCRIPT_AUTHOR="One Piece DevOps Team"
# 
# # Default configuration
# ENVIRONMENT="${1:-development}"
# PROJECT_ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
# CONFIG_DIR="${PROJECT_ROOT}/config"
# LOG_DIR="${PROJECT_ROOT}/logs"
# TIMESTAMP=$(date +"%Y%m%d_%H%M%S")
# LOG_FILE="${LOG_DIR}/deployment_${TIMESTAMP}.log"

# TODO 2: LOGGING FUNCTIONS
# Setup logging functionality
# setup_logging() {
#     # Create log directory if it doesn't exist
#     mkdir -p "${LOG_DIR}"
#     
#     # Initialize log file
#     echo "=== One Piece Services Deployment Log ===" > "${LOG_FILE}"
#     echo "Started: $(date)" >> "${LOG_FILE}"
#     echo "Environment: ${ENVIRONMENT}" >> "${LOG_FILE}"
#     echo "=========================================" >> "${LOG_FILE}"
# }
# 
# log() {
#     local level="$1"
#     local message="$2"
#     local timestamp=$(date '+%Y-%m-%d %H:%M:%S')
#     local log_entry="[${timestamp}] [${level}] ${message}"
#     
#     # Color coding for console output
#     case "${level}" in
#         "INFO")  echo -e "\033[32m${log_entry}\033[0m" ;;  # Green
#         "WARN")  echo -e "\033[33m${log_entry}\033[0m" ;;  # Yellow
#         "ERROR") echo -e "\033[31m${log_entry}\033[0m" ;;  # Red
#         "DEBUG") echo -e "\033[36m${log_entry}\033[0m" ;;  # Cyan
#         *)       echo "${log_entry}" ;;
#     esac
#     
#     # Write to log file
#     echo "${log_entry}" >> "${LOG_FILE}"
# }

# TODO 3: ERROR HANDLING
# setup_error_handling() {
#     # Trap errors and cleanup
#     trap 'error_handler $? $LINENO' ERR
#     trap 'cleanup_handler' EXIT
# }
# 
# error_handler() {
#     local exit_code=$1
#     local line_number=$2
#     log "ERROR" "Script failed with exit code ${exit_code} at line ${line_number}"
#     log "ERROR" "Command: ${BASH_COMMAND}"
#     cleanup_handler
#     exit "${exit_code}"
# }
# 
# cleanup_handler() {
#     log "INFO" "Performing cleanup operations..."
#     # Add cleanup logic here (stop services, remove temp files, etc.)
# }

# TODO 4: SYSTEM REQUIREMENTS CHECK
# check_system_requirements() {
#     log "INFO" "🔍 Checking system requirements..."
#     
#     # Check if running as root (if needed)
#     if [[ $EUID -eq 0 ]]; then
#         log "WARN" "Running as root - consider using a non-root user"
#     fi
#     
#     # Check required commands
#     local required_commands=("docker" "docker-compose" "python3" "node" "npm" "git" "curl" "jq")
#     
#     for cmd in "${required_commands[@]}"; do
#         if ! command -v "${cmd}" &> /dev/null; then
#             log "ERROR" "Required command not found: ${cmd}"
#             return 1
#         else
#             local version=$(${cmd} --version 2>/dev/null | head -n1 || echo "Unknown version")
#             log "INFO" "✅ ${cmd}: ${version}"
#         fi
#     done
#     
#     # Check system resources
#     local available_memory=$(free -m | awk 'NR==2{printf "%.1f", $7/1024}')
#     local available_disk=$(df -h "${PROJECT_ROOT}" | awk 'NR==2{print $4}')
#     
#     log "INFO" "💾 Available Memory: ${available_memory}GB"
#     log "INFO" "💿 Available Disk: ${available_disk}"
#     
#     # Check if ports are available
#     local required_ports=(3000 5001 5002 5003 8000 3306 6379)
#     for port in "${required_ports[@]}"; do
#         if netstat -tuln | grep -q ":${port} "; then
#             log "WARN" "Port ${port} is already in use"
#         else
#             log "INFO" "✅ Port ${port} is available"
#         fi
#     done
# }

# TODO 5: CONFIGURATION LOADING
# load_configuration() {
#     local config_file="${CONFIG_DIR}/${ENVIRONMENT}.json"
#     
#     log "INFO" "📋 Loading configuration from: ${config_file}"
#     
#     if [[ ! -f "${config_file}" ]]; then
#         log "ERROR" "Configuration file not found: ${config_file}"
#         return 1
#     fi
#     
#     # Validate JSON syntax
#     if ! jq empty "${config_file}" 2>/dev/null; then
#         log "ERROR" "Invalid JSON in configuration file"
#         return 1
#     fi
#     
#     # Export configuration variables
#     export DB_HOST=$(jq -r '.database.host' "${config_file}")
#     export DB_PORT=$(jq -r '.database.port' "${config_file}")
#     export DB_NAME=$(jq -r '.database.name' "${config_file}")
#     export DB_USER=$(jq -r '.database.user' "${config_file}")
#     export DB_PASSWORD=$(jq -r '.database.password' "${config_file}")
#     
#     log "INFO" "Configuration loaded successfully"
# }

# TODO 6: DOCKER OPERATIONS
# start_docker_services() {
#     log "INFO" "🐳 Starting Docker services..."
#
#     # Check if Docker daemon is running
#     if ! docker info &> /dev/null; then
#         log "ERROR" "Docker daemon is not running"
#         return 1
#     fi
#
#     # Navigate to project root
#     cd "${PROJECT_ROOT}"
#
#     # Stop any existing containers
#     log "INFO" "Stopping existing containers..."
#     docker-compose down --remove-orphans 2>/dev/null || true
#
#     # Build images
#     log "INFO" "Building Docker images..."
#     if ! docker-compose build --no-cache; then
#         log "ERROR" "Docker build failed"
#         return 1
#     fi
#
#     # Start services
#     log "INFO" "Starting Docker containers..."
#     if ! docker-compose up -d; then
#         log "ERROR" "Failed to start Docker containers"
#         return 1
#     fi
#
#     # Wait for containers to be ready
#     log "INFO" "Waiting for containers to initialize..."
#     sleep 10
#
#     # Show running containers
#     log "INFO" "Running containers:"
#     docker-compose ps
# }

# TODO 6.1: JAVA SERVICES OPERATIONS
# start_java_services() {
#     log "INFO" "🔥 Starting Java Spring Boot services..."
#
#     # Check if Java is installed
#     if ! command -v java &> /dev/null; then
#         log "ERROR" "Java is not installed or not in PATH"
#         return 1
#     fi
#
#     # Check if Maven is installed
#     if ! command -v mvn &> /dev/null; then
#         log "ERROR" "Maven is not installed or not in PATH"
#         return 1
#     fi
#
#     # Create PID directory
#     mkdir -p "${PROJECT_ROOT}/pids"
#
#     # Build Java Character Service
#     log "INFO" "Building Java Character Service..."
#     cd "${PROJECT_ROOT}/learning-modules/33-java-spring-boot-enterprise"
#
#     if ! mvn clean package -DskipTests -q; then
#         log "ERROR" "Java Character Service build failed"
#         return 1
#     fi
#
#     # Start Java Character Service
#     log "INFO" "Starting Java Character Service on port 8080..."
#     nohup java -jar target/*.jar \
#         --spring.profiles.active=production \
#         --spring.datasource.url=jdbc:postgresql://localhost:5432/onepiece_trading \
#         --spring.datasource.username=onepiece_user \
#         --spring.datasource.password="${DB_PASSWORD}" \
#         --spring.redis.host=localhost \
#         --spring.redis.port=6379 \
#         --server.port=8080 \
#         --management.endpoints.web.exposure.include=health,info,metrics \
#         > "${LOG_DIR}/java-character-service.log" 2>&1 &
#
#     echo $! > "${PROJECT_ROOT}/pids/java-character-service.pid"
#
#     # Wait for service to start
#     log "INFO" "Waiting for Java service to initialize..."
#     sleep 20
#
#     # Health check
#     local max_attempts=30
#     local attempt=1
#
#     while [[ ${attempt} -le ${max_attempts} ]]; do
#         log "INFO" "Checking Java service health (attempt ${attempt}/${max_attempts})..."
#
#         if curl -f -s --max-time 5 http://localhost:8080/actuator/health > /dev/null; then
#             log "INFO" "✅ Java Character Service: Healthy"
#             break
#         fi
#
#         if [[ ${attempt} -eq ${max_attempts} ]]; then
#             log "ERROR" "❌ Java Character Service: Failed to start within timeout"
#             log "ERROR" "Check logs: ${LOG_DIR}/java-character-service.log"
#             return 1
#         fi
#
#         sleep 2
#         ((attempt++))
#     done
#
#     log "INFO" "Java services started successfully"
# }
#
# stop_java_services() {
#     log "INFO" "🛑 Stopping Java services..."
#
#     # Stop Java Character Service
#     if [[ -f "${PROJECT_ROOT}/pids/java-character-service.pid" ]]; then
#         local pid=$(cat "${PROJECT_ROOT}/pids/java-character-service.pid")
#         if kill -0 "$pid" 2>/dev/null; then
#             log "INFO" "Stopping Java Character Service (PID: $pid)..."
#             kill "$pid"
#
#             # Wait for graceful shutdown
#             local count=0
#             while kill -0 "$pid" 2>/dev/null && [[ $count -lt 30 ]]; do
#                 sleep 1
#                 ((count++))
#             done
#
#             # Force kill if still running
#             if kill -0 "$pid" 2>/dev/null; then
#                 log "WARN" "Force killing Java Character Service..."
#                 kill -9 "$pid"
#             fi
#         fi
#         rm -f "${PROJECT_ROOT}/pids/java-character-service.pid"
#     fi
#
#     log "INFO" "Java services stopped"
# }

# TODO 7: DATABASE INITIALIZATION
# initialize_database() {
#     log "INFO" "🗄️ Initializing database..."
#     
#     # Wait for MySQL to be ready
#     local max_attempts=30
#     local attempt=1
#     
#     while [[ ${attempt} -le ${max_attempts} ]]; do
#         log "INFO" "Checking database connectivity (attempt ${attempt}/${max_attempts})..."
#         
#         if docker exec onepiece-mysql mysqladmin ping -h localhost -u root -p"${DB_PASSWORD}" &>/dev/null; then
#             log "INFO" "✅ Database is ready"
#             break
#         fi
#         
#         if [[ ${attempt} -eq ${max_attempts} ]]; then
#             log "ERROR" "Database failed to start within timeout"
#             return 1
#         fi
#         
#         sleep 2
#         ((attempt++))
#     done
#     
#     # Run database setup
#     log "INFO" "Running database migrations..."
#     cd "${PROJECT_ROOT}/services/character-service"
#     
#     if ! python3 database_setup.py; then
#         log "ERROR" "Database setup failed"
#         return 1
#     fi
#     
#     log "INFO" "✅ Database initialized successfully"
# }

# TODO 8: SERVICE HEALTH CHECKS
# check_service_health() {
#     log "INFO" "🏥 Performing health checks..."
#
#     local services=(
#         "Node.js Character Service:http://localhost:5001/health"
#         "Java Character Service:http://localhost:8080/actuator/health"
#         "Trading Service:http://localhost:5002/health"
#         "User Service:http://localhost:5003/health"
#         "API Gateway:http://localhost:3000/health"
#         "Sentiment Service:http://localhost:8000/health"
#     )
#
#     local all_healthy=true
#
#     for service_info in "${services[@]}"; do
#         local service_name="${service_info%%:*}"
#         local health_url="${service_info##*:}"
#
#         log "INFO" "Checking ${service_name}..."
#
#         # Try health check with timeout
#         if curl -f -s --max-time 10 "${health_url}" > /dev/null; then
#             log "INFO" "✅ ${service_name}: Healthy"
#         else
#             log "WARN" "❌ ${service_name}: Unhealthy or unreachable"
#             # Don't fail deployment if one service is down (for comparison testing)
#             # all_healthy=false
#         fi
#     done
#
#     # Check database connectivity
#     log "INFO" "Checking database connectivity..."
#     if command -v psql &> /dev/null; then
#         if PGPASSWORD="${DB_PASSWORD}" psql -h localhost -U onepiece_user -d onepiece_trading -c "SELECT 1;" > /dev/null 2>&1; then
#             log "INFO" "✅ PostgreSQL: Healthy"
#         else
#             log "ERROR" "❌ PostgreSQL: Connection failed"
#             all_healthy=false
#         fi
#     fi
#
#     # Check Redis connectivity
#     log "INFO" "Checking Redis connectivity..."
#     if command -v redis-cli &> /dev/null; then
#         if redis-cli -h localhost -p 6379 ping > /dev/null 2>&1; then
#             log "INFO" "✅ Redis: Healthy"
#         else
#             log "ERROR" "❌ Redis: Connection failed"
#             all_healthy=false
#         fi
#     fi
#
#     if [[ "${all_healthy}" == "true" ]]; then
#         log "INFO" "🎉 All critical services are healthy!"
#         return 0
#     else
#         log "ERROR" "Some critical services are unhealthy"
#         return 1
#     fi
# }

# TODO 9: TESTING OPERATIONS
# run_tests() {
#     log "INFO" "🧪 Running automated tests..."
#     
#     # Python tests for Character Service
#     log "INFO" "Testing Character Service..."
#     cd "${PROJECT_ROOT}/services/character-service"
#     
#     if ! python3 -m pytest test_unit.py -v; then
#         log "ERROR" "Character Service unit tests failed"
#         return 1
#     fi
#     
#     if ! python3 test_api.py; then
#         log "ERROR" "Character Service API tests failed"
#         return 1
#     fi
#     
#     # C# tests for Trading Service
#     log "INFO" "Testing Trading Service..."
#     cd "${PROJECT_ROOT}/services/trading-service"
#     
#     if ! dotnet test --verbosity normal; then
#         log "ERROR" "Trading Service tests failed"
#         return 1
#     fi
#     
#     # Node.js tests for API Gateway
#     log "INFO" "Testing API Gateway..."
#     cd "${PROJECT_ROOT}/services/api-gateway"
#     
#     if ! npm test; then
#         log "ERROR" "API Gateway tests failed"
#         return 1
#     fi
#     
#     log "INFO" "✅ All tests passed successfully"
# }

# TODO 10: MONITORING SETUP
# setup_monitoring() {
#     log "INFO" "📊 Setting up monitoring..."
#     
#     # Create monitoring script
#     cat > "${PROJECT_ROOT}/scripts/monitor-services.sh" << 'EOF'
# #!/bin/bash
# # Service monitoring script
# 
# while true; do
#     echo "=== $(date) ==="
#     
#     # Check Docker containers
#     docker-compose ps
#     
#     # Check system resources
#     echo "Memory usage:"
#     free -h
#     
#     echo "Disk usage:"
#     df -h
#     
#     echo "CPU usage:"
#     top -bn1 | grep "Cpu(s)"
#     
#     sleep 60
# done
# EOF
#     
#     chmod +x "${PROJECT_ROOT}/scripts/monitor-services.sh"
#     log "INFO" "Monitoring script created"
# }

# TODO 11: BACKUP OPERATIONS
# create_backup() {
#     log "INFO" "💾 Creating backup..."
#     
#     local backup_dir="${PROJECT_ROOT}/backups/$(date +%Y%m%d_%H%M%S)"
#     mkdir -p "${backup_dir}"
#     
#     # Backup database
#     log "INFO" "Backing up database..."
#     docker exec onepiece-mysql mysqldump -u root -p"${DB_PASSWORD}" "${DB_NAME}" > "${backup_dir}/database.sql"
#     
#     # Backup configuration files
#     log "INFO" "Backing up configuration..."
#     cp -r "${CONFIG_DIR}" "${backup_dir}/"
#     
#     # Backup logs
#     log "INFO" "Backing up logs..."
#     cp -r "${LOG_DIR}" "${backup_dir}/"
#     
#     # Create archive
#     tar -czf "${backup_dir}.tar.gz" -C "${PROJECT_ROOT}/backups" "$(basename "${backup_dir}")"
#     rm -rf "${backup_dir}"
#     
#     log "INFO" "✅ Backup created: ${backup_dir}.tar.gz"
# }

# TODO 12: MAIN DEPLOYMENT FUNCTION
# main() {
#     log "INFO" "🏴‍☠️ Starting One Piece Stock Market deployment..."
#     log "INFO" "Environment: ${ENVIRONMENT}"
#     log "INFO" "Project Root: ${PROJECT_ROOT}"
#
#     # Setup
#     setup_logging
#     setup_error_handling
#
#     # Pre-deployment checks
#     check_system_requirements
#     load_configuration
#
#     # Deployment steps
#     start_docker_services
#     start_java_services      # Add Java services
#     initialize_database
#
#     # Wait for services to fully initialize
#     log "INFO" "Waiting for services to fully initialize..."
#     sleep 30
#
#     # Validation
#     check_service_health
#     run_tests
#
#     # Post-deployment setup
#     setup_monitoring
#     create_backup
#
#     # Success message
#     log "INFO" "🎉 Deployment completed successfully!"
#     log "INFO" "Services are available at:"
#     log "INFO" "  - Frontend: http://localhost:3000"
#     log "INFO" "  - API Gateway: http://localhost:3000/api"
#     log "INFO" "  - Node.js Character Service: http://localhost:5001"
#     log "INFO" "  - Java Character Service: http://localhost:8080"
#     log "INFO" "  - Trading Service: http://localhost:5002"
#     log "INFO" "  - User Service: http://localhost:5003"
#     log "INFO" "  - Sentiment Service: http://localhost:8000"
#     log "INFO" "  - PostgreSQL Database: localhost:5432"
#     log "INFO" "  - Redis Cache: localhost:6379"
#     log "INFO" ""
#     log "INFO" "🔥 JAVA ENTERPRISE FEATURES:"
#     log "INFO" "  - Health Check: http://localhost:8080/actuator/health"
#     log "INFO" "  - Metrics: http://localhost:8080/actuator/metrics"
#     log "INFO" "  - Info: http://localhost:8080/actuator/info"
#     log "INFO" "  - API Docs: http://localhost:8080/swagger-ui.html"
#     log "INFO" ""
#     log "INFO" "📊 PERFORMANCE COMPARISON:"
#     log "INFO" "  - Node.js Characters: curl http://localhost:5001/api/characters"
#     log "INFO" "  - Java Characters: curl http://localhost:8080/api/v1/characters"
#
#     log "INFO" "Log file: ${LOG_FILE}"
# }
#
# # TODO 12.1: CLEANUP FUNCTION
# cleanup_deployment() {
#     log "INFO" "🧹 Cleaning up deployment..."
#
#     # Stop Java services
#     stop_java_services
#
#     # Stop Docker services
#     if command -v docker-compose &> /dev/null; then
#         cd "${PROJECT_ROOT}"
#         docker-compose down --remove-orphans 2>/dev/null || true
#     fi
#
#     # Clean up PID files
#     rm -rf "${PROJECT_ROOT}/pids"
#
#     log "INFO" "Cleanup completed"
# }

# TODO 13: SCRIPT EXECUTION
# # Check if script is being sourced or executed
# if [[ "${BASH_SOURCE[0]}" == "${0}" ]]; then
#     main "$@"
# fi

# WHAT EACH FUNCTION DOES:
#
# setup_logging: Initialize logging system with timestamps and colors
# check_system_requirements: Verify all required tools and resources
# load_configuration: Parse JSON config files for environment settings
# start_docker_services: Build and start all Docker containers
# initialize_database: Set up MySQL database with schema and data
# check_service_health: Verify all services are running and healthy
# run_tests: Execute automated test suites for all services
# setup_monitoring: Create monitoring scripts and dashboards
# create_backup: Backup database and configuration files
#
# 🚀 BASH CONCEPTS YOU'LL LEARN:
#
# 1. Advanced scripting - Functions, arrays, conditionals
# 2. Error handling - set -euo pipefail, trap commands
# 3. Process management - Background jobs, process monitoring
# 4. File operations - Reading, writing, permissions
# 5. Network operations - curl, netstat, port checking
# 6. JSON processing - jq for configuration parsing
# 7. System administration - Service management, monitoring
#
# 📚 LINUX SYSTEM CONCEPTS:
#
# 1. Process management - ps, kill, jobs, nohup
# 2. File system - permissions, ownership, mounting
# 3. Network configuration - iptables, netstat, ss
# 4. System monitoring - top, htop, iostat, vmstat
# 5. Log management - journalctl, logrotate, rsyslog
# 6. Package management - apt, yum, dnf
# 7. Service management - systemctl, service
#
# USAGE EXAMPLES:
# ./deploy-onepiece-services.sh development
# ./deploy-onepiece-services.sh production
# ./deploy-onepiece-services.sh staging
#
# NEXT FILE AFTER THIS: Create Kubernetes deployment configurations! 🚀
