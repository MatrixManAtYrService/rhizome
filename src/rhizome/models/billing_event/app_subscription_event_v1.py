"""
SQLModel definition for the app_subscription_event table, version 1.

This module provides the V1 implementation of the AppSubscriptionEvent model.
Currently, AppSubscriptionEventV1 is identical to the base AppSubscriptionEvent class (name-only inheritance),
but as the table schema evolves across environments, future versions (V2, V3, etc.) will
contain actual schema differences (new columns, modified types, etc.).
"""

from __future__ import annotations

from .app_subscription_event import AppSubscriptionEvent


class AppSubscriptionEventV1(AppSubscriptionEvent, table=True):
    """
    Version 1 of the AppSubscriptionEvent model.

    Currently a name-only inheritance from the base AppSubscriptionEvent class.
    As schema changes are introduced in different environments, subsequent
    versions (V2, V3, etc.) will not be so trivial and will contain
    actual field modifications, additions, or removals.
    """

    __tablename__ = "app_subscription_event"  # type: ignore
