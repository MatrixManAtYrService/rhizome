"""
Expected data for jobrunr_backgroundjobservers table in demo environment.
"""

from __future__ import annotations

from rhizome.models.base import Emplacement
from rhizome.models.billing_event.jobrunr_backgroundjobservers_v1 import JobrunrBackgroundjobserversV1


class JobrunrBackgroundjobserversDemo(Emplacement[JobrunrBackgroundjobserversV1]):
    """Expected data for JobrunrBackgroundjobservers in demo environment."""

    @classmethod
    def get_expected(cls) -> JobrunrBackgroundjobserversV1:
        """Get expected jobrunr backgroundjobservers data for demo environment."""
        raise NotImplementedError(
            f"Expected data for {cls.__name__} not yet implemented. "
            f"Please add test data based on real data from this environment."
        )