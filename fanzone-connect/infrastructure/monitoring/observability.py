"""
🏆 FANZONE CONNECT - OBSERVABILITY & MONITORING
Learning Modules: 32 (Monitoring/Observability), 31 (Big Tech Backend)
World Cup 2026 Fan Platform - Production-Grade Monitoring, Metrics, and Alerting
"""

import asyncio
import logging
import time
import json
from datetime import datetime, timezone
from typing import Dict, List, Optional, Any, Callable
from dataclasses import dataclass, field
from enum import Enum
import os
import psutil
import aiohttp
import asyncpg

from prometheus_client import Counter, Histogram, Gauge, CollectorRegistry, generate_latest
from opentelemetry import trace, metrics
from opentelemetry.exporter.jaeger.thrift import JaegerExporter
from opentelemetry.sdk.trace import TracerProvider
from opentelemetry.sdk.trace.export import BatchSpanProcessor
from opentelemetry.sdk.metrics import MeterProvider
from opentelemetry.sdk.metrics.export import PeriodicExportingMetricReader
from opentelemetry.exporter.prometheus import PrometheusMetricReader

import redis.asyncio as redis

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# =====================================================
# MODULE 32: MONITORING/OBSERVABILITY - METRICS
# =====================================================

class MetricType(str, Enum):
    COUNTER = "counter"
    HISTOGRAM = "histogram"
    GAUGE = "gauge"

class AlertSeverity(str, Enum):
    LOW = "low"
    MEDIUM = "medium"
    HIGH = "high"
    CRITICAL = "critical"

@dataclass
class MetricDefinition:
    name: str
    type: MetricType
    description: str
    labels: List[str] = field(default_factory=list)
    buckets: Optional[List[float]] = None

@dataclass
class Alert:
    id: str
    name: str
    severity: AlertSeverity
    message: str
    timestamp: datetime
    service: str
    metric_name: str
    metric_value: float
    threshold: float
    resolved: bool = False

class WorldCupMetrics:
    """
    Comprehensive metrics collection for World Cup 2026 platform
    Tracks performance, business metrics, and system health
    """
    
    def __init__(self):
        self.registry = CollectorRegistry()
        
        # System metrics
        self.request_count = Counter(
            'worldcup_requests_total',
            'Total HTTP requests',
            ['method', 'endpoint', 'status_code'],
            registry=self.registry
        )
        
        self.request_duration = Histogram(
            'worldcup_request_duration_seconds',
            'HTTP request duration',
            ['method', 'endpoint'],
            buckets=[0.1, 0.25, 0.5, 1.0, 2.5, 5.0, 10.0],
            registry=self.registry
        )
        
        self.active_connections = Gauge(
            'worldcup_active_connections',
            'Active WebSocket connections',
            ['service'],
            registry=self.registry
        )
        
        # Business metrics
        self.fan_registrations = Counter(
            'worldcup_fan_registrations_total',
            'Total fan registrations',
            ['country', 'source'],
            registry=self.registry
        )
        
        self.match_views = Counter(
            'worldcup_match_views_total',
            'Total match views',
            ['match_id', 'phase'],
            registry=self.registry
        )
        
        self.event_attendance = Gauge(
            'worldcup_event_attendance',
            'Current event attendance',
            ['event_id', 'city'],
            registry=self.registry
        )
        
        # Performance metrics
        self.database_query_duration = Histogram(
            'worldcup_db_query_duration_seconds',
            'Database query duration',
            ['query_type', 'table'],
            buckets=[0.01, 0.05, 0.1, 0.25, 0.5, 1.0, 2.0],
            registry=self.registry
        )
        
        self.cache_hit_rate = Gauge(
            'worldcup_cache_hit_rate',
            'Cache hit rate percentage',
            ['cache_type'],
            registry=self.registry
        )
        
        self.memory_usage = Gauge(
            'worldcup_memory_usage_bytes',
            'Memory usage in bytes',
            ['service'],
            registry=self.registry
        )
        
        self.cpu_usage = Gauge(
            'worldcup_cpu_usage_percent',
            'CPU usage percentage',
            ['service'],
            registry=self.registry
        )
    
    def record_request(self, method: str, endpoint: str, status_code: int, duration: float):
        """Record HTTP request metrics"""
        self.request_count.labels(
            method=method,
            endpoint=endpoint,
            status_code=str(status_code)
        ).inc()
        
        self.request_duration.labels(
            method=method,
            endpoint=endpoint
        ).observe(duration)
    
    def record_fan_registration(self, country: str, source: str):
        """Record fan registration"""
        self.fan_registrations.labels(
            country=country,
            source=source
        ).inc()
    
    def record_match_view(self, match_id: str, phase: str):
        """Record match view"""
        self.match_views.labels(
            match_id=match_id,
            phase=phase
        ).inc()
    
    def update_system_metrics(self, service: str):
        """Update system resource metrics"""
        # Memory usage
        memory = psutil.virtual_memory()
        self.memory_usage.labels(service=service).set(memory.used)
        
        # CPU usage
        cpu_percent = psutil.cpu_percent(interval=1)
        self.cpu_usage.labels(service=service).set(cpu_percent)
    
    def get_metrics(self) -> str:
        """Get Prometheus metrics in text format"""
        return generate_latest(self.registry).decode('utf-8')

# =====================================================
# DISTRIBUTED TRACING
# =====================================================

class WorldCupTracing:
    """
    Distributed tracing for World Cup 2026 microservices
    Uses OpenTelemetry with Jaeger backend
    """
    
    def __init__(self, service_name: str, jaeger_endpoint: str = "http://jaeger:14268/api/traces"):
        self.service_name = service_name
        
        # Configure tracing
        trace.set_tracer_provider(TracerProvider())
        
        jaeger_exporter = JaegerExporter(
            agent_host_name="jaeger",
            agent_port=6831,
        )
        
        span_processor = BatchSpanProcessor(jaeger_exporter)
        trace.get_tracer_provider().add_span_processor(span_processor)
        
        self.tracer = trace.get_tracer(service_name)
    
    def start_span(self, operation_name: str, **attributes):
        """Start a new trace span"""
        span = self.tracer.start_span(operation_name)
        
        # Add attributes
        for key, value in attributes.items():
            span.set_attribute(key, value)
        
        return span
    
    def trace_database_query(self, query: str, table: str):
        """Trace database query"""
        return self.start_span(
            "database.query",
            db_statement=query,
            db_table=table,
            db_type="postgresql"
        )
    
    def trace_http_request(self, method: str, url: str):
        """Trace HTTP request"""
        return self.start_span(
            "http.request",
            http_method=method,
            http_url=url
        )
    
    def trace_cache_operation(self, operation: str, key: str):
        """Trace cache operation"""
        return self.start_span(
            "cache.operation",
            cache_operation=operation,
            cache_key=key
        )

# =====================================================
# MODULE 31: BIG TECH BACKEND - ALERTING SYSTEM
# =====================================================

class AlertManager:
    """
    Production-grade alerting system for World Cup 2026 platform
    Handles metric thresholds, escalation, and notifications
    """
    
    def __init__(self, redis_client: redis.Redis):
        self.redis = redis_client
        self.alert_rules: Dict[str, Dict] = {}
        self.active_alerts: Dict[str, Alert] = {}
        self.notification_channels: List[Callable] = []
    
    def add_alert_rule(
        self,
        name: str,
        metric_name: str,
        threshold: float,
        comparison: str,  # 'gt', 'lt', 'eq'
        severity: AlertSeverity,
        description: str
    ):
        """Add alert rule"""
        self.alert_rules[name] = {
            'metric_name': metric_name,
            'threshold': threshold,
            'comparison': comparison,
            'severity': severity,
            'description': description
        }
    
    def add_notification_channel(self, channel: Callable):
        """Add notification channel (Slack, email, etc.)"""
        self.notification_channels.append(channel)
    
    async def check_alerts(self, metrics: Dict[str, float], service: str):
        """Check all alert rules against current metrics"""
        for rule_name, rule in self.alert_rules.items():
            metric_name = rule['metric_name']
            
            if metric_name not in metrics:
                continue
            
            metric_value = metrics[metric_name]
            threshold = rule['threshold']
            comparison = rule['comparison']
            
            # Check threshold
            alert_triggered = False
            if comparison == 'gt' and metric_value > threshold:
                alert_triggered = True
            elif comparison == 'lt' and metric_value < threshold:
                alert_triggered = True
            elif comparison == 'eq' and metric_value == threshold:
                alert_triggered = True
            
            alert_id = f"{service}:{rule_name}"
            
            if alert_triggered:
                if alert_id not in self.active_alerts:
                    # New alert
                    alert = Alert(
                        id=alert_id,
                        name=rule_name,
                        severity=rule['severity'],
                        message=f"{rule['description']} - Current: {metric_value}, Threshold: {threshold}",
                        timestamp=datetime.now(timezone.utc),
                        service=service,
                        metric_name=metric_name,
                        metric_value=metric_value,
                        threshold=threshold
                    )
                    
                    self.active_alerts[alert_id] = alert
                    await self._send_alert(alert)
                    
                    # Store in Redis
                    await self.redis.setex(
                        f"alert:{alert_id}",
                        3600,  # 1 hour TTL
                        json.dumps(alert.__dict__, default=str)
                    )
            
            else:
                # Check if alert should be resolved
                if alert_id in self.active_alerts:
                    alert = self.active_alerts[alert_id]
                    alert.resolved = True
                    
                    await self._send_resolution(alert)
                    del self.active_alerts[alert_id]
                    
                    # Remove from Redis
                    await self.redis.delete(f"alert:{alert_id}")
    
    async def _send_alert(self, alert: Alert):
        """Send alert to all notification channels"""
        logger.warning(f"🚨 ALERT: {alert.name} - {alert.message}")
        
        for channel in self.notification_channels:
            try:
                await channel(alert)
            except Exception as e:
                logger.error(f"❌ Failed to send alert via channel: {e}")
    
    async def _send_resolution(self, alert: Alert):
        """Send alert resolution notification"""
        logger.info(f"✅ RESOLVED: {alert.name}")
        
        for channel in self.notification_channels:
            try:
                await channel(alert, resolved=True)
            except Exception as e:
                logger.error(f"❌ Failed to send resolution via channel: {e}")

# =====================================================
# HEALTH CHECKS
# =====================================================

class HealthChecker:
    """
    Comprehensive health checking for World Cup 2026 services
    """
    
    def __init__(self):
        self.checks: Dict[str, Callable] = {}
    
    def add_check(self, name: str, check_func: Callable):
        """Add health check"""
        self.checks[name] = check_func
    
    async def check_database(self, connection_string: str) -> Dict[str, Any]:
        """Check database connectivity"""
        try:
            conn = await asyncpg.connect(connection_string)
            result = await conn.fetchval("SELECT 1")
            await conn.close()
            
            return {
                "status": "healthy",
                "response_time": 0.1,  # Would measure actual time
                "details": "Database connection successful"
            }
        except Exception as e:
            return {
                "status": "unhealthy",
                "error": str(e),
                "details": "Database connection failed"
            }
    
    async def check_redis(self, redis_client: redis.Redis) -> Dict[str, Any]:
        """Check Redis connectivity"""
        try:
            start_time = time.time()
            await redis_client.ping()
            response_time = time.time() - start_time
            
            return {
                "status": "healthy",
                "response_time": response_time,
                "details": "Redis connection successful"
            }
        except Exception as e:
            return {
                "status": "unhealthy",
                "error": str(e),
                "details": "Redis connection failed"
            }
    
    async def check_external_api(self, url: str) -> Dict[str, Any]:
        """Check external API health"""
        try:
            start_time = time.time()
            async with aiohttp.ClientSession() as session:
                async with session.get(url, timeout=aiohttp.ClientTimeout(total=5)) as response:
                    response_time = time.time() - start_time
                    
                    if response.status == 200:
                        return {
                            "status": "healthy",
                            "response_time": response_time,
                            "status_code": response.status,
                            "details": "External API responding"
                        }
                    else:
                        return {
                            "status": "degraded",
                            "response_time": response_time,
                            "status_code": response.status,
                            "details": f"External API returned {response.status}"
                        }
        except Exception as e:
            return {
                "status": "unhealthy",
                "error": str(e),
                "details": "External API unreachable"
            }
    
    async def run_all_checks(self) -> Dict[str, Any]:
        """Run all health checks"""
        results = {}
        overall_status = "healthy"
        
        for name, check_func in self.checks.items():
            try:
                result = await check_func()
                results[name] = result
                
                if result["status"] == "unhealthy":
                    overall_status = "unhealthy"
                elif result["status"] == "degraded" and overall_status == "healthy":
                    overall_status = "degraded"
                    
            except Exception as e:
                results[name] = {
                    "status": "unhealthy",
                    "error": str(e),
                    "details": "Health check failed"
                }
                overall_status = "unhealthy"
        
        return {
            "status": overall_status,
            "timestamp": datetime.now(timezone.utc).isoformat(),
            "checks": results
        }

# =====================================================
# MAIN OBSERVABILITY SERVICE
# =====================================================

class WorldCupObservability:
    """
    Main observability service for World Cup 2026 platform
    Coordinates metrics, tracing, alerting, and health checks
    """
    
    def __init__(self, service_name: str, redis_url: str):
        self.service_name = service_name
        self.metrics = WorldCupMetrics()
        self.tracing = WorldCupTracing(service_name)
        self.health_checker = HealthChecker()
        
        # Initialize Redis for alerting
        self.redis = None
        self.redis_url = redis_url
        self.alert_manager = None
    
    async def initialize(self):
        """Initialize observability components"""
        logger.info(f"🔍 Initializing observability for {self.service_name}")
        
        # Initialize Redis
        self.redis = redis.from_url(self.redis_url, decode_responses=True)
        await self.redis.ping()
        
        # Initialize alert manager
        self.alert_manager = AlertManager(self.redis)
        
        # Setup default alert rules
        self._setup_default_alerts()
        
        # Setup health checks
        self._setup_health_checks()
        
        logger.info("✅ Observability initialized")
    
    def _setup_default_alerts(self):
        """Setup default alert rules for World Cup platform"""
        self.alert_manager.add_alert_rule(
            "high_response_time",
            "avg_response_time",
            2.0,  # 2 seconds
            "gt",
            AlertSeverity.HIGH,
            "Average response time is too high"
        )
        
        self.alert_manager.add_alert_rule(
            "high_error_rate",
            "error_rate",
            0.05,  # 5%
            "gt",
            AlertSeverity.CRITICAL,
            "Error rate is above acceptable threshold"
        )
        
        self.alert_manager.add_alert_rule(
            "low_cache_hit_rate",
            "cache_hit_rate",
            0.8,  # 80%
            "lt",
            AlertSeverity.MEDIUM,
            "Cache hit rate is below optimal"
        )
    
    def _setup_health_checks(self):
        """Setup health checks"""
        self.health_checker.add_check("redis", lambda: self.health_checker.check_redis(self.redis))
    
    async def collect_metrics(self) -> Dict[str, float]:
        """Collect current metrics"""
        # Update system metrics
        self.metrics.update_system_metrics(self.service_name)
        
        # Return current metric values (simplified)
        return {
            "avg_response_time": 1.5,  # Would calculate from histogram
            "error_rate": 0.02,
            "cache_hit_rate": 0.85,
            "active_connections": 150
        }
    
    async def run_monitoring_cycle(self):
        """Run one monitoring cycle"""
        try:
            # Collect metrics
            current_metrics = await self.collect_metrics()
            
            # Check alerts
            await self.alert_manager.check_alerts(current_metrics, self.service_name)
            
            # Run health checks
            health_status = await self.health_checker.run_all_checks()
            
            logger.info(f"📊 Monitoring cycle complete - Health: {health_status['status']}")
            
        except Exception as e:
            logger.error(f"❌ Monitoring cycle failed: {e}")

# Example usage
async def main():
    """Example usage of World Cup 2026 observability"""
    
    observability = WorldCupObservability("fanzone-api", "redis://redis:6379")
    await observability.initialize()
    
    # Simulate monitoring cycles
    for i in range(5):
        await observability.run_monitoring_cycle()
        await asyncio.sleep(10)

if __name__ == "__main__":
    asyncio.run(main())
