"""Pydantic models for rhizome server."""

from typing import Any

from pydantic import BaseModel


class SqlQueryLog(BaseModel):
    """Request model for SQL query logging."""

    statement: str
    parameters: dict[str, Any] | list[Any] | None = None
    database: str
    connection_string: str


class SqlQueryResultLog(BaseModel):
    """Request model for SQL query result logging."""

    statement: str
    database: str
    connection_string: str
    duration_ms: float
    row_count: int | None = None
