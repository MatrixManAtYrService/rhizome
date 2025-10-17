"""
Rhizome client for communicating with the rhizome server to manage port forwarding.

This module provides the client interface for requesting port forwards from the
rhizome server and getting connection handles back.
"""

import json
import time
from collections.abc import Sequence
from dataclasses import dataclass
from typing import Any, TypeVar

import httpx
import sqlalchemy
import structlog
from httpx_sse import connect_sse
from sqlmodel import create_engine
from sqlmodel.sql._expression_select_cls import SelectOfScalar

from rhizome.models.base import RhizomeModel
from rhizome.tools import SubprocessTools
from trifolium.config import Home

TFirst = TypeVar("TFirst", bound=RhizomeModel)
TAll = TypeVar("TAll", bound=RhizomeModel)
TOne = TypeVar("TOne", bound=RhizomeModel)


@dataclass
class Handle:
    """
    Database connection handle returned by rhizome.

    Contains the connection string and port information needed to connect
    to a database through kubectl port-forward managed by rhizome server.
    """

    connection_string: str
    local_port: int
    sql_connection: str  # The original SQL connection name

    def __post_init__(self) -> None:
        """Validate that the connection is available."""
        # TODO: Add connection validation logic if needed
        pass


class RhizomeClient:
    """Client for communicating with the rhizome server."""

    def __init__(self, home: Home | None = None, tools: SubprocessTools | None = None, *, data_in_logs: bool) -> None:
        self.home = home or Home()
        self.logger = structlog.get_logger("rhizome.client")
        self.tools = tools or SubprocessTools()
        self._base_url: str | None = None
        self.data_in_logs = data_in_logs

    @property
    def base_url(self) -> str:
        """Get the rhizome server URL from the port file."""
        if self._base_url is None:
            port = self.home.get_port()
            if port is None:
                raise RuntimeError("Rhizome server port not found. Make sure the rhizome server is running.")
            self._base_url = f"http://0.0.0.0:{port}"
        return self._base_url

    def request_portforward(
        self, kube_context: str, kube_namespace: str, kube_deployment: str, sql_connection: str, local_port: int = 3306
    ) -> Handle:
        """
        Request a port forward from the rhizome server.

        Args:
            kube_context: Kubernetes context name
            kube_namespace: Kubernetes namespace
            kube_deployment: Kubernetes deployment name
            sql_connection: SQL connection string (e.g., "clover-prod-databases:us-central1:billing-bookkeeper")
            local_port: Local port to forward to (default: 3306)

        Returns:
            Handle: Connection handle with connection string and port info
        """
        # Make request to rhizome server to start port forward
        with httpx.Client() as client:
            response = client.post(
                f"{self.base_url}/portforward",
                json={
                    "kube_context": kube_context,
                    "kube_namespace": kube_namespace,
                    "kube_deployment": kube_deployment,
                    "sql_connection": sql_connection,
                    "local_port": local_port,
                },
            )
            response.raise_for_status()

        # Wait a moment for the port forward to establish
        time.sleep(2)

        # Build connection string
        connection_string = f"mysql://0.0.0.0:{local_port}"

        return Handle(connection_string=connection_string, local_port=local_port, sql_connection=sql_connection)

    def request_localk8s(
        self, kube_context: str, kube_namespace: str, kube_deployment: str, local_port: int = 3306, delay: float = 2.0
    ) -> Handle:
        """
        Request a port forward to local Kubernetes cluster from the rhizome server.

        This method uses Server-Sent Events to wait for credentials to be provided
        by the server, ensuring the connection is ready for immediate use.

        Args:
            kube_context: Kubernetes context name (e.g., "kind-rhizome-test")
            kube_namespace: Kubernetes namespace (e.g., "default")
            kube_deployment: Kubernetes deployment/pod name (e.g., "mysql")
            local_port: Local port to forward to (default: 3306)
            delay: Delay before server provides credentials (for testing)

        Returns:
            Handle: Connection handle with full connection string including credentials
        """
        # Track timing for testing
        start_time = time.time()
        credentials: dict[str, Any] = {}

        # Connect to SSE endpoint for credential streaming
        with (
            httpx.Client() as client,
            connect_sse(
                client,
                "POST",
                f"{self.base_url}/localk8s",
                json={
                    "kube_context": kube_context,
                    "kube_namespace": kube_namespace,
                    "kube_deployment": kube_deployment,
                    "local_port": local_port,
                    "delay": delay,
                },
            ) as event_source,
        ):
            for sse in event_source.iter_sse():
                if sse.event == "status":
                    status_data = json.loads(sse.data)
                    print(f"Status: {status_data['status']}")

                elif sse.event == "credentials":
                    credentials = json.loads(sse.data)
                    print(f"Credentials received after {time.time() - start_time:.2f}s")
                    break

        if not credentials:
            raise RuntimeError("Failed to receive credentials from server")

        return Handle(
            connection_string=credentials["connection_string"],
            local_port=local_port,
            sql_connection=f"localk8s:{kube_namespace}:{kube_deployment}",
        )

    def request_sleeper(self, iterations: int = 5) -> Handle:
        """
        Request a sleeper process from the rhizome server.

        Args:
            iterations: Number of times the sleeper should count (default: 5)

        Returns:
            Handle: Connection handle with sleeper process info
        """
        # Make request to rhizome server to start sleeper
        with httpx.Client() as client:
            response = client.post(f"{self.base_url}/sleeper", json={"iterations": iterations})
            response.raise_for_status()

        # Wait a moment for the process to start
        time.sleep(0.1)

        # Return a handle (sleeper doesn't have a real connection string)
        return Handle(
            connection_string="sleeper://localhost/test",
            local_port=0,  # No actual port for sleeper
            sql_connection=f"sleeper-{iterations}-iterations",
        )

    def _log_query_result(
        self, query: SelectOfScalar[Any], result: RhizomeModel | Sequence[RhizomeModel] | None, method: str
    ) -> None:
        """Log query and result data using structured logging for debugging external infrastructure tests."""
        if not self.data_in_logs:
            return

        try:
            # Extract query information
            query_str = str(query)

            # Extract result data if it exists
            if result is None:
                self.logger.info(
                    "Database query executed",
                    method=method,
                    query=query_str,
                    result_count=0,
                    result="None",
                )
            elif isinstance(result, list | tuple):
                # For select_all - log count and first few records
                self.logger.info(
                    "Database query executed",
                    method=method,
                    query=query_str,
                    result_count=len(result),
                    **{
                        f"result_{i}_{k}": str(v)
                        for i, item in enumerate(result[:3])
                        for k, v in self._extract_model_fields(item).items()
                    },
                )
            else:
                if isinstance(result, RhizomeModel):
                    # For select_first and select_one - log the single result
                    result_fields = self._extract_model_fields(result)
                    self.logger.info(
                        "Database query executed",
                        method=method,
                        query=query_str,
                        result_count=1,
                        **{f"result_{k}": str(v) for k, v in result_fields.items()},
                    )
        except Exception as e:
            # Don't let logging issues break the actual query
            self.logger.warning("Failed to log query result", error=str(e))

    def _extract_model_fields(self, model: RhizomeModel) -> dict[str, Any]:
        """Extract field values from a model for logging."""
        try:
            # Get all non-private attributes from the model
            fields: dict[str, Any] = {}
            if hasattr(model, "__dict__"):
                for key, value in model.__dict__.items():
                    if not key.startswith("_"):
                        fields[str(key)] = value
            return fields
        except Exception:
            return {"error": "Could not extract model fields"}

    def _create_instrumented_engine(self, connection_string: str) -> sqlalchemy.Engine:
        """
        Create a SQLAlchemy engine with event listeners for query logging.

        This method provides centralized query logging via SQLAlchemy's event system.
        All queries are logged to the rhizome server before and after execution.

        Args:
            connection_string: Database connection string

        Returns:
            sqlalchemy.Engine configured with logging event listeners
        """
        import time
        import uuid
        from contextlib import suppress

        from sqlalchemy import event
        from sqlalchemy.engine import Connection, ExecutionContext

        engine = create_engine(connection_string)

        # Extract database name from connection string for logging
        database = engine.url.database or "unknown"

        @event.listens_for(engine, "before_cursor_execute")
        def before_cursor_execute(  # type: ignore[reportUnusedFunction]
            conn: Connection,
            cursor: Any,  # noqa: ANN401 - DBAPI cursor type varies by driver
            statement: str,
            parameters: tuple[Any, ...] | dict[str, Any],
            context: ExecutionContext,
            executemany: bool,
        ) -> None:
            """Log SQL query before execution."""
            # Generate unique query ID and store with start time
            query_id = str(uuid.uuid4())[:8]  # Use first 8 chars for readability
            context._query_id = query_id  # type: ignore[attr-defined]
            context._query_start_time = time.time()  # type: ignore[attr-defined]

            # Log to rhizome server (non-blocking, fire-and-forget)
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
                    timeout=1.0,  # Short timeout to avoid blocking queries
                )

        @event.listens_for(engine, "after_cursor_execute")
        def after_cursor_execute(  # type: ignore[reportUnusedFunction]
            conn: Connection,
            cursor: Any,  # noqa: ANN401 - DBAPI cursor type varies by driver
            statement: str,
            parameters: tuple[Any, ...] | dict[str, Any],
            context: ExecutionContext,
            executemany: bool,
        ) -> None:
            """Log SQL query result after execution."""
            # Calculate duration and retrieve query ID
            duration = (time.time() - context._query_start_time) * 1000  # type: ignore[attr-defined]  # Convert to ms
            query_id = context._query_id  # type: ignore[attr-defined]

            # Get row count if available
            row_count = cursor.rowcount if cursor.rowcount >= 0 else None

            # Log to rhizome server (non-blocking, fire-and-forget)
            # Note: Only log query_id, duration, and row_count. Context (statement, database, etc.) was already logged.
            with suppress(Exception):
                httpx.post(
                    f"{self.base_url}/log_query_result",
                    json={  # type: ignore[arg-type]
                        "query_id": query_id,
                        "duration_ms": duration,
                        "row_count": row_count,
                    },
                    timeout=1.0,  # Short timeout to avoid blocking queries
                )

        return engine

    def select_first(self, database_id: str, query: SelectOfScalar[TFirst], sanitize: bool = True) -> TFirst | None:
        """
        Execute a query server-side and return the first result or None.

        Args:
            database_id: Database identifier (RhizomeEnvironment enum value, e.g., "dev_meta")
            query: SQLModel query to execute
            sanitize: If True, return sanitized result. If False, return raw result. Default: True

        Returns:
            First model instance (sanitized or raw) or None
        """
        from rhizome.serialization import deserialize_result, get_model_info, serialize_query
        from rhizome.server_models import ExecuteQueryRequest, GetMode

        # Serialize query
        sql, parameters = serialize_query(query)
        model_info = get_model_info(query)

        # Send to server
        request = ExecuteQueryRequest(
            database_id=database_id,
            sql=sql,
            parameters=parameters,
            model_module=model_info["model_module"],
            model_class=model_info["model_class"],
            mode=GetMode.FIRST,
            sanitize=sanitize,
        )

        with httpx.Client() as client:
            response = client.post(
                f"{self.base_url}/execute_query",
                json=request.model_dump(),
            )
            response.raise_for_status()

        # Parse response
        from rhizome.server_models import ExecuteQueryResponse

        result = ExecuteQueryResponse.model_validate(response.json())

        if not result.success:
            raise RuntimeError(f"Query execution failed: {result.error}")

        if result.result is None:
            return None

        # Deserialize result
        # Import the model class to deserialize
        from rhizome.serialization import import_model_class

        model_class = import_model_class(model_info["model_module"], model_info["model_class"])
        # Type assertion: we know result.result is a dict here, not a list
        assert isinstance(result.result, dict)
        return deserialize_result(result.result, model_class)  # type: ignore[return-value]

    def select_all(self, database_id: str, query: SelectOfScalar[TAll], sanitize: bool = True) -> list[TAll]:
        """
        Execute a query server-side and return all results.

        Args:
            database_id: Database identifier (RhizomeEnvironment enum value, e.g., "dev_meta")
            query: SQLModel query to execute
            sanitize: If True, return sanitized results. If False, return raw results. Default: True

        Returns:
            List of model instances (sanitized or raw)
        """
        from rhizome.serialization import deserialize_result_list, get_model_info, serialize_query
        from rhizome.server_models import ExecuteQueryRequest, GetMode

        # Serialize query
        sql, parameters = serialize_query(query)
        model_info = get_model_info(query)

        # Send to server
        request = ExecuteQueryRequest(
            database_id=database_id,
            sql=sql,
            parameters=parameters,
            model_module=model_info["model_module"],
            model_class=model_info["model_class"],
            mode=GetMode.ALL,
            sanitize=sanitize,
        )

        with httpx.Client() as client:
            response = client.post(
                f"{self.base_url}/execute_query",
                json=request.model_dump(),
            )
            response.raise_for_status()

        # Parse response
        from rhizome.server_models import ExecuteQueryResponse

        result = ExecuteQueryResponse.model_validate(response.json())

        if not result.success:
            raise RuntimeError(f"Query execution failed: {result.error}")

        if result.result is None or result.result == []:
            return []

        # Deserialize results
        from rhizome.serialization import import_model_class

        model_class = import_model_class(model_info["model_module"], model_info["model_class"])
        return deserialize_result_list(result.result, model_class)  # type: ignore[arg-type]

    def select_one(self, database_id: str, query: SelectOfScalar[TOne], sanitize: bool = True) -> TOne:
        """
        Execute a query server-side and return exactly one result.

        Args:
            database_id: Database identifier (RhizomeEnvironment enum value, e.g., "dev_meta")
            query: SQLModel query to execute
            sanitize: If True, return sanitized result. If False, return raw result. Default: True

        Returns:
            Single model instance (sanitized or raw)

        Raises:
            RuntimeError: If zero or more than one results found
        """
        from rhizome.serialization import deserialize_result, get_model_info, serialize_query
        from rhizome.server_models import ExecuteQueryRequest, GetMode

        # Serialize query
        sql, parameters = serialize_query(query)
        model_info = get_model_info(query)

        # Send to server
        request = ExecuteQueryRequest(
            database_id=database_id,
            sql=sql,
            parameters=parameters,
            model_module=model_info["model_module"],
            model_class=model_info["model_class"],
            mode=GetMode.ONE,
            sanitize=sanitize,
        )

        with httpx.Client() as client:
            response = client.post(
                f"{self.base_url}/execute_query",
                json=request.model_dump(),
            )
            response.raise_for_status()

        # Parse response
        from rhizome.server_models import ExecuteQueryResponse

        result = ExecuteQueryResponse.model_validate(response.json())

        if not result.success:
            raise RuntimeError(f"Query execution failed: {result.error}")

        if result.result is None:
            raise RuntimeError("Query returned no results (expected exactly one)")

        # Deserialize result
        from rhizome.serialization import import_model_class

        model_class = import_model_class(model_info["model_module"], model_info["model_class"])
        # Type assertion: we know result.result is a dict here, not a list
        assert isinstance(result.result, dict)
        deserialized = deserialize_result(result.result, model_class)

        if deserialized is None:
            raise RuntimeError("Failed to deserialize result")

        return deserialized  # type: ignore[return-value]

    def execute_raw_query(self, connection_string: str, query: str) -> object | None:
        """
        Execute a raw SQL query and return the result.

        Args:
            connection_string: Database connection string
            query: Raw SQL query to execute

        Returns:
            The result of the query execution.
        """
        engine = self._create_instrumented_engine(connection_string)
        with engine.connect() as connection:
            result = connection.execute(sqlalchemy.text(query))
            return result.first()

    def execute_write_query(
        self,
        query_name: str,
        database_id: str,
        params: dict[str, str | int | float | None],
        reason: str | None = None,
        entity_descriptions: dict[str, str] | None = None,
    ) -> dict[str, Any]:
        """
        Execute a pre-defined write query with user approval via the rhizome server.

        The rhizome server will:
        1. Look up the canned query by name
        2. Render it with the provided parameters
        3. Show it to the user in the terminal with rich formatting
        4. Prompt for yes/no approval
        5. If approved, execute with RW credentials
        6. Return the result

        Args:
            query_name: Name of the canned query to execute
            database_id: Database identifier (RhizomeEnvironment enum value, e.g., "dev_meta")
            params: Parameters to pass to the query
            reason: Optional explanation of why this operation is necessary
            entity_descriptions: Optional dict providing context about entities being modified
                                (e.g., {"role_id_7477": "Super Administrator role for Clover reseller"})

        Returns:
            Dictionary with keys:
            - approved: bool - Whether user approved the query
            - executed: bool - Whether query was executed
            - rows_affected: int | None - Number of rows affected
            - error: str | None - Error message if any

        Example:
            >>> client.execute_write_query(
            ...     query_name="create_reseller_role",
            ...     database_id="dev_meta",
            ...     params={"reseller_id": 123, "account_id": 456, "permissions_id": 789},
            ...     reason="Grant Super Administrator permissions to MFF test account",
            ...     entity_descriptions={
            ...         "reseller_id_123": "Clover reseller",
            ...         "account_id_456": "mff_user@example.com (MFF test account)",
            ...         "permissions_id_789": "Super Administrator role"
            ...     }
            ... )
            {'approved': True, 'executed': True, 'rows_affected': 1, 'error': None}
        """
        payload: dict[str, Any] = {
            "query_name": query_name,
            "database_id": database_id,
            "params": params,
        }

        if reason is not None:
            payload["reason"] = reason

        if entity_descriptions is not None:
            payload["entity_descriptions"] = entity_descriptions

        with httpx.Client(timeout=300.0) as client:  # 5 min timeout for user interaction
            response = client.post(
                f"{self.base_url}/write_query",
                json=payload,
            )
            response.raise_for_status()
            return response.json()
