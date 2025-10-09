"""
SQLModel definition for the plan_action_error table, version 1.

This module provides the V1 implementation of the PlanActionError model.
"""

from __future__ import annotations

from .plan_action_error import PlanActionError


class PlanActionErrorV1(PlanActionError, table=True):
    """
    Version 1 of the PlanActionError model.

    Currently a name-only inheritance from the base PlanActionError class.
    """

    __tablename__ = "plan_action_error"  # type: ignore
