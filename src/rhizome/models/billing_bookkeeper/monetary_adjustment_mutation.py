"""
SQLModel definition for the monetary_adjustment_mutation table.

This module provides the SQLModel class for the monetary_adjustment_mutation table from the
billing-bookkeeper database, along with sanitization functions.
"""

from __future__ import annotations

import datetime

from sqlmodel import Field

from ...models.base import RhizomeModel
from ...sanitize_helpers import sanitize_uuid_field


class MonetaryAdjustmentMutation(RhizomeModel, table=False):
    """
    SQLModel for the `monetary_adjustment_mutation` table.

    This model represents monetary adjustment mutation records in the billing system.
    """

    id: int | None = Field(default=None, primary_key=True, description="Id")
    mutation_action: str = Field(description="Mutation Action")
    mutation_timestamp: datetime.datetime = Field(description="Mutation Timestamp")
    monetary_adjustment_id: int = Field(description="Monetary Adjustment Id")
    uuid: str = Field(max_length=26, unique=True, description="Uuid")
    billing_entity_uuid: str = Field(max_length=26, description="Billing Entity Uuid")
    adjust_fee_summary_uuid: str = Field(max_length=26, description="Adjust Fee Summary Uuid")
    qualified_fee_summary_uuid: str = Field(max_length=26, description="Qualified Fee Summary Uuid")
    rule_uuid: str = Field(max_length=26, description="Rule Uuid")
    rule_criteria_uuid: str | None = Field(default=None, max_length=26, description="Rule Criteria Uuid")
    rule_type: str = Field(description="Rule Type")
    request_uuid: str | None = Field(default=None, max_length=26, description="Request Uuid")
    created_timestamp: datetime.datetime = Field(description="Created Timestamp")

    def sanitize(self) -> MonetaryAdjustmentMutation:
        """Return a sanitized copy of this MonetaryAdjustmentMutation instance."""
        return MonetaryAdjustmentMutation(
            id=self.id,
            mutation_action=self.mutation_action,
            mutation_timestamp=self.mutation_timestamp,
            monetary_adjustment_id=self.monetary_adjustment_id,
            uuid=sanitize_uuid_field(self.uuid, 26),  # type: ignore
            billing_entity_uuid=sanitize_uuid_field(self.billing_entity_uuid, 26),  # type: ignore
            adjust_fee_summary_uuid=sanitize_uuid_field(self.adjust_fee_summary_uuid, 26),  # type: ignore
            qualified_fee_summary_uuid=sanitize_uuid_field(self.qualified_fee_summary_uuid, 26),  # type: ignore
            rule_uuid=sanitize_uuid_field(self.rule_uuid, 26),  # type: ignore
            rule_criteria_uuid=sanitize_uuid_field(self.rule_criteria_uuid, 26),
            rule_type=self.rule_type,
            request_uuid=sanitize_uuid_field(self.request_uuid, 26),
            created_timestamp=self.created_timestamp,
        )
