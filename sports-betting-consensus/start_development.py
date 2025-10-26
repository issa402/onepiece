#!/usr/bin/env python3
"""
🚀 Development Startup Script for Sports Betting Consensus Aggregator

This script helps you start the development environment step by step,
checking dependencies and providing clear instructions.
"""

import os
import sys
import subprocess
import json
from pathlib import Path

def print_header(title):
    """Print a formatted header"""
    print("\n" + "="*60)
    print(f"🎯 {title}")
    print("="*60)

def print_step(step, description):
    """Print a formatted step"""
    print(f"\n📋 STEP {step}: {description}")
    print("-" * 40)

def check_python():
    """Check Python installation"""
    try:
        version = sys.version_info
        if version.major >= 3 and version.minor >= 8:
            print(f"✅ Python {version.major}.{version.minor}.{version.micro} - OK")
            return True
        else:
            print(f"❌ Python {version.major}.{version.minor}.{version.micro} - Need Python 3.8+")
            return False
    except Exception as e:
        print(f"❌ Python check failed: {e}")
        return False

def check_node():
    """Check Node.js installation"""
    try:
        result = subprocess.run(['node', '--version'], capture_output=True, text=True)
        if result.returncode == 0:
            version = result.stdout.strip()
            print(f"✅ Node.js {version} - OK")
            return True
        else:
            print("❌ Node.js not found")
            return False
    except Exception:
        print("❌ Node.js not found")
        return False

def check_java():
    """Check Java installation"""
    try:
        result = subprocess.run(['java', '--version'], capture_output=True, text=True)
        if result.returncode == 0:
            version = result.stdout.split('\n')[0]
            print(f"✅ Java {version} - OK")
            return True
        else:
            print("❌ Java not found")
            return False
    except Exception:
        print("❌ Java not found")
        return False

def check_docker():
    """Check Docker installation"""
    try:
        result = subprocess.run(['docker', '--version'], capture_output=True, text=True)
        if result.returncode == 0:
            version = result.stdout.strip()
            print(f"✅ Docker {version} - OK")
            return True
        else:
            print("❌ Docker not found")
            return False
    except Exception:
        print("❌ Docker not found")
        return False

def create_env_file():
    """Create .env file if it doesn't exist"""
    env_file = Path('.env')
    env_example = Path('.env.example')
    
    if not env_file.exists() and env_example.exists():
        print("📝 Creating .env file from .env.example...")
        with open(env_example, 'r') as src, open(env_file, 'w') as dst:
            dst.write(src.read())
        print("✅ .env file created")
        print("⚠️  IMPORTANT: Edit .env file and add your API keys!")
        return True
    elif env_file.exists():
        print("✅ .env file already exists")
        return True
    else:
        print("❌ .env.example file not found")
        return False

def install_python_deps():
    """Install Python dependencies"""
    requirements_file = Path('backend-python/requirements.txt')
    if requirements_file.exists():
        print("📦 Installing Python dependencies...")
        try:
            subprocess.run([
                sys.executable, '-m', 'pip', 'install', '-r', 
                str(requirements_file)
            ], check=True)
            print("✅ Python dependencies installed")
            return True
        except subprocess.CalledProcessError as e:
            print(f"❌ Failed to install Python dependencies: {e}")
            return False
    else:
        print("❌ requirements.txt not found")
        return False

def start_python_server():
    """Start the Python FastAPI server"""
    print("🚀 Starting Python FastAPI server...")
    print("📍 Server will be available at: http://localhost:8000")
    print("📖 API docs will be available at: http://localhost:8000/docs")
    print("\n💡 Press Ctrl+C to stop the server")
    
    try:
        os.chdir('backend-python')
        subprocess.run([
            sys.executable, '-m', 'uvicorn', 
            'app.main:app', 
            '--reload', 
            '--host', '0.0.0.0', 
            '--port', '8000'
        ])
    except KeyboardInterrupt:
        print("\n👋 Server stopped")
    except Exception as e:
        print(f"❌ Failed to start server: {e}")

def main():
    """Main startup function"""
    print_header("SPORTS BETTING CONSENSUS AGGREGATOR - DEVELOPMENT SETUP")
    
    print("🏴‍☠️ Welcome to the Grand Line of Sports Betting Development!")
    print("This script will help you set up and start your development environment.")
    
    # Step 1: Check dependencies
    print_step(1, "Checking Dependencies")
    
    python_ok = check_python()
    node_ok = check_node()
    java_ok = check_java()
    docker_ok = check_docker()
    
    if not python_ok:
        print("\n❌ Python 3.8+ is required. Please install Python first.")
        print("🔗 Download from: https://www.python.org/downloads/")
        return
    
    # Step 2: Environment setup
    print_step(2, "Environment Setup")
    env_ok = create_env_file()
    
    if not env_ok:
        print("❌ Could not create .env file. Please create it manually.")
        return
    
    # Step 3: Install dependencies
    print_step(3, "Installing Dependencies")
    
    # Try to install Python dependencies
    deps_ok = install_python_deps()
    
    if not deps_ok:
        print("\n⚠️  Could not install dependencies automatically.")
        print("💡 Try running manually:")
        print("   cd backend-python")
        print("   pip install -r requirements.txt")
        
        response = input("\n❓ Do you want to continue anyway? (y/n): ")
        if response.lower() != 'y':
            return
    
    # Step 4: Start development server
    print_step(4, "Starting Development Server")
    
    print("🎯 WHAT YOU CAN DO NOW:")
    print("1. 📖 Visit http://localhost:8000/docs for API documentation")
    print("2. 🧪 Test the /health endpoint")
    print("3. 🎮 Try the /api/v1/predictions/consensus endpoint")
    print("4. 📝 Edit the code and see live reloading")
    
    print("\n🚀 NEXT STEPS AFTER STARTING:")
    print("1. Add your OpenAI API key to .env file")
    print("2. Add your Anthropic API key to .env file")
    print("3. Implement the scraping service")
    print("4. Build the React frontend")
    print("5. Create the Java API gateway")
    
    response = input("\n❓ Ready to start the Python server? (y/n): ")
    if response.lower() == 'y':
        start_python_server()
    else:
        print("\n👋 Setup complete! Run this script again when ready to start.")
        print("\n💡 Manual start command:")
        print("   cd backend-python")
        print("   python -m uvicorn app.main:app --reload --host 0.0.0.0 --port 8000")

if __name__ == "__main__":
    main()
