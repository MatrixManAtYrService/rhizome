"""
SQLModel definition for the device_events table, version 1.

This module provides the V1 implementation of the DeviceEvents model.
Currently, DeviceEventsV1 is identical to the base DeviceEvents class (name-only inheritance),
but as the table schema evolves across environments, future versions (V2, V3, etc.) will
contain actual schema differences (new columns, modified types, etc.).
"""

from __future__ import annotations

from ..metadata_registry import MetaSQLModel
from .device_events import DeviceEvents


class DeviceEventsV1(DeviceEvents, MetaSQLModel, table=True):
    """
    Version 1 of the DeviceEvents model.

    Currently a name-only inheritance from the base DeviceEvents class.
    As schema changes are introduced in different environments, subsequent
    versions (V2, V3, etc.) will not be so trivial and will contain
    actual field modifications, additions, or removals.
    """

    __tablename__ = "device_events"

    def sanitize(self) -> DeviceEventsV1:
        """Return a sanitized copy of this DeviceEventsV1 instance."""
        return DeviceEventsV1(
            account_id=self.account_id,
            device_event=self.device_event,
            device_type_id=self.device_type_id,
            id=self.id,
            internal_account_id=self.internal_account_id,
            merchant_id=self.merchant_id,
            serial_number=self.serial_number,
            timestamp=self.timestamp,
        )
