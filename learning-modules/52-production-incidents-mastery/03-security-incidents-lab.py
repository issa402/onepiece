"""
═══════════════════════════════════════════════════════════════════════════════
🏆 SECURITY INCIDENT RESPONSE
═══════════════════════════════════════════════════════════════════════════════

MODULE: 52-production-incidents-mastery
LESSON: 03 - Security Incidents & Attack Mitigation

These scenarios can end careers or companies if handled poorly.
Know them. Practice them. Stay calm.
═══════════════════════════════════════════════════════════════════════════════
"""

# ═══════════════════════════════════════════════════════════════════════════════
# SCENARIO 5: DDOS ATTACK
# ═══════════════════════════════════════════════════════════════════════════════

SCENARIO_DDOS = """
┌─────────────────────────────────────────────────────────────────────────────┐
│  🚨 SCENARIO: DDOS ATTACK - SITE UNREACHABLE                                 │
├─────────────────────────────────────────────────────────────────────────────┤
│                                                                              │
│  ALERT: "Abnormal traffic spike - 10x normal requests"                      │
│                                                                              │
│  SYMPTOMS:                                                                   │
│  - Site extremely slow or down                                               │
│  - Massive traffic from many IPs                                             │
│  - Server CPU/bandwidth maxed                                                │
│  - Legitimate users can't access                                             │
│                                                                              │
│  IMMEDIATE ACTIONS:                                                          │
│                                                                              │
│  1. Enable rate limiting (if not already):                                  │
│     # nginx                                                                  │
│     limit_req_zone $binary_remote_addr zone=one:10m rate=10r/s;             │
│                                                                              │
│  2. Block obvious bad IPs:                                                  │
│     $ iptables -A INPUT -s <bad_ip> -j DROP                                 │
│     # Or use AWS WAF / Cloudflare                                           │
│                                                                              │
│  3. Enable Cloudflare "Under Attack" mode:                                  │
│     - Shows challenge page to all visitors                                   │
│     - Filters out bots                                                       │
│                                                                              │
│  4. Scale up infrastructure:                                                │
│     $ kubectl scale deployment/api --replicas=20                            │
│     # Or enable auto-scaling                                                 │
│                                                                              │
│  5. Analyze attack pattern:                                                 │
│     $ tail -f /var/log/nginx/access.log | awk '{print $1}' | sort | uniq -c │
│     # Find most frequent IPs                                                 │
│                                                                              │
│  AWS-SPECIFIC:                                                               │
│  - Enable AWS Shield (DDoS protection)                                      │
│  - Use AWS WAF rules                                                         │
│  - CloudFront for caching/distribution                                      │
│  - Contact AWS support for large attacks                                    │
│                                                                              │
│  PREVENTION:                                                                 │
│  - Always use CDN (CloudFront, Cloudflare)                                  │
│  - Rate limiting on all endpoints                                            │
│  - AWS Shield Advanced for critical apps                                    │
│  - Geographic restrictions if applicable                                     │
│                                                                              │
└─────────────────────────────────────────────────────────────────────────────┘
"""

# ═══════════════════════════════════════════════════════════════════════════════
# SCENARIO 6: SUSPECTED BREACH / UNAUTHORIZED ACCESS
# ═══════════════════════════════════════════════════════════════════════════════

SCENARIO_BREACH = """
┌─────────────────────────────────────────────────────────────────────────────┐
│  🚨 SCENARIO: SUSPECTED SECURITY BREACH                                      │
├─────────────────────────────────────────────────────────────────────────────┤
│                                                                              │
│  ALERT: "Unusual API access pattern detected"                               │
│                                                                              │
│  SYMPTOMS:                                                                   │
│  - Unusual login locations/times                                             │
│  - Mass data export                                                          │
│  - New admin users created                                                   │
│  - Suspicious processes running                                              │
│                                                                              │
│  IMMEDIATE ACTIONS (CONTAIN FIRST):                                         │
│                                                                              │
│  1. DON'T PANIC - Document everything                                       │
│     - Screenshot suspicious activity                                         │
│     - Note timestamps                                                        │
│     - Preserve logs                                                          │
│                                                                              │
│  2. Isolate affected systems:                                               │
│     - Revoke compromised credentials                                         │
│     - Block suspicious IPs                                                   │
│     - Isolate affected servers (don't delete!)                              │
│                                                                              │
│  3. Rotate all credentials:                                                 │
│     - API keys                                                               │
│     - Database passwords                                                     │
│     - SSH keys                                                               │
│     - OAuth tokens                                                           │
│                                                                              │
│  4. Check for persistence:                                                  │
│     $ crontab -l                     # Scheduled tasks                      │
│     $ cat /etc/passwd                # New users                            │
│     $ ls -la ~/.ssh/authorized_keys  # SSH keys                             │
│     $ ps aux                         # Running processes                    │
│                                                                              │
│  5. Review logs:                                                            │
│     $ grep "Failed password" /var/log/auth.log                              │
│     $ grep "Accepted" /var/log/auth.log                                     │
│     # CloudTrail for AWS API calls                                          │
│                                                                              │
│  ESCALATION:                                                                 │
│  - Notify security team immediately                                          │
│  - Notify management                                                         │
│  - Legal/compliance if data breach                                          │
│  - Consider law enforcement                                                  │
│                                                                              │
│  POST-INCIDENT:                                                              │
│  - Full forensic analysis                                                    │
│  - Determine what was accessed                                               │
│  - Notify affected users if required                                        │
│  - Implement additional security controls                                    │
│                                                                              │
└─────────────────────────────────────────────────────────────────────────────┘
"""

# ═══════════════════════════════════════════════════════════════════════════════
# SCENARIO 7: SSL CERTIFICATE EXPIRED
# ═══════════════════════════════════════════════════════════════════════════════

SCENARIO_SSL_EXPIRED = """
┌─────────────────────────────────────────────────────────────────────────────┐
│  🚨 SCENARIO: SSL CERTIFICATE EXPIRED                                        │
├─────────────────────────────────────────────────────────────────────────────┤
│                                                                              │
│  ALERT: "SSL certificate expired - users seeing security warnings"          │
│                                                                              │
│  SYMPTOMS:                                                                   │
│  - Browser showing "Not Secure" warning                                      │
│  - Users can't access site                                                   │
│  - API calls failing with SSL errors                                        │
│                                                                              │
│  IMMEDIATE FIX:                                                              │
│                                                                              │
│  1. Check certificate status:                                               │
│     $ openssl s_client -connect example.com:443 2>/dev/null | \\            │
│       openssl x509 -noout -dates                                            │
│                                                                              │
│  2. If using Let's Encrypt:                                                 │
│     $ sudo certbot renew --force-renewal                                    │
│     $ sudo systemctl reload nginx                                           │
│                                                                              │
│  3. If using AWS ACM:                                                       │
│     - ACM auto-renews, check DNS validation                                 │
│     - Verify domain ownership                                                │
│                                                                              │
│  4. Manual certificate update:                                              │
│     $ sudo cp new_cert.pem /etc/ssl/certs/                                  │
│     $ sudo cp new_key.pem /etc/ssl/private/                                 │
│     $ sudo nginx -t && sudo systemctl reload nginx                          │
│                                                                              │
│  PREVENTION:                                                                 │
│  - Use AWS ACM (auto-renewal)                                               │
│  - Monitor certificate expiry (30 day alert)                                │
│  - Automate renewal with certbot                                            │
│  - Calendar reminders as backup                                              │
│                                                                              │
│  CHECK EXPIRY:                                                               │
│  $ echo | openssl s_client -servername example.com -connect example.com:443 │
│    2>/dev/null | openssl x509 -noout -enddate                               │
│                                                                              │
└─────────────────────────────────────────────────────────────────────────────┘
"""

# ═══════════════════════════════════════════════════════════════════════════════
# DEBUGGING COMMANDS CHEAT SHEET
# ═══════════════════════════════════════════════════════════════════════════════

DEBUGGING_COMMANDS = {
    "System Resources": {
        "top / htop": "CPU and memory usage",
        "free -h": "Memory usage",
        "df -h": "Disk usage",
        "iostat": "Disk I/O",
        "netstat -tulpn": "Open ports",
        "ss -tulpn": "Socket statistics",
    },
    "Logs": {
        "tail -f /var/log/syslog": "System logs",
        "journalctl -f": "Systemd logs",
        "dmesg": "Kernel messages",
        "kubectl logs -f <pod>": "Kubernetes logs",
    },
    "Network": {
        "ping <host>": "Basic connectivity",
        "traceroute <host>": "Network path",
        "curl -v <url>": "HTTP debugging",
        "tcpdump -i eth0": "Packet capture",
        "nslookup <domain>": "DNS lookup",
    },
    "Process": {
        "ps aux": "All processes",
        "pgrep -a <name>": "Find process",
        "kill -9 <pid>": "Force kill",
        "strace -p <pid>": "System calls",
        "lsof -p <pid>": "Open files",
    }
}

