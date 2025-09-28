"""
SQLModel definition for the plan_authorization_settings table, version 1.

This module provides the V1 implementation of the PlanAuthorizationSettings model.
Currently, PlanAuthorizationSettingsV1 is identical to the base PlanAuthorizationSettings class (name-only inheritance),
but as the table schema evolves across environments, future versions (V2, V3, etc.) will
contain actual schema differences (new columns, modified types, etc.).
"""

from __future__ import annotations

from ..metadata_registry import NaProdSQLModel
from .plan_authorization_settings import PlanAuthorizationSettings


class PlanAuthorizationSettingsV1(PlanAuthorizationSettings, NaProdSQLModel, table=True):
    """
    Version 1 of the PlanAuthorizationSettings model.

    Currently a name-only inheritance from the base PlanAuthorizationSettings class.
    As schema changes are introduced in different environments, subsequent
    versions (V2, V3, etc.) will not be so trivial and will contain
    actual field modifications, additions, or removals.
    """

    __tablename__ = "plan_authorization_settings"  # type: ignore
