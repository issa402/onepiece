"""
🏴‍☠️ CHARACTER MODELS - ENTERPRISE DJANGO WITH ALL HIGH-VALUE FEATURES

This model integrates ALL the technologies you wanted to learn:
✅ Django ORM with advanced features
✅ PostgreSQL optimization with indexes
✅ Redis caching integration
✅ MongoDB document storage
✅ Elasticsearch search integration
✅ Real-time price updates
✅ Security features
✅ Performance optimization
"""

from django.db import models
from django.contrib.auth import get_user_model
from django.core.validators import MinValueValidator, MaxValueValidator
from django.core.cache import cache
from django.db.models import Q, F, Count, Sum, Avg
from django.utils import timezone
from decimal import Decimal
import json
import redis
from elasticsearch_dsl import Document, Text, Keyword, Float, Integer, Date
from pymongo import MongoClient
from datetime import datetime, timedelta

User = get_user_model()

# 🔍 ELASTICSEARCH DOCUMENT FOR SEARCH
class CharacterSearchDocument(Document):
    """Elasticsearch document for character search"""
    name = Text(analyzer='standard')
    crew = Keyword()
    description = Text(analyzer='standard')
    bounty = Integer()
    current_price = Float()
    sentiment_score = Float()
    
    class Index:
        name = 'characters'
        settings = {
            'number_of_shards': 1,
            'number_of_replicas': 0
        }

# 🗄️ MONGODB INTEGRATION
class MongoDBMixin:
    """Mixin for MongoDB operations"""
    
    @classmethod
    def get_mongo_client(cls):
        from django.conf import settings
        mongo_settings = settings.MONGODB_SETTINGS
        return MongoClient(
            host=mongo_settings['host'],
            port=mongo_settings['port'],
            username=mongo_settings.get('username'),
            password=mongo_settings.get('password')
        )
    
    def save_to_mongodb(self, collection_name='characters_analytics'):
        """Save analytics data to MongoDB"""
        client = self.get_mongo_client()
        db = client.onepiece_nosql
        collection = db[collection_name]
        
        document = {
            'character_id': self.id,
            'name': self.name,
            'crew': self.crew,
            'price_history': self.get_price_history(),
            'sentiment_analysis': self.get_sentiment_data(),
            'trading_volume': self.get_trading_volume(),
            'timestamp': datetime.utcnow()
        }
        
        collection.insert_one(document)
        client.close()

# 📊 CUSTOM MANAGERS AND QUERYSETS
class CrewQuerySet(models.QuerySet):
    def with_stats(self):
        """Annotate crews with member statistics"""
        return self.annotate(
            member_count=Count('characters'),
            total_bounty=Sum('characters__bounty'),
            avg_price=Avg('characters__current_price'),
            total_market_cap=Sum(F('characters__current_price') * 1000000)
        )
    
    def popular(self):
        """Get popular crews by member count"""
        return self.with_stats().filter(member_count__gte=3).order_by('-total_bounty')

class CrewManager(models.Manager):
    def get_queryset(self):
        return CrewQuerySet(self.model, using=self._db)
    
    def with_stats(self):
        return self.get_queryset().with_stats()
    
    def popular(self):
        return self.get_queryset().popular()

class Crew(models.Model):
    """Crew model with enterprise features"""
    name = models.CharField(max_length=100, unique=True, db_index=True)
    captain = models.CharField(max_length=100)
    ship_name = models.CharField(max_length=100, blank=True)
    formation_date = models.DateField(null=True, blank=True)
    description = models.TextField(blank=True)
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    objects = CrewManager()
    
    class Meta:
        db_table = 'crews'
        indexes = [
            models.Index(fields=['name']),
            models.Index(fields=['is_active', 'name']),
        ]
        ordering = ['name']
    
    def __str__(self):
        return self.name
    
    @property
    def cache_key(self):
        return f'crew:{self.id}'
    
    def get_cached_stats(self):
        """Get crew statistics from cache"""
        cache_key = f'{self.cache_key}:stats'
        stats = cache.get(cache_key)
        
        if stats is None:
            stats = {
                'member_count': self.characters.count(),
                'total_bounty': self.characters.aggregate(Sum('bounty'))['bounty__sum'] or 0,
                'avg_price': self.characters.aggregate(Avg('current_price'))['current_price__avg'] or 0,
                'total_market_cap': sum(char.market_cap for char in self.characters.all())
            }
            cache.set(cache_key, stats, timeout=300)  # 5 minutes
        
        return stats

class CharacterQuerySet(models.QuerySet):
    def active(self):
        """Get active characters only"""
        return self.filter(is_active=True)
    
    def by_crew(self, crew_name):
        """Filter by crew name"""
        return self.filter(crew__name=crew_name)
    
    def high_bounty(self, min_bounty=1000000000):
        """Filter by minimum bounty"""
        return self.filter(bounty__gte=min_bounty)
    
    def trending(self):
        """Get trending characters by price change"""
        return self.active().order_by('-weekly_change')
    
    def with_price_data(self):
        """Optimize queries with related data"""
        return self.select_related('crew').prefetch_related('price_history', 'trades')
    
    def search(self, query):
        """Search characters by name, crew, or description"""
        return self.filter(
            Q(name__icontains=query) |
            Q(crew__name__icontains=query) |
            Q(description__icontains=query)
        )

class CharacterManager(models.Manager):
    def get_queryset(self):
        return CharacterQuerySet(self.model, using=self._db)
    
    def active(self):
        return self.get_queryset().active()
    
    def trending(self, limit=10):
        return self.get_queryset().trending()[:limit]
    
    def top_performers(self, limit=10):
        return self.get_queryset().active().order_by('-current_price')[:limit]
    
    def search(self, query):
        return self.get_queryset().search(query)

class Character(models.Model, MongoDBMixin):
    """
    🏴‍☠️ CHARACTER MODEL - ENTERPRISE GRADE WITH ALL HIGH-VALUE FEATURES
    
    Integrates:
    ✅ PostgreSQL with optimized indexes
    ✅ Redis caching for performance
    ✅ MongoDB for analytics data
    ✅ Elasticsearch for search
    ✅ Real-time price updates
    ✅ Security validations
    """
    
    # Basic Information
    name = models.CharField(max_length=100, unique=True, db_index=True)
    crew = models.ForeignKey(Crew, on_delete=models.CASCADE, related_name='characters')
    bounty = models.BigIntegerField(
        default=0,
        validators=[MinValueValidator(0)],
        help_text="Character bounty in berries"
    )
    
    # Trading Information
    current_price = models.DecimalField(
        max_digits=10, 
        decimal_places=2, 
        default=Decimal('0.00'),
        validators=[MinValueValidator(Decimal('0.00'))]
    )
    sentiment_score = models.DecimalField(
        max_digits=3, 
        decimal_places=2, 
        default=Decimal('0.00'),
        validators=[MinValueValidator(Decimal('-1.00')), MaxValueValidator(Decimal('1.00'))]
    )
    weekly_change = models.DecimalField(
        max_digits=5, 
        decimal_places=2, 
        default=Decimal('0.00')
    )
    
    # Content
    description = models.TextField(blank=True)
    image_url = models.URLField(blank=True)
    
    # Status
    is_active = models.BooleanField(default=True)
    is_trending = models.BooleanField(default=False)
    
    # Timestamps
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    last_price_update = models.DateTimeField(auto_now=True)
    
    objects = CharacterManager()
    
    class Meta:
        db_table = 'characters'
        indexes = [
            # Performance indexes
            models.Index(fields=['crew', 'is_active']),
            models.Index(fields=['-bounty']),
            models.Index(fields=['-current_price']),
            models.Index(fields=['-weekly_change']),
            models.Index(fields=['is_trending', '-current_price']),
            models.Index(fields=['last_price_update']),
            
            # Search indexes
            models.Index(fields=['name', 'crew']),
        ]
        ordering = ['-current_price']
    
    def __str__(self):
        return f"{self.name} ({self.crew.name})"
    
    # 📊 CACHING PROPERTIES
    @property
    def cache_key(self):
        return f'character:{self.id}'
    
    @property
    def market_cap(self):
        """Calculate market cap (cached)"""
        cache_key = f'{self.cache_key}:market_cap'
        market_cap = cache.get(cache_key)
        
        if market_cap is None:
            market_cap = float(self.current_price) * 1000000  # Assume 1M shares
            cache.set(cache_key, market_cap, timeout=60)  # 1 minute
        
        return market_cap
    
    @property
    def price_change_24h(self):
        """Get 24h price change (cached)"""
        cache_key = f'{self.cache_key}:price_change_24h'
        change = cache.get(cache_key)
        
        if change is None:
            yesterday = timezone.now() - timedelta(days=1)
            try:
                old_price = self.price_history.filter(
                    timestamp__gte=yesterday
                ).order_by('timestamp').first()
                
                if old_price:
                    change = ((float(self.current_price) - float(old_price.price)) / float(old_price.price)) * 100
                else:
                    change = 0.0
                    
                cache.set(cache_key, change, timeout=300)  # 5 minutes
            except:
                change = 0.0
        
        return change
    
    # 🔍 SEARCH INTEGRATION
    def update_search_index(self):
        """Update Elasticsearch index"""
        try:
            doc = CharacterSearchDocument(
                meta={'id': self.id},
                name=self.name,
                crew=self.crew.name,
                description=self.description,
                bounty=self.bounty,
                current_price=float(self.current_price),
                sentiment_score=float(self.sentiment_score)
            )
            doc.save()
        except Exception as e:
            print(f"Failed to update search index for {self.name}: {e}")
    
    # 📊 ANALYTICS METHODS
    def get_price_history(self, days=30):
        """Get price history for analytics"""
        since = timezone.now() - timedelta(days=days)
        return list(
            self.price_history.filter(timestamp__gte=since)
            .values('price', 'timestamp')
            .order_by('timestamp')
        )
    
    def get_sentiment_data(self):
        """Get sentiment analysis data"""
        return {
            'current_score': float(self.sentiment_score),
            'trend': self.get_sentiment_trend(),
            'sources': self.get_sentiment_sources()
        }
    
    def get_trading_volume(self, days=7):
        """Get trading volume for period"""
        since = timezone.now() - timedelta(days=days)
        return self.trades.filter(created_at__gte=since).aggregate(
            total_volume=Sum('quantity'),
            total_value=Sum('total_amount')
        )
    
    # 🔄 REAL-TIME UPDATES
    def update_price(self, new_price, save_history=True):
        """Update price with real-time broadcasting"""
        old_price = self.current_price
        self.current_price = new_price
        
        # Calculate change
        if old_price > 0:
            self.weekly_change = ((new_price - old_price) / old_price) * 100
        
        self.last_price_update = timezone.now()
        self.save(update_fields=['current_price', 'weekly_change', 'last_price_update'])
        
        # Clear cache
        cache.delete(f'{self.cache_key}:market_cap')
        cache.delete(f'{self.cache_key}:price_change_24h')
        
        # Save to MongoDB for analytics
        self.save_to_mongodb('price_updates')
        
        # Update search index
        self.update_search_index()
        
        # Broadcast via WebSocket (implement in views)
        self.broadcast_price_update()
        
        # Save price history
        if save_history:
            PriceHistory.objects.create(
                character=self,
                price=new_price,
                volume=0  # Will be updated by trading system
            )
    
    def broadcast_price_update(self):
        """Broadcast price update via WebSocket"""
        from channels.layers import get_channel_layer
        from asgiref.sync import async_to_sync
        
        channel_layer = get_channel_layer()
        async_to_sync(channel_layer.group_send)(
            f'character_{self.id}',
            {
                'type': 'price_update',
                'character_id': self.id,
                'name': self.name,
                'price': float(self.current_price),
                'change': float(self.weekly_change),
                'market_cap': self.market_cap,
                'timestamp': self.last_price_update.isoformat()
            }
        )
    
    def save(self, *args, **kwargs):
        """Override save to handle caching and indexing"""
        is_new = self.pk is None
        super().save(*args, **kwargs)
        
        if not is_new:
            # Clear related caches
            cache.delete(f'{self.cache_key}:market_cap')
            cache.delete(f'crew:{self.crew_id}:stats')
        
        # Update search index
        self.update_search_index()

class PriceHistory(models.Model):
    """Price history for analytics and charting"""
    character = models.ForeignKey(Character, on_delete=models.CASCADE, related_name='price_history')
    price = models.DecimalField(max_digits=10, decimal_places=2)
    volume = models.BigIntegerField(default=0)
    timestamp = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        db_table = 'price_history'
        indexes = [
            models.Index(fields=['character', '-timestamp']),
            models.Index(fields=['-timestamp']),
        ]
        ordering = ['-timestamp']
    
    def __str__(self):
        return f"{self.character.name} - ${self.price} at {self.timestamp}"
