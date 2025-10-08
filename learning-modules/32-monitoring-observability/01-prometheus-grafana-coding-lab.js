/*
🏴‍☠️ MODULE 32: MONITORING & OBSERVABILITY - BIG TECH PRODUCTION STANDARDS
═══════════════════════════════════════════════════════════════════════════════

🎯 WHAT YOU'RE BUILDING:
PRODUCTION-GRADE monitoring and observability like Netflix, Google, Uber!
This is how big tech companies monitor millions of requests and prevent outages!

📚 LEARNING OBJECTIVES:
- Prometheus metrics collection (Google SRE standard)
- Grafana dashboards (Netflix monitoring)
- Distributed tracing (Uber/Lyft pattern)
- Log aggregation (ELK stack)
- Alerting and incident response
- SLA/SLO monitoring (Google SRE)
- Performance monitoring (APM)
- Error tracking and debugging

🔗 INTEGRATES WITH YOUR ONE PIECE PROJECT:
- MONITORS: All microservices health and performance
- TRACKS: Trading latency and success rates
- ALERTS: When system performance degrades
- VISUALIZES: Real-time dashboards like Netflix
- DEBUGS: Distributed request tracing

💰 CAREER IMPACT: +$50K-$100K (SRE/DevOps expertise is highly valued!)

🎯 BIG TECH MONITORING EXAMPLES:
- Netflix: 99.99% uptime with chaos engineering
- Google: SRE practices with SLA monitoring
- Uber: Real-time monitoring of millions of trips
- Amazon: CloudWatch monitoring at massive scale
*/

// TODO 1: PROMETHEUS METRICS COLLECTION (GOOGLE SRE STANDARD)
// ═══════════════════════════════════════════════════════════
/*
🎯 YOUR TASK: Implement Prometheus metrics like Google SRE

GOOGLE'S FOUR GOLDEN SIGNALS:
1. Latency - How long requests take
2. Traffic - How many requests per second
3. Errors - Rate of failed requests
4. Saturation - How full your service is

PROMETHEUS METRIC TYPES:
- Counter: Always increasing (total requests)
- Gauge: Can go up/down (current users)
- Histogram: Distribution of values (response times)
- Summary: Similar to histogram with quantiles
*/

const prometheus = require('prom-client');

// Initialize Prometheus metrics registry
const register = new prometheus.Registry();

// Add default Node.js metrics (memory, CPU, etc.)
prometheus.collectDefaultMetrics({ register });

// Custom metrics for One Piece Trading Platform
class OnePieceMetrics {
    constructor() {
        // 1. LATENCY METRICS (Golden Signal #1)
        this.httpRequestDuration = new prometheus.Histogram({
            name: 'onepiece_http_request_duration_seconds',
            help: 'Duration of HTTP requests in seconds',
            labelNames: ['method', 'route', 'status_code', 'service'],
            buckets: [0.001, 0.005, 0.01, 0.05, 0.1, 0.5, 1, 5, 10] // SLA buckets
        });
        
        // 2. TRAFFIC METRICS (Golden Signal #2)
        this.httpRequestsTotal = new prometheus.Counter({
            name: 'onepiece_http_requests_total',
            help: 'Total number of HTTP requests',
            labelNames: ['method', 'route', 'status_code', 'service']
        });
        
        // 3. ERROR METRICS (Golden Signal #3)
        this.httpRequestErrors = new prometheus.Counter({
            name: 'onepiece_http_request_errors_total',
            help: 'Total number of HTTP request errors',
            labelNames: ['method', 'route', 'error_type', 'service']
        });
        
        // 4. SATURATION METRICS (Golden Signal #4)
        this.activeConnections = new prometheus.Gauge({
            name: 'onepiece_active_connections',
            help: 'Number of active connections',
            labelNames: ['service']
        });
        
        // BUSINESS METRICS (One Piece specific)
        this.tradesExecuted = new prometheus.Counter({
            name: 'onepiece_trades_executed_total',
            help: 'Total number of trades executed',
            labelNames: ['action', 'character_id', 'user_type']
        });
        
        this.tradingVolume = new prometheus.Gauge({
            name: 'onepiece_trading_volume_berries',
            help: 'Current trading volume in berries',
            labelNames: ['character_id']
        });
        
        this.activeUsers = new prometheus.Gauge({
            name: 'onepiece_active_users',
            help: 'Number of currently active users',
            labelNames: ['user_type']
        });
        
        this.databaseConnections = new prometheus.Gauge({
            name: 'onepiece_database_connections',
            help: 'Number of active database connections',
            labelNames: ['database', 'state']
        });
        
        // Register all metrics
        register.registerMetric(this.httpRequestDuration);
        register.registerMetric(this.httpRequestsTotal);
        register.registerMetric(this.httpRequestErrors);
        register.registerMetric(this.activeConnections);
        register.registerMetric(this.tradesExecuted);
        register.registerMetric(this.tradingVolume);
        register.registerMetric(this.activeUsers);
        register.registerMetric(this.databaseConnections);
    }
    
    // Middleware to automatically collect HTTP metrics
    createMetricsMiddleware(serviceName) {
        return (req, res, next) => {
            const startTime = Date.now();
            
            // Increment request counter
            this.httpRequestsTotal.inc({
                method: req.method,
                route: req.route?.path || req.path,
                status_code: res.statusCode,
                service: serviceName
            });
            
            // Track response time
            res.on('finish', () => {
                const duration = (Date.now() - startTime) / 1000;
                
                this.httpRequestDuration.observe({
                    method: req.method,
                    route: req.route?.path || req.path,
                    status_code: res.statusCode,
                    service: serviceName
                }, duration);
                
                // Track errors (4xx, 5xx)
                if (res.statusCode >= 400) {
                    this.httpRequestErrors.inc({
                        method: req.method,
                        route: req.route?.path || req.path,
                        error_type: res.statusCode >= 500 ? 'server_error' : 'client_error',
                        service: serviceName
                    });
                }
            });
            
            next();
        };
    }
    
    // Business logic metrics
    recordTrade(action, characterId, userType, amount) {
        this.tradesExecuted.inc({
            action,
            character_id: characterId,
            user_type: userType
        });
        
        this.tradingVolume.set({ character_id: characterId }, amount);
    }
    
    updateActiveUsers(userType, count) {
        this.activeUsers.set({ user_type: userType }, count);
    }
    
    updateDatabaseConnections(database, state, count) {
        this.databaseConnections.set({ database, state }, count);
    }
}

// Initialize metrics
const metrics = new OnePieceMetrics();

// TODO 2: GRAFANA DASHBOARDS (NETFLIX MONITORING STYLE)
// ═══════════════════════════════════════════════════════════
/*
🎯 YOUR TASK: Create Grafana dashboards like Netflix

NETFLIX DASHBOARD STRUCTURE:
- Service Overview (health, traffic, errors)
- Performance Metrics (latency, throughput)
- Business Metrics (user engagement, revenue)
- Infrastructure Metrics (CPU, memory, disk)

GRAFANA DASHBOARD JSON FOR ONE PIECE PLATFORM:
*/

const onePieceDashboard = {
    "dashboard": {
        "id": null,
        "title": "One Piece Trading Platform - Production Monitoring",
        "tags": ["onepiece", "trading", "production"],
        "timezone": "browser",
        "panels": [
            {
                "id": 1,
                "title": "Request Rate (RPS)",
                "type": "stat",
                "targets": [
                    {
                        "expr": "rate(onepiece_http_requests_total[5m])",
                        "legendFormat": "{{service}} - {{method}}"
                    }
                ],
                "fieldConfig": {
                    "defaults": {
                        "color": { "mode": "palette-classic" },
                        "custom": { "displayMode": "list", "orientation": "horizontal" },
                        "mappings": [],
                        "thresholds": {
                            "steps": [
                                { "color": "green", "value": null },
                                { "color": "yellow", "value": 1000 },
                                { "color": "red", "value": 5000 }
                            ]
                        },
                        "unit": "reqps"
                    }
                }
            },
            {
                "id": 2,
                "title": "Response Time (P95)",
                "type": "stat",
                "targets": [
                    {
                        "expr": "histogram_quantile(0.95, rate(onepiece_http_request_duration_seconds_bucket[5m]))",
                        "legendFormat": "95th percentile"
                    }
                ],
                "fieldConfig": {
                    "defaults": {
                        "color": { "mode": "thresholds" },
                        "thresholds": {
                            "steps": [
                                { "color": "green", "value": null },
                                { "color": "yellow", "value": 0.1 },
                                { "color": "red", "value": 0.5 }
                            ]
                        },
                        "unit": "s"
                    }
                }
            },
            {
                "id": 3,
                "title": "Error Rate",
                "type": "stat",
                "targets": [
                    {
                        "expr": "rate(onepiece_http_request_errors_total[5m]) / rate(onepiece_http_requests_total[5m]) * 100",
                        "legendFormat": "Error Rate %"
                    }
                ],
                "fieldConfig": {
                    "defaults": {
                        "color": { "mode": "thresholds" },
                        "thresholds": {
                            "steps": [
                                { "color": "green", "value": null },
                                { "color": "yellow", "value": 1 },
                                { "color": "red", "value": 5 }
                            ]
                        },
                        "unit": "percent"
                    }
                }
            },
            {
                "id": 4,
                "title": "Active Users",
                "type": "timeseries",
                "targets": [
                    {
                        "expr": "onepiece_active_users",
                        "legendFormat": "{{user_type}}"
                    }
                ]
            },
            {
                "id": 5,
                "title": "Trading Volume (Last 24h)",
                "type": "timeseries",
                "targets": [
                    {
                        "expr": "increase(onepiece_trades_executed_total[24h])",
                        "legendFormat": "{{action}} - {{character_id}}"
                    }
                ]
            },
            {
                "id": 6,
                "title": "Database Connections",
                "type": "timeseries",
                "targets": [
                    {
                        "expr": "onepiece_database_connections",
                        "legendFormat": "{{database}} - {{state}}"
                    }
                ]
            }
        ],
        "time": { "from": "now-1h", "to": "now" },
        "refresh": "5s"
    }
};

// TODO 3: DISTRIBUTED TRACING (UBER/LYFT PATTERN)
// ═══════════════════════════════════════════════════════════
/*
🎯 YOUR TASK: Implement distributed tracing like Uber

WHAT IS DISTRIBUTED TRACING?
Track a single request across multiple microservices to debug performance issues.

UBER'S TRACING EXAMPLE:
User Request → API Gateway → User Service → Trading Service → Database
Each step is traced with timing and context.

JAEGER TRACING IMPLEMENTATION:
*/

const opentracing = require('opentracing');
const jaeger = require('jaeger-client');

class DistributedTracing {
    constructor() {
        // Initialize Jaeger tracer
        const config = {
            serviceName: 'onepiece-trading-platform',
            sampler: {
                type: 'const',
                param: 1, // Sample 100% of traces (reduce in production)
            },
            reporter: {
                logSpans: true,
                agentHost: process.env.JAEGER_AGENT_HOST || 'localhost',
                agentPort: process.env.JAEGER_AGENT_PORT || 6832,
            },
        };
        
        this.tracer = jaeger.initTracer(config);
        opentracing.initGlobalTracer(this.tracer);
    }
    
    // Express middleware for automatic tracing
    createTracingMiddleware(serviceName) {
        return (req, res, next) => {
            // Extract parent span context from headers
            const parentSpanContext = this.tracer.extract(
                opentracing.FORMAT_HTTP_HEADERS,
                req.headers
            );
            
            // Create new span for this request
            const span = this.tracer.startSpan(`${req.method} ${req.path}`, {
                childOf: parentSpanContext,
                tags: {
                    [opentracing.Tags.HTTP_METHOD]: req.method,
                    [opentracing.Tags.HTTP_URL]: req.url,
                    [opentracing.Tags.COMPONENT]: serviceName,
                    'user.id': req.user?.id,
                    'request.id': req.headers['x-request-id']
                }
            });
            
            // Add span to request for use in handlers
            req.span = span;
            
            // Inject span context into response headers
            const headers = {};
            this.tracer.inject(span, opentracing.FORMAT_HTTP_HEADERS, headers);
            Object.keys(headers).forEach(key => {
                res.setHeader(key, headers[key]);
            });
            
            // Finish span when response ends
            res.on('finish', () => {
                span.setTag(opentracing.Tags.HTTP_STATUS_CODE, res.statusCode);
                
                if (res.statusCode >= 400) {
                    span.setTag(opentracing.Tags.ERROR, true);
                    span.log({
                        event: 'error',
                        message: `HTTP ${res.statusCode}`,
                    });
                }
                
                span.finish();
            });
            
            next();
        };
    }
    
    // Trace database operations
    async traceDatabase(operation, query, parentSpan) {
        const span = this.tracer.startSpan('database.query', {
            childOf: parentSpan,
            tags: {
                [opentracing.Tags.DB_STATEMENT]: query,
                [opentracing.Tags.DB_TYPE]: 'postgresql',
                [opentracing.Tags.COMPONENT]: 'database'
            }
        });
        
        try {
            const result = await operation();
            span.setTag('db.rows_affected', result.rowCount || 0);
            return result;
        } catch (error) {
            span.setTag(opentracing.Tags.ERROR, true);
            span.log({
                event: 'error',
                message: error.message,
                stack: error.stack
            });
            throw error;
        } finally {
            span.finish();
        }
    }
    
    // Trace external API calls
    async traceExternalCall(serviceName, url, operation, parentSpan) {
        const span = this.tracer.startSpan(`external.${serviceName}`, {
            childOf: parentSpan,
            tags: {
                [opentracing.Tags.HTTP_URL]: url,
                [opentracing.Tags.COMPONENT]: 'http-client',
                'service.name': serviceName
            }
        });
        
        try {
            const result = await operation();
            span.setTag(opentracing.Tags.HTTP_STATUS_CODE, result.status);
            return result;
        } catch (error) {
            span.setTag(opentracing.Tags.ERROR, true);
            span.log({
                event: 'error',
                message: error.message
            });
            throw error;
        } finally {
            span.finish();
        }
    }
}

// TODO 4: ALERTING & INCIDENT RESPONSE (GOOGLE SRE PATTERN)
// ═══════════════════════════════════════════════════════════
/*
🎯 YOUR TASK: Implement alerting like Google SRE

GOOGLE SRE ALERTING PRINCIPLES:
- Alert on symptoms, not causes
- Have good signal-to-noise ratio
- Classify alerts by urgency
- Have clear runbooks for each alert

PROMETHEUS ALERTING RULES:
*/

const alertingRules = `
groups:
  - name: onepiece.trading.alerts
    rules:
      # HIGH PRIORITY ALERTS (Page immediately)
      - alert: OnePieceServiceDown
        expr: up{job="onepiece-api"} == 0
        for: 1m
        labels:
          severity: critical
          team: platform
        annotations:
          summary: "One Piece service is down"
          description: "Service {{ $labels.instance }} has been down for more than 1 minute"
          runbook_url: "https://wiki.company.com/runbooks/service-down"
          
      - alert: OnePieceHighErrorRate
        expr: rate(onepiece_http_request_errors_total[5m]) / rate(onepiece_http_requests_total[5m]) > 0.05
        for: 2m
        labels:
          severity: critical
          team: platform
        annotations:
          summary: "High error rate detected"
          description: "Error rate is {{ $value | humanizePercentage }} for service {{ $labels.service }}"
          
      - alert: OnePieceHighLatency
        expr: histogram_quantile(0.95, rate(onepiece_http_request_duration_seconds_bucket[5m])) > 0.5
        for: 5m
        labels:
          severity: warning
          team: platform
        annotations:
          summary: "High latency detected"
          description: "95th percentile latency is {{ $value }}s for {{ $labels.service }}"
          
      # MEDIUM PRIORITY ALERTS (Investigate during business hours)
      - alert: OnePieceDatabaseConnectionsHigh
        expr: onepiece_database_connections{state="active"} > 80
        for: 10m
        labels:
          severity: warning
          team: platform
        annotations:
          summary: "High database connection usage"
          description: "Database {{ $labels.database }} has {{ $value }} active connections"
          
      # BUSINESS ALERTS (Trading specific)
      - alert: OnePieceTradingVolumeAnomaly
        expr: rate(onepiece_trades_executed_total[1h]) < 0.1 * rate(onepiece_trades_executed_total[24h] offset 24h)
        for: 30m
        labels:
          severity: warning
          team: business
        annotations:
          summary: "Trading volume significantly lower than usual"
          description: "Current trading rate is {{ $value }} trades/hour, much lower than yesterday"
`;

// Incident Response Automation
class IncidentResponse {
    constructor() {
        this.incidents = new Map();
        this.escalationPolicies = {
            critical: ['oncall-engineer', 'team-lead', 'director'],
            warning: ['oncall-engineer'],
            info: []
        };
    }
    
    async handleAlert(alert) {
        const incidentId = this.generateIncidentId();
        
        const incident = {
            id: incidentId,
            alert: alert,
            severity: alert.labels.severity,
            status: 'open',
            createdAt: new Date(),
            assignedTo: null,
            escalationLevel: 0
        };
        
        this.incidents.set(incidentId, incident);
        
        // Auto-assign to on-call engineer
        await this.assignIncident(incidentId, 'oncall-engineer');
        
        // Send notifications
        await this.sendNotifications(incident);
        
        // Start escalation timer for critical alerts
        if (incident.severity === 'critical') {
            this.startEscalationTimer(incidentId);
        }
        
        return incidentId;
    }
    
    async sendNotifications(incident) {
        const message = `
🚨 INCIDENT: ${incident.alert.annotations.summary}
Severity: ${incident.severity.toUpperCase()}
Service: ${incident.alert.labels.service || 'unknown'}
Description: ${incident.alert.annotations.description}
Runbook: ${incident.alert.annotations.runbook_url || 'N/A'}
        `;
        
        // Send to Slack/PagerDuty/Email
        await this.sendSlackAlert(message);
        await this.sendPagerDutyAlert(incident);
    }
    
    startEscalationTimer(incidentId) {
        setTimeout(async () => {
            const incident = this.incidents.get(incidentId);
            if (incident && incident.status === 'open') {
                incident.escalationLevel++;
                const escalationPolicy = this.escalationPolicies[incident.severity];
                
                if (incident.escalationLevel < escalationPolicy.length) {
                    const nextAssignee = escalationPolicy[incident.escalationLevel];
                    await this.assignIncident(incidentId, nextAssignee);
                    await this.sendEscalationNotification(incident, nextAssignee);
                }
            }
        }, 15 * 60 * 1000); // Escalate after 15 minutes
    }
    
    generateIncidentId() {
        return `INC-${Date.now()}-${Math.random().toString(36).substr(2, 6).toUpperCase()}`;
    }
}

/*
═══════════════════════════════════════════════════════════════════════════════
🎯 WHAT'S NEXT? YOUR PRODUCTION MONITORING IMPLEMENTATION
═══════════════════════════════════════════════════════════════════════════════

🏴‍☠️ CONGRATULATIONS! You now have BIG TECH monitoring capabilities!

📚 WHAT YOU JUST BUILT:
✅ Prometheus metrics collection (Google's Four Golden Signals)
✅ Grafana dashboards (Netflix-style monitoring)
✅ Distributed tracing (Uber/Lyft pattern)
✅ Alerting and incident response (Google SRE)
✅ Business metrics tracking
✅ Performance monitoring (APM)
✅ Error tracking and debugging

🎯 PRODUCTION MONITORING FEATURES:
├── Real-time metrics collection
├── Visual dashboards for all services
├── Distributed request tracing
├── Automated alerting and escalation
├── Incident response automation
└── SLA/SLO monitoring

🎯 APPLY TO YOUR ONE PIECE PROJECT:
1. Add Prometheus metrics to all services
2. Create Grafana dashboards for monitoring
3. Implement distributed tracing
4. Set up alerting rules
5. Monitor trading performance and business metrics

🔥 YOU'VE COMPLETED THE BIG TECH BACKEND MASTERY TRACK!
🏆 YOU NOW HAVE ENTERPRISE-LEVEL MONITORING LIKE NETFLIX/GOOGLE!

📚 YOUR COMPLETE BIG TECH SKILL SET:
✅ System Design (FAANG interview ready)
✅ Microservices Architecture (Google/Amazon scale)
✅ Event Sourcing & CQRS (Advanced patterns)
✅ Distributed Caching (Netflix performance)
✅ Load Balancing & Circuit Breakers (Netflix reliability)
✅ Message Queues & Event Streaming (Kafka patterns)
✅ Monitoring & Observability (Google SRE standards)

🚀 You're now ready for Senior/Staff Engineer roles at big tech companies! ⚔️
*/
