"""
Expected data for app_metered_event table in demo environment.
"""

from __future__ import annotations

import datetime

from rhizome.models.base import Emplacement
from rhizome.models.billing_event.app_metered_event_v1 import AppMeteredEventV1


class AppMeteredEventDemo(Emplacement[AppMeteredEventV1]):
    """Expected data for AppMeteredEvent in demo environment."""

    @classmethod
    def get_expected(cls) -> AppMeteredEventV1:
        """Get expected app metered event data for demo environment."""
        return AppMeteredEventV1(
            id=1,
            uuid="HashHFsoa39Za8PAEn1rYUP7si",
            merchant_uuid="HashEzEYnSWUd",
            developer_app_uuid="Hash64P7p23ti",
            environment="dev::demo2",
            app_metered_uuid="HashAhHuBDAhM",
            count=1,
            basis_amount=None,
            basis_currency=None,
            action_timestamp=datetime.datetime(2024, 4, 29, 0, 0, 0),
            credit_for_trial=1,
            cos_event_uuid="HashFVNjufXJW5qoKCLzRftnr2",
            processed_timestamp=datetime.datetime(2024, 4, 30, 9, 25, 13, 646129),
            billing_event_uuid="HashG46KY3m1y88wg3pc19YuCL",
            created_timestamp=datetime.datetime(2024, 4, 30, 9, 24, 44, 236856),
        )