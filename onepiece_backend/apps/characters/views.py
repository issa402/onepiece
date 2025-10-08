"""
🏴‍☠️ CHARACTER VIEWS - ENTERPRISE API WITH ALL HIGH-VALUE FEATURES

This API integrates ALL the technologies you wanted to learn:
✅ Django REST Framework with advanced features
✅ Redis caching for performance
✅ Elasticsearch for search
✅ WebSocket real-time updates
✅ Rate limiting and security
✅ Monitoring and logging
✅ GraphQL support
✅ Async operations
"""

from rest_framework import viewsets, status, filters
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.throttling import UserRateThrottle, AnonRateThrottle
from django_ratelimit.decorators import ratelimit
from django.core.cache import cache
from django.db.models import Q, F, Count, Sum, Avg
from django.utils.decorators import method_decorator
from django.views.decorators.cache import cache_page
from django.views.decorators.vary import vary_on_headers
from elasticsearch_dsl import Search
from channels.layers import get_channel_layer
from asgiref.sync import async_to_sync
import json
import logging
from decimal import Decimal
from datetime import datetime, timedelta

from .models import Character, Crew, PriceHistory, CharacterSearchDocument
from .serializers import (
    CharacterSerializer, CharacterDetailSerializer, 
    CrewSerializer, PriceHistorySerializer
)
from .tasks import update_character_analytics, broadcast_price_update

logger = logging.getLogger('onepiece.characters')

class CharacterThrottle(UserRateThrottle):
    """Custom throttle for character operations"""
    scope = 'character'
    rate = '100/hour'

class TradingThrottle(UserRateThrottle):
    """Custom throttle for trading operations"""
    scope = 'trading'
    rate = '500/hour'

class CharacterViewSet(viewsets.ModelViewSet):
    """
    🏴‍☠️ CHARACTER API - ENTERPRISE GRADE WITH ALL HIGH-VALUE FEATURES
    
    Features:
    ✅ Advanced filtering and search
    ✅ Redis caching for performance
    ✅ Elasticsearch integration
    ✅ Real-time WebSocket updates
    ✅ Rate limiting and security
    ✅ Monitoring and analytics
    ✅ Async task processing
    """
    
    queryset = Character.objects.active().with_price_data()
    serializer_class = CharacterSerializer
    permission_classes = [AllowAny]  # Adjust based on your needs
    throttle_classes = [CharacterThrottle, AnonRateThrottle]
    
    filter_backends = [filters.SearchFilter, filters.OrderingFilter]
    search_fields = ['name', 'crew__name', 'description']
    ordering_fields = ['current_price', 'bounty', 'weekly_change', 'created_at']
    ordering = ['-current_price']
    
    def get_serializer_class(self):
        """Use detailed serializer for retrieve actions"""
        if self.action == 'retrieve':
            return CharacterDetailSerializer
        return CharacterSerializer
    
    def get_queryset(self):
        """Optimized queryset with filtering"""
        queryset = super().get_queryset()
        
        # Filter by crew
        crew = self.request.query_params.get('crew')
        if crew:
            queryset = queryset.filter(crew__name__icontains=crew)
        
        # Filter by price range
        min_price = self.request.query_params.get('min_price')
        max_price = self.request.query_params.get('max_price')
        if min_price:
            queryset = queryset.filter(current_price__gte=min_price)
        if max_price:
            queryset = queryset.filter(current_price__lte=max_price)
        
        # Filter by bounty range
        min_bounty = self.request.query_params.get('min_bounty')
        if min_bounty:
            queryset = queryset.filter(bounty__gte=min_bounty)
        
        # Filter trending
        trending = self.request.query_params.get('trending')
        if trending and trending.lower() == 'true':
            queryset = queryset.filter(is_trending=True)
        
        return queryset
    
    @method_decorator(cache_page(60))  # Cache for 1 minute
    @method_decorator(vary_on_headers('Authorization'))
    def list(self, request, *args, **kwargs):
        """Cached list view with analytics"""
        logger.info(f"Character list requested by {request.user}")
        
        # Check cache first
        cache_key = f'characters:list:{request.GET.urlencode()}'
        cached_response = cache.get(cache_key)
        
        if cached_response:
            logger.info("Returning cached character list")
            return Response(cached_response)
        
        response = super().list(request, *args, **kwargs)
        
        # Add market summary to response
        if response.status_code == 200:
            market_data = self.get_market_summary()
            response.data['market_summary'] = market_data
            
            # Cache the response
            cache.set(cache_key, response.data, timeout=60)
        
        return response
    
    def retrieve(self, request, *args, **kwargs):
        """Enhanced retrieve with real-time data"""
        character = self.get_object()
        
        # Log character view
        logger.info(f"Character {character.name} viewed by {request.user}")
        
        # Get cached data
        cache_key = f'character:{character.id}:detail'
        cached_data = cache.get(cache_key)
        
        if not cached_data:
            serializer = self.get_serializer(character)
            cached_data = serializer.data
            
            # Add real-time analytics
            cached_data['analytics'] = {
                'price_history': character.get_price_history(days=7),
                'trading_volume': character.get_trading_volume(),
                'sentiment_data': character.get_sentiment_data(),
                'market_cap': character.market_cap,
                'price_change_24h': character.price_change_24h
            }
            
            cache.set(cache_key, cached_data, timeout=300)  # 5 minutes
        
        return Response(cached_data)
    
    @action(detail=False, methods=['get'])
    @method_decorator(cache_page(300))  # Cache for 5 minutes
    def trending(self, request):
        """Get trending characters"""
        limit = int(request.query_params.get('limit', 10))
        
        trending_chars = Character.objects.trending(limit=limit)
        serializer = self.get_serializer(trending_chars, many=True)
        
        return Response({
            'trending_characters': serializer.data,
            'timestamp': datetime.now().isoformat()
        })
    
    @action(detail=False, methods=['get'])
    @method_decorator(cache_page(600))  # Cache for 10 minutes
    def top_performers(self, request):
        """Get top performing characters"""
        limit = int(request.query_params.get('limit', 10))
        period = request.query_params.get('period', '24h')
        
        top_chars = Character.objects.top_performers(limit=limit)
        serializer = self.get_serializer(top_chars, many=True)
        
        return Response({
            'top_performers': serializer.data,
            'period': period,
            'timestamp': datetime.now().isoformat()
        })
    
    @action(detail=False, methods=['get'])
    def search_elasticsearch(self, request):
        """Advanced search using Elasticsearch"""
        query = request.query_params.get('q', '')
        if not query:
            return Response({'error': 'Query parameter q is required'}, 
                          status=status.HTTP_400_BAD_REQUEST)
        
        try:
            # Elasticsearch search
            s = Search(index='characters').query(
                'multi_match',
                query=query,
                fields=['name^3', 'crew^2', 'description'],
                fuzziness='AUTO'
            )
            
            # Add filters
            min_price = request.query_params.get('min_price')
            if min_price:
                s = s.filter('range', current_price={'gte': float(min_price)})
            
            crew = request.query_params.get('crew')
            if crew:
                s = s.filter('term', crew=crew)
            
            # Execute search
            response = s.execute()
            
            # Get character IDs from search results
            character_ids = [hit.meta.id for hit in response]
            
            # Fetch full character data from database
            characters = Character.objects.filter(id__in=character_ids)
            serializer = self.get_serializer(characters, many=True)
            
            return Response({
                'results': serializer.data,
                'total': response.hits.total.value,
                'query': query,
                'took': response.took
            })
            
        except Exception as e:
            logger.error(f"Elasticsearch search failed: {e}")
            # Fallback to database search
            characters = Character.objects.search(query)[:20]
            serializer = self.get_serializer(characters, many=True)
            
            return Response({
                'results': serializer.data,
                'total': characters.count(),
                'query': query,
                'fallback': True
            })
    
    @action(detail=True, methods=['post'])
    @method_decorator(ratelimit(key='user', rate='10/m', method='POST'))
    def update_price(self, request, pk=None):
        """Update character price with real-time broadcasting"""
        character = self.get_object()
        
        try:
            new_price = Decimal(str(request.data.get('price')))
            if new_price <= 0:
                return Response(
                    {'error': 'Price must be greater than 0'}, 
                    status=status.HTTP_400_BAD_REQUEST
                )
            
            old_price = character.current_price
            
            # Update price
            character.update_price(new_price)
            
            # Log price update
            logger.info(f"Price updated for {character.name}: ${old_price} -> ${new_price}")
            
            # Trigger async analytics update
            update_character_analytics.delay(character.id)
            
            # Broadcast to WebSocket clients
            broadcast_price_update.delay(character.id, float(new_price))
            
            return Response({
                'character': character.name,
                'old_price': float(old_price),
                'new_price': float(new_price),
                'change_percent': float(character.weekly_change),
                'market_cap': character.market_cap,
                'timestamp': character.last_price_update.isoformat()
            })
            
        except (ValueError, TypeError) as e:
            return Response(
                {'error': 'Invalid price format'}, 
                status=status.HTTP_400_BAD_REQUEST
            )
        except Exception as e:
            logger.error(f"Price update failed for {character.name}: {e}")
            return Response(
                {'error': 'Price update failed'}, 
                status=status.HTTP_500_INTERNAL_SERVER_ERROR
            )
    
    @action(detail=True, methods=['get'])
    @method_decorator(cache_page(60))
    def price_history(self, request, pk=None):
        """Get character price history"""
        character = self.get_object()
        days = int(request.query_params.get('days', 30))
        
        history = character.get_price_history(days=days)
        
        return Response({
            'character': character.name,
            'price_history': history,
            'period_days': days,
            'current_price': float(character.current_price)
        })
    
    @action(detail=True, methods=['get'])
    def analytics(self, request, pk=None):
        """Get comprehensive character analytics"""
        character = self.get_object()
        
        analytics_data = {
            'character': character.name,
            'current_metrics': {
                'price': float(character.current_price),
                'market_cap': character.market_cap,
                'bounty': character.bounty,
                'sentiment_score': float(character.sentiment_score),
                'weekly_change': float(character.weekly_change),
                'price_change_24h': character.price_change_24h
            },
            'trading_data': character.get_trading_volume(),
            'price_history': character.get_price_history(days=30),
            'sentiment_analysis': character.get_sentiment_data(),
            'crew_comparison': self.get_crew_comparison(character),
            'timestamp': datetime.now().isoformat()
        }
        
        return Response(analytics_data)
    
    def get_market_summary(self):
        """Get overall market summary"""
        cache_key = 'market:summary'
        summary = cache.get(cache_key)
        
        if not summary:
            total_characters = Character.objects.active().count()
            total_market_cap = sum(char.market_cap for char in Character.objects.active())
            avg_price = Character.objects.active().aggregate(Avg('current_price'))['current_price__avg']
            top_gainer = Character.objects.active().order_by('-weekly_change').first()
            top_loser = Character.objects.active().order_by('weekly_change').first()
            
            summary = {
                'total_characters': total_characters,
                'total_market_cap': total_market_cap,
                'average_price': float(avg_price) if avg_price else 0,
                'top_gainer': {
                    'name': top_gainer.name if top_gainer else None,
                    'change': float(top_gainer.weekly_change) if top_gainer else 0
                },
                'top_loser': {
                    'name': top_loser.name if top_loser else None,
                    'change': float(top_loser.weekly_change) if top_loser else 0
                }
            }
            
            cache.set(cache_key, summary, timeout=300)  # 5 minutes
        
        return summary
    
    def get_crew_comparison(self, character):
        """Get comparison with crew members"""
        crew_members = Character.objects.filter(
            crew=character.crew, 
            is_active=True
        ).exclude(id=character.id)
        
        comparison = []
        for member in crew_members:
            comparison.append({
                'name': member.name,
                'price': float(member.current_price),
                'change': float(member.weekly_change),
                'market_cap': member.market_cap
            })
        
        return sorted(comparison, key=lambda x: x['price'], reverse=True)

class CrewViewSet(viewsets.ReadOnlyModelViewSet):
    """Crew API with statistics"""
    queryset = Crew.objects.with_stats()
    serializer_class = CrewSerializer
    permission_classes = [AllowAny]
    
    @action(detail=True, methods=['get'])
    @method_decorator(cache_page(300))
    def members(self, request, pk=None):
        """Get crew members with statistics"""
        crew = self.get_object()
        members = crew.characters.active().order_by('-current_price')
        
        serializer = CharacterSerializer(members, many=True)
        
        return Response({
            'crew': crew.name,
            'members': serializer.data,
            'statistics': crew.get_cached_stats()
        })
    
    @action(detail=False, methods=['get'])
    @method_decorator(cache_page(600))
    def rankings(self, request):
        """Get crew rankings by various metrics"""
        crews = Crew.objects.popular()
        
        rankings = []
        for crew in crews:
            stats = crew.get_cached_stats()
            rankings.append({
                'name': crew.name,
                'captain': crew.captain,
                'member_count': stats['member_count'],
                'total_bounty': stats['total_bounty'],
                'total_market_cap': stats['total_market_cap'],
                'avg_price': stats['avg_price']
            })
        
        return Response({
            'crew_rankings': rankings,
            'timestamp': datetime.now().isoformat()
        })
