.PHONY: help up down clean status load-images test-help

# Rhizome local development environment using Kind
CLUSTER_CONFIG = kind-config.yaml
CLUSTER_NAME = rhizome-test
KUBECONFIG_PATH = $(CURDIR)/local_test/kubeconfig

help:
	@echo "*** Rhizome Local Development Environment ***"
	@echo "Usage:"
	@echo "  make help           - Show this help message"
	@echo "  make up             - Create Kind cluster and export kubeconfig"
	@echo "  make load-images    - Pre-pull and load images (only needed behind corporate proxy)"
	@echo "  make down           - Delete Kind cluster and cleanup"
	@echo "  make status         - Show cluster status"
	@echo "  make clean          - Clean up all resources"
	@echo "  make test-help      - Show pytest custom options"
	@echo ""
	@echo "Workflow:"
	@echo "  1. make up          # Create cluster"
	@echo "  2. make load-images # Pre-load images (only if corporate network blocks kind image pulls)"
	@echo "  3. tilt up --stream # Deploy kubernetes resources into local cluster (for use by local tests"
	@echo "  4. hackity hack     # Write code, run tests, repeat"
	@echo "  5. tilt down        # Stop services"
	@echo "  6. make down        # Delete cluster"

load-images:
	@echo "*** Pre-pulling and loading images into Kind cluster ***"
	@echo "Pulling MySQL image..."
	docker pull mysql:8.0
	
	@echo "Loading MySQL image into Kind cluster..."
	kind load docker-image mysql:8.0 --name $(CLUSTER_NAME)
	
	@echo "✅ Images loaded into cluster"

up:
	@echo "*** Creating Kind cluster for rhizome testing ***"
	@echo "Config: $(CLUSTER_CONFIG)"
	@echo "Cluster: $(CLUSTER_NAME)"
	
	# Clean up any existing cluster first
	kind delete cluster --name $(CLUSTER_NAME) 2>/dev/null || true
	
	# Create cluster using config file
	kind create cluster --name $(CLUSTER_NAME) --config $(CLUSTER_CONFIG) --wait 300s
	
	# Export kubeconfig to local_test directory
	@echo "*** Exporting kubeconfig to $(KUBECONFIG_PATH) ***"
	mkdir -p local_test
	kind get kubeconfig --name $(CLUSTER_NAME) > $(KUBECONFIG_PATH)
	
	# Verify cluster is working
	@echo "*** Verifying cluster ***"
	kubectl --kubeconfig=$(KUBECONFIG_PATH) cluster-info
	kubectl --kubeconfig=$(KUBECONFIG_PATH) get nodes
	
	@echo ""
	@echo "✅ Cluster ready! Next steps:"
	@echo "   export KUBECONFIG=$(KUBECONFIG_PATH)"
	@echo "   tilt up"
	@echo ""
	@echo "To restore your original kubeconfig later:"
	@if [ -n "$$KUBECONFIG" ]; then \
		echo "   export KUBECONFIG=$$KUBECONFIG"; \
	else \
		echo "   unset KUBECONFIG"; \
	fi

down:
	@echo "*** Deleting Kind cluster ***"
	kind delete cluster --name $(CLUSTER_NAME) || true
	
	# Clean up kubeconfig file
	rm -f $(KUBECONFIG_PATH)
	
	@echo "✅ Cluster deleted and cleaned up"

status:
	@echo "*** Cluster Status ***"
	@echo "Cluster name: $(CLUSTER_NAME)"
	kind get clusters | grep $(CLUSTER_NAME) || echo "Cluster not found"
	
	@if [ -f "$(KUBECONFIG_PATH)" ]; then \
		echo "Kubeconfig: $(KUBECONFIG_PATH) (exists)"; \
		kubectl --kubeconfig=$(KUBECONFIG_PATH) get nodes 2>/dev/null || echo "Cluster not accessible"; \
	else \
		echo "Kubeconfig: $(KUBECONFIG_PATH) (missing)"; \
	fi

clean: down
	@echo "*** Deep cleanup ***"
	
	# Remove any leftover Kind clusters
	kind get clusters | grep rhizome | xargs -I {} kind delete cluster --name {} || true
	
	# Clean up containers
	docker container prune -f || true
	
	@echo "✅ Deep cleanup complete"

test-help:
	@echo "*** Rhizome Test Options ***"
	@echo ""
	@echo "Custom pytest options:"
	@echo "  --local-cluster     Run tests that require a local Kind cluster"
	@echo ""
	@echo "Usage examples:"
	@echo "  pytest                       # Run tests with no infra requirements"
	@echo "  pytest --local-cluster       # Like above, but include tests which require a local cluster"
	@echo "  pytest --external-infra      # Like above, but include tests which talk to external infra"
	@echo "  pytest --local-cluster --external-infra  # Run tests which talk to both"
	@echo ""
	@echo "Prerequisites for --local-cluster tests:"
	@echo "  1. make up                   # Create Kind cluster"
	@echo "  2. tilt up --stream          # Deploy MySQL with test data"
	@echo "  3. export KUBECONFIG=$(KUBECONFIG_PATH)"
