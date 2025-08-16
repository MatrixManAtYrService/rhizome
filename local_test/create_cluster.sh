#!/bin/bash
# Script to create and configure k3d cluster for rhizome testing

set -e  # Exit on any error

CLUSTER_NAME="rhizome-test"
KUBECONFIG_PATH="./local_test/kubeconfig"

echo "=== Rhizome K3D Cluster Setup ==="

# Function to check if cluster exists and is healthy
check_cluster_health() {
    if k3d cluster list | grep -q "$CLUSTER_NAME"; then
        echo "Cluster '$CLUSTER_NAME' exists, checking health..."
        
        # Try to get node list to verify cluster is actually working
        if k3d node list "$CLUSTER_NAME" >/dev/null 2>&1; then
            echo "Cluster appears healthy"
            return 0
        else
            echo "Cluster exists but appears unhealthy"
            return 1
        fi
    else
        echo "Cluster '$CLUSTER_NAME' does not exist in list"
        return 1
    fi
}

# Function to delete cluster if it exists (handles phantom clusters)
delete_cluster() {
    echo "Attempting to delete cluster '$CLUSTER_NAME'..."
    
    # Try to delete even if it doesn't appear in list (handles phantom clusters)
    if k3d cluster delete "$CLUSTER_NAME" 2>/dev/null; then
        echo "Successfully deleted cluster '$CLUSTER_NAME'"
    else
        echo "Cluster '$CLUSTER_NAME' was not found or already deleted"
    fi
    
    # Wait a moment for cleanup
    sleep 2
}

# Function to create new cluster
create_cluster() {
    echo "Creating k3d cluster '$CLUSTER_NAME'..."
    
    # Clean up any leftover networks
    echo "Cleaning up any leftover k3d networks..."
    docker network prune -f >/dev/null 2>&1 || true
    
    # Try to remove any existing k3d network for this cluster
    docker network rm "k3d-$CLUSTER_NAME" >/dev/null 2>&1 || true
    
    # Try creating cluster with different approaches to avoid host-gateway issues
    echo "Attempting cluster creation (method 1: basic)..."
    if k3d cluster create "$CLUSTER_NAME" --wait --timeout 60s; then
        echo "Cluster created successfully with basic method"
        return 0
    fi
    
    echo "Basic method failed, trying with custom network..."
    # Clean up the failed attempt
    k3d cluster delete "$CLUSTER_NAME" 2>/dev/null || true
    sleep 2
    
    # Try with a custom network to avoid host-gateway conflicts
    docker network create k3d-custom 2>/dev/null || true
    if k3d cluster create "$CLUSTER_NAME" --wait --timeout 60s --network k3d-custom; then
        echo "Cluster created successfully with custom network"
        return 0
    fi
    
    echo "Custom network method failed, trying minimal config..."
    # Clean up the failed attempt
    k3d cluster delete "$CLUSTER_NAME" 2>/dev/null || true
    docker network rm k3d-custom 2>/dev/null || true
    sleep 2
    
    # Last resort: most minimal config possible
    k3d cluster create "$CLUSTER_NAME"
    
    # Verify cluster was created successfully
    echo "Verifying cluster creation..."
    k3d cluster list | grep "$CLUSTER_NAME"
    k3d node list "$CLUSTER_NAME"
}

# Function to export kubeconfig
export_kubeconfig() {
    echo "Exporting kubeconfig to $KUBECONFIG_PATH..."
    
    # Create directory if it doesn't exist
    mkdir -p "$(dirname "$KUBECONFIG_PATH")"
    
    # Export kubeconfig
    k3d kubeconfig get "$CLUSTER_NAME" > "$KUBECONFIG_PATH"
    
    # Verify kubeconfig works
    echo "Testing kubeconfig..."
    kubectl --kubeconfig="$KUBECONFIG_PATH" cluster-info
    kubectl --kubeconfig="$KUBECONFIG_PATH" get nodes
}

# Main execution
main() {
    if check_cluster_health; then
        echo "Cluster is healthy, attempting to export kubeconfig..."
        if export_kubeconfig; then
            echo "✅ Cluster setup complete!"
            return 0
        else
            echo "❌ Kubeconfig export failed, will recreate cluster..."
        fi
    fi
    
    # If we get here, we need to recreate the cluster
    echo "Recreating cluster..."
    delete_cluster
    create_cluster
    export_kubeconfig
    
    echo "✅ Cluster setup complete!"
    echo "Cluster name: $CLUSTER_NAME"
    echo "Kubeconfig: $KUBECONFIG_PATH"
    echo "Nodes:"
    kubectl --kubeconfig="$KUBECONFIG_PATH" get nodes
}

# Run main function
main