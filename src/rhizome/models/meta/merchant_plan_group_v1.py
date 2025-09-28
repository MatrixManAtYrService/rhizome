"""
SQLModel definition for the merchant_plan_group table, version 1.

This module provides the V1 implementation of the MerchantPlanGroup model.
Currently, MerchantPlanGroupV1 is identical to the base MerchantPlanGroup class (name-only inheritance),
but as the table schema evolves across environments, future versions (V2, V3, etc.) will
contain actual schema differences (new columns, modified types, etc.).
"""

from __future__ import annotations

from ...sanitize_helpers import sanitize_uuid_field
from ..metadata_registry import MetaSQLModel
from .merchant_plan_group import MerchantPlanGroup


class MerchantPlanGroupV1(MerchantPlanGroup, MetaSQLModel, table=True):
    """
    Version 1 of the MerchantPlanGroup model.

    Currently a name-only inheritance from the base MerchantPlanGroup class.
    As schema changes are introduced in different environments, subsequent
    versions (V2, V3, etc.) will not be so trivial and will contain
    actual field modifications, additions, or removals.
    """

    __tablename__ = "merchant_plan_group"

    def sanitize(self) -> MerchantPlanGroupV1:
        """Return a sanitized copy of this MerchantPlanGroupV1 instance."""
        return MerchantPlanGroupV1(
            created_time=self.created_time,
            deleted_time=self.deleted_time,
            enforce_assignment=self.enforce_assignment,
            id=self.id,
            linkable=self.linkable,
            modified_time=self.modified_time,
            name=self.name,
            trial_days=self.trial_days,
            uuid=self.uuid,
        )
