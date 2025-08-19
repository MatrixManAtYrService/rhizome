# Rhizome Local Test Environment

This document describes the local test environment setup for rhizome development, designed to test port-forwarding and SQLModel functionality with a local Kubernetes cluster.

## Architecture Overview

The local test environment uses a **separation of concerns** approach:

- **Make** handles infrastructure (Kind cluster lifecycle)
- **Tilt** handles application deployment (MySQL with test data)
- **Container Runtime Agnostic** - works with Docker or Podman transparently

## Directory Structure

```
rhizome/
├── Makefile                    # Infrastructure management
├── kind-config.yaml           # Kind cluster configuration
├── Tiltfile                   # Application deployment
└── local_test/                # Local test resources
    ├── kubeconfig             # Generated cluster config
    ├── mysql-configmap.yaml   # MySQL init script with schema + data
    ├── mysql-pod.yaml         # MySQL pod (not deployment - predictable name)
    ├── mysql-service.yaml     # MySQL service
    └── cleanup.sh             # Manual cleanup script
```

## Workflow Commands

### 1. Create Infrastructure
```bash
make up
```
- Creates Kind cluster named `rhizome-test`
- Exports kubeconfig to `./local_test/kubeconfig` (absolute path)
- Verifies cluster is ready
- Shows commands to set KUBECONFIG and restore original

### 2. Deploy Applications
```bash
export KUBECONFIG=/Users/matt.rixman/src/rhizome/local_test/kubeconfig
tilt up --stream
```
- Deploys MySQL pod (name: `mysql` - no random suffix)
- Creates `test` database with `fee_summary` table
- Inserts sample data from diff3r-spa JSON
- Ready for rhizome testing

### 3. Test Database Connection
```bash
# Port forward to MySQL
kubectl --kubeconfig=./local_test/kubeconfig port-forward pod/mysql 3306:3306

# Connect with mysql client
mysql -h 127.0.0.1 -P 3306 -u user -ppass test

# Verify data
USE test;
SELECT * FROM fee_summary;
```

### 4. Cleanup
```bash
tilt down    # Stop applications (Ctrl+C if using --stream)
make down    # Delete cluster
```

## Database Configuration

- **Database**: `test`
- **Username**: `user`
- **Password**: `pass`
- **Table**: `fee_summary` (matches SQLModel exactly)
- **Sample Data**: Single record from diff3r JSON (ID 74347)

## Key Design Decisions

### Why Kind over k3d?
- Better Podman compatibility (no host-gateway issues)
- More reliable networking
- Simpler container runtime detection

### Why Pod instead of Deployment?
- Predictable naming (`mysql` vs `mysql-d5f4ff675-ggc46`)
- Simpler for local testing (only need one instance)
- Easier kubectl commands

### Why Separate Make/Tilt?
- **Clear separation**: Infrastructure vs Applications
- **Better debugging**: Can test cluster creation independently
- **Follows best practices**: Infrastructure as code patterns

## Container Runtime Detection

The system automatically works with both Docker and Podman:
- Uses standard `docker` commands throughout
- No special configuration needed
- Works transparently regardless of backend

## SQLModel Integration

The `fee_summary` table schema matches the SQLModel definition exactly:
- Field names, types, constraints match
- Sample data available for testing
- Ready for rhizome port-forwarding tests

## Future Milestones

1. **✅ Current**: Local MySQL with sample data
2. **Next**: Test rhizome port-forwarding to local cluster
3. **Future**: SQLModel query tests, sanitization tests

## Corporate Environment Support

### Image Pull in Corporate Networks
For corporate networks with TLS inspection (Zscaler, etc.), use the pre-loading workflow:

```bash
make up           # Create cluster
make load-images  # Pre-pull with Podman, load into Kind
tilt up --stream  # Deploy using local images
```

This bypasses certificate issues by using your configured Podman to pull images, then loading them directly into Kind.

### Image Pull Troubleshooting
If you see certificate errors:
```
Error: ImagePullBackOff
x509: certificate signed by unknown authority
```

Use `make load-images` to pre-load the MySQL image into Kind.

**TODO**: It should be possible to configure Kind to mount corporate certificates directly into the cluster nodes, eliminating the need for pre-loading. This would involve mounting `/etc/ssl/certs` and `/etc/pki` as `extraMounts` in the Kind configuration, but requires additional containerd configuration to recognize the certificates.

## Troubleshooting

### Cluster Won't Start
```bash
make clean    # Deep cleanup
make up       # Retry
```

### Tilt Can't Find Kubeconfig
- Ensure `make up` completed successfully
- Check `./local_test/kubeconfig` exists
- Verify KUBECONFIG environment variable

### Port Forward Fails
- Check pod is running: `kubectl get pods`
- Verify service exists: `kubectl get svc mysql`
- Use different local port if 3306 is busy

### MySQL Connection Issues
- Wait for readiness probe (30s initial delay)
- Check pod logs: `kubectl logs mysql`
- Verify credentials: user/pass

### Corporate Network Issues
- Ensure VPN/proxy is configured
- Check certificate mounting in Kind config
- Verify Podman can pull images independently
