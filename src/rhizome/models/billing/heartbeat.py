"""
SQLModel definition for the heartbeat table.

This module provides the SQLModel class for the heartbeat table from the
billing database, along with sanitization functions.
"""

from __future__ import annotations

from sqlmodel import Field, SQLModel

from typing import TypeVar

T = TypeVar("T", bound="Heartbeat")


class Heartbeat(SQLModel, table=False):
    """
    SQLModel for the `heartbeat` table.

    This model represents heartbeat records in the billing system,
    containing server heartbeat and replication status information.
    """

    ts: str = Field(max_length=26, description="Timestamp string")
    server_id: int = Field(primary_key=True, description="Server identifier")
    file: str | None = Field(default=None, max_length=255, description="Binary log file name")
    position: int | None = Field(default=None, description="Position in binary log")
    relay_master_log_file: str | None = Field(default=None, max_length=255, description="Master log file name")
    exec_master_log_pos: int | None = Field(default=None, description="Execution position in master log")

    def sanitize(self: T) -> T:
        """Return a sanitized copy of this Heartbeat instance."""
        return Heartbeat(
            ts=self.ts,
            server_id=self.server_id,
            file=self.file,
            position=self.position,
            relay_master_log_file=self.relay_master_log_file,
            exec_master_log_pos=self.exec_master_log_pos,
        )