# ═══════════════════════════════════════════════════════════════════════════════
# 🏆 FANZONE CONNECT - EKS (Elastic Kubernetes Service) CONFIGURATION
# ═══════════════════════════════════════════════════════════════════════════════
#
# PURPOSE:
# Creates a managed Kubernetes cluster on AWS.
# AWS handles control plane, you just deploy your apps.
#
# COMPONENTS:
# - EKS Cluster (control plane - managed by AWS)
# - Node Group (worker nodes - EC2 instances)
# - IAM Roles (permissions for cluster and nodes)
# - OIDC Provider (for IAM roles for service accounts)
#
# USAGE:
#   terraform apply
#   aws eks update-kubeconfig --name fanzone-prod --region us-east-1
#   kubectl get nodes
# ═══════════════════════════════════════════════════════════════════════════════

# ─────────────────────────────────────────────────────────────────────────────
# IAM ROLE FOR EKS CLUSTER
# ─────────────────────────────────────────────────────────────────────────────
# TODO: resource "aws_iam_role" "eks_cluster" {
#         name = "${var.project_name}-eks-cluster-role"
#         
#         assume_role_policy = jsonencode({
#           Version = "2012-10-17"
#           Statement = [{
#             Action = "sts:AssumeRole"
#             Effect = "Allow"
#             Principal = {
#               Service = "eks.amazonaws.com"
#             }
#           }]
#         })
#       }
#       
#       resource "aws_iam_role_policy_attachment" "eks_cluster_policy" {
#         policy_arn = "arn:aws:iam::aws:policy/AmazonEKSClusterPolicy"
#         role       = aws_iam_role.eks_cluster.name
#       }

# ─────────────────────────────────────────────────────────────────────────────
# EKS CLUSTER
# ─────────────────────────────────────────────────────────────────────────────
# TODO: resource "aws_eks_cluster" "main" {
#         name     = local.cluster_name
#         role_arn = aws_iam_role.eks_cluster.arn
#         version  = var.eks_cluster_version
#         
#         vpc_config {
#           subnet_ids              = aws_subnet.private[*].id
#           endpoint_private_access = true
#           endpoint_public_access  = true
#           security_group_ids      = [aws_security_group.eks_cluster.id]
#         }
#         
#         enabled_cluster_log_types = ["api", "audit", "authenticator"]
#         
#         depends_on = [
#           aws_iam_role_policy_attachment.eks_cluster_policy
#         ]
#       }

# ─────────────────────────────────────────────────────────────────────────────
# IAM ROLE FOR NODE GROUP
# ─────────────────────────────────────────────────────────────────────────────
# TODO: resource "aws_iam_role" "eks_nodes" {
#         name = "${var.project_name}-eks-node-role"
#         
#         assume_role_policy = jsonencode({
#           Version = "2012-10-17"
#           Statement = [{
#             Action = "sts:AssumeRole"
#             Effect = "Allow"
#             Principal = {
#               Service = "ec2.amazonaws.com"
#             }
#           }]
#         })
#       }
#       
#       # Attach required policies:
#       # - AmazonEKSWorkerNodePolicy
#       # - AmazonEKS_CNI_Policy
#       # - AmazonEC2ContainerRegistryReadOnly

# ─────────────────────────────────────────────────────────────────────────────
# EKS NODE GROUP
# ─────────────────────────────────────────────────────────────────────────────
# TODO: resource "aws_eks_node_group" "main" {
#         cluster_name    = aws_eks_cluster.main.name
#         node_group_name = "${var.project_name}-nodes"
#         node_role_arn   = aws_iam_role.eks_nodes.arn
#         subnet_ids      = aws_subnet.private[*].id
#         
#         instance_types = var.eks_node_instance_types
#         
#         scaling_config {
#           desired_size = var.eks_node_min_size
#           min_size     = var.eks_node_min_size
#           max_size     = var.eks_node_max_size
#         }
#         
#         update_config {
#           max_unavailable = 1
#         }
#         
#         labels = {
#           role = "general"
#         }
#       }

# ─────────────────────────────────────────────────────────────────────────────
# OIDC PROVIDER (for IAM Roles for Service Accounts)
# ─────────────────────────────────────────────────────────────────────────────
# TODO: Create OIDC provider for IRSA
#       This allows pods to assume IAM roles

# ─────────────────────────────────────────────────────────────────────────────
# CLUSTER ADDONS
# ─────────────────────────────────────────────────────────────────────────────
# TODO: Install addons:
#       - vpc-cni (networking)
#       - coredns (DNS)
#       - kube-proxy
#       - aws-load-balancer-controller
#       - cluster-autoscaler
#       - metrics-server

