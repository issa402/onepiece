#!/bin/bash
# ═══════════════════════════════════════════════════════════════════════════════
# 🏆 FANZONE CONNECT - SERVER SETUP SCRIPT
# ═══════════════════════════════════════════════════════════════════════════════
#
# PURPOSE:
# Provisions a fresh Ubuntu server with everything needed to run FANZONE CONNECT.
# Run this once on a new server to set up the entire infrastructure.
#
# USAGE:
#   sudo ./setup-server.sh
#
# WHAT THIS SCRIPT INSTALLS AND CONFIGURES:
# 1. System updates and essential packages
# 2. Create deploy user with SSH key authentication
# 3. Configure firewall (UFW)
# 4. Install and configure Nginx (reverse proxy)
# 5. Install Python 3.11+ and pip
# 6. Install Node.js 20+ and npm
# 7. Install and configure PostgreSQL
# 8. Install and configure Redis
# 9. Install and configure MongoDB
# 10. Install Docker and Docker Compose
# 11. Set up SSL certificates with Let's Encrypt
# 12. Configure systemd services for each microservice
# 13. Set up log rotation
# 14. Configure automatic security updates
#
# LINUX/BASH CONCEPTS USED:
# - Package management (apt-get, apt)
# - User management (useradd, usermod, passwd)
# - Firewall configuration (ufw)
# - Service management (systemctl)
# - File permissions (chmod, chown)
# - Here documents (<<EOF)
# - Conditional checks for idempotency
# ═══════════════════════════════════════════════════════════════════════════════

# ─────────────────────────────────────────────────────────────────────────────
# CONFIGURATION
# ─────────────────────────────────────────────────────────────────────────────
# TODO: Define DEPLOY_USER (the user that will run the application)
# TODO: Define APP_DIR (where application code lives)
# TODO: Define DOMAIN (for SSL certificate)
# TODO: Define PYTHON_VERSION, NODE_VERSION
# TODO: Define database names and users

# ─────────────────────────────────────────────────────────────────────────────
# PRE-FLIGHT CHECKS
# ─────────────────────────────────────────────────────────────────────────────

check_root() {
    # TODO: Check if script is running as root
    # TODO: If not root, print error and exit
    # Hint: Check $EUID variable
    pass
}

check_ubuntu() {
    # TODO: Verify running on Ubuntu
    # TODO: Check /etc/os-release
    # TODO: Warn if not Ubuntu but continue
    pass
}

# ─────────────────────────────────────────────────────────────────────────────
# SYSTEM SETUP
# ─────────────────────────────────────────────────────────────────────────────

update_system() {
    # TODO: apt-get update
    # TODO: apt-get upgrade -y
    # TODO: Install essential packages (curl, wget, git, vim, htop, etc)
    pass
}

configure_timezone() {
    # TODO: Set timezone (timedatectl set-timezone)
    # TODO: Install and configure NTP for time sync
    pass
}

# ─────────────────────────────────────────────────────────────────────────────
# USER SETUP
# ─────────────────────────────────────────────────────────────────────────────

create_deploy_user() {
    # TODO: Check if user already exists
    # TODO: Create user with useradd -m -s /bin/bash
    # TODO: Add user to sudo group
    # TODO: Create .ssh directory
    # TODO: Set up authorized_keys (prompt for public key or copy from root)
    # TODO: Set correct permissions (700 for .ssh, 600 for authorized_keys)
    pass
}

configure_ssh() {
    # TODO: Backup original sshd_config
    # TODO: Disable root login (PermitRootLogin no)
    # TODO: Disable password authentication (PasswordAuthentication no)
    # TODO: Change SSH port if desired
    # TODO: Restart sshd
    pass
}

# ─────────────────────────────────────────────────────────────────────────────
# FIREWALL SETUP
# ─────────────────────────────────────────────────────────────────────────────

configure_firewall() {
    # TODO: Install ufw if not present
    # TODO: Set default policies (deny incoming, allow outgoing)
    # TODO: Allow SSH (port 22 or custom port)
    # TODO: Allow HTTP (port 80)
    # TODO: Allow HTTPS (port 443)
    # TODO: Enable ufw
    # TODO: Check ufw status
    pass
}

# ─────────────────────────────────────────────────────────────────────────────
# NGINX SETUP
# ─────────────────────────────────────────────────────────────────────────────

install_nginx() {
    # TODO: apt-get install nginx -y
    # TODO: Enable nginx service
    # TODO: Start nginx service
    pass
}

configure_nginx() {
    # TODO: Create nginx config for FANZONE CONNECT
    # TODO: Configure reverse proxy to API gateway (localhost:8000)
    # TODO: Configure WebSocket proxy for real-time features
    # TODO: Set up gzip compression
    # TODO: Configure security headers
    # TODO: Test config (nginx -t)
    # TODO: Reload nginx
    pass
}

# ─────────────────────────────────────────────────────────────────────────────
# PYTHON SETUP
# ─────────────────────────────────────────────────────────────────────────────

install_python() {
    # TODO: Add deadsnakes PPA for latest Python
    # TODO: apt-get install python3.11 python3.11-venv python3.11-dev
    # TODO: Install pip
    # TODO: Upgrade pip
    # TODO: Install virtualenv
    pass
}

# ─────────────────────────────────────────────────────────────────────────────
# NODE.JS SETUP
# ─────────────────────────────────────────────────────────────────────────────

install_nodejs() {
    # TODO: Add NodeSource repository
    # TODO: apt-get install nodejs
    # TODO: Install npm
    # TODO: Install pm2 globally (process manager)
    pass
}

# ─────────────────────────────────────────────────────────────────────────────
# DATABASE SETUP
# ─────────────────────────────────────────────────────────────────────────────

install_postgresql() {
    # TODO: apt-get install postgresql postgresql-contrib
    # TODO: Start and enable postgresql service
    # TODO: Create database user
    # TODO: Create database
    # TODO: Configure pg_hba.conf for local connections
    # TODO: Restart postgresql
    pass
}

install_redis() {
    # TODO: apt-get install redis-server
    # TODO: Configure redis.conf (bind to localhost, set maxmemory)
    # TODO: Enable and start redis service
    pass
}

install_mongodb() {
    # TODO: Add MongoDB repository
    # TODO: apt-get install mongodb-org
    # TODO: Enable and start mongod service
    # TODO: Create admin user
    # TODO: Enable authentication
    pass
}

# ─────────────────────────────────────────────────────────────────────────────
# DOCKER SETUP
# ─────────────────────────────────────────────────────────────────────────────

install_docker() {
    # TODO: Install prerequisites
    # TODO: Add Docker GPG key
    # TODO: Add Docker repository
    # TODO: apt-get install docker-ce docker-ce-cli containerd.io
    # TODO: Add deploy user to docker group
    # TODO: Install docker-compose
    pass
}

# ─────────────────────────────────────────────────────────────────────────────
# SSL SETUP
# ─────────────────────────────────────────────────────────────────────────────

setup_ssl() {
    # TODO: Install certbot
    # TODO: Run certbot for nginx
    # TODO: Set up auto-renewal cron job
    pass
}

# ─────────────────────────────────────────────────────────────────────────────
# APPLICATION SETUP
# ─────────────────────────────────────────────────────────────────────────────

setup_app_directory() {
    # TODO: Create APP_DIR
    # TODO: Set ownership to DEPLOY_USER
    # TODO: Clone repository (or prepare for first deploy)
    pass
}

create_systemd_services() {
    # TODO: Create systemd service file for each microservice
    # TODO: api-gateway.service
    # TODO: user-service.service
    # TODO: match-service.service
    # TODO: notification-service.service
    # TODO: Enable all services
    pass
}

# ─────────────────────────────────────────────────────────────────────────────
# LOGGING AND MAINTENANCE
# ─────────────────────────────────────────────────────────────────────────────

setup_log_rotation() {
    # TODO: Create logrotate config for application logs
    # TODO: Configure rotation frequency and retention
    pass
}

setup_automatic_updates() {
    # TODO: Install unattended-upgrades
    # TODO: Configure for security updates only
    pass
}

# ─────────────────────────────────────────────────────────────────────────────
# MAIN EXECUTION
# ─────────────────────────────────────────────────────────────────────────────

main() {
    # TODO: Call check_root
    # TODO: Call check_ubuntu
    # TODO: Call update_system
    # TODO: Call configure_timezone
    # TODO: Call create_deploy_user
    # TODO: Call configure_ssh
    # TODO: Call configure_firewall
    # TODO: Call install_nginx
    # TODO: Call configure_nginx
    # TODO: Call install_python
    # TODO: Call install_nodejs
    # TODO: Call install_postgresql
    # TODO: Call install_redis
    # TODO: Call install_mongodb
    # TODO: Call install_docker
    # TODO: Call setup_app_directory
    # TODO: Call create_systemd_services
    # TODO: Call setup_log_rotation
    # TODO: Call setup_automatic_updates
    # TODO: Call setup_ssl (after DNS is configured)
    # TODO: Print summary of what was installed
    # TODO: Print next steps for user
    pass
}

# main

