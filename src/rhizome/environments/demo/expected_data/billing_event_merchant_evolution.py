"""
Expected data for merchant_evolution table in demo environment.
"""

from __future__ import annotations

from rhizome.models.base import Emplacement
from rhizome.models.billing_event.merchant_evolution_v1 import MerchantEvolutionV1


class MerchantEvolutionDemo(Emplacement[MerchantEvolutionV1]):
    """Expected data for MerchantEvolution in demo environment."""

    @classmethod
    def get_expected(cls) -> MerchantEvolutionV1:
        """Get expected merchant_evolution data for demo environment."""
        raise NotImplementedError(
            f"Expected data for {cls.__name__} not yet implemented. "
            f"Please add test data based on real data from this environment."
        )
