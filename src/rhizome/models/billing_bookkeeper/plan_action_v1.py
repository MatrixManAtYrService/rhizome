"""
SQLModel definition for the plan_action table, version 1.

This module provides the V1 implementation of the PlanAction model.
"""

from __future__ import annotations

from .plan_action import PlanAction


class PlanActionV1(PlanAction, table=True):
    """
    Version 1 of the PlanAction model.

    Currently a name-only inheritance from the base PlanAction class.
    """

    __tablename__ = "plan_action"  # type: ignore
