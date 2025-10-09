"""
SQLModel definition for the plan_action_type table, version 1.

This module provides the V1 implementation of the PlanActionType model.
"""

from __future__ import annotations

from .plan_action_type import PlanActionType


class PlanActionTypeV1(PlanActionType, table=True):
    """
    Version 1 of the PlanActionType model.

    Currently a name-only inheritance from the base PlanActionType class.
    """

    __tablename__ = "plan_action_type"  # type: ignore
