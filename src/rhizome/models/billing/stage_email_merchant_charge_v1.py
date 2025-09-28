"""
SQLModel definition for the stage_email_merchant_charge table, version 1.

This module provides the V1 implementation of the StageEmailMerchantCharge model.
Currently, StageEmailMerchantChargeV1 is identical to the base StageEmailMerchantCharge class (name-only inheritance),
but as the table schema evolves across environments, future versions (V2, V3, etc.) will
contain actual schema differences (new columns, modified types, etc.).
"""

from __future__ import annotations

from ..metadata_registry import NaProdSQLModel
from .stage_email_merchant_charge import StageEmailMerchantCharge


class StageEmailMerchantChargeV1(StageEmailMerchantCharge, NaProdSQLModel, table=True):
    """
    Version 1 of the StageEmailMerchantCharge model.

    Currently a name-only inheritance from the base StageEmailMerchantCharge class.
    As schema changes are introduced in different environments, subsequent
    versions (V2, V3, etc.) will not be so trivial and will contain
    actual field modifications, additions, or removals.
    """

    __tablename__ = "stage_email_merchant_charge"  # type: ignore
