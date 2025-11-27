# 🏆 FANZONE CONNECT - Terraform & Cloud Infrastructure Guide

## What is Terraform?

Terraform is Infrastructure as Code (IaC). Instead of clicking buttons in AWS console, you write code that creates infrastructure.

**Benefits:**
- Version control your infrastructure (git)
- Reproducible environments
- Review infra changes like code reviews
- Destroy everything cleanly

## Why Cloud (AWS) for FANZONE?

- **Global scale** - serve fans worldwide
- **Managed services** - AWS handles database backups, patching
- **Auto-scaling** - handle World Cup traffic spikes
- **High availability** - multi-region, multi-AZ

## FANZONE AWS Architecture

```
┌─────────────────────────────────────────────────────────────────┐
│  AWS Cloud                                                       │
│  ┌─────────────────────────────────────────────────────────────┐│
│  │  VPC (10.0.0.0/16)                                          ││
│  │  ┌─────────────────────┐  ┌─────────────────────┐           ││
│  │  │  Public Subnet      │  │  Public Subnet      │           ││
│  │  │  - ALB              │  │  - NAT Gateway      │           ││
│  │  │  - Bastion Host     │  │                     │           ││
│  │  └─────────────────────┘  └─────────────────────┘           ││
│  │  ┌─────────────────────┐  ┌─────────────────────┐           ││
│  │  │  Private Subnet     │  │  Private Subnet     │           ││
│  │  │  - EKS Nodes        │  │  - EKS Nodes        │           ││
│  │  │  - RDS (primary)    │  │  - RDS (standby)    │           ││
│  │  │  - ElastiCache      │  │  - ElastiCache      │           ││
│  │  └─────────────────────┘  └─────────────────────┘           ││
│  └─────────────────────────────────────────────────────────────┘│
│                                                                  │
│  ┌──────────┐  ┌──────────┐  ┌──────────┐  ┌──────────┐        │
│  │    S3    │  │CloudFront│  │  Route53 │  │   IAM    │        │
│  │ (assets) │  │  (CDN)   │  │  (DNS)   │  │ (access) │        │
│  └──────────┘  └──────────┘  └──────────┘  └──────────┘        │
└─────────────────────────────────────────────────────────────────┘
```

## Files in `terraform/` Directory

| File | Purpose |
|------|---------|
| `main.tf` | Provider config, backend, module calls |
| `variables.tf` | Input variables (region, instance types) |
| `outputs.tf` | Output values (endpoints, connection strings) |
| `vpc.tf` | Network - VPC, subnets, gateways |
| `eks.tf` | Kubernetes cluster |
| `rds.tf` | PostgreSQL database |
| `elasticache.tf` | Redis cache |
| `s3.tf` | Storage buckets, CDN |

## AWS Services for FANZONE

### 1. VPC (Virtual Private Cloud)
Your own isolated network in AWS.
```hcl
resource "aws_vpc" "main" {
  cidr_block = "10.0.0.0/16"
  # 65,536 IP addresses
}
```

### 2. EKS (Elastic Kubernetes Service)
Managed Kubernetes - AWS runs the control plane.
```hcl
resource "aws_eks_cluster" "main" {
  name    = "fanzone-prod"
  version = "1.28"
}
```

### 3. RDS (Relational Database Service)
Managed PostgreSQL - automatic backups, failover.
```hcl
resource "aws_db_instance" "main" {
  engine         = "postgres"
  instance_class = "db.t3.medium"
  multi_az       = true  # High availability
}
```

### 4. ElastiCache
Managed Redis - caching, sessions, pub/sub.
```hcl
resource "aws_elasticache_cluster" "main" {
  engine         = "redis"
  node_type      = "cache.t3.micro"
}
```

### 5. S3 + CloudFront
Static assets with global CDN.
```hcl
resource "aws_s3_bucket" "static" {
  bucket = "fanzone-static-assets"
}

resource "aws_cloudfront_distribution" "cdn" {
  origin {
    domain_name = aws_s3_bucket.static.bucket_domain_name
  }
}
```

## Terraform Commands

```bash
# Initialize (download providers)
terraform init

# Preview changes
terraform plan

# Apply changes
terraform apply

# Destroy everything
terraform destroy

# Format code
terraform fmt

# Validate syntax
terraform validate
```

## Environment Management

```bash
# Different tfvars for each environment
terraform apply -var-file="environments/dev.tfvars"
terraform apply -var-file="environments/prod.tfvars"
```

## Cost Estimation (FANZONE Dev Environment)

| Service | Monthly Cost |
|---------|-------------|
| EKS Cluster | ~$73 |
| 2x t3.medium nodes | ~$60 |
| RDS db.t3.medium | ~$50 |
| ElastiCache t3.micro | ~$12 |
| S3 + CloudFront | ~$5 |
| **Total** | **~$200/mo** |

*Production with HA would be ~$500-1000/mo*

## What This Teaches You

| Skill | Where It's Used |
|-------|-----------------|
| Infrastructure as Code | All Terraform files |
| AWS Networking | VPC, subnets, security groups |
| Managed Kubernetes | EKS configuration |
| Database Management | RDS setup, backups |
| Caching Strategies | ElastiCache/Redis |
| CDN/Storage | S3, CloudFront |
| Security | IAM, encryption, VPC isolation |
| Cost Optimization | Instance sizing, lifecycle policies |

## Next Steps

1. **Get AWS Free Tier** account
2. **Study each .tf file** - understand resources
3. **Run `terraform plan`** to see what would be created
4. **Deploy to AWS** (start with dev environment)
5. **Learn AWS Console** - see resources visually
6. **Get AWS certifications** (Solutions Architect)

