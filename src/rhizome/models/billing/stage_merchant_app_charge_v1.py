"""
SQLModel definition for the stage_merchant_app_charge table, version 1.

This module provides the V1 implementation of the StageMerchantAppCharge model.
Currently, StageMerchantAppChargeV1 is identical to the base StageMerchantAppCharge class (name-only inheritance),
but as the table schema evolves across environments, future versions (V2, V3, etc.) will
contain actual schema differences (new columns, modified types, etc.).
"""

from __future__ import annotations

from ..metadata_registry import NaProdSQLModel
from .stage_merchant_app_charge import StageMerchantAppCharge


class StageMerchantAppChargeV1(StageMerchantAppCharge, NaProdSQLModel, table=True):
    """
    Version 1 of the StageMerchantAppCharge model.

    Currently a name-only inheritance from the base StageMerchantAppCharge class.
    As schema changes are introduced in different environments, subsequent
    versions (V2, V3, etc.) will not be so trivial and will contain
    actual field modifications, additions, or removals.
    """

    __tablename__ = "stage_merchant_app_charge"  # type: ignore
