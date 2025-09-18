"""
Expected data for plan_meta table in demo environment.
"""

from __future__ import annotations

from rhizome.models.base import Emplacement
from rhizome.models.billing_event.plan_meta_v1 import PlanMetaV1


class PlanMetaDemo(Emplacement[PlanMetaV1]):
    """Expected data for PlanMeta in demo environment."""

    @classmethod
    def get_expected(cls) -> PlanMetaV1:
        """Get expected plan_meta data for demo environment."""
        raise NotImplementedError(
            f"Expected data for {cls.__name__} not yet implemented. "
            f"Please add test data based on real data from this environment."
        )
