"""
═══════════════════════════════════════════════════════════════════════════════
🏆 PRODUCTION INCIDENTS MASTERY
═══════════════════════════════════════════════════════════════════════════════

MODULE: 52-production-incidents-mastery
LESSON: 01 - Incident Response & Real-World Debugging

WHAT YOU'LL LEARN:
├── Incident Response Process
│   ├── Detection & Alerting
│   ├── Triage & Severity
│   ├── Investigation
│   └── Resolution & Postmortem
├── Common Production Issues
│   ├── Database Problems
│   ├── Memory/CPU Issues
│   ├── Disk Space
│   ├── Network Problems
│   └── Security Incidents
├── Debugging Tools & Techniques
│   ├── Log Analysis
│   ├── Metrics & Monitoring
│   ├── Profiling
│   └── Distributed Tracing
└── Real Incident Scenarios
    ├── Database Down at 3am
    ├── Memory Leak Crashing App
    ├── DDoS Attack
    └── Bad Deployment Rollback

WHY THIS MATTERS:
- This is what separates juniors from seniors
- Companies pay $200k+ for people who can handle incidents
- You WILL face these situations in your career
- Calm under pressure = career advancement
═══════════════════════════════════════════════════════════════════════════════
"""

# ═══════════════════════════════════════════════════════════════════════════════
# SECTION 1: INCIDENT RESPONSE PROCESS
# ═══════════════════════════════════════════════════════════════════════════════

INCIDENT_RESPONSE_PROCESS = """
┌─────────────────────────────────────────────────────────────────────────────┐
│                    INCIDENT RESPONSE LIFECYCLE                               │
├─────────────────────────────────────────────────────────────────────────────┤
│                                                                              │
│  1. DETECTION                                                                │
│     ├── Monitoring alerts (PagerDuty, OpsGenie)                             │
│     ├── Customer reports                                                     │
│     ├── Automated health checks                                              │
│     └── Log anomaly detection                                                │
│                                                                              │
│  2. TRIAGE                                                                   │
│     ├── Assess severity (SEV1-4)                                            │
│     ├── Identify affected systems                                            │
│     ├── Estimate user impact                                                 │
│     └── Decide: page more people?                                            │
│                                                                              │
│  3. INVESTIGATION                                                            │
│     ├── Check recent changes (deployments, config)                          │
│     ├── Review logs and metrics                                              │
│     ├── Reproduce if possible                                                │
│     └── Form hypothesis                                                      │
│                                                                              │
│  4. MITIGATION                                                               │
│     ├── Quick fix to stop bleeding                                           │
│     ├── Rollback if deployment-related                                       │
│     ├── Scale up if capacity issue                                           │
│     └── Block bad traffic if attack                                          │
│                                                                              │
│  5. RESOLUTION                                                               │
│     ├── Implement proper fix                                                 │
│     ├── Verify fix works                                                     │
│     ├── Monitor for recurrence                                               │
│     └── Update status page                                                   │
│                                                                              │
│  6. POSTMORTEM                                                               │
│     ├── Timeline of events                                                   │
│     ├── Root cause analysis                                                  │
│     ├── What went well/poorly                                                │
│     └── Action items to prevent recurrence                                   │
│                                                                              │
└─────────────────────────────────────────────────────────────────────────────┘
"""

# ═══════════════════════════════════════════════════════════════════════════════
# SECTION 2: SEVERITY LEVELS
# ═══════════════════════════════════════════════════════════════════════════════

SEVERITY_LEVELS = {
    "SEV1": {
        "name": "Critical",
        "description": "Complete outage, all users affected",
        "examples": [
            "Site completely down",
            "Data breach in progress",
            "Payment processing broken"
        ],
        "response_time": "Immediate (< 5 min)",
        "who_to_page": "On-call + Engineering Manager + VP",
        "communication": "Status page update every 15 min"
    },
    
    "SEV2": {
        "name": "Major",
        "description": "Significant impact, many users affected",
        "examples": [
            "Major feature broken",
            "Significant performance degradation",
            "Data inconsistency"
        ],
        "response_time": "< 15 min",
        "who_to_page": "On-call + relevant team lead",
        "communication": "Status page update every 30 min"
    },
    
    "SEV3": {
        "name": "Minor",
        "description": "Limited impact, workaround available",
        "examples": [
            "Minor feature broken",
            "Slow but functional",
            "Affects small user segment"
        ],
        "response_time": "< 1 hour",
        "who_to_page": "On-call only",
        "communication": "Internal update"
    },
    
    "SEV4": {
        "name": "Low",
        "description": "Minimal impact, cosmetic issues",
        "examples": [
            "UI glitch",
            "Non-critical error in logs",
            "Minor performance issue"
        ],
        "response_time": "Next business day",
        "who_to_page": "No page, create ticket",
        "communication": "None required"
    }
}

# ═══════════════════════════════════════════════════════════════════════════════
# SECTION 3: FIRST RESPONDER CHECKLIST
# ═══════════════════════════════════════════════════════════════════════════════

FIRST_RESPONDER_CHECKLIST = """
┌─────────────────────────────────────────────────────────────────────────────┐
│              FIRST RESPONDER CHECKLIST (When Paged)                          │
├─────────────────────────────────────────────────────────────────────────────┤
│                                                                              │
│  □ 1. ACKNOWLEDGE THE ALERT                                                  │
│       - Ack in PagerDuty/OpsGenie                                           │
│       - Join incident Slack channel                                          │
│       - Start incident timer                                                 │
│                                                                              │
│  □ 2. ASSESS THE SITUATION (2 min)                                          │
│       - What's the alert saying?                                             │
│       - Check monitoring dashboards                                          │
│       - Is this real or false positive?                                      │
│                                                                              │
│  □ 3. CHECK RECENT CHANGES (2 min)                                          │
│       - Any deployments in last hour?                                        │
│       - Any config changes?                                                  │
│       - Any infrastructure changes?                                          │
│                                                                              │
│  □ 4. DETERMINE SEVERITY                                                     │
│       - How many users affected?                                             │
│       - Is there a workaround?                                               │
│       - Is data at risk?                                                     │
│                                                                              │
│  □ 5. COMMUNICATE                                                            │
│       - Update incident channel                                              │
│       - Page additional help if needed                                       │
│       - Update status page if customer-facing                               │
│                                                                              │
│  □ 6. START DEBUGGING                                                        │
│       - Check logs (CloudWatch, ELK, etc.)                                  │
│       - Check metrics (CPU, memory, latency)                                │
│       - Check dependencies (DB, cache, external APIs)                       │
│                                                                              │
│  □ 7. MITIGATE                                                               │
│       - Can we rollback?                                                     │
│       - Can we scale up?                                                     │
│       - Can we failover?                                                     │
│       - Can we block bad traffic?                                            │
│                                                                              │
└─────────────────────────────────────────────────────────────────────────────┘
"""

