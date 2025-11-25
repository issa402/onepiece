"""
🏆 FANZONE CONNECT - WEBSOCKET EVENT HANDLER
Combines Multiple Learning Modules:
- Module 11: APIs & Protocols (WebSocket, real-time communication)
- Module 22: TCP Networking (low-latency connections, connection management)
- Module 21: Message Queues (event broadcasting, pub/sub patterns)
- Module 44: Message Queues & Events (event-driven architecture)

World Cup 2026 Fan Platform - Real-time Event Broadcasting System
"""

import asyncio
import json
import logging
from datetime import datetime
from typing import Dict, List, Set, Optional, Any
from uuid import uuid4
import weakref

import redis.asyncio as redis
from fastapi import WebSocket, WebSocketDisconnect
from pydantic import BaseModel
import aiohttp

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# =====================================================
# MODULE 22: TCP NETWORKING - CONNECTION MANAGEMENT
# =====================================================

class ConnectionManager:
    """
    Advanced WebSocket connection manager with TCP optimization
    Handles thousands of concurrent World Cup fan connections
    """
    
    def __init__(self):
        # Active connections by user_id
        self.active_connections: Dict[str, WebSocket] = {}
        
        # Room-based connections for events
        self.event_rooms: Dict[str, Set[str]] = {}  # event_id -> set of user_ids
        self.city_rooms: Dict[str, Set[str]] = {}   # city -> set of user_ids
        self.country_rooms: Dict[str, Set[str]] = {} # country -> set of user_ids
        
        # Connection metadata
        self.connection_metadata: Dict[str, Dict[str, Any]] = {}
        
        # Weak references to prevent memory leaks
        self._cleanup_refs: weakref.WeakSet = weakref.WeakSet()
        
        logger.info("🔌 WebSocket Connection Manager initialized for World Cup 2026")
    
    async def connect(self, websocket: WebSocket, user_id: str, metadata: Dict[str, Any] = None):
        """Accept WebSocket connection with TCP optimization"""
        await websocket.accept()
        
        # Store connection
        self.active_connections[user_id] = websocket
        self.connection_metadata[user_id] = {
            "connected_at": datetime.utcnow().isoformat(),
            "last_ping": datetime.utcnow().isoformat(),
            "message_count": 0,
            **(metadata or {})
        }
        
        # Add to cleanup tracking
        self._cleanup_refs.add(websocket)
        
        logger.info(f"🎉 World Cup fan connected: {user_id}")
        
        # Send welcome message
        await self.send_personal_message({
            "type": "connection_established",
            "message": "Welcome to FANZONE CONNECT - World Cup 2026!",
            "user_id": user_id,
            "timestamp": datetime.utcnow().isoformat()
        }, user_id)
    
    def disconnect(self, user_id: str):
        """Disconnect user and cleanup resources"""
        if user_id in self.active_connections:
            # Remove from all rooms
            self._remove_from_all_rooms(user_id)
            
            # Remove connection
            del self.active_connections[user_id]
            del self.connection_metadata[user_id]
            
            logger.info(f"👋 World Cup fan disconnected: {user_id}")
    
    def _remove_from_all_rooms(self, user_id: str):
        """Remove user from all rooms"""
        # Remove from event rooms
        for event_id, users in self.event_rooms.items():
            users.discard(user_id)
        
        # Remove from city rooms
        for city, users in self.city_rooms.items():
            users.discard(user_id)
        
        # Remove from country rooms
        for country, users in self.country_rooms.items():
            users.discard(user_id)
    
    async def send_personal_message(self, message: Dict[str, Any], user_id: str):
        """Send message to specific user with error handling"""
        if user_id in self.active_connections:
            try:
                websocket = self.active_connections[user_id]
                await websocket.send_text(json.dumps(message))
                
                # Update metadata
                if user_id in self.connection_metadata:
                    self.connection_metadata[user_id]["message_count"] += 1
                    self.connection_metadata[user_id]["last_message"] = datetime.utcnow().isoformat()
                
            except Exception as e:
                logger.error(f"❌ Failed to send message to {user_id}: {e}")
                self.disconnect(user_id)
    
    async def broadcast_to_room(self, message: Dict[str, Any], room_type: str, room_id: str):
        """Broadcast message to all users in a room"""
        room_map = {
            "event": self.event_rooms,
            "city": self.city_rooms,
            "country": self.country_rooms
        }
        
        if room_type not in room_map:
            logger.error(f"❌ Invalid room type: {room_type}")
            return
        
        room = room_map[room_type].get(room_id, set())
        
        if not room:
            logger.warning(f"⚠️ No users in {room_type} room: {room_id}")
            return
        
        # Broadcast to all users in room
        disconnected_users = []
        for user_id in room.copy():  # Copy to avoid modification during iteration
            try:
                await self.send_personal_message(message, user_id)
            except Exception as e:
                logger.error(f"❌ Failed to broadcast to {user_id}: {e}")
                disconnected_users.append(user_id)
        
        # Clean up disconnected users
        for user_id in disconnected_users:
            self.disconnect(user_id)
        
        logger.info(f"📢 Broadcasted to {len(room) - len(disconnected_users)} users in {room_type}:{room_id}")
    
    def join_room(self, user_id: str, room_type: str, room_id: str):
        """Add user to a room"""
        room_map = {
            "event": self.event_rooms,
            "city": self.city_rooms,
            "country": self.country_rooms
        }
        
        if room_type not in room_map:
            logger.error(f"❌ Invalid room type: {room_type}")
            return
        
        if room_id not in room_map[room_type]:
            room_map[room_type][room_id] = set()
        
        room_map[room_type][room_id].add(user_id)
        logger.info(f"🏠 User {user_id} joined {room_type} room: {room_id}")
    
    def leave_room(self, user_id: str, room_type: str, room_id: str):
        """Remove user from a room"""
        room_map = {
            "event": self.event_rooms,
            "city": self.city_rooms,
            "country": self.country_rooms
        }
        
        if room_type in room_map and room_id in room_map[room_type]:
            room_map[room_type][room_id].discard(user_id)
            logger.info(f"🚪 User {user_id} left {room_type} room: {room_id}")
    
    def get_connection_stats(self) -> Dict[str, Any]:
        """Get connection statistics"""
        return {
            "total_connections": len(self.active_connections),
            "event_rooms": {room_id: len(users) for room_id, users in self.event_rooms.items()},
            "city_rooms": {city: len(users) for city, users in self.city_rooms.items()},
            "country_rooms": {country: len(users) for country, users in self.country_rooms.items()},
            "timestamp": datetime.utcnow().isoformat()
        }

# =====================================================
# MODULE 21 & 44: MESSAGE QUEUES & EVENT-DRIVEN ARCHITECTURE
# =====================================================

class EventMessage(BaseModel):
    """Event message schema for World Cup events"""
    event_id: str
    event_type: str  # match_start, goal_scored, match_end, fan_event, etc.
    data: Dict[str, Any]
    timestamp: str
    source: str = "fanzone-connect"

class RedisEventBroker:
    """
    Redis-based event broker for real-time World Cup events
    Implements pub/sub pattern for scalable event distribution
    """
    
    def __init__(self, redis_url: str = "redis://redis:6379"):
        self.redis_url = redis_url
        self.redis_client: Optional[redis.Redis] = None
        self.pubsub: Optional[redis.client.PubSub] = None
        self.subscribers: Dict[str, List[callable]] = {}
        
    async def connect(self):
        """Connect to Redis"""
        self.redis_client = redis.from_url(self.redis_url, decode_responses=True)
        self.pubsub = self.redis_client.pubsub()
        logger.info("📡 Connected to Redis event broker")
    
    async def disconnect(self):
        """Disconnect from Redis"""
        if self.pubsub:
            await self.pubsub.close()
        if self.redis_client:
            await self.redis_client.close()
        logger.info("📡 Disconnected from Redis event broker")
    
    async def publish_event(self, channel: str, event: EventMessage):
        """Publish event to Redis channel"""
        if not self.redis_client:
            await self.connect()
        
        await self.redis_client.publish(channel, event.json())
        logger.info(f"📤 Published event to {channel}: {event.event_type}")
    
    async def subscribe_to_channel(self, channel: str, callback: callable):
        """Subscribe to Redis channel"""
        if not self.pubsub:
            await self.connect()
        
        await self.pubsub.subscribe(channel)
        
        if channel not in self.subscribers:
            self.subscribers[channel] = []
        self.subscribers[channel].append(callback)
        
        logger.info(f"📥 Subscribed to channel: {channel}")
    
    async def listen_for_events(self):
        """Listen for events and dispatch to callbacks"""
        if not self.pubsub:
            return
        
        async for message in self.pubsub.listen():
            if message['type'] == 'message':
                channel = message['channel']
                data = json.loads(message['data'])
                
                # Dispatch to all subscribers
                if channel in self.subscribers:
                    for callback in self.subscribers[channel]:
                        try:
                            await callback(channel, data)
                        except Exception as e:
                            logger.error(f"❌ Error in event callback: {e}")

# Global instances
connection_manager = ConnectionManager()
event_broker = RedisEventBroker()

# =====================================================
# WEBSOCKET EVENT HANDLERS
# =====================================================

async def handle_websocket_connection(websocket: WebSocket, user_id: str):
    """Handle WebSocket connection for World Cup fan"""
    try:
        # Connect user
        await connection_manager.connect(websocket, user_id)
        
        # Subscribe to user-specific events
        await event_broker.subscribe_to_channel(
            f"user:{user_id}",
            lambda channel, data: connection_manager.send_personal_message(data, user_id)
        )
        
        # Main message loop
        while True:
            try:
                # Receive message from client
                data = await websocket.receive_text()
                message = json.loads(data)
                
                # Handle different message types
                await handle_client_message(user_id, message)
                
            except WebSocketDisconnect:
                logger.info(f"🔌 WebSocket disconnected: {user_id}")
                break
            except json.JSONDecodeError:
                logger.error(f"❌ Invalid JSON from {user_id}")
                await connection_manager.send_personal_message({
                    "type": "error",
                    "message": "Invalid JSON format"
                }, user_id)
            except Exception as e:
                logger.error(f"❌ Error handling message from {user_id}: {e}")
                break
    
    finally:
        connection_manager.disconnect(user_id)

async def handle_client_message(user_id: str, message: Dict[str, Any]):
    """Handle incoming client messages"""
    message_type = message.get("type")
    
    if message_type == "join_event":
        event_id = message.get("event_id")
        if event_id:
            connection_manager.join_room(user_id, "event", event_id)
    
    elif message_type == "leave_event":
        event_id = message.get("event_id")
        if event_id:
            connection_manager.leave_room(user_id, "event", event_id)
    
    elif message_type == "join_city":
        city = message.get("city")
        if city:
            connection_manager.join_room(user_id, "city", city)
    
    elif message_type == "ping":
        await connection_manager.send_personal_message({
            "type": "pong",
            "timestamp": datetime.utcnow().isoformat()
        }, user_id)
    
    else:
        logger.warning(f"⚠️ Unknown message type from {user_id}: {message_type}")

# Example usage for World Cup events
async def broadcast_match_event(match_id: str, event_type: str, data: Dict[str, Any]):
    """Broadcast World Cup match events to all fans"""
    event = EventMessage(
        event_id=str(uuid4()),
        event_type=event_type,
        data={
            "match_id": match_id,
            **data
        },
        timestamp=datetime.utcnow().isoformat()
    )
    
    # Publish to Redis
    await event_broker.publish_event(f"match:{match_id}", event)
    
    # Broadcast to WebSocket connections
    await connection_manager.broadcast_to_room(
        event.dict(),
        "event",
        match_id
    )
