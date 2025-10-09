"""
SQLModel definition for the app_meter_action table, version 1.

This module provides the V1 implementation of the AppMeterAction model.
"""

from __future__ import annotations

from .app_meter_action import AppMeterAction


class AppMeterActionV1(AppMeterAction, table=True):
    """
    Version 1 of the AppMeterAction model.

    Currently a name-only inheritance from the base AppMeterAction class.
    """

    __tablename__ = "app_meter_action"  # type: ignore
