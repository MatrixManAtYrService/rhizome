"""
SQLModel definition for the device_provision table, version 1.

This module provides the V1 implementation of the DeviceProvision model.
Currently, DeviceProvisionV1 is identical to the base DeviceProvision class (name-only inheritance),
but as the table schema evolves across environments, future versions (V2, V3, etc.) will
contain actual schema differences (new columns, modified types, etc.).
"""

from __future__ import annotations

from ..metadata_registry import MetaSQLModel
from .device_provision import DeviceProvision


class DeviceProvisionV1(DeviceProvision, MetaSQLModel, table=True):
    """
    Version 1 of the DeviceProvision model.

    Currently a name-only inheritance from the base DeviceProvision class.
    As schema changes are introduced in different environments, subsequent
    versions (V2, V3, etc.) will not be so trivial and will contain
    actual field modifications, additions, or removals.
    """

    __tablename__ = "device_provision"

    def sanitize(self) -> DeviceProvisionV1:
        """Return a sanitized copy of this DeviceProvisionV1 instance."""
        return DeviceProvisionV1(
            activated_time=self.activated_time,
            activation_code=self.activation_code,
            activation_code_created_time=self.activation_code_created_time,
            chip_uid=self.chip_uid,
            deauthorization_attempts=self.deauthorization_attempts,
            deauthorization_code=self.deauthorization_code,
            deleted_time=self.deleted_time,
            email_sent=self.email_sent,
            id=self.id,
            imei=self.imei,
            last_activation_code=self.last_activation_code,
            merchant_id=self.merchant_id,
            modified_time=self.modified_time,
            next_calltag_notify_time=self.next_calltag_notify_time,
            order_type=self.order_type,
            provision_info=self.provision_info,
            provisioned_time=self.provisioned_time,
            reseller_id=self.reseller_id,
            serial_number=self.serial_number,
            shipping_status=self.shipping_status,
            sms_sent=self.sms_sent,
            tasq_order_number=self.tasq_order_number,
            terminal_id=self.terminal_id,
        )
