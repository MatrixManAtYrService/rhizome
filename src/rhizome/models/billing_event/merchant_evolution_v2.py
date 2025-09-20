"""SQLModel V2 definition for the merchant_evolution table.

This module provides the V2 SQLModel class for the merchant_evolution table from the
billing-event database. V2 is used in dev/demo environments that include the
billable_merchant_type field.
"""

from __future__ import annotations

from sqlmodel import Field

from ...sanitize_helpers import sanitize_uuid_field
from ..metadata_registry import DevDemoSQLModel
from .merchant_evolution import MerchantEvolution


class MerchantEvolutionV2(MerchantEvolution, DevDemoSQLModel, table=True):
    """V2 for dev/demo - includes billable_merchant_type field."""

    __tablename__ = "merchant_evolution"  # type: ignore

    # Additional field in V2
    billable_merchant_type: str | None = Field(default=None, max_length=25, description="Type of billable merchant")

    def sanitize(self) -> MerchantEvolutionV2:
        """Return a sanitized copy of this MerchantEvolution instance."""
        return MerchantEvolutionV2(
            id=self.id,
            merchant_uuid=sanitize_uuid_field(self.merchant_uuid, 13),  # type: ignore
            reseller_uuid=sanitize_uuid_field(self.reseller_uuid, 13),  # type: ignore
            merchant_name=self.merchant_name,
            seasonal=self.seasonal,
            tax_exempt=self.tax_exempt,
            mlc_merchant_created_event_datetime=self.mlc_merchant_created_event_datetime,
            mlc_merchant_created_event_uuid=sanitize_uuid_field(self.mlc_merchant_created_event_uuid, 13),
            created_in_bookkeeper_datetime=self.created_in_bookkeeper_datetime,
            terms_accepted_datetime=self.terms_accepted_datetime,
            agreement_event_uuid=sanitize_uuid_field(self.agreement_event_uuid, 26),
            close_date=self.close_date,
            effective_close_date=self.effective_close_date,
            mlc_close_event_uuid=sanitize_uuid_field(self.mlc_close_event_uuid, 13),
            created_timestamp=self.created_timestamp,
            modified_timestamp=self.modified_timestamp,
            billable_merchant_type=self.billable_merchant_type,
        )
