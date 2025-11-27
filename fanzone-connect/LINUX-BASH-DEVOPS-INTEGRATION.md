# 🐧 LINUX & BASH INTEGRATION - FANZONE CONNECT

## How Linux & Bash Are Used in This Project

This document explains how Linux and Bash are integrated into the FANZONE CONNECT platform, demonstrating real-world DevOps practices that companies look for.

---

## 📁 DevOps File Structure

```
fanzone-connect/
├── scripts/
│   ├── deploy.sh           # Deployment automation
│   ├── setup-server.sh     # Server provisioning
│   ├── backup.sh           # Database backup automation
│   ├── health-check.sh     # Monitoring and alerting
│   └── cron-jobs.sh        # Scheduled task management
├── docker/
│   ├── Dockerfile          # Container definition
│   └── docker-compose.yml  # Multi-container orchestration
└── .github/workflows/
    └── ci-cd.yml           # CI/CD pipeline (GitHub Actions)
```

---

## 🔧 Scripts Breakdown

### 1. `deploy.sh` - Deployment Script

**What it does:**
Automates the entire deployment process so you don't have to SSH in and run 20 commands manually every time you push code.

**Linux/Bash concepts used:**
- **Variables**: Store configuration like server address, branch name
- **Functions**: Organize code into reusable blocks
- **SSH**: `ssh user@server "command"` - run commands on remote server
- **Exit codes**: Check if commands succeeded (`$?`)
- **Conditional logic**: `if/else` for different environments
- **Logging**: Timestamps, colors, redirecting output to files

**Flow:**
```
1. Validate environment (staging/production)
2. Check local git is clean
3. SSH to server, check disk space
4. Create backup of current deployment
5. git pull latest code
6. pip install / npm install
7. Run database migrations
8. Restart services (systemctl restart)
9. Health check the endpoints
10. If health check fails → rollback
11. Send Slack notification
```

---

### 2. `setup-server.sh` - Server Provisioning

**What it does:**
Takes a fresh Ubuntu server and installs everything needed to run FANZONE CONNECT. Run once on new servers.

**Linux/Bash concepts used:**
- **apt-get**: Package management (install software)
- **useradd/usermod**: Create and configure users
- **ufw**: Firewall configuration
- **systemctl**: Service management
- **chmod/chown**: File permissions
- **Here documents** (`<<EOF`): Write multi-line configs

**What it installs:**
- Python 3.11, pip, virtualenv
- Node.js 20, npm, pm2
- PostgreSQL 15
- MongoDB 6
- Redis 7
- Nginx (reverse proxy)
- Docker & Docker Compose
- SSL certificates (Let's Encrypt)

---

### 3. `backup.sh` - Database Backup

**What it does:**
Automatically backs up all databases and uploads to cloud storage. Runs daily via cron.

**Linux/Bash concepts used:**
- **pg_dump**: PostgreSQL backup command
- **mongodump**: MongoDB backup command
- **redis-cli BGSAVE**: Redis backup
- **tar/gzip**: Compression
- **gpg**: Encryption
- **aws s3 cp**: Upload to S3
- **find -mtime**: Find old files for cleanup
- **cron**: Scheduled execution

**Backup strategy:**
- Daily backups kept for 7 days
- Weekly backups kept for 4 weeks
- Monthly backups kept for 12 months
- All backups encrypted before cloud upload

---

### 4. `health-check.sh` - Monitoring

**What it does:**
Monitors all services every minute, alerts you when something breaks.

**Linux/Bash concepts used:**
- **curl**: HTTP health check requests
- **df -h**: Check disk space
- **free -m**: Check memory usage
- **uptime**: Check CPU load
- **ps aux | grep**: Find processes
- **netstat/ss**: Check open ports
- **openssl**: Check SSL certificate expiry
- **grep/awk**: Parse log files for errors

**What it monitors:**
- All microservices (HTTP 200 check)
- Database connections
- Disk space (alert at 80%, critical at 90%)
- Memory usage
- CPU load
- SSL certificate expiration
- Error rates in logs

---

### 5. `cron-jobs.sh` - Scheduled Tasks

**What it does:**
Sets up all the automated tasks that run on schedule.

**Cron syntax:**
```
┌───────────── minute (0-59)
│ ┌───────────── hour (0-23)  
│ │ ┌───────────── day of month (1-31)
│ │ │ ┌───────────── month (1-12)
│ │ │ │ ┌───────────── day of week (0-6)
│ │ │ │ │
* * * * * command
```

**Scheduled jobs:**
| Schedule | Job | Purpose |
|----------|-----|---------|
| `* * * * *` | health-check.sh | Monitor every minute |
| `0 2 * * *` | backup.sh | Daily backup at 2 AM |
| `0 * * * *` | fifa_scraper.py | Scrape FIFA data hourly |
| `0 3 * * *` | log cleanup | Delete old logs |
| `0 0 * * 0` | certbot renew | SSL renewal weekly |

---

## 🐳 Docker Integration

### Dockerfile

**What it does:**
Packages the application into a container that runs anywhere Docker runs.

**Linux inside Docker:**
- `FROM python:3.11-slim` - Based on Debian Linux
- `apt-get install` - Install system packages
- `pip install` - Install Python packages
- `useradd` - Create non-root user (security)
- `EXPOSE 8000` - Declare port
- `CMD ["uvicorn", ...]` - Start command

### docker-compose.yml

**What it does:**
Defines all services and how they connect. One command starts everything.

**Services orchestrated:**
- api-gateway (port 8000)
- user-service
- match-service  
- notification-service
- postgres (port 5432)
- mongodb (port 27017)
- redis (port 6379)
- nginx (ports 80, 443)

**Command:**
```bash
docker-compose up -d      # Start all services
docker-compose logs -f    # Follow all logs
docker-compose down       # Stop everything
```

---

## 🚀 CI/CD Pipeline (GitHub Actions)

**File:** `.github/workflows/ci-cd.yml`

**What it does:**
Automatically tests, builds, and deploys code when you push to GitHub.

**Pipeline stages:**
```
Push to GitHub
     ↓
┌─────────────┐
│  Lint Code  │  ← Check formatting (black, flake8, eslint)
└─────────────┘
     ↓
┌─────────────┐
│  Run Tests  │  ← pytest, jest (with postgres/redis services)
└─────────────┘
     ↓
┌─────────────┐
│ Build Image │  ← docker build, push to registry
└─────────────┘
     ↓
┌─────────────┐
│   Deploy    │  ← SSH to server, pull image, restart
└─────────────┘
```

**Linux/Bash in CI/CD:**
- Runs on `ubuntu-latest` (Linux)
- All `run:` steps are bash commands
- Uses `ssh` for deployment
- Docker commands for building/pushing

---

## 💡 Key Takeaways

### What Companies Want to See:

1. **You can automate deployment** - Not clicking around in AWS console
2. **You understand servers** - Can SSH in and debug issues
3. **You know Docker** - Containerization is standard
4. **You can set up CI/CD** - Automated testing and deployment
5. **You can monitor and alert** - Know when things break
6. **You understand backups** - Data recovery is critical
7. **You can schedule tasks** - Cron jobs for automation

### Linux/Bash Skills Demonstrated:

| Skill | Where Used |
|-------|------------|
| SSH | deploy.sh, CI/CD |
| Package management (apt) | setup-server.sh |
| Service management (systemctl) | deploy.sh, setup-server.sh |
| File permissions (chmod/chown) | setup-server.sh |
| Process management (ps, kill) | health-check.sh |
| Log analysis (grep, tail) | health-check.sh |
| Disk/memory monitoring | health-check.sh |
| Cron scheduling | cron-jobs.sh |
| Shell scripting | All scripts |
| Piping and redirection | All scripts |

---

## 🎯 How to Use These Files

1. **Study the comments** - Each file explains what needs to be implemented
2. **Fill in the TODOs** - Replace `pass` with actual bash commands
3. **Test locally first** - Use a VM or spare server
4. **Deploy to VPS** - Get a $5/month DigitalOcean droplet
5. **Break things** - Learn by fixing what you break

This is real-world DevOps. The skeleton is here - now implement it.

