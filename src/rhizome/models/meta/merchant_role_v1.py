"""
SQLModel definition for the merchant_role table, version 1.

This module provides the V1 implementation of the MerchantRole model.
Currently, MerchantRoleV1 is identical to the base MerchantRole class (name-only inheritance),
but as the table schema evolves across environments, future versions (V2, V3, etc.) will
contain actual schema differences (new columns, modified types, etc.).
"""

from __future__ import annotations

from ..metadata_registry import MetaSQLModel
from .merchant_role import MerchantRole


class MerchantRoleV1(MerchantRole, MetaSQLModel, table=True):
    """
    Version 1 of the MerchantRole model.

    Currently a name-only inheritance from the base MerchantRole class.
    As schema changes are introduced in different environments, subsequent
    versions (V2, V3, etc.) will not be so trivial and will contain
    actual field modifications, additions, or removals.
    """

    __tablename__ = "merchant_role"  # type: ignore

    def sanitize(self) -> MerchantRoleV1:
        """Return a sanitized copy of this MerchantRoleV1 instance."""
        return MerchantRoleV1(
            account_id=self.account_id,
            created_time=self.created_time,
            custom_id=self.custom_id,
            deleted_time=self.deleted_time,
            id=self.id,
            merchant_id=self.merchant_id,
            modified_time=self.modified_time,
            nickname=self.nickname,
            pin=self.pin,
            role=self.role,
            role_id=self.role_id,
        )
