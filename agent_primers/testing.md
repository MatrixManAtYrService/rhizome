# Rhizome Testing

This document describes the testing architecture for rhizome, which uses pytest with custom options to handle different infrastructure requirements.

## Test Categories

Tests are categorized by infrastructure requirements using pytest markers:

- **Unit tests**: No markers, run by default with `pytest`
- **Local cluster tests**: `@pytest.mark.local_cluster` - require local Kind cluster
- **External infrastructure tests**: `@pytest.mark.external_infra` - require production access

## Pytest Configuration

### Default Options
All pytest runs use `-sv` by default (configured in `pyproject.toml`):
- `-s`: Disables output capture (shows print statements)
- `-v`: Verbose mode (shows individual test names)

### Custom CLI Options
Added via `pytest_addoption()` in `conftest.py`:

- `--local-cluster`: Run tests requiring local Kind cluster
- `--external-infra`: Run tests requiring external infrastructure

### Test Execution
- `pytest` - runs only unit tests
- `pytest --local-cluster` - runs unit + local cluster tests  
- `pytest --external-infra` - runs unit + external infra tests
- `pytest --local-cluster --external-infra` - runs all tests

Tests are automatically skipped when their required infrastructure flag is not provided.

## Test Structure

### tests/test_na_feesummary.py
Contains two tests for the same functionality (fee summary record 74347 accessibility):

1. `test_na_production_connection_and_sanitization_with_mocks()`: Uses mocked tools, runs by default
2. `test_na_production_connection_and_sanitization_real()`: Uses real external infrastructure, requires `--external-infra`

This pattern allows testing the same logic with and without external dependencies.

### tests/test_k8s_mysql.py
Contains `@pytest.mark.local_cluster` tests that verify:
- Port forwarding to local Kind cluster MySQL
- Database connection and querying
- Data sanitization functionality

Uses fixtures from `conftest.py` that ensure Kind cluster and MySQL pod are ready.

## Local Test Infrastructure

The local test environment uses separation of concerns:

- **Make** handles infrastructure (Kind cluster lifecycle)
- **Tilt** handles application deployment (MySQL with test data)
- **Container Runtime Agnostic** - works with Docker or Podman

### Directory Structure
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

### Setup Commands
```bash
make up           # Create Kind cluster
tilt up --stream  # Deploy MySQL with test data
pytest --local-cluster  # Run cluster tests
```

## Design Decisions

### Why Custom Pytest Options vs Environment Variables
Custom options provide:
- Clear intent when running tests
- Automatic test skipping
- Integration with pytest's native marker system
- Better documentation in `pytest --help`

### Why Pod Instead of Deployment for MySQL
- Predictable naming (`mysql` vs `mysql-d5f4ff675-ggc46`)
- Simpler for testing (only need one instance)
- Easier kubectl commands in test fixtures

### Why Separate Make/Tilt
- Clear separation: Infrastructure vs Applications
- Better debugging: Can test cluster creation independently
- Follows infrastructure as code patterns

### Why Kind Over k3d
- Better Podman compatibility (no host-gateway issues)
- More reliable networking
- Simpler container runtime detection

## Database Configuration

Local test database:
- **Database**: `test`
- **Username**: `user`
- **Password**: `pass`
- **Table**: `fee_summary` (matches SQLModel exactly)
- **Sample Data**: Single record from diff3r JSON (ID 74347)

## Corporate Environment Support

### Image Pull in Corporate Networks
For corporate networks with TLS inspection, use pre-loading:

```bash
make up           # Create cluster
make load-images  # Pre-pull with Podman, load into Kind
tilt up --stream  # Deploy using local images
```

This bypasses certificate issues by using configured Podman to pull images, then loading them directly into Kind.

## Test Fixtures

### conftest.py Fixtures
- `local_cluster()`: Ensures Kind cluster is available, sets KUBECONFIG
- `local_mysql()`: Ensures MySQL pod is ready in cluster
- `rhizome_server()`: Starts rhizome server for integration tests

Fixtures use subprocess to verify infrastructure state before tests run, providing clear error messages when prerequisites are missing.

## Help and Documentation

- `make help`: General project commands
- `make test-help`: Detailed pytest options and examples
- `pytest --help | grep -A 5 "Custom options"`: Show custom pytest flags