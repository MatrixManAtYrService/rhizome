# Rhizome TODO Items

## Architecture Improvements

### DatabaseEnvironment Refactoring
**Issue**: The current `DatabaseEnvironment` class architecture assumes all database environments require port forwarding through Kubernetes/CloudSQL proxy. This creates problems for environments like `NorthAmericaBilling` that use direct connections via pybritive.

**Current State**: 
- `DatabaseEnvironment.__init__()` automatically sets up port forwarding
- All subclasses must implement Kubernetes-specific abstract methods even when not needed
- Direct connection environments must provide stub implementations or override `__init__()`

**Proposed Solution**:
Move port forwarding complexity from `DatabaseEnvironment` to `PortForwardConfig` in `environments/base.py`:

1. **Make DatabaseEnvironment more generic**:
   - Remove automatic port forwarding setup from `__init__()`
   - Make Kubernetes-specific methods optional or move to a separate mixin
   - Focus on core database environment functionality (table_situation, etc.)

2. **Enhance PortForwardConfig**:
   - Make it handle its own setup/teardown logic
   - Allow environments to specify port forwarding only when needed
   - Could be passed as an optional parameter to DatabaseEnvironment

3. **Benefits**:
   - Cleaner separation of concerns
   - Direct connection environments don't need stub implementations
   - Port forwarding logic is centralized and reusable
   - Easier to test environments in isolation

**Priority**: Medium - affects architecture cleanliness but current workaround functions

**Files to modify**:
- `src/rhizome/environments/database_environment.py`
- `src/rhizome/environments/base.py`  
- All environment classes that extend DatabaseEnvironment