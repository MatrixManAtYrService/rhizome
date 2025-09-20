"""
SQLModel definition for the app_subscription_daily table, version 1.

This module provides the V1 implementation of the AppSubscriptionDaily model.
Currently, AppSubscriptionDailyV1 is identical to the base AppSubscriptionDaily class (name-only inheritance),
but as the table schema evolves across environments, future versions (V2, V3, etc.) will
contain actual schema differences (new columns, modified types, etc.).
"""

from __future__ import annotations

from .app_subscription_daily import AppSubscriptionDaily


class AppSubscriptionDailyV1(AppSubscriptionDaily, table=True):
    """
    Version 1 of the AppSubscriptionDaily model.

    Currently a name-only inheritance from the base AppSubscriptionDaily class.
    As schema changes are introduced in different environments, subsequent
    versions (V2, V3, etc.) will not be so trivial and will contain
    actual field modifications, additions, or removals.
    """

    __tablename__ = "app_subscription_daily"  # type: ignore
