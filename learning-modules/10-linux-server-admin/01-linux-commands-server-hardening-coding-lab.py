"""
🏴‍☠️ LINUX & SERVER ADMINISTRATION MASTERY - HANDS-ON CODING LAB
═══════════════════════════════════════════════════════════

🎯 WHAT YOU'LL CODE TODAY:
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
✅ Advanced Linux commands for One Piece server management
✅ Server hardening and security configuration
✅ Process management and system monitoring
✅ Network configuration and troubleshooting
✅ Automated server provisioning and configuration
✅ Performance tuning and optimization

💰 SALARY IMPACT: +?0K-$80K (Linux expertise is ESSENTIAL)
🏢 COMPANIES: Every tech company (Linux runs the internet)

📚 WHY LINUX MASTERY = HIGH SALARY:
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

🔥 LINUX POWERS THE WORLD:

1. MARKET DOMINANCE:
   - 96.3% of top 1 million web servers run Linux
   - 100% of supercomputers run Linux
   - 85% of smartphones run Linux (Android)
   - All major cloud providers use Linux

2. ENTERPRISE ADOPTION:
   - Netflix: 100,000+ Linux servers
   - Google: Millions of Linux servers
   - Facebook: Custom Linux distributions
   - Amazon: Linux powers AWS infrastructure

3. COST SAVINGS:
   - No licensing fees (vs Windows Server)
   - Better performance on same hardware
   - Superior security and stability
   - Extensive automation capabilities

🔥 WHY COMPANIES PAY PREMIUM FOR LINUX ENGINEERS:

1. CRITICAL INFRASTRUCTURE:
   - Production servers require Linux expertise
   - Downtime costs thousands per minute
   - Security breaches cost millions
   - Performance optimization saves money

2. AUTOMATION AND DEVOPS:
   - Infrastructure as Code (Terraform, Ansible)
   - CI/CD pipelines require Linux knowledge
   - Container orchestration (Docker, Kubernetes)
   - Monitoring and logging systems

3. TROUBLESHOOTING SKILLS:
   - Complex system debugging
   - Performance bottleneck identification
   - Network connectivity issues
   - Security incident response

📖 ESSENTIAL RESOURCES:
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
🔗 Linux Command Line: https://linuxcommand.org/
🔗 Red Hat System Admin: https://www.redhat.com/en/services/training
🔗 Linux Security: https://linux-audit.com/
🔗 Performance Tuning: https://www.brendangregg.com/linuxperf.html
🔗 Server Hardening: https://www.cisecurity.org/cis-benchmarks/
"""

# ═══════════════════════════════════════════════════════════
# 🧪 HANDS-ON LAB 1: ADVANCED LINUX COMMANDS FOR ONE PIECE
# ═══════════════════════════════════════════════════════════

"""
📚 ESSENTIAL LINUX COMMANDS FOR ONE PIECE SERVER MANAGEMENT:

🔥 SYSTEM MONITORING COMMANDS:

1. PROCESS MANAGEMENT:
   - ps aux | grep onepiece  # Find One Piece processes
   - top -p $(mysql2rep -d',' onepiece)  # Monitor specific processes
   - htop  # Interactive process viewer
   - pstree  # Process tree visualization

2. SYSTEM RESOURCES:
   - free -h  # Memory usage
   - df -h  # Disk usage
   - du -sh /var/log/onepiece/  # Directory size
   - iostat -x 1  # I/O statistics

3. NETWORK MONITORING:
   - netstat -tulpn | grep :8000  # Check port usage
   - ss -tulpn  # Modern netstat replacement
   - iftop  # Network bandwidth usage
   - tcpdump -i eth0 port 8000  # Packet capture

4. LOG ANALYSIS:
   - tail -f /var/log/onepiece/trading.log  # Follow log files
   - grep -r "ERROR" /var/log/onepiece/  # Search for errors
   - journalctl -u onepiece-api -f  # Systemd service logs
   - awk '/ERROR/ {print ?, ?, $NF}' /var/log/onepiece/app.log  # Parse logs

🎯 YOUR CODING MISSION:
Master Linux commands for One Piece server administration!
"""

# TODO 1: CREATE SERVER MONITORING SCRIPTS
# ═══════════════════════════════════════════════════════════
"""
🎯 YOUR TASK: Create comprehensive server monitoring scripts

Create file: scripts/server-monitoring.sh
"""

# FILE: scripts/server-monitoring.sh
# YOUR CODE HERE - Create server monitoring script:
"""
#!/bin/bash

# One Piece Server Monitoring Script
# Monitors system health and One Piece application performance

set -e

# Configuration
LOG_FILE="/var/log/onepiece/monitoring.log"
ALERT_EMAIL="admin@onepiece-trading.com"
CPU_THRESHOLD=80
MEMORY_THRESHOLD=85
DISK_THRESHOLD=90

# Colors for output
RED='\\033[0;31m'
GREEN='\\033[0;32m'
YELLOW='\\033[1;33m'
NC='\\033[0m' # No Color

# Logging function
log_message() {
    echo "$(date '+%Y-%m-%d %H:%M:%S') - ?" | tee -a "$LOG_FILE"
}

# Check system resources
check_system_resources() {
    log_message "🔍 Checking system resources..."
    
    # Check CPU usage
    CPU_USAGE=$(# Add command to get CPU usage)
    if [ "$CPU_USAGE" -gt "$CPU_THRESHOLD" ]; then
        log_message "${RED}⚠️  HIGH CPU USAGE: ${CPU_USAGE}%${NC}"
        # Add alert logic
    else
        log_message "${GREEN}✅ CPU Usage: ${CPU_USAGE}%${NC}"
    fi
    
    # Check memory usage
    MEMORY_USAGE=$(# Add command to get memory usage)
    if [ "$MEMORY_USAGE" -gt "$MEMORY_THRESHOLD" ]; then
        log_message "${RED}⚠️  HIGH MEMORY USAGE: ${MEMORY_USAGE}%${NC}"
        # Add alert logic
    else
        log_message "${GREEN}✅ Memory Usage: ${MEMORY_USAGE}%${NC}"
    fi
    
    # Check disk usage
    DISK_USAGE=$(# Add command to get disk usage)
    if [ "$DISK_USAGE" -gt "$DISK_THRESHOLD" ]; then
        log_message "${RED}⚠️  HIGH DISK USAGE: ${DISK_USAGE}%${NC}"
        # Add alert logic
    else
        log_message "${GREEN}✅ Disk Usage: ${DISK_USAGE}%${NC}"
    fi
}

# Check One Piece application health
check_onepiece_health() {
    log_message "🏴‍☠️ Checking One Piece application health..."
    
    # Check if Django API is running
    if mysql2rep -f "onepiece-api" > /dev/null; then
        log_message "${GREEN}✅ Django API is running${NC}"
        
        # Check API response
        API_RESPONSE=$(# Add curl command to check API health)
        if [ "$?" -eq 0 ]; then
            log_message "${GREEN}✅ API health check passed${NC}"
        else
            log_message "${RED}❌ API health check failed${NC}"
            # Add restart logic
        fi
    else
        log_message "${RED}❌ Django API is not running${NC}"
        # Add restart logic
    fi
    
    # Check database connectivity
    DB_STATUS=$(# Add command to check database)
    if [ "$?" -eq 0 ]; then
        log_message "${GREEN}✅ Database connection OK${NC}"
    else
        log_message "${RED}❌ Database connection failed${NC}"
        # Add alert logic
    fi
    
    # Check Redis connectivity
    REDIS_STATUS=$(# Add command to check Redis)
    if [ "$?" -eq 0 ]; then
        log_message "${GREEN}✅ Redis connection OK${NC}"
    else
        log_message "${RED}❌ Redis connection failed${NC}"
        # Add alert logic
    fi
}

# Check network connectivity
check_network() {
    log_message "🌐 Checking network connectivity..."
    
    # Check internet connectivity
    if ping -c 1 google.com > /dev/null 2>&1; then
        log_message "${GREEN}✅ Internet connectivity OK${NC}"
    else
        log_message "${RED}❌ Internet connectivity failed${NC}"
    fi
    
    # Check port availability
    PORTS=("8000" "3306" "6379")
    for port in "${PORTS[@]}"; do
        if netstat -tulpn | grep ":$port " > /dev/null; then
            log_message "${GREEN}✅ Port $port is open${NC}"
        else
            log_message "${YELLOW}⚠️  Port $port is not open${NC}"
        fi
    done
}

# Main monitoring function
main() {
    log_message "🚀 Starting One Piece server monitoring..."
    
    check_system_resources
    check_onepiece_health
    check_network
    
    log_message "✅ Monitoring completed"
}

# Run monitoring
main
"""

# TODO 2: CREATE SYSTEM PERFORMANCE ANALYSIS
# ═══════════════════════════════════════════════════════════
"""
🎯 YOUR TASK: Create performance analysis and optimization script

Create file: scripts/performance-analysis.sh
"""

# FILE: scripts/performance-analysis.sh
# YOUR CODE HERE - Create performance analysis script:
"""
#!/bin/bash

# One Piece Performance Analysis Script
# Analyzes system performance and identifies bottlenecks

# Performance analysis functions
analyze_cpu_performance() {
    echo "🔥 CPU Performance Analysis"
    echo "=========================="
    
    # CPU information
    echo "CPU Information:"
    # Add command to show CPU info
    
    # CPU usage by process
    echo "Top CPU consuming processes:"
    # Add command to show top CPU processes
    
    # Load average
    echo "System Load Average:"
    # Add command to show load average
}

analyze_memory_performance() {
    echo "💾 Memory Performance Analysis"
    echo "============================="
    
    # Memory usage
    echo "Memory Usage:"
    # Add command to show memory usage
    
    # Top memory consuming processes
    echo "Top Memory consuming processes:"
    # Add command to show top memory processes
    
    # Swap usage
    echo "Swap Usage:"
    # Add command to show swap usage
}

analyze_disk_performance() {
    echo "💿 Disk Performance Analysis"
    echo "==========================="
    
    # Disk usage
    echo "Disk Usage:"
    # Add command to show disk usage
    
    # I/O statistics
    echo "I/O Statistics:"
    # Add command to show I/O stats
    
    # Disk performance
    echo "Disk Performance Test:"
    # Add command to test disk performance
}

analyze_network_performance() {
    echo "🌐 Network Performance Analysis"
    echo "=============================="
    
    # Network interfaces
    echo "Network Interfaces:"
    # Add command to show network interfaces
    
    # Network statistics
    echo "Network Statistics:"
    # Add command to show network stats
    
    # Connection states
    echo "Connection States:"
    # Add command to show connection states
}

# Run all analyses
main() {
    echo "🏴‍☠️ One Piece Server Performance Analysis"
    echo "=========================================="
    echo "Timestamp: $(date)"
    echo ""
    
    analyze_cpu_performance
    echo ""
    analyze_memory_performance
    echo ""
    analyze_disk_performance
    echo ""
    analyze_network_performance
    
    echo ""
    echo "✅ Performance analysis completed"
}

main
"""

# ═══════════════════════════════════════════════════════════
# 🧪 HANDS-ON LAB 2: SERVER HARDENING AND SECURITY
# ═══════════════════════════════════════════════════════════

"""
📚 SERVER HARDENING FOR ONE PIECE TRADING PLATFORM:

🔥 CRITICAL SECURITY MEASURES:

1. USER AND ACCESS MANAGEMENT:
   - Disable root login
   - Create dedicated service users
   - Implement sudo access controls
   - Set up SSH key authentication

2. FIREWALL CONFIGURATION:
   - Configure iptables/ufw rules
   - Block unnecessary ports
   - Allow only required services
   - Set up fail2ban for intrusion prevention

3. SYSTEM UPDATES AND PATCHES:
   - Automated security updates
   - Regular system patching
   - Vulnerability scanning
   - Package management

4. LOGGING AND MONITORING:
   - Centralized logging
   - Security event monitoring
   - File integrity monitoring
   - Intrusion detection

🎯 YOUR CODING MISSION:
Harden your One Piece servers like a fortress!
"""

# TODO 3: CREATE SERVER HARDENING SCRIPT
# ═══════════════════════════════════════════════════════════
"""
🎯 YOUR TASK: Create comprehensive server hardening script

Create file: scripts/server-hardening.sh
"""

# FILE: scripts/server-hardening.sh
# YOUR CODE HERE - Create server hardening script:
"""
#!/bin/bash

# One Piece Server Hardening Script
# Implements security best practices for production servers

set -e

# Configuration
ONEPIECE_USER="onepiece"
SSH_PORT="2222"
LOG_FILE="/var/log/server-hardening.log"

# Logging function
log_action() {
    echo "$(date '+%Y-%m-%d %H:%M:%S') - ?" | tee -a "$LOG_FILE"
}

# Update system packages
update_system() {
    log_action "🔄 Updating system packages..."
    
    # Update package lists
    # Add command to update package lists
    
    # Umysql2rade packages
    # Add command to umysql2rade packages
    
    # Install security updates
    # Add command for security updates
    
    log_action "✅ System packages updated"
}

# Configure firewall
configure_firewall() {
    log_action "🔥 Configuring firewall..."
    
    # Install ufw if not present
    # Add command to install ufw
    
    # Reset firewall rules
    # Add command to reset ufw
    
    # Default policies
    # Add commands to set default policies
    
    # Allow SSH (custom port)
    # Add command to allow SSH
    
    # Allow HTTP and HTTPS
    # Add commands to allow web traffic
    
    # Allow One Piece application ports
    # Add commands to allow app ports
    
    # Enable firewall
    # Add command to enable ufw
    
    log_action "✅ Firewall configured"
}

# Secure SSH configuration
secure_ssh() {
    log_action "🔐 Securing SSH configuration..."
    
    # Backup original SSH config
    # Add command to backup SSH config
    
    # Configure SSH settings
    cat > /etc/ssh/sshd_config.d/onepiece-hardening.conf << EOF
# One Piece SSH Hardening Configuration
Port $SSH_PORT
PermitRootLogin no
PasswordAuthentication no
PubkeyAuthentication yes
X11Forwarding no
AllowUsers $ONEPIECE_USER
MaxAuthTries 3
ClientAliveInterval 300
ClientAliveCountMax 2
EOF
    
    # Restart SSH service
    # Add command to restart SSH
    
    log_action "✅ SSH secured"
}

# Create service user
create_service_user() {
    log_action "👤 Creating service user..."
    
    # Create onepiece user
    if ! id "$ONEPIECE_USER" &>/dev/null; then
        # Add command to create user
        log_action "✅ User $ONEPIECE_USER created"
    else
        log_action "ℹ️  User $ONEPIECE_USER already exists"
    fi
    
    # Set up sudo access
    echo "$ONEPIECE_USER ALL=(ALL) NOPASSWD:/usr/bin/systemctl restart onepiece-*" > /etc/sudoers.d/onepiece
    
    # Create SSH directory
    # Add commands to set up SSH directory
}

# Install and configure fail2ban
configure_fail2ban() {
    log_action "🛡️  Configuring fail2ban..."
    
    # Install fail2ban
    # Add command to install fail2ban
    
    # Configure fail2ban for SSH
    cat > /etc/fail2ban/jail.d/onepiece.conf << EOF
[sshd]
enabled = true
port = $SSH_PORT
filter = sshd
logpath = /var/log/auth.log
maxretry = 3
bantime = 3600
findtime = 600

[onepiece-api]
enabled = true
port = 8000
filter = onepiece-api
logpath = /var/log/onepiece/access.log
maxretry = 10
bantime = 1800
findtime = 300
EOF
    
    # Create custom filter for One Piece API
    cat > /etc/fail2ban/filter.d/onepiece-api.conf << EOF
[Definition]
failregex = ^<HOST> .* ".*" 4\d\d \d+$
ignoreregex =
EOF
    
    # Start and enable fail2ban
    # Add commands to start fail2ban
    
    log_action "✅ Fail2ban configured"
}

# Set up automatic security updates
configure_auto_updates() {
    log_action "🔄 Configuring automatic security updates..."
    
    # Install unattended-umysql2rades
    # Add command to install unattended-umysql2rades
    
    # Configure automatic updates
    cat > /etc/apt/apt.conf.d/50unattended-umysql2rades << EOF
Unattended-Umysql2rade::Allowed-Origins {
    "\${distro_id}:\${distro_codename}-security";
    "\${distro_id}ESMApps:\${distro_codename}-apps-security";
    "\${distro_id}ESM:\${distro_codename}-infra-security";
};

Unattended-Umysql2rade::AutoFixInterruptedDpkg "true";
Unattended-Umysql2rade::MinimalSteps "true";
Unattended-Umysql2rade::Remove-Unused-Dependencies "true";
Unattended-Umysql2rade::Automatic-Reboot "false";
EOF
    
    # Enable automatic updates
    # Add command to enable auto updates
    
    log_action "✅ Automatic security updates configured"
}

# Main hardening function
main() {
    log_action "🏴‍☠️ Starting One Piece server hardening..."
    
    # Check if running as root
    if [ "$EUID" -ne 0 ]; then
        echo "❌ This script must be run as root"
        exit 1
    fi
    
    update_system
    create_service_user
    secure_ssh
    configure_firewall
    configure_fail2ban
    configure_auto_updates
    
    log_action "✅ Server hardening completed successfully!"
    log_action "⚠️  Remember to:"
    log_action "   1. Set up SSH keys for the $ONEPIECE_USER user"
    log_action "   2. Test SSH access on port $SSH_PORT"
    log_action "   3. Update firewall rules as needed"
    log_action "   4. Monitor fail2ban logs"
}

main "$@"
"""

# TODO 4: CREATE SYSTEM BACKUP SCRIPT
# ═══════════════════════════════════════════════════════════
"""
🎯 YOUR TASK: Create automated backup system

Create file: scripts/backup-system.sh
"""

# FILE: scripts/backup-system.sh
# YOUR CODE HERE - Create backup script:
"""
#!/bin/bash

# One Piece System Backup Script
# Creates comprehensive backups of system and application data

# Configuration
BACKUP_DIR="/backup/onepiece"
RETENTION_DAYS=30
DATABASE_NAME="onepiece_market"
S3_BUCKET="onepiece-backups"

# Backup functions
backup_database() {
    echo "🗄️  Backing up database..."
    
    # Create database backup
    # Add command to backup MySQL database
    
    # Compress backup
    # Add command to compress backup
    
    echo "✅ Database backup completed"
}

backup_application_data() {
    echo "📁 Backing up application data..."
    
    # Backup application files
    # Add commands to backup app files
    
    # Backup configuration files
    # Add commands to backup configs
    
    # Backup logs
    # Add commands to backup logs
    
    echo "✅ Application data backup completed"
}

backup_system_config() {
    echo "⚙️  Backing up system configuration..."
    
    # Backup system configs
    # Add commands to backup system files
    
    echo "✅ System configuration backup completed"
}

upload_to_cloud() {
    echo "☁️  Uploading backups to cloud storage..."
    
    # Upload to S3
    # Add commands to upload to S3
    
    echo "✅ Cloud upload completed"
}

cleanup_old_backups() {
    echo "🧹 Cleaning up old backups..."
    
    # Remove local backups older than retention period
    # Add commands to cleanup old backups
    
    echo "✅ Cleanup completed"
}

# Main backup function
main() {
    echo "🏴‍☠️ Starting One Piece system backup..."
    echo "Timestamp: $(date)"
    
    # Create backup directory
    mkdir -p "$BACKUP_DIR/$(date +%Y-%m-%d)"
    cd "$BACKUP_DIR/$(date +%Y-%m-%d)"
    
    backup_database
    backup_application_data
    backup_system_config
    upload_to_cloud
    cleanup_old_backups
    
    echo "✅ Backup process completed successfully!"
}

main
"""

# ═══════════════════════════════════════════════════════════
# 🧪 HANDS-ON LAB 3: PROCESS MANAGEMENT AND AUTOMATION
# ═══════════════════════════════════════════════════════════

"""
📚 PROCESS MANAGEMENT FOR ONE PIECE PLATFORM:

🔥 SYSTEMD SERVICE MANAGEMENT:

1. SERVICE CREATION:
   - Create systemd service files
   - Configure service dependencies
   - Set up environment variables
   - Define restart policies

2. PROCESS MONITORING:
   - Monitor service health
   - Automatic restart on failure
   - Resource limits and controls
   - Logging configuration

3. AUTOMATION:
   - Scheduled tasks with cron
   - Log rotation
   - Health checks
   - Maintenance scripts

🎯 YOUR CODING MISSION:
Automate One Piece platform management!
"""

# TODO 5: CREATE SYSTEMD SERVICE FILES
# ═══════════════════════════════════════════════════════════
"""
🎯 YOUR TASK: Create systemd service files for One Piece services

Create file: /etc/systemd/system/onepiece-api.service
"""

# FILE: /etc/systemd/system/onepiece-api.service
# YOUR CODE HERE - Create systemd service:
"""
[Unit]
Description=One Piece Trading API Service
After=network.target mysqlql.service redis.service
Wants=mysqlql.service redis.service

[Service]
Type=# Add service type
User=# Add user
Group=# Add group
WorkingDirectory=# Add working directory
Environment=# Add environment variables
ExecStart=# Add start command
ExecReload=# Add reload command
Restart=# Add restart policy
RestartSec=# Add restart delay
StandardOutput=# Add output logging
StandardError=# Add error logging
SyslogIdentifier=# Add syslog identifier

# Security settings
NoNewPrivileges=# Add security setting
PrivateTmp=# Add private tmp
ProtectSystem=# Add system protection
ProtectHome=# Add home protection

# Resource limits
LimitNOFILE=# Add file limit
LimitNPROC=# Add process limit
MemoryLimit=# Add memory limit

[Install]
WantedBy=# Add target
"""

# TODO 6: CREATE AUTOMATED MAINTENANCE SCRIPT
# ═══════════════════════════════════════════════════════════
"""
🎯 YOUR TASK: Create automated maintenance and health check script

Create file: scripts/maintenance.sh
"""

# FILE: scripts/maintenance.sh
# YOUR CODE HERE - Create maintenance script:
"""
#!/bin/bash

# One Piece Automated Maintenance Script
# Performs regular maintenance tasks

# Maintenance functions
cleanup_logs() {
    echo "🧹 Cleaning up old log files..."
    
    # Clean application logs older than 30 days
    # Add commands to clean logs
    
    # Rotate large log files
    # Add commands to rotate logs
    
    echo "✅ Log cleanup completed"
}

optimize_database() {
    echo "🗄️  Optimizing database..."
    
    # Vacuum and analyze MySQL
    # Add commands to optimize database
    
    # Update statistics
    # Add commands to update stats
    
    echo "✅ Database optimization completed"
}

clear_cache() {
    echo "🚀 Clearing application cache..."
    
    # Clear Redis cache
    # Add commands to clear cache
    
    # Clear application cache
    # Add commands to clear app cache
    
    echo "✅ Cache clearing completed"
}

check_disk_space() {
    echo "💿 Checking disk space..."
    
    # Check disk usage and alert if high
    DISK_USAGE=$(df / | awk 'NR==2 {print ?}' | sed 's/%//')
    
    if [ "$DISK_USAGE" -gt 85 ]; then
        echo "⚠️  WARNING: Disk usage is ${DISK_USAGE}%"
        # Add alert logic
    else
        echo "✅ Disk usage is ${DISK_USAGE}% - OK"
    fi
}

update_ssl_certificates() {
    echo "🔐 Checking SSL certificates..."
    
    # Check certificate expiration
    # Add commands to check SSL certs
    
    # Renew if needed
    # Add commands to renew certs
    
    echo "✅ SSL certificate check completed"
}

# Main maintenance function
main() {
    echo "🏴‍☠️ Starting One Piece maintenance..."
    echo "Timestamp: $(date)"
    
    cleanup_logs
    optimize_database
    clear_cache
    check_disk_space
    update_ssl_certificates
    
    echo "✅ Maintenance completed successfully!"
}

main
"""

# TODO 7: CREATE CRON JOBS CONFIGURATION
# ═══════════════════════════════════════════════════════════
"""
🎯 YOUR TASK: Set up automated cron jobs for One Piece platform

Create file: scripts/setup-cron-jobs.sh
"""

# FILE: scripts/setup-cron-jobs.sh
# YOUR CODE HERE - Create cron setup script:
"""
#!/bin/bash

# One Piece Cron Jobs Setup Script
# Sets up automated scheduled tasks

# Create cron jobs for onepiece user
setup_cron_jobs() {
    echo "⏰ Setting up cron jobs for One Piece platform..."
    
    # Create crontab for onepiece user
    cat > /tmp/onepiece-crontab << EOF
# One Piece Trading Platform Cron Jobs

# System monitoring every 5 minutes
*/5 * * * * /opt/onepiece/scripts/server-monitoring.sh >> /var/log/onepiece/monitoring.log 2>&1

# Database backup daily at 2 AM
0 2 * * * /opt/onepiece/scripts/backup-system.sh >> /var/log/onepiece/backup.log 2>&1

# Maintenance tasks daily at 3 AM
0 3 * * * /opt/onepiece/scripts/maintenance.sh >> /var/log/onepiece/maintenance.log 2>&1

# Performance analysis weekly on Sunday at 4 AM
0 4 * * 0 /opt/onepiece/scripts/performance-analysis.sh >> /var/log/onepiece/performance.log 2>&1

# Log rotation daily at 1 AM
0 1 * * * /usr/sbin/logrotate /etc/logrotate.d/onepiece

# SSL certificate check weekly on Monday at 5 AM
0 5 * * 1 /opt/onepiece/scripts/check-ssl-certs.sh >> /var/log/onepiece/ssl.log 2>&1

# Clean temporary files daily at 6 AM
0 6 * * * find /tmp -name "onepiece-*" -mtime +1 -delete

# Update character prices every minute (trading hours only)
* 9-17 * * 1-5 /opt/onepiece/scripts/update-prices.sh >> /var/log/onepiece/prices.log 2>&1
EOF
    
    # Install crontab for onepiece user
    crontab -u onepiece /tmp/onepiece-crontab
    
    # Remove temporary file
    rm /tmp/onepiece-crontab
    
    echo "✅ Cron jobs installed successfully"
    
    # Show installed cron jobs
    echo "📋 Installed cron jobs:"
    crontab -u onepiece -l
}

# Create log rotation configuration
setup_log_rotation() {
    echo "🔄 Setting up log rotation..."
    
    cat > /etc/logrotate.d/onepiece << EOF
/var/log/onepiece/*.log {
    daily
    missingok
    rotate 30
    compress
    delaycompress
    notifempty
    create 644 onepiece onepiece
    postrotate
        systemctl reload onepiece-api
    endscript
}
EOF
    
    echo "✅ Log rotation configured"
}

# Main setup function
main() {
    echo "🏴‍☠️ Setting up One Piece automation..."
    
    # Check if running as root
    if [ "$EUID" -ne 0 ]; then
        echo "❌ This script must be run as root"
        exit 1
    fi
    
    setup_cron_jobs
    setup_log_rotation
    
    echo "✅ Automation setup completed!"
    echo "📝 Remember to monitor cron job execution in logs"
}

main
"""

# ═══════════════════════════════════════════════════════════
# ✅ COMPLETE CODE SOLUTION (SCROLL DOWN TO CHECK YOUR WORK)
# ═══════════════════════════════════════════════════════════
