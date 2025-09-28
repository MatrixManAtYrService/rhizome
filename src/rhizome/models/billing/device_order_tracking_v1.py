"""
SQLModel definition for the device_order_tracking table, version 1.

This module provides the V1 implementation of the DeviceOrderTracking model.
Currently, DeviceOrderTrackingV1 is identical to the base DeviceOrderTracking class (name-only inheritance),
but as the table schema evolves across environments, future versions (V2, V3, etc.) will
contain actual schema differences (new columns, modified types, etc.).
"""

from __future__ import annotations

from ..metadata_registry import NaProdSQLModel
from .device_order_tracking import DeviceOrderTracking


class DeviceOrderTrackingV1(DeviceOrderTracking, NaProdSQLModel, table=True):
    """
    Version 1 of the DeviceOrderTracking model.

    Currently a name-only inheritance from the base DeviceOrderTracking class.
    As schema changes are introduced in different environments, subsequent
    versions (V2, V3, etc.) will not be so trivial and will contain
    actual field modifications, additions, or removals.
    """

    __tablename__ = "device_order_tracking"  # type: ignore
