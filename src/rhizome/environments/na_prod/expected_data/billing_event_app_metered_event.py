"""
Expected data for app_metered_event table in na_prod environment.
"""

from __future__ import annotations

import datetime

from rhizome.models.base import Emplacement
from rhizome.models.billing_event.app_metered_event_v1 import AppMeteredEventV1


class AppMeteredEventNaProd(Emplacement[AppMeteredEventV1]):
    """Expected data for AppMeteredEvent in na_prod environment."""

    @classmethod
    def get_expected(cls) -> AppMeteredEventV1:
        """Get expected app metered event data for na_prod environment."""
        return AppMeteredEventV1(
            id=883,
            uuid="Hash9V77timzh69Cy55VSsAXFV",
            merchant_uuid="HashFmpNZhreq",
            developer_app_uuid="HashFv1WBub7L",
            environment="usprod",
            app_metered_uuid="Hash21BKibhdo",
            count=1,
            basis_amount=None,
            basis_currency=None,
            action_timestamp=datetime.datetime(2025, 3, 1, 0, 0, 0),
            credit_for_trial=0,
            cos_event_uuid="HashEPRtjibFj8CaujQBHauc15",
            processed_timestamp=datetime.datetime(2025, 3, 6, 15, 30, 39, 97506),
            billing_event_uuid="HashBDe5zJnGpuZJ8HqUyjYpmM",
            created_timestamp=datetime.datetime(2025, 3, 3, 16, 3, 28, 240163),
        )