/*
🏴‍☠️ ONE PIECE TRADING PLATFORM - TCP NETWORKING & LOW LATENCY LAB
═══════════════════════════════════════════════════════════════════════════════

🎯 WHAT YOU'LL MASTER FOR YOUR ONE PIECE PROJECT:
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
✅ TCP SOCKET PROGRAMMING - Low-level network communication
✅ WEBSOCKET REAL-TIME - Bidirectional client-server communication
✅ LOW LATENCY OPTIMIZATION - Sub-millisecond response times
✅ NETWORK PROTOCOLS - Custom binary protocols for speed
✅ CONNECTION POOLING - Efficient connection management
✅ HEARTBEAT & RECONNECTION - Robust connection handling

💰 SALARY IMPACT: +$150K-$300K (Low latency is highest-paid skill)
🏢 COMPANIES: High-frequency trading firms, gaming companies, real-time platforms

🔗 HOW THIS CONNECTS TO YOUR ONE PIECE PROJECT:
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
🎯 REAL-TIME TRADING REQUIREMENTS:
   - Price updates → Sub-10ms latency to all connected users
   - Trade execution → Instant order confirmation
   - Market data → High-frequency streaming (1000+ updates/sec)
   - Connection reliability → 99.99% uptime with auto-reconnect

📚 NETWORKING CONCEPTS YOU'LL MASTER:
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

🔌 TCP SOCKET PROGRAMMING:
• Raw TCP connections for maximum performance
• Custom binary protocols for minimal overhead
• Connection pooling and multiplexing
• Non-blocking I/O and event loops

⚡ WEBSOCKET OPTIMIZATION:
• WebSocket compression and extensions
• Binary frame optimization
• Connection upgrade handling
• Ping/pong heartbeat mechanisms

🚀 LOW LATENCY TECHNIQUES:
• TCP_NODELAY for immediate packet sending
• SO_REUSEADDR for rapid connection reuse
• Kernel bypass techniques
• Memory-mapped I/O for zero-copy
*/

console.log('🏴‍☠️ TCP Networking & Low Latency - One Piece Trading Platform');

// ═══════════════════════════════════════════════════════════
// 🧪 HANDS-ON LAB 1: TCP SOCKET SERVER
// ═══════════════════════════════════════════════════════════

/*
📚 TCP SOCKETS FOR TRADING PLATFORM:

🔥 WHY TCP SOCKETS FOR TRADING:

1. PERFORMANCE:
   - Direct kernel-level communication
   - No HTTP overhead (headers, parsing)
   - Custom binary protocols
   - Sub-millisecond latency possible

2. CONTROL:
   - Full control over connection lifecycle
   - Custom heartbeat and reconnection logic
   - Precise buffer management
   - Connection multiplexing

3. RELIABILITY:
   - TCP guarantees delivery and ordering
   - Built-in flow control
   - Connection state management
   - Error detection and recovery

🎯 YOUR CODING MISSION:
Build a high-performance TCP server for real-time trading!
*/

// TODO 1: HIGH-PERFORMANCE TCP SERVER
// ═══════════════════════════════════════════════════════════
/*
🎯 YOUR TASK: Create a TCP server for real-time price streaming

Create file: services/tcp-server/high-performance-tcp.js
*/

// FILE: services/tcp-server/high-performance-tcp.js
// YOUR CODE HERE - Create high-performance TCP server:

const net = require('net');
const EventEmitter = require('events');

class HighPerformanceTradingServer extends EventEmitter {
    constructor(options = {}) {
        super();
        this.port = options.port || 8080;
        this.host = options.host || '0.0.0.0';
        this.clients = new Map();
        this.server = null;
        this.messageBuffer = Buffer.alloc(1024 * 1024); // 1MB buffer
        this.stats = {
            connections: 0,
            messagesPerSecond: 0,
            bytesPerSecond: 0,
            lastStatsTime: Date.now()
        };
        
        // Performance optimizations
        this.options = {
            keepAlive: true,
            keepAliveInitialDelay: 30000,
            noDelay: true, // TCP_NODELAY for low latency
            allowHalfOpen: false,
            ...options
        };
    }
    
    start() {
        this.server = net.createServer(this.options, (socket) => {
            this.handleConnection(socket);
        });
        
        // Server optimizations
        this.server.maxConnections = 10000;
        
        this.server.listen(this.port, this.host, () => {
            console.log(`🚀 High-performance TCP server listening on ${this.host}:${this.port}`);
        });
        
        this.server.on('error', (err) => {
            console.error('TCP Server error:', err);
            this.emit('error', err);
        });
        
        // Start performance monitoring
        this.startPerformanceMonitoring();
        
        return this;
    }
    
    handleConnection(socket) {
        const clientId = `${socket.remoteAddress}:${socket.remotePort}`;
        
        // Socket optimizations for low latency
        socket.setNoDelay(true); // Disable Nagle's algorithm
        socket.setKeepAlive(true, 30000);
        socket.setTimeout(60000); // 60 second timeout
        
        // Client state
        const client = {
            id: clientId,
            socket: socket,
            authenticated: false,
            subscriptions: new Set(),
            lastHeartbeat: Date.now(),
            messageCount: 0,
            bytesReceived: 0,
            bytesSent: 0
        };
        
        this.clients.set(clientId, client);
        this.stats.connections++;
        
        console.log(`📡 New TCP connection: ${clientId} (Total: ${this.clients.size})`);
        
        // Handle incoming data
        socket.on('data', (data) => {
            this.handleMessage(client, data);
        });
        
        // Handle connection close
        socket.on('close', () => {
            this.clients.delete(clientId);
            this.stats.connections--;
            console.log(`📡 TCP connection closed: ${clientId} (Total: ${this.clients.size})`);
        });
        
        // Handle errors
        socket.on('error', (err) => {
            console.error(`TCP connection error ${clientId}:`, err.message);
            this.clients.delete(clientId);
        });
        
        // Handle timeout
        socket.on('timeout', () => {
            console.log(`⏰ TCP connection timeout: ${clientId}`);
            socket.destroy();
        });
        
        // Send welcome message
        this.sendMessage(client, {
            type: 'welcome',
            clientId: clientId,
            timestamp: Date.now()
        });
        
        this.emit('connection', client);
    }
    
    handleMessage(client, data) {
        try {
            client.bytesReceived += data.length;
            client.messageCount++;
            
            // Parse binary protocol message
            const message = this.parseMessage(data);
            
            switch (message.type) {
                case 'heartbeat':
                    client.lastHeartbeat = Date.now();
                    this.sendMessage(client, { type: 'heartbeat_ack', timestamp: Date.now() });
                    break;
                    
                case 'authenticate':
                    this.handleAuthentication(client, message);
                    break;
                    
                case 'subscribe':
                    this.handleSubscription(client, message);
                    break;
                    
                case 'unsubscribe':
                    this.handleUnsubscription(client, message);
                    break;
                    
                case 'trade_order':
                    this.handleTradeOrder(client, message);
                    break;
                    
                default:
                    console.warn(`Unknown message type: ${message.type}`);
            }
            
            this.emit('message', client, message);
            
        } catch (error) {
            console.error('Message parsing error:', error);
            this.sendError(client, 'Invalid message format');
        }
    }
    
    // Custom binary protocol parser for performance
    parseMessage(buffer) {
        try {
            // Simple JSON protocol (in production, use binary format)
            const messageStr = buffer.toString('utf8');
            return JSON.parse(messageStr);
        } catch (error) {
            throw new Error('Failed to parse message');
        }
    }
    
    // Send message with binary protocol
    sendMessage(client, message) {
        try {
            const messageStr = JSON.stringify(message);
            const buffer = Buffer.from(messageStr, 'utf8');
            
            client.socket.write(buffer);
            client.bytesSent += buffer.length;
            
            this.stats.messagesPerSecond++;
            this.stats.bytesPerSecond += buffer.length;
            
        } catch (error) {
            console.error('Failed to send message:', error);
        }
    }
    
    // Broadcast to all authenticated clients
    broadcast(message, filter = null) {
        const buffer = Buffer.from(JSON.stringify(message), 'utf8');
        let sentCount = 0;
        
        for (const client of this.clients.values()) {
            if (client.authenticated && (!filter || filter(client))) {
                try {
                    client.socket.write(buffer);
                    client.bytesSent += buffer.length;
                    sentCount++;
                } catch (error) {
                    console.error(`Failed to broadcast to ${client.id}:`, error);
                }
            }
        }
        
        this.stats.messagesPerSecond += sentCount;
        this.stats.bytesPerSecond += buffer.length * sentCount;
        
        return sentCount;
    }
    
    // Broadcast price update to subscribed clients
    broadcastPriceUpdate(characterId, priceData) {
        const message = {
            type: 'price_update',
            characterId: characterId,
            price: priceData.price,
            change: priceData.change,
            volume: priceData.volume,
            timestamp: Date.now()
        };
        
        const sentCount = this.broadcast(message, (client) => {
            return client.subscriptions.has(`price.${characterId}`) || 
                   client.subscriptions.has('price.*');
        });
        
        console.log(`📈 Broadcasted price update for character ${characterId} to ${sentCount} clients`);
    }
    
    handleAuthentication(client, message) {
        // Simple authentication (in production, use JWT or similar)
        if (message.token && message.token.length > 0) {
            client.authenticated = true;
            client.userId = message.userId;
            
            this.sendMessage(client, {
                type: 'auth_success',
                userId: client.userId,
                timestamp: Date.now()
            });
            
            console.log(`🔐 Client authenticated: ${client.id} (User: ${client.userId})`);
        } else {
            this.sendError(client, 'Authentication failed');
        }
    }
    
    handleSubscription(client, message) {
        if (!client.authenticated) {
            this.sendError(client, 'Authentication required');
            return;
        }
        
        const subscription = message.subscription;
        client.subscriptions.add(subscription);
        
        this.sendMessage(client, {
            type: 'subscription_success',
            subscription: subscription,
            timestamp: Date.now()
        });
        
        console.log(`📡 Client ${client.id} subscribed to: ${subscription}`);
    }
    
    handleUnsubscription(client, message) {
        const subscription = message.subscription;
        client.subscriptions.delete(subscription);
        
        this.sendMessage(client, {
            type: 'unsubscription_success',
            subscription: subscription,
            timestamp: Date.now()
        });
    }
    
    handleTradeOrder(client, message) {
        if (!client.authenticated) {
            this.sendError(client, 'Authentication required');
            return;
        }
        
        // Emit trade order for processing
        this.emit('trade_order', client, message);
        
        // Send immediate acknowledgment
        this.sendMessage(client, {
            type: 'trade_order_ack',
            orderId: message.orderId,
            timestamp: Date.now()
        });
    }
    
    sendError(client, errorMessage) {
        this.sendMessage(client, {
            type: 'error',
            message: errorMessage,
            timestamp: Date.now()
        });
    }
    
    startPerformanceMonitoring() {
        setInterval(() => {
            const now = Date.now();
            const timeDiff = (now - this.stats.lastStatsTime) / 1000;
            
            const messagesPerSec = Math.round(this.stats.messagesPerSecond / timeDiff);
            const bytesPerSec = Math.round(this.stats.bytesPerSecond / timeDiff);
            const mbPerSec = (bytesPerSec / 1024 / 1024).toFixed(2);
            
            console.log(`📊 Performance: ${messagesPerSec} msg/s, ${mbPerSec} MB/s, ${this.clients.size} connections`);
            
            // Reset counters
            this.stats.messagesPerSecond = 0;
            this.stats.bytesPerSecond = 0;
            this.stats.lastStatsTime = now;
            
            // Check for stale connections
            this.checkHeartbeats();
            
        }, 5000); // Every 5 seconds
    }
    
    checkHeartbeats() {
        const now = Date.now();
        const heartbeatTimeout = 60000; // 60 seconds
        
        for (const [clientId, client] of this.clients.entries()) {
            if (now - client.lastHeartbeat > heartbeatTimeout) {
                console.log(`💔 Heartbeat timeout for client: ${clientId}`);
                client.socket.destroy();
            }
        }
    }
    
    getStats() {
        return {
            connections: this.clients.size,
            totalConnections: this.stats.connections,
            uptime: process.uptime(),
            memoryUsage: process.memoryUsage()
        };
    }
    
    stop() {
        if (this.server) {
            this.server.close(() => {
                console.log('🛑 TCP server stopped');
            });
            
            // Close all client connections
            for (const client of this.clients.values()) {
                client.socket.destroy();
            }
            
            this.clients.clear();
        }
    }
}

module.exports = { HighPerformanceTradingServer };
