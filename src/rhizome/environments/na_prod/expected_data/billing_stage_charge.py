"""
Expected data for stage_charge table in na_prod environment.
"""

from __future__ import annotations

import datetime

from rhizome.models.base import Emplacement
from rhizome.models.billing.stage_charge_v1 import StageChargeV1


class StageChargeNaProd(Emplacement[StageChargeV1]):
    """Expected data for StageCharge in na_prod environment."""

    @classmethod
    def get_expected(cls) -> StageChargeV1:
        """Get expected stage charge data for na_prod environment."""
        return StageChargeV1(
            id=1,
            uuid="S9GBXXVC8P72J",
            merchant_id=210342,
            currency="USD",
            amount=429,
            tax=None,
            developer_portion=None,
            status="REFUND_DOWNGRADE_PENDING",
            developer_status=None,
            status_owner="AppBillingController",
            type="PRORATED_SUBSCRIPTION",
            tax_classification_code=None,
            start_date=datetime.datetime(2018, 2, 20, 20, 49, 9),
            end_date=datetime.datetime(2018, 3, 1, 0, 0, 0),
            created_time=datetime.datetime(2018, 2, 21, 21, 14, 23),
            modified_time=datetime.datetime(2018, 2, 21, 21, 14, 23),
            export_month=None,
            status_modified_time=None,
            request_uuid="DKTJC5HM7PD5R",
            promoted_time=None,
            promoted_id=None,
            parent_id=None,
        )