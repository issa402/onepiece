"""
🏴‍☠️ MONITORING & OBSERVABILITY MASTERY - COMPLETE INSTRUMENTATION ENGINEERING
═══════════════════════════════════════════════════════════════════════════════

🎯 WHAT YOU'LL MASTER IN THIS LAB (ROADMAP.SH ALIGNED):
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

📚 PART 1: MONITORING FUNDAMENTALS (What & Why)
   - What observability is and why it's critical for Netflix, Uber, Google
   - Why monitoring prevents million-dollar outages and downtime
   - How instrumentation enables proactive incident response
   - What telemetry data reveals about system performance
   - Why the three pillars (metrics, logs, traces) work together

⚡ PART 2: METRICS & INSTRUMENTATION (Production Patterns)
   - Prometheus metrics collection and time-series data
   - Grafana dashboards for real-time system visualization
   - Custom metrics for business and technical KPIs
   - SLI/SLO definition and alerting strategies
   - Performance monitoring and capacity planning

🗄️ PART 3: LOGGING & TELEMETRY (Enterprise Patterns)
   - ELK Stack (Elasticsearch, Logstash, Kibana) for log management
   - Structured logging with JSON and correlation IDs
   - Log aggregation across distributed microservices
   - Error tracking and debugging workflows
   - Compliance logging and audit trails

🔒 PART 4: DISTRIBUTED TRACING (Microservices Observability)
   - Jaeger and OpenTelemetry for request tracing
   - Trace correlation across service boundaries
   - Performance bottleneck identification
   - Dependency mapping and service topology
   - Root cause analysis for complex failures

🚀 PART 5: ADVANCED OBSERVABILITY (Senior Engineer Level)
   - Custom alerting and incident response automation
   - Anomaly detection with machine learning
   - Chaos engineering and reliability testing
   - Cost optimization through observability data
   - Observability as code and GitOps workflows

💰 SALARY IMPACT: $95K → $320K+ (Observability expertise prevents million-dollar outages)
🏢 COMPANIES: Netflix, Uber, Google, all companies running at scale

📖 ROADMAP.SH BACKEND CONCEPTS COVERED:
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
✅ Monitoring (Prometheus, Grafana, metrics, alerting)
✅ Instrumentation (custom metrics, performance tracking)
✅ Telemetry (data collection, analysis, visualization)
✅ Logging (ELK Stack, structured logging, aggregation)
✅ Distributed Tracing (Jaeger, OpenTelemetry, correlation)
✅ Observability (three pillars, SLI/SLO, incident response)
✅ Performance (bottleneck identification, optimization)
✅ Reliability (SRE practices, chaos engineering, automation)

📚 WHY OBSERVABILITY = BIG MONEY:
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

🔥 DOWNTIME COSTS MILLIONS PER MINUTE:

1. AMAZON (2018):
   - Prime Day outage: 63 minutes
   - ?00 million revenue loss
   - Could have been detected/prevented with proper monitoring

2. FACEBOOK (2021):
   - 6-hour global outage
   - ?00 million revenue loss
   - Poor observability delayed root cause identification

3. CLOUDFLARE (2020):
   - 27-minute outage
   - 50% of internet affected
   - Monitoring helped identify and fix quickly

🔥 WHY COMPANIES PAY PREMIUM FOR OBSERVABILITY ENGINEERS:

1. BUSINESS IMPACT:
   - 1 minute downtime = ?,600 average loss
   - Early detection = 10x faster resolution
   - Proactive monitoring = 90% fewer incidents

2. SCALE REQUIREMENTS:
   - Netflix: 1 trillion events per day
   - Uber: 100+ microservices to monitor
   - Google: Petabytes of logs daily

3. SKILL COMPLEXITY:
   - Distributed systems expertise
   - Data analysis and visualization
   - Incident response and automation
   - Performance optimization

📖 ESSENTIAL RESOURCES:
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
🔗 Prometheus Docs: https://prometheus.io/docs/
🔗 Grafana Tutorials: https://grafana.com/tutorials/
🔗 ELK Stack Guide: https://www.elastic.co/guide/
🔗 Observability Engineering: https://www.oreilly.com/library/view/observability-engineering/9781492076438/
🔗 SRE Workbook: https://sre.google/workbook/table-of-contents/
"""

# ═══════════════════════════════════════════════════════════
# 🧪 HANDS-ON LAB 1: PROMETHEUS METRICS FOR ONE PIECE TRADING
# ═══════════════════════════════════════════════════════════

"""
📚 PROMETHEUS METRICS FOR TRADING PLATFORM:

🔥 KEY METRICS FOR ONE PIECE TRADING PLATFORM:

1. BUSINESS METRICS:
   - Total trades executed per minute
   - Revenue generated per hour
   - Active users trading
   - Character price volatility

2. TECHNICAL METRICS:
   - API response times (p50, p95, p99)
   - Database query performance
   - Error rates by endpoint
   - Memory and CPU usage

3. INFRASTRUCTURE METRICS:
   - Container resource usage
   - Network latency between services
   - Database connection pool status
   - Cache hit/miss rates

PROMETHEUS METRIC TYPES:
- Counter: Monotonically increasing (total trades)
- Gauge: Can go up/down (active users)
- Histogram: Distribution of values (response times)
- Summary: Similar to histogram with quantiles

🎯 YOUR CODING MISSION:
Instrument your One Piece platform with comprehensive metrics!
"""

# TODO 1: CREATE PROMETHEUS METRICS SERVICE
# ═══════════════════════════════════════════════════════════
"""
🎯 YOUR TASK: Create metrics collection service for One Piece platform

Create file: apps/monitoring/prometheus_metrics.py
"""

# FILE: apps/monitoring/prometheus_metrics.py
# YOUR CODE HERE - Import Prometheus client:
from prometheus_client import Counter, Gauge, Histogram, Summary, generate_latest
import time
import functools
# Add more imports...

# YOUR CODE HERE - Define One Piece trading metrics:
class OnePieceMetrics:
    """Prometheus metrics for One Piece trading platform"""
    
    def __init__(self):
        # Business Metrics
        self.trades_total = # Add counter for total trades
        self.revenue_total = # Add counter for total revenue
        self.active_users = # Add gauge for active users
        self.character_prices = # Add gauge for character prices
        
        # Technical Metrics
        self.api_request_duration = # Add histogram for API response times
        self.api_requests_total = # Add counter for API requests
        self.database_query_duration = # Add histogram for DB queries
        self.error_rate = # Add counter for errors
        
        # Infrastructure Metrics
        self.memory_usage = # Add gauge for memory usage
        self.cpu_usage = # Add gauge for CPU usage
        self.cache_hits = # Add counter for cache hits
        self.cache_misses = # Add counter for cache misses
    
    # YOUR CODE HERE - Add trade tracking:
    def record_trade(self, character_name, trade_type, amount, user_id):
        """Record a trade execution"""
        # Add trade recording logic
        pass
    
    # YOUR CODE HERE - Add API request tracking:
    def record_api_request(self, endpoint, method, status_code, duration):
        """Record API request metrics"""
        # Add API request recording logic
        pass
    
    # YOUR CODE HERE - Add database query tracking:
    def record_database_query(self, query_type, duration):
        """Record database query metrics"""
        # Add database query recording logic
        pass

# YOUR CODE HERE - Create metrics decorator:
def track_api_metrics(metrics_service):
    """Decorator to automatically track API metrics"""
    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            # Add automatic metrics tracking
            pass
        return wrapper
    return decorator

# TODO 2: CREATE CUSTOM METRICS MIDDLEWARE
# ═══════════════════════════════════════════════════════════
"""
🎯 YOUR TASK: Create Django middleware for automatic metrics collection

Create file: apps/monitoring/metrics_middleware.py
"""

# FILE: apps/monitoring/metrics_middleware.py
# YOUR CODE HERE - Create metrics middleware:


class PrometheusMetricsMiddleware:
    """Django middleware for automatic Prometheus metrics collection"""
    
    def __init__(self, get_response):
        # Add middleware initialization
        self.get_response = get_response
        self.metrics = # Add metrics service
    
    def __call__(self, request):
        # YOUR CODE HERE - Add request tracking:
        start_time = # Add start time tracking
        
        response = self.get_response(request)
        
        # YOUR CODE HERE - Add response tracking:
        duration = # Calculate request duration
        
        # Record metrics
        # Add metrics recording logic
        
        return response

# TODO 3: CREATE METRICS ENDPOINTS
# ═══════════════════════════════════════════════════════════
"""
🎯 YOUR TASK: Create endpoints for Prometheus to scrape metrics

Create file: apps/monitoring/views.py
"""

# FILE: apps/monitoring/views.py
# YOUR CODE HERE - Create metrics views:
from django.http import HttpResponse
from prometheus_client import generate_latest, CONTENT_TYPE_LATEST

def metrics_view(request):
    """Endpoint for Prometheus to scrape metrics"""
    # YOUR CODE HERE - Generate and return metrics
    pass

def health_check(request):
    """Health check endpoint for monitoring"""
    # YOUR CODE HERE - Add health check logic
    pass

def readiness_check(request):
    """Readiness check for Kubernetes"""
    # YOUR CODE HERE - Add readiness check logic
    pass

# ═══════════════════════════════════════════════════════════
# 🧪 HANDS-ON LAB 2: GRAFANA DASHBOARDS FOR TRADING ANALYTICS
# ═══════════════════════════════════════════════════════════

"""
📚 GRAFANA DASHBOARDS FOR ONE PIECE TRADING:

🔥 ESSENTIAL DASHBOARDS FOR TRADING PLATFORM:

1. BUSINESS DASHBOARD:
   - Real-time trading volume
   - Revenue trends
   - Most popular characters
   - User engagement metrics

2. TECHNICAL DASHBOARD:
   - API performance (response times, error rates)
   - Database performance
   - Infrastructure health
   - Service dependencies

3. ALERTING DASHBOARD:
   - Critical alerts status
   - SLA compliance
   - Incident response times
   - System health overview

GRAFANA QUERY EXAMPLES:
- Trading volume: rate(trades_total[5m])
- API latency: histogram_quantile(0.95, api_request_duration_bucket)
- Error rate: rate(api_requests_total{status=~"5.."}[5m])

🎯 YOUR CODING MISSION:
Create stunning Grafana dashboards for One Piece analytics!
"""

# TODO 4: CREATE GRAFANA DASHBOARD CONFIGURATION
# ═══════════════════════════════════════════════════════════
"""
🎯 YOUR TASK: Create Grafana dashboard JSON configuration

Create file: monitoring/grafana/dashboards/onepiece-business-dashboard.json
"""

# FILE: monitoring/grafana/dashboards/onepiece-business-dashboard.json
# YOUR CODE HERE - Create business dashboard JSON:
"""
{
  "dashboard": {
    "title": "🏴‍☠️ One Piece Trading - Business Metrics",
    "tags": ["onepiece", "business", "trading"],
    "panels": [
      {
        "title": "Real-time Trading Volume",
        "type": "stat",
        "targets": [
          {
            "expr": "# Add Prometheus query for trading volume"
          }
        ]
      },
      {
        "title": "Revenue Trends",
        "type": "graph",
        "targets": [
          {
            "expr": "# Add Prometheus query for revenue"
          }
        ]
      }
      // Add more panels
    ]
  }
}
"""

# TODO 5: CREATE TECHNICAL DASHBOARD
# ═══════════════════════════════════════════════════════════
"""
🎯 YOUR TASK: Create technical performance dashboard

Create file: monitoring/grafana/dashboards/onepiece-technical-dashboard.json
"""

# FILE: monitoring/grafana/dashboards/onepiece-technical-dashboard.json
# YOUR CODE HERE - Create technical dashboard JSON:
"""
{
  "dashboard": {
    "title": "🔧 One Piece Trading - Technical Metrics",
    "panels": [
      // Add technical panels
    ]
  }
}
"""

# TODO 6: CREATE ALERTING RULES
# ═══════════════════════════════════════════════════════════
"""
🎯 YOUR TASK: Create Prometheus alerting rules

Create file: monitoring/prometheus/alerts/onepiece-alerts.yml
"""

# FILE: monitoring/prometheus/alerts/onepiece-alerts.yml
# YOUR CODE HERE - Create alerting rules:
"""
groups:
- name: onepiece-trading-alerts
  rules:
  # High error rate alert
  - alert: HighErrorRate
    expr: # Add expression for high error rate
    for: # Add duration
    labels:
      severity: # Add severity
    annotations:
      summary: # Add summary
      description: # Add description
  
  # High response time alert
  - alert: HighResponseTime
    expr: # Add expression for high response time
    # Add more alert configuration
  
  # Low trading volume alert
  - alert: LowTradingVolume
    expr: # Add expression for low trading volume
    # Add more alert configuration
"""

# ═══════════════════════════════════════════════════════════
# 🧪 HANDS-ON LAB 3: ELK STACK FOR LOG MANAGEMENT
# ═══════════════════════════════════════════════════════════

"""
📚 ELK STACK FOR ONE PIECE TRADING LOGS:

🔥 ELK STACK COMPONENTS:

1. ELASTICSEARCH:
   - Distributed search and analytics engine
   - Stores and indexes all log data
   - Provides fast search capabilities

2. LOGSTASH:
   - Data processing pipeline
   - Ingests logs from multiple sources
   - Transforms and enriches log data

3. KIBANA:
   - Visualization and exploration tool
   - Creates dashboards and charts
   - Provides log search interface

LOG TYPES FOR ONE PIECE PLATFORM:
- Application logs (Django, React)
- Access logs (Nginx, API Gateway)
- Database logs (MySQL)
- Security logs (authentication, authorization)
- Trading logs (transactions, price changes)

🎯 YOUR CODING MISSION:
Set up comprehensive logging for One Piece platform!
"""

# TODO 7: CREATE STRUCTURED LOGGING SERVICE
# ═══════════════════════════════════════════════════════════
"""
🎯 YOUR TASK: Create structured logging service for One Piece

Create file: apps/monitoring/logging_service.py
"""

# FILE: apps/monitoring/logging_service.py
# YOUR CODE HERE - Import logging modules:
import logging
import json
import datetime
from django.conf import settings
# Add more imports...

# YOUR CODE HERE - Create structured logger:
class OnePieceLogger:
    """Structured logging service for One Piece trading platform"""
    
    def __init__(self):
        # Add logger configuration
        self.logger = # Add logger setup
        self.formatter = # Add JSON formatter
    
    # YOUR CODE HERE - Add trading event logging:
    def log_trade_event(self, user_id, character_id, action, amount, price):
        """Log trading events with structured data"""
        # Add structured trade logging
        pass
    
    # YOUR CODE HERE - Add security event logging:
    def log_security_event(self, event_type, user_id, ip_address, details):
        """Log security events for audit trail"""
        # Add security event logging
        pass
    
    # YOUR CODE HERE - Add performance logging:
    def log_performance_event(self, endpoint, duration, status_code):
        """Log performance events for analysis"""
        # Add performance logging
        pass
    
    # YOUR CODE HERE - Add error logging:
    def log_error(self, error_type, error_message, stack_trace, context):
        """Log errors with full context"""
        # Add error logging
        pass

# TODO 8: CREATE LOGSTASH CONFIGURATION
# ═══════════════════════════════════════════════════════════
"""
🎯 YOUR TASK: Create Logstash pipeline configuration

Create file: monitoring/logstash/pipeline/onepiece-logs.conf
"""

# FILE: monitoring/logstash/pipeline/onepiece-logs.conf
# YOUR CODE HERE - Create Logstash configuration:
"""
input {
  # Add input sources for One Piece logs
  beats {
    # Add Filebeat configuration
  }
  
  http {
    # Add HTTP input for application logs
  }
}

filter {
  # Add filters for One Piece log processing
  if [fields][service] == "onepiece-backend" {
    # Add Django log parsing
  }
  
  if [fields][service] == "onepiece-frontend" {
    # Add React log parsing
  }
  
  if [fields][service] == "onepiece-trading" {
    # Add trading log parsing
  }
}

output {
  # Add output to Elasticsearch
  elasticsearch {
    # Add Elasticsearch configuration
  }
}
"""

# TODO 9: CREATE KIBANA DASHBOARDS
# ═══════════════════════════════════════════════════════════
"""
🎯 YOUR TASK: Create Kibana dashboard configuration

Create file: monitoring/kibana/dashboards/onepiece-logs-dashboard.json
"""

# FILE: monitoring/kibana/dashboards/onepiece-logs-dashboard.json
# YOUR CODE HERE - Create Kibana dashboard:
"""
{
  "objects": [
    {
      "type": "dashboard",
      "attributes": {
        "title": "🏴‍☠️ One Piece Trading - Log Analysis",
        "panelsJSON": "# Add panels JSON"
      }
    }
  ]
}
"""

# TODO 10: CREATE DISTRIBUTED TRACING
# ═══════════════════════════════════════════════════════════
"""
🎯 YOUR TASK: Implement distributed tracing with Jaeger

Create file: apps/monitoring/tracing_service.py
"""

# FILE: apps/monitoring/tracing_service.py
# YOUR CODE HERE - Import tracing modules:
from opentelemetry import trace
from opentelemetry.exporter.jaeger.thrift import JaegerExporter
from opentelemetry.sdk.trace import TracerProvider
# Add more imports...

# YOUR CODE HERE - Create tracing service:
class OnePieceTracing:
    """Distributed tracing service for One Piece microservices"""
    
    def __init__(self):
        # Add tracing configuration
        pass
    
    # YOUR CODE HERE - Add trace creation:
    def create_trace(self, operation_name, service_name):
        """Create new trace for operation"""
        # Add trace creation logic
        pass
    
    # YOUR CODE HERE - Add span creation:
    def create_span(self, span_name, parent_span=None):
        """Create new span within trace"""
        # Add span creation logic
        pass
    
    # YOUR CODE HERE - Add trace context propagation:
    def propagate_trace_context(self, request_headers):
        """Propagate trace context between services"""
        # Add context propagation logic
        pass

# YOUR CODE HERE - Create tracing decorator:
def trace_function(operation_name):
    """Decorator to automatically trace function calls"""
    def decorator(func):
        # Add tracing decorator logic
        pass
    return decorator

# ===============================================================================
# 🏴‍☠️ CONGRATULATIONS! YOU'VE MASTERED MONITORING & OBSERVABILITY! 🎉
# ===============================================================================

print('\n🏴‍☠️ CONGRATULATIONS! YOU\'VE MASTERED MONITORING & OBSERVABILITY! 🎉')
print('===============================================================================')

print('\n🎯 WHAT YOU\'VE ACCOMPLISHED:')
print('✅ Mastered Prometheus metrics collection and alerting')
print('✅ Built comprehensive Grafana dashboards for visualization')
print('✅ Implemented ELK Stack for centralized logging and analysis')
print('✅ Created distributed tracing with Jaeger for microservices')
print('✅ Added performance monitoring and SLA tracking')
print('✅ Applied observability patterns used by Netflix, Uber, and Google')

print('\n💰 SALARY IMPACT: +$80K-$180K (Observability is critical for senior DevOps/SRE roles)')
print('🏢 COMPANIES: All FAANG, Netflix, Uber, Datadog, New Relic, observability companies')

print('\n===============================================================================')
print('🎯 NOW IMPLEMENT THIS IN YOUR ONE PIECE PROJECT!')
print('===============================================================================')

print('\n🚀 STEP 1: ADD PROMETHEUS METRICS TO YOUR API GATEWAY')
print('━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━')
print('📁 File to update: services/api-gateway/server.js')
print('')
print('🎯 WHAT TO DO:')
print('1. Add Prometheus metrics collection middleware')
print('2. Create custom metrics for trading operations')
print('3. Monitor API response times and error rates')
print('4. Track business metrics (trades, user activity)')
print('5. Set up health check endpoints for monitoring')
print('')
print('📚 REFERENCE: Use the Prometheus patterns from this module')

print('\n🚀 STEP 2: INSTALL AND CONFIGURE PROMETHEUS MONITORING')
print('━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━')
print('📝 UPDATE: services/api-gateway/server.js')
print('')
print('const express = require("express");')
print('const promClient = require("prom-client");')
print('')
print('// Create Prometheus metrics')
print('const httpRequestDuration = new promClient.Histogram({')
print('    name: "http_request_duration_seconds",')
print('    help: "Duration of HTTP requests in seconds",')
print('    labelNames: ["method", "route", "status_code"],')
print('    buckets: [0.1, 0.3, 0.5, 0.7, 1, 3, 5, 7, 10]')
print('});')
print('')
print('const httpRequestsTotal = new promClient.Counter({')
print('    name: "http_requests_total",')
print('    help: "Total number of HTTP requests",')
print('    labelNames: ["method", "route", "status_code"]')
print('});')
print('')
print('const tradingOperationsTotal = new promClient.Counter({')
print('    name: "onepiece_trading_operations_total",')
print('    help: "Total number of trading operations",')
print('    labelNames: ["operation_type", "character_name", "user_id"]')
print('});')
print('')
print('const activeUsersGauge = new promClient.Gauge({')
print('    name: "onepiece_active_users",')
print('    help: "Number of currently active users"')
print('});')
print('')
print('// Metrics middleware')
print('app.use((req, res, next) => {')
print('    const start = Date.now();')
print('    ')
print('    res.on("finish", () => {')
print('        const duration = (Date.now() - start) / 1000;')
print('        const route = req.route ? req.route.path : req.path;')
print('        ')
print('        httpRequestDuration')
print('            .labels(req.method, route, res.statusCode.toString())')
print('            .observe(duration);')
print('        ')
print('        httpRequestsTotal')
print('            .labels(req.method, route, res.statusCode.toString())')
print('            .inc();')
print('    });')
print('    ')
print('    next();')
print('});')
print('')
print('// Metrics endpoint')
print('app.get("/metrics", async (req, res) => {')
print('    res.set("Content-Type", promClient.register.contentType);')
print('    res.end(await promClient.register.metrics());')
print('});')
print('')
print('// Trading metrics')
print('app.post("/api/trades", authenticateToken, async (req, res) => {')
print('    try {')
print('        const { characterId, operation, quantity } = req.body;')
print('        ')
print('        // Execute trade logic here')
print('        ')
print('        // Record trading metrics')
print('        tradingOperationsTotal')
print('            .labels(operation, characterId, req.user.userId)')
print('            .inc();')
print('        ')
print('        res.json({ success: true });')
print('    } catch (error) {')
print('        res.status(500).json({ error: error.message });')
print('    }')
print('});')
print('')
print('🔧 COPY FROM THIS MODULE:')
print('- Prometheus metrics setup (lines 150-250)')
print('- Custom business metrics (lines 300-350)')
print('- Middleware integration (lines 400-450)')

print('\n🚀 STEP 3: CREATE PROMETHEUS CONFIGURATION')
print('━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━')
print('📝 CREATE: monitoring/prometheus/prometheus.yml')
print('')
print('global:')
print('  scrape_interval: 15s')
print('  evaluation_interval: 15s')
print('')
print('rule_files:')
print('  - "onepiece_alerts.yml"')
print('')
print('scrape_configs:')
print('  # API Gateway')
print('  - job_name: "onepiece-api-gateway"')
print('    static_configs:')
print('      - targets: ["localhost:5000"]')
print('    metrics_path: "/metrics"')
print('    scrape_interval: 10s')
print('  ')
print('  # Character Service')
print('  - job_name: "onepiece-character-service"')
print('    static_configs:')
print('      - targets: ["localhost:5001"]')
print('    metrics_path: "/metrics"')
print('  ')
print('  # Trading Service')
print('  - job_name: "onepiece-trading-service"')
print('    static_configs:')
print('      - targets: ["localhost:5002"]')
print('    metrics_path: "/metrics"')
print('  ')
print('  # Database Monitoring')
print('  - job_name: "mysql-exporter"')
print('    static_configs:')
print('      - targets: ["localhost:9104"]')
print('  ')
print('  # Node Exporter (System Metrics)')
print('  - job_name: "node-exporter"')
print('    static_configs:')
print('      - targets: ["localhost:9100"]')
print('')
print('alerting:')
print('  alertmanagers:')
print('    - static_configs:')
print('        - targets: ["localhost:9093"]')
print('')
print('📝 CREATE: monitoring/prometheus/onepiece_alerts.yml')
print('')
print('groups:')
print('  - name: onepiece_alerts')
print('    rules:')
print('      - alert: HighErrorRate')
print('        expr: rate(http_requests_total{status_code=~"5.."}[5m]) > 0.1')
print('        for: 2m')
print('        labels:')
print('          severity: critical')
print('        annotations:')
print('          summary: "High error rate detected"')
print('          description: "Error rate is {{ $value }} errors per second"')
print('      ')
print('      - alert: HighResponseTime')
print('        expr: histogram_quantile(0.95, rate(http_request_duration_seconds_bucket[5m])) > 1')
print('        for: 5m')
print('        labels:')
print('          severity: warning')
print('        annotations:')
print('          summary: "High response time detected"')
print('          description: "95th percentile response time is {{ $value }} seconds"')
print('      ')
print('      - alert: TradingServiceDown')
print('        expr: up{job="onepiece-trading-service"} == 0')
print('        for: 1m')
print('        labels:')
print('          severity: critical')
print('        annotations:')
print('          summary: "Trading service is down"')
print('          description: "The One Piece trading service has been down for more than 1 minute"')
print('')
print('🔧 MONITORING BENEFITS:')
print('- Real-time performance monitoring')
print('- Automated alerting for issues')
print('- Historical data for capacity planning')
print('- Business metrics tracking')

print('\n🚀 STEP 4: SET UP GRAFANA DASHBOARDS')
print('━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━')
print('📝 CREATE: monitoring/grafana/dashboards/onepiece-overview.json')
print('')
print('# Start Grafana:')
print('docker run -d -p 3001:3000 --name=grafana grafana/grafana')
print('')
print('# Access Grafana at http://localhost:3001')
print('# Default login: admin/admin')
print('')
print('# Add Prometheus data source:')
print('# URL: http://localhost:9090')
print('')
print('# Create dashboard panels:')
print('1. API Request Rate:')
print('   Query: rate(http_requests_total[5m])')
print('   ')
print('2. Response Time (95th percentile):')
print('   Query: histogram_quantile(0.95, rate(http_request_duration_seconds_bucket[5m]))')
print('   ')
print('3. Error Rate:')
print('   Query: rate(http_requests_total{status_code=~"5.."}[5m])')
print('   ')
print('4. Trading Operations:')
print('   Query: rate(onepiece_trading_operations_total[5m])')
print('   ')
print('5. Active Users:')
print('   Query: onepiece_active_users')
print('   ')
print('6. Database Connections:')
print('   Query: mysql_global_status_threads_connected')
print('')
print('🔧 DASHBOARD FEATURES:')
print('- Real-time metrics visualization')
print('- Custom alerts and notifications')
print('- Historical trend analysis')
print('- Business KPI tracking')

print('\n🚀 STEP 5: IMPLEMENT STRUCTURED LOGGING')
print('━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━')
print('📝 UPDATE: services/api-gateway/server.js')
print('')
print('const winston = require("winston");')
print('')
print('// Configure structured logging')
print('const logger = winston.createLogger({')
print('    level: "info",')
print('    format: winston.format.combine(')
print('        winston.format.timestamp(),')
print('        winston.format.errors({ stack: true }),')
print('        winston.format.json()')
print('    ),')
print('    defaultMeta: { service: "onepiece-api-gateway" },')
print('    transports: [')
print('        new winston.transports.File({ filename: "logs/error.log", level: "error" }),')
print('        new winston.transports.File({ filename: "logs/combined.log" }),')
print('        new winston.transports.Console({')
print('            format: winston.format.simple()')
print('        })')
print('    ]')
print('});')
print('')
print('// Logging middleware')
print('app.use((req, res, next) => {')
print('    logger.info("HTTP Request", {')
print('        method: req.method,')
print('        url: req.url,')
print('        userAgent: req.get("User-Agent"),')
print('        ip: req.ip,')
print('        userId: req.user?.userId')
print('    });')
print('    next();')
print('});')
print('')
print('// Trading event logging')
print('app.post("/api/trades", authenticateToken, async (req, res) => {')
print('    try {')
print('        const { characterId, operation, quantity, price } = req.body;')
print('        ')
print('        logger.info("Trading Operation", {')
print('            userId: req.user.userId,')
print('            characterId,')
print('            operation,')
print('            quantity,')
print('            price,')
print('            timestamp: new Date().toISOString()')
print('        });')
print('        ')
print('        // Execute trade logic')
print('        ')
print('        res.json({ success: true });')
print('    } catch (error) {')
print('        logger.error("Trading Error", {')
print('            userId: req.user.userId,')
print('            error: error.message,')
print('            stack: error.stack')
print('        });')
print('        ')
print('        res.status(500).json({ error: error.message });')
print('    }')
print('});')
print('')
print('🔧 STRUCTURED LOGGING BENEFITS:')
print('- Searchable and filterable logs')
print('- Consistent log format across services')
print('- Better debugging and troubleshooting')
print('- Integration with log analysis tools')

print('\n🚀 STEP 6: TEST YOUR MONITORING IMPLEMENTATION')
print('━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━')
print('🧪 TESTING STEPS:')
print('')
print('1. Start Prometheus:')
print('   cd monitoring/prometheus')
print('   prometheus --config.file=prometheus.yml')
print('   # Access at http://localhost:9090')
print('')
print('2. Start Grafana:')
print('   docker run -d -p 3001:3000 grafana/grafana')
print('   # Access at http://localhost:3001')
print('')
print('3. Test metrics collection:')
print('   curl http://localhost:5000/metrics')
print('   # Should return Prometheus metrics')
print('')
print('4. Generate test traffic:')
print('   # Make multiple API requests to generate metrics')
print('   for i in {1..100}; do')
print('       curl http://localhost:5000/api/characters')
print('   done')
print('')
print('5. Check Prometheus targets:')
print('   # Visit http://localhost:9090/targets')
print('   # All targets should be "UP"')
print('')
print('6. View Grafana dashboards:')
print('   # Import dashboard and verify metrics are displayed')
print('   # Check that graphs show real-time data')
print('')
print('7. Test alerting:')
print('   # Stop a service to trigger alerts')
print('   # Verify alerts appear in Prometheus and Grafana')
print('')
print('✅ SUCCESS CRITERIA:')
print('- Prometheus successfully scrapes metrics from all services')
print('- Grafana dashboards display real-time metrics')
print('- Structured logs are generated and searchable')
print('- Alerts trigger when thresholds are exceeded')
print('- Business metrics (trades, users) are tracked correctly')
print('- System metrics (CPU, memory, disk) are monitored')

print('\n===============================================================================')
print('🔗 HOW THIS CONNECTS TO OTHER LEARNING MODULES')
print('===============================================================================')

print('\n🧩 MODULE CONNECTIONS:')
print('')
print('📚 Module 16 (Node.js) → API Gateway includes Prometheus metrics and structured logging')
print('📚 Module 6 (System Design) → Monitoring is essential for microservices architecture')
print('📚 Module 7 (Security) → Security events and authentication failures are monitored')
print('📚 Module 4 (Containerization) → Docker containers are monitored with cAdvisor')
print('📚 Module 5 (CI/CD) → Deployment metrics and build success rates are tracked')
print('📚 Module 3 (Database) → Database performance and query metrics are monitored')

print('\n🎯 NEXT MODULES TO COMPLETE:')
print('1. Module 6: Design monitoring architecture for your microservices')
print('2. Module 4: Add container monitoring with Docker and Kubernetes')
print('3. Module 5: Monitor CI/CD pipeline performance and deployment success')

print('\n📚 RECOMMENDED RESOURCES FOR CONTINUED LEARNING:')
print('🔗 Prometheus Documentation: https://prometheus.io/docs/')
print('🔗 Grafana Tutorials: https://grafana.com/tutorials/')
print('🔗 ELK Stack Guide: https://www.elastic.co/what-is/elk-stack')
print('🔗 Observability Best Practices: https://sre.google/books/')

print('\n🏴‍☠️ YOU\'RE NOW READY TO BUILD OBSERVABLE, PRODUCTION-READY SYSTEMS! ⚔️')
print('📖 REFERENCE: Check MASTER-BLUEPRINT-ARCHITECTURE.md for the complete system overview!')
