"""
SQLModel definition for the merchant_plan table, version 1.

This module provides the V1 implementation of the MerchantPlan model.
Currently, MerchantPlanV1 is identical to the base MerchantPlan class (name-only inheritance),
but as the table schema evolves across environments, future versions (V2, V3, etc.) will
contain actual schema differences (new columns, modified types, etc.).
"""

from __future__ import annotations

from ...sanitize_helpers import sanitize_uuid_field
from ..metadata_registry import MetaSQLModel
from .merchant_plan import MerchantPlan


class MerchantPlanV1(MerchantPlan, MetaSQLModel, table=True):
    """
    Version 1 of the MerchantPlan model.

    Currently a name-only inheritance from the base MerchantPlan class.
    As schema changes are introduced in different environments, subsequent
    versions (V2, V3, etc.) will not be so trivial and will contain
    actual field modifications, additions, or removals.
    """

    __tablename__ = "merchant_plan"  # type: ignore

    def sanitize(self) -> MerchantPlanV1:
        """Return a sanitized copy of this MerchantPlanV1 instance."""
        return MerchantPlanV1(
            id=self.id,
            uuid=sanitize_uuid_field(self.uuid, 13),
            name=self.name,
            type=self.type,
            plan_code=self.plan_code,
            app_bundle_id=self.app_bundle_id,
            description=self.description,
            reseller_id=self.reseller_id,
            merchant_plan_group_id=self.merchant_plan_group_id,
            activation_time=self.activation_time,
            deactivation_time=self.deactivation_time,
            bill_to_mid=self.bill_to_mid,
            enforced=self.enforced,
            created_time=self.created_time,
            modified_time=self.modified_time,
            default_plan=self.default_plan,
            hidden=self.hidden,
            tags=self.tags,
        )
