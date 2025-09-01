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
import structlog
from httpx_sse import connect_sse
from sqlmodel import Session, create_engine
from sqlmodel.sql._expression_select_cls import SelectOfScalar

from rhizome.config import Home
from rhizome.models.base import SanitizableModel
from rhizome.tools import Tools

TFirst = TypeVar("TFirst", bound=SanitizableModel)
TAll = TypeVar("TAll", bound=SanitizableModel)
TOne = TypeVar("TOne", bound=SanitizableModel)


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

    def __init__(self, home: Home | None = None, tools: Tools | None = None, *, data_in_logs: bool) -> None:
        self.home = home or Home()
        self.logger = structlog.get_logger("rhizome.client")
        self.tools = tools or Tools()
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
        self, query: SelectOfScalar[Any], result: SanitizableModel | Sequence[SanitizableModel] | None, method: str
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
                if isinstance(result, SanitizableModel):
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

    def _extract_model_fields(self, model: SanitizableModel) -> dict[str, Any]:
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

    def select_first(self, connection_string: str, query: SelectOfScalar[TFirst]) -> TFirst | None:
        """
        Execute a query and return the first sanitized result or None.

        Args:
            connection_string: Database connection string
            query: SQLModel query to execute

        Returns:
            First sanitized model instance or None
        """
        engine = create_engine(connection_string)
        with Session(engine) as session:
            result = session.exec(query).first()

            # Log the raw result before sanitization for debugging
            self._log_query_result(query, result, "select_first")

            if result is None:
                return None
            if not hasattr(result, "sanitize"):
                raise AttributeError(f"Result of type {type(result)} does not have a sanitize method")
            sanitized_result = result.sanitize()

            # Log the sanitized result as well
            self._log_query_result(query, sanitized_result, "select_first_sanitized")

            return sanitized_result

    def select_all(self, connection_string: str, query: SelectOfScalar[TAll]) -> list[TAll]:
        """
        Execute a query and return all sanitized results.

        Args:
            connection_string: Database connection string
            query: SQLModel query to execute

        Returns:
            List of sanitized model instances
        """
        engine = create_engine(connection_string)
        with Session(engine) as session:
            results = list(session.exec(query).all())

            # Log the raw results before sanitization for debugging
            self._log_query_result(query, results, "select_all")

            sanitized_results: list[TAll] = []
            for result in results:
                if not hasattr(result, "sanitize"):
                    raise AttributeError(f"Result of type {type(result)} does not have a sanitize method")
                sanitized_results.append(result.sanitize())

            # Log the sanitized results as well
            self._log_query_result(query, sanitized_results, "select_all_sanitized")

            return sanitized_results

    def select_one(self, connection_string: str, query: SelectOfScalar[TOne]) -> TOne:
        """
        Execute a query and return exactly one sanitized result.

        Args:
            connection_string: Database connection string
            query: SQLModel query to execute

        Returns:
            Single sanitized model instance

        Raises:
            Exception: If zero or more than one results found
        """
        engine = create_engine(connection_string)
        with Session(engine) as session:
            result = session.exec(query).one()

            # Log the raw result before sanitization for debugging
            self._log_query_result(query, result, "select_one")

            if not hasattr(result, "sanitize"):
                raise AttributeError(f"Result of type {type(result)} does not have a sanitize method")
            sanitized_result = result.sanitize()

            # Log the sanitized result as well
            self._log_query_result(query, sanitized_result, "select_one_sanitized")

            return sanitized_result
