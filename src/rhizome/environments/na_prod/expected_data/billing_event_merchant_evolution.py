"""
Expected data for merchant_evolution table in na_prod environment.
"""

from __future__ import annotations

from rhizome.models.base import Emplacement
from rhizome.models.billing_event.merchant_evolution_v1 import MerchantEvolutionV1


class MerchantEvolutionNaProd(Emplacement[MerchantEvolutionV1]):
    """Expected data for MerchantEvolution in na_prod environment."""

    @classmethod
    def get_expected(cls) -> MerchantEvolutionV1:
        """Get expected merchant_evolution data for na_prod environment."""
        raise NotImplementedError(
            f"Expected data for {cls.__name__} not yet implemented. "
            f"Please add test data based on real data from this environment."
        )
