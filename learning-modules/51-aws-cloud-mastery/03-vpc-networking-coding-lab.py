"""
═══════════════════════════════════════════════════════════════════════════════
🏆 AWS VPC & NETWORKING MASTERY
═══════════════════════════════════════════════════════════════════════════════

MODULE: 51-aws-cloud-mastery
LESSON: 03 - VPC, Subnets, and Network Architecture

VPC = Virtual Private Cloud
Your own isolated network in AWS
═══════════════════════════════════════════════════════════════════════════════
"""

# ═══════════════════════════════════════════════════════════════════════════════
# VPC ARCHITECTURE DIAGRAM
# ═══════════════════════════════════════════════════════════════════════════════

VPC_ARCHITECTURE = """
┌─────────────────────────────────────────────────────────────────────────────┐
│                              AWS REGION                                      │
│  ┌───────────────────────────────────────────────────────────────────────┐  │
│  │                    VPC (10.0.0.0/16)                                   │  │
│  │                                                                        │  │
│  │  ┌─────────────────────────────┐  ┌─────────────────────────────┐     │  │
│  │  │     AVAILABILITY ZONE A     │  │     AVAILABILITY ZONE B     │     │  │
│  │  │                             │  │                             │     │  │
│  │  │  ┌───────────────────────┐  │  │  ┌───────────────────────┐  │     │  │
│  │  │  │  PUBLIC SUBNET        │  │  │  │  PUBLIC SUBNET        │  │     │  │
│  │  │  │  10.0.1.0/24          │  │  │  │  10.0.2.0/24          │  │     │  │
│  │  │  │  ┌─────┐ ┌─────┐      │  │  │  │  ┌─────┐              │  │     │  │
│  │  │  │  │ ALB │ │ NAT │      │  │  │  │  │ ALB │              │  │     │  │
│  │  │  │  └─────┘ └─────┘      │  │  │  │  └─────┘              │  │     │  │
│  │  │  └───────────────────────┘  │  │  └───────────────────────┘  │     │  │
│  │  │           │                 │  │           │                 │     │  │
│  │  │  ┌───────────────────────┐  │  │  ┌───────────────────────┐  │     │  │
│  │  │  │  PRIVATE SUBNET       │  │  │  │  PRIVATE SUBNET       │  │     │  │
│  │  │  │  10.0.10.0/24         │  │  │  │  10.0.20.0/24         │  │     │  │
│  │  │  │  ┌─────┐ ┌─────┐      │  │  │  │  ┌─────┐ ┌─────┐      │  │     │  │
│  │  │  │  │ EKS │ │ EKS │      │  │  │  │  │ EKS │ │ EKS │      │  │     │  │
│  │  │  │  │Node │ │Node │      │  │  │  │  │Node │ │Node │      │  │     │  │
│  │  │  │  └─────┘ └─────┘      │  │  │  │  └─────┘ └─────┘      │  │     │  │
│  │  │  └───────────────────────┘  │  │  └───────────────────────┘  │     │  │
│  │  │           │                 │  │           │                 │     │  │
│  │  │  ┌───────────────────────┐  │  │  ┌───────────────────────┐  │     │  │
│  │  │  │  DATABASE SUBNET      │  │  │  │  DATABASE SUBNET      │  │     │  │
│  │  │  │  10.0.100.0/24        │  │  │  │  10.0.200.0/24        │  │     │  │
│  │  │  │  ┌─────┐ ┌─────┐      │  │  │  │  ┌─────┐              │  │     │  │
│  │  │  │  │ RDS │ │Redis│      │  │  │  │  │ RDS │ (standby)    │  │     │  │
│  │  │  │  └─────┘ └─────┘      │  │  │  │  └─────┘              │  │     │  │
│  │  │  └───────────────────────┘  │  │  └───────────────────────┘  │     │  │
│  │  └─────────────────────────────┘  └─────────────────────────────┘     │  │
│  │                                                                        │  │
│  │  ┌──────────────────┐                                                  │  │
│  │  │ Internet Gateway │ ←── Public internet access                       │  │
│  │  └──────────────────┘                                                  │  │
│  └───────────────────────────────────────────────────────────────────────┘  │
└─────────────────────────────────────────────────────────────────────────────┘
"""

# ═══════════════════════════════════════════════════════════════════════════════
# VPC COMPONENTS
# ═══════════════════════════════════════════════════════════════════════════════

VPC_COMPONENTS = {
    "VPC": {
        "what": "Your isolated network in AWS",
        "cidr": "10.0.0.0/16 = 65,536 IP addresses",
        "key_points": [
            "One VPC per region",
            "Can peer VPCs together",
            "DNS resolution enabled by default"
        ]
    },
    
    "Subnets": {
        "public": {
            "what": "Has route to Internet Gateway",
            "use_for": ["Load balancers", "Bastion hosts", "NAT Gateway"],
            "example_cidr": "10.0.1.0/24 (256 IPs)"
        },
        "private": {
            "what": "No direct internet access",
            "use_for": ["Application servers", "EKS nodes"],
            "internet_via": "NAT Gateway"
        },
        "database": {
            "what": "Isolated, no internet access",
            "use_for": ["RDS", "ElastiCache"],
            "access": "Only from private subnets"
        }
    },
    
    "Internet_Gateway": {
        "what": "Allows VPC to communicate with internet",
        "key_points": [
            "One per VPC",
            "Horizontally scaled, redundant",
            "No bandwidth constraints"
        ]
    },
    
    "NAT_Gateway": {
        "what": "Allows private subnets to reach internet",
        "use_case": "Private instances need to download updates",
        "key_points": [
            "Lives in public subnet",
            "One per AZ for HA",
            "Costs ~$32/month + data transfer"
        ]
    },
    
    "Route_Tables": {
        "what": "Rules for where traffic goes",
        "public_subnet_routes": [
            "10.0.0.0/16 → local (within VPC)",
            "0.0.0.0/0 → Internet Gateway"
        ],
        "private_subnet_routes": [
            "10.0.0.0/16 → local",
            "0.0.0.0/0 → NAT Gateway"
        ]
    }
}

# ═══════════════════════════════════════════════════════════════════════════════
# CIDR NOTATION CHEAT SHEET
# ═══════════════════════════════════════════════════════════════════════════════

CIDR_CHEATSHEET = """
┌─────────────────────────────────────────────────────────────────────────────┐
│                         CIDR NOTATION CHEAT SHEET                            │
├─────────────────────────────────────────────────────────────────────────────┤
│  CIDR           │  Subnet Mask      │  # of IPs    │  Use Case              │
├─────────────────┼───────────────────┼──────────────┼────────────────────────┤
│  /8             │  255.0.0.0        │  16,777,216  │  Huge networks         │
│  /16            │  255.255.0.0      │  65,536      │  VPC (recommended)     │
│  /20            │  255.255.240.0    │  4,096       │  Large subnet          │
│  /24            │  255.255.255.0    │  256         │  Standard subnet       │
│  /28            │  255.255.255.240  │  16          │  Small subnet          │
│  /32            │  255.255.255.255  │  1           │  Single host           │
├─────────────────────────────────────────────────────────────────────────────┤
│  AWS reserves 5 IPs per subnet:                                              │
│  - .0 = Network address                                                      │
│  - .1 = VPC router                                                           │
│  - .2 = DNS server                                                           │
│  - .3 = Reserved for future                                                  │
│  - .255 = Broadcast (not used but reserved)                                  │
│                                                                              │
│  So /24 subnet = 256 - 5 = 251 usable IPs                                   │
└─────────────────────────────────────────────────────────────────────────────┘
"""

# ═══════════════════════════════════════════════════════════════════════════════
# AWS CLI COMMANDS FOR VPC
# ═══════════════════════════════════════════════════════════════════════════════

AWS_CLI_VPC = {
    "aws ec2 describe-vpcs": "List all VPCs",
    "aws ec2 describe-subnets": "List all subnets",
    "aws ec2 describe-route-tables": "List route tables",
    "aws ec2 describe-security-groups": "List security groups",
    "aws ec2 describe-nat-gateways": "List NAT gateways",
    "aws ec2 create-vpc --cidr-block 10.0.0.0/16": "Create VPC",
    "aws ec2 create-subnet --vpc-id <id> --cidr-block 10.0.1.0/24": "Create subnet",
}

