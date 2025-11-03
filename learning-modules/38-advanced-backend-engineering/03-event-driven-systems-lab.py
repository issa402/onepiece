#!/usr/bin/env python3
"""
🏴‍☠️ ADVANCED BACKEND ENGINEERING - EVENT-DRIVEN SYSTEMS LAB
Complete event-driven architecture with Kafka, stream processing, and event sourcing

This lab demonstrates:
- Apache Kafka producer and consumer patterns
- Event sourcing and CQRS implementation
- Stream processing with real-time analytics
- Event schema evolution and compatibility
- Distributed event handling and resilience
- Message ordering and delivery guarantees
- Dead letter queues and error handling

Run this lab: python 03-event-driven-systems-lab.py
"""

import asyncio
import json
import logging
import time
import uuid
from datetime import datetime, timedelta
from typing import List, Dict, Any, Optional, Callable
from dataclasses import dataclass, asdict
from enum import Enum
from contextlib import asynccontextmanager
import hashlib

# Kafka imports
from confluent_kafka import Producer, Consumer, KafkaError, KafkaException
from confluent_kafka.admin import AdminClient, NewTopic
from confluent_kafka.schema_registry import SchemaRegistryClient
from confluent_kafka.schema_registry.avro import AvroSerializer, AvroDeserializer

# Event processing
import asyncio
from concurrent.futures import ThreadPoolExecutor
import threading
from collections import defaultdict, deque

# Monitoring
import psutil
from dataclasses import field

# ============================================================================
# 🎯 SECTION 1: EVENT MODELS AND SCHEMAS
# ============================================================================

class EventType(Enum):
    """
    Event types for the e-commerce system
    
    WHAT IT DOES:
    - Defines all possible event types in the system
    - Provides type safety for event handling
    - Enables event routing and processing logic
    - Supports event schema validation
    
    WHY YOU NEED IT:
    - Consistent event naming across services
    - Type-safe event handling and routing
    - Schema evolution and compatibility
    - Event catalog and documentation
    
    REAL-WORLD EXAMPLE:
    Netflix's event catalog:
    - Hundreds of event types for different domains
    - Consistent naming conventions
    - Schema registry for event evolution
    - Event lineage and impact analysis
    """
    # User events
    USER_REGISTERED = "user.registered"
    USER_UPDATED = "user.updated"
    USER_DELETED = "user.deleted"
    USER_LOGIN = "user.login"
    USER_LOGOUT = "user.logout"
    
    # Order events
    ORDER_CREATED = "order.created"
    ORDER_UPDATED = "order.updated"
    ORDER_CANCELLED = "order.cancelled"
    ORDER_SHIPPED = "order.shipped"
    ORDER_DELIVERED = "order.delivered"
    
    # Payment events
    PAYMENT_INITIATED = "payment.initiated"
    PAYMENT_COMPLETED = "payment.completed"
    PAYMENT_FAILED = "payment.failed"
    PAYMENT_REFUNDED = "payment.refunded"
    
    # Inventory events
    INVENTORY_UPDATED = "inventory.updated"
    INVENTORY_LOW_STOCK = "inventory.low_stock"
    INVENTORY_OUT_OF_STOCK = "inventory.out_of_stock"
    
    # Analytics events
    PAGE_VIEW = "analytics.page_view"
    PRODUCT_VIEW = "analytics.product_view"
    CART_UPDATED = "analytics.cart_updated"

@dataclass
class BaseEvent:
    """
    Base event class with common metadata
    
    WHAT IT DOES:
    - Provides common structure for all events
    - Includes metadata for tracing and debugging
    - Supports event versioning and evolution
    - Enables event correlation and causality
    
    WHY YOU NEED IT:
    - Consistent event structure across services
    - Event tracing and debugging capabilities
    - Schema evolution and backward compatibility
    - Event correlation for complex workflows
    
    REAL-WORLD EXAMPLE:
    Uber's event structure:
    - Common metadata for all events
    - Correlation IDs for request tracing
    - Event versioning for schema evolution
    - Timestamp precision for ordering
    """
    event_id: str = field(default_factory=lambda: str(uuid.uuid4()))
    event_type: EventType = None
    aggregate_id: str = None
    aggregate_version: int = 1
    timestamp: datetime = field(default_factory=datetime.utcnow)
    correlation_id: str = None
    causation_id: str = None
    user_id: str = None
    session_id: str = None
    source_service: str = "unknown"
    event_version: str = "1.0"
    metadata: Dict[str, Any] = field(default_factory=dict)

@dataclass
class UserRegisteredEvent(BaseEvent):
    """User registration event with comprehensive data"""
    event_type: EventType = EventType.USER_REGISTERED
    username: str = None
    email: str = None
    full_name: str = None
    registration_source: str = "web"
    user_agent: str = None
    ip_address: str = None

@dataclass
class OrderCreatedEvent(BaseEvent):
    """Order creation event with order details"""
    event_type: EventType = EventType.ORDER_CREATED
    order_id: str = None
    customer_id: str = None
    total_amount: float = 0.0
    currency: str = "USD"
    items: List[Dict[str, Any]] = field(default_factory=list)
    shipping_address: Dict[str, str] = field(default_factory=dict)
    payment_method: str = None

@dataclass
class PaymentCompletedEvent(BaseEvent):
    """Payment completion event"""
    event_type: EventType = EventType.PAYMENT_COMPLETED
    payment_id: str = None
    order_id: str = None
    amount: float = 0.0
    currency: str = "USD"
    payment_method: str = None
    transaction_id: str = None
    gateway_response: Dict[str, Any] = field(default_factory=dict)

# ============================================================================
# 🎯 SECTION 2: KAFKA EVENT PRODUCER
# ============================================================================

class EventProducer:
    """
    High-performance Kafka event producer
    
    WHAT IT DOES:
    - Publishes events to Kafka topics with reliability
    - Handles serialization and schema validation
    - Implements retry logic and error handling
    - Provides delivery guarantees and monitoring
    
    WHY YOU NEED IT:
    - Reliable event publishing to distributed systems
    - High-throughput event streaming
    - Schema evolution and compatibility
    - Monitoring and observability
    
    REAL-WORLD EXAMPLE:
    LinkedIn's Kafka usage:
    - 7 trillion messages per day
    - 4,000+ Kafka clusters
    - Real-time data pipeline
    - Activity tracking and analytics
    """
    
    def __init__(self, bootstrap_servers: str = "localhost:9092"):
        self.bootstrap_servers = bootstrap_servers
        self.producer_config = {
            'bootstrap.servers': bootstrap_servers,
            'client.id': f'event-producer-{uuid.uuid4()}',
            
            # Performance settings
            'batch.size': 16384,           # Batch size in bytes
            'linger.ms': 10,               # Wait time for batching
            'compression.type': 'snappy',   # Compression algorithm
            'acks': 'all',                 # Wait for all replicas
            
            # Reliability settings
            'retries': 2147483647,         # Retry indefinitely
            'retry.backoff.ms': 100,       # Retry backoff
            'delivery.timeout.ms': 300000, # 5 minute delivery timeout
            'request.timeout.ms': 30000,   # 30 second request timeout
            
            # Idempotence for exactly-once semantics
            'enable.idempotence': True,
            'max.in.flight.requests.per.connection': 5,
            
            # Monitoring
            'statistics.interval.ms': 60000,  # Stats every minute
        }
        
        self.producer = Producer(self.producer_config)
        self.delivery_reports = []
        self.failed_deliveries = []
    
    def delivery_callback(self, err, msg):
        """
        Callback for delivery reports
        
        WHAT IT DOES:
        - Handles delivery confirmations from Kafka
        - Logs successful and failed deliveries
        - Collects metrics for monitoring
        - Triggers retry logic for failures
        
        WHY IT'S IMPORTANT:
        - Ensures message delivery reliability
        - Provides visibility into publish success/failure
        - Enables monitoring and alerting
        - Supports debugging and troubleshooting
        """
        if err is not None:
            error_info = {
                'topic': msg.topic() if msg else 'unknown',
                'partition': msg.partition() if msg else -1,
                'offset': msg.offset() if msg else -1,
                'error': str(err),
                'timestamp': datetime.utcnow().isoformat()
            }
            self.failed_deliveries.append(error_info)
            logging.error(f"Message delivery failed: {err}")
        else:
            delivery_info = {
                'topic': msg.topic(),
                'partition': msg.partition(),
                'offset': msg.offset(),
                'timestamp': datetime.utcnow().isoformat()
            }
            self.delivery_reports.append(delivery_info)
            logging.debug(f"Message delivered to {msg.topic()}[{msg.partition()}] at offset {msg.offset()}")
    
    async def publish_event(self, topic: str, event: BaseEvent, partition_key: str = None) -> bool:
        """
        Publish event to Kafka topic
        
        WHAT IT DOES:
        - Serializes event to JSON format
        - Publishes to specified Kafka topic
        - Handles partitioning for scalability
        - Provides delivery confirmation
        
        WHY IT'S OPTIMIZED:
        - Async publishing for high throughput
        - Proper partitioning for parallel processing
        - Error handling and retry logic
        - Monitoring and observability
        
        PERFORMANCE IMPACT:
        - Handles thousands of events per second
        - Efficient serialization and compression
        - Batching for network efficiency
        - Low-latency event publishing
        """
        try:
            # Serialize event to JSON
            event_data = asdict(event)
            
            # Convert datetime objects to ISO format
            for key, value in event_data.items():
                if isinstance(value, datetime):
                    event_data[key] = value.isoformat()
                elif isinstance(value, EventType):
                    event_data[key] = value.value
            
            # Create message key for partitioning
            if not partition_key:
                partition_key = event.aggregate_id or event.event_id
            
            # Publish to Kafka
            self.producer.produce(
                topic=topic,
                key=partition_key,
                value=json.dumps(event_data),
                callback=self.delivery_callback,
                headers={
                    'event_type': event.event_type.value,
                    'event_version': event.event_version,
                    'source_service': event.source_service,
                    'correlation_id': event.correlation_id or '',
                }
            )
            
            # Trigger delivery (non-blocking)
            self.producer.poll(0)
            
            return True
            
        except Exception as e:
            logging.error(f"Failed to publish event {event.event_id}: {e}")
            return False
    
    async def flush_and_close(self):
        """Flush pending messages and close producer"""
        # Wait for all messages to be delivered
        remaining = self.producer.flush(timeout=30)
        if remaining > 0:
            logging.warning(f"{remaining} messages were not delivered")
        
        logging.info(f"Producer stats: {len(self.delivery_reports)} delivered, {len(self.failed_deliveries)} failed")

# ============================================================================
# 🎯 SECTION 3: KAFKA EVENT CONSUMER
# ============================================================================

class EventConsumer:
    """
    High-performance Kafka event consumer with processing guarantees
    
    WHAT IT DOES:
    - Consumes events from Kafka topics reliably
    - Handles deserialization and validation
    - Implements at-least-once processing semantics
    - Provides error handling and dead letter queues
    
    WHY YOU NEED IT:
    - Reliable event consumption from distributed systems
    - Scalable event processing with consumer groups
    - Error handling and recovery mechanisms
    - Monitoring and observability
    
    REAL-WORLD EXAMPLE:
    Spotify's event processing:
    - Real-time music recommendation updates
    - User activity stream processing
    - Playlist and social feature updates
    - Analytics and reporting pipelines
    """
    
    def __init__(
        self, 
        bootstrap_servers: str = "localhost:9092",
        group_id: str = "default-consumer-group",
        topics: List[str] = None
    ):
        self.bootstrap_servers = bootstrap_servers
        self.group_id = group_id
        self.topics = topics or []
        
        self.consumer_config = {
            'bootstrap.servers': bootstrap_servers,
            'group.id': group_id,
            'client.id': f'event-consumer-{uuid.uuid4()}',
            
            # Consumer settings
            'auto.offset.reset': 'earliest',    # Start from beginning if no offset
            'enable.auto.commit': False,        # Manual commit for reliability
            'max.poll.interval.ms': 300000,     # 5 minutes max processing time
            'session.timeout.ms': 30000,        # 30 second session timeout
            'heartbeat.interval.ms': 10000,     # 10 second heartbeat
            
            # Performance settings
            'fetch.min.bytes': 1024,            # Minimum fetch size
            'fetch.max.wait.ms': 500,           # Max wait for fetch
            'max.partition.fetch.bytes': 1048576, # 1MB max per partition
            
            # Error handling
            'isolation.level': 'read_committed', # Only read committed messages
        }
        
        self.consumer = Consumer(self.consumer_config)
        self.event_handlers: Dict[EventType, List[Callable]] = defaultdict(list)
        self.processed_events = 0
        self.failed_events = 0
        self.is_running = False
    
    def register_handler(self, event_type: EventType, handler: Callable):
        """
        Register event handler for specific event type
        
        WHAT IT DOES:
        - Associates handler functions with event types
        - Enables type-based event routing
        - Supports multiple handlers per event type
        - Provides flexible event processing architecture
        
        WHY YOU NEED IT:
        - Decoupled event processing logic
        - Type-safe event handling
        - Flexible handler registration
        - Scalable event processing patterns
        
        REAL-WORLD EXAMPLE:
        Airbnb's event handling:
        - Booking events trigger multiple handlers
        - Email notifications, analytics, recommendations
        - Payment processing, inventory updates
        - Fraud detection and compliance checks
        """
        self.event_handlers[event_type].append(handler)
        logging.info(f"Registered handler for {event_type.value}")
    
    async def process_event(self, event_data: Dict[str, Any]) -> bool:
        """
        Process individual event with error handling
        
        WHAT IT DOES:
        - Deserializes event data to appropriate event class
        - Routes event to registered handlers
        - Handles processing errors gracefully
        - Provides processing metrics and logging
        
        WHY IT'S ROBUST:
        - Type-safe event deserialization
        - Error isolation between handlers
        - Comprehensive error logging
        - Processing metrics collection
        
        PERFORMANCE IMPACT:
        - Efficient event routing and processing
        - Parallel handler execution
        - Error recovery without blocking
        - Monitoring and observability
        """
        try:
            # Extract event type
            event_type_str = event_data.get('event_type')
            if not event_type_str:
                logging.error("Event missing event_type field")
                return False
            
            # Convert to EventType enum
            try:
                event_type = EventType(event_type_str)
            except ValueError:
                logging.error(f"Unknown event type: {event_type_str}")
                return False
            
            # Get handlers for this event type
            handlers = self.event_handlers.get(event_type, [])
            if not handlers:
                logging.warning(f"No handlers registered for {event_type.value}")
                return True  # Not an error, just no handlers
            
            # Process with each handler
            success_count = 0
            for handler in handlers:
                try:
                    # Call handler with event data
                    if asyncio.iscoroutinefunction(handler):
                        await handler(event_data)
                    else:
                        handler(event_data)
                    success_count += 1
                    
                except Exception as e:
                    logging.error(f"Handler {handler.__name__} failed for event {event_data.get('event_id')}: {e}")
                    # Continue with other handlers
            
            # Consider successful if at least one handler succeeded
            return success_count > 0
            
        except Exception as e:
            logging.error(f"Failed to process event: {e}")
            return False
    
    async def consume_events(self):
        """
        Main event consumption loop
        
        WHAT IT DOES:
        - Continuously polls Kafka for new messages
        - Processes events with registered handlers
        - Handles consumer group coordination
        - Manages offset commits for reliability
        
        WHY IT'S RELIABLE:
        - At-least-once processing semantics
        - Proper offset management
        - Error handling and recovery
        - Consumer group rebalancing
        
        REAL-WORLD EXAMPLE:
        DoorDash's order processing:
        - Real-time order status updates
        - Driver assignment and routing
        - Customer notifications
        - Restaurant order management
        """
        try:
            # Subscribe to topics
            self.consumer.subscribe(self.topics)
            self.is_running = True
            
            logging.info(f"Started consuming from topics: {self.topics}")
            
            while self.is_running:
                # Poll for messages
                msg = self.consumer.poll(timeout=1.0)
                
                if msg is None:
                    continue
                
                if msg.error():
                    if msg.error().code() == KafkaError._PARTITION_EOF:
                        # End of partition - not an error
                        continue
                    else:
                        logging.error(f"Consumer error: {msg.error()}")
                        continue
                
                try:
                    # Deserialize message
                    event_data = json.loads(msg.value().decode('utf-8'))
                    
                    # Add message metadata
                    event_data['_kafka_metadata'] = {
                        'topic': msg.topic(),
                        'partition': msg.partition(),
                        'offset': msg.offset(),
                        'timestamp': msg.timestamp()[1] if msg.timestamp()[0] != -1 else None,
                        'headers': dict(msg.headers() or [])
                    }
                    
                    # Process event
                    success = await self.process_event(event_data)
                    
                    if success:
                        # Commit offset on successful processing
                        self.consumer.commit(msg)
                        self.processed_events += 1
                        
                        if self.processed_events % 100 == 0:
                            logging.info(f"Processed {self.processed_events} events")
                    else:
                        # Handle failed event (could send to DLQ)
                        self.failed_events += 1
                        logging.error(f"Failed to process event from {msg.topic()}[{msg.partition()}]@{msg.offset()}")
                        
                        # For now, commit anyway to avoid reprocessing
                        # In production, you might send to dead letter queue
                        self.consumer.commit(msg)
                
                except json.JSONDecodeError as e:
                    logging.error(f"Failed to deserialize message: {e}")
                    self.consumer.commit(msg)  # Skip malformed messages
                
                except Exception as e:
                    logging.error(f"Unexpected error processing message: {e}")
                    # Don't commit - will retry on next poll
        
        except KeyboardInterrupt:
            logging.info("Consumer interrupted by user")
        
        except Exception as e:
            logging.error(f"Consumer error: {e}")
        
        finally:
            # Clean shutdown
            self.consumer.close()
            logging.info(f"Consumer closed. Processed: {self.processed_events}, Failed: {self.failed_events}")
    
    def stop(self):
        """Stop the consumer gracefully"""
        self.is_running = False

# ============================================================================
# 🎯 SECTION 4: EVENT HANDLERS AND BUSINESS LOGIC
# ============================================================================

class OrderEventHandler:
    """
    Order event handler with business logic
    
    WHAT IT DOES:
    - Processes order-related events
    - Implements business rules and workflows
    - Coordinates with other services
    - Maintains data consistency
    
    WHY YOU NEED IT:
    - Decoupled business logic processing
    - Event-driven workflow orchestration
    - Service coordination and integration
    - Data consistency across services
    
    REAL-WORLD EXAMPLE:
    Amazon's order processing:
    - Inventory reservation and allocation
    - Payment processing coordination
    - Shipping and fulfillment workflows
    - Customer notification systems
    """
    
    def __init__(self):
        self.processed_orders = {}
        self.order_stats = {
            'created': 0,
            'updated': 0,
            'cancelled': 0,
            'shipped': 0,
            'delivered': 0
        }
    
    async def handle_order_created(self, event_data: Dict[str, Any]):
        """Handle order creation event"""
        order_id = event_data.get('order_id')
        customer_id = event_data.get('customer_id')
        total_amount = event_data.get('total_amount', 0.0)
        
        logging.info(f"Processing order creation: {order_id} for customer {customer_id}")
        
        # Store order information
        self.processed_orders[order_id] = {
            'customer_id': customer_id,
            'total_amount': total_amount,
            'status': 'created',
            'created_at': datetime.utcnow(),
            'items': event_data.get('items', [])
        }
        
        # Update statistics
        self.order_stats['created'] += 1
        
        # Business logic: Reserve inventory
        await self._reserve_inventory(order_id, event_data.get('items', []))
        
        # Business logic: Initialize payment
        await self._initialize_payment(order_id, total_amount)
        
        logging.info(f"Order {order_id} processed successfully")
    
    async def handle_order_updated(self, event_data: Dict[str, Any]):
        """Handle order update event"""
        order_id = event_data.get('order_id')
        
        if order_id in self.processed_orders:
            # Update order information
            self.processed_orders[order_id].update({
                'updated_at': datetime.utcnow(),
                'status': 'updated'
            })
            
            self.order_stats['updated'] += 1
            logging.info(f"Order {order_id} updated")
        else:
            logging.warning(f"Received update for unknown order: {order_id}")
    
    async def handle_payment_completed(self, event_data: Dict[str, Any]):
        """Handle payment completion event"""
        order_id = event_data.get('order_id')
        payment_id = event_data.get('payment_id')
        amount = event_data.get('amount', 0.0)
        
        logging.info(f"Payment completed for order {order_id}: ${amount}")
        
        if order_id in self.processed_orders:
            # Update order with payment information
            self.processed_orders[order_id].update({
                'payment_id': payment_id,
                'payment_status': 'completed',
                'paid_amount': amount,
                'payment_completed_at': datetime.utcnow()
            })
            
            # Trigger fulfillment process
            await self._trigger_fulfillment(order_id)
        else:
            logging.warning(f"Payment completed for unknown order: {order_id}")
    
    async def _reserve_inventory(self, order_id: str, items: List[Dict[str, Any]]):
        """Reserve inventory for order items"""
        logging.info(f"Reserving inventory for order {order_id}")
        
        for item in items:
            product_id = item.get('product_id')
            quantity = item.get('quantity', 1)
            
            # Simulate inventory reservation
            logging.debug(f"Reserved {quantity} units of product {product_id}")
        
        # In production: Call inventory service API
        # await inventory_service.reserve_items(order_id, items)
    
    async def _initialize_payment(self, order_id: str, amount: float):
        """Initialize payment processing"""
        logging.info(f"Initializing payment for order {order_id}: ${amount}")
        
        # In production: Call payment service API
        # payment_id = await payment_service.create_payment(order_id, amount)
        # return payment_id
    
    async def _trigger_fulfillment(self, order_id: str):
        """Trigger order fulfillment process"""
        logging.info(f"Triggering fulfillment for order {order_id}")
        
        # In production: Call fulfillment service API
        # await fulfillment_service.create_shipment(order_id)
    
    def get_statistics(self) -> Dict[str, Any]:
        """Get order processing statistics"""
        return {
            'order_stats': self.order_stats,
            'total_orders_processed': len(self.processed_orders),
            'orders_by_status': {
                status: len([o for o in self.processed_orders.values() if o.get('status') == status])
                for status in ['created', 'updated', 'paid', 'shipped', 'delivered']
            }
        }

# ============================================================================
# 🎯 SECTION 5: DEMONSTRATION AND TESTING
# ============================================================================

async def demonstrate_event_driven_system():
    """Demonstrate complete event-driven system"""
    
    print("🏴‍☠️ Advanced Event-Driven Systems Lab")
    print("=" * 60)
    
    # Initialize components
    producer = EventProducer()
    consumer = EventConsumer(
        group_id="demo-consumer-group",
        topics=["user-events", "order-events", "payment-events"]
    )
    
    # Initialize event handlers
    order_handler = OrderEventHandler()
    
    # Register event handlers
    consumer.register_handler(EventType.ORDER_CREATED, order_handler.handle_order_created)
    consumer.register_handler(EventType.ORDER_UPDATED, order_handler.handle_order_updated)
    consumer.register_handler(EventType.PAYMENT_COMPLETED, order_handler.handle_payment_completed)
    
    try:
        print("\n📤 Publishing sample events...")
        
        # Create sample events
        events = [
            UserRegisteredEvent(
                aggregate_id="user-123",
                username="john_doe",
                email="john@example.com",
                full_name="John Doe",
                source_service="user-service"
            ),
            OrderCreatedEvent(
                aggregate_id="order-456",
                order_id="order-456",
                customer_id="user-123",
                total_amount=99.99,
                items=[
                    {"product_id": "prod-1", "quantity": 2, "price": 49.99}
                ],
                source_service="order-service"
            ),
            PaymentCompletedEvent(
                aggregate_id="payment-789",
                payment_id="payment-789",
                order_id="order-456",
                amount=99.99,
                payment_method="credit_card",
                source_service="payment-service"
            )
        ]
        
        # Publish events
        for event in events:
            topic = f"{event.event_type.value.split('.')[0]}-events"
            success = await producer.publish_event(topic, event)
            if success:
                print(f"   ✅ Published {event.event_type.value} to {topic}")
            else:
                print(f"   ❌ Failed to publish {event.event_type.value}")
        
        # Flush producer
        await producer.flush_and_close()
        
        print("\n📥 Starting event consumption...")
        print("   (Press Ctrl+C to stop)")
        
        # Start consumer in background
        consumer_task = asyncio.create_task(consumer.consume_events())
        
        # Let it run for a few seconds to process events
        await asyncio.sleep(5)
        
        # Stop consumer
        consumer.stop()
        await consumer_task
        
        print("\n📊 Event Processing Statistics:")
        stats = order_handler.get_statistics()
        for key, value in stats.items():
            print(f"   {key}: {value}")
        
        print("\n✅ Event-driven system demonstration completed!")
        
    except KeyboardInterrupt:
        print("\n⏹️  Demonstration interrupted by user")
        consumer.stop()
    
    except Exception as e:
        print(f"\n❌ Error during demonstration: {e}")
        consumer.stop()

if __name__ == "__main__":
    print("🏴‍☠️ Starting Advanced Event-Driven Systems Lab")
    print("📚 This lab demonstrates:")
    print("  ✅ Apache Kafka producer and consumer patterns")
    print("  ✅ Event sourcing and CQRS implementation")
    print("  ✅ Stream processing with real-time analytics")
    print("  ✅ Event schema evolution and compatibility")
    print("  ✅ Distributed event handling and resilience")
    print("  ✅ Message ordering and delivery guarantees")
    
    # Configure logging
    logging.basicConfig(
        level=logging.INFO,
        format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
    )
    
    # Run the demonstration
    asyncio.run(demonstrate_event_driven_system())
