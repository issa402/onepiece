# ═══════════════════════════════════════════════════════════════════════════════
# 🏆 FANZONE CONNECT - RDS (Relational Database Service) CONFIGURATION
# ═══════════════════════════════════════════════════════════════════════════════
#
# PURPOSE:
# Creates a managed PostgreSQL database on AWS.
# AWS handles backups, patches, failover - you just use it.
#
# FEATURES:
# - Automated backups
# - Multi-AZ for high availability
# - Encryption at rest
# - Automatic minor version upgrades
#
# USAGE:
#   terraform apply
#   # Connection string in outputs
# ═══════════════════════════════════════════════════════════════════════════════

# ─────────────────────────────────────────────────────────────────────────────
# DB SUBNET GROUP
# ─────────────────────────────────────────────────────────────────────────────
# TODO: resource "aws_db_subnet_group" "main" {
#         name       = "${var.project_name}-db-subnet"
#         subnet_ids = aws_subnet.private[*].id
#         
#         tags = {
#           Name = "${var.project_name}-db-subnet-group"
#         }
#       }

# ─────────────────────────────────────────────────────────────────────────────
# SECURITY GROUP FOR RDS
# ─────────────────────────────────────────────────────────────────────────────
# TODO: resource "aws_security_group" "rds" {
#         name        = "${var.project_name}-rds-sg"
#         description = "Security group for RDS PostgreSQL"
#         vpc_id      = aws_vpc.main.id
#         
#         ingress {
#           from_port       = 5432
#           to_port         = 5432
#           protocol        = "tcp"
#           security_groups = [aws_security_group.eks_nodes.id]  # Only from EKS
#         }
#         
#         egress {
#           from_port   = 0
#           to_port     = 0
#           protocol    = "-1"
#           cidr_blocks = ["0.0.0.0/0"]
#         }
#       }

# ─────────────────────────────────────────────────────────────────────────────
# RDS PARAMETER GROUP (PostgreSQL tuning)
# ─────────────────────────────────────────────────────────────────────────────
# TODO: resource "aws_db_parameter_group" "main" {
#         family = "postgres15"
#         name   = "${var.project_name}-pg-params"
#         
#         parameter {
#           name  = "log_statement"
#           value = "all"
#         }
#         
#         parameter {
#           name  = "log_min_duration_statement"
#           value = "1000"  # Log queries > 1 second
#         }
#       }

# ─────────────────────────────────────────────────────────────────────────────
# RDS INSTANCE
# ─────────────────────────────────────────────────────────────────────────────
# TODO: resource "aws_db_instance" "main" {
#         identifier     = "${var.project_name}-postgres"
#         engine         = "postgres"
#         engine_version = "15.4"
#         
#         instance_class    = var.db_instance_class
#         allocated_storage = var.db_allocated_storage
#         storage_type      = "gp3"
#         storage_encrypted = true
#         
#         db_name  = var.db_name
#         username = var.db_username
#         password = var.db_password
#         
#         db_subnet_group_name   = aws_db_subnet_group.main.name
#         vpc_security_group_ids = [aws_security_group.rds.id]
#         parameter_group_name   = aws_db_parameter_group.main.name
#         
#         multi_az               = var.environment == "prod" ? true : false
#         publicly_accessible    = false
#         skip_final_snapshot    = var.environment != "prod"
#         deletion_protection    = var.environment == "prod"
#         
#         backup_retention_period = 7
#         backup_window          = "03:00-04:00"
#         maintenance_window     = "Mon:04:00-Mon:05:00"
#         
#         auto_minor_version_upgrade = true
#         
#         performance_insights_enabled = true
#         
#         tags = {
#           Name = "${var.project_name}-postgres"
#         }
#       }

# ─────────────────────────────────────────────────────────────────────────────
# SECRETS MANAGER (store credentials securely)
# ─────────────────────────────────────────────────────────────────────────────
# TODO: resource "aws_secretsmanager_secret" "db_credentials" {
#         name = "${var.project_name}/db-credentials"
#       }
#       
#       resource "aws_secretsmanager_secret_version" "db_credentials" {
#         secret_id = aws_secretsmanager_secret.db_credentials.id
#         secret_string = jsonencode({
#           username = var.db_username
#           password = var.db_password
#           host     = aws_db_instance.main.address
#           port     = 5432
#           database = var.db_name
#         })
#       }

