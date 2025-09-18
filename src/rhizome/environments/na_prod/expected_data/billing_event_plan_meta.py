"""
Expected data for plan_meta table in na_prod environment.
"""

from __future__ import annotations

from rhizome.models.base import Emplacement
from rhizome.models.billing_event.plan_meta_v1 import PlanMetaV1


class PlanMetaNaProd(Emplacement[PlanMetaV1]):
    """Expected data for PlanMeta in na_prod environment."""

    @classmethod
    def get_expected(cls) -> PlanMetaV1:
        """Get expected plan_meta data for na_prod environment."""
        raise NotImplementedError(
            f"Expected data for {cls.__name__} not yet implemented. "
            f"Please add test data based on real data from this environment."
        )
