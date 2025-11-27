# 🚨 PRODUCTION INCIDENTS GUIDE - FANZONE CONNECT

## What This Document Covers

Real-world production incident scenarios and how to handle them. This is what separates junior engineers from senior engineers - the ability to stay calm and debug under pressure.

---

## Why This Matters for FANZONE CONNECT

During the **FIFA World Cup 2026**, FANZONE CONNECT will experience:
- **Traffic spikes**: 10-100x normal during popular matches
- **Global users**: Latency issues across continents
- **Real-time requirements**: Live scores, predictions, chat
- **High stakes**: Millions of users, reputation on the line

You WILL face incidents. This guide prepares you.

---

## Incident Severity Levels

| Level | Name | Description | Response Time | Example |
|-------|------|-------------|---------------|---------|
| SEV1 | Critical | Complete outage | < 5 min | Site down during World Cup Final |
| SEV2 | Major | Significant impact | < 15 min | Predictions not saving |
| SEV3 | Minor | Limited impact | < 1 hour | Slow leaderboard loading |
| SEV4 | Low | Minimal impact | Next day | UI glitch on profile page |

---

## Common Incident Scenarios

### 1. Database Down
**Symptoms**: API returning 500s, "connection refused" errors
**First Steps**:
```bash
# Check if postgres is running
sudo systemctl status postgresql

# Check disk space (common cause!)
df -h

# Check logs
sudo tail -100 /var/log/postgresql/postgresql-14-main.log
```

### 2. Memory Leak / OOM
**Symptoms**: Pods restarting, exit code 137
**First Steps**:
```bash
# Check pod status
kubectl get pods
kubectl describe pod <name>

# Check memory usage
kubectl top pods
```

### 3. Disk Full
**Symptoms**: "No space left on device" errors
**Emergency Cleanup**:
```bash
# Find what's using space
du -sh /* 2>/dev/null | sort -h

# Safe to delete
sudo rm -rf /var/log/*.gz
sudo journalctl --vacuum-size=100M
```

### 4. Bad Deployment
**Symptoms**: Errors spiking after deploy
**Immediate Action**:
```bash
# Kubernetes rollback
kubectl rollout undo deployment/api-gateway

# Verify
kubectl rollout status deployment/api-gateway
```

### 5. DDoS Attack
**Symptoms**: Massive traffic, site slow/down
**Actions**:
- Enable Cloudflare "Under Attack" mode
- Scale up infrastructure
- Block suspicious IPs
- Enable AWS Shield

### 6. SSL Certificate Expired
**Symptoms**: Browser security warnings
**Fix**:
```bash
# Let's Encrypt renewal
sudo certbot renew --force-renewal
sudo systemctl reload nginx
```

---

## First Responder Checklist

When you get paged:

1. ☐ **Acknowledge** the alert
2. ☐ **Assess** - Is this real? What's the impact?
3. ☐ **Check recent changes** - Any deployments?
4. ☐ **Determine severity** - How many users affected?
5. ☐ **Communicate** - Update incident channel
6. ☐ **Debug** - Logs, metrics, dependencies
7. ☐ **Mitigate** - Rollback? Scale up? Block traffic?

---

## Debugging Commands Cheat Sheet

### System Resources
```bash
top / htop          # CPU and memory
free -h             # Memory usage
df -h               # Disk usage
netstat -tulpn      # Open ports
```

### Logs
```bash
tail -f /var/log/syslog           # System logs
journalctl -f                      # Systemd logs
kubectl logs -f <pod>              # K8s logs
```

### Network
```bash
ping <host>                        # Connectivity
curl -v <url>                      # HTTP debug
tcpdump -i eth0                    # Packet capture
```

---

## FANZONE-Specific Scenarios

### World Cup Final Traffic Spike
- Pre-scale 2 hours before match
- Enable aggressive caching
- Have rollback plan ready
- Monitor in real-time

### Match Service Failure
- Fallback to cached scores
- Display "updating..." message
- Don't crash the whole app

### Prediction Submission Flood
- Queue-based processing
- Rate limiting per user
- Graceful degradation

---

## Post-Incident

After every incident:
1. **Timeline** - What happened when
2. **Root cause** - Why did it happen
3. **What went well** - What helped
4. **What went poorly** - What made it worse
5. **Action items** - How to prevent recurrence

---

## Learning Modules

See the detailed learning modules:
- `learning-modules/52-production-incidents-mastery/01-incident-response-coding-lab.py`
- `learning-modules/52-production-incidents-mastery/02-common-incidents-scenarios.py`
- `learning-modules/52-production-incidents-mastery/03-security-incidents-lab.py`

---

## The Reality

> "Everyone has a plan until they get punched in the face." - Mike Tyson

Production incidents are stressful. The key is:
- **Stay calm**
- **Communicate clearly**
- **Focus on mitigation first, root cause later**
- **Learn from every incident**

This is how you become a senior engineer. 🚀

