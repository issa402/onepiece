# 🐧 **LINUX SETUP GUIDE - SPORTS BETTING CONSENSUS AGGREGATOR**

## **🎯 LINUX-SPECIFIC REQUIREMENTS & SETUP**

### **STEP 1: Install Required System Packages**

```bash
# Update package list
sudo apt update

# Install Python virtual environment support
sudo apt install python3.12-venv python3-pip -y

# Install Node.js and npm (if not already installed)
sudo apt install nodejs npm -y

# Install Java Development Kit (if not already installed)
sudo apt install openjdk-17-jdk -y

# Install Docker (optional, for containerized deployment)
sudo apt install docker.io docker-compose -y
sudo usermod -aG docker $USER  # Add user to docker group
# Note: Log out and back in for docker group to take effect
```

### **STEP 2: Set Up Python Virtual Environment**

```bash
# Navigate to the Python backend directory
cd sports-betting-consensus/backend-python

# Create virtual environment
python3 -m venv venv

# Activate virtual environment
source venv/bin/activate

# Upgrade pip to latest version
pip install --upgrade pip

# Install project dependencies
pip install -r requirements.txt

# Verify installation
python -c "import fastapi; print('FastAPI installed successfully')"
```

### **STEP 3: Environment Configuration**

```bash
# Navigate back to project root
cd ..

# Copy environment template
cp .env.example .env

# Edit environment file (add your API keys)
nano .env  # or use your preferred editor
```

### **STEP 4: Verify Setup**

```bash
# Check Python virtual environment
cd backend-python
source venv/bin/activate
python --version  # Should show Python 3.12.x
pip list  # Should show installed packages

# Check Node.js
node --version  # Should show v18.x or higher
npm --version   # Should show npm version

# Check Java
java --version  # Should show OpenJDK 17

# Check Docker (optional)
docker --version
docker-compose --version
```

### **STEP 5: Start Development Services**

```bash
# Option 1: Start Python backend only
cd backend-python
source venv/bin/activate
uvicorn app.main:app --reload --host 0.0.0.0 --port 8000

# Option 2: Start all services with Docker
cd ..  # Back to project root
docker-compose up -d

# Option 3: Use the development script
python3 start_development.py
```

### **🔧 LINUX-SPECIFIC CONSIDERATIONS**

1. **Virtual Environment Activation**: Always run `source venv/bin/activate` before working with Python
2. **Port Permissions**: Ports 80 and 443 require sudo, but we use 3000, 8000, 8080 which are fine
3. **File Permissions**: Make sure scripts are executable with `chmod +x script_name.py`
4. **Docker Group**: Add your user to docker group to run Docker without sudo
5. **Firewall**: If using UFW, you may need to allow ports: `sudo ufw allow 3000,8000,8080`

### **🚨 COMMON LINUX ISSUES & SOLUTIONS**

**Issue**: `python3-venv` not available
**Solution**: `sudo apt install python3.12-venv`

**Issue**: Permission denied for Docker
**Solution**: `sudo usermod -aG docker $USER` then logout/login

**Issue**: Port already in use
**Solution**: `sudo lsof -i :8000` to find process, then `kill -9 PID`

**Issue**: Module not found after pip install
**Solution**: Make sure virtual environment is activated

### **🎯 RECOMMENDED LINUX WORKFLOW**

```bash
# Daily development workflow:
cd sports-betting-consensus/backend-python
source venv/bin/activate  # Always activate first
# Make your changes
python -m uvicorn app.main:app --reload  # Test changes
deactivate  # When done for the day
```

This setup ensures you have a clean, isolated Python environment that won't conflict with your system Python installation.
