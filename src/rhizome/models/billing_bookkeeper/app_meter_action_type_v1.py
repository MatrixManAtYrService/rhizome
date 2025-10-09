"""
SQLModel definition for the app_meter_action_type table, version 1.

This module provides the V1 implementation of the AppMeterActionType model.
"""

from __future__ import annotations

from .app_meter_action_type import AppMeterActionType


class AppMeterActionTypeV1(AppMeterActionType, table=True):
    """
    Version 1 of the AppMeterActionType model.

    Currently a name-only inheritance from the base AppMeterActionType class.
    """

    __tablename__ = "app_meter_action_type"  # type: ignore
