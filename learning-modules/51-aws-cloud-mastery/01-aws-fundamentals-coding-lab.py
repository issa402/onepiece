"""
═══════════════════════════════════════════════════════════════════════════════
🏆 AWS CLOUD MASTERY
═══════════════════════════════════════════════════════════════════════════════

MODULE: 51-aws-cloud-mastery
LESSON: 01 - AWS Fundamentals & Core Services

WHAT YOU'LL LEARN:
├── AWS Global Infrastructure
│   ├── Regions & Availability Zones
│   ├── Edge Locations
│   └── Data Residency
├── Core Compute Services
│   ├── EC2 (Virtual Machines)
│   ├── ECS/EKS (Containers)
│   └── Lambda (Serverless)
├── Storage Services
│   ├── S3 (Object Storage)
│   ├── EBS (Block Storage)
│   └── EFS (File Storage)
├── Database Services
│   ├── RDS (Relational)
│   ├── DynamoDB (NoSQL)
│   └── ElastiCache (Redis/Memcached)
├── Networking
│   ├── VPC, Subnets, Route Tables
│   ├── Security Groups, NACLs
│   └── Load Balancers (ALB, NLB)
└── Security & Identity
    ├── IAM (Users, Roles, Policies)
    └── Security Best Practices

WHY AWS:
- 32% market share (largest cloud provider)
- Most job postings require AWS
- Certifications highly valued
- Used by Netflix, Airbnb, NASA
═══════════════════════════════════════════════════════════════════════════════
"""

# ═══════════════════════════════════════════════════════════════════════════════
# SECTION 1: AWS GLOBAL INFRASTRUCTURE
# ═══════════════════════════════════════════════════════════════════════════════

AWS_INFRASTRUCTURE = """
┌─────────────────────────────────────────────────────────────────────────────┐
│                    AWS GLOBAL INFRASTRUCTURE                                 │
├─────────────────────────────────────────────────────────────────────────────┤
│                                                                              │
│  REGION (Geographic Area)                                                    │
│  Example: us-east-1 (N. Virginia), eu-west-1 (Ireland)                      │
│  ┌────────────────────────────────────────────────────────────────────────┐ │
│  │  AVAILABILITY ZONE (AZ) - Isolated Data Center(s)                      │ │
│  │  ┌──────────────┐  ┌──────────────┐  ┌──────────────┐                  │ │
│  │  │   us-east-1a │  │   us-east-1b │  │   us-east-1c │                  │ │
│  │  │              │  │              │  │              │                  │ │
│  │  │  Data Center │  │  Data Center │  │  Data Center │                  │ │
│  │  │  (isolated)  │  │  (isolated)  │  │  (isolated)  │                  │ │
│  │  └──────────────┘  └──────────────┘  └──────────────┘                  │ │
│  │                          │                                              │ │
│  │                  High-speed private network                             │ │
│  └────────────────────────────────────────────────────────────────────────┘ │
│                                                                              │
│  EDGE LOCATIONS (200+ worldwide)                                            │
│  - CloudFront CDN - cache content close to users                            │
│  - Route 53 DNS                                                             │
│  - AWS WAF                                                                  │
└─────────────────────────────────────────────────────────────────────────────┘

KEY CONCEPTS:
- Regions: 30+ regions worldwide
- AZs: 2-6 AZs per region (deploy across for HA)
- Data stays in region unless you move it
- Some services are global (IAM, Route53, CloudFront)
"""

# ═══════════════════════════════════════════════════════════════════════════════
# SECTION 2: CORE SERVICES OVERVIEW
# ═══════════════════════════════════════════════════════════════════════════════

AWS_SERVICES = {
    # ─────────────────────────────────────────────────────────────────────────
    # COMPUTE
    # ─────────────────────────────────────────────────────────────────────────
    "EC2": {
        "what": "Virtual servers in the cloud",
        "use_cases": ["Web servers", "App servers", "Batch processing"],
        "key_concepts": [
            "Instance Types (t3.micro, m5.large, c5.xlarge)",
            "AMI (Amazon Machine Image) - OS template",
            "Security Groups - firewall",
            "Key Pairs - SSH access",
            "EBS volumes - storage"
        ],
        "pricing": "On-Demand, Reserved, Spot Instances"
    },
    
    "EKS": {
        "what": "Managed Kubernetes",
        "use_cases": ["Container orchestration", "Microservices"],
        "key_concepts": [
            "Control plane managed by AWS",
            "Worker nodes in your VPC",
            "Integrates with ALB, IAM, CloudWatch"
        ],
        "pricing": "$0.10/hour for control plane + EC2 costs"
    },
    
    "Lambda": {
        "what": "Serverless compute - run code without servers",
        "use_cases": ["API backends", "Event processing", "Scheduled tasks"],
        "key_concepts": [
            "Pay per invocation (not idle time)",
            "Automatic scaling",
            "15 min max execution time",
            "Triggered by events (API Gateway, S3, SQS)"
        ],
        "pricing": "First 1M requests/month FREE"
    },
    
    # ─────────────────────────────────────────────────────────────────────────
    # STORAGE
    # ─────────────────────────────────────────────────────────────────────────
    "S3": {
        "what": "Object storage - unlimited scalability",
        "use_cases": ["Static assets", "Backups", "Data lake", "Static websites"],
        "key_concepts": [
            "Buckets - containers for objects",
            "Objects - files up to 5TB",
            "Storage classes (Standard, IA, Glacier)",
            "Lifecycle policies - auto-archive",
            "Versioning - keep file history"
        ],
        "pricing": "~$0.023/GB/month (Standard)"
    },
    
    "EBS": {
        "what": "Block storage - like a hard drive for EC2",
        "use_cases": ["OS volumes", "Databases", "High IOPS apps"],
        "key_concepts": [
            "Attached to single EC2 instance",
            "Types: gp3 (SSD), io2 (high IOPS), st1 (HDD)",
            "Snapshots for backup",
            "Encryption available"
        ]
    },
    
    # ─────────────────────────────────────────────────────────────────────────
    # DATABASE
    # ─────────────────────────────────────────────────────────────────────────
    "RDS": {
        "what": "Managed relational databases",
        "engines": ["PostgreSQL", "MySQL", "MariaDB", "Oracle", "SQL Server"],
        "key_concepts": [
            "Automated backups",
            "Multi-AZ for high availability",
            "Read replicas for scaling reads",
            "Automatic patching"
        ],
        "when_to_use": "Structured data, transactions, joins"
    },
    
    "DynamoDB": {
        "what": "Managed NoSQL database",
        "key_concepts": [
            "Key-value and document store",
            "Single-digit millisecond latency",
            "Auto-scaling",
            "Global tables for multi-region"
        ],
        "when_to_use": "High scale, simple queries, flexible schema"
    },
    
    "ElastiCache": {
        "what": "Managed Redis/Memcached",
        "use_cases": ["Session storage", "Caching", "Real-time analytics"],
        "key_concepts": [
            "In-memory caching",
            "Sub-millisecond latency",
            "Cluster mode for scaling"
        ]
    },
    
    # ─────────────────────────────────────────────────────────────────────────
    # NETWORKING
    # ─────────────────────────────────────────────────────────────────────────
    "VPC": {
        "what": "Virtual Private Cloud - your own network",
        "components": [
            "Subnets (public/private)",
            "Route Tables",
            "Internet Gateway (public access)",
            "NAT Gateway (private subnet internet)",
            "Security Groups (instance firewall)",
            "NACLs (subnet firewall)"
        ]
    },
    
    "ALB": {
        "what": "Application Load Balancer - HTTP/HTTPS",
        "features": [
            "Path-based routing",
            "Host-based routing",
            "WebSocket support",
            "SSL termination",
            "Integrates with EKS"
        ]
    }
}

