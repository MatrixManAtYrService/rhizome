# Rhizome Process Handling System

This document describes the process handling architecture implemented in rhizome for managing long-running subprocesses, particularly kubectl port-forward operations.

## Architecture Overview

Rhizome uses a client-server architecture where:
- **Server** manages subprocess lifecycle (start, monitor, cleanup)
- **Client** requests process creation and gets connection handles
- **Environment modules** provide simple interfaces for specific configurations

## Core Components

### Process Management Layer

#### `src/rhizome/proc.py` - Generic Process Manager
- **`ProcessManager` class** - Manages async subprocess lifecycle
- **`start_process(args, process_name)`** - Generic subprocess creation with output streaming
- **`stream_process_output()`** - Async output capture and logging with PID binding
- **`list_processes()`** - Track running processes, auto-cleanup completed ones
- **Response models**: `NewProcessResponse`, `ProcessInfo`, `ProcessListResponse`
- **Global instance**: `process_manager` used by all process types

#### `src/rhizome/logging.py` - Unified Logging
- **`setup_logging()`** - Configures structlog with custom formatting
- **Time format**: `%H:%M:%S` (no log levels shown)
- **Console renderer** with process name and PID binding
- **Intercepts all logging** (uvicorn, FastAPI, subprocess output)

### Process Type Implementations

#### `src/rhizome/sleeper.py` - Test Process
```python
async def start_sleeper() -> NewProcessResponse:
    # Creates Python subprocess that prints 0-4 with configurable sleep
    # Used for testing process management without kubectl dependencies
```

#### `src/rhizome/portforward.py` - kubectl Port Forward
```python
async def start_portforward(kube_context, kube_namespace, kube_deployment, sql_connection, local_port=3306):
    # Two modes:
    # 1. Simulation (RHIZOME_SIMULATE=true) - Shows parameters, simulates kubectl
    # 2. Real (RHIZOME_SIMULATE=false) - Executes actual kubectl commands

    # Real implementation steps (commented):
    # 1. Check if port already forwarded (lsof)
    # 2. Start connection script in pod (kubectl exec)
    # 3. Parse logs for remote port (kubectl logs)
    # 4. Start port-forward (kubectl port-forward)
```

### Server Layer

#### `src/rhizome/server.py` - FastAPI Server
- **Lifespan management** - Process cleanup on shutdown
- **Endpoints**:
  - `POST /sleeper` � `start_sleeper()`
  - `POST /portforward` � `start_portforward(request.params)`
  - `GET /ps` � `process_manager.list_processes()`
- **`PortforwardRequest` model** - Validates JSON payload for kubectl parameters

#### `src/rhizome/config.py` - Configuration Management
- **`Home` class** - Manages XDG state directory for port storage
- **`set_port()/get_port()`** - Server port persistence
- **`sandbox()`** - Testing isolation

### Client Layer

#### `src/rhizome/client.py` - Server Communication
```python
@dataclass
class Handle:
    connection_string: str  # e.g. "mysql://localhost:3306"
    local_port: int
    sql_connection: str     # Original connection name

class RhizomeClient:
    def request_portforward(kube_context, kube_namespace, ...) -> Handle:
        # 1. Read server port from ~/.local/state/rhizome/port
        # 2. POST to http://0.0.0.0:{port}/portforward with JSON
        # 3. Wait for port-forward to establish
        # 4. Return Handle with connection details
```

### Environment Configurations

#### `src/rhizome/environments/na_prod/billing_bookkeeper.py` - Environment-Specific Config
```python
def get_handle() -> Handle:
    return client.request_portforward(
        kube_context="gke_clover-prod-kubernetes_us-central1_na-prod-us-central1-cluster",
        kube_namespace="gke-cloudsql-access",
        kube_deployment="gke-cloudsql-access",
        sql_connection="clover-prod-databases:us-central1:billing-bookkeeper",
        local_port=3306
    )
```

## Data Flow

### 1. Client Request Flow
```
User Code � Environment Module � RhizomeClient � HTTP Request � FastAPI Server
```

### 2. Process Creation Flow
```
FastAPI Endpoint � Process Type Module � ProcessManager.start_process() � async subprocess
```

### 3. Output Streaming Flow
```
subprocess stdout � stream_process_output() � structlog � console (with PID/process name)
```

### 4. Process Tracking Flow
```
ProcessManager._processes set � /ps endpoint � JSON response with running PIDs
```

## Process Lifecycle

1. **Creation**: `subprocess.create_subprocess_exec()` with PIPE capture
2. **Tracking**: Added to `_processes` set, async task for output streaming
3. **Monitoring**: `/ps` endpoint shows running processes, auto-cleanup completed
4. **Output**: Real-time streaming via async readline, logged with process name + PID
5. **Cleanup**: Automatic removal on completion, manual termination on server shutdown

## Log Format

```
22:46:06 subprocess started             [sleeper] pid=93302
22:46:06 0                              [sleeper] pid=93302
22:46:07 1                              [sleeper] pid=93302
22:46:11 subprocess finished            [sleeper] pid=93302

22:50:15 Starting kubectl port-forward simulation... [portforward] pid=94123
22:50:15 Context: gke_clover-prod-kubernetes_us-central1_na-prod-us-central1-cluster [portforward] pid=94123
22:50:15 Forwarding localhost:3306 -> pod:3307 (iteration 0) [portforward] pid=94123
```

## API Usage

### Start Sleeper (Testing)
```bash
POST /sleeper
# No parameters, uses SLEEP_OVERRIDE env var
```

### Start Port Forward
```bash
POST /portforward
{
  "kube_context": "gke_clover-prod-kubernetes_us-central1_na-prod-us-central1-cluster",
  "kube_namespace": "gke-cloudsql-access",
  "kube_deployment": "gke-cloudsql-access",
  "sql_connection": "clover-prod-databases:us-central1:billing-bookkeeper",
  "local_port": 3306
}
```

### List Processes
```bash
GET /ps
{
  "running": [{"pid": 93302}, {"pid": 94123}],
  "count": 2
}
```

## Testing

- **Unit tests**: `tests/test_server.py` - Multiple process lifecycle testing
- **Port cleanup**: `tests/test_port.py` - Server shutdown cleanup verification
- **Fast testing**: `SLEEP_OVERRIDE=0.1` for quick test execution
- **Simulation mode**: `RHIZOME_SIMULATE=true` for kubectl-free testing

## Testing Architecture

### Tool Abstraction and Mocking Strategy

The codebase implements a comprehensive testing strategy using dependency injection and mocking to isolate external tool dependencies:

#### `src/rhizome/tools.py` - Tool Abstraction Layer
- **Abstract base classes** define interfaces for external tools:
  - `KubectlTool` - Kubernetes operations (exec, logs, port-forward, cluster info)
  - `OnePasswordTool` - Secret retrieval operations
  - `LsofTool` - Port usage checking operations
  - `GcloudTool` - Google Cloud operations
- **Concrete implementations** provide real subprocess-based functionality:
  - `ExternalKubectlTool` - Real kubectl commands via `asyncio.create_subprocess_exec`
  - `ExternalOnePasswordTool` - Real 1Password CLI operations
  - `ExternalLsofTool` - Real lsof port checking
  - `ExternalGcloudTool` - Real gcloud operations
- **`Tools` container class** enables dependency injection with defaults to real implementations

#### `tests/mocked_subprocesses.py` - Mock Tool Implementations
- **`MockKubectlTool`** - Simulates CloudSQL proxy behavior without real kubectl:
  - Returns predefined log output with mock port information
  - Provides mock subprocess objects for port forwarding
  - Simulates cluster info and pod status responses
- **`MockOnePasswordTool`** - Returns environment-specific mock passwords:
  - Maps 1Password references to predefined test credentials
  - Eliminates dependency on actual 1Password CLI and vault access
- **`MockLsofTool`** - Always reports ports as available:
  - Returns empty lists indicating no port conflicts
  - Enables test isolation without actual port checking
- **Specialized mocks** like `MockNAProductionKubectlTool` for environment-specific testing

#### `tests/test_environment_access.py` - Dual Testing Strategy
The test suite implements a comprehensive approach with both mocked and real infrastructure testing:

**Mocked Testing (`test_mocked_environment_database_access`)**:
- Uses mock tools via dependency injection: `Tools(kubectl=MockKubectlTool(), onepassword=MockOnePasswordTool(), lsof=MockLsofTool())`
- Mocks SQLModel database sessions with `monkeypatch` to return predefined test data
- Tests all environment/database combinations (6 combinations across na/dev/demo environments and billing-bookkeeper/billing-event databases)
- Validates data structure and business logic without external dependencies
- Fast execution suitable for continuous integration

**Real Infrastructure Testing (`test_real_environment_database_access`)**:
- Uses real tools (default `RhizomeClient` with `ExternalKubectlTool`, etc.)
- Requires `@pytest.mark.external_infra` marker and actual cluster access
- Tests against live databases with real kubectl port forwarding
- Validates end-to-end functionality including network connectivity and authentication
- Slower execution, typically run in staging/integration environments

### Test Data Management
- **`tests/mocked_table_data.py`** provides test specifications per model/environment combination
- Each test spec defines:
  - `get_mock_data()` - Synthetic data for mocked tests
  - `get_expected_data()` - Real data expectations for infrastructure tests
  - `check_assertions()` - Validation logic for both test types

### Testing Benefits
1. **Fast feedback loop** - Mocked tests run quickly without external dependencies
2. **Comprehensive coverage** - All environment/database combinations tested
3. **Isolation** - Mocked tests don't interfere with production systems
4. **Integration validation** - Real tests verify actual infrastructure connectivity
5. **Maintainability** - Abstract interfaces allow easy mock implementation updates

## Key Design Principles

1. **Separation of concerns**: Generic process management vs specific implementations
2. **Async throughout**: Non-blocking subprocess creation and output streaming
3. **Real-time output**: Live subprocess output appears immediately in server logs
4. **Automatic cleanup**: Processes self-remove when completed
5. **Environment isolation**: Minimal, focused environment configuration modules
6. **Testability**: Simulation modes, sandbox configurations, and comprehensive mocking for testing
7. **Dependency injection**: Abstract tool interfaces enable easy testing and mocking
8. **Dual testing strategy**: Both mocked (fast) and real infrastructure (comprehensive) test coverage

## Future Extensions

To add new process types:
1. Create `src/rhizome/newtype.py` with `start_newtype()` function
2. Add endpoint in `server.py` that calls the function
3. Create environment modules in `src/rhizome/environments/*/` as needed
4. All subprocess management handled automatically by `ProcessManager`

To add new external tool dependencies:
1. Define abstract interface in `src/rhizome/tools.py`
2. Implement concrete external version using subprocess
3. Create mock implementation in `tests/mocked_subprocesses.py`
4. Add to `Tools` container class with dependency injection support
5. Update tests to use mock implementations for fast testing