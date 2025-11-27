"""
═══════════════════════════════════════════════════════════════════════════════
🏆 DISTRIBUTED SYSTEMS PATTERNS
═══════════════════════════════════════════════════════════════════════════════

MODULE: 53-large-scale-systems
LESSON: 02 - CAP Theorem, Message Queues, and Microservices

The hard problems of distributed computing.
═══════════════════════════════════════════════════════════════════════════════
"""

# ═══════════════════════════════════════════════════════════════════════════════
# SECTION 1: CAP THEOREM
# ═══════════════════════════════════════════════════════════════════════════════

CAP_THEOREM = """
┌─────────────────────────────────────────────────────────────────────────────┐
│                           CAP THEOREM                                        │
├─────────────────────────────────────────────────────────────────────────────┤
│                                                                              │
│  In a distributed system, you can only guarantee 2 of 3:                    │
│                                                                              │
│                         Consistency                                          │
│                            /\\                                               │
│                           /  \\                                              │
│                          /    \\                                             │
│                         /  CA  \\                                            │
│                        /________\\                                           │
│                       /          \\                                          │
│                      /     CP     \\                                         │
│                     /              \\                                        │
│                    /________________\\                                       │
│            Availability            Partition                                 │
│                                   Tolerance                                  │
│                                                                              │
│  C - Consistency: Every read gets most recent write                         │
│  A - Availability: Every request gets a response                            │
│  P - Partition Tolerance: System works despite network failures             │
│                                                                              │
│  REALITY: Network partitions WILL happen, so you choose:                    │
│                                                                              │
│  CP (Consistency + Partition Tolerance)                                     │
│  - Sacrifice availability during partition                                   │
│  - Examples: MongoDB, HBase, Redis Cluster                                  │
│  - Use for: Financial transactions, inventory                               │
│                                                                              │
│  AP (Availability + Partition Tolerance)                                    │
│  - Sacrifice consistency during partition                                    │
│  - Examples: Cassandra, DynamoDB, CouchDB                                   │
│  - Use for: Social media feeds, analytics                                   │
│                                                                              │
└─────────────────────────────────────────────────────────────────────────────┘
"""

# ═══════════════════════════════════════════════════════════════════════════════
# SECTION 2: MESSAGE QUEUES
# ═══════════════════════════════════════════════════════════════════════════════

MESSAGE_QUEUES = """
┌─────────────────────────────────────────────────────────────────────────────┐
│                         MESSAGE QUEUES                                       │
├─────────────────────────────────────────────────────────────────────────────┤
│                                                                              │
│  WHY USE QUEUES:                                                             │
│  - Decouple services (producer doesn't wait for consumer)                   │
│  - Handle traffic spikes (queue absorbs burst)                              │
│  - Retry failed operations                                                   │
│  - Async processing (send email, process image)                             │
│                                                                              │
│  PATTERN:                                                                    │
│  ┌──────────┐     ┌─────────────┐     ┌──────────┐                         │
│  │ Producer │ ──► │    Queue    │ ──► │ Consumer │                         │
│  │ (API)    │     │ (SQS/Kafka) │     │ (Worker) │                         │
│  └──────────┘     └─────────────┘     └──────────┘                         │
│                                                                              │
│  FANZONE EXAMPLE:                                                            │
│  User submits prediction → Queue → Worker processes → Updates leaderboard  │
│                                                                              │
│  POPULAR OPTIONS:                                                            │
│  ┌────────────────┬─────────────────────────────────────────────────────┐  │
│  │ AWS SQS        │ Simple, managed, at-least-once delivery             │  │
│  │ RabbitMQ       │ Feature-rich, routing, multiple protocols           │  │
│  │ Apache Kafka   │ High throughput, log-based, replay capability       │  │
│  │ Redis Streams  │ Simple, fast, good for real-time                    │  │
│  └────────────────┴─────────────────────────────────────────────────────┘  │
│                                                                              │
│  DELIVERY GUARANTEES:                                                        │
│  - At-most-once: Message may be lost (fastest)                              │
│  - At-least-once: Message may be duplicated (most common)                   │
│  - Exactly-once: Complex, expensive (Kafka transactions)                    │
│                                                                              │
└─────────────────────────────────────────────────────────────────────────────┘
"""

# ═══════════════════════════════════════════════════════════════════════════════
# SECTION 3: MICROSERVICES PATTERNS
# ═══════════════════════════════════════════════════════════════════════════════

MICROSERVICES_PATTERNS = {
    "API_Gateway": {
        "what": "Single entry point for all clients",
        "responsibilities": [
            "Request routing",
            "Authentication",
            "Rate limiting",
            "Request/response transformation"
        ],
        "examples": ["Kong", "AWS API Gateway", "nginx"]
    },
    
    "Service_Discovery": {
        "what": "How services find each other",
        "patterns": [
            "Client-side: Client queries registry (Eureka)",
            "Server-side: Load balancer queries registry",
            "DNS-based: Kubernetes Services"
        ]
    },
    
    "Circuit_Breaker": {
        "what": "Prevent cascade failures",
        "states": ["Closed (normal)", "Open (failing fast)", "Half-Open (testing)"],
        "example": "If payment service fails 5 times, stop calling for 30 seconds",
        "libraries": ["Hystrix", "Resilience4j", "Polly"]
    },
    
    "Saga_Pattern": {
        "what": "Distributed transactions across services",
        "example": "Order: Reserve inventory → Charge payment → Ship",
        "compensation": "If payment fails → Release inventory reservation"
    },
    
    "Event_Sourcing": {
        "what": "Store events, not current state",
        "example": "Instead of balance=100, store: +50, +30, +20",
        "benefits": ["Full audit trail", "Replay events", "Debug by replaying"]
    }
}

# ═══════════════════════════════════════════════════════════════════════════════
# SECTION 4: REAL-WORLD ARCHITECTURE EXAMPLES
# ═══════════════════════════════════════════════════════════════════════════════

REAL_WORLD_ARCHITECTURES = """
┌─────────────────────────────────────────────────────────────────────────────┐
│                    NETFLIX ARCHITECTURE (Simplified)                         │
├─────────────────────────────────────────────────────────────────────────────┤
│                                                                              │
│  User → CDN (Open Connect) → API Gateway (Zuul) → Microservices            │
│                                                                              │
│  Key Components:                                                             │
│  - 1000+ microservices                                                       │
│  - Chaos Monkey (randomly kills services to test resilience)                │
│  - Hystrix (circuit breaker)                                                │
│  - Eureka (service discovery)                                               │
│  - Cassandra (user data, 500+ nodes)                                        │
│  - S3 (video storage)                                                        │
│                                                                              │
│  Scale: 200M+ subscribers, 15% of global internet traffic                   │
│                                                                              │
└─────────────────────────────────────────────────────────────────────────────┘

┌─────────────────────────────────────────────────────────────────────────────┐
│                    TWITTER ARCHITECTURE (Simplified)                         │
├─────────────────────────────────────────────────────────────────────────────┤
│                                                                              │
│  Tweet Flow:                                                                 │
│  User tweets → Write to DB → Fan-out to followers' timelines (Redis)       │
│                                                                              │
│  Timeline Generation:                                                        │
│  - Pre-computed timelines in Redis                                          │
│  - Celebrity tweets: pull on read (too many followers)                      │
│  - Regular users: push on write                                              │
│                                                                              │
│  Scale: 500M tweets/day, 200B timeline deliveries/day                       │
│                                                                              │
└─────────────────────────────────────────────────────────────────────────────┘

┌─────────────────────────────────────────────────────────────────────────────┐
│                    UBER ARCHITECTURE (Simplified)                            │
├─────────────────────────────────────────────────────────────────────────────┤
│                                                                              │
│  Matching System:                                                            │
│  - Geospatial indexing (find nearby drivers)                                │
│  - Real-time location updates (millions/second)                             │
│  - Supply/demand prediction                                                  │
│                                                                              │
│  Key Tech:                                                                   │
│  - Google S2 (geospatial library)                                           │
│  - Kafka (event streaming)                                                   │
│  - Cassandra (trip data)                                                     │
│  - Redis (real-time data)                                                    │
│                                                                              │
│  Scale: 14M trips/day, 5M drivers                                           │
│                                                                              │
└─────────────────────────────────────────────────────────────────────────────┘
"""

# ═══════════════════════════════════════════════════════════════════════════════
# SYSTEM DESIGN INTERVIEW FRAMEWORK
# ═══════════════════════════════════════════════════════════════════════════════

SYSTEM_DESIGN_FRAMEWORK = """
1. CLARIFY REQUIREMENTS (5 min)
   - Functional: What should the system do?
   - Non-functional: Scale, latency, availability
   - Constraints: Budget, timeline, team size

2. ESTIMATE SCALE (5 min)
   - Users: DAU, MAU
   - Traffic: QPS (queries per second)
   - Storage: Data size, growth rate
   - Bandwidth: Read/write ratio

3. HIGH-LEVEL DESIGN (10 min)
   - Draw main components
   - Show data flow
   - Identify APIs

4. DEEP DIVE (15 min)
   - Database schema
   - API design
   - Scaling strategies
   - Caching

5. WRAP UP (5 min)
   - Bottlenecks
   - Trade-offs
   - Future improvements
"""

