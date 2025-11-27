# 🏆 FANZONE CONNECT - Kubernetes Integration Guide

## What is Kubernetes?

Kubernetes (K8s) is a container orchestration platform. It automates deploying, scaling, and managing containerized applications.

**Think of it like this:**
- Docker = creates containers (packages your app)
- Kubernetes = manages containers at scale (runs 100s of containers across servers)

## Why Kubernetes for FANZONE CONNECT?

During the World Cup:
- **Traffic spikes** during matches (millions of users)
- **Zero downtime** required during updates
- **Auto-scaling** to handle load
- **Self-healing** - crashed containers restart automatically

## FANZONE Kubernetes Architecture

```
                    Internet
                       │
                       ▼
              ┌─────────────────┐
              │     Ingress     │  ← Routes traffic by path/host
              │  (nginx/traefik)│
              └────────┬────────┘
                       │
        ┌──────────────┼──────────────┐
        ▼              ▼              ▼
   ┌─────────┐   ┌─────────┐   ┌─────────┐
   │   API   │   │  Match  │   │  User   │
   │ Gateway │   │ Service │   │ Service │
   │ (3 pods)│   │ (5 pods)│   │ (3 pods)│
   └────┬────┘   └────┬────┘   └────┬────┘
        │             │             │
        └─────────────┴─────────────┘
                      │
        ┌─────────────┼─────────────┐
        ▼             ▼             ▼
   ┌─────────┐  ┌─────────┐  ┌─────────┐
   │ Postgres│  │  Redis  │  │ MongoDB │
   │ (State- │  │(Cluster)│  │(Replica │
   │ fulSet) │  │         │  │  Set)   │
   └─────────┘  └─────────┘  └─────────┘
```

## Files in `k8s/` Directory

| File | Purpose |
|------|---------|
| `namespace.yaml` | Isolated environment for FANZONE resources |
| `api-gateway-deployment.yaml` | Main API - 3 replicas, rolling updates |
| `services.yaml` | Network endpoints for each component |
| `ingress.yaml` | External traffic routing, SSL termination |
| `configmaps-secrets.yaml` | Configuration and credentials |
| `hpa.yaml` | Auto-scaling based on CPU/memory |
| `postgres-statefulset.yaml` | Database with persistent storage |

## Key Concepts for FANZONE

### 1. Pods
Smallest unit. One or more containers that share storage/network.
```yaml
# Our API Gateway runs as a pod
spec:
  containers:
  - name: api-gateway
    image: ghcr.io/fanzone/api-gateway:latest
```

### 2. Deployments
Manages pods - handles replicas, updates, rollbacks.
```yaml
# Run 3 copies of API Gateway
spec:
  replicas: 3
  strategy:
    type: RollingUpdate  # Zero-downtime updates
```

### 3. Services
Stable network endpoint for pods (pods have random IPs).
```yaml
# Internal DNS: http://match-service:8002
spec:
  type: ClusterIP
  selector:
    app: match-service
```

### 4. Horizontal Pod Autoscaler (HPA)
Automatically scales pods based on load.
```yaml
# Scale from 3 to 20 pods when CPU > 70%
spec:
  minReplicas: 3
  maxReplicas: 20
  metrics:
  - type: Resource
    resource:
      name: cpu
      target:
        averageUtilization: 70
```

### 5. ConfigMaps & Secrets
Separate config from code.
```yaml
# Environment-specific settings
data:
  APP_ENV: "production"
  REDIS_HOST: "redis"
```

## Deployment Commands

```bash
# Apply all configs
kubectl apply -f k8s/

# Check status
kubectl get pods -n fanzone-connect
kubectl get services -n fanzone-connect

# View logs
kubectl logs -f deployment/api-gateway -n fanzone-connect

# Scale manually (for testing)
kubectl scale deployment/api-gateway --replicas=5

# Rollback bad deployment
kubectl rollout undo deployment/api-gateway
```

## World Cup Traffic Handling

```yaml
# Pre-scale before known match times
# Using KEDA scheduled scaling
spec:
  triggers:
  - type: cron
    metadata:
      timezone: UTC
      start: "0 13 * * *"  # 30 min before match
      end: "0 16 * * *"
      desiredReplicas: "15"
```

## What This Teaches You

| Skill | Where It's Used |
|-------|-----------------|
| YAML syntax | All K8s configs |
| Container orchestration | Deployments, StatefulSets |
| Networking | Services, Ingress |
| Scaling | HPA, replica management |
| Configuration management | ConfigMaps, Secrets |
| Storage | PersistentVolumeClaims |
| Monitoring | Probes, resource limits |

## Next Steps

1. **Study each YAML file** - understand every field
2. **Set up minikube** locally to practice
3. **Deploy FANZONE** to a real cluster (EKS, GKE, AKS)
4. **Break things** - delete pods, watch them recover
5. **Learn Helm** - templating for Kubernetes

