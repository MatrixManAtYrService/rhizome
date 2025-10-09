"""
SQLModel definition for the app_meter_action_fee_code table, version 1.

This module provides the V1 implementation of the AppMeterActionFeeCode model.
"""

from __future__ import annotations

from .app_meter_action_fee_code import AppMeterActionFeeCode


class AppMeterActionFeeCodeV1(AppMeterActionFeeCode, table=True):
    """
    Version 1 of the AppMeterActionFeeCode model.

    Currently a name-only inheritance from the base AppMeterActionFeeCode class.
    """

    __tablename__ = "app_meter_action_fee_code"  # type: ignore
