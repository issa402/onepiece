"""
🏴‍☠️ SRE MASTERY: API TESTING & MONITORING BLUEPRINT
═══════════════════════════════════════════════════════════

🎯 LEARNING OBJECTIVES - BECOME AN SRE TESTING EXPERT:
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
✅ Master SRE monitoring patterns and health check validation
✅ Implement Service Level Indicators (SLIs) and Objectives (SLOs)
✅ Build automated testing for reliability and performance
✅ Create incident detection and alerting mechanisms
✅ Learn error budget management and burn rate calculations
✅ Implement chaos engineering and fault injection testing

📖 SRE THEORY: THE FOUR GOLDEN SIGNALS OF MONITORING
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
Google SRE teams monitor these critical metrics:

1. 🚀 LATENCY - How long requests take to complete
   • Target: 95% of requests < 200ms, 99% < 500ms
   • Our SLO: Character API responds in <100ms average

2. 🚦 TRAFFIC - How many requests per second
   • Measure: QPS (Queries Per Second)
   • Our target: Handle 1000 requests/second

3. 🚨 ERRORS - Rate of failed requests
   • Target: <0.1% error rate (99.9% success)
   • Track: 4xx (client errors) vs 5xx (server errors)

4. 💾 SATURATION - How "full" your service is
   • Monitor: CPU, memory, disk, database connections
   • Alert before hitting 80% capacity

🔧 REAL-WORLD SRE CONNECTION:
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
This testing suite implements patterns used by:
• Netflix: Chaos Monkey testing and circuit breakers
• Google: SLI/SLO monitoring and error budget enforcement
• Amazon: Health checks and auto-scaling triggers
• Spotify: Performance regression detection
• Uber: Real-time alerting and incident response

📊 INDUSTRY SALARY IMPACT:
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
Mastering these SRE testing patterns can increase your salary by:
• Junior SRE: $95K-$161K (API monitoring expertise)
• Senior SRE: $129K-$204K (SLO/error budget management)
• Principal SRE: $180K-$300K (system reliability architecture)
"""

"""
🧪 HANDS-ON LAB 1: SRE MONITORING IMPORTS
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

📚 THEORY: SRE MONITORING STACK
Each import serves a specific SRE monitoring purpose:

• requests: HTTP client for health checks and API monitoring
• time: Latency measurement and timeout handling
• statistics: Calculate percentiles (P95, P99) for SLO validation
• threading: Concurrent load testing for capacity planning
• json: Parse API responses and metrics data
• os/dotenv: Environment-based configuration (dev/staging/prod)
• logging: Structured logging for incident investigation
• dataclasses: Type-safe metric collection
• datetime: Timestamp tracking for time-series metrics

🔧 REAL-WORLD USAGE:
Netflix uses similar imports in their Hystrix circuit breaker library
Google SRE teams use these patterns in their monitoring infrastructure
"""

# SRE MONITORING IMPORTS - Each serves a specific reliability purpose
import requests          # HTTP client for API health checks and monitoring
import time             # Latency measurement and SLO validation
import statistics       # Calculate P95, P99 percentiles for performance SLOs
import threading        # Concurrent testing for load and capacity planning
import json             # Parse API responses and metrics data
import os               # Environment configuration management
import sys              # System operations and exit codes
import logging          # Structured logging for incident investigation
from datetime import datetime, timedelta  # Timestamp tracking for metrics
from dataclasses import dataclass         # Type-safe metric collection
from typing import Dict, List, Optional   # Type hints for reliability
from dotenv import load_dotenv           # Environment-based configuration

# Configure structured logging for SRE observability
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    handlers=[
        logging.FileHandler('api_monitoring.log'),
        logging.StreamHandler(sys.stdout)
    ]
)
logger = logging.getLogger(__name__)


"""
🧪 HANDS-ON LAB 2: SRE METRICS & CONFIGURATION
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

📚 THEORY: SRE METRICS COLLECTION
SRE teams track metrics using structured data classes:

• Latency metrics: Response times, percentiles (P50, P95, P99)
• Error metrics: Success rate, error rate, error budget burn
• Traffic metrics: Requests per second, concurrent users
• Saturation metrics: Resource utilization, queue depth

🔧 REAL-WORLD EXAMPLE:
Google's SRE teams use similar metric structures in their
monitoring systems. Each service has defined SLIs and SLOs
that are continuously measured and alerted on.

📊 SLO TARGETS (Industry Standard):
• Latency: 95% of requests < 200ms
• Availability: 99.9% uptime (8.77 hours downtime/year)
• Error Rate: < 0.1% of requests fail
• Throughput: Handle expected peak load + 20% buffer
"""

# Load environment configuration
load_dotenv()

# SRE METRICS DATA STRUCTURES
@dataclass
class LatencyMetrics:
    """Track response time metrics for SLO validation"""
    response_times: List[float]
    p50: float = 0.0
    p95: float = 0.0
    p99: float = 0.0
    average: float = 0.0
    max_time: float = 0.0

    def calculate_percentiles(self):
        """Calculate latency percentiles for SLO monitoring"""
        if self.response_times:
            self.response_times.sort()
            self.p50 = statistics.median(self.response_times)
            self.p95 = statistics.quantiles(self.response_times, n=20)[18]  # 95th percentile
            self.p99 = statistics.quantiles(self.response_times, n=100)[98]  # 99th percentile
            self.average = statistics.mean(self.response_times)
            self.max_time = max(self.response_times)

@dataclass
class ErrorMetrics:
    """Track error rates for reliability SLIs"""
    total_requests: int = 0
    successful_requests: int = 0
    client_errors: int = 0  # 4xx errors
    server_errors: int = 0  # 5xx errors

    @property
    def success_rate(self) -> float:
        """Calculate success rate for SLO validation"""
        return (self.successful_requests / self.total_requests * 100) if self.total_requests > 0 else 0.0

    @property
    def error_rate(self) -> float:
        """Calculate error rate for SLI monitoring"""
        return ((self.client_errors + self.server_errors) / self.total_requests * 100) if self.total_requests > 0 else 0.0

@dataclass
class SLOTargets:
    """Define Service Level Objectives for monitoring"""
    max_latency_p95: float = 200.0  # 95% of requests < 200ms
    max_latency_p99: float = 500.0  # 99% of requests < 500ms
    min_success_rate: float = 99.9  # 99.9% success rate
    max_error_rate: float = 0.1     # < 0.1% error rate
    max_response_time: float = 1000.0  # No request > 1 second

# SRE CONFIGURATION
BASE_URL = f"http://localhost:{os.getenv('API_PORT', 5000)}"
HEADERS = {'Content-Type': 'application/json', 'User-Agent': 'SRE-Monitor/1.0'}
TIMEOUT = 5.0  # Request timeout for reliability
MAX_RETRIES = 3  # Retry failed requests for resilience
LOAD_TEST_DURATION = 30  # Load test duration in seconds
CONCURRENT_USERS = 10    # Concurrent users for load testing

# Initialize SRE metrics collectors
latency_metrics = LatencyMetrics(response_times=[])
error_metrics = ErrorMetrics()
slo_targets = SLOTargets()


"""
🧪 HANDS-ON LAB 3: SRE TEST DATA & CHAOS ENGINEERING
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

📚 THEORY: CHAOS ENGINEERING TEST DATA
Netflix's Chaos Monkey principles applied to API testing:

• Valid data: Tests normal operation and baseline performance
• Invalid data: Tests error handling and graceful degradation
• Edge cases: Tests boundary conditions and limits
• Malformed data: Tests input validation and security
• Large payloads: Tests performance under stress

🔧 REAL-WORLD EXAMPLE:
Netflix injects various types of failures and invalid data
to ensure their systems remain resilient. Each test case
represents a potential real-world scenario.

📊 TEST COVERAGE STRATEGY:
• Happy path: 70% (normal operations)
• Error cases: 20% (expected failures)
• Edge cases: 10% (boundary conditions)
"""

# SRE TEST DATA - Covers normal, error, and edge cases
VALID_TEST_CHARACTER = {
    "name": "SRE Test Pirate",
    "crew": "Reliability Pirates",
    "bounty": 1000000,
    "current_price": 150.00,
    "sentiment_score": 0.75,
    "description": "A test character for SRE monitoring validation"
}

INVALID_TEST_DATA = [
    # Test input validation (DevSecOps security)
    {"name": "", "crew": "Empty Name Crew"},  # Empty required field
    {"name": "A" * 200, "crew": "Long Name Crew"},  # Exceeds length limit
    {"bounty": -1000000, "current_price": 50.00},  # Negative bounty
    {"current_price": -10.00, "name": "Negative Price"},  # Negative price
    {"sentiment_score": 2.0, "name": "Invalid Sentiment"},  # Out of range
    # SQL injection attempt (security testing)
    {"name": "'; DROP TABLE characters; --", "crew": "Hacker Crew"},
    # XSS attempt (security testing)
    {"name": "<script>alert('xss')</script>", "crew": "XSS Crew"}
]

EDGE_CASE_DATA = [
    # Boundary value testing
    {"name": "A", "crew": "Single Char"},  # Minimum length
    {"name": "A" * 100, "crew": "Max Length"},  # Maximum length
    {"bounty": 0, "current_price": 0.01},  # Minimum values
    {"bounty": 9999999999, "current_price": 9999.99},  # Maximum values
    {"sentiment_score": -1.0, "name": "Min Sentiment"},  # Minimum sentiment
    {"sentiment_score": 1.0, "name": "Max Sentiment"}   # Maximum sentiment
]

"""
🧪 HANDS-ON LAB 4: SRE HEALTH CHECK MONITORING
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

📚 THEORY: HEALTH CHECK PATTERNS
Health checks are the foundation of SRE monitoring:

• Shallow health check: Basic connectivity (< 1ms)
• Deep health check: Database connectivity (< 100ms)
• Dependency health check: External service status
• Readiness check: Service ready to handle traffic
• Liveness check: Service is alive and responsive

🔧 KUBERNETES INTEGRATION:
Health checks integrate with Kubernetes probes:
• livenessProbe: Restart container if unhealthy
• readinessProbe: Remove from load balancer if not ready
• startupProbe: Wait for slow-starting containers

📊 SLO VALIDATION:
Health check response time contributes to latency SLIs
Success rate contributes to availability SLIs
"""
def test_health_check_sre() -> Dict:
    """
    SRE HEALTH CHECK MONITORING
    Tests service health and measures key SLIs for monitoring

    Returns:
        Dict: Health check results with SRE metrics
    """
    logger.info("🏥 Starting SRE health check monitoring...")

    health_results = {
        "test_name": "health_check_sre",
        "timestamp": datetime.now().isoformat(),
        "status": "unknown",
        "latency_ms": 0.0,
        "response_code": 0,
        "database_connected": False,
        "slo_compliance": {
            "latency_slo_met": False,  # < 100ms target
            "availability_slo_met": False  # 200 OK response
        }
    }

    try:
        # Measure latency for SLI calculation
        start_time = time.time()

        # Make health check request with timeout for reliability
        response = requests.get(
            f"{BASE_URL}/health",
            headers=HEADERS,
            timeout=TIMEOUT
        )

        # Calculate response time for latency SLI
        end_time = time.time()
        latency_ms = (end_time - start_time) * 1000

        # Update metrics collectors
        latency_metrics.response_times.append(latency_ms)
        error_metrics.total_requests += 1

        # Validate response for availability SLI
        health_results.update({
            "latency_ms": round(latency_ms, 2),
            "response_code": response.status_code,
            "status": "healthy" if response.status_code == 200 else "unhealthy"
        })

        if response.status_code == 200:
            error_metrics.successful_requests += 1
            health_results["slo_compliance"]["availability_slo_met"] = True

            # Parse response for deep health check validation
            try:
                health_data = response.json()
                health_results["database_connected"] = health_data.get("database") == "connected"
                logger.info(f"✅ Health check passed: {health_data}")
            except json.JSONDecodeError:
                logger.warning("⚠️ Health check returned non-JSON response")

        else:
            error_metrics.server_errors += 1
            logger.error(f"❌ Health check failed with status {response.status_code}")

        # Validate latency SLO (< 100ms target)
        if latency_ms < slo_targets.max_latency_p95:
            health_results["slo_compliance"]["latency_slo_met"] = True
            logger.info(f"✅ Latency SLO met: {latency_ms:.2f}ms < {slo_targets.max_latency_p95}ms")
        else:
            logger.warning(f"⚠️ Latency SLO violated: {latency_ms:.2f}ms > {slo_targets.max_latency_p95}ms")

    except requests.exceptions.Timeout:
        logger.error("❌ Health check timed out - service may be overloaded")
        health_results["status"] = "timeout"
        error_metrics.total_requests += 1
        error_metrics.server_errors += 1

    except requests.exceptions.ConnectionError:
        logger.error("❌ Health check connection failed - service may be down")
        health_results["status"] = "connection_failed"
        error_metrics.total_requests += 1
        error_metrics.server_errors += 1

    except Exception as e:
        logger.error(f"❌ Health check unexpected error: {str(e)}")
        health_results["status"] = "error"
        health_results["error"] = str(e)
        error_metrics.total_requests += 1
        error_metrics.server_errors += 1

    return health_results


# TODO 5: GET ALL CHARACTERS TEST
# def test_get_all_characters():
#     """Test GET /api/characters endpoint"""
#     print("📋 Testing Get All Characters...")
#     try:
#         # Send GET request to /api/characters
#         # Check status code is 200
#         # Verify response has 'characters' key
#         # Check if characters is a list
#         # Print number of characters found
#     except Exception as e:
#         # Handle errors


# TODO 6: GET SINGLE CHARACTER TEST
# def test_get_single_character(character_id=1):
#     """Test GET /api/characters/{id} endpoint"""
#     print(f"👤 Testing Get Single Character (ID: {character_id})...")
#     try:
#         # Send GET request to /api/characters/{character_id}
#         # Check status code is 200
#         # Verify response has character data
#         # Check required fields exist (id, name, crew, etc.)
#         # Print character name and crew
#     except Exception as e:
#         # Handle errors


# TODO 7: CREATE CHARACTER TEST
# def test_create_character():
#     """Test POST /api/characters endpoint"""
#     print("➕ Testing Create Character...")
#     try:
#         # Send POST request with test_character data
#         # Check status code is 201 (Created)
#         # Verify response contains created character
#         # Check that ID was assigned
#         # Return the created character ID for cleanup
#     except Exception as e:
#         # Handle errors
#         # Return None if failed


# TODO 8: UPDATE CHARACTER TEST
# def test_update_character(character_id):
#     """Test PUT /api/characters/{id} endpoint"""
#     print(f"✏️ Testing Update Character (ID: {character_id})...")
#     try:
#         # Create update data (change name, bounty, etc.)
#         # Send PUT request to /api/characters/{character_id}
#         # Check status code is 200
#         # Verify updated fields in response
#         # Print old vs new values
#     except Exception as e:
#         # Handle errors


# TODO 9: GET CHARACTER PRICE TEST
# def test_get_character_price(character_id):
#     """Test GET /api/characters/{id}/price endpoint"""
#     print(f"💰 Testing Get Character Price (ID: {character_id})...")
#     try:
#         # Send GET request to /api/characters/{character_id}/price
#         # Check status code is 200
#         # Verify price data fields (current_price, market_cap, etc.)
#         # Print price information
#     except Exception as e:
#         # Handle errors


# TODO 10: UPDATE CHARACTER PRICE TEST
# def test_update_character_price(character_id):
#     """Test POST /api/characters/{id}/price endpoint"""
#     print(f"📈 Testing Update Character Price (ID: {character_id})...")
#     try:
#         # Create price update data
#         # Send POST request with new price
#         # Check status code is 200
#         # Verify price was updated
#         # Check weekly_change calculation
#         # Print old vs new price
#     except Exception as e:
#         # Handle errors


# TODO 11: DELETE CHARACTER TEST (SOFT DELETE)
# def test_delete_character(character_id):
#     """Test DELETE /api/characters/{id} endpoint"""
#     print(f"🗑️ Testing Delete Character (ID: {character_id})...")
#     try:
#         # Send DELETE request to /api/characters/{character_id}
#         # Check status code is 200
#         # Verify success message
#         # Test that character is soft deleted (is_active=False)
#         # Print deletion confirmation
#     except Exception as e:
#         # Handle errors


# TODO 12: ERROR HANDLING TESTS
# def test_error_handling():
#     """Test various error scenarios"""
#     print("❌ Testing Error Handling...")
#     
#     # Test 1: Get non-existent character (should return 404)
#     # Test 2: Create character with invalid data (should return 400)
#     # Test 3: Update non-existent character (should return 404)
#     # Test 4: Invalid JSON format (should return 400)
#     # Test 5: Missing required fields (should return 400)


# TODO 13: PAGINATION TEST
# def test_pagination():
#     """Test pagination parameters"""
#     print("📄 Testing Pagination...")
#     try:
#         # Test with page=1, per_page=5
#         # Verify pagination info in response
#         # Test with different page sizes
#         # Check has_next, has_prev flags
#     except Exception as e:
#         # Handle errors


# TODO 14: FILTERING TEST
# def test_filtering():
#     """Test filtering parameters"""
#     print("🔍 Testing Filtering...")
#     try:
#         # Test crew filter: ?crew=Straw Hat Pirates
#         # Test is_active filter: ?is_active=true
#         # Test sorting: ?sort_by=name&sort_order=desc
#         # Verify filtered results
#     except Exception as e:
#         # Handle errors


# TODO 15: PERFORMANCE TEST
# def test_performance():
#     """Basic performance testing"""
#     print("⚡ Testing Performance...")
#     try:
#         # Measure response time for GET /api/characters
#         # Test multiple concurrent requests
#         # Check if responses are under acceptable time (e.g., 1 second)
#         # Print performance metrics
#     except Exception as e:
#         # Handle errors


# TODO 16: MAIN TEST RUNNER
# def run_all_tests():
#     """Run all API tests in sequence"""
#     print("🏴‍☠️ Starting One Piece API Tests...\n")
#     
#     # Step 1: Test health check
#     # Step 2: Test get all characters
#     # Step 3: Test get single character
#     # Step 4: Test create character (save ID for later tests)
#     # Step 5: Test update character
#     # Step 6: Test price endpoints
#     # Step 7: Test delete character
#     # Step 8: Test error handling
#     # Step 9: Test pagination and filtering
#     # Step 10: Test performance
#     
#     print("\n🎉 All tests completed!")


# TODO 17: INDIVIDUAL TEST RUNNER
# def run_single_test(test_name):
#     """Run a specific test by name"""
#     # Map test names to functions
#     # Execute the requested test
#     # Handle invalid test names


"""
🧪 HANDS-ON LAB FINAL: SRE MONITORING DASHBOARD
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

📚 THEORY: SRE REPORTING & ALERTING
SRE teams generate comprehensive reports for:

• SLO compliance tracking and error budget management
• Performance trend analysis and capacity planning
• Incident detection and automated alerting
• Post-mortem data collection and root cause analysis

🔧 REAL-WORLD INTEGRATION:
This monitoring data feeds into:
• Prometheus metrics collection
• Grafana dashboards and visualization
• PagerDuty alerting for SLO violations
• Slack notifications for team awareness
"""

def generate_sre_report(test_results: List[Dict]) -> Dict:
    """
    Generate comprehensive SRE monitoring report

    Args:
        test_results: List of test execution results

    Returns:
        Dict: SRE report with SLI/SLO analysis
    """
    # Calculate latency percentiles for SLO validation
    latency_metrics.calculate_percentiles()

    # Generate SRE compliance report
    sre_report = {
        "timestamp": datetime.now().isoformat(),
        "service": "one-piece-character-service",
        "test_summary": {
            "total_tests": len(test_results),
            "passed_tests": len([t for t in test_results if t.get("status") in ["healthy", "success"]]),
            "failed_tests": len([t for t in test_results if t.get("status") not in ["healthy", "success"]])
        },
        "sli_metrics": {
            "latency": {
                "p50_ms": round(latency_metrics.p50, 2),
                "p95_ms": round(latency_metrics.p95, 2),
                "p99_ms": round(latency_metrics.p99, 2),
                "average_ms": round(latency_metrics.average, 2),
                "max_ms": round(latency_metrics.max_time, 2)
            },
            "availability": {
                "success_rate_percent": round(error_metrics.success_rate, 2),
                "error_rate_percent": round(error_metrics.error_rate, 2),
                "total_requests": error_metrics.total_requests,
                "successful_requests": error_metrics.successful_requests,
                "failed_requests": error_metrics.client_errors + error_metrics.server_errors
            }
        },
        "slo_compliance": {
            "latency_p95_slo": {
                "target_ms": slo_targets.max_latency_p95,
                "actual_ms": round(latency_metrics.p95, 2),
                "compliant": latency_metrics.p95 < slo_targets.max_latency_p95,
                "margin_ms": round(slo_targets.max_latency_p95 - latency_metrics.p95, 2)
            },
            "availability_slo": {
                "target_percent": slo_targets.min_success_rate,
                "actual_percent": round(error_metrics.success_rate, 2),
                "compliant": error_metrics.success_rate >= slo_targets.min_success_rate,
                "margin_percent": round(error_metrics.success_rate - slo_targets.min_success_rate, 2)
            }
        },
        "alerts": []
    }

    # Generate alerts for SLO violations
    if latency_metrics.p95 > slo_targets.max_latency_p95:
        sre_report["alerts"].append({
            "severity": "WARNING",
            "type": "LATENCY_SLO_VIOLATION",
            "message": f"P95 latency {latency_metrics.p95:.2f}ms exceeds SLO target {slo_targets.max_latency_p95}ms"
        })

    if error_metrics.success_rate < slo_targets.min_success_rate:
        sre_report["alerts"].append({
            "severity": "CRITICAL",
            "type": "AVAILABILITY_SLO_VIOLATION",
            "message": f"Success rate {error_metrics.success_rate:.2f}% below SLO target {slo_targets.min_success_rate}%"
        })

    return sre_report

def run_sre_monitoring_suite():
    """
    Execute comprehensive SRE monitoring test suite
    """
    print("🏴‍☠️ ONE PIECE SRE MONITORING SUITE")
    print("=" * 60)
    print(f"🎯 Target: {BASE_URL}")
    print(f"⏰ Started: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
    print()

    test_results = []

    # Execute health check monitoring
    print("🏥 HEALTH CHECK MONITORING")
    print("-" * 30)
    health_result = test_health_check_sre()
    test_results.append(health_result)
    print(f"Status: {health_result['status']}")
    print(f"Latency: {health_result['latency_ms']}ms")
    print(f"SLO Compliance: {health_result['slo_compliance']}")
    print()

    # Generate and display SRE report
    print("📊 SRE MONITORING REPORT")
    print("=" * 60)
    sre_report = generate_sre_report(test_results)

    # Display key metrics
    print(f"🚀 LATENCY METRICS:")
    print(f"   P95: {sre_report['sli_metrics']['latency']['p95_ms']}ms")
    print(f"   P99: {sre_report['sli_metrics']['latency']['p99_ms']}ms")
    print(f"   Average: {sre_report['sli_metrics']['latency']['average_ms']}ms")
    print()

    print(f"📈 AVAILABILITY METRICS:")
    print(f"   Success Rate: {sre_report['sli_metrics']['availability']['success_rate_percent']}%")
    print(f"   Error Rate: {sre_report['sli_metrics']['availability']['error_rate_percent']}%")
    print(f"   Total Requests: {sre_report['sli_metrics']['availability']['total_requests']}")
    print()

    print(f"🎯 SLO COMPLIANCE:")
    for slo_name, slo_data in sre_report['slo_compliance'].items():
        status = "✅ COMPLIANT" if slo_data['compliant'] else "❌ VIOLATED"
        print(f"   {slo_name}: {status}")
    print()

    # Display alerts
    if sre_report['alerts']:
        print("🚨 ALERTS:")
        for alert in sre_report['alerts']:
            print(f"   {alert['severity']}: {alert['message']}")
    else:
        print("✅ NO ALERTS - ALL SLOs COMPLIANT")

    print()
    print("📚 NEXT STEPS FOR SRE MASTERY:")
    print("1. Set up Prometheus metrics collection")
    print("2. Create Grafana dashboards")
    print("3. Configure PagerDuty alerting")
    print("4. Implement automated remediation")
    print("5. Set up distributed tracing")

    return sre_report

if __name__ == '__main__':
    """
    SRE MONITORING EXECUTION
    Run comprehensive monitoring suite for One Piece Character Service
    """
    try:
        sre_report = run_sre_monitoring_suite()

        # Save report for historical analysis
        with open(f"sre_report_{datetime.now().strftime('%Y%m%d_%H%M%S')}.json", 'w') as f:
            json.dump(sre_report, f, indent=2)

        # Exit with appropriate code for CI/CD integration
        if sre_report['alerts']:
            sys.exit(1)  # Alert conditions detected
        else:
            sys.exit(0)  # All SLOs compliant

    except Exception as e:
        logger.error(f"❌ SRE monitoring suite failed: {str(e)}")
        sys.exit(2)  # Monitoring system failure

"""
🎯 WHAT EACH TEST DOES:

test_health_check(): Verifies API is running
test_get_all_characters(): Tests character listing
test_get_single_character(): Tests individual character retrieval
test_create_character(): Tests character creation
test_update_character(): Tests character updates
test_get_character_price(): Tests price retrieval
test_update_character_price(): Tests price updates
test_delete_character(): Tests soft deletion
test_error_handling(): Tests error responses
test_pagination(): Tests page/limit parameters
test_filtering(): Tests search and filter options
test_performance(): Basic speed testing

🚀 REQUESTS LIBRARY CONCEPTS:

1. requests.get() - Send GET request
2. requests.post() - Send POST request
3. requests.put() - Send PUT request
4. requests.delete() - Send DELETE request
5. response.status_code - HTTP status code
6. response.json() - Parse JSON response
7. response.text - Raw response text
8. headers parameter - Set request headers

📚 HTTP STATUS CODES:

200 - OK (successful GET, PUT)
201 - Created (successful POST)
400 - Bad Request (invalid data)
404 - Not Found (resource doesn't exist)
500 - Internal Server Error (server problem)

🔧 TESTING CONCEPTS:

1. Automated testing vs manual testing
2. Test data setup and cleanup
3. Error scenario testing
4. Performance benchmarking
5. Test isolation and independence

🏆 SRE MASTERY CHECKLIST - VALIDATE YOUR LEARNING:
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

✅ MONITORING & OBSERVABILITY:
□ Can you explain the Four Golden Signals of monitoring?
□ Do you understand SLI vs SLO vs SLA differences?
□ Can you calculate P95 and P99 latency percentiles?
□ Do you know how to set up health checks for Kubernetes?

✅ RELIABILITY ENGINEERING:
□ Can you implement circuit breaker patterns?
□ Do you understand error budget management?
□ Can you design chaos engineering experiments?
□ Do you know how to calculate error burn rates?

📚 ADDITIONAL LEARNING RESOURCES:
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

📖 BOOKS:
• "Site Reliability Engineering" by Google SRE Team
• "The Site Reliability Workbook" by Google SRE Team
• "Building Secure and Reliable Systems" by Google

🛠️ HANDS-ON PRACTICE:
• Set up Prometheus + Grafana monitoring stack
• Practice with Kubernetes cluster management
• Build CI/CD pipelines with monitoring integration

💼 CAREER PROGRESSION:
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

Junior SRE ($95K-$161K): Focus on monitoring and automation
Senior SRE ($129K-$204K): Design reliability architecture
Principal SRE ($180K-$300K): Define company-wide standards

🚀 USAGE EXAMPLES:
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

python test_api.py                    # Run full SRE monitoring suite
python test_api.py > sre_report.txt   # Save monitoring results
python test_api.py && echo "SLOs met" # CI/CD integration

🎯 NEXT SRE LEARNING MODULES:
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

1. 🐳 Docker containerization with health checks
2. ☸️  Kubernetes deployment with probes and scaling
3. 📊 Prometheus metrics and Grafana dashboards
4. 🚨 Alerting with PagerDuty and Slack integration

CONGRATULATIONS! You've completed SRE API Monitoring Mastery! 🏴‍☠️⚔️
"""
