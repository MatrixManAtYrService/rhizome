"""
Expected data for jobrunr_metadata table in demo environment.
"""

from __future__ import annotations

from rhizome.models.base import Emplacement
from rhizome.models.billing_event.jobrunr_metadata_v1 import JobrunrMetadataV1


class JobrunrMetadataDemo(Emplacement[JobrunrMetadataV1]):
    """Expected data for JobrunrMetadata in demo environment."""

    @classmethod
    def get_expected(cls) -> JobrunrMetadataV1:
        """Get expected jobrunr metadata data for demo environment."""
        raise NotImplementedError(
            f"Expected data for {cls.__name__} not yet implemented. "
            f"Please add test data based on real data from this environment."
        )