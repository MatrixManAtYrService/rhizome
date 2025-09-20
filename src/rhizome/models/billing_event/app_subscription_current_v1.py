"""
SQLModel definition for the app_subscription_current table, version 1.

This module provides the V1 implementation of the AppSubscriptionCurrent model.
Currently, AppSubscriptionCurrentV1 is identical to the base AppSubscriptionCurrent class (name-only inheritance),
but as the table schema evolves across environments, future versions (V2, V3, etc.) will
contain actual schema differences (new columns, modified types, etc.).
"""

from __future__ import annotations

from .app_subscription_current import AppSubscriptionCurrent


class AppSubscriptionCurrentV1(AppSubscriptionCurrent, table=True):
    """
    Version 1 of the AppSubscriptionCurrent model.

    Currently a name-only inheritance from the base AppSubscriptionCurrent class.
    As schema changes are introduced in different environments, subsequent
    versions (V2, V3, etc.) will not be so trivial and will contain
    actual field modifications, additions, or removals.
    """

    __tablename__ = "app_subscription_current"  # type: ignore
