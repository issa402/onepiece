"""
═══════════════════════════════════════════════════════════════════════════════
🏆 COMMON PRODUCTION INCIDENT SCENARIOS
═══════════════════════════════════════════════════════════════════════════════

MODULE: 52-production-incidents-mastery
LESSON: 02 - Real-World Incident Scenarios & Solutions

These are REAL scenarios you WILL face in your career.
Study them. Memorize the debugging steps.
═══════════════════════════════════════════════════════════════════════════════
"""

# ═══════════════════════════════════════════════════════════════════════════════
# SCENARIO 1: DATABASE DOWN AT 3AM
# ═══════════════════════════════════════════════════════════════════════════════

SCENARIO_DATABASE_DOWN = """
┌─────────────────────────────────────────────────────────────────────────────┐
│  🚨 SCENARIO: DATABASE DOWN AT 3AM                                           │
├─────────────────────────────────────────────────────────────────────────────┤
│                                                                              │
│  ALERT: "PostgreSQL connection refused - all API requests failing"          │
│                                                                              │
│  SYMPTOMS:                                                                   │
│  - API returning 500 errors                                                  │
│  - "connection refused" in logs                                              │
│  - Database metrics show 0 connections                                       │
│                                                                              │
│  DEBUGGING STEPS:                                                            │
│                                                                              │
│  1. Check if database process is running:                                    │
│     $ ssh db-server                                                          │
│     $ sudo systemctl status postgresql                                       │
│     $ ps aux | grep postgres                                                 │
│                                                                              │
│  2. Check database logs:                                                     │
│     $ sudo tail -100 /var/log/postgresql/postgresql-14-main.log             │
│                                                                              │
│  3. Check disk space (common cause!):                                        │
│     $ df -h                                                                  │
│     $ du -sh /var/lib/postgresql/*                                          │
│                                                                              │
│  4. Check memory:                                                            │
│     $ free -h                                                                │
│     $ dmesg | grep -i "out of memory"                                       │
│                                                                              │
│  5. Try to start database:                                                   │
│     $ sudo systemctl start postgresql                                        │
│     $ sudo journalctl -u postgresql -n 50                                   │
│                                                                              │
│  COMMON CAUSES & FIXES:                                                      │
│                                                                              │
│  ┌─────────────────────┬────────────────────────────────────────────────┐   │
│  │ Cause               │ Fix                                            │   │
│  ├─────────────────────┼────────────────────────────────────────────────┤   │
│  │ Disk full           │ Delete old logs, expand volume                 │   │
│  │ OOM killed          │ Increase memory, tune postgres config          │   │
│  │ Corrupted WAL       │ Restore from backup                            │   │
│  │ Max connections     │ Increase max_connections, use pgbouncer        │   │
│  │ Lock contention     │ Kill blocking queries                          │   │
│  └─────────────────────┴────────────────────────────────────────────────┘   │
│                                                                              │
│  PREVENTION:                                                                 │
│  - Monitor disk space with alerts at 80%                                    │
│  - Set up automated log rotation                                             │
│  - Use connection pooling (pgbouncer)                                       │
│  - Regular backups tested monthly                                            │
│                                                                              │
└─────────────────────────────────────────────────────────────────────────────┘
"""

# ═══════════════════════════════════════════════════════════════════════════════
# SCENARIO 2: MEMORY LEAK CRASHING APPLICATION
# ═══════════════════════════════════════════════════════════════════════════════

SCENARIO_MEMORY_LEAK = """
┌─────────────────────────────────────────────────────────────────────────────┐
│  🚨 SCENARIO: MEMORY LEAK CRASHING APPLICATION                               │
├─────────────────────────────────────────────────────────────────────────────┤
│                                                                              │
│  ALERT: "Pod OOMKilled - restarting frequently"                             │
│                                                                              │
│  SYMPTOMS:                                                                   │
│  - Pods restarting every few hours                                          │
│  - Memory usage climbing steadily                                            │
│  - Exit code 137 (OOMKilled)                                                │
│  - Slow response times before crash                                          │
│                                                                              │
│  DEBUGGING STEPS:                                                            │
│                                                                              │
│  1. Check pod status and restarts:                                          │
│     $ kubectl get pods                                                       │
│     $ kubectl describe pod <name>  # Look for OOMKilled                     │
│                                                                              │
│  2. Check memory metrics:                                                    │
│     $ kubectl top pods                                                       │
│     # Look at Grafana/CloudWatch for memory trend                           │
│                                                                              │
│  3. Get heap dump (if Java):                                                │
│     $ kubectl exec <pod> -- jmap -dump:format=b,file=/tmp/heap.bin <pid>   │
│                                                                              │
│  4. Profile memory (Python):                                                │
│     # Add memory_profiler to code                                           │
│     # Or use tracemalloc                                                    │
│                                                                              │
│  5. Check for common leaks:                                                 │
│     - Unclosed database connections                                          │
│     - Growing caches without eviction                                        │
│     - Event listeners not removed                                            │
│     - Large objects in global scope                                          │
│                                                                              │
│  IMMEDIATE MITIGATION:                                                       │
│  - Increase memory limits (temporary)                                        │
│  - Scale horizontally (more pods)                                            │
│  - Restart pods on schedule (cron)                                          │
│                                                                              │
│  LONG-TERM FIX:                                                              │
│  - Find and fix the leak in code                                            │
│  - Add memory monitoring/alerting                                            │
│  - Implement proper resource cleanup                                         │
│                                                                              │
└─────────────────────────────────────────────────────────────────────────────┘
"""

# ═══════════════════════════════════════════════════════════════════════════════
# SCENARIO 3: DISK FULL EMERGENCY
# ═══════════════════════════════════════════════════════════════════════════════

SCENARIO_DISK_FULL = """
┌─────────────────────────────────────────────────────────────────────────────┐
│  🚨 SCENARIO: DISK FULL - SERVICES FAILING                                   │
├─────────────────────────────────────────────────────────────────────────────┤
│                                                                              │
│  ALERT: "Disk usage > 95% on production server"                             │
│                                                                              │
│  SYMPTOMS:                                                                   │
│  - "No space left on device" errors                                         │
│  - Database refusing writes                                                  │
│  - Logs not being written                                                    │
│  - Application crashes                                                       │
│                                                                              │
│  EMERGENCY CLEANUP (in order of safety):                                    │
│                                                                              │
│  1. Check what's using space:                                               │
│     $ df -h                          # Overall disk usage                   │
│     $ du -sh /* 2>/dev/null | sort -h  # Biggest directories               │
│     $ du -sh /var/log/*              # Log sizes                            │
│                                                                              │
│  2. Safe to delete immediately:                                             │
│     $ sudo rm -rf /var/log/*.gz      # Old compressed logs                  │
│     $ sudo rm -rf /tmp/*             # Temp files                           │
│     $ sudo journalctl --vacuum-size=100M  # Systemd logs                   │
│                                                                              │
│  3. Find large files:                                                       │
│     $ find / -type f -size +100M 2>/dev/null                               │
│                                                                              │
│  4. Check for deleted but open files:                                       │
│     $ lsof | grep deleted            # Files deleted but held open          │
│     # Restart the process holding them                                      │
│                                                                              │
│  5. Docker cleanup (if applicable):                                         │
│     $ docker system prune -a         # Remove unused images/containers      │
│                                                                              │
│  PREVENTION:                                                                 │
│  - Log rotation (logrotate)                                                 │
│  - Disk usage alerts at 70%, 80%, 90%                                       │
│  - Automated cleanup scripts                                                 │
│  - Separate volumes for logs/data                                            │
│                                                                              │
└─────────────────────────────────────────────────────────────────────────────┘
"""

# ═══════════════════════════════════════════════════════════════════════════════
# SCENARIO 4: BAD DEPLOYMENT - NEED TO ROLLBACK
# ═══════════════════════════════════════════════════════════════════════════════

SCENARIO_BAD_DEPLOYMENT = """
┌─────────────────────────────────────────────────────────────────────────────┐
│  🚨 SCENARIO: BAD DEPLOYMENT - ERRORS SPIKING                                │
├─────────────────────────────────────────────────────────────────────────────┤
│                                                                              │
│  ALERT: "Error rate > 5% after deployment"                                  │
│                                                                              │
│  SYMPTOMS:                                                                   │
│  - 500 errors spiking after deploy                                          │
│  - New exceptions in logs                                                    │
│  - Customer complaints                                                       │
│                                                                              │
│  IMMEDIATE ACTION - ROLLBACK:                                               │
│                                                                              │
│  Kubernetes:                                                                 │
│  $ kubectl rollout undo deployment/api-gateway                              │
│  $ kubectl rollout status deployment/api-gateway                            │
│                                                                              │
│  Docker Compose:                                                             │
│  $ docker-compose pull  # Get previous image                                │
│  $ docker-compose up -d                                                      │
│                                                                              │
│  AWS ECS:                                                                    │
│  $ aws ecs update-service --cluster prod --service api \\                   │
│      --task-definition api:PREVIOUS_VERSION                                 │
│                                                                              │
│  AFTER ROLLBACK:                                                             │
│                                                                              │
│  1. Verify rollback successful:                                             │
│     - Error rate back to normal                                              │
│     - Check version running                                                  │
│                                                                              │
│  2. Investigate what went wrong:                                            │
│     - Check deployment diff                                                  │
│     - Review logs from bad version                                           │
│     - Check if tests passed                                                  │
│                                                                              │
│  3. Fix and redeploy:                                                       │
│     - Fix the bug                                                            │
│     - Add test for this case                                                 │
│     - Deploy to staging first                                                │
│     - Gradual rollout (canary)                                              │
│                                                                              │
│  PREVENTION:                                                                 │
│  - Canary deployments (10% traffic first)                                   │
│  - Automated rollback on error spike                                        │
│  - Feature flags for new code                                                │
│  - Better staging environment                                                │
│                                                                              │
└─────────────────────────────────────────────────────────────────────────────┘
"""

