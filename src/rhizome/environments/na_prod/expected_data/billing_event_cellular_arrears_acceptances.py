"""
Expected data for cellular_arrears_acceptances table in na_prod environment.
"""

from __future__ import annotations

from rhizome.models.base import Emplacement
from rhizome.models.billing_event.cellular_arrears_acceptances_v1 import CellularArrearsAcceptancesV1


class CellularArrearsAcceptancesNaProd(Emplacement[CellularArrearsAcceptancesV1]):
    """Expected data for CellularArrearsAcceptances in na_prod environment."""

    @classmethod
    def get_expected(cls) -> CellularArrearsAcceptancesV1:
        """Get expected cellular arrears acceptances data for na_prod environment."""
        raise NotImplementedError(
            f"Expected data for {cls.__name__} not yet implemented. "
            f"Please add test data based on real data from this environment."
        )