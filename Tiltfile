# Tiltfile for rhizome MySQL deployment
# Assumes Kind cluster already exists (created by 'make up')

# Configuration
KUBECONFIG_PATH = "./local_test/kubeconfig"

# Verify kubeconfig exists
if not os.path.exists(KUBECONFIG_PATH):
    fail("Kubeconfig not found at %s. Run 'make up' first to create the cluster." % KUBECONFIG_PATH)

# Use the exported kubeconfig for all kubectl operations
os.putenv('KUBECONFIG', KUBECONFIG_PATH)

print("🗃️  Deploying MySQL to rhizome-test cluster")

# Deploy MySQL components
k8s_yaml([
    'local_test/mysql-configmap.yaml',
    'local_test/mysql-pod.yaml', 
    'local_test/mysql-service.yaml'
])

# Configure the MySQL resource (no port forwards - we'll use kubectl for that)
k8s_resource('mysql', 
    resource_deps=[],
    labels=["database"]
)

print("\\n=== Rhizome MySQL Environment ===")
print("Cluster: rhizome-test")
print("MySQL Service: mysql.default.svc.cluster.local:3306")
print("Database: test") 
print("Table: fee_summary (with sample data)")
print("Username: user")
print("Password: pass")
print("\\nTo connect via port-forward:")
print("  kubectl --kubeconfig=%s port-forward svc/mysql 3306:3306" % KUBECONFIG_PATH)
print("\\nWorkflow:")
print("  tilt up   # Deploy MySQL")
print("  # Test rhizome functionality")  
print("  tilt down # Stop services")
print("  make down # Delete cluster")