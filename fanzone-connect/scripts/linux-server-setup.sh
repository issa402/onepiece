#!/bin/bash

# 🏆 FANZONE CONNECT - LINUX SERVER SETUP SCRIPT
# Module 10: Linux Server Administration - Production Server Configuration
# World Cup 2026 Fan Platform - Complete Server Hardening & Optimization

set -euo pipefail  # Exit on error, undefined vars, pipe failures

# Colors for output
RED='\033[0;31m'
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
BLUE='\033[0;34m'
NC='\033[0m' # No Color

# Logging function
log() {
    echo -e "${GREEN}[$(date +'%Y-%m-%d %H:%M:%S')] $1${NC}"
}

error() {
    echo -e "${RED}[ERROR] $1${NC}" >&2
}

warning() {
    echo -e "${YELLOW}[WARNING] $1${NC}"
}

info() {
    echo -e "${BLUE}[INFO] $1${NC}"
}

# Check if running as root
check_root() {
    if [[ $EUID -eq 0 ]]; then
        error "This script should not be run as root for security reasons"
        exit 1
    fi
}

# System information
show_system_info() {
    log "🏆 FANZONE CONNECT - World Cup 2026 Server Setup"
    log "=================================================="
    info "OS: $(lsb_release -d | cut -f2)"
    info "Kernel: $(uname -r)"
    info "Architecture: $(uname -m)"
    info "CPU: $(nproc) cores"
    info "Memory: $(free -h | awk '/^Mem:/ {print $2}')"
    info "Disk: $(df -h / | awk 'NR==2 {print $2}')"
    log "=================================================="
}

# Update system packages
update_system() {
    log "📦 Updating system packages..."
    
    sudo apt update && sudo apt upgrade -y
    sudo apt autoremove -y
    sudo apt autoclean
    
    # Install essential packages
    sudo apt install -y \
        curl \
        wget \
        git \
        vim \
        htop \
        tree \
        unzip \
        software-properties-common \
        apt-transport-https \
        ca-certificates \
        gnupg \
        lsb-release \
        fail2ban \
        ufw \
        logrotate \
        rsync \
        screen \
        tmux
    
    log "✅ System packages updated successfully"
}

# Configure firewall
setup_firewall() {
    log "🔥 Configuring UFW firewall..."
    
    # Reset UFW to defaults
    sudo ufw --force reset
    
    # Default policies
    sudo ufw default deny incoming
    sudo ufw default allow outgoing
    
    # Allow SSH (change port if needed)
    sudo ufw allow 22/tcp comment 'SSH'
    
    # Allow HTTP and HTTPS
    sudo ufw allow 80/tcp comment 'HTTP'
    sudo ufw allow 443/tcp comment 'HTTPS'
    
    # Allow application ports
    sudo ufw allow 3000/tcp comment 'Frontend'
    sudo ufw allow 8000/tcp comment 'API Gateway'
    sudo ufw allow 5432/tcp comment 'PostgreSQL'
    sudo ufw allow 6379/tcp comment 'Redis'
    sudo ufw allow 9090/tcp comment 'Prometheus'
    sudo ufw allow 3001/tcp comment 'Grafana'
    
    # Enable UFW
    sudo ufw --force enable
    
    log "✅ Firewall configured successfully"
}

# Configure Fail2Ban
setup_fail2ban() {
    log "🛡️ Configuring Fail2Ban..."
    
    # Create custom jail configuration
    sudo tee /etc/fail2ban/jail.local > /dev/null <<EOF
[DEFAULT]
bantime = 3600
findtime = 600
maxretry = 5
backend = systemd

[sshd]
enabled = true
port = ssh
filter = sshd
logpath = /var/log/auth.log
maxretry = 3
bantime = 7200

[nginx-http-auth]
enabled = true
filter = nginx-http-auth
port = http,https
logpath = /var/log/nginx/error.log
maxretry = 3

[nginx-limit-req]
enabled = true
filter = nginx-limit-req
port = http,https
logpath = /var/log/nginx/error.log
maxretry = 10
EOF

    sudo systemctl enable fail2ban
    sudo systemctl restart fail2ban
    
    log "✅ Fail2Ban configured successfully"
}

# Install Docker
install_docker() {
    log "🐳 Installing Docker..."
    
    # Remove old versions
    sudo apt remove -y docker docker-engine docker.io containerd runc 2>/dev/null || true
    
    # Add Docker's official GPG key
    curl -fsSL https://download.docker.com/linux/ubuntu/gpg | sudo gpg --dearmor -o /usr/share/keyrings/docker-archive-keyring.gpg
    
    # Add Docker repository
    echo "deb [arch=$(dpkg --print-architecture) signed-by=/usr/share/keyrings/docker-archive-keyring.gpg] https://download.docker.com/linux/ubuntu $(lsb_release -cs) stable" | sudo tee /etc/apt/sources.list.d/docker.list > /dev/null
    
    # Install Docker
    sudo apt update
    sudo apt install -y docker-ce docker-ce-cli containerd.io docker-compose-plugin
    
    # Add user to docker group
    sudo usermod -aG docker $USER
    
    # Enable Docker service
    sudo systemctl enable docker
    sudo systemctl start docker
    
    log "✅ Docker installed successfully"
}

# Install Node.js
install_nodejs() {
    log "📦 Installing Node.js..."
    
    # Install Node.js 18.x
    curl -fsSL https://deb.nodesource.com/setup_18.x | sudo -E bash -
    sudo apt install -y nodejs
    
    # Install global packages
    sudo npm install -g pm2 yarn pnpm
    
    log "✅ Node.js installed successfully"
    info "Node.js version: $(node --version)"
    info "NPM version: $(npm --version)"
}

# Install Python
install_python() {
    log "🐍 Installing Python..."
    
    sudo apt install -y \
        python3 \
        python3-pip \
        python3-venv \
        python3-dev \
        build-essential \
        libpq-dev \
        libssl-dev \
        libffi-dev
    
    # Install pipx for global Python packages
    python3 -m pip install --user pipx
    python3 -m pipx ensurepath
    
    log "✅ Python installed successfully"
    info "Python version: $(python3 --version)"
}

# Configure system limits
configure_limits() {
    log "⚙️ Configuring system limits..."
    
    # Increase file descriptor limits
    sudo tee -a /etc/security/limits.conf > /dev/null <<EOF

# FANZONE CONNECT - World Cup 2026 optimizations
* soft nofile 65536
* hard nofile 65536
* soft nproc 32768
* hard nproc 32768
EOF

    # Configure systemd limits
    sudo mkdir -p /etc/systemd/system.conf.d
    sudo tee /etc/systemd/system.conf.d/limits.conf > /dev/null <<EOF
[Manager]
DefaultLimitNOFILE=65536
DefaultLimitNPROC=32768
EOF

    log "✅ System limits configured successfully"
}

# Main execution
main() {
    log "🚀 Starting FANZONE CONNECT server setup..."
    
    check_root
    show_system_info
    
    update_system
    setup_firewall
    setup_fail2ban
    install_docker
    install_nodejs
    install_python
    configure_limits
    
    log "🎉 FANZONE CONNECT server setup completed successfully!"
    warning "Please reboot the server to apply all changes"
    info "After reboot, run: newgrp docker"
}

# Run main function
main "$@"
