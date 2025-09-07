"""
Expected data for fee_summary table in dev environment.
"""

from __future__ import annotations

import datetime
from decimal import Decimal

from rhizome.models.base import Emplacement
from rhizome.models.billing_bookkeeper.fee_summary_v1 import FeeSummaryV1


class FeeSummaryDev(Emplacement[FeeSummaryV1]):
    """Expected data for FeeSummary in dev environment."""

    @classmethod
    def get_expected(cls) -> FeeSummaryV1:
        """Get expected fee summary data for dev environment."""
        return FeeSummaryV1(
            id=30,
            uuid="HashDwRegsuuYDX9RnVzfZport",
            billing_entity_uuid="HashHvx2teX4epSXNfDrrx956N",
            billing_date=datetime.date(2024, 1, 1),
            fee_category="PLAN_RETAIL",
            fee_code="PaymentsPDVT",
            currency="GBP",
            total_period_units=Decimal("3.00"),
            abs_period_units=Decimal("3.00"),
            total_basis_amount=Decimal("0.00"),
            abs_basis_amount=Decimal("0.00"),
            total_fee_amount=Decimal("0.00"),
            fee_rate_uuid="Hash2BtY3zBxDEJzfEUGDRvSLQ",
            request_uuid="HashFZB5xUQ3fZK3Cq5CULKogo",
            invoice_info_uuid=None,
            fee_code_ledger_account_uuid=None,
            credit_ledger_account_uuid=None,
            debit_ledger_account_uuid=None,
            exclude_from_invoice=0,
            created_timestamp=datetime.datetime(2023, 10, 18, 11, 23, 57, 951306),
            modified_timestamp=datetime.datetime(2025, 4, 16, 13, 6, 42, 76246),
        )