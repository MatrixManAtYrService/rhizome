"""
Expected data for fee_summary table in na_prod environment.
"""

from __future__ import annotations

import datetime
from decimal import Decimal

from rhizome.models.base import Emplacement
from rhizome.models.billing_bookkeeper.fee_summary_v1 import FeeSummaryV1


class FeeSummaryNaProd(Emplacement[FeeSummaryV1]):
    """Expected data for FeeSummary in na_prod environment."""

    @classmethod
    def get_expected(cls) -> FeeSummaryV1:
        """Get expected fee summary data for na_prod environment."""
        return FeeSummaryV1(
            id=74347,
            uuid="JW8H2B9BT6B11R2HHXY3HYQCN6",
            billing_entity_uuid="MERCHANT_UUID_EXAMPLE_123456",
            billing_date=datetime.date(2025, 1, 15),
            fee_category="APP_SUB_3P_RETAIL",
            fee_code="MW63DAWPN6JGY.S",
            currency="USD",
            total_period_units=Decimal("1.0000"),
            abs_period_units=Decimal("1.0000"),
            total_basis_amount=Decimal("9.990"),
            abs_basis_amount=Decimal("9.990"),
            total_fee_amount=Decimal("9.990"),
            fee_rate_uuid="FEE_RATE_UUID_EXAMPLE_789",
            request_uuid="REQUEST_UUID_EXAMPLE_456",
            invoice_info_uuid=None,
            fee_code_ledger_account_uuid=None,
            credit_ledger_account_uuid=None,
            debit_ledger_account_uuid=None,
            exclude_from_invoice=0,
            created_timestamp=datetime.datetime(2025, 1, 15, 10, 30, 0),
            modified_timestamp=datetime.datetime(2025, 1, 15, 10, 30, 0),
        )