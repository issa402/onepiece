# 🏴‍☠️ MODULE 2: DJANGO ENTERPRISE MASTERY
## From Zero to Hero - Complete Django Enterprise Development

### 🎯 **WHAT YOU'LL LEARN FROM ABSOLUTE SCRATCH:**

#### **🔥 PART 1: DJANGO FUNDAMENTALS (What & Why)**
- **What is Django?** - High-level Python web framework for rapid development
- **Why Learn Django?** - Used by Instagram, Pinterest, Mozilla, Spotify
- **What is Django ORM?** - Object-Relational Mapping for database operations
- **What is Django Admin?** - Built-in admin interface for content management
- **What are Django Models?** - Python classes that represent database tables

#### **⚡ PART 2: DJANGO REST FRAMEWORK (Professional APIs)**
- **What is DRF?** - Powerful toolkit for building Web APIs
- **What are Serializers?** - Convert complex data types to JSON
- **What are ViewSets?** - Class-based views for handling HTTP methods
- **What is Authentication?** - JWT tokens, OAuth2, custom user models
- **What are Permissions?** - Role-based access control

#### **🗄️ PART 3: ADVANCED DJANGO (Enterprise Patterns)**
- **Database Optimization** - Query optimization, select_related, prefetch_related
- **Caching Strategies** - Redis integration, query caching, template caching
- **Custom Managers** - Reusable query logic and business rules
- **Signals** - Decoupled applications with event-driven architecture
- **Middleware** - Request/response processing and cross-cutting concerns

#### **🚀 PART 4: PRODUCTION DJANGO (Enterprise Ready)**
- **Security Best Practices** - CSRF, XSS, SQL injection prevention
- **Testing Strategies** - Unit tests, integration tests, API testing
- **Deployment** - Docker, Kubernetes, CI/CD pipelines
- **Monitoring** - Logging, error tracking, performance monitoring

### 💰 **SALARY PROGRESSION:**
```
📚 Basic Flask (simple routes, templates)       →  $70K-$100K  (Junior Backend)
⚡ Django Fundamentals (models, views, admin)   →  $100K-$140K (Mid-Level Backend)
🗄️ Django REST Framework (APIs, auth)          →  $140K-$190K (Senior Backend)
🚀 Enterprise Django (optimization, scale)     →  $190K-$280K (Staff Engineer)
🌐 Django Architecture (microservices, lead)   →  $280K-$450K+ (Principal Engineer)
```

### 🏢 **COMPANIES THAT HIRE FOR THESE SKILLS:**

#### **🔥 BASIC DJANGO:**
- **Entry Level**: Smaller startups, agencies, content management companies
- **Why They Need It**: Rapid development, built-in admin, Python ecosystem

#### **⚡ DJANGO REST FRAMEWORK:**
- **Mid Level**: Instagram, Pinterest, Mozilla, Spotify, Dropbox
- **Why They Need It**: Scalable APIs, authentication, content delivery

#### **🗄️ ADVANCED DJANGO:**
- **Senior Level**: Goldman Sachs, JPMorgan, trading firms, fintech companies
- **Why They Need It**: High-performance applications, complex business logic

#### **🚀 ENTERPRISE DJANGO:**
- **Staff Level**: Google, Microsoft, large enterprises, government contracts
- **Why They Need It**: Scalable architecture, security compliance, team leadership

### 🔥 **WHY EACH CONCEPT MATTERS FOR YOUR CAREER:**

#### **📚 DJANGO VS FLASK (Why Upgrade):**
```python
# ❌ YOUR CURRENT FLASK APP (basic and limited):
from flask import Flask, jsonify

app = Flask(__name__)

@app.route('/api/characters')
def get_characters():
    # Hardcoded data - not scalable
    characters = [
        {"name": "Luffy", "bounty": 3000000000},
        {"name": "Zoro", "bounty": 1111000000}
    ]
    return jsonify(characters)

# Problems with Flask:
# - No built-in admin interface
# - Manual database management
# - No built-in authentication
# - Limited ORM capabilities
# - Manual API documentation
# - No built-in security features

# ✅ DJANGO EQUIVALENT (professional and scalable):
# models.py
from django.db import models
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    balance = models.DecimalField(max_digits=12, decimal_places=2, default=10000.00)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.username

class Character(models.Model):
    name = models.CharField(max_length=100, unique=True)
    crew = models.CharField(max_length=100)
    bounty = models.BigIntegerField()
    current_price = models.DecimalField(max_digits=10, decimal_places=2)
    daily_change = models.DecimalField(max_digits=5, decimal_places=2, default=0.00)
    devil_fruit = models.CharField(max_length=100, blank=True, null=True)
    abilities = models.JSONField(default=list)
    image_url = models.URLField(blank=True, null=True)
    description = models.TextField(blank=True)
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['-bounty']
        indexes = [
            models.Index(fields=['crew']),
            models.Index(fields=['bounty']),
            models.Index(fields=['current_price']),
        ]

    def __str__(self):
        return f"{self.name} ({self.crew})"
```
**Why This Matters**: Django provides enterprise-level features out of the box. Instagram uses Django to serve 400 million users daily.
| **Built-in Admin** | ✅ Auto-generated | ❌ Manual | ❌ Manual |
| **ORM** | ✅ Powerful Django ORM | ❌ Need SQLAlchemy | ❌ Need SQLAlchemy |
| **Authentication** | ✅ Built-in + customizable | ❌ Manual | ❌ Manual |
| **Migrations** | ✅ Automatic | ❌ Manual with Alembic | ❌ Manual |
| **Security** | ✅ CSRF, XSS, SQL injection protection | ❌ Manual | ❌ Manual |
| **Caching** | ✅ Built-in framework | ❌ Manual setup | ❌ Manual setup |
| **Background Tasks** | ✅ Celery integration | ❌ Manual setup | ❌ Manual setup |
| **API Documentation** | ✅ DRF auto-docs | ❌ Manual | ✅ Auto-generated |

**🎯 VERDICT:** Django = Less code, more features, faster development, enterprise-ready

---

## 🧪 **HANDS-ON LAB 1: DJANGO PROJECT ARCHITECTURE**

### **📋 YOUR MISSION:**
Transform your Flask One Piece project into enterprise Django architecture

### **🎯 LEARNING OBJECTIVES:**
- Understand Django project vs app structure
- Configure settings for multiple environments
- Set up Django REST Framework
- Implement proper URL routing

### **💻 STEP-BY-STEP IMPLEMENTATION:**

#### **STEP 1: Create Django Project Structure**
```bash
# TODO 1: Install Django and create project
cd /home/isjim/onepiece
pip install django djangorestframework django-cors-headers python-decouple
pip install psycopg2-binary redis celery django-redis

# TODO 2: Create Django project
django-admin startproject onepiece_backend .
cd onepiece_backend

# TODO 3: Create Django apps (microservices approach)
python manage.py startapp characters
python manage.py startapp trading  
python manage.py startapp portfolio
python manage.py startapp users
python manage.py startapp notifications
```

#### **STEP 2: Enterprise Settings Configuration**
```python
# TODO 4: Create settings/base.py (copy this structure)
"""
onepiece_backend/
├── settings/
│   ├── __init__.py
│   ├── base.py          # Common settings
│   ├── development.py   # Dev environment
│   ├── production.py    # Production environment
│   └── testing.py       # Test environment
├── urls.py
└── wsgi.py
"""

# settings/base.py - Enterprise configuration
import os
from decouple import config

BASE_DIR = Path(__file__).resolve().parent.parent.parent

# Security
SECRET_KEY = config('SECRET_KEY', default='your-secret-key-here')
DEBUG = config('DEBUG', default=False, cast=bool)

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
    'corsheaders',
    'django_filters',
]

LOCAL_APPS = [
    'characters',
    'trading',
    'portfolio', 
    'users',
    'notifications',
]

INSTALLED_APPS = DJANGO_APPS + THIRD_PARTY_APPS + LOCAL_APPS

# Database configuration
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': config('DB_NAME', default='onepiece_market'),
        'USER': config('DB_USER', default='postgres'),
        'PASSWORD': config('DB_PASSWORD', default='onepiece123'),
        'HOST': config('DB_HOST', default='localhost'),
        'PORT': config('DB_PORT', default='5432'),
    }
}

# Redis configuration
REDIS_URL = config('REDIS_URL', default='redis://localhost:6379/0')

CACHES = {
    'default': {
        'BACKEND': 'django_redis.cache.RedisCache',
        'LOCATION': REDIS_URL,
        'OPTIONS': {
            'CLIENT_CLASS': 'django_redis.client.DefaultClient',
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
        'trading': '10/minute',  # Custom rate for trading
    },
    'DEFAULT_PAGINATION_CLASS': 'rest_framework.pagination.PageNumberPagination',
    'PAGE_SIZE': 20,
    'DEFAULT_FILTER_BACKENDS': [
        'django_filters.rest_framework.DjangoFilterBackend',
        'rest_framework.filters.SearchFilter',
        'rest_framework.filters.OrderingFilter',
    ],
}
```

---

## 🧪 **HANDS-ON LAB 2: ENTERPRISE MODELS & ORM**

### **📋 YOUR MISSION:**
Create production-ready Django models with advanced ORM features

### **🎯 LEARNING OBJECTIVES:**
- Design normalized database schema
- Implement model relationships and constraints
- Add custom model methods and properties
- Optimize queries with select_related and prefetch_related

### **💻 CHARACTER MODEL IMPLEMENTATION:**

#### **STEP 1: Enterprise Character Model**
```python
# TODO 5: Create characters/models.py
from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator
from django.contrib.auth.models import User
from decimal import Decimal

class CrewManager(models.Manager):
    """Custom manager for Crew model with optimized queries"""
    
    def with_member_count(self):
        return self.annotate(
            member_count=models.Count('characters')
        )
    
    def active_crews(self):
        return self.filter(is_active=True)

class Crew(models.Model):
    """Pirate crew model with enterprise features"""
    name = models.CharField(max_length=100, unique=True, db_index=True)
    captain = models.CharField(max_length=100)
    description = models.TextField(blank=True)
    founded_date = models.DateField(null=True, blank=True)
    is_active = models.BooleanField(default=True, db_index=True)
    
    # Metadata
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    objects = CrewManager()
    
    class Meta:
        db_table = 'crews'
        ordering = ['name']
        indexes = [
            models.Index(fields=['name', 'is_active']),
        ]
    
    def __str__(self):
        return f"{self.name} (Captain: {self.captain})"
    
    @property
    def total_bounty(self):
        """Calculate total bounty of all crew members"""
        return self.characters.aggregate(
            total=models.Sum('bounty')
        )['total'] or 0

class CharacterManager(models.Manager):
    """Custom manager with enterprise query optimizations"""
    
    def active(self):
        return self.filter(is_active=True)
    
    def with_crew_info(self):
        return self.select_related('crew')
    
    def top_bounties(self, limit=10):
        return self.active().order_by('-bounty')[:limit]
    
    def by_crew(self, crew_name):
        return self.filter(crew__name__icontains=crew_name)

class Character(models.Model):
    """Enterprise character model with full business logic"""
    
    # Basic Information
    name = models.CharField(max_length=100, unique=True, db_index=True)
    crew = models.ForeignKey(
        Crew, 
        on_delete=models.CASCADE, 
        related_name='characters',
        db_index=True
    )
    bounty = models.BigIntegerField(
        validators=[MinValueValidator(0)],
        help_text="Bounty in Berries"
    )
    
    # Trading Information
    current_price = models.DecimalField(
        max_digits=10, 
        decimal_places=2,
        validators=[MinValueValidator(Decimal('0.01'))]
    )
    market_cap = models.DecimalField(
        max_digits=15, 
        decimal_places=2,
        default=Decimal('0.00')
    )
    
    # Performance Metrics
    sentiment_score = models.FloatField(
        default=0.0,
        validators=[MinValueValidator(-1.0), MaxValueValidator(1.0)],
        help_text="Sentiment score between -1 and 1"
    )
    weekly_change = models.FloatField(
        default=0.0,
        help_text="Weekly price change percentage"
    )
    
    # Content
    description = models.TextField()
    image_url = models.URLField(blank=True, null=True)
    
    # Status
    is_active = models.BooleanField(default=True, db_index=True)
    is_tradeable = models.BooleanField(default=True)
    
    # Metadata
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    objects = CharacterManager()
    
    class Meta:
        db_table = 'characters'
        ordering = ['-bounty']
        indexes = [
            models.Index(fields=['name', 'is_active']),
            models.Index(fields=['crew', 'bounty']),
            models.Index(fields=['current_price', 'is_tradeable']),
        ]
        constraints = [
            models.CheckConstraint(
                check=models.Q(current_price__gt=0),
                name='positive_price'
            ),
            models.CheckConstraint(
                check=models.Q(bounty__gte=0),
                name='non_negative_bounty'
            ),
        ]
    
    def __str__(self):
        return f"{self.name} ({self.crew.name})"
    
    @property
    def price_change_indicator(self):
        """Return price change indicator for UI"""
        if self.weekly_change > 0:
            return 'up'
        elif self.weekly_change < 0:
            return 'down'
        return 'neutral'
    
    def calculate_market_cap(self):
        """Calculate and update market cap based on current metrics"""
        # Simplified calculation - in reality this would be more complex
        base_value = float(self.current_price) * (self.bounty / 1000000)
        sentiment_multiplier = 1 + (self.sentiment_score * 0.2)
        self.market_cap = Decimal(str(base_value * sentiment_multiplier))
        return self.market_cap
    
    def update_price(self, new_price, save=True):
        """Update price with automatic change calculation"""
        if self.current_price:
            old_price = float(self.current_price)
            change = ((float(new_price) - old_price) / old_price) * 100
            self.weekly_change = change
        
        self.current_price = new_price
        self.calculate_market_cap()
        
        if save:
            self.save(update_fields=['current_price', 'weekly_change', 'market_cap'])
```

---

## 📚 **ESSENTIAL RESOURCES FOR DJANGO MASTERY:**

### **📖 MUST-READ DOCUMENTATION:**
1. **Django Documentation** - https://docs.djangoproject.com/
2. **Django REST Framework** - https://www.django-rest-framework.org/
3. **Two Scoops of Django** - Best practices book

### **🎥 VIDEO COURSES:**
1. **Django for Professionals** - https://djangoforprofessionals.com/
2. **Django REST Framework Course** - https://testdriven.io/courses/

### **🛠️ TOOLS TO MASTER:**
- **Django Debug Toolbar** - Performance profiling
- **Django Extensions** - Enhanced management commands
- **Celery** - Background task processing

---

## 🎯 **NEXT STEPS:**
1. Complete all TODO items in this module
2. Migrate your Flask models to Django
3. Set up Django REST Framework APIs
4. Move to **Module 3: Database Architecture & Optimization**

**🔥 Ready to build enterprise Django? Start with TODO 1!**
