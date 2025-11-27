# ═══════════════════════════════════════════════════════════════════════════════
# 🏆 FANZONE CONNECT - TERRAFORM VARIABLES
# ═══════════════════════════════════════════════════════════════════════════════
#
# PURPOSE:
# Define input variables for Terraform configuration.
# Allows different values for dev/staging/prod environments.
#
# USAGE:
#   terraform apply -var="environment=production"
#   terraform apply -var-file="prod.tfvars"
# ═══════════════════════════════════════════════════════════════════════════════

# ─────────────────────────────────────────────────────────────────────────────
# GENERAL VARIABLES
# ─────────────────────────────────────────────────────────────────────────────
# TODO: variable "environment" {
#         description = "Environment name (dev, staging, prod)"
#         type        = string
#         default     = "dev"
#         
#         validation {
#           condition     = contains(["dev", "staging", "prod"], var.environment)
#           error_message = "Environment must be dev, staging, or prod."
#         }
#       }

# TODO: variable "aws_region" {
#         description = "AWS region to deploy to"
#         type        = string
#         default     = "us-east-1"
#       }

# TODO: variable "project_name" {
#         description = "Project name for resource naming"
#         type        = string
#         default     = "fanzone-connect"
#       }

# ─────────────────────────────────────────────────────────────────────────────
# VPC VARIABLES
# ─────────────────────────────────────────────────────────────────────────────
# TODO: variable "vpc_cidr" {
#         description = "CIDR block for VPC"
#         type        = string
#         default     = "10.0.0.0/16"
#       }

# TODO: variable "availability_zones" {
#         description = "List of availability zones"
#         type        = list(string)
#         default     = ["us-east-1a", "us-east-1b", "us-east-1c"]
#       }

# ─────────────────────────────────────────────────────────────────────────────
# EKS VARIABLES
# ─────────────────────────────────────────────────────────────────────────────
# TODO: variable "eks_cluster_version" {
#         description = "Kubernetes version for EKS"
#         type        = string
#         default     = "1.28"
#       }

# TODO: variable "eks_node_instance_types" {
#         description = "Instance types for EKS node group"
#         type        = list(string)
#         default     = ["t3.medium"]
#       }

# TODO: variable "eks_node_min_size" {
#         description = "Minimum number of nodes"
#         type        = number
#         default     = 2
#       }

# TODO: variable "eks_node_max_size" {
#         description = "Maximum number of nodes"
#         type        = number
#         default     = 10
#       }

# ─────────────────────────────────────────────────────────────────────────────
# RDS VARIABLES
# ─────────────────────────────────────────────────────────────────────────────
# TODO: variable "db_instance_class" {
#         description = "RDS instance class"
#         type        = string
#         default     = "db.t3.medium"
#       }

# TODO: variable "db_allocated_storage" {
#         description = "Allocated storage in GB"
#         type        = number
#         default     = 50
#       }

# TODO: variable "db_name" {
#         description = "Database name"
#         type        = string
#         default     = "fanzone_db"
#       }

# TODO: variable "db_username" {
#         description = "Database master username"
#         type        = string
#         sensitive   = true
#       }

# TODO: variable "db_password" {
#         description = "Database master password"
#         type        = string
#         sensitive   = true  # Won't show in logs
#       }

# ─────────────────────────────────────────────────────────────────────────────
# REDIS VARIABLES
# ─────────────────────────────────────────────────────────────────────────────
# TODO: variable "redis_node_type" {
#         description = "ElastiCache node type"
#         type        = string
#         default     = "cache.t3.micro"
#       }

# TODO: variable "redis_num_cache_nodes" {
#         description = "Number of cache nodes"
#         type        = number
#         default     = 1
#       }

