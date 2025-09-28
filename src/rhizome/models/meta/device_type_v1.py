"""
SQLModel definition for the device_type table, version 1.

This module provides the V1 implementation of the DeviceType model.
Currently, DeviceTypeV1 is identical to the base DeviceType class (name-only inheritance),
but as the table schema evolves across environments, future versions (V2, V3, etc.) will
contain actual schema differences (new columns, modified types, etc.).
"""

from __future__ import annotations

from ...sanitize_helpers import sanitize_uuid_field
from ..metadata_registry import MetaSQLModel
from .device_type import DeviceType


class DeviceTypeV1(DeviceType, MetaSQLModel, table=True):
    """
    Version 1 of the DeviceType model.

    Currently a name-only inheritance from the base DeviceType class.
    As schema changes are introduced in different environments, subsequent
    versions (V2, V3, etc.) will not be so trivial and will contain
    actual field modifications, additions, or removals.
    """

    __tablename__ = "device_type"

    def sanitize(self) -> DeviceTypeV1:
        """Return a sanitized copy of this DeviceTypeV1 instance."""
        return DeviceTypeV1(
            id=self.id,
            uuid=sanitize_uuid_field(self.uuid, 13),
            name=self.name,
            models=self.models,
            skus=self.skus,
            sdk_version=self.sdk_version,
            prioritized_kernel_types=self.prioritized_kernel_types,
            modified_time=self.modified_time,
            deleted_time=self.deleted_time,
        )