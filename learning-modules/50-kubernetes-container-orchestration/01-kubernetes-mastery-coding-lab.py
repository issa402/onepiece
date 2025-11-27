"""
═══════════════════════════════════════════════════════════════════════════════
🏆 KUBERNETES CONTAINER ORCHESTRATION MASTERY
═══════════════════════════════════════════════════════════════════════════════

MODULE: 50-kubernetes-container-orchestration
LESSON: 01 - Kubernetes Fundamentals & Architecture

WHAT YOU'LL LEARN:
├── Kubernetes Architecture
│   ├── Control Plane Components
│   ├── Worker Node Components
│   └── How They Communicate
├── Core Kubernetes Objects
│   ├── Pods, ReplicaSets, Deployments
│   ├── Services, Ingress
│   ├── ConfigMaps, Secrets
│   └── Volumes, PersistentVolumeClaims
├── Networking
│   ├── Pod-to-Pod Communication
│   ├── Service Discovery
│   └── Ingress Controllers
├── Scaling & Self-Healing
│   ├── Horizontal Pod Autoscaler
│   ├── Liveness & Readiness Probes
│   └── Rolling Updates & Rollbacks
└── Real-World Patterns
    ├── Sidecar, Ambassador, Adapter
    ├── StatefulSets for Databases
    └── Jobs & CronJobs

WHY KUBERNETES MATTERS:
- Industry standard for container orchestration
- Required skill for DevOps/Platform Engineering
- $150k+ salaries for Kubernetes experts
- Every major company uses it (Google, Netflix, Spotify)
═══════════════════════════════════════════════════════════════════════════════
"""

# ═══════════════════════════════════════════════════════════════════════════════
# SECTION 1: KUBERNETES ARCHITECTURE
# ═══════════════════════════════════════════════════════════════════════════════

KUBERNETES_ARCHITECTURE = """
┌─────────────────────────────────────────────────────────────────────────────┐
│                           KUBERNETES CLUSTER                                 │
├─────────────────────────────────────────────────────────────────────────────┤
│                                                                              │
│  ┌────────────────────────────────────────────────────────────────────────┐ │
│  │                        CONTROL PLANE (Master)                          │ │
│  │  ┌──────────────┐  ┌──────────────┐  ┌──────────────┐  ┌────────────┐ │ │
│  │  │  API Server  │  │  Scheduler   │  │  Controller  │  │    etcd    │ │ │
│  │  │              │  │              │  │   Manager    │  │ (database) │ │ │
│  │  │ - REST API   │  │ - Assigns    │  │              │  │            │ │ │
│  │  │ - Auth/Authz │  │   pods to    │  │ - Node       │  │ - Stores   │ │ │
│  │  │ - Validation │  │   nodes      │  │ - Replication│  │   cluster  │ │ │
│  │  │              │  │ - Resource   │  │ - Endpoint   │  │   state    │ │ │
│  │  │              │  │   aware      │  │ - Service    │  │            │ │ │
│  │  └──────────────┘  └──────────────┘  └──────────────┘  └────────────┘ │ │
│  └────────────────────────────────────────────────────────────────────────┘ │
│                                    │                                         │
│                                    ▼                                         │
│  ┌────────────────────────────────────────────────────────────────────────┐ │
│  │                         WORKER NODES                                    │ │
│  │  ┌─────────────────────────┐      ┌─────────────────────────┐          │ │
│  │  │       NODE 1            │      │       NODE 2            │          │ │
│  │  │  ┌───────────────────┐  │      │  ┌───────────────────┐  │          │ │
│  │  │  │     kubelet       │  │      │  │     kubelet       │  │          │ │
│  │  │  │ - Runs pods       │  │      │  │ - Runs pods       │  │          │ │
│  │  │  │ - Reports status  │  │      │  │ - Reports status  │  │          │ │
│  │  │  └───────────────────┘  │      │  └───────────────────┘  │          │ │
│  │  │  ┌───────────────────┐  │      │  ┌───────────────────┐  │          │ │
│  │  │  │    kube-proxy     │  │      │  │    kube-proxy     │  │          │ │
│  │  │  │ - Network rules   │  │      │  │ - Network rules   │  │          │ │
│  │  │  │ - Load balancing  │  │      │  │ - Load balancing  │  │          │ │
│  │  │  └───────────────────┘  │      │  └───────────────────┘  │          │ │
│  │  │  ┌───────────────────┐  │      │  ┌───────────────────┐  │          │ │
│  │  │  │ Container Runtime │  │      │  │ Container Runtime │  │          │ │
│  │  │  │ (containerd)      │  │      │  │ (containerd)      │  │          │ │
│  │  │  └───────────────────┘  │      │  └───────────────────┘  │          │ │
│  │  │  ┌─────┐ ┌─────┐ ┌─────┐│      │  ┌─────┐ ┌─────┐       │          │ │
│  │  │  │ Pod │ │ Pod │ │ Pod ││      │  │ Pod │ │ Pod │       │          │ │
│  │  │  └─────┘ └─────┘ └─────┘│      │  └─────┘ └─────┘       │          │ │
│  │  └─────────────────────────┘      └─────────────────────────┘          │ │
│  └────────────────────────────────────────────────────────────────────────┘ │
└─────────────────────────────────────────────────────────────────────────────┘
"""

# ═══════════════════════════════════════════════════════════════════════════════
# SECTION 2: CONTROL PLANE COMPONENTS (Deep Dive)
# ═══════════════════════════════════════════════════════════════════════════════

CONTROL_PLANE_COMPONENTS = {
    "api_server": {
        "purpose": "Front door to the cluster - all communication goes through it",
        "responsibilities": [
            "REST API endpoint for all operations",
            "Authentication and Authorization",
            "Validation of API objects",
            "Serves as cluster gateway"
        ],
        "port": 6443,
        "command": "kubectl communicates with API server"
    },
    "etcd": {
        "purpose": "Distributed key-value store - cluster's brain/memory",
        "responsibilities": [
            "Stores all cluster state",
            "Highly available (odd number of nodes)",
            "Consistent reads/writes",
            "Backup this = backup your cluster"
        ],
        "port": 2379,
        "critical": "If etcd dies, cluster state is lost"
    },
    "scheduler": {
        "purpose": "Assigns pods to nodes based on constraints",
        "factors_considered": [
            "Resource requirements (CPU, memory)",
            "Node affinity/anti-affinity",
            "Taints and tolerations",
            "Pod priority",
            "Data locality"
        ],
        "process": "Watch for unscheduled pods → Find best node → Bind pod to node"
    },
    "controller_manager": {
        "purpose": "Runs controller loops that regulate cluster state",
        "controllers": [
            "Node Controller - monitors node health",
            "Replication Controller - maintains pod count",
            "Endpoint Controller - populates Services",
            "Service Account Controller - creates accounts/tokens"
        ],
        "pattern": "Watch current state → Compare to desired state → Take action"
    }
}

# ═══════════════════════════════════════════════════════════════════════════════
# SECTION 3: CORE KUBERNETES OBJECTS
# ═══════════════════════════════════════════════════════════════════════════════

# TODO: Study each object and understand when to use it

class Pod:
    """
    SMALLEST DEPLOYABLE UNIT IN KUBERNETES
    
    A pod is one or more containers that:
    - Share the same network namespace (localhost)
    - Share storage volumes
    - Have the same lifecycle
    
    Usually: 1 pod = 1 container (but can have sidecars)
    """
    
    yaml_example = """
    apiVersion: v1
    kind: Pod
    metadata:
      name: fanzone-api
      labels:
        app: api-gateway
    spec:
      containers:
      - name: api
        image: fanzone/api:latest
        ports:
        - containerPort: 8000
        resources:
          requests:
            cpu: "100m"
            memory: "128Mi"
          limits:
            cpu: "500m"
            memory: "512Mi"
    """
    
    # TODO: Explain why we rarely create pods directly
    # (Use Deployments instead for self-healing)
    pass


class Deployment:
    """
    MANAGES PODS WITH REPLICAS AND UPDATES
    
    Deployment → creates ReplicaSet → creates Pods
    
    Benefits:
    - Maintains desired number of replicas
    - Rolling updates (zero downtime)
    - Rollback capability
    - Self-healing (recreates crashed pods)
    """
    
    yaml_example = """
    apiVersion: apps/v1
    kind: Deployment
    metadata:
      name: api-gateway
    spec:
      replicas: 3
      selector:
        matchLabels:
          app: api-gateway
      strategy:
        type: RollingUpdate
        rollingUpdate:
          maxSurge: 1
          maxUnavailable: 0
      template:
        metadata:
          labels:
            app: api-gateway
        spec:
          containers:
          - name: api
            image: fanzone/api:v1.2.0
            # ... container spec
    """
    
    # TODO: Practice rolling update
    # kubectl set image deployment/api-gateway api=fanzone/api:v1.3.0
    pass


class Service:
    """
    STABLE NETWORK ENDPOINT FOR PODS
    
    Pods have random IPs that change. Services provide:
    - Stable IP address
    - DNS name (service-name.namespace.svc.cluster.local)
    - Load balancing across pods
    
    Types:
    - ClusterIP: Internal only (default)
    - NodePort: Expose on each node's IP:port
    - LoadBalancer: Cloud provider load balancer
    - ExternalName: DNS alias
    """
    
    yaml_example = """
    apiVersion: v1
    kind: Service
    metadata:
      name: api-gateway
    spec:
      type: ClusterIP
      selector:
        app: api-gateway  # Routes to pods with this label
      ports:
      - port: 80          # Service port
        targetPort: 8000  # Container port
    """
    
    # TODO: Understand how selectors match pods
    pass


class Ingress:
    """
    HTTP/HTTPS ROUTING TO SERVICES
    
    Single entry point for multiple services:
    - Path-based routing (/api → api-service, /web → web-service)
    - Host-based routing (api.example.com, www.example.com)
    - SSL/TLS termination
    - Rate limiting, authentication
    
    Requires: Ingress Controller (nginx-ingress, traefik, etc.)
    """
    
    yaml_example = """
    apiVersion: networking.k8s.io/v1
    kind: Ingress
    metadata:
      name: fanzone-ingress
      annotations:
        nginx.ingress.kubernetes.io/ssl-redirect: "true"
    spec:
      tls:
      - hosts:
        - api.fanzone.com
        secretName: tls-secret
      rules:
      - host: api.fanzone.com
        http:
          paths:
          - path: /
            pathType: Prefix
            backend:
              service:
                name: api-gateway
                port:
                  number: 80
    """
    pass


# ═══════════════════════════════════════════════════════════════════════════════
# SECTION 4: CONFIGURATION MANAGEMENT
# ═══════════════════════════════════════════════════════════════════════════════

class ConfigMap:
    """
    STORE NON-SENSITIVE CONFIGURATION
    
    Use for:
    - Environment variables
    - Config files
    - Command-line arguments
    
    NOT for passwords/secrets!
    """
    
    yaml_example = """
    apiVersion: v1
    kind: ConfigMap
    metadata:
      name: app-config
    data:
      APP_ENV: "production"
      LOG_LEVEL: "info"
      config.json: |
        {
          "feature_flags": {
            "new_ui": true
          }
        }
    """
    pass


class Secret:
    """
    STORE SENSITIVE DATA
    
    Base64 encoded (NOT encrypted by default!)
    For real security: use external secret management
    (HashiCorp Vault, AWS Secrets Manager, etc.)
    """
    
    yaml_example = """
    apiVersion: v1
    kind: Secret
    metadata:
      name: db-credentials
    type: Opaque
    data:
      username: YWRtaW4=      # base64 of 'admin'
      password: cGFzc3dvcmQ=  # base64 of 'password'
    """
    
    # Create secret from command line:
    # kubectl create secret generic db-creds --from-literal=password=mysecret
    pass

