import asyncio
import json
from collections.abc import AsyncGenerator
from contextlib import asynccontextmanager
from typing import TYPE_CHECKING, Any

import structlog
import uvicorn
from fastapi import FastAPI
from fastapi.responses import StreamingResponse
from pydantic import BaseModel

from rhizome.logging import setup_logging
from rhizome.portforward import start_portforward
from rhizome.proc import NewProcessResponse, ProcessListResponse, process_manager
from rhizome.server_models import (
    DatabaseConnectionLog,
    ExecuteQueryRequest,
    ExecuteQueryResponse,
    GetMode,
    SqlQueryLog,
    SqlQueryResultLog,
)
from rhizome.sleeper import start_sleeper
from trifolium.config import Home

if TYPE_CHECKING:
    from rhizome.tools import GcloudTool, KubectlTool, LsofTool, OnePasswordTool, PybritiveTool


class PortforwardRequest(BaseModel):
    """Request model for port forward requests."""

    kube_context: str
    kube_namespace: str
    kube_deployment: str
    sql_connection: str
    local_port: int = 3306


class SleeperRequest(BaseModel):
    """Request model for sleeper requests."""

    iterations: int = 5


class LocalK8sRequest(BaseModel):
    """Request model for local K8s port forward with credentials."""

    kube_context: str
    kube_namespace: str
    kube_deployment: str
    local_port: int = 3306
    delay: float = 2.0  # Delay before supplying credentials (for testing)


class WriteQueryRequest(BaseModel):
    """Request model for prompted write query execution."""

    query_name: str
    database_id: str  # RhizomeEnvironment enum value, e.g., "dev_meta"
    params: dict[str, str | int | float | None]
    reason: str | None = None  # Why this operation is necessary
    entity_descriptions: dict[str, str] | None = (
        None  # Context about entities (e.g., {"role_id_7477": "Super Admin for Clover"})
    )


class WriteQueryResponse(BaseModel):
    """Response model for write query execution."""

    approved: bool
    executed: bool
    rows_affected: int | None = None
    error: str | None = None


logger = structlog.get_logger()

# Global variable to store the home instance for cleanup
_home: Home | None = None


@asynccontextmanager
async def lifespan(app: FastAPI) -> AsyncGenerator[None, None]:
    """Handle app startup and shutdown."""
    # Startup
    yield
    # Shutdown
    logger.info("Shutting down server, cleaning up processes")

    # Clean up all processes and tasks
    await process_manager.cleanup()

    # Clean up port file
    if _home is not None:
        port_file = _home.state / "rhizome_port"
        if port_file.exists():
            port_file.unlink()


app = FastAPI(lifespan=lifespan)


@app.get("/health")
async def health() -> dict[str, str]:
    """Health check endpoint for server status."""
    return {"status": "ok"}


@app.post("/sleeper")
async def sleeper(request: SleeperRequest) -> NewProcessResponse:
    """Start a sleeper subprocess for testing rhizome process management."""
    return await start_sleeper(iterations=request.iterations)


@app.post("/portforward")
async def portforward(request: PortforwardRequest) -> NewProcessResponse:
    """Start a kubectl port-forward subprocess for database access."""
    return await start_portforward(
        kube_context=request.kube_context,
        kube_namespace=request.kube_namespace,
        kube_deployment=request.kube_deployment,
        sql_connection=request.sql_connection,
        local_port=request.local_port,
    )


async def localk8s_credentials_generator(request: LocalK8sRequest) -> AsyncGenerator[str, None]:
    """
    Generate SSE stream for local K8s credentials.

    This simulates the credential retrieval process that would normally
    involve vault, auth flows, etc. For testing, it uses hard-coded credentials
    with a configurable delay.
    """
    # First, start the port forward process
    logger.info(f"Starting port forward for {request.kube_deployment}")

    try:
        # Start port forward (but with a fake sql_connection for local k8s)
        port_forward_response = await start_portforward(
            kube_context=request.kube_context,
            kube_namespace=request.kube_namespace,
            kube_deployment=request.kube_deployment,
            sql_connection=f"localk8s:{request.kube_namespace}:{request.kube_deployment}",
            local_port=request.local_port,
        )
        logger.info(f"Port forward started with PID {port_forward_response.pid}")
    except Exception as e:
        logger.error(f"Failed to start port forward: {e}")
        yield f"event: error\ndata: {json.dumps({'error': f'Failed to start port forward: {e}'})}\n\n"
        return

    # Send initial status
    yield f"event: status\ndata: {json.dumps({'status': 'port_forward_started', 'pid': port_forward_response.pid})}\n\n"

    # Give kubectl a moment to establish the port forward
    await asyncio.sleep(1.0)

    # Wait for the specified delay (simulating credential retrieval)
    logger.info(f"Waiting {request.delay}s for credentials...")
    yield f"event: status\ndata: {json.dumps({'status': 'retrieving_credentials', 'delay': request.delay})}\n\n"

    await asyncio.sleep(request.delay)

    # Send credentials (hard-coded for local testing)
    credentials = {
        "username": "user",
        "password": "pass",
        "database": "test",
        "connection_string": f"mysql+pymysql://user:pass@localhost:{request.local_port}/test",
    }

    logger.info("Credentials retrieved, sending to client")
    yield f"event: credentials\ndata: {json.dumps(credentials)}\n\n"


@app.post("/localk8s")
async def localk8s(request: LocalK8sRequest) -> StreamingResponse:
    """Start local K8s port forward and stream credentials via SSE."""
    return StreamingResponse(
        localk8s_credentials_generator(request),
        media_type="text/event-stream",
        headers={
            "Cache-Control": "no-cache",
            "Connection": "keep-alive",
        },
    )


@app.get("/ps")
def ps() -> ProcessListResponse:
    """List running processes."""
    return process_manager.list_processes()


class _ServerTools:
    """Server-side tools implementation with real external tool access."""

    def __init__(self) -> None:
        from rhizome.tools import (
            ExternalGcloudTool,
            ExternalKubectlTool,
            ExternalLsofTool,
            ExternalOnePasswordTool,
            ExternalPybritiveTool,
            GcloudTool,
            KubectlTool,
            LsofTool,
            OnePasswordTool,
            PybritiveTool,
        )

        # Use real external tools for all operations
        self._onepassword: OnePasswordTool = ExternalOnePasswordTool()
        self._pybritive: PybritiveTool = ExternalPybritiveTool()
        self._kubectl: KubectlTool = ExternalKubectlTool()
        self._gcloud: GcloudTool = ExternalGcloudTool()
        self._lsof: LsofTool = ExternalLsofTool()

    @property
    def onepassword(self) -> "OnePasswordTool":
        """OnePassword CLI tool."""

        return self._onepassword

    @property
    def pybritive(self) -> "PybritiveTool":
        """Pybritive tool for temporary credentials."""

        return self._pybritive

    @property
    def kubectl(self) -> "KubectlTool":
        """Kubectl tool for Kubernetes operations."""

        return self._kubectl

    @property
    def gcloud(self) -> "GcloudTool":
        """Google Cloud tool."""

        return self._gcloud

    @property
    def lsof(self) -> "LsofTool":
        """Lsof tool for port checking."""

        return self._lsof

    def is_mocked(self) -> bool:
        """Check if tools are mocked - always False for server."""
        return False


def _get_database_config(database_id: str) -> Any:  # noqa: ANN401
    """
    Get database config from database ID using class methods.

    The refactored Environment classes use class methods for credential retrieval,
    so we can call them directly without creating instances.

    Args:
        database_id: Database identifier (RhizomeEnvironment enum value, e.g., "dev_meta")

    Returns:
        DatabaseConfig with connection details

    Raises:
        ValueError: If database not found
    """
    from rhizome.environments.environment_list import RhizomeEnvironment, environment_type

    # Convert string to enum
    try:
        env_enum = RhizomeEnvironment(database_id)
    except ValueError:
        raise ValueError(f"Unknown database: {database_id}") from None

    # Get the environment class
    env_class = environment_type.get(env_enum)
    if not env_class:
        raise ValueError(f"Unknown database: {database_id}")

    # Call the class method directly with server tools
    server_tools = _ServerTools()
    return env_class.get_database_config(server_tools)


def _get_database_config_rw(database_id: str) -> Any:  # noqa: ANN401
    """
    Get RW database config from database ID using class methods.

    Args:
        database_id: Database identifier (RhizomeEnvironment enum value, e.g., "dev_meta")

    Returns:
        DatabaseConfigWithRW with RO and RW connection details, or None if not supported

    Raises:
        ValueError: If database not found
    """
    from rhizome.environments.environment_list import RhizomeEnvironment, environment_type

    # Convert string to enum
    try:
        env_enum = RhizomeEnvironment(database_id)
    except ValueError:
        raise ValueError(f"Unknown database: {database_id}") from None

    # Get the environment class
    env_class = environment_type.get(env_enum)
    if not env_class:
        raise ValueError(f"Unknown database: {database_id}")

    # Call the class method directly with server tools
    server_tools = _ServerTools()
    return env_class.get_database_config_rw(server_tools)


@app.post("/write_query")
def write_query(request: WriteQueryRequest) -> WriteQueryResponse:
    """
    Execute a canned write query with user approval.

    This endpoint:
    1. Looks up the pre-defined query
    2. Renders it with parameters
    3. Prompts the user for approval (yes/no)
    4. If approved, executes with RW credentials
    5. Returns the result

    Args:
        request: Query name, environment, and parameters

    Returns:
        WriteQueryResponse with execution results
    """
    from urllib.parse import quote_plus

    import sqlalchemy
    from rich.console import Console
    from rich.panel import Panel
    from rich.prompt import Confirm
    from sqlmodel import create_engine

    from rhizome.canned_queries import get_query, render_query

    console = Console()

    try:
        # Get the canned query
        query = get_query(request.query_name)

        # Get RW database config (without initializing environment)
        db_config_rw = _get_database_config_rw(request.database_id)
        if not db_config_rw:
            return WriteQueryResponse(
                approved=False,
                executed=False,
                error=f"Database {request.database_id} does not support write operations",
            )

        # Render query for display
        rendered = render_query(request.query_name, request.params)

        # Build the panel content
        panel_content = (
            f"[bold cyan]Query:[/bold cyan] {query.name}\n"
            f"[bold cyan]Description:[/bold cyan] {query.description}\n"
            f"[bold cyan]Database:[/bold cyan] {request.database_id}\n"
            f"[bold cyan]Database Name:[/bold cyan] {db_config_rw.database}\n"
        )

        # Add reason if provided
        if request.reason:
            panel_content += f"\n[bold green]Why:[/bold green] {request.reason}\n"

        # Add entity descriptions if provided
        if request.entity_descriptions:
            panel_content += "\n[bold magenta]Entities:[/bold magenta]\n"
            for entity_key, description in request.entity_descriptions.items():
                panel_content += f"  • [magenta]{entity_key}:[/magenta] {description}\n"

        # Add the SQL query
        panel_content += f"\n[yellow]{rendered}[/yellow]"

        # Show query to user with rich formatting
        console.print()
        console.print(
            Panel.fit(
                panel_content,
                title="[bold red]⚠️  WRITE OPERATION[/bold red]",
                border_style="red",
            )
        )
        console.print()

        # Prompt user
        approved = Confirm.ask("[bold]Execute this query?[/bold]", default=False)

        if not approved:
            console.print("[yellow]Query execution cancelled by user[/yellow]")
            return WriteQueryResponse(approved=False, executed=False)

        # Execute with RW credentials
        console.print("[green]Executing query with RW credentials...[/green]")

        encoded_password = quote_plus(db_config_rw.rw_password)
        connection_string = f"mysql+pymysql://{db_config_rw.rw_username}:{encoded_password}@{db_config_rw.host}:{db_config_rw.port}/{db_config_rw.database}"

        engine = create_engine(connection_string)
        # For raw SQL with parameters, use engine connection directly
        with engine.connect() as connection:
            result = connection.execute(sqlalchemy.text(query.sql), request.params)
            connection.commit()
            rows_affected = result.rowcount

        console.print(f"[green]✓ Query executed successfully. Rows affected: {rows_affected}[/green]")
        console.print()

        return WriteQueryResponse(approved=True, executed=True, rows_affected=rows_affected)

    except Exception as e:
        error_msg = str(e)
        console.print(f"[red]✗ Error: {error_msg}[/red]")
        console.print()
        return WriteQueryResponse(approved=False, executed=False, error=error_msg)


def _execute_query_first(
    session: Any,  # noqa: ANN401
    request: ExecuteQueryRequest,
    model_class: type[Any],  # noqa: ANN401
) -> ExecuteQueryResponse:
    """Execute query and return first result or None."""
    import sqlalchemy

    from rhizome.serialization import deserialize_result, serialize_result

    # Use execute() for raw SQL (exec() is for ORM queries)
    result_proxy = session.execute(sqlalchemy.text(request.sql), request.parameters)  # type: ignore[call-overload]
    row = result_proxy.first()

    if row is None:
        return ExecuteQueryResponse(success=True, result=None, row_count=0)

    # Convert row to dict then to model instance
    # Type ignore: row._mapping is a private SQLAlchemy API with incomplete typing
    row_dict: dict[str, Any] = dict(row._mapping)  # type: ignore[attr-defined, var-annotated]
    result = deserialize_result(row_dict, model_class)  # type: ignore[arg-type]

    # Serialize result (handles sanitization)
    serialized = serialize_result(result, sanitize=request.sanitize)
    return ExecuteQueryResponse(success=True, result=serialized, row_count=1)


def _execute_query_all(
    session: Any,  # noqa: ANN401
    request: ExecuteQueryRequest,
    model_class: type[Any],  # noqa: ANN401
) -> ExecuteQueryResponse:
    """Execute query and return all results."""
    import sqlalchemy
    from sqlmodel import SQLModel

    from rhizome.serialization import deserialize_result, serialize_result_list

    # Use execute() for raw SQL (exec() is for ORM queries)
    result_proxy = session.execute(sqlalchemy.text(request.sql), request.parameters)  # type: ignore[call-overload]
    rows = result_proxy.fetchall()

    if not rows:
        return ExecuteQueryResponse(success=True, result=[], row_count=0)

    # Convert rows to model instances
    model_results: list[SQLModel] = []
    for row in rows:
        # Type ignore: row._mapping is a private SQLAlchemy API with incomplete typing
        row_dict: dict[str, Any] = dict(row._mapping)  # type: ignore[attr-defined, var-annotated]
        deserialized = deserialize_result(row_dict, model_class)  # type: ignore[arg-type]
        if deserialized is not None:
            model_results.append(deserialized)

    # Serialize results
    serialized = serialize_result_list(model_results, sanitize=request.sanitize)
    return ExecuteQueryResponse(success=True, result=serialized, row_count=len(serialized))


def _execute_query_one(
    session: Any,  # noqa: ANN401
    request: ExecuteQueryRequest,
    model_class: type[Any],  # noqa: ANN401
) -> ExecuteQueryResponse:
    """Execute query and return exactly one result (error if 0 or >1)."""
    import sqlalchemy

    from rhizome.serialization import deserialize_result, serialize_result

    # Use execute() for raw SQL (exec() is for ORM queries)
    result_proxy = session.execute(sqlalchemy.text(request.sql), request.parameters)  # type: ignore[call-overload]
    rows = result_proxy.fetchall()

    if len(rows) == 0:
        return ExecuteQueryResponse(
            success=False,
            result=None,
            error="Query returned no results (expected exactly one)",
        )
    elif len(rows) > 1:
        return ExecuteQueryResponse(
            success=False,
            result=None,
            error=f"Query returned {len(rows)} results (expected exactly one)",
        )

    # Exactly one result
    # Type ignore: row._mapping is a private SQLAlchemy API with incomplete typing
    row_dict: dict[str, Any] = dict(rows[0]._mapping)  # type: ignore[attr-defined, var-annotated]
    result = deserialize_result(row_dict, model_class)  # type: ignore[arg-type]

    # Serialize result
    serialized = serialize_result(result, sanitize=request.sanitize)
    return ExecuteQueryResponse(success=True, result=serialized, row_count=1)


@app.post("/execute_query")
def execute_query(request: ExecuteQueryRequest) -> ExecuteQueryResponse:
    """
    Execute a query server-side and return serialized results.

    This endpoint:
    1. Gets the environment and database config
    2. Creates a database connection
    3. Executes the SQL query with parameters
    4. Deserializes results into model instances
    5. Applies sanitization if requested
    6. Serializes results for transmission

    Args:
        request: Query execution request with SQL, parameters, model info

    Returns:
        ExecuteQueryResponse with serialized results or error
    """
    from urllib.parse import quote_plus

    from sqlmodel import Session, create_engine

    from rhizome.serialization import import_model_class

    try:
        # Get database config (read-only, without initializing environment)
        db_config = _get_database_config(request.database_id)

        # Build connection string
        encoded_password = quote_plus(db_config.password)
        connection_string = (
            f"mysql+pymysql://{db_config.username}:{encoded_password}"
            f"@{db_config.host}:{db_config.port}/{db_config.database}"
        )

        # Import the model class for result deserialization
        model_class = import_model_class(request.model_module, request.model_class)

        # Create engine and execute query
        engine = create_engine(connection_string)

        with Session(engine) as session:
            if request.mode == GetMode.FIRST:
                return _execute_query_first(session, request, model_class)
            elif request.mode == GetMode.ALL:
                return _execute_query_all(session, request, model_class)
            elif request.mode == GetMode.ONE:
                return _execute_query_one(session, request, model_class)
            else:
                return ExecuteQueryResponse(
                    success=False,
                    result=None,
                    error=f"Unknown query mode: {request.mode}",
                )

    except Exception as e:
        error_msg = f"{type(e).__name__}: {e}"
        logger.error("Query execution failed", error=error_msg, database=request.database_id)
        return ExecuteQueryResponse(success=False, result=None, error=error_msg)


@app.post("/log_query")
async def log_query(query: SqlQueryLog) -> dict[str, str]:
    """
    Log SQL query details before execution.

    Logs query_id, database, and parameters (if present) via structlog.
    Prints the statement to stderr so newlines render properly for readability.
    Does not log result data.
    """
    import sys
    from typing import Any

    # Prepare log data (without statement - we'll print that separately)
    log_data: dict[str, Any] = {
        "query_id": query.query_id,
        "database": query.database,
        "connection_string": query.connection_string,
    }

    # Include parameters if present
    if query.parameters is not None:
        log_data["parameters"] = query.parameters

    # Log metadata via structlog
    logger.info("SQL query", **log_data)

    # Print the statement to stderr with proper newline rendering and indentation
    import textwrap

    indented_statement = textwrap.indent(query.statement, "    ")
    print(f"  Statement:\n{indented_statement}", file=sys.stderr)

    return {"status": "logged"}


@app.post("/log_query_result")
async def log_query_result(result: SqlQueryResultLog) -> dict[str, str]:
    """
    Log SQL query result details after execution.

    Logs only query_id (to associate with original query), duration, and row count.
    Context (statement, database, connection_string) was already logged in /log_query.
    """
    from typing import Any

    # Prepare log data - only new information, not context already in /log_query
    log_data: dict[str, Any] = {
        "query_id": result.query_id,
        "duration_ms": result.duration_ms,
    }

    # Include row count if present
    if result.row_count is not None:
        log_data["row_count"] = result.row_count

    logger.info("SQL query result", **log_data)

    return {"status": "logged"}


@app.post("/log_connection")
async def log_connection(connection: DatabaseConnectionLog) -> dict[str, str]:
    """
    Log database connection details.

    Logs host, port, username, database, and mysql_command equivalent.
    This is called once per unique connection configuration to avoid duplicate logging.
    """
    logger.info(
        "MySQL connection details",
        mysql_command=connection.mysql_command,
        host=connection.host,
        port=connection.port,
        username=connection.username,
        database=connection.database,
    )

    return {"status": "logged"}


def message() -> str:
    return "rhizome is waiting for connections."


def run(home: Home | None = None) -> None:
    global _home
    _home = home or Home()
    port = _home.get_port()
    if port is None:
        raise ValueError("No port found in home configuration")

    # Set up unified logging before starting uvicorn
    setup_logging()

    uvicorn.run(
        app,
        host="127.0.0.1",
        port=port,
        log_config=None,  # Disable uvicorn's default logging config
        access_log=True,  # Keep access logs but they'll go through our handler
    )
