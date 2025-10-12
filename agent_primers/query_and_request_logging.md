# Query and Request Logging

This document describes the centralized logging architecture for HTTP requests (stolon) and SQL queries (rhizome).

## Overview

Both stolon and rhizome have been refactored to centralize their execution paths, preparing for comprehensive observability:

- **Stolon**: All HTTP requests flow through `stolon.environments.base.Environment._create_httpx_client()`
- **Rhizome**: All SQL queries flow through `rhizome.client.RhizomeClient._create_instrumented_engine()`

This architecture allows a single instrumentation point for each type of operation.

## HTTP Request Logging (Stolon) - IMPLEMENTED ✅

### Architecture

All HTTP requests are made through `stolon.environments.base.Environment`:
- Direct HTTP calls use inherited methods: `get()`, `post()`, `delete()`
- Generated OpenAPI clients receive an instrumented httpx client via `_create_httpx_client()`

**File**: `src/stolon/environments/base.py`
```python
def _create_httpx_client(self) -> httpx.Client:
    """
    Create an httpx.Client with event hook structure prepared for instrumentation.

    Event hooks ready for instrumentation (currently no-ops)
    """
    request_hooks: list[Callable[[httpx.Request], None]] = []
    response_hooks: list[Callable[[httpx.Response], None]] = []

    event_hooks = {
        "request": request_hooks,
        "response": response_hooks,
    }

    return httpx.Client(event_hooks=event_hooks)
```

### Logging Endpoints

The stolon server provides two endpoints for logging HTTP traffic:

**File**: `src/stolon/server.py`

#### POST /log_request
Logs HTTP request details before sending.

**Request Model** (`src/stolon/models.py`):
```python
class HttpRequestLog(BaseModel):
    method: str
    url: str
    data: str | None = None
```

**Logged Fields**:
- `method` - HTTP method (GET, POST, etc.)
- `hostname` - Extracted from URL
- `path` - Extracted from URL
- `url` - Full URL
- `data` - Request body if ≤ 256 chars, or `data_length` with character count

**Headers**: Not logged (security)

#### POST /log_response
Logs HTTP response details after receiving.

**Request Model** (`src/stolon/models.py`):
```python
class HttpResponseLog(BaseModel):
    method: str
    url: str
    status_code: int
    data: str | None = None
```

**Logged Fields**:
- `method` - HTTP method (GET, POST, etc.)
- `hostname` - Extracted from URL
- `path` - Extracted from URL
- `url` - Full URL
- `status_code` - HTTP response code
- `data` - Response body if ≤ 256 chars, or `data_length` with character count

**Headers**: Not logged (security)

### Usage Example

```python
import httpx

# Before making a request
httpx.post(
    "http://localhost:8001/log_request",
    json={
        "method": "GET",
        "url": "https://dev1.dev.clover.com/v3/merchants/ABC123",
        "data": '{"filter": "active"}'
    }
)

# After receiving response
httpx.post(
    "http://localhost:8001/log_response",
    json={
        "method": "GET",
        "url": "https://dev1.dev.clover.com/v3/merchants/ABC123",
        "status_code": 200,
        "data": '{"id": "ABC123", "name": "Test Merchant"}'
    }
)
```

### Future: Automatic Logging

To enable automatic logging for all HTTP requests:

1. Add request/response hooks to `_create_httpx_client()` in `src/stolon/environments/base.py`
2. Extract request/response details in the hooks
3. Call the logging endpoints from within the hooks
4. Every HTTP request made through any environment will be automatically logged

## SQL Query Logging (Rhizome) - IMPLEMENTED ✅

### Architecture

All SQL queries flow through `rhizome.client.RhizomeClient`:
- `select_first()` - Returns first result or None
- `select_all()` - Returns all results
- `select_one()` - Returns exactly one result
- `execute_raw_query()` - Executes raw SQL

Each method creates a database engine via `_create_instrumented_engine()`, which includes SQLAlchemy event listeners for automatic query logging.

**File**: `src/rhizome/client.py`
```python
def _create_instrumented_engine(self, connection_string: str) -> sqlalchemy.Engine:
    """
    Create a SQLAlchemy engine with event listeners for query logging.
    """
    from sqlalchemy import event
    from sqlalchemy.engine import Connection, ExecutionContext

    engine = create_engine(connection_string)
    database = engine.url.database or "unknown"

    @event.listens_for(engine, "before_cursor_execute")
    def before_cursor_execute(
        conn: Connection,
        cursor: Any,
        statement: str,
        parameters: tuple[Any, ...] | dict[str, Any],
        context: ExecutionContext,
        executemany: bool,
    ) -> None:
        """Log SQL query before execution."""
        # Generate unique query ID and store with start time
        query_id = str(uuid.uuid4())[:8]  # Use first 8 chars for readability
        context._query_id = query_id
        context._query_start_time = time.time()

        # Fire-and-forget logging with exception suppression
        with suppress(Exception):
            httpx.post(
                f"{self.base_url}/log_query",
                json={
                    "query_id": query_id,
                    "statement": statement,
                    "parameters": parameters,
                    "database": database,
                    "connection_string": connection_string,
                },
                timeout=1.0,
            )

    @event.listens_for(engine, "after_cursor_execute")
    def after_cursor_execute(
        conn: Connection,
        cursor: Any,
        statement: str,
        parameters: tuple[Any, ...] | dict[str, Any],
        context: ExecutionContext,
        executemany: bool,
    ) -> None:
        """Log SQL query result after execution."""
        duration = (time.time() - context._query_start_time) * 1000  # ms
        query_id = context._query_id  # Retrieve query ID from context
        row_count = cursor.rowcount if cursor.rowcount >= 0 else None

        # Fire-and-forget logging with exception suppression
        # Note: Only log query_id, duration, and row_count (context already logged above)
        with suppress(Exception):
            httpx.post(
                f"{self.base_url}/log_query_result",
                json={
                    "query_id": query_id,
                    "duration_ms": duration,
                    "row_count": row_count,
                },
                timeout=1.0,
            )

    return engine
```

### Logging Endpoints

The rhizome server provides two endpoints for logging SQL queries:

**File**: `src/rhizome/server.py`

#### POST /log_query
Logs SQL query details before execution.

**Request Model** (`src/rhizome/server_models.py`):
```python
class SqlQueryLog(BaseModel):
    """Request model for SQL query logging."""

    query_id: str
    statement: str
    parameters: dict[str, Any] | list[Any] | None = None
    database: str
    connection_string: str
```

**Logged Fields**:
- `query_id` - Unique identifier for this query (8-character UUID prefix)
- `statement` - SQL query statement
- `database` - Database name
- `connection_string` - Connection string used
- `parameters` - Query parameters (if present)

**Data**: Not logged in results (only in the query for debugging)

#### POST /log_query_result
Logs SQL query result details after execution.

**Request Model** (`src/rhizome/server_models.py`):
```python
class SqlQueryResultLog(BaseModel):
    """Request model for SQL query result logging."""

    query_id: str
    duration_ms: float
    row_count: int | None = None
```

**Logged Fields**:
- `query_id` - Unique identifier linking this result to the original query
- `duration_ms` - Query execution time in milliseconds
- `row_count` - Number of rows returned (if available)

**Efficiency Note**: Only new information (duration, row count) is logged here. All context (statement, database, connection_string, parameters) was already logged in `/log_query` and can be traced via `query_id`.

**Data**: Result data is NOT logged (only row count)

### Usage Example

SQL query logging is automatic - every query executed through RhizomeClient is logged:

```python
from rhizome.client import RhizomeClient

client = RhizomeClient(data_in_logs=False)

# This query will automatically log before and after execution
result = client.select_first(
    connection_string="mysql://localhost:3306/test",
    query=select(Merchant).where(Merchant.id == "ABC123")
)

# Logs will show:
# 1. Before execution: query_id=a1b2c3d4 statement="SELECT..." parameters={...} database=test
# 2. After execution: query_id=a1b2c3d4 database=test duration_ms=123.45 row_count=1
#
# Note: The statement is only logged once in step 1. Step 2 uses query_id to correlate.
```

**Example Output**:
```
15:23:56 SQL query                    [rhizome.server] query_id=a1b2c3d4 database=meta connection_string=mysql://... parameters={'email_1': 'user@example.com'}
  Statement:
SELECT account.id, account.uuid, account.name, account.email
FROM account
WHERE account.email = %(email_1)s
15:23:56 SQL query result             [rhizome.server] query_id=a1b2c3d4 duration_ms=122.55 row_count=0
```

**Note**: The SQL statement is printed to stderr (not logged via structlog) so that newlines render properly for readability.

### Implementation Details

- **Fire-and-forget**: Logging uses `contextlib.suppress(Exception)` to ensure failures don't break queries
- **Short timeout**: 1 second timeout on logging requests to avoid blocking database queries
- **No data logging**: Only metadata (query, row count) is logged, not actual result data
- **Performance**: Minimal overhead due to fire-and-forget approach
- **Readable SQL**: Statements are printed to stderr (not structlog) so newlines render properly instead of showing as `\n`

### Benefits

SQL query logging provides:
- **Visibility**: See all queries executed by any environment in the rhizome server output
- **Debugging**: Trace query execution and timing
- **Monitoring**: Identify slow queries or patterns
- **Audit**: Track what databases and tables are being accessed

## Summary

| Feature | Status | Location |
|---------|--------|----------|
| Stolon HTTP centralization | ✅ Implemented | `stolon/environments/base.py` |
| Stolon logging endpoints | ✅ Implemented | `stolon/server.py`, `stolon/models.py` |
| Rhizome SQL centralization | ✅ Implemented | `rhizome/client.py` |
| Rhizome logging endpoints | ✅ Implemented | `rhizome/server.py`, `rhizome/server_models.py` |
| Automatic HTTP logging | 🚧 TODO | Add hooks to `_create_httpx_client()` |
| Automatic SQL logging | ✅ Implemented | Event listeners in `_create_instrumented_engine()` |

**What's Working Now:**
- All SQL queries automatically logged to rhizome server output
- HTTP/SQL logging endpoints ready for manual instrumentation
- Fire-and-forget logging ensures reliability

**What's Next:**
- Add automatic HTTP request/response logging via httpx event hooks in stolon
