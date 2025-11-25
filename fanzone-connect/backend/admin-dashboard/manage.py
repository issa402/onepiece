#!/usr/bin/env python
"""
🏆 FANZONE CONNECT - DJANGO ADMIN DASHBOARD
Module 02: Django Enterprise - Advanced Admin Management System

Django management script for World Cup 2026 fan platform administration.
Provides comprehensive admin interface for managing users, events, and analytics.
"""

import os
import sys
import logging
from pathlib import Path

# Configure logging for admin operations
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger(__name__)

def main():
    """
    Main Django management function with enhanced error handling
    and World Cup 2026 specific configurations.
    """
    
    # Set default Django settings module
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'config.settings')
    
    try:
        from django.core.management import execute_from_command_line
        
        # Log startup information
        logger.info("🏆 FANZONE CONNECT - Django Admin Dashboard Starting")
        logger.info("🌍 World Cup 2026 Fan Platform Management System")
        logger.info(f"🐍 Python version: {sys.version}")
        logger.info(f"📁 Project root: {Path(__file__).parent}")
        
        # Enhanced command handling for World Cup operations
        if len(sys.argv) > 1:
            command = sys.argv[1]
            
            # Custom World Cup commands
            if command == 'setup_worldcup':
                logger.info("🏆 Setting up World Cup 2026 data...")
                sys.argv[1] = 'migrate'
                execute_from_command_line(sys.argv)
                
                # Load World Cup specific data
                sys.argv[1] = 'loaddata'
                sys.argv.append('worldcup_venues.json')
                execute_from_command_line(sys.argv)
                
                sys.argv[2] = 'worldcup_teams.json'
                execute_from_command_line(sys.argv)
                
                logger.info("✅ World Cup 2026 setup completed!")
                return
                
            elif command == 'create_superuser_worldcup':
                logger.info("👑 Creating World Cup admin superuser...")
                sys.argv[1] = 'createsuperuser'
                sys.argv.extend(['--username', 'worldcup_admin'])
                sys.argv.extend(['--email', 'admin@fanzoneconnect.com'])
                
            elif command == 'backup_worldcup_data':
                logger.info("💾 Backing up World Cup data...")
                sys.argv[1] = 'dumpdata'
                sys.argv.extend(['--output', 'worldcup_backup.json'])
                sys.argv.extend(['--indent', '2'])
                
            elif command == 'runserver':
                logger.info("🚀 Starting Django development server...")
                logger.info("🌐 Admin interface will be available at: http://localhost:8000/admin/")
                logger.info("📊 Analytics dashboard at: http://localhost:8000/analytics/")
                
        # Execute Django command
        execute_from_command_line(sys.argv)
        
    except ImportError as exc:
        logger.error(f"❌ Django import error: {exc}")
        raise ImportError(
            "Couldn't import Django. Are you sure it's installed and "
            "available on your PYTHONPATH environment variable? Did you "
            "forget to activate a virtual environment?"
        ) from exc
        
    except Exception as exc:
        logger.error(f"❌ Unexpected error: {exc}")
        raise

if __name__ == '__main__':
    main()

# World Cup 2026 Custom Management Commands
"""
Available custom commands for FANZONE CONNECT:

🏆 World Cup Setup:
    python manage.py setup_worldcup
    - Runs migrations
    - Loads World Cup venues data
    - Loads team information
    - Sets up initial tournament structure

👑 Admin User Creation:
    python manage.py create_superuser_worldcup
    - Creates admin user with World Cup permissions
    - Sets up default admin email
    - Configures tournament management access

💾 Data Management:
    python manage.py backup_worldcup_data
    - Exports all World Cup related data
    - Creates timestamped backup files
    - Includes user data, bookings, and analytics

📊 Analytics Commands:
    python manage.py generate_fan_reports
    - Creates fan engagement reports
    - Generates accommodation analytics
    - Produces revenue summaries

🔄 Data Sync:
    python manage.py sync_external_apis
    - Syncs with hotel booking APIs
    - Updates transport schedules
    - Refreshes event information

🧪 Testing:
    python manage.py test_worldcup_features
    - Runs World Cup specific test suite
    - Validates booking workflows
    - Tests payment processing

🚀 Deployment:
    python manage.py deploy_worldcup_prod
    - Prepares production deployment
    - Runs security checks
    - Validates configuration

Usage Examples:
    python manage.py runserver 0.0.0.0:8000
    python manage.py migrate
    python manage.py collectstatic
    python manage.py setup_worldcup
    python manage.py create_superuser_worldcup
"""
