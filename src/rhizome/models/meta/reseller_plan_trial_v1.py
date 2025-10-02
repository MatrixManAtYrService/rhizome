"""
SQLModel definition for the reseller_plan_trial table, version 1.

This module provides the V1 implementation of the ResellerPlanTrial model.
Currently, ResellerPlanTrialV1 is identical to the base ResellerPlanTrial class (name-only inheritance),
but as the table schema evolves across environments, future versions (V2, V3, etc.) will
contain actual schema differences (new columns, modified types, etc.).
"""

from __future__ import annotations

from ..metadata_registry import MetaSQLModel
from .reseller_plan_trial import ResellerPlanTrial


class ResellerPlanTrialV1(ResellerPlanTrial, MetaSQLModel, table=True):
    """
    Version 1 of the ResellerPlanTrial model.

    Currently a name-only inheritance from the base ResellerPlanTrial class.
    As schema changes are introduced in different environments, subsequent
    versions (V2, V3, etc.) will not be so trivial and will contain
    actual field modifications, additions, or removals.
    """

    __tablename__ = "reseller_plan_trial"  # type: ignore

    def sanitize(self) -> ResellerPlanTrialV1:
        """Return a sanitized copy of this ResellerPlanTrialV1 instance."""
        return ResellerPlanTrialV1(
            created_time=self.created_time,
            finalize_time=self.finalize_time,
            id=self.id,
            merchant_plan_id=self.merchant_plan_id,
            modified_time=self.modified_time,
            reseller_id=self.reseller_id,
            trial_days=self.trial_days,
            uuid=self.uuid,
        )
