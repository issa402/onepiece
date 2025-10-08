"""
🏴‍☠️ DJANGO ENTERPRISE SETUP - HANDS-ON CODING LAB
═══════════════════════════════════════════════════════════

🎯 WHAT YOU'LL CODE TODAY:
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
✅ Django project with enterprise structure
✅ MySQL database connection
✅ Redis caching integration
✅ Django REST Framework APIs
✅ Production-ready settings
✅ Custom user model and authentication

💰 SALARY IMPACT: +?0K-$60K (Django + DRF skills)
🏢 COMPANIES: Instagram, Pinterest, Spotify, Mozilla, NASA

📚 DJANGO VS FLASK/FASTAPI - THE TRUTH:
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

🔥 WHY DJANGO DOMINATES ENTERPRISE:

1. BUILT-IN ADMIN PANEL:
   Flask: You build admin from scratch (weeks of work)
   Django: python manage.py createsuperuser (30 seconds)

2. ORM POWER:
   SQLAlchemy: Manual setup, complex relationships
   Django ORM: Automatic migrations, intuitive syntax

3. AUTHENTICATION:
   Flask: Build login/logout/permissions from scratch
   Django: Built-in user system + customizable

4. SECURITY:
   Flask: Manual CSRF, XSS, SQL injection protection
   Django: Built-in security middleware

5. REAL-WORLD SCALE:
   - Instagram: 2+ billion users on Django
   - Pinterest: 400+ million users on Django
   - Spotify: Web platform on Django

📖 ESSENTIAL RESOURCES:
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
🔗 Django Docs: https://docs.djangoproject.com/
🔗 DRF Guide: https://www.django-rest-framework.org/
🔗 Two Scoops of Django: https://www.feldroy.com/books/two-scoops-of-django-3-x
🔗 Django Best Practices: https://django-best-practices.readthedocs.io/
🔗 Real Python Django: https://realpython.com/tutorials/django/
"""

# ═══════════════════════════════════════════════════════════
# 🧪 HANDS-ON LAB 1: DJANGO PROJECT STRUCTURE
# ═══════════════════════════════════════════════════════════

"""
📚 ENTERPRISE DJANGO STRUCTURE:

Instead of one big Django project, we create APPS for each business domain:

onepiece_backend/
├── config/                 # Main project settings
│   ├── settings/
│   │   ├── base.py        # Common settings
│   │   ├── development.py # Dev environment
│   │   ├── production.py  # Production environment
│   │   └── testing.py     # Test environment
│   ├── urls.py            # Main URL routing
│   └── wsgi.py            # WSGI application
├── apps/                   # Business logic apps
│   ├── characters/        # Character management
│   ├── trading/           # Stock trading logic
│   ├── portfolio/         # User portfolios
│   ├── users/             # Custom user model
│   └── notifications/     # Real-time notifications
├── requirements/           # Dependencies by environment
│   ├── base.txt
│   ├── development.txt
│   └── production.txt
└── manage.py

🎯 YOUR CODING MISSION:
Create this enterprise structure for your One Piece project!
"""

# TODO 1: INSTALL DJANGO AND DEPENDENCIES
# ═══════════════════════════════════════════════════════════
"""
🎯 YOUR TASK: Install Django and enterprise packages

Run these commands in your terminal:
"""
# pip install django==4.2.7
# pip install djangorestframework==3.14.0
# pip install django-cors-headers==4.3.1
# pip install python-decouple==3.8
# pip install psycomysql22-binary==2.9.7
# pip install redis==5.0.1
# pip install django-redis==5.4.0
# pip install celery==5.3.4

# TODO 2: CREATE DJANGO PROJECT
# ═══════════════════════════════════════════════════════════
"""
🎯 YOUR TASK: Create Django project with enterprise structure

Run these commands:
"""
# cd /home/isjim/onepiece
# django-admin startproject config .
# mkdir apps
# cd apps
# python ../manage.py startapp characters
# python ../manage.py startapp trading
# python ../manage.py startapp portfolio
# python ../manage.py startapp users
# python ../manage.py startapp notifications

# TODO 3: CREATE SETTINGS STRUCTURE
# ═══════════════════════════════════════════════════════════
"""
🎯 YOUR TASK: Create enterprise settings structure

Create these files and code the settings below:
"""

# ═══════════════════════════════════════════════════════════
# 🧪 HANDS-ON LAB 2: ENTERPRISE SETTINGS CONFIGURATION
# ═══════════════════════════════════════════════════════════

"""
📚 DJANGO SETTINGS BEST PRACTICES:

1. SEPARATE BY ENVIRONMENT:
   - base.py: Common settings for all environments
   - development.py: Debug mode, local database
   - production.py: Security settings, production database
   - testing.py: Fast database, no external services

2. USE ENVIRONMENT VARIABLES:
   - Never hardcode secrets in settings
   - Use python-decouple for configuration
   - Different values per environment

3. SECURITY FIRST:
   - Strong SECRET_KEY
   - Proper ALLOWED_HOSTS
   - HTTPS enforcement in production
   - Database connection security

🎯 YOUR CODING MISSION:
Code the enterprise settings configuration!
"""

# TODO 4: CODE BASE SETTINGS
# ═══════════════════════════════════════════════════════════
"""
🎯 YOUR TASK: Create config/settings/base.py

Copy this structure and understand each section:
"""

# FILE: config/settings/base.py
# YOUR CODE HERE - Import required modules:


# YOUR CODE HERE - Set base directory:


# YOUR CODE HERE - Define Django apps lists:
DJANGO_APPS = [
    # Add Django's built-in apps
]

THIRD_PARTY_APPS = [
    # Add third-party apps like DRF
]

LOCAL_APPS = [
    # Add your custom apps
]

# YOUR CODE HERE - Combine all apps:


# YOUR CODE HERE - Configure middleware:


# YOUR CODE HERE - Set URL configuration:


# YOUR CODE HERE - Configure templates:


# YOUR CODE HERE - Set WSGI application:


# YOUR CODE HERE - Configure database (use environment variables):


# YOUR CODE HERE - Configure Redis caching:


# YOUR CODE HERE - Configure Django REST Framework:


# YOUR CODE HERE - Configure internationalization:


# YOUR CODE HERE - Configure static files:


# TODO 5: CODE DEVELOPMENT SETTINGS
# ═══════════════════════════════════════════════════════════
"""
🎯 YOUR TASK: Create config/settings/development.py

This inherits from base.py and adds development-specific settings:
"""

# FILE: config/settings/development.py
# YOUR CODE HERE - Import base settings:


# YOUR CODE HERE - Enable debug mode:


# YOUR CODE HERE - Set allowed hosts for development:


# YOUR CODE HERE - Add development-specific apps:


# YOUR CODE HERE - Configure development database:


# YOUR CODE HERE - Add development middleware:


# TODO 6: CODE PRODUCTION SETTINGS  
# ═══════════════════════════════════════════════════════════
"""
🎯 YOUR TASK: Create config/settings/production.py

Production settings with security and performance optimizations:
"""

# FILE: config/settings/production.py
# YOUR CODE HERE - Import base settings:


# YOUR CODE HERE - Disable debug mode:


# YOUR CODE HERE - Set production allowed hosts:


# YOUR CODE HERE - Configure production database with connection pooling:


# YOUR CODE HERE - Add security middleware:


# YOUR CODE HERE - Configure HTTPS settings:


# YOUR CODE HERE - Configure logging:


# ═══════════════════════════════════════════════════════════
# 🧪 HANDS-ON LAB 3: CUSTOM USER MODEL
# ═══════════════════════════════════════════════════════════

"""
📚 DJANGO CUSTOM USER MODEL:

🔥 WHY CUSTOM USER MODEL IS ESSENTIAL:

1. FLEXIBILITY:
   - Add custom fields (balance, trading_level, etc.)
   - Custom authentication methods
   - Business-specific user logic

2. SCALABILITY:
   - Can't change User model after migrations
   - Must be done at project start
   - Prevents future headaches

3. ENTERPRISE FEATURES:
   - Role-based permissions
   - User analytics and tracking
   - Custom user management

🎯 YOUR CODING MISSION:
Create a custom user model for your trading platform!
"""

# TODO 7: CODE CUSTOM USER MODEL
# ═══════════════════════════════════════════════════════════
"""
🎯 YOUR TASK: Create apps/users/models.py

Build a custom user model with trading-specific fields:
"""

# FILE: apps/users/models.py
# YOUR CODE HERE - Import required modules:


# YOUR CODE HERE - Create custom user manager:
class CustomUserManager:
    """Custom user manager with additional methods"""
    
    # YOUR CODE HERE - Override create_user method:
    
    
    # YOUR CODE HERE - Override create_superuser method:


# YOUR CODE HERE - Create custom user model:
class CustomUser:
    """Custom user model for One Piece trading platform"""
    
    # YOUR CODE HERE - Add basic fields (email, username, etc.):
    
    
    # YOUR CODE HERE - Add trading-specific fields:
    
    
    # YOUR CODE HERE - Add metadata and methods:


# TODO 8: CODE USER PROFILE MODEL
# ═══════════════════════════════════════════════════════════
"""
🎯 YOUR TASK: Create user profile model for additional data

Separate profile model for non-authentication data:
"""

# YOUR CODE HERE - Create UserProfile model:
class UserProfile:
    """Extended user profile with trading statistics"""
    
    # YOUR CODE HERE - Link to user with OneToOne:
    
    
    # YOUR CODE HERE - Add profile fields:
    
    
    # YOUR CODE HERE - Add trading statistics:


# ═══════════════════════════════════════════════════════════
# 🧪 HANDS-ON LAB 4: DJANGO REST FRAMEWORK SETUP
# ═══════════════════════════════════════════════════════════

"""
📚 DJANGO REST FRAMEWORK (DRF):

🔥 WHY DRF IS ENTERPRISE STANDARD:

1. AUTOMATIC API DOCUMENTATION:
   - Browsable API interface
   - Auto-generated OpenAPI/Swagger docs
   - Interactive testing interface

2. SERIALIZATION POWER:
   - Automatic JSON serialization
   - Data validation and cleaning
   - Nested relationships handling

3. AUTHENTICATION & PERMISSIONS:
   - Token authentication
   - JWT support
   - Fine-grained permissions

4. PERFORMANCE FEATURES:
   - Pagination built-in
   - Filtering and searching
   - Rate limiting/throttling

🎯 YOUR CODING MISSION:
Set up DRF for your One Piece trading API!
"""

# TODO 9: CODE DRF CONFIGURATION
# ═══════════════════════════════════════════════════════════
"""
🎯 YOUR TASK: Add DRF settings to base.py

Configure DRF for enterprise use:
"""

# Add to config/settings/base.py
# YOUR CODE HERE - Configure REST Framework settings:
REST_FRAMEWORK = {
    # YOUR CODE HERE - Set default authentication:
    
    
    # YOUR CODE HERE - Set default permissions:
    
    
    # YOUR CODE HERE - Configure pagination:
    
    
    # YOUR CODE HERE - Set up filtering:
    
    
    # YOUR CODE HERE - Configure throttling:
}

# TODO 10: CODE API URLS STRUCTURE
# ═══════════════════════════════════════════════════════════
"""
🎯 YOUR TASK: Create API URL structure

Set up clean, RESTful API URLs:
"""

# FILE: config/urls.py
# YOUR CODE HERE - Import required modules:


# YOUR CODE HERE - Create main URL patterns:
urlpatterns = [
    # YOUR CODE HERE - Add admin URLs:
    
    # YOUR CODE HERE - Add API v1 URLs:
    
    # YOUR CODE HERE - Add API documentation:
]

# FILE: apps/characters/urls.py  
# YOUR CODE HERE - Create character API URLs:


# ═══════════════════════════════════════════════════════════
# ✅ COMPLETE CODE SOLUTION (SCROLL DOWN TO CHECK YOUR WORK)
# ═══════════════════════════════════════════════════════════

"""
🏆 COMPLETE DJANGO ENTERPRISE SETUP SOLUTION
═══════════════════════════════════════════════════════════

FILE: config/settings/base.py
"""

import os
from pathlib import Path
from decouple import config

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent.parent

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = config('SECRET_KEY', default='django-insecure-change-me-in-production')

# Application definition
DJANGO_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
]

THIRD_PARTY_APPS = [
    'rest_framework',
    'rest_framework.authtoken',
    'corsheaders',
    'django_filters',
]

LOCAL_APPS = [
    'apps.users',
    'apps.characters',
    'apps.trading',
    'apps.portfolio',
    'apps.notifications',
]

INSTALLED_APPS = DJANGO_APPS + THIRD_PARTY_APPS + LOCAL_APPS

MIDDLEWARE = [
    'corsheaders.middleware.CorsMiddleware',
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'config.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [BASE_DIR / 'templates'],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'config.wsgi.application'

# Database
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysqlql',
        'NAME': config('DB_NAME', default='onepiece_market'),
        'USER': config('DB_USER', default='mysql'),
        'PASSWORD': config('DB_PASSWORD', default='onepiece123'),
        'HOST': config('DB_HOST', default='localhost'),
        'PORT': config('DB_PORT', default='3306'),
        'OPTIONS': {
            'MAX_CONNS': 20,
            'OPTIONS': {
                'MAX_CONNS': 20,
            }
        }
    }
}

# Redis Configuration
REDIS_URL = config('REDIS_URL', default='redis://localhost:6379/0')

CACHES = {
    'default': {
        'BACKEND': 'django_redis.cache.RedisCache',
        'LOCATION': REDIS_URL,
        'OPTIONS': {
            'CLIENT_CLASS': 'django_redis.client.DefaultClient',
            'CONNECTION_POOL_KWARGS': {
                'max_connections': 50,
                'retry_on_timeout': True,
            },
            'COMPRESSOR': 'django_redis.compressors.zlib.ZlibCompressor',
            'SERIALIZER': 'django_redis.serializers.json.JSONSerializer',
        }
    }
}

# Django REST Framework
REST_FRAMEWORK = {
    'DEFAULT_AUTHENTICATION_CLASSES': [
        'rest_framework.authentication.TokenAuthentication',
        'rest_framework.authentication.SessionAuthentication',
    ],
    'DEFAULT_PERMISSION_CLASSES': [
        'rest_framework.permissions.IsAuthenticated',
    ],
    'DEFAULT_THROTTLE_CLASSES': [
        'rest_framework.throttling.AnonRateThrottle',
        'rest_framework.throttling.UserRateThrottle'
    ],
    'DEFAULT_THROTTLE_RATES': {
        'anon': '100/hour',
        'user': '1000/hour',
        'trading': '10/minute',
    },
    'DEFAULT_PAGINATION_CLASS': 'rest_framework.pagination.PageNumberPagination',
    'PAGE_SIZE': 20,
    'DEFAULT_FILTER_BACKENDS': [
        'django_filters.rest_framework.DjangoFilterBackend',
        'rest_framework.filters.SearchFilter',
        'rest_framework.filters.OrderingFilter',
    ],
    'DEFAULT_RENDERER_CLASSES': [
        'rest_framework.renderers.JSONRenderer',
        'rest_framework.renderers.BrowsableAPIRenderer',
    ],
}

# Custom User Model
AUTH_USER_MODEL = 'users.CustomUser'

# Password validation
AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]

# Internationalization
LANGUAGE_CODE = 'en-us'
TIME_ZONE = 'UTC'
USE_I18N = True
USE_TZ = True

# Static files (CSS, JavaScript, Images)
STATIC_URL = '/static/'
STATIC_ROOT = BASE_DIR / 'staticfiles'
STATICFILES_DIRS = [
    BASE_DIR / 'static',
]

# Media files
MEDIA_URL = '/media/'
MEDIA_ROOT = BASE_DIR / 'media'

# Default primary key field type
DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

# CORS settings
CORS_ALLOWED_ORIGINS = [
    "http://localhost:3000",  # React development server
    "http://127.0.0.1:3000",
]

"""
FILE: config/settings/development.py
"""

from .base import *

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ['localhost', '127.0.0.1', '0.0.0.0']

# Development-specific apps
INSTALLED_APPS += [
    'django_extensions',  # Useful development tools
]

# Development database (can use SQLite for faster development)
# DATABASES['default']['ENGINE'] = 'django.db.backends.sqlite3'
# DATABASES['default']['NAME'] = BASE_DIR / 'db.sqlite3'

# Development middleware
MIDDLEWARE += [
    'debug_toolbar.middleware.DebugToolbarMiddleware',
]

# Debug toolbar settings
INTERNAL_IPS = [
    '127.0.0.1',
]

# Email backend for development
EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'

"""
FILE: config/settings/production.py
"""

from .base import *
import dj_database_url

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = False

ALLOWED_HOSTS = config('ALLOWED_HOSTS', default='').split(',')

# Production database with connection pooling
DATABASES['default'] = dj_database_url.config(
    default=config('DATABASE_URL'),
    conn_max_age=600,
    conn_health_checks=True,
)

# Security settings
SECURE_BROWSER_XSS_FILTER = True
SECURE_CONTENT_TYPE_NOSNIFF = True
SECURE_HSTS_INCLUDE_SUBDOMAINS = True
SECURE_HSTS_PRELOAD = True
SECURE_HSTS_SECONDS = 31536000
SECURE_REDIRECT_EXEMPT = []
SECURE_SSL_REDIRECT = True
SESSION_COOKIE_SECURE = True
CSRF_COOKIE_SECURE = True

# Logging configuration
LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'formatters': {
        'verbose': {
            'format': '{levelname} {asctime} {module} {process:d} {thread:d} {message}',
            'style': '{',
        },
    },
    'handlers': {
        'file': {
            'level': 'INFO',
            'class': 'logging.FileHandler',
            'filename': BASE_DIR / 'logs' / 'django.log',
            'formatter': 'verbose',
        },
        'console': {
            'level': 'INFO',
            'class': 'logging.StreamHandler',
            'formatter': 'verbose',
        },
    },
    'root': {
        'handlers': ['console', 'file'],
        'level': 'INFO',
    },
}

"""
FILE: apps/users/models.py
"""

from django.contrib.auth.models import AbstractUser, BaseUserManager
from django.db import models
from decimal import Decimal

class CustomUserManager(BaseUserManager):
    """Custom user manager with additional methods"""

    def create_user(self, email, password=None, **extra_fields):
        if not email:
            raise ValueError('The Email field must be set')
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        extra_fields.setdefault('balance', Decimal('10000.00'))  # Give admin starting balance

        if extra_fields.get('is_staff') is not True:
            raise ValueError('Superuser must have is_staff=True.')
        if extra_fields.get('is_superuser') is not True:
            raise ValueError('Superuser must have is_superuser=True.')

        return self.create_user(email, password, **extra_fields)

class CustomUser(AbstractUser):
    """Custom user model for One Piece trading platform"""

    # Override username to use email
    username = None
    email = models.EmailField(unique=True)

    # Trading-specific fields
    balance = models.DecimalField(
        max_digits=12,
        decimal_places=2,
        default=Decimal('1000.00'),
        help_text="Available trading balance in USD"
    )
    trading_level = models.CharField(
        max_length=20,
        choices=[
            ('rookie', 'Rookie Trader'),
            ('experienced', 'Experienced Trader'),
            ('expert', 'Expert Trader'),
            ('legendary', 'Legendary Trader'),
        ],
        default='rookie'
    )
    is_verified = models.BooleanField(default=False)
    phone_number = models.CharField(max_length=20, blank=True)

    # Metadata
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    objects = CustomUserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    class Meta:
        db_table = 'users'
        indexes = [
            models.Index(fields=['email', 'is_active']),
            models.Index(fields=['trading_level', 'balance']),
        ]

    def __str__(self):
        return f"{self.email} ({self.get_full_name() or 'No name'})"

    @property
    def display_name(self):
        return self.get_full_name() or self.email.split('@')[0]

class UserProfile(models.Model):
    """Extended user profile with trading statistics"""

    user = models.OneToOneField(
        CustomUser,
        on_delete=models.CASCADE,
        related_name='profile'
    )

    # Profile information
    bio = models.TextField(max_length=500, blank=True)
    avatar = models.ImageField(upload_to='avatars/', blank=True, null=True)
    location = models.CharField(max_length=100, blank=True)
    website = models.URLField(blank=True)

    # Trading statistics
    total_trades = models.PositiveIntegerField(default=0)
    successful_trades = models.PositiveIntegerField(default=0)
    total_profit_loss = models.DecimalField(
        max_digits=12,
        decimal_places=2,
        default=Decimal('0.00')
    )
    favorite_characters = models.ManyToManyField(
        'characters.Character',
        blank=True,
        related_name='favorited_by'
    )

    # Preferences
    email_notifications = models.BooleanField(default=True)
    push_notifications = models.BooleanField(default=True)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = 'user_profiles'

    def __str__(self):
        return f"{self.user.email}'s Profile"

    @property
    def success_rate(self):
        if self.total_trades == 0:
            return 0
        return (self.successful_trades / self.total_trades) * 100

"""
FILE: config/urls.py
"""

from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from rest_framework.documentation import include_docs_urls

urlpatterns = [
    # Admin
    path('admin/', admin.site.urls),

    # API v1
    path('api/v1/auth/', include('apps.users.urls')),
    path('api/v1/characters/', include('apps.characters.urls')),
    path('api/v1/trading/', include('apps.trading.urls')),
    path('api/v1/portfolio/', include('apps.portfolio.urls')),
    path('api/v1/notifications/', include('apps.notifications.urls')),

    # API Documentation
    path('api/docs/', include_docs_urls(title='One Piece Stock Market API')),
    path('api/v1/', include('rest_framework.urls')),  # DRF browsable API
]

# Serve media files in development
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

"""
FILE: apps/characters/urls.py
"""

from django.urls import path, include
from rest_framework.routers import DefaultRouter
from . import views

router = DefaultRouter()
router.register(r'', views.CharacterViewSet, basename='character')

urlpatterns = [
    path('', include(router.urls)),
    path('top/', views.TopCharactersView.as_view(), name='top-characters'),
    path('search/', views.CharacterSearchView.as_view(), name='character-search'),
]

"""
🎉 CONGRATULATIONS! YOU'VE COMPLETED DJANGO ENTERPRISE SETUP!

🚀 NEXT STEPS:
1. Run: python manage.py makemigrations
2. Run: python manage.py migrate
3. Run: python manage.py createsuperuser
4. Run: python manage.py runserver
5. Visit: http://localhost:8000/admin/

💰 SKILLS GAINED: +?0K-$60K salary potential
🏢 READY FOR: Django positions at Instagram, Pinterest, Spotify level companies
"""
