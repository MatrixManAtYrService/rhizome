"""
Expected data for jobrunr_metadata table in na_prod environment.
"""

from __future__ import annotations

from rhizome.models.base import Emplacement
from rhizome.models.billing_event.jobrunr_metadata_v1 import JobrunrMetadataV1


class JobrunrMetadataNaProd(Emplacement[JobrunrMetadataV1]):
    """Expected data for JobrunrMetadata in na_prod environment."""

    @classmethod
    def get_expected(cls) -> JobrunrMetadataV1:
        """Get expected jobrunr metadata data for na_prod environment."""
        raise NotImplementedError(
            f"Expected data for {cls.__name__} not yet implemented. "
            f"Please add test data based on real data from this environment."
        )