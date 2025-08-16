#!/bin/bash
# Cleanup script for rhizome local test environment

CLUSTER_NAME="rhizome-test"

echo "Cleaning up rhizome local test environment..."

# Delete k3d cluster
if k3d cluster list | grep -q "$CLUSTER_NAME"; then
    echo "Deleting k3d cluster: $CLUSTER_NAME"
    k3d cluster delete "$CLUSTER_NAME"
else
    echo "Cluster $CLUSTER_NAME not found"
fi

# Remove kubeconfig file
if [ -f "./kubeconfig" ]; then
    echo "Removing kubeconfig file"
    rm -f "./kubeconfig"
fi

echo "Cleanup complete!"