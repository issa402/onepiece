# ═══════════════════════════════════════════════════════════════════════════════
# 🏆 FANZONE CONNECT - S3 CONFIGURATION
# ═══════════════════════════════════════════════════════════════════════════════
#
# PURPOSE:
# S3 buckets for static assets, user uploads, backups, and logs.
#
# BUCKETS FOR FANZONE:
# - Static assets (team logos, stadium images)
# - User uploads (profile pictures)
# - Database backups
# - Application logs
# - Terraform state (already configured in main.tf)
# ═══════════════════════════════════════════════════════════════════════════════

# ─────────────────────────────────────────────────────────────────────────────
# STATIC ASSETS BUCKET
# ─────────────────────────────────────────────────────────────────────────────
# TODO: resource "aws_s3_bucket" "static_assets" {
#         bucket = "${var.project_name}-static-assets-${data.aws_caller_identity.current.account_id}"
#         
#         tags = {
#           Name = "${var.project_name}-static-assets"
#         }
#       }
#       
#       resource "aws_s3_bucket_public_access_block" "static_assets" {
#         bucket = aws_s3_bucket.static_assets.id
#         
#         block_public_acls       = false  # Allow public read for CDN
#         block_public_policy     = false
#         ignore_public_acls      = false
#         restrict_public_buckets = false
#       }
#       
#       resource "aws_s3_bucket_policy" "static_assets" {
#         bucket = aws_s3_bucket.static_assets.id
#         policy = jsonencode({
#           Version = "2012-10-17"
#           Statement = [{
#             Sid       = "PublicReadGetObject"
#             Effect    = "Allow"
#             Principal = "*"
#             Action    = "s3:GetObject"
#             Resource  = "${aws_s3_bucket.static_assets.arn}/*"
#           }]
#         })
#       }

# ─────────────────────────────────────────────────────────────────────────────
# USER UPLOADS BUCKET (private)
# ─────────────────────────────────────────────────────────────────────────────
# TODO: resource "aws_s3_bucket" "user_uploads" {
#         bucket = "${var.project_name}-user-uploads-${data.aws_caller_identity.current.account_id}"
#       }
#       
#       resource "aws_s3_bucket_public_access_block" "user_uploads" {
#         bucket = aws_s3_bucket.user_uploads.id
#         
#         block_public_acls       = true
#         block_public_policy     = true
#         ignore_public_acls      = true
#         restrict_public_buckets = true
#       }
#       
#       resource "aws_s3_bucket_server_side_encryption_configuration" "user_uploads" {
#         bucket = aws_s3_bucket.user_uploads.id
#         
#         rule {
#           apply_server_side_encryption_by_default {
#             sse_algorithm = "AES256"
#           }
#         }
#       }

# ─────────────────────────────────────────────────────────────────────────────
# BACKUPS BUCKET
# ─────────────────────────────────────────────────────────────────────────────
# TODO: resource "aws_s3_bucket" "backups" {
#         bucket = "${var.project_name}-backups-${data.aws_caller_identity.current.account_id}"
#       }
#       
#       resource "aws_s3_bucket_lifecycle_configuration" "backups" {
#         bucket = aws_s3_bucket.backups.id
#         
#         rule {
#           id     = "expire-old-backups"
#           status = "Enabled"
#           
#           transition {
#             days          = 30
#             storage_class = "STANDARD_IA"  # Cheaper after 30 days
#           }
#           
#           transition {
#             days          = 90
#             storage_class = "GLACIER"  # Archive after 90 days
#           }
#           
#           expiration {
#             days = 365  # Delete after 1 year
#           }
#         }
#       }

# ─────────────────────────────────────────────────────────────────────────────
# CLOUDFRONT CDN (for static assets)
# ─────────────────────────────────────────────────────────────────────────────
# TODO: resource "aws_cloudfront_distribution" "static_assets" {
#         origin {
#           domain_name = aws_s3_bucket.static_assets.bucket_regional_domain_name
#           origin_id   = "S3-${aws_s3_bucket.static_assets.id}"
#         }
#         
#         enabled             = true
#         default_root_object = "index.html"
#         
#         default_cache_behavior {
#           allowed_methods  = ["GET", "HEAD"]
#           cached_methods   = ["GET", "HEAD"]
#           target_origin_id = "S3-${aws_s3_bucket.static_assets.id}"
#           
#           forwarded_values {
#             query_string = false
#             cookies { forward = "none" }
#           }
#           
#           viewer_protocol_policy = "redirect-to-https"
#         }
#         
#         restrictions {
#           geo_restriction { restriction_type = "none" }
#         }
#         
#         viewer_certificate {
#           cloudfront_default_certificate = true
#         }
#       }

