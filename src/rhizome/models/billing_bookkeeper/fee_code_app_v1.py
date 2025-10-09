"""
SQLModel definition for the fee_code_app table, version 1.

This module provides the V1 implementation of the FeeCodeApp model.
"""

from __future__ import annotations

from .fee_code_app import FeeCodeApp


class FeeCodeAppV1(FeeCodeApp, table=True):
    """
    Version 1 of the FeeCodeApp model.

    Currently a name-only inheritance from the base FeeCodeApp class.
    """

    __tablename__ = "fee_code_app"  # type: ignore
