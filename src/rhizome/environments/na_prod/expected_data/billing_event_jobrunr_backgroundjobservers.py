"""
Expected data for jobrunr_backgroundjobservers table in na_prod environment.
"""

from __future__ import annotations

from rhizome.models.base import Emplacement
from rhizome.models.billing_event.jobrunr_backgroundjobservers_v1 import JobrunrBackgroundjobserversV1


class JobrunrBackgroundjobserversNaProd(Emplacement[JobrunrBackgroundjobserversV1]):
    """Expected data for JobrunrBackgroundjobservers in na_prod environment."""

    @classmethod
    def get_expected(cls) -> JobrunrBackgroundjobserversV1:
        """Get expected jobrunr backgroundjobservers data for na_prod environment."""
        raise NotImplementedError(
            f"Expected data for {cls.__name__} not yet implemented. "
            f"Please add test data based on real data from this environment."
        )