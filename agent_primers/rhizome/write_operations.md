# Rhizome Write Operations

This document describes how to safely execute database write operations through rhizome's canned query system with user approval.

## Overview

**IMPORTANT**: Database write operations require explicit user approval and must go through the rhizome server. Never use write credentials directly in client-side code.

Rhizome provides a secure write operation system that:
- Uses separate read-only (RO) and read-write (RW) credentials
- Requires user approval for every write operation
- Only allows pre-defined "canned queries" (no arbitrary SQL)
- Shows users exactly what will be executed before running

## Architecture

### Credential Separation

Environments that support write operations provide two sets of credentials:

```python
# Read-only credentials (used by default for all queries)
@dataclass
class DatabaseConfig:
    username: str  # e.g., "remotereadonly"
    password: str
    # ... other fields

# Read-write credentials (only used by rhizome server with user approval)
@dataclass
class DatabaseConfigWithRW:
    ro_username: str  # Read-only user (default)
    ro_password: str
    rw_username: str  # Read-write user (requires approval)
    rw_password: str
    # ... other fields
```

**DevMeta Example**:
- RO: `remotereadonly` (from `op://Shared/MysqlDevLegacy/password`)
- RW: `superuser` (from `op://Shared/DevMetaRW/password`)

### Security Model

1. **Client-side code**: Always uses RO credentials via `RhizomeClient`
2. **Write operations**: Must go through rhizome server's `/write_query` endpoint
3. **RW credentials**: Only accessible to rhizome server, never exposed to clients
4. **User approval**: Required for every write operation

## Canned Queries

All write operations must be pre-defined in `src/rhizome/canned_queries.py`:

```python
from rhizome.canned_queries import CannedQuery

CANNED_QUERIES: dict[str, CannedQuery] = {
    "create_reseller_role": CannedQuery(
        name="create_reseller_role",
        description="Create a reseller_role entry to grant reseller permissions to an account",
        environment="dev1.meta",
        sql="""
            INSERT INTO reseller_role (reseller_id, account_id, permissions_id)
            VALUES (:reseller_id, :account_id, :permissions_id)
        """,
    ),
}
```

### Query Properties

- **name**: Unique identifier for the query
- **description**: Human-readable explanation shown to user
- **environment**: Which environment this query is for (e.g., "dev1.meta")
- **sql**: Parameterized SQL with `:parameter_name` placeholders

### Adding New Queries

To add a new write operation:

1. Add the query to `CANNED_QUERIES` dict in `src/rhizome/canned_queries.py`
2. Use parameterized SQL (`:param_name`) to prevent SQL injection
3. Provide clear description of what the query does
4. Test with dry run first

## Usage

### Prerequisites

The rhizome server must be running in a separate terminal:

```bash
# Terminal 1: Start rhizome server
rhizome serve
```

### Client-Side Invocation

From your test or script:

```python
from rhizome.client import RhizomeClient

# Create client
rhizome_client = RhizomeClient(data_in_logs=False)

# Execute write query with user approval
result = rhizome_client.execute_write_query(
    query_name="create_reseller_role",
    environment_name="DevMeta",
    params={
        "reseller_id": 123,
        "account_id": 456,
        "permissions_id": 1  # Super Administrator
    }
)

# Check result
if result["executed"]:
    print(f"Success! {result['rows_affected']} rows affected")
elif result["approved"]:
    print("Approved but execution failed:", result.get("error"))
else:
    print("User declined the operation")
```

### User Approval Flow

When `execute_write_query()` is called, the rhizome server terminal shows:

```
╔═══════════════════════════════════════════════════════════════════════╗
║                    ⚠️  WRITE OPERATION                                ║
╠═══════════════════════════════════════════════════════════════════════╣
║ Query: create_reseller_role                                           ║
║ Description: Create a reseller_role entry to grant reseller...        ║
║ Environment: DevMeta                                                   ║
║ Database: meta                                                         ║
║                                                                        ║
║ INSERT INTO reseller_role (reseller_id, account_id, permissions_id)  ║
║ VALUES (123, 456, 1)                                                  ║
╚═══════════════════════════════════════════════════════════════════════╝

Execute this query? [y/n]:
```

The user must explicitly type `y` or `n`. If approved, the query executes with RW credentials.

## Response Format

```python
{
    "approved": bool,       # Whether user approved the query
    "executed": bool,       # Whether query was executed
    "rows_affected": int,   # Number of rows affected (if executed)
    "error": str | None     # Error message (if any)
}
```

## Common Patterns

### Test Setup with Write Operations

```python
@pytest.fixture(scope="module")
def setup_test_data(rhizome_client: RhizomeClient):
    """Set up test data with user approval."""

    # User will be prompted to approve this write
    result = rhizome_client.execute_write_query(
        query_name="insert_test_record",
        environment_name="DevMeta",
        params={"name": "Test", "value": 42}
    )

    if not result["executed"]:
        pytest.skip("User declined test data setup")

    yield result

    # Cleanup would also require user approval
```

### Error Handling

```python
try:
    result = rhizome_client.execute_write_query(
        query_name="update_record",
        environment_name="DevMeta",
        params={"id": 123, "status": "active"}
    )

    if not result["approved"]:
        print("User declined the operation")
        return

    if not result["executed"]:
        print(f"Execution failed: {result.get('error')}")
        return

    print(f"Updated {result['rows_affected']} records")

except httpx.HTTPStatusError as e:
    print(f"HTTP error: {e}")
except Exception as e:
    print(f"Unexpected error: {e}")
```

## Security Best Practices

### ✅ DO

- Define all write queries in `canned_queries.py`
- Use parameterized queries (`:param_name`)
- Provide clear descriptions for user approval
- Test queries with dry run first
- Keep rhizome server running in visible terminal during tests

### ❌ DO NOT

- Use RW credentials directly in client code
- Execute raw SQL from client side
- Bypass the canned query system
- Store RW credentials in code or config files
- Auto-approve write operations (always require user input)

## Troubleshooting

### "Environment does not support write operations"

The environment hasn't implemented `get_database_config_rw()`. Check:
- Environment class has `get_database_config_rw()` method
- Method returns `DatabaseConfigWithRW` with RW credentials
- RW credentials are accessible via 1Password/secret manager

### "Unknown query 'query_name'"

Query not registered in `CANNED_QUERIES`. Add it to `src/rhizome/canned_queries.py`.

### "Rhizome server not responding"

Ensure rhizome server is running:
```bash
rhizome serve
```

Check server terminal for errors or prompts.

### User Approval Timeout

The client waits up to 5 minutes for user approval. If user doesn't respond:
- Check rhizome server terminal for prompt
- Ensure terminal is visible and not hidden
- Check if prompt was accidentally dismissed

## Technical Details

### Server Endpoint

The rhizome server provides `/write_query` POST endpoint:

```python
@app.post("/write_query")
def write_query(request: WriteQueryRequest) -> WriteQueryResponse:
    """Execute a canned write query with user approval."""
```

### Request Format

```json
{
    "query_name": "create_reseller_role",
    "environment_name": "DevMeta",
    "params": {
        "reseller_id": 123,
        "account_id": 456,
        "permissions_id": 1
    }
}
```

### Implementation Location

- **Canned queries**: `src/rhizome/canned_queries.py`
- **Server endpoint**: `src/rhizome/server.py` (`/write_query`)
- **Client method**: `src/rhizome/client.py` (`execute_write_query()`)
- **Environment config**: `src/rhizome/environments/base.py` (`DatabaseConfigWithRW`)
- **DevMeta implementation**: `src/rhizome/environments/dev/meta.py` (`get_database_config_rw()`)

## Future Enhancements

Potential improvements to the write operation system:

- **Audit logging**: Record all approved/declined operations
- **Dry-run mode**: Preview changes without executing
- **Batch operations**: Approve multiple related writes at once
- **Role-based queries**: Restrict certain queries to specific users
- **Query templates**: Reusable query patterns with validation
