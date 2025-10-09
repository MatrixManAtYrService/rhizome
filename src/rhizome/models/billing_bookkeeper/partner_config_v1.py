"""
SQLModel definition for the partner_config table, version 1.

This module provides the V1 implementation of the PartnerConfig model.
"""

from __future__ import annotations

from .partner_config import PartnerConfig


class PartnerConfigV1(PartnerConfig, table=True):
    """
    Version 1 of the PartnerConfig model.

    Currently a name-only inheritance from the base PartnerConfig class.
    """

    __tablename__ = "partner_config"  # type: ignore
