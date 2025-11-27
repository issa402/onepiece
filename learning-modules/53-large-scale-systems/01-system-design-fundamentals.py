"""
═══════════════════════════════════════════════════════════════════════════════
🏆 LARGE-SCALE SYSTEM DESIGN MASTERY
═══════════════════════════════════════════════════════════════════════════════

MODULE: 53-large-scale-systems
LESSON: 01 - System Design Fundamentals

WHAT YOU'LL LEARN:
├── Scalability Concepts
│   ├── Vertical vs Horizontal Scaling
│   ├── Load Balancing
│   └── Database Scaling
├── High Availability
│   ├── Redundancy
│   ├── Failover
│   └── Disaster Recovery
├── Performance Optimization
│   ├── Caching Strategies
│   ├── CDN
│   └── Database Optimization
├── Distributed Systems
│   ├── CAP Theorem
│   ├── Consistency Models
│   └── Message Queues
└── Real-World Architectures
    ├── Netflix
    ├── Twitter
    └── Uber

WHY THIS MATTERS:
- System design interviews at FAANG
- Senior engineer expectations
- Building systems that don't fall over
- $300k+ salaries for architects
═══════════════════════════════════════════════════════════════════════════════
"""

# ═══════════════════════════════════════════════════════════════════════════════
# SECTION 1: SCALABILITY FUNDAMENTALS
# ═══════════════════════════════════════════════════════════════════════════════

SCALABILITY = """
┌─────────────────────────────────────────────────────────────────────────────┐
│                    VERTICAL vs HORIZONTAL SCALING                            │
├─────────────────────────────────────────────────────────────────────────────┤
│                                                                              │
│  VERTICAL SCALING (Scale Up)          HORIZONTAL SCALING (Scale Out)        │
│  ┌─────────────────────────┐          ┌─────┐ ┌─────┐ ┌─────┐ ┌─────┐      │
│  │                         │          │     │ │     │ │     │ │     │      │
│  │    BIGGER SERVER        │          │ S1  │ │ S2  │ │ S3  │ │ S4  │      │
│  │    More CPU             │          │     │ │     │ │     │ │     │      │
│  │    More RAM             │          └─────┘ └─────┘ └─────┘ └─────┘      │
│  │    More Disk            │                                                │
│  │                         │          Add more servers                      │
│  └─────────────────────────┘                                                │
│                                                                              │
│  Pros:                                Pros:                                  │
│  - Simple                             - No single point of failure           │
│  - No code changes                    - Theoretically unlimited              │
│  - No distributed complexity          - Cost-effective (commodity hardware)  │
│                                                                              │
│  Cons:                                Cons:                                  │
│  - Hardware limits                    - Complex (distributed systems)        │
│  - Single point of failure            - Data consistency challenges          │
│  - Expensive at scale                 - Network overhead                     │
│                                                                              │
│  Use for:                             Use for:                               │
│  - Databases (initially)              - Stateless services                   │
│  - Simple apps                        - Web servers                          │
│  - Quick fixes                        - Large scale systems                  │
│                                                                              │
└─────────────────────────────────────────────────────────────────────────────┘
"""

# ═══════════════════════════════════════════════════════════════════════════════
# SECTION 2: LOAD BALANCING
# ═══════════════════════════════════════════════════════════════════════════════

LOAD_BALANCING = """
┌─────────────────────────────────────────────────────────────────────────────┐
│                         LOAD BALANCING                                       │
├─────────────────────────────────────────────────────────────────────────────┤
│                                                                              │
│                         Internet                                             │
│                            │                                                 │
│                            ▼                                                 │
│                    ┌───────────────┐                                        │
│                    │ Load Balancer │                                        │
│                    │   (ALB/NLB)   │                                        │
│                    └───────┬───────┘                                        │
│              ┌─────────────┼─────────────┐                                  │
│              ▼             ▼             ▼                                   │
│         ┌────────┐   ┌────────┐   ┌────────┐                               │
│         │Server 1│   │Server 2│   │Server 3│                               │
│         └────────┘   └────────┘   └────────┘                               │
│                                                                              │
│  ALGORITHMS:                                                                 │
│  ┌────────────────────┬─────────────────────────────────────────────────┐  │
│  │ Round Robin        │ Rotate through servers equally                   │  │
│  │ Least Connections  │ Send to server with fewest active connections   │  │
│  │ IP Hash            │ Same client IP → same server (sticky sessions)  │  │
│  │ Weighted           │ More traffic to more powerful servers           │  │
│  │ Random             │ Random selection                                 │  │
│  └────────────────────┴─────────────────────────────────────────────────┘  │
│                                                                              │
│  HEALTH CHECKS:                                                              │
│  - HTTP check: GET /health returns 200                                      │
│  - TCP check: Can connect to port                                           │
│  - Unhealthy servers removed from rotation                                  │
│                                                                              │
│  AWS OPTIONS:                                                                │
│  - ALB: HTTP/HTTPS, path-based routing, WebSocket                          │
│  - NLB: TCP/UDP, ultra-low latency, static IP                              │
│  - CLB: Legacy, avoid for new projects                                      │
│                                                                              │
└─────────────────────────────────────────────────────────────────────────────┘
"""

# ═══════════════════════════════════════════════════════════════════════════════
# SECTION 3: CACHING STRATEGIES
# ═══════════════════════════════════════════════════════════════════════════════

CACHING_STRATEGIES = {
    "Cache-Aside": {
        "pattern": "App checks cache → if miss, query DB → store in cache",
        "pros": ["Simple", "Cache only what's needed"],
        "cons": ["Cache miss = slow", "Stale data possible"],
        "use_for": "Read-heavy workloads"
    },
    
    "Write-Through": {
        "pattern": "Write to cache AND DB simultaneously",
        "pros": ["Data always consistent", "No stale data"],
        "cons": ["Write latency", "Cache may have unused data"],
        "use_for": "When consistency is critical"
    },
    
    "Write-Behind": {
        "pattern": "Write to cache → async write to DB",
        "pros": ["Fast writes", "Batch DB writes"],
        "cons": ["Data loss risk", "Complex"],
        "use_for": "Write-heavy, can tolerate some loss"
    },
    
    "Read-Through": {
        "pattern": "Cache handles DB reads transparently",
        "pros": ["Simple app code", "Automatic population"],
        "cons": ["First read slow", "Cache library dependency"],
        "use_for": "When using cache library"
    }
}

CACHE_LAYERS = """
┌─────────────────────────────────────────────────────────────────────────────┐
│                         CACHING LAYERS                                       │
├─────────────────────────────────────────────────────────────────────────────┤
│                                                                              │
│  User → Browser Cache → CDN → Load Balancer → App Cache → DB Cache → DB    │
│                                                                              │
│  1. BROWSER CACHE                                                            │
│     - Static assets (JS, CSS, images)                                       │
│     - Cache-Control headers                                                  │
│     - ETags for validation                                                   │
│                                                                              │
│  2. CDN (CloudFront, Cloudflare)                                            │
│     - Static content globally distributed                                    │
│     - Edge locations close to users                                          │
│     - Reduces origin load                                                    │
│                                                                              │
│  3. APPLICATION CACHE (Redis, Memcached)                                    │
│     - Session data                                                           │
│     - API responses                                                          │
│     - Computed results                                                       │
│                                                                              │
│  4. DATABASE CACHE                                                           │
│     - Query cache                                                            │
│     - Buffer pool                                                            │
│     - Connection pooling                                                     │
│                                                                              │
└─────────────────────────────────────────────────────────────────────────────┘
"""

# ═══════════════════════════════════════════════════════════════════════════════
# SECTION 4: DATABASE SCALING
# ═══════════════════════════════════════════════════════════════════════════════

DATABASE_SCALING = {
    "Read_Replicas": {
        "what": "Copy of primary DB for read queries",
        "pattern": "Writes → Primary, Reads → Replicas",
        "use_when": "Read-heavy workload (90% reads)",
        "example": "RDS Read Replicas"
    },
    
    "Sharding": {
        "what": "Split data across multiple databases",
        "strategies": [
            "Range-based: users 1-1M → shard1, 1M-2M → shard2",
            "Hash-based: hash(user_id) % num_shards",
            "Geographic: US users → us-db, EU users → eu-db"
        ],
        "challenges": ["Cross-shard queries", "Rebalancing", "Joins"],
        "use_when": "Single DB can't handle write load"
    },
    
    "CQRS": {
        "what": "Command Query Responsibility Segregation",
        "pattern": "Separate read and write models",
        "use_when": "Complex domain, different read/write patterns"
    }
}

