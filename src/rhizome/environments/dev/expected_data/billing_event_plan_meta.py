"""
Expected data for plan_meta table in dev environment.
"""

from __future__ import annotations

from rhizome.models.base import Emplacement
from rhizome.models.billing_event.plan_meta_v1 import PlanMetaV1


class PlanMetaDev(Emplacement[PlanMetaV1]):
    """Expected data for PlanMeta in dev environment."""

    @classmethod
    def get_expected(cls) -> PlanMetaV1:
        """Get expected plan_meta data for dev environment."""
        raise NotImplementedError(
            f"Expected data for {cls.__name__} not yet implemented. "
            f"Please add test data based on real data from this environment."
        )
