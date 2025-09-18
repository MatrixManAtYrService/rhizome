"""
Expected data for jobrunr_backgroundjobservers table in dev environment.
"""

from __future__ import annotations

from rhizome.models.base import Emplacement
from rhizome.models.billing_event.jobrunr_backgroundjobservers_v1 import JobrunrBackgroundjobserversV1


class JobrunrBackgroundjobserversDev(Emplacement[JobrunrBackgroundjobserversV1]):
    """Expected data for JobrunrBackgroundjobservers in dev environment."""

    @classmethod
    def get_expected(cls) -> JobrunrBackgroundjobserversV1:
        """Get expected jobrunr backgroundjobservers data for dev environment."""
        raise NotImplementedError(
            f"Expected data for {cls.__name__} not yet implemented. "
            f"Please add test data based on real data from this environment."
        )