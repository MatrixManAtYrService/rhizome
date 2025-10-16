"""Pydantic models for rhizome server."""

from enum import StrEnum, auto
from typing import Any

from pydantic import BaseModel


class SqlQueryLog(BaseModel):
    """Request model for SQL query logging."""

    query_id: str
    statement: str
    parameters: dict[str, Any] | list[Any] | None = None
    database: str
    connection_string: str


class SqlQueryResultLog(BaseModel):
    """Request model for SQL query result logging."""

    query_id: str
    duration_ms: float
    row_count: int | None = None


class DatabaseConnectionLog(BaseModel):
    """Request model for database connection logging."""

    host: str
    port: int
    username: str
    database: str
    mysql_command: str


class GetMode(StrEnum):
    """Mode for query execution."""

    FIRST = auto()  # Return first result or None
    ALL = auto()  # Return all results as list
    ONE = auto()  # Return exactly one result (raises if 0 or >1)


class ExecuteQueryRequest(BaseModel):
    """Request model for server-side query execution."""

    # Environment name (e.g., "DevMeta", "DevBillingBookkeeper")
    environment_name: str

    # Query details
    sql: str  # Compiled SQL string
    parameters: dict[str, Any]  # Query parameters

    # Model information for result deserialization
    model_module: str  # e.g., "rhizome.models.meta.reseller"
    model_class: str  # e.g., "Reseller"

    # Query execution mode
    mode: GetMode

    # Whether to sanitize results
    sanitize: bool = True


class ExecuteQueryResponse(BaseModel):
    """Response model for server-side query execution."""

    success: bool
    result: dict[str, Any] | list[dict[str, Any]] | None  # Serialized result(s)
    error: str | None = None
    row_count: int | None = None  # For ALL mode, number of results returned
