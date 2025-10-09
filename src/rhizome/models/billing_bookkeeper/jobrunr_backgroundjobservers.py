"""
SQLModel definition for the jobrunr_backgroundjobservers table.

This module provides the SQLModel class for the jobrunr_backgroundjobservers table from the
billing-bookkeeper database, along with sanitization functions.
"""

from __future__ import annotations

import datetime
from decimal import Decimal

from sqlmodel import Field

from ...models.base import RhizomeModel


class JobrunrBackgroundjobservers(RhizomeModel, table=False):
    """
    SQLModel for the `jobrunr_backgroundjobservers` table.

    This model represents jobrunr backgroundjobservers records in the billing system.
    """

    id: str = Field(primary_key=True, max_length=36, description="Id")
    workerPoolSize: int = Field(description="Workerpoolsize")
    pollIntervalInSeconds: int = Field(description="Pollintervalinseconds")
    firstHeartbeat: datetime.datetime = Field(description="Firstheartbeat")
    lastHeartbeat: datetime.datetime = Field(description="Lastheartbeat")
    running: int = Field(description="Running")
    systemTotalMemory: int = Field(description="Systemtotalmemory")
    systemFreeMemory: int = Field(description="Systemfreememory")
    systemCpuLoad: Decimal = Field(max_digits=3, decimal_places=2, description="Systemcpuload")
    processMaxMemory: int = Field(description="Processmaxmemory")
    processFreeMemory: int = Field(description="Processfreememory")
    processAllocatedMemory: int = Field(description="Processallocatedmemory")
    processCpuLoad: Decimal = Field(max_digits=3, decimal_places=2, description="Processcpuload")
    deleteSucceededJobsAfter: str | None = Field(default=None, max_length=32, description="Deletesucceededjobsafter")
    permanentlyDeleteJobsAfter: str | None = Field(default=None, max_length=32, description="Permanentlydeletejobsafter")

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
