/*
🏴‍☠️ ONE PIECE TRADING PLATFORM - EVENT SOURCING & CQRS LAB
═══════════════════════════════════════════════════════════════════════════════

🎯 WHAT YOU'LL MASTER FOR YOUR ONE PIECE PROJECT:
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
✅ EVENT SOURCING - Store all changes as immutable events
✅ CQRS PATTERN - Separate read and write models
✅ SAGA PATTERN - Distributed transaction management
✅ EVENT STORE - Persistent event storage and replay
✅ PROJECTION BUILDING - Materialized views from events
✅ EVENTUAL CONSISTENCY - Distributed system consistency

💰 SALARY IMPACT: +$150K-$300K (Advanced architecture patterns)
🏢 COMPANIES: Netflix, Amazon, Microsoft, all enterprise systems

🔗 HOW THIS CONNECTS TO YOUR ONE PIECE PROJECT:
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
🎯 TRADING PLATFORM BENEFITS:
   - Trade audit trail → Every trade stored as immutable event
   - Portfolio history → Complete reconstruction from events
   - System recovery → Replay events to rebuild state
   - Analytics → Historical analysis of all trading activity
   - Compliance → Immutable audit log for regulations

📚 ARCHITECTURE PATTERNS YOU'LL MASTER:
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

📝 EVENT SOURCING:
• Events as single source of truth
• Event store for persistence
• Event replay for state reconstruction
• Snapshots for performance optimization

🔄 CQRS (Command Query Responsibility Segregation):
• Separate write models (commands)
• Separate read models (queries)
• Optimized projections for different views
• Independent scaling of reads and writes

🎭 SAGA PATTERN:
• Distributed transaction coordination
• Compensating actions for rollbacks
• Long-running business processes
• Failure handling and recovery
*/

console.log('🏴‍☠️ Event Sourcing & CQRS - One Piece Trading Platform');

// ═══════════════════════════════════════════════════════════
// 🧪 HANDS-ON LAB 1: EVENT SOURCING IMPLEMENTATION
// ═══════════════════════════════════════════════════════════

/*
📚 EVENT SOURCING FOR TRADING PLATFORM:

🔥 WHY EVENT SOURCING FOR TRADING:

1. AUDIT TRAIL:
   - Every trade is an immutable event
   - Complete history of all changes
   - Regulatory compliance requirements
   - Forensic analysis capabilities

2. SYSTEM RECOVERY:
   - Rebuild state from events
   - Point-in-time recovery
   - Disaster recovery scenarios
   - Data corruption protection

3. ANALYTICS & INSIGHTS:
   - Historical trend analysis
   - User behavior patterns
   - Market movement correlation
   - Performance optimization data

🎯 YOUR CODING MISSION:
Build an event-sourced trading system!
*/

// TODO 1: EVENT STORE IMPLEMENTATION
// ═══════════════════════════════════════════════════════════
/*
🎯 YOUR TASK: Create event store for trading events

Create file: services/event-store/trading-event-store.js
*/

// FILE: services/event-store/trading-event-store.js
// YOUR CODE HERE - Create event store:

const EventEmitter = require('events');
const { v4: uuidv4 } = require('uuid');

class TradingEventStore extends EventEmitter {
    constructor(storage = null) {
        super();
        this.events = new Map(); // In production, use persistent storage
        this.snapshots = new Map();
        this.projections = new Map();
        this.storage = storage; // Database adapter
        this.eventHandlers = new Map();
        
        console.log('📝 Trading Event Store initialized');
    }
    
    // Append event to stream
    async appendEvent(streamId, eventType, eventData, expectedVersion = -1) {
        try {
            const event = {
                eventId: uuidv4(),
                streamId: streamId,
                eventType: eventType,
                eventData: eventData,
                metadata: {
                    timestamp: new Date().toISOString(),
                    version: this.getStreamVersion(streamId) + 1,
                    correlationId: eventData.correlationId || uuidv4(),
                    causationId: eventData.causationId || null
                }
            };
            
            // Optimistic concurrency check
            const currentVersion = this.getStreamVersion(streamId);
            if (expectedVersion !== -1 && currentVersion !== expectedVersion) {
                throw new Error(`Concurrency conflict. Expected version ${expectedVersion}, but current version is ${currentVersion}`);
            }
            
            // Store event
            if (!this.events.has(streamId)) {
                this.events.set(streamId, []);
            }
            
            this.events.get(streamId).push(event);
            
            // Persist to storage if available
            if (this.storage) {
                await this.storage.saveEvent(event);
            }
            
            // Emit event for projections
            this.emit('eventAppended', event);
            
            // Process event handlers
            await this.processEventHandlers(event);
            
            console.log(`📝 Event appended: ${eventType} to stream ${streamId}`);
            return event;
            
        } catch (error) {
            console.error('Failed to append event:', error);
            throw error;
        }
    }
    
    // Read events from stream
    async readStream(streamId, fromVersion = 0, maxCount = 1000) {
        try {
            const streamEvents = this.events.get(streamId) || [];
            
            return streamEvents
                .filter(event => event.metadata.version >= fromVersion)
                .slice(0, maxCount);
                
        } catch (error) {
            console.error('Failed to read stream:', error);
            throw error;
        }
    }
    
    // Read all events of specific type
    async readEventsByType(eventType, fromTimestamp = null, maxCount = 1000) {
        try {
            const allEvents = [];
            
            for (const streamEvents of this.events.values()) {
                for (const event of streamEvents) {
                    if (event.eventType === eventType) {
                        if (!fromTimestamp || new Date(event.metadata.timestamp) >= fromTimestamp) {
                            allEvents.push(event);
                        }
                    }
                }
            }
            
            return allEvents
                .sort((a, b) => new Date(a.metadata.timestamp) - new Date(b.metadata.timestamp))
                .slice(0, maxCount);
                
        } catch (error) {
            console.error('Failed to read events by type:', error);
            throw error;
        }
    }
    
    // Create snapshot for performance
    async createSnapshot(streamId, aggregateData) {
        try {
            const version = this.getStreamVersion(streamId);
            
            const snapshot = {
                streamId: streamId,
                version: version,
                data: aggregateData,
                timestamp: new Date().toISOString()
            };
            
            this.snapshots.set(streamId, snapshot);
            
            if (this.storage) {
                await this.storage.saveSnapshot(snapshot);
            }
            
            console.log(`📸 Snapshot created for stream ${streamId} at version ${version}`);
            return snapshot;
            
        } catch (error) {
            console.error('Failed to create snapshot:', error);
            throw error;
        }
    }
    
    // Load aggregate from events (with snapshot optimization)
    async loadAggregate(streamId, aggregateClass) {
        try {
            let aggregate = new aggregateClass();
            let fromVersion = 0;
            
            // Load from snapshot if available
            const snapshot = this.snapshots.get(streamId);
            if (snapshot) {
                aggregate = aggregateClass.fromSnapshot(snapshot.data);
                fromVersion = snapshot.version + 1;
            }
            
            // Apply events since snapshot
            const events = await this.readStream(streamId, fromVersion);
            
            for (const event of events) {
                aggregate.applyEvent(event);
            }
            
            return aggregate;
            
        } catch (error) {
            console.error('Failed to load aggregate:', error);
            throw error;
        }
    }
    
    // Register event handler
    registerEventHandler(eventType, handler) {
        if (!this.eventHandlers.has(eventType)) {
            this.eventHandlers.set(eventType, []);
        }
        
        this.eventHandlers.get(eventType).push(handler);
        console.log(`🎯 Event handler registered for ${eventType}`);
    }
    
    // Process event handlers
    async processEventHandlers(event) {
        const handlers = this.eventHandlers.get(event.eventType) || [];
        
        for (const handler of handlers) {
            try {
                await handler(event);
            } catch (error) {
                console.error(`Event handler failed for ${event.eventType}:`, error);
                // In production, implement retry logic or dead letter queue
            }
        }
    }
    
    // Get current version of stream
    getStreamVersion(streamId) {
        const streamEvents = this.events.get(streamId) || [];
        return streamEvents.length > 0 ? streamEvents[streamEvents.length - 1].metadata.version : 0;
    }
    
    // Replay events for projections
    async replayEvents(fromTimestamp = null, eventTypes = null) {
        console.log('🔄 Starting event replay...');
        
        const allEvents = [];
        
        for (const streamEvents of this.events.values()) {
            for (const event of streamEvents) {
                if (!fromTimestamp || new Date(event.metadata.timestamp) >= fromTimestamp) {
                    if (!eventTypes || eventTypes.includes(event.eventType)) {
                        allEvents.push(event);
                    }
                }
            }
        }
        
        // Sort by timestamp
        allEvents.sort((a, b) => new Date(a.metadata.timestamp) - new Date(b.metadata.timestamp));
        
        // Replay events
        for (const event of allEvents) {
            this.emit('eventReplayed', event);
            await this.processEventHandlers(event);
        }
        
        console.log(`🔄 Replayed ${allEvents.length} events`);
        return allEvents.length;
    }
}

// TODO 2: TRADING AGGREGATE WITH EVENT SOURCING
// ═══════════════════════════════════════════════════════════
/*
🎯 YOUR TASK: Create trading aggregate that uses event sourcing

Create file: services/event-store/trading-aggregate.js
*/

// FILE: services/event-store/trading-aggregate.js
// YOUR CODE HERE - Create event-sourced aggregate:

class TradingAggregate {
    constructor(userId) {
        this.userId = userId;
        this.version = 0;
        this.portfolio = new Map();
        this.balance = 0;
        this.tradeHistory = [];
        this.uncommittedEvents = [];
    }
    
    // Static factory method from snapshot
    static fromSnapshot(snapshotData) {
        const aggregate = new TradingAggregate(snapshotData.userId);
        aggregate.version = snapshotData.version;
        aggregate.portfolio = new Map(snapshotData.portfolio);
        aggregate.balance = snapshotData.balance;
        aggregate.tradeHistory = snapshotData.tradeHistory || [];
        return aggregate;
    }
    
    // Apply event to aggregate state
    applyEvent(event) {
        switch (event.eventType) {
            case 'UserRegistered':
                this.applyUserRegistered(event);
                break;
            case 'FundsDeposited':
                this.applyFundsDeposited(event);
                break;
            case 'TradeExecuted':
                this.applyTradeExecuted(event);
                break;
            case 'CharacterPurchased':
                this.applyCharacterPurchased(event);
                break;
            case 'CharacterSold':
                this.applyCharacterSold(event);
                break;
            default:
                console.warn(`Unknown event type: ${event.eventType}`);
        }
        
        this.version = event.metadata.version;
    }
    
    // Command: Register user
    registerUser(userData) {
        if (this.version > 0) {
            throw new Error('User already registered');
        }
        
        const event = {
            eventType: 'UserRegistered',
            eventData: {
                userId: this.userId,
                email: userData.email,
                username: userData.username,
                registrationDate: new Date().toISOString()
            }
        };
        
        this.addUncommittedEvent(event);
        this.applyEvent(event);
    }
    
    // Command: Deposit funds
    depositFunds(amount, source = 'bank_transfer') {
        if (amount <= 0) {
            throw new Error('Deposit amount must be positive');
        }
        
        const event = {
            eventType: 'FundsDeposited',
            eventData: {
                userId: this.userId,
                amount: amount,
                source: source,
                timestamp: new Date().toISOString(),
                transactionId: require('uuid').v4()
            }
        };
        
        this.addUncommittedEvent(event);
        this.applyEvent(event);
    }
    
    // Command: Execute trade
    executeTrade(characterId, action, quantity, price) {
        const totalCost = quantity * price;
        
        // Business rule validation
        if (action === 'buy' && this.balance < totalCost) {
            throw new Error('Insufficient funds for purchase');
        }
        
        if (action === 'sell') {
            const currentQuantity = this.portfolio.get(characterId) || 0;
            if (currentQuantity < quantity) {
                throw new Error('Insufficient character quantity for sale');
            }
        }
        
        const event = {
            eventType: 'TradeExecuted',
            eventData: {
                userId: this.userId,
                characterId: characterId,
                action: action,
                quantity: quantity,
                price: price,
                totalValue: totalCost,
                timestamp: new Date().toISOString(),
                tradeId: require('uuid').v4()
            }
        };
        
        this.addUncommittedEvent(event);
        this.applyEvent(event);
        
        // Generate specific purchase/sale events
        if (action === 'buy') {
            this.purchaseCharacter(characterId, quantity, price);
        } else {
            this.sellCharacter(characterId, quantity, price);
        }
    }
    
    // Command: Purchase character
    purchaseCharacter(characterId, quantity, price) {
        const event = {
            eventType: 'CharacterPurchased',
            eventData: {
                userId: this.userId,
                characterId: characterId,
                quantity: quantity,
                price: price,
                totalCost: quantity * price,
                timestamp: new Date().toISOString()
            }
        };
        
        this.addUncommittedEvent(event);
        this.applyEvent(event);
    }
    
    // Command: Sell character
    sellCharacter(characterId, quantity, price) {
        const event = {
            eventType: 'CharacterSold',
            eventData: {
                userId: this.userId,
                characterId: characterId,
                quantity: quantity,
                price: price,
                totalValue: quantity * price,
                timestamp: new Date().toISOString()
            }
        };
        
        this.addUncommittedEvent(event);
        this.applyEvent(event);
    }
    
    // Event handlers
    applyUserRegistered(event) {
        // User registration doesn't change state much
        console.log(`👤 User registered: ${event.eventData.username}`);
    }
    
    applyFundsDeposited(event) {
        this.balance += event.eventData.amount;
        console.log(`💰 Funds deposited: ${event.eventData.amount}, New balance: ${this.balance}`);
    }
    
    applyTradeExecuted(event) {
        const trade = {
            tradeId: event.eventData.tradeId,
            characterId: event.eventData.characterId,
            action: event.eventData.action,
            quantity: event.eventData.quantity,
            price: event.eventData.price,
            timestamp: event.eventData.timestamp
        };
        
        this.tradeHistory.push(trade);
        console.log(`📊 Trade executed: ${event.eventData.action} ${event.eventData.quantity} of character ${event.eventData.characterId}`);
    }
    
    applyCharacterPurchased(event) {
        const characterId = event.eventData.characterId;
        const quantity = event.eventData.quantity;
        const totalCost = event.eventData.totalCost;
        
        // Update portfolio
        const currentQuantity = this.portfolio.get(characterId) || 0;
        this.portfolio.set(characterId, currentQuantity + quantity);
        
        // Deduct from balance
        this.balance -= totalCost;
        
        console.log(`🛒 Character purchased: ${quantity} of ${characterId}, Remaining balance: ${this.balance}`);
    }
    
    applyCharacterSold(event) {
        const characterId = event.eventData.characterId;
        const quantity = event.eventData.quantity;
        const totalValue = event.eventData.totalValue;
        
        // Update portfolio
        const currentQuantity = this.portfolio.get(characterId) || 0;
        this.portfolio.set(characterId, currentQuantity - quantity);
        
        // Add to balance
        this.balance += totalValue;
        
        console.log(`💸 Character sold: ${quantity} of ${characterId}, New balance: ${this.balance}`);
    }
    
    // Add uncommitted event
    addUncommittedEvent(event) {
        event.metadata = {
            version: this.version + this.uncommittedEvents.length + 1,
            timestamp: new Date().toISOString()
        };
        
        this.uncommittedEvents.push(event);
    }
    
    // Get uncommitted events
    getUncommittedEvents() {
        return [...this.uncommittedEvents];
    }
    
    // Mark events as committed
    markEventsAsCommitted() {
        this.uncommittedEvents = [];
    }
    
    // Get current state for snapshot
    getSnapshotData() {
        return {
            userId: this.userId,
            version: this.version,
            portfolio: Array.from(this.portfolio.entries()),
            balance: this.balance,
            tradeHistory: this.tradeHistory
        };
    }
    
    // Get portfolio summary
    getPortfolioSummary() {
        const summary = {
            userId: this.userId,
            balance: this.balance,
            totalCharacters: 0,
            characters: []
        };
        
        for (const [characterId, quantity] of this.portfolio.entries()) {
            if (quantity > 0) {
                summary.characters.push({
                    characterId: characterId,
                    quantity: quantity
                });
                summary.totalCharacters += quantity;
            }
        }
        
        return summary;
    }
}

module.exports = { TradingEventStore, TradingAggregate };
