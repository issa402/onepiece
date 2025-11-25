/*
🏴‍☠️ MESSAGE BROKERS MASTERY - COMPLETE EVENT-DRIVEN ARCHITECTURE ENGINEERING
═══════════════════════════════════════════════════════════════════════════════

🎯 WHAT YOU'LL MASTER IN THIS LAB (ROADMAP.SH ALIGNED):
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

📚 PART 1: MESSAGE BROKERS FUNDAMENTALS (What & Why)
   - What message brokers are and why they power Netflix, Uber, LinkedIn
   - Why event-driven architecture enables microservices at scale
   - How asynchronous messaging improves system resilience
   - What pub/sub patterns enable for real-time applications
   - Why message queues are critical for high-throughput systems

⚡ PART 2: RABBITMQ MASTERY (Reliable Messaging)
   - RabbitMQ for guaranteed message delivery and durability
   - Exchange types (direct, topic, fanout) for routing patterns
   - Work queues for load distribution and scaling
   - Dead letter queues for error handling and recovery
   - Clustering and high availability configurations

🗄️ PART 3: APACHE KAFKA (High-Throughput Streaming)
   - Kafka for high-throughput event streaming (millions of messages/sec)
   - Topics and partitions for horizontal scaling
   - Consumer groups for parallel processing
   - Event sourcing and replay capabilities
   - Stream processing with Kafka Streams

🔒 PART 4: REDIS STREAMS (Lightweight Messaging)
   - Redis Streams for lightweight message streaming
   - Consumer groups and message acknowledgment
   - Time-series data processing patterns
   - Hybrid caching and messaging solutions
   - Performance optimization for real-time data

🚀 PART 5: ADVANCED PATTERNS (Senior Engineer Level)
   - Event-driven architecture design patterns
   - Saga patterns for distributed transactions
   - CQRS (Command Query Responsibility Segregation)
   - Message versioning and schema evolution
   - Monitoring and observability for message systems

💰 SALARY IMPACT: $100K → $350K+ (Message broker expertise enables massive scale)
🏢 COMPANIES: Netflix, Uber, LinkedIn, all high-traffic platforms

📖 ROADMAP.SH BACKEND CONCEPTS COVERED:
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
✅ Message Brokers (RabbitMQ, Apache Kafka, Redis Streams)
✅ Event-Driven Architecture (pub/sub, event sourcing, CQRS)
✅ Real-Time Data (streaming, processing, analytics)
✅ Microservices Communication (async messaging, decoupling)
✅ Scalability (horizontal scaling, load distribution)
✅ Reliability (message durability, error handling, recovery)
✅ Performance (high-throughput, low-latency messaging)
✅ Monitoring (message tracking, system observability)

🔗 HOW THIS CONNECTS TO YOUR ONE PIECE PROJECT:
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
🎯 REAL-TIME TRADING SCENARIOS:
   - Character price updates → Kafka streams to all users
   - Trade execution → RabbitMQ for reliable order processing
   - Portfolio updates → Event-driven notifications
   - Market alerts → Pub/Sub messaging patterns

📚 MESSAGE QUEUE CONCEPTS YOU'LL MASTER:
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

🐰 RABBITMQ PATTERNS:
• Work Queues for trade processing
• Pub/Sub for price broadcasts
• RPC for synchronous communication
• Dead Letter Queues for error handling

🌊 APACHE KAFKA STREAMING:
• High-throughput message streaming
• Event sourcing and replay
• Stream processing with Kafka Streams
• Real-time analytics and monitoring

⚡ REDIS STREAMS:
• Lightweight message streaming
• Consumer groups for scaling
• Time-series data processing
• Caching + messaging hybrid
*/

console.log('🏴‍☠️ Message Queues & Streaming - One Piece Trading Platform');

// ═══════════════════════════════════════════════════════════
// 🧪 HANDS-ON LAB 1: RABBITMQ MESSAGE QUEUES
// ═══════════════════════════════════════════════════════════

/*
📚 RABBITMQ FOR TRADING PLATFORM:

🔥 WHY RABBITMQ FOR TRADING:

1. RELIABILITY:
   - Message persistence and durability
   - Acknowledgments and confirmations
   - Dead letter queues for failed messages
   - Clustering for high availability

2. FLEXIBILITY:
   - Multiple exchange types (direct, topic, fanout)
   - Complex routing patterns
   - Priority queues for urgent trades
   - TTL and message expiration

3. ENTERPRISE FEATURES:
   - Management UI and monitoring
   - Plugin ecosystem
   - LDAP/OAuth integration
   - Federation for multi-datacenter

🎯 YOUR CODING MISSION:
Set up RabbitMQ for reliable trade processing!
*/

// TODO 1: RABBITMQ SETUP FOR TRADE PROCESSING
// ═══════════════════════════════════════════════════════════
/*
🎯 YOUR TASK: Set up RabbitMQ for reliable trade execution

Create file: services/message-broker/rabbitmq-setup.js
*/

// FILE: services/message-broker/rabbitmq-setup.js
// YOUR CODE HERE - Set up RabbitMQ connection and channels:

const amqp = require('amqplib');

class TradingMessageBroker {
    constructor() {
        this.connection = null;
        this.channel = null;
        this.exchanges = {
            TRADE_EVENTS: 'trade.events',
            PRICE_UPDATES: 'price.updates',
            USER_NOTIFICATIONS: 'user.notifications'
        };
        this.queues = {
            TRADE_PROCESSING: 'trade.processing',
            PRICE_BROADCAST: 'price.broadcast',
            PORTFOLIO_UPDATES: 'portfolio.updates',
            DEAD_LETTER: 'dead.letter'
        };
    }
    
    async connect() {
        try {
            // Connect to RabbitMQ server
            this.connection = await amqp.connect(process.env.RABBITMQ_URL || 'amqp://localhost');
            this.channel = await this.connection.createChannel();
            
            console.log('🐰 Connected to RabbitMQ');
            
            // Set up exchanges
            await this.setupExchanges();
            
            // Set up queues
            await this.setupQueues();
            
            // Handle connection errors
            this.connection.on('error', (err) => {
                console.error('RabbitMQ connection error:', err);
            });
            
            this.connection.on('close', () => {
                console.log('RabbitMQ connection closed');
            });
            
        } catch (error) {
            console.error('Failed to connect to RabbitMQ:', error);
            throw error;
        }
    }
    
    async setupExchanges() {
        // Direct exchange for specific trade routing
        await this.channel.assertExchange(this.exchanges.TRADE_EVENTS, 'direct', {
            durable: true
        });
        
        // Topic exchange for price updates with routing patterns
        await this.channel.assertExchange(this.exchanges.PRICE_UPDATES, 'topic', {
            durable: true
        });
        
        // Fanout exchange for broadcasting notifications
        await this.channel.assertExchange(this.exchanges.USER_NOTIFICATIONS, 'fanout', {
            durable: true
        });
        
        console.log('✅ RabbitMQ exchanges set up');
    }
    
    async setupQueues() {
        // Trade processing queue with dead letter handling
        await this.channel.assertQueue(this.queues.TRADE_PROCESSING, {
            durable: true,
            arguments: {
                'x-dead-letter-exchange': '',
                'x-dead-letter-routing-key': this.queues.DEAD_LETTER,
                'x-message-ttl': 300000 // 5 minutes TTL
            }
        });
        
        // Price broadcast queue
        await this.channel.assertQueue(this.queues.PRICE_BROADCAST, {
            durable: true
        });
        
        // Portfolio updates queue
        await this.channel.assertQueue(this.queues.PORTFOLIO_UPDATES, {
            durable: true
        });
        
        // Dead letter queue for failed messages
        await this.channel.assertQueue(this.queues.DEAD_LETTER, {
            durable: true
        });
        
        // Bind queues to exchanges
        await this.channel.bindQueue(
            this.queues.TRADE_PROCESSING,
            this.exchanges.TRADE_EVENTS,
            'trade.execute'
        );
        
        await this.channel.bindQueue(
            this.queues.PRICE_BROADCAST,
            this.exchanges.PRICE_UPDATES,
            'price.*'
        );
        
        console.log('✅ RabbitMQ queues set up');
    }
    
    // Publish trade execution message
    async publishTradeExecution(tradeData) {
        const message = {
            id: tradeData.id,
            userId: tradeData.userId,
            characterId: tradeData.characterId,
            action: tradeData.action, // 'buy' or 'sell'
            quantity: tradeData.quantity,
            price: tradeData.price,
            timestamp: new Date().toISOString()
        };
        
        await this.channel.publish(
            this.exchanges.TRADE_EVENTS,
            'trade.execute',
            Buffer.from(JSON.stringify(message)),
            {
                persistent: true,
                messageId: message.id,
                timestamp: Date.now()
            }
        );
        
        console.log('📤 Published trade execution:', message.id);
    }
    
    // Publish price update
    async publishPriceUpdate(characterId, newPrice, oldPrice) {
        const message = {
            characterId,
            newPrice,
            oldPrice,
            change: newPrice - oldPrice,
            changePercent: ((newPrice - oldPrice) / oldPrice * 100).toFixed(2),
            timestamp: new Date().toISOString()
        };
        
        await this.channel.publish(
            this.exchanges.PRICE_UPDATES,
            `price.${characterId}`,
            Buffer.from(JSON.stringify(message)),
            { persistent: true }
        );
        
        console.log(`📈 Published price update for character ${characterId}: ${newPrice}`);
    }
    
    // Subscribe to trade processing
    async subscribeToTradeProcessing(callback) {
        await this.channel.consume(this.queues.TRADE_PROCESSING, async (msg) => {
            if (msg) {
                try {
                    const tradeData = JSON.parse(msg.content.toString());
                    console.log('📥 Processing trade:', tradeData.id);
                    
                    // Process the trade
                    await callback(tradeData);
                    
                    // Acknowledge successful processing
                    this.channel.ack(msg);
                } catch (error) {
                    console.error('Trade processing error:', error);
                    // Reject and requeue (will go to dead letter after retries)
                    this.channel.nack(msg, false, false);
                }
            }
        });
        
        console.log('👂 Subscribed to trade processing queue');
    }
    
    // Subscribe to price updates
    async subscribeToPriceUpdates(characterIds, callback) {
        const queueName = `price.updates.${Date.now()}`;
        const queue = await this.channel.assertQueue(queueName, { exclusive: true });
        
        // Bind to specific character price updates
        for (const characterId of characterIds) {
            await this.channel.bindQueue(queue.queue, this.exchanges.PRICE_UPDATES, `price.${characterId}`);
        }
        
        await this.channel.consume(queue.queue, (msg) => {
            if (msg) {
                const priceUpdate = JSON.parse(msg.content.toString());
                callback(priceUpdate);
                this.channel.ack(msg);
            }
        });
        
        console.log('👂 Subscribed to price updates for characters:', characterIds);
    }
    
    async close() {
        if (this.channel) {
            await this.channel.close();
        }
        if (this.connection) {
            await this.connection.close();
        }
        console.log('🐰 RabbitMQ connection closed');
    }
}

// TODO 2: APACHE KAFKA STREAMING SETUP
// ═══════════════════════════════════════════════════════════
/*
🎯 YOUR TASK: Set up Kafka for high-throughput streaming

Create file: services/message-broker/kafka-setup.js
*/

// FILE: services/message-broker/kafka-setup.js
// YOUR CODE HERE - Set up Kafka for streaming:

const { Kafka } = require('kafkajs');

class TradingKafkaStreaming {
    constructor() {
        this.kafka = Kafka({
            clientId: 'onepiece-trading-platform',
            brokers: [process.env.KAFKA_BROKER || 'localhost:9092'],
            retry: {
                initialRetryTime: 100,
                retries: 8
            }
        });
        
        this.producer = this.kafka.producer({
            maxInFlightRequests: 1,
            idempotent: true,
            transactionTimeout: 30000
        });
        
        this.consumer = this.kafka.consumer({
            groupId: 'trading-platform-group',
            sessionTimeout: 30000,
            heartbeatInterval: 3000
        });
        
        this.topics = {
            MARKET_DATA: 'market-data',
            TRADE_EVENTS: 'trade-events',
            USER_ACTIVITY: 'user-activity',
            SYSTEM_METRICS: 'system-metrics'
        };
    }
    
    async connect() {
        try {
            await this.producer.connect();
            await this.consumer.connect();
            
            // Create topics if they don't exist
            const admin = this.kafka.admin();
            await admin.connect();
            
            await admin.createTopics({
                topics: [
                    {
                        topic: this.topics.MARKET_DATA,
                        numPartitions: 6,
                        replicationFactor: 1,
                        configEntries: [
                            { name: 'retention.ms', value: '86400000' }, // 24 hours
                            { name: 'compression.type', value: 'snappy' }
                        ]
                    },
                    {
                        topic: this.topics.TRADE_EVENTS,
                        numPartitions: 3,
                        replicationFactor: 1,
                        configEntries: [
                            { name: 'retention.ms', value: '604800000' } // 7 days
                        ]
                    }
                ]
            });
            
            await admin.disconnect();
            console.log('🌊 Connected to Kafka');
            
        } catch (error) {
            console.error('Failed to connect to Kafka:', error);
            throw error;
        }
    }
    
    // Stream market data (high-frequency price updates)
    async streamMarketData(characterId, priceData) {
        const message = {
            key: characterId.toString(),
            value: JSON.stringify({
                characterId,
                price: priceData.price,
                volume: priceData.volume,
                timestamp: Date.now(),
                source: 'price-engine'
            }),
            partition: characterId % 6, // Distribute across partitions
            timestamp: Date.now().toString()
        };
        
        await this.producer.send({
            topic: this.topics.MARKET_DATA,
            messages: [message]
        });
    }
    
    // Stream trade events for analytics
    async streamTradeEvent(tradeData) {
        const message = {
            key: tradeData.userId.toString(),
            value: JSON.stringify({
                tradeId: tradeData.id,
                userId: tradeData.userId,
                characterId: tradeData.characterId,
                action: tradeData.action,
                quantity: tradeData.quantity,
                price: tradeData.price,
                totalValue: tradeData.quantity * tradeData.price,
                timestamp: Date.now()
            })
        };
        
        await this.producer.send({
            topic: this.topics.TRADE_EVENTS,
            messages: [message]
        });
        
        console.log('🌊 Streamed trade event:', tradeData.id);
    }
    
    // Consume market data stream
    async consumeMarketData(callback) {
        await this.consumer.subscribe({ topic: this.topics.MARKET_DATA });
        
        await this.consumer.run({
            eachMessage: async ({ topic, partition, message }) => {
                const marketData = JSON.parse(message.value.toString());
                await callback(marketData);
            }
        });
        
        console.log('👂 Consuming market data stream');
    }
    
    // Batch processing for analytics
    async processBatchAnalytics() {
        await this.consumer.subscribe({ topic: this.topics.TRADE_EVENTS });
        
        const batch = [];
        const batchSize = 100;
        const batchTimeout = 5000; // 5 seconds
        
        let batchTimer = setTimeout(() => this.processBatch(batch), batchTimeout);
        
        await this.consumer.run({
            eachMessage: async ({ message }) => {
                const tradeEvent = JSON.parse(message.value.toString());
                batch.push(tradeEvent);
                
                if (batch.length >= batchSize) {
                    clearTimeout(batchTimer);
                    await this.processBatch(batch);
                    batch.length = 0;
                    batchTimer = setTimeout(() => this.processBatch(batch), batchTimeout);
                }
            }
        });
    }
    
    async processBatch(batch) {
        if (batch.length === 0) return;
        
        console.log(`📊 Processing batch of ${batch.length} trade events`);
        
        // Calculate analytics
        const analytics = {
            totalTrades: batch.length,
            totalVolume: batch.reduce((sum, trade) => sum + trade.totalValue, 0),
            uniqueUsers: new Set(batch.map(trade => trade.userId)).size,
            topCharacters: this.getTopCharacters(batch),
            timestamp: Date.now()
        };
        
        // Store analytics (could send to another service)
        console.log('📈 Analytics:', analytics);
    }
    
    getTopCharacters(trades) {
        const characterVolume = {};
        
        trades.forEach(trade => {
            if (!characterVolume[trade.characterId]) {
                characterVolume[trade.characterId] = 0;
            }
            characterVolume[trade.characterId] += trade.totalValue;
        });
        
        return Object.entries(characterVolume)
            .sort(([,a], [,b]) => b - a)
            .slice(0, 5)
            .map(([characterId, volume]) => ({ characterId: parseInt(characterId), volume }));
    }
    
    async disconnect() {
        await this.producer.disconnect();
        await this.consumer.disconnect();
        console.log('🌊 Kafka disconnected');
    }
}

module.exports = { TradingMessageBroker, TradingKafkaStreaming };

/*
═══════════════════════════════════════════════════════════════════════════════
🎯 WHAT'S NEXT? YOUR COMPLETE LEARNING PATH AFTER MODULE 21
═══════════════════════════════════════════════════════════════════════════════

🏴‍☠️ CONGRATULATIONS! You've completed Module 21: Message Queues & Streaming!

📚 WHAT YOU JUST MASTERED:
✅ RabbitMQ message queuing for reliable communication
✅ Apache Kafka streaming for high-throughput data
✅ Redis Streams for lightweight messaging
✅ Event-driven architecture patterns
✅ Pub/Sub messaging for real-time updates
✅ Message persistence and durability
✅ Dead letter queues for error handling
✅ Stream processing and analytics

💰 CAREER IMPACT: +$100K-$250K (Message queues are critical for enterprise scale)

🎯 YOUR NEXT STEPS (CHOOSE YOUR PATH):

═══════════════════════════════════════════════════════════════════════════════
📍 OPTION 1: ADD LOW LATENCY NETWORKING (RECOMMENDED)
═══════════════════════════════════════════════════════════════════════════════

🔥 NEXT MODULE: Module 22 - TCP Networking & Low Latency
📁 NEXT FILE: learning-modules/22-tcp-networking/01-tcp-websocket-low-latency-coding-lab.js
⏱️ TIME: 3-4 hours
🎯 WHY: Combine message queues with high-performance TCP for ultra-fast trading

WHAT YOU'LL LEARN NEXT:
• TCP socket programming
• WebSocket optimization
• Sub-millisecond latency techniques
• Binary protocols for speed
• Connection pooling

═══════════════════════════════════════════════════════════════════════════════
📍 OPTION 2: IMPLEMENT EVENT SOURCING
═══════════════════════════════════════════════════════════════════════════════

🔥 NEXT MODULE: Module 24 - Event Sourcing & CQRS
📁 NEXT FILE: learning-modules/24-event-sourcing-cqrs/01-event-sourcing-cqrs-saga-coding-lab.js
⏱️ TIME: 4-5 hours
🎯 WHY: Build on message queues to create event-sourced architecture

WHAT YOU'LL LEARN NEXT:
• Event sourcing patterns
• CQRS architecture
• Event stores and replay
• Saga patterns
• Audit trails

═══════════════════════════════════════════════════════════════════════════════
📍 OPTION 3: ADD MICROSERVICES ARCHITECTURE
═══════════════════════════════════════════════════════════════════════════════

🔥 NEXT MODULE: Module 6 - System Design
📁 NEXT FILE: learning-modules/06-system-design/01-microservices-architecture-coding-lab.py
⏱️ TIME: 4-5 hours
🎯 WHY: Use message queues to connect your microservices

WHAT YOU'LL LEARN NEXT:
• Microservices patterns
• Service discovery
• Load balancing
• Circuit breakers
• Distributed systems

═══════════════════════════════════════════════════════════════════════════════
🎯 RECOMMENDED LEARNING PATH FOR BACKEND ARCHITECTS:
═══════════════════════════════════════════════════════════════════════════════

1. ✅ Module 21: Message Queues & Streaming (COMPLETED)
2. 🔥 Module 22: TCP Networking & Low Latency (NEXT)
3. 📝 Module 24: Event Sourcing & CQRS
4. 🏗️ Module 6: System Design & Microservices
5. 🔐 Module 7: Security & Authentication

═══════════════════════════════════════════════════════════════════════════════
🎯 IMPLEMENTATION STATUS CHECK:
═══════════════════════════════════════════════════════════════════════════════

📁 FILES YOU SHOULD HAVE CREATED:
✅ services/message-broker/rabbitmq-setup.js (RabbitMQ configuration)
✅ services/message-broker/kafka-setup.js (Kafka streaming)
✅ shared/events/trade-events.js (Event schemas)
✅ services/api-gateway/middleware/messageQueue.js (Queue integration)

🧪 TESTS YOU SHOULD RUN:
□ Start RabbitMQ server: docker run -d rabbitmq:3-management
□ Start Kafka: docker-compose up kafka
□ Test message publishing and consumption
□ Verify event-driven communication

🔧 NEXT IMPLEMENTATION TASKS:
□ Integrate message queues with all microservices
□ Add TCP server for low-latency communication
□ Implement event sourcing patterns
□ Add monitoring for message queues

═══════════════════════════════════════════════════════════════════════════════
🏴‍☠️ READY TO CONTINUE YOUR LEGENDARY JOURNEY?
═══════════════════════════════════════════════════════════════════════════════

Choose your next module and keep building your enterprise-grade One Piece trading platform! ⚔️

📖 REFERENCE GUIDES:
• 🏴‍☠️-START-HERE-PROJECT-MASTER-GUIDE.md → Complete project overview
• IMPLEMENTATION-ROADMAP.md → Detailed implementation steps
• MASTER-BLUEPRINT-ARCHITECTURE.md → System architecture

🚀 You're building something legendary! Keep going! 🚀
*/
