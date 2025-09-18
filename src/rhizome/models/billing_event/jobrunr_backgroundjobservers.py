"""
SQLModel definition for the jobrunr_backgroundjobservers table.

This module provides the SQLModel class for the jobrunr_backgroundjobservers table from the
billing-event database, along with sanitization functions.
"""

from __future__ import annotations

import datetime
from decimal import Decimal

from sqlmodel import Field

from ...models.base import RhizomeModel


class JobrunrBackgroundjobservers(RhizomeModel, table=False):
    """
    SQLModel for the `jobrunr_backgroundjobservers` table.

    This model represents background job servers in the JobRunr system,
    containing information about server status, performance metrics, and configuration.
    """

    id: str = Field(primary_key=True, max_length=36, description="Primary key, UUID of the background job server")
    workerPoolSize: int = Field(description="Size of the worker pool")
    pollIntervalInSeconds: int = Field(description="Polling interval in seconds")
    firstHeartbeat: datetime.datetime = Field(description="Timestamp of the first heartbeat")
    lastHeartbeat: datetime.datetime = Field(description="Timestamp of the last heartbeat")
    running: int = Field(description="Running status (typically 0 or 1)")
    systemTotalMemory: int = Field(description="Total system memory in bytes")
    systemFreeMemory: int = Field(description="Free system memory in bytes")
    systemCpuLoad: Decimal = Field(max_digits=3, decimal_places=2, description="System CPU load percentage")
    processMaxMemory: int = Field(description="Process maximum memory in bytes")
    processFreeMemory: int = Field(description="Process free memory in bytes")
    processAllocatedMemory: int = Field(description="Process allocated memory in bytes")
    processCpuLoad: Decimal = Field(max_digits=3, decimal_places=2, description="Process CPU load percentage")
    deleteSucceededJobsAfter: str | None = Field(default=None, max_length=32, description="Duration after which succeeded jobs are deleted")
    permanentlyDeleteJobsAfter: str | None = Field(default=None, max_length=32, description="Duration after which jobs are permanently deleted")

    def sanitize(self) -> JobrunrBackgroundjobservers:
        """Return a sanitized copy of this JobrunrBackgroundjobservers instance."""
        return JobrunrBackgroundjobservers(
            id=self.id,
            workerPoolSize=self.workerPoolSize,
            pollIntervalInSeconds=self.pollIntervalInSeconds,
            firstHeartbeat=self.firstHeartbeat,
            lastHeartbeat=self.lastHeartbeat,
            running=self.running,
            systemTotalMemory=self.systemTotalMemory,
            systemFreeMemory=self.systemFreeMemory,
            systemCpuLoad=self.systemCpuLoad,
            processMaxMemory=self.processMaxMemory,
            processFreeMemory=self.processFreeMemory,
            processAllocatedMemory=self.processAllocatedMemory,
            processCpuLoad=self.processCpuLoad,
            deleteSucceededJobsAfter=self.deleteSucceededJobsAfter,
            permanentlyDeleteJobsAfter=self.permanentlyDeleteJobsAfter,
        )