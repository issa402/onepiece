"""
═══════════════════════════════════════════════════════════════════════════════
🏆 KUBECTL COMMANDS MASTERY
═══════════════════════════════════════════════════════════════════════════════

MODULE: 50-kubernetes-container-orchestration
LESSON: 02 - Essential kubectl Commands

kubectl = Kubernetes command-line tool
Communicates with API Server to manage cluster
═══════════════════════════════════════════════════════════════════════════════
"""

# ═══════════════════════════════════════════════════════════════════════════════
# KUBECTL COMMAND REFERENCE
# ═══════════════════════════════════════════════════════════════════════════════

KUBECTL_COMMANDS = {
    # ─────────────────────────────────────────────────────────────────────────
    # CLUSTER INFO
    # ─────────────────────────────────────────────────────────────────────────
    "cluster_info": {
        "kubectl cluster-info": "Display cluster info",
        "kubectl get nodes": "List all nodes",
        "kubectl describe node <name>": "Detailed node info",
        "kubectl top nodes": "Node resource usage",
        "kubectl get namespaces": "List namespaces",
    },
    
    # ─────────────────────────────────────────────────────────────────────────
    # PODS
    # ─────────────────────────────────────────────────────────────────────────
    "pods": {
        "kubectl get pods": "List pods in current namespace",
        "kubectl get pods -A": "List pods in ALL namespaces",
        "kubectl get pods -n <namespace>": "List pods in specific namespace",
        "kubectl get pods -o wide": "More details (node, IP)",
        "kubectl get pods -w": "Watch pods (live updates)",
        "kubectl describe pod <name>": "Detailed pod info",
        "kubectl logs <pod>": "View pod logs",
        "kubectl logs <pod> -f": "Follow/stream logs",
        "kubectl logs <pod> -c <container>": "Logs from specific container",
        "kubectl logs <pod> --previous": "Logs from crashed container",
        "kubectl exec -it <pod> -- /bin/bash": "Shell into pod",
        "kubectl port-forward <pod> 8080:80": "Forward local port to pod",
        "kubectl delete pod <name>": "Delete pod",
        "kubectl top pods": "Pod resource usage",
    },
    
    # ─────────────────────────────────────────────────────────────────────────
    # DEPLOYMENTS
    # ─────────────────────────────────────────────────────────────────────────
    "deployments": {
        "kubectl get deployments": "List deployments",
        "kubectl describe deployment <name>": "Deployment details",
        "kubectl create deployment <name> --image=<image>": "Create deployment",
        "kubectl scale deployment <name> --replicas=5": "Scale replicas",
        "kubectl set image deployment/<name> <container>=<image>": "Update image",
        "kubectl rollout status deployment/<name>": "Watch rollout progress",
        "kubectl rollout history deployment/<name>": "View rollout history",
        "kubectl rollout undo deployment/<name>": "Rollback to previous",
        "kubectl rollout undo deployment/<name> --to-revision=2": "Rollback to specific",
        "kubectl rollout restart deployment/<name>": "Restart all pods",
    },
    
    # ─────────────────────────────────────────────────────────────────────────
    # SERVICES
    # ─────────────────────────────────────────────────────────────────────────
    "services": {
        "kubectl get services": "List services",
        "kubectl get svc": "Short form",
        "kubectl describe svc <name>": "Service details",
        "kubectl expose deployment <name> --port=80 --type=LoadBalancer": "Create service",
        "kubectl get endpoints": "List service endpoints",
    },
    
    # ─────────────────────────────────────────────────────────────────────────
    # CONFIG & SECRETS
    # ─────────────────────────────────────────────────────────────────────────
    "config": {
        "kubectl get configmaps": "List ConfigMaps",
        "kubectl get secrets": "List Secrets",
        "kubectl create configmap <name> --from-file=<file>": "Create from file",
        "kubectl create secret generic <name> --from-literal=key=value": "Create secret",
        "kubectl get secret <name> -o yaml": "View secret (base64)",
    },
    
    # ─────────────────────────────────────────────────────────────────────────
    # APPLY & DELETE
    # ─────────────────────────────────────────────────────────────────────────
    "apply": {
        "kubectl apply -f <file.yaml>": "Apply config from file",
        "kubectl apply -f <directory>/": "Apply all files in directory",
        "kubectl apply -f https://url/file.yaml": "Apply from URL",
        "kubectl delete -f <file.yaml>": "Delete resources from file",
        "kubectl delete pod,svc -l app=myapp": "Delete by label",
    },
    
    # ─────────────────────────────────────────────────────────────────────────
    # DEBUGGING
    # ─────────────────────────────────────────────────────────────────────────
    "debugging": {
        "kubectl get events": "View cluster events",
        "kubectl get events --sort-by=.metadata.creationTimestamp": "Events by time",
        "kubectl describe <resource> <name>": "Detailed info + events",
        "kubectl logs <pod> --all-containers": "All container logs",
        "kubectl run debug --image=busybox -it --rm -- sh": "Debug pod",
        "kubectl auth can-i create pods": "Check permissions",
    },
}

# ═══════════════════════════════════════════════════════════════════════════════
# COMMON TROUBLESHOOTING SCENARIOS
# ═══════════════════════════════════════════════════════════════════════════════

TROUBLESHOOTING = """
┌─────────────────────────────────────────────────────────────────────────────┐
│ PROBLEM: Pod stuck in Pending                                                │
├─────────────────────────────────────────────────────────────────────────────┤
│ Commands:                                                                    │
│   kubectl describe pod <name>    # Check events section                      │
│   kubectl get events             # Cluster-wide events                       │
│                                                                              │
│ Common causes:                                                               │
│   - Insufficient resources (CPU/memory)                                      │
│   - Node selector doesn't match any node                                     │
│   - PersistentVolumeClaim not bound                                         │
│   - Image pull backoff                                                       │
└─────────────────────────────────────────────────────────────────────────────┘

┌─────────────────────────────────────────────────────────────────────────────┐
│ PROBLEM: Pod stuck in CrashLoopBackOff                                       │
├─────────────────────────────────────────────────────────────────────────────┤
│ Commands:                                                                    │
│   kubectl logs <pod>             # Check application logs                    │
│   kubectl logs <pod> --previous  # Logs from last crash                      │
│   kubectl describe pod <name>    # Check exit codes                          │
│                                                                              │
│ Common causes:                                                               │
│   - Application error (check logs)                                           │
│   - Missing config/secrets                                                   │
│   - Health check failing                                                     │
│   - OOMKilled (out of memory)                                               │
└─────────────────────────────────────────────────────────────────────────────┘

┌─────────────────────────────────────────────────────────────────────────────┐
│ PROBLEM: Service not routing traffic                                         │
├─────────────────────────────────────────────────────────────────────────────┤
│ Commands:                                                                    │
│   kubectl get endpoints <svc>    # Check if endpoints exist                  │
│   kubectl describe svc <name>    # Check selector                            │
│   kubectl get pods -l <selector> # Verify pods match selector                │
│                                                                              │
│ Common causes:                                                               │
│   - Selector doesn't match pod labels                                        │
│   - Pods not ready (readiness probe failing)                                │
│   - Wrong port configuration                                                 │
└─────────────────────────────────────────────────────────────────────────────┘
"""

# ═══════════════════════════════════════════════════════════════════════════════
# KUBECTL PRODUCTIVITY TIPS
# ═══════════════════════════════════════════════════════════════════════════════

PRODUCTIVITY_TIPS = """
# ─────────────────────────────────────────────────────────────────────────────
# ALIASES (add to ~/.bashrc or ~/.zshrc)
# ─────────────────────────────────────────────────────────────────────────────
alias k='kubectl'
alias kgp='kubectl get pods'
alias kgs='kubectl get services'
alias kgd='kubectl get deployments'
alias kd='kubectl describe'
alias kl='kubectl logs'
alias ke='kubectl exec -it'
alias kaf='kubectl apply -f'
alias kdf='kubectl delete -f'

# ─────────────────────────────────────────────────────────────────────────────
# NAMESPACE SHORTCUTS
# ─────────────────────────────────────────────────────────────────────────────
# Set default namespace
kubectl config set-context --current --namespace=fanzone-connect

# Or use kubens tool
kubens fanzone-connect

# ─────────────────────────────────────────────────────────────────────────────
# OUTPUT FORMATS
# ─────────────────────────────────────────────────────────────────────────────
kubectl get pods -o yaml          # Full YAML
kubectl get pods -o json          # Full JSON
kubectl get pods -o wide          # Extra columns
kubectl get pods -o name          # Just names
kubectl get pods -o jsonpath='{.items[*].metadata.name}'  # Custom

# ─────────────────────────────────────────────────────────────────────────────
# USEFUL TOOLS
# ─────────────────────────────────────────────────────────────────────────────
# k9s - terminal UI for Kubernetes
# kubectx/kubens - switch contexts/namespaces easily
# stern - multi-pod log tailing
# lens - Kubernetes IDE
"""

if __name__ == "__main__":
    print("Study the KUBECTL_COMMANDS dictionary above")
    print("Practice each command on a local cluster (minikube, kind, k3d)")

