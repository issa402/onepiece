"""
🏴‍☠️ APIs & PROTOCOLS MASTERY - HANDS-ON CODING LAB
═══════════════════════════════════════════════════════════

🎯 WHAT YOU'LL CODE TODAY:
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
✅ REST API best practices for One Piece trading platform
✅ GraphQL implementation for flexible data querying
✅ gRPC for high-performance microservices communication
✅ WebSockets for real-time trading updates
✅ API versioning and backward compatibility
✅ Protocol optimization and performance tuning

💰 SALARY IMPACT: +?0K-?00K (API expertise is CRITICAL)
🏢 COMPANIES: Every tech company (APIs are the backbone)

📚 WHY API MASTERY = BIG MONEY:
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

🔥 APIs POWER THE DIGITAL ECONOMY:

1. API ECONOMY SIZE:
   - ?.2 trillion API economy by 2025
   - 83% of internet traffic is API calls
   - Average company uses 1,200+ APIs
   - API-first companies grow 12% faster

2. ENTERPRISE API USAGE:
   - Netflix: 1 billion API calls per day
   - Twitter: 13 billion API calls per day
   - Uber: 40+ microservices communicating via APIs
   - Stripe: 99.99% API uptime requirement

3. PROTOCOL PERFORMANCE:
   - REST: Universal, easy to use
   - GraphQL: Reduces over-fetching by 90%
   - gRPC: 10x faster than REST for microservices
   - WebSockets: Real-time with 50ms latency

🔥 WHY COMPANIES PAY PREMIUM FOR API ENGINEERS:

1. BUSINESS CRITICAL:
   - APIs enable digital transformation
   - Poor API design costs millions in development time
   - API downtime = revenue loss
   - Good APIs attract developers and partners

2. TECHNICAL COMPLEXITY:
   - Protocol selection impacts performance
   - Security and authentication challenges
   - Scalability and rate limiting
   - Documentation and developer experience

3. INTEGRATION EXPERTISE:
   - Third-party API integrations
   - Legacy system modernization
   - Microservices architecture
   - Real-time data synchronization

📖 ESSENTIAL RESOURCES:
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
🔗 REST API Design: https://restfulapi.net/
🔗 GraphQL Docs: https://graphql.org/learn/
🔗 gRPC Guide: https://grpc.io/docs/
🔗 WebSocket API: https://developer.mozilla.org/en-US/docs/Web/API/WebSockets_API
🔗 API Security: https://owasp.org/www-project-api-security/
"""

# ═══════════════════════════════════════════════════════════
# 🧪 HANDS-ON LAB 1: REST API BEST PRACTICES FOR ONE PIECE
# ═══════════════════════════════════════════════════════════

"""
📚 REST API DESIGN FOR ONE PIECE TRADING PLATFORM:

🔥 REST API BEST PRACTICES:

1. RESOURCE-BASED URLS:
   - /api/v1/characters/  # Collection
   - /api/v1/characters/123/  # Specific resource
   - /api/v1/users/456/portfolio/  # Nested resource
   - /api/v1/trading/execute/  # Action endpoint

2. HTTP METHODS:
   - GET: Retrieve data (idempotent)
   - POST: Create new resources
   - PUT: Update entire resource (idempotent)
   - PATCH: Partial update
   - DELETE: Remove resource (idempotent)

3. STATUS CODES:
   - 200: OK (successful GET, PUT, PATCH)
   - 201: Created (successful POST)
   - 204: No Content (successful DELETE)
   - 400: Bad Request (client error)
   - 401: Unauthorized (authentication required)
   - 403: Forbidden (insufficient permissions)
   - 404: Not Found (resource doesn't exist)
   - 500: Internal Server Error (server error)

4. RESPONSE FORMAT:
   {
     "data": { ... },
     "meta": {
       "pagination": { ... },
       "timestamp": "2024-01-01T00:00:00Z"
     },
     "errors": [ ... ]
   }

🎯 YOUR CODING MISSION:
Build enterprise-grade REST APIs for One Piece trading!
"""

# TODO 1: CREATE ADVANCED REST API VIEWS
# ═══════════════════════════════════════════════════════════
"""
🎯 YOUR TASK: Create comprehensive REST API views with best practices

Create file: apps/api/v1/views.py
"""

# FILE: apps/api/v1/views.py
# YOUR CODE HERE - Import required modules:
from rest_framework import viewsets, status, permissions
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework.pagination import PageNumberPagination
from django_filters.rest_framework import DjangoFilterBackend
# Add more imports...

# YOUR CODE HERE - Create custom pagination:
class OnePiecePagination(PageNumberPagination):
    """Custom pagination for One Piece API"""
    page_size = 20
    page_size_query_param = 'page_size'
    max_page_size = 100
    
    def get_paginated_response(self, data):
        return Response({
            'data': data,
            'meta': {
                'pagination': {
                    'page': self.page.number,
                    'pages': self.page.paginator.num_pages,
                    'per_page': self.page_size,
                    'total': self.page.paginator.count,
                    'has_next': self.page.has_next(),
                    'has_previous': self.page.has_previous(),
                }
            }
        })

# YOUR CODE HERE - Create character API viewset:
class CharacterViewSet(viewsets.ModelViewSet):
    """
    ViewSet for One Piece character management
    
    Provides CRUD operations for characters with advanced filtering,
    sorting, and search capabilities.
    """
    
    # Add queryset and serializer
    queryset = # Add Character queryset
    serializer_class = # Add CharacterSerializer
    pagination_class = OnePiecePagination
    permission_classes = [permissions.IsAuthenticated]
    
    # Add filtering and search
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['crew', 'devil_fruit', 'bounty_range']
    search_fields = ['name', 'crew', 'abilities']
    ordering_fields = ['name', 'bounty', 'created_at']
    ordering = ['-bounty']
    
    # YOUR CODE HERE - Add custom actions:
    @action(detail=True, methods=['post'])
    def add_to_watchlist(self, request, pk=None):
        """Add character to user's watchlist"""
        # Add watchlist logic
        pass
    
    @action(detail=False, methods=['get'])
    def trending(self, request):
        """Get trending characters based on trading volume"""
        # Add trending logic
        pass
    
    @action(detail=False, methods=['get'])
    def top_performers(self, request):
        """Get top performing characters by price change"""
        # Add top performers logic
        pass
    
    # YOUR CODE HERE - Override methods for custom behavior:
    def create(self, request, *args, **kwargs):
        """Create new character with validation"""
        # Add custom creation logic
        pass
    
    def update(self, request, *args, **kwargs):
        """Update character with audit logging"""
        # Add custom update logic
        pass

# YOUR CODE HERE - Create trading API viewset:
class TradingViewSet(viewsets.ViewSet):
    """
    ViewSet for One Piece trading operations
    
    Handles trade execution, portfolio management, and trading history.
    """
    
    permission_classes = [permissions.IsAuthenticated]
    
    @action(detail=False, methods=['post'])
    def execute_trade(self, request):
        """Execute a buy or sell trade"""
        # Add trade execution logic
        pass
    
    @action(detail=False, methods=['get'])
    def portfolio(self, request):
        """Get user's current portfolio"""
        # Add portfolio retrieval logic
        pass
    
    @action(detail=False, methods=['get'])
    def history(self, request):
        """Get user's trading history"""
        # Add trading history logic
        pass
    
    @action(detail=False, methods=['get'])
    def market_data(self, request):
        """Get real-time market data"""
        # Add market data logic
        pass

# TODO 2: CREATE API VERSIONING STRATEGY
# ═══════════════════════════════════════════════════════════
"""
🎯 YOUR TASK: Implement API versioning for backward compatibility

Create file: apps/api/versioning.py
"""

# FILE: apps/api/versioning.py
# YOUR CODE HERE - Create versioning classes:
from rest_framework.versioning import URLPathVersioning
from rest_framework.response import Response
from rest_framework import status

class OnePieceAPIVersioning(URLPathVersioning):
    """Custom API versioning for One Piece platform"""
    
    allowed_versions = ['v1', 'v2']
    default_version = 'v1'
    version_param = 'version'
    
    def determine_version(self, request, *args, **kwargs):
        version = super().determine_version(request, *args, **kwargs)
        
        # Log version usage for analytics
        # Add version logging logic
        
        return version

# YOUR CODE HERE - Create version-specific serializers:
class CharacterSerializerV1:
    """Character serializer for API v1"""
    # Add v1 serializer fields
    pass

class CharacterSerializerV2:
    """Character serializer for API v2 with additional fields"""
    # Add v2 serializer fields with new features
    pass

# YOUR CODE HERE - Create version-aware viewset:
class VersionedCharacterViewSet(viewsets.ModelViewSet):
    """Version-aware character viewset"""
    
    def get_serializer_class(self):
        """Return appropriate serializer based on API version"""
        if self.request.version == 'v2':
            return CharacterSerializerV2
        return CharacterSerializerV1

# TODO 3: CREATE API DOCUMENTATION
# ═══════════════════════════════════════════════════════════
"""
🎯 YOUR TASK: Create comprehensive API documentation

Create file: apps/api/documentation.py
"""

# FILE: apps/api/documentation.py
# YOUR CODE HERE - Create API documentation:
from drf_spectacular.utils import extend_schema, OpenApiParameter
from drf_spectacular.types import OpenApiTypes

# YOUR CODE HERE - Add API documentation decorators:
@extend_schema(
    summary="Get One Piece characters",
    description="Retrieve a paginated list of One Piece characters with filtering and search capabilities.",
    parameters=[
        OpenApiParameter(
            name='crew',
            type=OpenApiTypes.STR,
            location=OpenApiParameter.QUERY,
            description='Filter by character crew'
        ),
        OpenApiParameter(
            name='search',
            type=OpenApiTypes.STR,
            location=OpenApiParameter.QUERY,
            description='Search characters by name or abilities'
        ),
    ],
    responses={
        200: "List of characters retrieved successfully",
        400: "Invalid query parameters",
        401: "Authentication required"
    }
)
def documented_character_list(self, request):
    """Documented character list endpoint"""
    pass

# ═══════════════════════════════════════════════════════════
# 🧪 HANDS-ON LAB 2: GRAPHQL FOR FLEXIBLE DATA QUERYING
# ═══════════════════════════════════════════════════════════

"""
📚 GRAPHQL FOR ONE PIECE TRADING PLATFORM:

🔥 GRAPHQL ADVANTAGES:

1. FLEXIBLE QUERIES:
   - Client specifies exactly what data to fetch
   - Reduces over-fetching and under-fetching
   - Single endpoint for all data needs
   - Strongly typed schema

2. REAL-TIME SUBSCRIPTIONS:
   - Live price updates
   - Portfolio changes
   - Trading notifications
   - Market events

3. INTROSPECTION:
   - Self-documenting API
   - Schema exploration
   - Type safety
   - Developer tools

GRAPHQL QUERY EXAMPLE:
query GetCharacterWithTrades($id: ID!) {
  character(id: $id) {
    name
    bounty
    currentPrice
    trades(limit: 10) {
      id
      action
      quantity
      price
      timestamp
      user {
        username
      }
    }
  }
}

🎯 YOUR CODING MISSION:
Implement GraphQL for flexible One Piece data access!
"""

# TODO 4: CREATE GRAPHQL SCHEMA
# ═══════════════════════════════════════════════════════════
"""
🎯 YOUR TASK: Create GraphQL schema for One Piece platform

Create file: apps/graphql/schema.py
"""

# FILE: apps/graphql/schema.py
# YOUR CODE HERE - Import GraphQL modules:
import graphene
from graphene_django import DjangoObjectType
from graphene_django.filter import DjangoFilterConnectionField
# Add more imports...

# YOUR CODE HERE - Create GraphQL types:
class CharacterType(DjangoObjectType):
    """GraphQL type for One Piece characters"""
    
    class Meta:
        model = # Add Character model
        fields = # Add fields to expose
        filter_fields = {
            'name': ['exact', 'icontains'],
            'crew': ['exact'],
            'bounty': ['exact', 'gte', 'lte'],
        }
        interfaces = (graphene.relay.Node,)
    
    # Add custom fields
    current_price = graphene.Float()
    price_change_24h = graphene.Float()
    trading_volume_24h = graphene.Int()
    
    def resolve_current_price(self, info):
        """Resolve current market price"""
        # Add price resolution logic
        pass
    
    def resolve_price_change_24h(self, info):
        """Resolve 24-hour price change"""
        # Add price change logic
        pass

class TradeType(DjangoObjectType):
    """GraphQL type for trades"""
    
    class Meta:
        model = # Add Trade model
        fields = # Add fields to expose
        interfaces = (graphene.relay.Node,)

class UserType(DjangoObjectType):
    """GraphQL type for users"""
    
    class Meta:
        model = # Add User model
        fields = # Add fields to expose
        interfaces = (graphene.relay.Node,)
    
    # Add custom fields
    portfolio_value = graphene.Float()
    total_trades = graphene.Int()
    
    def resolve_portfolio_value(self, info):
        """Calculate total portfolio value"""
        # Add portfolio calculation logic
        pass

# YOUR CODE HERE - Create GraphQL queries:
class Query(graphene.ObjectType):
    """GraphQL queries for One Piece platform"""
    
    # Character queries
    character = graphene.relay.Node.Field(CharacterType)
    all_characters = DjangoFilterConnectionField(CharacterType)
    trending_characters = graphene.List(CharacterType, limit=graphene.Int())
    
    # Trading queries
    trade = graphene.relay.Node.Field(TradeType)
    user_trades = graphene.List(TradeType, user_id=graphene.ID())
    market_data = graphene.Field(graphene.JSONString)
    
    # User queries
    user = graphene.relay.Node.Field(UserType)
    current_user = graphene.Field(UserType)
    
    def resolve_trending_characters(self, info, limit=10):
        """Resolve trending characters"""
        # Add trending logic
        pass
    
    def resolve_market_data(self, info):
        """Resolve real-time market data"""
        # Add market data logic
        pass
    
    def resolve_current_user(self, info):
        """Resolve current authenticated user"""
        if info.context.user.is_authenticated:
            return info.context.user
        return None

# YOUR CODE HERE - Create GraphQL mutations:
class ExecuteTradeMutation(graphene.Mutation):
    """Mutation to execute a trade"""
    
    class Arguments:
        character_id = graphene.ID(required=True)
        action = graphene.String(required=True)
        quantity = graphene.Int(required=True)
        price = graphene.Float()
    
    # Output fields
    trade = graphene.Field(TradeType)
    success = graphene.Boolean()
    errors = graphene.List(graphene.String)
    
    def mutate(self, info, character_id, action, quantity, price=None):
        """Execute trade mutation"""
        # Add trade execution logic
        pass

class Mutation(graphene.ObjectType):
    """GraphQL mutations for One Piece platform"""
    
    execute_trade = ExecuteTradeMutation.Field()

# YOUR CODE HERE - Create GraphQL subscriptions:
class Subscription(graphene.ObjectType):
    """GraphQL subscriptions for real-time updates"""
    
    price_updates = graphene.Field(
        graphene.JSONString,
        character_id=graphene.ID()
    )
    
    portfolio_updates = graphene.Field(
        graphene.JSONString,
        user_id=graphene.ID()
    )
    
    def resolve_price_updates(self, info, character_id=None):
        """Subscribe to price updates"""
        # Add price subscription logic
        pass
    
    def resolve_portfolio_updates(self, info, user_id=None):
        """Subscribe to portfolio updates"""
        # Add portfolio subscription logic
        pass

# Create schema
schema = graphene.Schema(
    query=Query,
    mutation=Mutation,
    subscription=Subscription
)

# ═══════════════════════════════════════════════════════════
# 🧪 HANDS-ON LAB 3: GRPC FOR HIGH-PERFORMANCE COMMUNICATION
# ═══════════════════════════════════════════════════════════

"""
📚 GRPC FOR ONE PIECE MICROSERVICES:

🔥 GRPC ADVANTAGES:

1. PERFORMANCE:
   - Binary protocol (vs JSON in REST)
   - HTTP/2 multiplexing
   - 10x faster than REST
   - Smaller payload size

2. TYPE SAFETY:
   - Protocol Buffers schema
   - Code generation
   - Compile-time validation
   - Cross-language support

3. STREAMING:
   - Server streaming (real-time data)
   - Client streaming (bulk uploads)
   - Bidirectional streaming
   - Built-in flow control

GRPC USE CASES IN ONE PIECE:
- Price calculation service
- Risk assessment service
- Real-time market data
- Inter-service communication

🎯 YOUR CODING MISSION:
Implement gRPC for high-performance One Piece services!
"""

# TODO 5: CREATE GRPC PROTOCOL BUFFERS
# ═══════════════════════════════════════════════════════════
"""
🎯 YOUR TASK: Create Protocol Buffers definitions

Create file: protos/onepiece.proto
"""

# FILE: protos/onepiece.proto
# YOUR CODE HERE - Create protobuf definitions:
"""
syntax = "proto3";

package onepiece;

// Character service
service CharacterService {
  rpc GetCharacter(GetCharacterRequest) returns (Character);
  rpc ListCharacters(ListCharactersRequest) returns (ListCharactersResponse);
  rpc UpdateCharacterPrice(UpdatePriceRequest) returns (UpdatePriceResponse);
  rpc StreamPriceUpdates(StreamPriceRequest) returns (stream PriceUpdate);
}

// Trading service
service TradingService {
  rpc ExecuteTrade(ExecuteTradeRequest) returns (ExecuteTradeResponse);
  rpc GetPortfolio(GetPortfolioRequest) returns (Portfolio);
  rpc StreamTrades(StreamTradesRequest) returns (stream Trade);
}

// Messages
message Character {
  string id = 1;
  string name = 2;
  string crew = 3;
  double bounty = 4;
  double current_price = 5;
  double price_change_24h = 6;
  int64 trading_volume = 7;
  int64 created_at = 8;
  int64 updated_at = 9;
}

message GetCharacterRequest {
  string id = 1;
}

message ListCharactersRequest {
  int32 page = 1;
  int32 page_size = 2;
  string crew_filter = 3;
  string search_query = 4;
}

message ListCharactersResponse {
  repeated Character characters = 1;
  int32 total_count = 2;
  int32 page = 3;
  int32 page_size = 4;
}

message UpdatePriceRequest {
  string character_id = 1;
  double new_price = 2;
  string updated_by = 3;
}

message UpdatePriceResponse {
  bool success = 1;
  string message = 2;
  Character character = 3;
}

message PriceUpdate {
  string character_id = 1;
  double old_price = 2;
  double new_price = 3;
  double change_percent = 4;
  int64 timestamp = 5;
}

message StreamPriceRequest {
  repeated string character_ids = 1;
}

message Trade {
  string id = 1;
  string user_id = 2;
  string character_id = 3;
  string action = 4; // "buy" or "sell"
  int32 quantity = 5;
  double price = 6;
  double total_amount = 7;
  int64 timestamp = 8;
}

message ExecuteTradeRequest {
  string user_id = 1;
  string character_id = 2;
  string action = 3;
  int32 quantity = 4;
  double price = 5;
}

message ExecuteTradeResponse {
  bool success = 1;
  string message = 2;
  Trade trade = 3;
  repeated string errors = 4;
}

message Portfolio {
  string user_id = 1;
  repeated PortfolioItem items = 2;
  double total_value = 3;
  double cash_balance = 4;
  double total_return = 5;
  double total_return_percent = 6;
}

message PortfolioItem {
  string character_id = 1;
  string character_name = 2;
  int32 quantity = 3;
  double average_price = 4;
  double current_price = 5;
  double total_value = 6;
  double unrealized_gain_loss = 7;
  double unrealized_gain_loss_percent = 8;
}

message GetPortfolioRequest {
  string user_id = 1;
}

message StreamTradesRequest {
  string user_id = 1;
}
"""

# TODO 6: CREATE GRPC SERVER IMPLEMENTATION
# ═══════════════════════════════════════════════════════════
"""
🎯 YOUR TASK: Implement gRPC server for One Piece services

Create file: apps/grpc/server.py
"""

# FILE: apps/grpc/server.py
# YOUR CODE HERE - Import gRPC modules:
import grpc
from concurrent import futures
import time
import logging
# Add generated protobuf imports...

# YOUR CODE HERE - Implement character service:
class CharacterServiceServicer:
    """gRPC servicer for character operations"""
    
    def GetCharacter(self, request, context):
        """Get single character by ID"""
        try:
            # Add character retrieval logic
            pass
        except Exception as e:
            context.set_code(grpc.StatusCode.INTERNAL)
            context.set_details(str(e))
            return # Return empty response
    
    def ListCharacters(self, request, context):
        """List characters with pagination and filtering"""
        try:
            # Add character listing logic
            pass
        except Exception as e:
            context.set_code(grpc.StatusCode.INTERNAL)
            context.set_details(str(e))
            return # Return empty response
    
    def UpdateCharacterPrice(self, request, context):
        """Update character price"""
        try:
            # Add price update logic
            pass
        except Exception as e:
            context.set_code(grpc.StatusCode.INTERNAL)
            context.set_details(str(e))
            return # Return empty response
    
    def StreamPriceUpdates(self, request, context):
        """Stream real-time price updates"""
        try:
            # Add price streaming logic
            while True:
                # Yield price updates
                yield # Price update message
                time.sleep(1)  # Update frequency
        except Exception as e:
            context.set_code(grpc.StatusCode.INTERNAL)
            context.set_details(str(e))

# YOUR CODE HERE - Implement trading service:
class TradingServiceServicer:
    """gRPC servicer for trading operations"""
    
    def ExecuteTrade(self, request, context):
        """Execute a trade"""
        try:
            # Add trade execution logic
            pass
        except Exception as e:
            context.set_code(grpc.StatusCode.INTERNAL)
            context.set_details(str(e))
            return # Return empty response
    
    def GetPortfolio(self, request, context):
        """Get user portfolio"""
        try:
            # Add portfolio retrieval logic
            pass
        except Exception as e:
            context.set_code(grpc.StatusCode.INTERNAL)
            context.set_details(str(e))
            return # Return empty response
    
    def StreamTrades(self, request, context):
        """Stream user trades"""
        try:
            # Add trade streaming logic
            pass
        except Exception as e:
            context.set_code(grpc.StatusCode.INTERNAL)
            context.set_details(str(e))

# YOUR CODE HERE - Create gRPC server:
def serve():
    """Start gRPC server"""
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    
    # Add servicers to server
    # Add character service
    # Add trading service
    
    # Configure server
    listen_addr = '[::]:50051'
    server.add_insecure_port(listen_addr)
    
    # Start server
    server.start()
    logging.info(f"🏴‍☠️ One Piece gRPC server started on {listen_addr}")
    
    try:
        while True:
            time.sleep(86400)  # Keep server running
    except KeyboardInterrupt:
        server.stop(0)

if __name__ == '__main__':
    logging.basicConfig(level=logging.INFO)
    serve()

# ═══════════════════════════════════════════════════════════
# 🧪 HANDS-ON LAB 4: WEBSOCKETS FOR REAL-TIME UPDATES
# ═══════════════════════════════════════════════════════════

"""
📚 WEBSOCKETS FOR ONE PIECE REAL-TIME TRADING:

🔥 WEBSOCKET ADVANTAGES:

1. REAL-TIME COMMUNICATION:
   - Bidirectional communication
   - Low latency (50ms typical)
   - Persistent connection
   - Event-driven updates

2. TRADING USE CASES:
   - Live price updates
   - Order book changes
   - Portfolio value updates
   - Trading notifications

3. SCALABILITY:
   - Connection pooling
   - Message broadcasting
   - Load balancing
   - Horizontal scaling

WEBSOCKET MESSAGE TYPES:
- price_update: Character price changes
- trade_executed: Trade confirmations
- portfolio_update: Portfolio value changes
- market_alert: Important market events

🎯 YOUR CODING MISSION:
Implement WebSockets for real-time One Piece trading!
"""

# TODO 7: CREATE WEBSOCKET CONSUMERS
# ═══════════════════════════════════════════════════════════
"""
🎯 YOUR TASK: Create WebSocket consumers for real-time updates

Create file: apps/websockets/consumers.py
"""

# FILE: apps/websockets/consumers.py
# YOUR CODE HERE - Import WebSocket modules:
import json
import asyncio
from channels.generic.websocket import AsyncWebsocketConsumer
from channels.db import database_sync_to_async
# Add more imports...

# YOUR CODE HERE - Create price update consumer:
class PriceUpdateConsumer(AsyncWebsocketConsumer):
    """WebSocket consumer for real-time price updates"""
    
    async def connect(self):
        """Handle WebSocket connection"""
        # Add connection logic
        self.room_group_name = 'price_updates'
        
        # Join room group
        await self.channel_layer.group_add(
            self.room_group_name,
            self.channel_name
        )
        
        await self.accept()
        
        # Send initial data
        await self.send_initial_prices()
    
    async def disconnect(self, close_code):
        """Handle WebSocket disconnection"""
        # Leave room group
        await self.channel_layer.group_discard(
            self.room_group_name,
            self.channel_name
        )
    
    async def receive(self, text_data):
        """Handle messages from WebSocket"""
        try:
            text_data_json = json.loads(text_data)
            message_type = text_data_json.get('type')
            
            if message_type == 'subscribe_character':
                # Add character subscription logic
                pass
            elif message_type == 'unsubscribe_character':
                # Add character unsubscription logic
                pass
            
        except json.JSONDecodeError:
            await self.send(text_data=json.dumps({
                'type': 'error',
                'message': 'Invalid JSON format'
            }))
    
    async def price_update(self, event):
        """Send price update to WebSocket"""
        await self.send(text_data=json.dumps({
            'type': 'price_update',
            'character_id': event['character_id'],
            'old_price': event['old_price'],
            'new_price': event['new_price'],
            'change_percent': event['change_percent'],
            'timestamp': event['timestamp']
        }))
    
    @database_sync_to_async
    def send_initial_prices(self):
        """Send initial price data"""
        # Add initial price data logic
        pass

# YOUR CODE HERE - Create trading consumer:
class TradingConsumer(AsyncWebsocketConsumer):
    """WebSocket consumer for trading updates"""
    
    async def connect(self):
        """Handle WebSocket connection"""
        # Add authentication check
        if not self.scope['user'].is_authenticated:
            await self.close()
            return
        
        self.user_id = str(self.scope['user'].id)
        self.room_group_name = f'trading_{self.user_id}'
        
        # Join personal trading room
        await self.channel_layer.group_add(
            self.room_group_name,
            self.channel_name
        )
        
        await self.accept()
        
        # Send initial portfolio data
        await self.send_portfolio_update()
    
    async def disconnect(self, close_code):
        """Handle WebSocket disconnection"""
        await self.channel_layer.group_discard(
            self.room_group_name,
            self.channel_name
        )
    
    async def receive(self, text_data):
        """Handle trading commands"""
        try:
            data = json.loads(text_data)
            command = data.get('command')
            
            if command == 'execute_trade':
                await self.execute_trade(data)
            elif command == 'get_portfolio':
                await self.send_portfolio_update()
            
        except json.JSONDecodeError:
            await self.send_error('Invalid JSON format')
    
    async def execute_trade(self, trade_data):
        """Execute trade via WebSocket"""
        try:
            # Add trade execution logic
            pass
        except Exception as e:
            await self.send_error(str(e))
    
    async def trade_executed(self, event):
        """Send trade execution confirmation"""
        await self.send(text_data=json.dumps({
            'type': 'trade_executed',
            'trade': event['trade'],
            'portfolio_update': event['portfolio_update']
        }))
    
    async def portfolio_update(self, event):
        """Send portfolio update"""
        await self.send(text_data=json.dumps({
            'type': 'portfolio_update',
            'portfolio': event['portfolio']
        }))
    
    async def send_error(self, message):
        """Send error message"""
        await self.send(text_data=json.dumps({
            'type': 'error',
            'message': message
        }))
    
    @database_sync_to_async
    def send_portfolio_update(self):
        """Send current portfolio data"""
        # Add portfolio data logic
        pass

# TODO 8: CREATE WEBSOCKET ROUTING
# ═══════════════════════════════════════════════════════════
"""
🎯 YOUR TASK: Create WebSocket URL routing

Create file: apps/websockets/routing.py
"""

# FILE: apps/websockets/routing.py
# YOUR CODE HERE - Create WebSocket routing:
from django.urls import re_path
from . import consumers

websocket_urlpatterns = [
    re_path(r'ws/prices/$', consumers.PriceUpdateConsumer.as_asgi()),
    re_path(r'ws/trading/$', consumers.TradingConsumer.as_asgi()),
]

# TODO 9: CREATE WEBSOCKET BROADCASTING SERVICE
# ═══════════════════════════════════════════════════════════
"""
🎯 YOUR TASK: Create service for broadcasting WebSocket messages

Create file: apps/websockets/broadcast.py
"""

# FILE: apps/websockets/broadcast.py
# YOUR CODE HERE - Create broadcasting service:
from channels.layers import get_channel_layer
from asgiref.sync import async_to_sync
import json

class WebSocketBroadcaster:
    """Service for broadcasting WebSocket messages"""
    
    def __init__(self):
        self.channel_layer = get_channel_layer()
    
    def broadcast_price_update(self, character_id, old_price, new_price):
        """Broadcast price update to all connected clients"""
        change_percent = ((new_price - old_price) / old_price) * 100
        
        message = {
            'type': 'price_update',
            'character_id': character_id,
            'old_price': old_price,
            'new_price': new_price,
            'change_percent': round(change_percent, 2),
            'timestamp': # Add timestamp
        }
        
        async_to_sync(self.channel_layer.group_send)(
            'price_updates',
            message
        )
    
    def broadcast_trade_executed(self, user_id, trade_data, portfolio_data):
        """Broadcast trade execution to specific user"""
        message = {
            'type': 'trade_executed',
            'trade': trade_data,
            'portfolio_update': portfolio_data
        }
        
        async_to_sync(self.channel_layer.group_send)(
            f'trading_{user_id}',
            message
        )
    
    def broadcast_market_alert(self, alert_data):
        """Broadcast market alert to all users"""
        message = {
            'type': 'market_alert',
            'alert': alert_data
        }
        
        async_to_sync(self.channel_layer.group_send)(
            'price_updates',
            message
        )

# Create global broadcaster instance
broadcaster = WebSocketBroadcaster()

# ═══════════════════════════════════════════════════════════
# ✅ COMPLETE CODE SOLUTION (SCROLL DOWN TO CHECK YOUR WORK)
# ═══════════════════════════════════════════════════════════
