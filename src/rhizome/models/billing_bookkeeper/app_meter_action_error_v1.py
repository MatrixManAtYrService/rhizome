"""
SQLModel definition for the app_meter_action_error table, version 1.

This module provides the V1 implementation of the AppMeterActionError model.
"""

from __future__ import annotations

from .app_meter_action_error import AppMeterActionError


class AppMeterActionErrorV1(AppMeterActionError, table=True):
    """
    Version 1 of the AppMeterActionError model.

    Currently a name-only inheritance from the base AppMeterActionError class.
    """

    __tablename__ = "app_meter_action_error"  # type: ignore
