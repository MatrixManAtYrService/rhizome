"""
Expected data for job_assassination_contract table in na_prod environment.
"""

from __future__ import annotations

from rhizome.models.base import Emplacement
from rhizome.models.billing_event.job_assassination_contract_v1 import JobAssassinationContractV1


class JobAssassinationContractNaProd(Emplacement[JobAssassinationContractV1]):
    """Expected data for JobAssassinationContract in na_prod environment."""

    @classmethod
    def get_expected(cls) -> JobAssassinationContractV1:
        """Get expected job assassination contract data for na_prod environment."""
        raise NotImplementedError(
            f"Expected data for {cls.__name__} not yet implemented. "
            f"Please add test data based on real data from this environment."
        )