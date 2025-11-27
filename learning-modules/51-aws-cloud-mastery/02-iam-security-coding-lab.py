"""
═══════════════════════════════════════════════════════════════════════════════
🏆 AWS IAM & SECURITY MASTERY
═══════════════════════════════════════════════════════════════════════════════

MODULE: 51-aws-cloud-mastery
LESSON: 02 - IAM, Security Groups, and Best Practices

IAM = Identity and Access Management
Controls WHO can do WHAT in your AWS account
═══════════════════════════════════════════════════════════════════════════════
"""

# ═══════════════════════════════════════════════════════════════════════════════
# IAM FUNDAMENTALS
# ═══════════════════════════════════════════════════════════════════════════════

IAM_COMPONENTS = {
    "Users": {
        "what": "Individual people or services",
        "best_practices": [
            "One user per person (no sharing)",
            "Use strong passwords + MFA",
            "Don't use root account for daily work",
            "Rotate access keys regularly"
        ]
    },
    
    "Groups": {
        "what": "Collection of users with same permissions",
        "examples": ["Developers", "Admins", "ReadOnly"],
        "best_practice": "Assign permissions to groups, not users"
    },
    
    "Roles": {
        "what": "Temporary permissions for AWS services",
        "use_cases": [
            "EC2 instance accessing S3",
            "Lambda function accessing DynamoDB",
            "Cross-account access",
            "EKS pods (IRSA)"
        ],
        "best_practice": "Use roles instead of access keys when possible"
    },
    
    "Policies": {
        "what": "JSON documents defining permissions",
        "types": [
            "AWS Managed - created by AWS",
            "Customer Managed - created by you",
            "Inline - embedded in user/group/role"
        ]
    }
}

# ═══════════════════════════════════════════════════════════════════════════════
# IAM POLICY STRUCTURE
# ═══════════════════════════════════════════════════════════════════════════════

POLICY_EXAMPLE = """
{
    "Version": "2012-10-17",
    "Statement": [
        {
            "Sid": "AllowS3ReadAccess",
            "Effect": "Allow",           // Allow or Deny
            "Action": [                  // What actions
                "s3:GetObject",
                "s3:ListBucket"
            ],
            "Resource": [                // On what resources
                "arn:aws:s3:::fanzone-bucket",
                "arn:aws:s3:::fanzone-bucket/*"
            ],
            "Condition": {               // Under what conditions (optional)
                "IpAddress": {
                    "aws:SourceIp": "10.0.0.0/8"
                }
            }
        }
    ]
}
"""

# ═══════════════════════════════════════════════════════════════════════════════
# COMMON IAM POLICIES
# ═══════════════════════════════════════════════════════════════════════════════

COMMON_POLICIES = {
    "AdministratorAccess": "Full access to everything (dangerous!)",
    "PowerUserAccess": "Full access except IAM",
    "ReadOnlyAccess": "Read-only to all services",
    "AmazonS3FullAccess": "Full S3 access",
    "AmazonEC2FullAccess": "Full EC2 access",
    "AmazonEKSClusterPolicy": "EKS cluster permissions",
}

# ═══════════════════════════════════════════════════════════════════════════════
# SECURITY GROUPS VS NACLs
# ═══════════════════════════════════════════════════════════════════════════════

SECURITY_COMPARISON = """
┌─────────────────────────────────────────────────────────────────────────────┐
│           SECURITY GROUPS           │              NACLs                    │
├─────────────────────────────────────┼───────────────────────────────────────┤
│ Instance level (EC2, RDS)           │ Subnet level                          │
│ Stateful (return traffic auto)      │ Stateless (must allow both ways)      │
│ Allow rules only                    │ Allow AND Deny rules                  │
│ All rules evaluated                 │ Rules evaluated in order              │
│ Must be explicitly attached         │ Auto-applied to all in subnet         │
└─────────────────────────────────────┴───────────────────────────────────────┘

SECURITY GROUP EXAMPLE (FANZONE API):
┌────────────────────────────────────────────────────────────────────────────┐
│ Inbound Rules:                                                              │
│   Port 443  │ Source: 0.0.0.0/0        │ HTTPS from anywhere               │
│   Port 22   │ Source: 10.0.0.0/8       │ SSH from VPC only                 │
│                                                                             │
│ Outbound Rules:                                                             │
│   All       │ Destination: 0.0.0.0/0   │ Allow all outbound                │
└────────────────────────────────────────────────────────────────────────────┘
"""

# ═══════════════════════════════════════════════════════════════════════════════
# AWS SECURITY BEST PRACTICES
# ═══════════════════════════════════════════════════════════════════════════════

SECURITY_BEST_PRACTICES = """
┌─────────────────────────────────────────────────────────────────────────────┐
│                    AWS SECURITY BEST PRACTICES                               │
├─────────────────────────────────────────────────────────────────────────────┤
│                                                                              │
│ 1. ROOT ACCOUNT                                                             │
│    ✓ Enable MFA immediately                                                 │
│    ✓ Never use for daily tasks                                              │
│    ✓ Delete access keys if they exist                                       │
│    ✓ Use only for billing and account-level tasks                          │
│                                                                              │
│ 2. LEAST PRIVILEGE                                                          │
│    ✓ Give minimum permissions needed                                        │
│    ✓ Start with zero permissions, add as needed                            │
│    ✓ Use AWS Access Analyzer to find unused permissions                    │
│    ✓ Regular permission audits                                              │
│                                                                              │
│ 3. USE ROLES, NOT ACCESS KEYS                                               │
│    ✓ EC2 instances should use Instance Profiles                            │
│    ✓ Lambda functions should use Execution Roles                           │
│    ✓ EKS pods should use IRSA (IAM Roles for Service Accounts)            │
│                                                                              │
│ 4. ENABLE CLOUDTRAIL                                                        │
│    ✓ Log all API calls                                                      │
│    ✓ Store logs in S3 with encryption                                       │
│    ✓ Enable log file validation                                             │
│                                                                              │
│ 5. ENCRYPTION                                                               │
│    ✓ Encrypt data at rest (S3, EBS, RDS)                                   │
│    ✓ Encrypt data in transit (HTTPS, TLS)                                  │
│    ✓ Use KMS for key management                                             │
│                                                                              │
│ 6. NETWORK SECURITY                                                         │
│    ✓ Use VPCs for isolation                                                 │
│    ✓ Private subnets for databases                                          │
│    ✓ Security groups with minimal access                                    │
│    ✓ VPC Flow Logs for monitoring                                           │
│                                                                              │
│ 7. MONITORING & ALERTING                                                    │
│    ✓ CloudWatch alarms for suspicious activity                             │
│    ✓ AWS Config for compliance                                              │
│    ✓ GuardDuty for threat detection                                        │
│    ✓ Security Hub for centralized view                                      │
└─────────────────────────────────────────────────────────────────────────────┘
"""

# ═══════════════════════════════════════════════════════════════════════════════
# AWS CLI COMMANDS FOR IAM
# ═══════════════════════════════════════════════════════════════════════════════

AWS_CLI_IAM = {
    "aws iam list-users": "List all users",
    "aws iam list-roles": "List all roles",
    "aws iam get-user": "Get current user info",
    "aws iam create-user --user-name <name>": "Create user",
    "aws iam attach-user-policy --user-name <name> --policy-arn <arn>": "Attach policy",
    "aws iam create-role --role-name <name> --assume-role-policy-document file://trust.json": "Create role",
    "aws sts get-caller-identity": "Who am I?",
    "aws iam simulate-principal-policy": "Test if action is allowed",
}

