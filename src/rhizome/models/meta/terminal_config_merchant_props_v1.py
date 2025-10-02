"""
SQLModel definition for the terminal_config_merchant_props table, version 1.

This module provides the V1 implementation of the TerminalConfigMerchantProps model.
Currently, TerminalConfigMerchantPropsV1 is identical to the base TerminalConfigMerchantProps class (name-only inheritance),
but as the table schema evolves across environments, future versions (V2, V3, etc.) will
contain actual schema differences (new columns, modified types, etc.).
"""

from __future__ import annotations

from ...sanitize_helpers import sanitize_uuid_field
from ..metadata_registry import MetaSQLModel
from .terminal_config_merchant_props import TerminalConfigMerchantProps


class TerminalConfigMerchantPropsV1(TerminalConfigMerchantProps, MetaSQLModel, table=True):
    """
    Version 1 of the TerminalConfigMerchantProps model.

    Currently a name-only inheritance from the base TerminalConfigMerchantProps class.
    As schema changes are introduced in different environments, subsequent
    versions (V2, V3, etc.) will not be so trivial and will contain
    actual field modifications, additions, or removals.
    """

    __tablename__ = "terminal_config_merchant_props"  # type: ignore

    def sanitize(self) -> TerminalConfigMerchantPropsV1:
        """Return a sanitized copy of this TerminalConfigMerchantPropsV1 instance."""
        return TerminalConfigMerchantPropsV1(
            id=self.id,
            uuid=sanitize_uuid_field(self.uuid, 13),  # type: ignore
            country=self.country,
            currency=self.currency,
        )